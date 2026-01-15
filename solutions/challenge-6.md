# Challenge: C06 - Lateral Movement Source
**Category:** Threat Hunting
**Points:** 210
**Flag:** workstation04.otrf.local

## Challenge Description
From which device was the malicious file transferred to srv03?

## Solution Walkthrough

### Initial Analysis
The file was created via network (ntoskrnl.exe as initiating process indicates SMB/network transfer). Check RequestSourceIP field.

### KQL Query
```kql
DeviceFileEvents
| where DeviceName contains 'srv03'
  and FileName == 'ssh-aqent.exe'
| project Timestamp, FileName, InitiatingProcessFileName, RequestAccountName, RequestSourceIP
```

Result: RequestSourceIP = 192.168.16.29

Query 2 - Identify device:
```kql
DeviceNetworkInfo
| where IPAddresses contains '192.168.16.29'
| distinct DeviceName
```

### Key Finding
- File transferred from IP **192.168.16.29**
- Device: **workstation04.otrf.local**
- Account used: svc.winbackup

### Key Learnings
- ntoskrnl.exe as initiating process indicates network file operations
- RequestSourceIP reveals the source of network file transfers
- DeviceNetworkInfo can map IPs to device names
