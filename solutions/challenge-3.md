# Challenge: C03 - Malicious File Hash
**Category:** Threat Hunting
**Points:** 210
**Flag:** c3c29cb8ee743c79788d7a9e0347afd2bff1fb67

## Challenge Description
What is the SHA-1 hash of the malicious file involved in the service modification on srv03?

## Solution Walkthrough

### Initial Analysis
The malicious file was `ssh-aqent.exe` (typosquatted name). Need to find its SHA-1 hash from DeviceFileEvents.

### KQL Query
```kql
DeviceFileEvents
| where DeviceName contains 'srv03'
  and FileName contains 'ssh-aqent'
| project Timestamp, FileName, FolderPath, SHA1, ActionType
```

### Key Finding
| Timestamp | FileName | SHA1 |
|-----------|----------|------|
| 2025-12-24 17:34:27 | ssh-aqent.exe | c3c29cb8ee743c79788d7a9e0347afd2bff1fb67 |

### Key Learnings
- DeviceFileEvents contains SHA1 hashes for file operations
- Typosquatted executables are a common attack technique
