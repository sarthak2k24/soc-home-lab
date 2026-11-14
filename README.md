# Home SOC Lab: Threat Detection & Automation

A home Security Operations Center lab for practicing the core loop of security operations: **collect logs → simulate attacks → detect → enrich → investigate → document.**

> Status: 🚧 In progress

## Architecture

```
 ┌──────────────┐  attacks   ┌──────────────────────┐  logs   ┌──────────────┐
 │  Kali Linux  │ ─────────▶ │ Windows 10/11        │ ──────▶ │ Wazuh SIEM   │
 │  (attacker)  │            │ + Sysmon + Wazuh agent│         │ (manager +   │
 └──────────────┘            └──────────────────────┘         │  dashboard)  │
                                                               └──────┬───────┘
                                                                      │ alerts
                                                               ┌──────▼───────┐
                                                               │ Python       │
                                                               │ enrichment   │──▶ AbuseIPDB / VirusTotal
                                                               └──────────────┘
```

## Tools

Wazuh · Sysmon · Kali Linux · Atomic Red Team · Python · MITRE ATT&CK · VirtualBox

## Repository layout

| Folder | Contents |
|---|---|
| `docs/` | Lab setup notes |
| `detections/` | Custom Wazuh detection rules, mapped to MITRE ATT&CK |
| `enrichment/` | Python alert-enrichment tool (threat intelligence lookups) |
| `playbooks/` | Incident response playbooks |
| `incident-reports/` | Write-ups of simulated incidents |
| `screenshots/` | Dashboards, alerts, and evidence |

## Detections

| Rule ID | Detects | MITRE ATT&CK | Status |
|---|---|---|---|
| 100100 | Windows logon brute force | T1110 | Planned |
| 100101 | Suspicious encoded PowerShell | T1059.001 | Planned |
| 100102 | Network scanning from internal host | T1046 | Planned |
| 100103 | New local admin account created | T1136.001 | Planned |

## Roadmap

- [ ] Deploy Wazuh manager and dashboard
- [ ] Onboard Windows endpoint with Sysmon and Wazuh agent
- [ ] Simulate attacks (brute force, Nmap scan, PowerShell, Atomic Red Team)
- [ ] Write and tune custom detection rules
- [ ] Build Python threat-intel enrichment tool
- [ ] Dashboard of alert volume and severity
- [ ] Incident report and response playbook

## Results

_To be filled in with real measurements as the lab is built (rules written, attacks detected, false-positive reduction, triage time saved)._
