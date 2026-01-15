# Challenge: C19 - Malicious File (non-.exe)
**Category:** Threat Hunting
**Points:** 244
**Flag:** d8ec9eb8b763d89704e426fa3cfe564a499aa09d

## Challenge Description
Attackers tend to avoid using obvious .exe files. What is the SHA-1 hash of the malicious file used on labsrv02?

## Solution Walkthrough

### Initial Analysis
Look for non-.exe files in the WebService folder that could be malicious (DLLs, scripts, etc.)

### KQL Query
```kql
DeviceFileEvents
| where DeviceName == 'labsrv02.otrf.local'
  and FolderPath contains 'WebService'
  and isnotempty(SHA1)
| project Timestamp, FileName, FolderPath, SHA1
```

### Key Finding
- **python311.dll** (SHA1: d8ec9eb8b763d89704e426fa3cfe564a499aa09d)
- Located in C:\WebService\
- Malicious Python DLL loaded by pythonw.exe

### Key Learnings
- Attackers use DLL sideloading to avoid detection
- Python DLLs can be trojaned to execute malicious code
- Look beyond .exe files for malware
