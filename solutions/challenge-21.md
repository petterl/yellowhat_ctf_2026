# Challenge: C21 - C2 After Lateral from labsrv02
**Category:** Threat Hunting
**Points:** 493
**Flag:** upload.forgersonline.org

## Challenge Description
After compromising labsrv02, the attackers moved laterally to another device. What is the C2 hostname on workstation01?

## Solution Walkthrough

### Initial Analysis
Earlier analysis showed pythonw.exe on labsrv02 copying files to workstation01. Check network connections from workstation01.

### KQL Query
```kql
DeviceNetworkEvents
| where DeviceName == 'workstation01.otrf.local'
  and isnotempty(RemoteUrl)
  and InitiatingProcessFileName == 'pythonw.exe'
| project Timestamp, RemoteUrl
```

### Key Finding
- pythonw.exe on workstation01 contacted **upload.forgersonline.org**
- This is the C2 for the final stage of the attack

### Key Learnings
- Track lateral movement by following network connections
- Attackers use different C2 infrastructure for different stages
- Domain names designed to look legitimate (forgersonline.org)
