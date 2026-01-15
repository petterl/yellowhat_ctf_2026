# Challenge: C12 - Lateral Movement Account
**Category:** Threat Hunting
**Points:** 231
**Flag:** svc.winbackup

## Challenge Description
What account was used to move laterally from workstation04 to srv03?

## Solution Walkthrough

### Initial Analysis
Check the RequestAccountName field in file events when the malicious file was copied to srv03.

### KQL Query
```kql
DeviceFileEvents
| where DeviceName contains 'srv03'
  and FileName == 'ssh-aqent.exe'
| project RequestAccountName, RequestSourceIP
```

### Key Finding
- Account: **svc.winbackup**
- This is a service account that was compromised and used for lateral movement

### Key Learnings
- Service accounts are valuable targets for lateral movement
- RequestAccountName reveals the account used for network file operations
- Monitor service account usage for anomalies
