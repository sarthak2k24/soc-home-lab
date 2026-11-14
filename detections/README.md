# Custom Detection Rules

Each rule documents **what it detects, the MITRE ATT&CK technique, how it was tested, and tuning notes**.

Wazuh custom rules go in `/var/ossec/etc/rules/local_rules.xml` on the manager (rule IDs 100000+).

## Template

```
Rule ID:
Name:
MITRE ATT&CK:
Log source:
Logic:
How I tested it:
False positives seen / tuning:
```
