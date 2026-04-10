#!/usr/bin/env python3
"""
watch.py — Detect new marketplaces and payment feature changes.

Uses web search + URL checks to find:
1. New agent skill marketplaces not in our known list
2. Payment features appearing on known platforms

Usage: python3 watch.py [--config CONFIG_PATH] [--output FILE]
"""

import json
import sys
import os
import re
import urllib.request
import urllib.error
from datetime import datetime, timezone


def load_config(config_path):
    with open(config_path) as f:
        return json.load(f)


def check_url_has_payment_content(url, timeout=10):
    """Check if a URL exists AND contains payment-related content."""
    payment_terms = [
        "stripe", "payment", "pricing", "checkout", "billing",
        "commission", "payout", "subscription", "pay", "purchase",
        "buy", "sell", "merchant", "revenue share"
    ]
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ecosystem-radar/1.0)"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content = resp.read().decode("utf-8", errors="replace")[:10000]
        if len(content) < 200:
            return False, "too short"
        content_lower = content.lower()
        found = [t for t in payment_terms if t in content_lower]
        return len(found) >= 2, found
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, "404"
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:50]


def check_payment_features(config):
    """Check known platforms for payment/pricing pages with real content."""
    results = {}
    platforms = config["platforms"]

    for name, cfg in platforms.items():
        if not cfg.get("enabled", False):
            continue

        platform_result = {"hasPayment": False, "paymentUrls": {}}
        check_urls = config.get("watch", {}).get("paymentCheckUrls", {}).get(name, [])

        # Also check common pricing patterns
        domain = cfg.get("url", "").replace("https://", "").replace("http://", "").split("/")[0]
        common_paths = ["/pricing", "/pro", "/premium", "/monetize", "/sell", "/payments"]
        for path in common_paths:
            check_urls.append(f"https://{domain}{path}")

        for url in check_urls:
            has_pay, detail = check_url_has_payment_content(url)
            platform_result["paymentUrls"][url] = {
                "hasPaymentContent": has_pay,
                "detail": detail
            }
            if has_pay:
                platform_result["hasPayment"] = True
                if not platform_result.get("evidence"):
                    platform_result["evidence"] = []
                platform_result["evidence"].append({"url": url, "terms": detail})

        results[name] = platform_result

    return results


def detect_new_marketplaces(config):
    """
    This is a placeholder for marketplace discovery.
    The actual detection should be done by the LLM using web_search,
    comparing results against the known platform list in config.
    
    Returns the known platform URLs for comparison.
    """
    known = set()
    for name, cfg in config["platforms"].items():
        if cfg.get("url"):
            known.add(cfg["url"])
    return {
        "knownPlatforms": sorted(list(known)),
        "searchQueries": config.get("watch", {}).get("searchQueries", []),
        "note": "Marketplace discovery should use web_search in the LLM step. Compare results against knownPlatforms."
    }


def check_agensi_payment_detail(cfg):
    """Deep check on Agensi payment setup (Stripe)."""
    result = {"checked": False}
    payment_url = cfg.get("paymentIndicator")
    if not payment_url:
        return result

    try:
        req = urllib.request.Request(
            payment_url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; ecosystem-radar/1.0)"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode("utf-8", errors="replace")
            result["checked"] = True
            result["hasContent"] = len(content) > 500
            result["contentLength"] = len(content)

            # Extract meaningful details
            if result["hasContent"]:
                # Look for commission/fee structure
                fees = re.findall(r'(\d+(?:\.\d+)?)\s*%', content)
                if fees:
                    result["percentagesFound"] = fees[:5]

                # Look for payment-related terms
                terms = ["stripe", "connect", "payout", "commission", "fee", "revenue", "seller", "buyer"]
                found_terms = [t for t in terms if t.lower() in content.lower()]
                result["paymentTerms"] = found_terms
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Watch for new marketplaces and payment features")
    parser.add_argument("--config", default=None, help="Path to config.json")
    parser.add_argument("--output", default=None, help="Write output to file instead of stdout")
    args = parser.parse_args()

    config_path = args.config
    if not config_path:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "..", "config.json")

    config = load_config(config_path)
    timestamp = datetime.now(timezone.utc).isoformat()

    result = {
        "timestamp": timestamp,
        "runType": "watch",
        "paymentFeatures": check_payment_features(config),
        "newMarketplaceSearch": detect_new_marketplaces(config),
    }

    # Deep check Agensi if enabled
    if config["platforms"].get("agensi", {}).get("enabled"):
        result["agensiPaymentDetail"] = check_agensi_payment_detail(config["platforms"]["agensi"])

    output = json.dumps(result, indent=2, default=str)

    if args.output:
        outdir = os.path.dirname(os.path.abspath(args.output))
        os.makedirs(outdir, exist_ok=True)
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Watch data written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
