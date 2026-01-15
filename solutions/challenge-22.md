# Challenge: C22 - Lateral Movement Account (workstation01)
**Category:** Threat Hunting
**Points:** 244
**Flag:** j.taylor

## Challenge Description
What is the name of the account used for lateral movement from labsrv02 to workstation01?

## Solution Walkthrough

### Initial Analysis
Check DeviceLogonEvents on workstation01 for network logons from labsrv02.

### KQL Query
```kql
DeviceLogonEvents
| where DeviceName == 'workstation01.otrf.local'
| project Timestamp, AccountName, RemoteIP, LogonType
| order by Timestamp desc
```

### Key Finding
- Account: **j.taylor**
- Network logon from 192.168.16.1 (labsrv02)
- Used for lateral movement to workstation01

### Key Learnings
- User accounts can be compromised for lateral movement
- Network logons from unexpected sources indicate compromise
- j.taylor's credentials were likely harvested from labsrv02
