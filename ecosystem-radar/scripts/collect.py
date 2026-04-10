#!/usr/bin/env python3
"""
collect.py — Fetch raw data from all enabled platforms.

Platforms:
- ClawHub: inspect tracked skills
- Agensi: scrape skill listing for total count + payment check + slug list for diffing
- GitHub: repo stats for platform adoption tracking

Outputs JSON to stdout or file.
Usage: python3 collect.py [--config CONFIG_PATH] [--output FILE] [--platform NAME]
"""

import json
import subprocess
import sys
import urllib.request
import urllib.error
import urllib.parse
import re
import os
from datetime import datetime, timezone


def load_config(config_path):
    with open(config_path) as f:
        return json.load(f)


def run_clawhub(args, timeout=30):
    """Run a clawhub CLI command and return parsed JSON."""
    try:
        result = subprocess.run(
            ["clawhub"] + args,
            capture_output=True, text=True, timeout=timeout
        )
        stdout = result.stdout.strip()
        if stdout.startswith("{"):
            try:
                return json.loads(stdout)
            except json.JSONDecodeError:
                pass
        return {"raw": stdout[:500], "error": "no JSON output"}
    except subprocess.TimeoutExpired:
        return {"error": "timeout"}
    except FileNotFoundError:
        return {"error": "clawhub not found"}
    except Exception as e:
        return {"error": str(e)}


def collect_clawhub(cfg):
    """Collect data from ClawHub: tracked skill stats."""
    data = {"trackedSkills": [], "yourSkills": []}

    all_slugs = list(set(
        cfg.get("trackSkills", []) + cfg.get("yourSkills", [])
    ))
    your_set = set(cfg.get("yourSkills", []))

    # Inspect specific skills
    for slug in all_slugs:
        result = run_clawhub(["inspect", slug, "--json"])
        skill = result.get("skill", {})
        if not skill.get("slug"):
            data.setdefault("errors", []).append(f"{slug}: {result.get('error', 'not found')}")
            continue
        entry = {
            "slug": skill["slug"],
            "displayName": skill.get("displayName", ""),
            "downloads": skill.get("stats", {}).get("downloads", 0),
            "installs": skill.get("stats", {}).get("installsCurrent", 0),
            "stars": skill.get("stats", {}).get("stars", 0),
            "comments": skill.get("stats", {}).get("comments", 0),
            "versions": skill.get("stats", {}).get("versions", 0),
            "updatedAt": skill.get("updatedAt"),
        }
        if slug in your_set:
            data["yourSkills"].append(entry)
        else:
            data["trackedSkills"].append(entry)

    data["trackedSkills"].sort(key=lambda x: x.get("downloads", 0), reverse=True)

    return data


