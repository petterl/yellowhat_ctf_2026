# Challenge: C07 - Initial Compromise Executable
**Category:** Threat Hunting
**Points:** 216
**Flag:** filezilla.exe

## Challenge Description
What executable was used to compromise workstation04?

## Solution Walkthrough

### Initial Analysis
Need to trace back how workstation04 was initially compromised. Look for how ssh-aqent.exe arrived on workstation04.

### KQL Query
```kql
DeviceFileEvents
| where DeviceName contains 'workstation04'
  and FileName == 'ssh-aqent.exe'
| project Timestamp, ActionType, FolderPath, InitiatingProcessFileName
```

Result: ssh-aqent.exe was copied by **filezilla.exe**

### Key Finding
- FileZilla was used to transfer the malicious file
- The FileZilla installation itself was malicious (trojanized)
- FileZilla was received via email as a ZIP file

### Key Learnings
- Legitimate software can be weaponized (supply chain / trojanized apps)
- Track file operations to identify the initial compromise vector
