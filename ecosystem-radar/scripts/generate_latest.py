#!/usr/bin/env python3
"""
generate_latest.py — Build compact summary + change detection from raw data.

Compares current against previous latest.json to find deltas.
Usage: python3 generate_latest.py --raw FILE --watch FILE [--prev FILE] [--output FILE]
"""

import json
import sys
import os
from datetime import datetime, timezone, timedelta


def load_json(path):
    with open(path) as f:
        return json.load(f)


def build_summary(raw, watch):
    platforms = raw.get("platforms", {})
    summary = {
        "timestamp": raw.get("timestamp", datetime.now(timezone.utc).isoformat()),
        "platforms": {},
        "paymentStatus": {},
        "alerts": [],
    }

    # ClawHub
    ch = platforms.get("clawhub", {})
    if ch.get("trackedSkills") or ch.get("yourSkills"):
        summary["platforms"]["clawhub"] = {
            "trackedSkills": {
                s["slug"]: {"downloads": s["downloads"], "stars": s["stars"]}
                for s in ch.get("trackedSkills", [])
            },
            "yourSkills": {
                s["slug"]: {"downloads": s["downloads"], "stars": s["stars"]}
                for s in ch.get("yourSkills", []) if not s.get("error")
            },
        }

    # Agensi
    ag = platforms.get("agensi", {})
    if ag.get("totalSkills") is not None:
        summary["platforms"]["agensi"] = {
            "totalSkills": ag["totalSkills"],
            "hasPayments": ag.get("hasPayments", False),
            "paymentProvider": ag.get("paymentProvider"),
            "skillSlugs": ag.get("skillSlugs", []),  # Keep for diffing
        }

    # GitHub
    gh = platforms.get("github", {})
    if gh.get("repos"):
        summary["platforms"]["github"] = {}
        for label, repo in gh.get("repos", {}).items():
            if repo.get("stars") is not None:
                summary["platforms"]["github"][label] = {
                    "stars": repo["stars"],
                    "forks": repo["forks"],
                    "openIssues": repo["openIssues"],
                    "latestRelease": repo.get("latestRelease", {}).get("tag"),
                }

    # Cursor
    cursor = platforms.get("cursor", {})
    if cursor.get("pagesAccessible"):
        summary["platforms"]["cursor"] = {
            "pagesAccessible": cursor.get("pagesAccessible", {}),
            "featuredCount": cursor.get("featuredCount", 0),
        }

    # Claude Skills Market
    csm = platforms.get("claude-skills-market", {})
    if csm.get("pagesAccessible"):
        summary["platforms"]["claude-skills-market"] = {
            "pagesAccessible": csm.get("pagesAccessible", {}),
            "hasBrowsePage": csm.get("hasBrowsePage", False),
            "hasFreeSkills": csm.get("hasFreeSkills", False),
        }

    # Payment status from watch
    if watch:
        for name, pdata in watch.get("paymentFeatures", {}).items():
            summary["paymentStatus"][name] = pdata.get("hasPayment", False)
            if pdata.get("evidence"):
                summary["alerts"].append({
                    "type": "payment",
                    "platform": name,
                    "message": f"Payment content detected: {', '.join([e['url'] for e in pdata['evidence'][:2]])}"
                })

    return summary


