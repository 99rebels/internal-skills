#!/usr/bin/env python3
"""
trends.py — Compute growth metrics from daily.json.

Reads data/daily.json (append-only compact entries) and produces
data/trends.json with per-skill/repo growth metrics across configurable
time windows.

Usage:
    python3 trends.py [--daily FILE] [--output FILE] [--windows 7,30,90]
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone, timedelta


def load_json(path):
    with open(path) as f:
        return json.load(f)


def find_entry_for_window(daily, target_date, window_days):
    """Find the entry closest to (target_date - window_days).

    Returns the entry dict and the number of days between it and target_date.
    """
    cutoff = target_date - timedelta(days=window_days)

    best = None
    best_dt = None
    best_diff = None

    for entry in daily:
        date_str = entry.get("date", "")
        try:
            entry_dt = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            continue

        # Must be at or before the cutoff date
        if entry_dt > cutoff:
            continue

        diff = (target_date - entry_dt).days
        if best is None or diff < best_diff:
            best = entry
            best_dt = entry_dt
            best_diff = diff

    return best, best_diff


def compute_skill_metrics(current_data, ref_data, days):
    """Compute growth metrics for a single skill/repo dict."""
    if not ref_data or not days or days < 1:
        return None

    result = {}
    for key, curr_val in current_data.items():
        ref_val = ref_data.get(key, 0)
        change = curr_val - ref_val
        pct = None
        if ref_val > 0:
            pct = round((change / ref_val) * 100, 1)
        elif change > 0:
            pct = None  # Can't compute percentage from zero, but there was growth

        metric_key = key.lower()
        if metric_key == "dl" or metric_key == "downloads":
            result["dlChange"] = change
            result["dlPct"] = pct
            result["avgDailyDl"] = round(change / days, 1) if days > 0 else None
        elif metric_key == "stars":
            result["starsChange"] = change
        elif metric_key == "forks":
            result["forksChange"] = change
            if ref_val > 0:
                result["forksPct"] = pct

    # For github repos: add avgDailyStars
    if "starsChange" in result and days > 0:
        result["avgDailyStars"] = round(result["starsChange"] / days, 1)

    # For github repos: add starsPct
    if "starsChange" in result and "starsPct" not in result:
        stars_val = current_data.get("stars", 0)
        ref_stars = ref_data.get("stars", 0) if ref_data else 0
        if ref_stars > 0:
            result["starsPct"] = round(((stars_val - ref_stars) / ref_stars) * 100, 1)

    return result if result else None


def compute_github_repo_metrics(current_repo, ref_repo, days):
    """Compute growth metrics for a GitHub repo entry."""
    if not ref_repo or not days or days < 1:
        return None

    result = {}
    for metric in ["stars", "forks", "openIssues"]:
        curr = current_repo.get(metric, 0)
        prev = ref_repo.get(metric, 0)
        change = curr - prev
        if change != 0 or metric == "stars":  # Always include stars
            key = metric
            if metric == "stars":
                result[f"starsChange"] = change
                if prev > 0:
                    result["starsPct"] = round((change / prev) * 100, 1)
                result["avgDailyStars"] = round(change / days, 1) if days > 0 else None
            elif metric == "forks":
                result["forksChange"] = change
                if prev > 0:
                    result["forksPct"] = round((change / prev) * 100, 1)
            elif metric == "openIssues":
                result["openIssuesChange"] = change

    return result if result else None


def compute_agensi_window(daily, latest_entry, window_days):
    """Compute Agensi growth for a window."""
    latest_date = datetime.strptime(latest_entry["date"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    ref_entry, days = find_entry_for_window(daily, latest_date, window_days)

    if not ref_entry or days < 1:
        return None

    latest_ag = latest_entry.get("agensi", {})
    ref_ag = ref_entry.get("agensi", {})

    latest_slugs = set(latest_ag.get("skillSlugs", []))
    ref_slugs = set(ref_ag.get("skillSlugs", []))
    new_slugs = sorted(latest_slugs - ref_slugs)

    total_change = latest_ag.get("totalSkills", 0) - ref_ag.get("totalSkills", 0)

    return {
        "newCount": len(new_slugs),
        "newSlugs": new_slugs,
        "totalChange": total_change,
        "daysSpan": days,
    }


def main():
    parser = argparse.ArgumentParser(description="Compute growth metrics from daily.json")
    parser.add_argument("--daily", default=None, help="Path to daily.json")
    parser.add_argument("--output", default=None, help="Path to write trends.json")
    parser.add_argument("--windows", default="7,30,90", help="Comma-separated window sizes in days")
    args = parser.parse_args()

    # Resolve paths
    if not args.daily:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        args.daily = os.path.join(script_dir, "..", "data", "daily.json")
    if not args.output:
        args.output = os.path.join(os.path.dirname(os.path.abspath(args.daily)), "trends.json")

    windows = [int(w.strip()) for w in args.windows.split(",")]

    # Load daily data
    daily = load_json(args.daily)
    if not daily:
        print("No entries in daily.json. Nothing to compute.", file=sys.stderr)
        with open(args.output, "w") as f:
            json.dump({"error": "no data", "windows": windows}, f, indent=2)
        return

    latest = daily[-1]
    latest_date_str = latest.get("date", "")
    latest_dt = datetime.strptime(latest_date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    first_date_str = daily[0].get("date", "")

    now = datetime.now(timezone.utc)
    generated_at = now.isoformat()

    trends = {
        "lastUpdated": latest_date_str,
        "generatedAt": generated_at,
        "dataPoints": len(daily),
        "dateRange": f"{first_date_str} to {latest_date_str}",
        "windows": windows,
    }

    # Your skills
    your_skills = latest.get("clawhub", {}).get("yours", {})
    if your_skills:
        trends["yourSkills"] = {}
        for slug, current in your_skills.items():
            skill_trend = {"current": current}
            for w in windows:
                ref_entry, days = find_entry_for_window(daily, latest_dt, w)
                if not ref_entry or days < 1:
                    skill_trend[f"{w}d"] = None
                    continue
                ref_data = ref_entry.get("clawhub", {}).get("yours", {}).get(slug)
                if not ref_data:
                    skill_trend[f"{w}d"] = None
                    continue
                metrics = compute_skill_metrics(current, ref_data, days)
                skill_trend[f"{w}d"] = metrics
            trends["yourSkills"][slug] = skill_trend

    # Tracked skills
    tracked_skills = latest.get("clawhub", {}).get("tracked", {})
    if tracked_skills:
        trends["trackedSkills"] = {}
        for slug, current in tracked_skills.items():
            skill_trend = {"current": current}
            for w in windows:
                ref_entry, days = find_entry_for_window(daily, latest_dt, w)
                if not ref_entry or days < 1:
                    skill_trend[f"{w}d"] = None
                    continue
                ref_data = ref_entry.get("clawhub", {}).get("tracked", {}).get(slug)
                if not ref_data:
                    skill_trend[f"{w}d"] = None
                    continue
                metrics = compute_skill_metrics(current, ref_data, days)
                skill_trend[f"{w}d"] = metrics
            trends["trackedSkills"][slug] = skill_trend

    # Agensi
    if latest.get("agensi"):
        agensi_trend = {"current": {"totalSkills": latest["agensi"].get("totalSkills", 0)}}
        for w in windows:
            result = compute_agensi_window(daily, latest, w)
            agensi_trend[f"{w}d"] = result
        trends["agensi"] = agensi_trend

    # GitHub repos
    github_repos = latest.get("github", {})
    if github_repos:
        trends["github"] = {}
        for label, repo in github_repos.items():
            gh_trend = {"current": {"stars": repo.get("stars", 0), "forks": repo.get("forks", 0)}}
            for w in windows:
                ref_entry, days = find_entry_for_window(daily, latest_dt, w)
                if not ref_entry or days < 1:
                    gh_trend[f"{w}d"] = None
                    continue
                ref_repo = ref_entry.get("github", {}).get(label)
                if not ref_repo:
                    gh_trend[f"{w}d"] = None
                    continue
                metrics = compute_github_repo_metrics(repo, ref_repo, days)
                gh_trend[f"{w}d"] = metrics
            trends["github"][label] = gh_trend

    # Write output
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(trends, f, indent=2)

    print(f"Trends written: {len(daily)} data points, windows={windows} → {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
