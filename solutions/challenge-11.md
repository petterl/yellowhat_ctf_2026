# Challenge: C11 - Exfiltrated File
**Category:** Threat Hunting
**Points:** 226
**Flag:** 20251223162036_december.zip

## Challenge Description
What file was potentially exfiltrated from workstation04?

## Solution Walkthrough

### Initial Analysis
Look for archive files created by the malicious filezilla.exe process.

### KQL Query
```kql
DeviceFileEvents
| where DeviceName contains 'workstation04'
  and InitiatingProcessFileName == 'filezilla.exe'
  and ActionType == 'FileCreated'
| project Timestamp, FileName, FolderPath
```

### Key Finding
FileZilla created: **20251223162036_december.zip**

This appears to be a timestamped archive (2025-12-23 16:20:36) containing collected data for exfiltration.

### Key Learnings
- Attackers often create timestamped archives for exfiltration
- Look for ZIP files created by suspicious processes
- File naming patterns can reveal attacker TTPs