def diff_with_prev(summary, prev, daily_entries=None):
    """Compute change detection between current summary and previous run.

    Args:
        summary: Current run summary.
        prev: Previous latest.json summary (or None).
        daily_entries: List of daily.json entries (or None). When provided,
            also computes yourSkills deltas against yesterday's entry.
    """
    changes = []
    prev_p = prev.get("platforms", {}) if prev else {}

    # ClawHub
    ch = summary.get("platforms", {}).get("clawhub", {})
    prev_ch = prev_p.get("clawhub", {})

    # When daily entries are provided, compute yourSkills deltas against yesterday
    daily_yourskills_changes = []
    if daily_entries and len(daily_entries) >= 2:
        yesterday_entry = daily_entries[-2]
        daily_yourskills = yesterday_entry.get("clawhub", {}).get("yours", {})
        current_yourskills = ch.get("yourSkills", {})
        # daily.json uses "dl" key, summary uses "downloads" — map them
        metric_map = {"downloads": "dl", "stars": "stars"}
        for slug, current in current_yourskills.items():
            prev_daily = daily_yourskills.get(slug)
            if not prev_daily:
                continue
            for summary_metric in ["downloads", "stars"]:
                daily_key = metric_map[summary_metric]
                curr_val = current.get(summary_metric, 0)
                prev_val = prev_daily.get(daily_key, 0)
                if curr_val != prev_val:
                    delta = curr_val - prev_val
                    arrow = "↑" if delta > 0 else "↓" if delta < 0 else "→"
                    daily_yourskills_changes.append(f"{slug}* {summary_metric}: {curr_val:,} ({arrow}{abs(delta):+d})")

    for skill_group in ["trackedSkills", "yourSkills"]:
        # If we have daily-based yourSkills deltas, use those instead
        if skill_group == "yourSkills" and daily_yourskills_changes:
            changes.extend(daily_yourskills_changes)
            continue

        for slug, current in ch.get(skill_group, {}).items():
            prev_data = prev_ch.get(skill_group, {}).get(slug)
            if not prev_data:
                continue
            for metric in ["downloads", "stars"]:
                curr_val = current.get(metric, 0)
                prev_val = prev_data.get(metric, 0)
                if curr_val != prev_val:
                    delta = curr_val - prev_val
                    arrow = "↑" if delta > 0 else "↓" if delta < 0 else "→"
                    tag = " *" if skill_group == "yourSkills" else ""
                    changes.append(f"{slug}{tag} {metric}: {curr_val:,} ({arrow}{abs(delta):+d})")

    # Agensi
    ag = summary.get("platforms", {}).get("agensi", {})
    prev_ag = prev_p.get("agensi", {})

    if ag.get("totalSkills") and prev_ag.get("totalSkills"):
        delta = ag["totalSkills"] - prev_ag["totalSkills"]
        if delta != 0:
            arrow = "↑" if delta > 0 else "↓"
            changes.append(f"Agensi: {ag['totalSkills']} skills ({arrow}{abs(delta):+d})")

    # Agensi new skills (slug diff)
    if ag.get("skillSlugs") and prev_ag.get("skillSlugs"):
        new_slugs = set(ag["skillSlugs"]) - set(prev_ag["skillSlugs"])
        removed_slugs = set(prev_ag["skillSlugs"]) - set(ag["skillSlugs"])
        if new_slugs:
            changes.append(f"Agensi new skills: {len(new_slugs)} ({', '.join(sorted(new_slugs)[:5])})")
        if removed_slugs:
            changes.append(f"Agensi removed skills: {len(removed_slugs)}")

    # GitHub
    gh = summary.get("platforms", {}).get("github", {})
    prev_gh = prev_p.get("github", {})
    for label, repo in gh.items():
        prev_repo = prev_gh.get(label, {})
        for metric in ["stars", "forks", "openIssues"]:
            curr = repo.get(metric, 0)
            prev_val = prev_repo.get(metric, 0)
            if prev_val and curr != prev_val:
                delta = curr - prev_val
                arrow = "↑" if delta > 0 else "↓"
                changes.append(f"{label} {metric}: {curr:,} ({arrow}{abs(delta):+d})")

    # Payment changes
    for name, has_pay in summary.get("paymentStatus", {}).items():
        prev_pay = prev.get("paymentStatus", {}).get(name)
        if prev_pay is False and has_pay is True:
            changes.append(f"🆕 {name} appears to have added payments!")
        elif prev_pay is True and has_pay is False:
            changes.append(f"⚠️ {name} payment indicator disappeared")

    return changes


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw", required=True)
    parser.add_argument("--watch", default=None)
    parser.add_argument("--prev", default=None)
    parser.add_argument("--output", default=None)
    parser.add_argument("--daily", default=None,
                        help="Path to daily.json for daily-based yourSkills comparison")
    args = parser.parse_args()

    raw = load_json(args.raw)
    watch = load_json(args.watch) if args.watch else None
    prev = load_json(args.prev) if args.prev else None

    summary = build_summary(raw, watch)

    # Load daily entries if --daily is provided
    daily_entries = None
    if args.daily:
        try:
            with open(args.daily) as f:
                daily_entries = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            print(f"Warning: could not load {args.daily}: {e}", file=sys.stderr)

    if prev or daily_entries:
        summary["changes"] = diff_with_prev(summary, prev, daily_entries=daily_entries)

    output = args.output or os.path.join(os.path.dirname(os.path.abspath(args.raw)), "..", "latest.json")
    os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
    with open(output, "w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
