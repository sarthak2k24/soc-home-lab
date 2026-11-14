"""Enrich Wazuh alerts with threat intelligence.

Reads alerts (JSON lines from Wazuh's alerts.json), extracts source IPs,
looks them up on AbuseIPDB and VirusTotal, and prints a short triage summary.

Usage:
    python enrich.py path/to/alerts.json
"""
import json
import os
import sys

ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_API_KEY")
VIRUSTOTAL_KEY = os.getenv("VIRUSTOTAL_API_KEY")


def load_alerts(path):
    """Yield one alert dict per line of a Wazuh alerts.json file."""
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def extract_source_ip(alert):
    """Return the attacker/source IP from an alert, or None.

    TODO: inspect a real alert and find where the source IP lives
    (often alert["data"]["srcip"] or inside alert["data"]["win"]["eventdata"]).
    """
    return None


def lookup_abuseipdb(ip):
    """TODO: call the AbuseIPDB /api/v2/check endpoint and return the abuse score."""
    return None


def lookup_virustotal(ip):
    """TODO: call the VirusTotal /api/v3/ip_addresses/{ip} endpoint and return malicious-vote counts."""
    return None


def summarize(alert, ip, abuse, vt):
    """TODO: print a one-line triage summary: rule, severity, IP, reputation."""
    print(alert.get("rule", {}).get("description"), ip, abuse, vt)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    for alert in load_alerts(sys.argv[1]):
        ip = extract_source_ip(alert)
        if not ip:
            continue
        summarize(alert, ip, lookup_abuseipdb(ip), lookup_virustotal(ip))


if __name__ == "__main__":
    main()
