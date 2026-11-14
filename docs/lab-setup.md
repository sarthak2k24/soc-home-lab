# Lab Setup

## Requirements
- VirtualBox (or VMware Workstation Player)
- ~16 GB RAM recommended (Wazuh ~4–8 GB, Windows ~4 GB, Kali ~2–4 GB)
- Put all VMs on the same **host-only / internal network** so attacks stay inside the lab

## Steps
1. **Wazuh server**: Ubuntu Server VM → install Wazuh (all-in-one) using the official quickstart.
2. **Windows endpoint**: install Sysmon with a community config, then install the Wazuh agent and point it at the Wazuh server.
3. **Kali Linux**: attacker VM on the same internal network.
4. Confirm Windows events appear in the Wazuh dashboard before simulating attacks.

## Notes
<!-- Record IPs, versions, problems you hit and how you fixed them. This becomes great interview material. -->
