# Challenge: C17 - Lateral Movement Account (labsrv02)
**Category:** Threat Hunting
**Points:** 280
**Flag:** srv_automation

## Challenge Description
What account was used to move laterally from srv03 to labsrv02?

## Solution Walkthrough

### Initial Analysis
Check DeviceLogonEvents on labsrv02 for network logons from srv03 around the time of the RDP connection.

### KQL Query
```kql
DeviceLogonEvents
| where DeviceName == 'labsrv02.otrf.local'
  and LogonType == 'RemoteInteractive'
| project Timestamp, AccountName, RemoteIP, LogonType
| order by Timestamp desc
```

### Key Finding
- Account: **srv_automation**
- Logged in via RDP from srv03

### Key Learnings
- RemoteInteractive logon type indicates RDP
- Service/automation accounts are valuable targets for lateral movement
- Track logon events to identify compromised accounts
