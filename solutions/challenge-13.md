# Challenge: C13 - Workstation Persistence
**Category:** Threat Hunting
**Points:** 244
**Flag:** FileZilla.lnk

## Challenge Description
What file was used to establish persistence on workstation04?

## Solution Walkthrough

### Initial Analysis
Look for files created in persistence locations (Startup folder, Run keys, etc.) by filezilla.exe.

### KQL Query
```kql
DeviceFileEvents
| where DeviceName contains 'workstation04'
  and InitiatingProcessFileName == 'filezilla.exe'
  and FolderPath contains 'Startup'
| project Timestamp, FileName, FolderPath
```

### Key Finding
- **FileZilla.lnk** was created in the Startup folder
- This ensures the malicious FileZilla runs on user login

### Key Learnings
- Startup folder is a classic persistence location
- LNK files in Startup folder execute on user login
- Look for DeviceFileEvents with Startup in the path