def fetch_json(url, params=None, headers=None, timeout=20):
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def collect_agensi(cfg):
    """Collect data from Agensi: skill count, payment status, slug list for diffing."""
    data = {"totalSkills": 0, "hasPayments": False, "paymentProvider": None, "skillSlugs": []}

    known_categories = {
        "frontend-design", "testing-qa", "devops-deployment", "code-review",
        "documentation", "productivity", "data-engineering", "api-development"
    }

    try:
        req = urllib.request.Request(
            cfg["url"] + "/skills",
            headers={"User-Agent": "Mozilla/5.0 (compatible; ecosystem-radar/1.0)"}
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        slugs = re.findall(r'/skills/([a-z0-9\-]+)', html)
        seen = set()
        unique_slugs = []
        for s in slugs:
            if s not in seen:
                seen.add(s)
                unique_slugs.append(s)

        skill_slugs = [s for s in unique_slugs if s not in known_categories]
        data["totalSkills"] = len(skill_slugs)
        data["skillSlugs"] = skill_slugs  # Full list for diffing
    except Exception as e:
        data["error"] = str(e)

    # Payment check
    payment_url = cfg.get("paymentIndicator")
    if payment_url:
        try:
            req = urllib.request.Request(
                payment_url,
                headers={"User-Agent": "Mozilla/5.0 (compatible; ecosystem-radar/1.0)"}
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode("utf-8", errors="replace")
                if len(content) > 500 and "404" not in content[:200].lower():
                    data["hasPayments"] = True
                    if "stripe" in content.lower():
                        data["paymentProvider"] = "Stripe"
        except Exception as e:
            data["paymentCheckError"] = str(e)[:100]

    return data


def collect_github(cfg):
    """Collect GitHub repo stats for platform adoption tracking."""
    repos = cfg.get("repos", {})
    data = {"repos": {}}

    for label, repo in repos.items():
        repo_data = {"repo": repo}
        try:
            result = fetch_json(
                f"https://api.github.com/repos/{repo}",
                headers={"User-Agent": "ecosystem-radar/1.0", "Accept": "application/vnd.github.v3+json"}
            )
            repo_data["stars"] = result.get("stargazers_count", 0)
            repo_data["forks"] = result.get("forks_count", 0)
            repo_data["openIssues"] = result.get("open_issues_count", 0)
            repo_data["pushedAt"] = result.get("pushed_at")
        except Exception as e:
            repo_data["error"] = str(e)[:100]

        # Latest release
        try:
            releases = fetch_json(
                f"https://api.github.com/repos/{repo}/releases?per_page=1",
                headers={"User-Agent": "ecosystem-radar/1.0", "Accept": "application/vnd.github.v3+json"}
            )
            if releases and isinstance(releases, list) and len(releases) > 0:
                repo_data["latestRelease"] = {
                    "tag": releases[0].get("tag_name"),
                    "publishedAt": releases[0].get("published_at"),
                }
        except Exception as e:
            if "error" not in repo_data:
                repo_data["releaseError"] = str(e)[:100]

        data["repos"][label] = repo_data

    return data


def collect_cursor(cfg):
    """Collect data from Cursor Marketplace (JS-rendered, limited data)."""
    data = {"pagesAccessible": {}, "featuredCount": 0, "note": "JS-rendered, limited server-side data"}
    pages = cfg.get("pages", {})
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ecosystem-radar/1.0)"}
    for label, url in pages.items():
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode("utf-8", errors="replace")
            accessible = len(content) > 1000
            data["pagesAccessible"][label] = accessible
            # Count featured items
            featured = len(re.findall(r'Featured', content))
            if label == "home":
                data["featuredCount"] = featured // 2  # Approximate
        except Exception as e:
            data["pagesAccessible"][label] = False
    return data

def collect_claude_skills_market(cfg):
    """Collect data from Claude Skills Market (JS-rendered, limited data)."""
    data = {"pagesAccessible": {}, "hasBrowsePage": False, "hasFreeSkills": False, "note": "JS-rendered, limited server-side data"}
    pages = cfg.get("pages", {})
    headers = {"User-Agent": "Mozilla/5.0 (compatible; ecosystem-radar/1.0)"}
    for label, url in pages.items():
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read().decode("utf-8", errors="replace")
            accessible = len(content) > 1000
            data["pagesAccessible"][label] = accessible
            if label == "browse":
                data["hasBrowsePage"] = accessible
            elif label == "free":
                data["hasFreeSkills"] = accessible
        except Exception as e:
            data["pagesAccessible"][label] = False
    return data

COLLECTORS = {
    "clawhub": collect_clawhub,
    "agensi": collect_agensi,
    "github": collect_github,
    "cursor": collect_cursor,
    "claude-skills-market": collect_claude_skills_market,
}


def append_daily_entry(result, daily_path):
    """Append a compact daily entry from collected data to daily.json.

    If an entry for today's date already exists, overwrite it (latest run wins).
    """
    platforms = result.get("platforms", {})
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    timestamp = result.get("timestamp", datetime.now(timezone.utc).isoformat())

    # Build compact entry
    entry = {"date": today, "timestamp": timestamp}

    # ClawHub
    ch = platforms.get("clawhub", {})
    tracked = {
        s["slug"]: {"dl": s.get("downloads", 0), "stars": s.get("stars", 0)}
        for s in ch.get("trackedSkills", [])
    }
    yours = {
        s["slug"]: {"dl": s.get("downloads", 0), "stars": s.get("stars", 0)}
        for s in ch.get("yourSkills", [])
    }
    if tracked or yours:
        entry["clawhub"] = {}
        if tracked:
            entry["clawhub"]["tracked"] = tracked
        if yours:
            entry["clawhub"]["yours"] = yours

    # Agensi
    ag = platforms.get("agensi", {})
    if ag.get("totalSkills") is not None:
        entry["agensi"] = {
            "totalSkills": ag["totalSkills"],
            "skillSlugs": ag.get("skillSlugs", []),
        }

    # GitHub
    gh = platforms.get("github", {})
    repos = gh.get("repos", {})
    gh_data = {}
    for label, repo in repos.items():
        if repo.get("stars") is not None:
            gh_data[label] = {
                "stars": repo.get("stars", 0),
                "forks": repo.get("forks", 0),
                "openIssues": repo.get("openIssues", 0),
            }
    if gh_data:
        entry["github"] = gh_data

    try:
        # Load existing daily.json
        if os.path.exists(daily_path):
            with open(daily_path) as f:
                daily = json.load(f)
        else:
            daily = []

        # Overwrite today's entry if it exists, otherwise append
        found = False
        for i, existing in enumerate(daily):
            if existing.get("date") == today:
                daily[i] = entry
                found = True
                break
        if not found:
            daily.append(entry)

        os.makedirs(os.path.dirname(os.path.abspath(daily_path)), exist_ok=True)
        with open(daily_path, "w") as f:
            json.dump(daily, f, indent=2)
        action = "Updated" if found else "Appended"
        print(f"{action} daily entry for {today}", file=sys.stderr)
    except Exception as e:
        print(f"Warning: failed to write daily entry: {e}", file=sys.stderr)






def main():
    import argparse
    parser = argparse.ArgumentParser(description="Collect ecosystem data from all platforms")
    parser.add_argument("--config", default=None)
    parser.add_argument("--output", default=None)
    parser.add_argument("--platform", default=None)
    args = parser.parse_args()

    config_path = args.config
    if not config_path:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "..", "config.json")

    config = load_config(config_path)
    platforms = config["platforms"]
    timestamp = datetime.now(timezone.utc).isoformat()

    result = {"timestamp": timestamp, "runType": "collect", "platforms": {}}
    targets = {args.platform: platforms[args.platform]} if args.platform else platforms

    for name, cfg in targets.items():
        if not cfg.get("enabled", False):
            result["platforms"][name] = {"skipped": True}
            continue
        collector = COLLECTORS.get(name)
        if collector:
            try:
                result["platforms"][name] = collector(cfg)
            except Exception as e:
                result["platforms"][name] = {"error": str(e)}
        else:
            result["platforms"][name] = {"error": f"No collector for {name}"}

    output = json.dumps(result, indent=2, default=str)
    if args.output:
        outdir = os.path.dirname(os.path.abspath(args.output))
        os.makedirs(outdir, exist_ok=True)
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Data written to {args.output}", file=sys.stderr)
    else:
        print(output)

    # Append compact entry to daily.json
    script_dir = os.path.dirname(os.path.abspath(__file__))
    daily_path = os.path.join(script_dir, "..", "data", "daily.json")
    append_daily_entry(result, daily_path)


if __name__ == "__main__":
    main()
