# Challenge: C18 - Persistence on labsrv02
**Category:** Threat Hunting
**Points:** 289
**Flag:** 59a97f9d7c1d6e10fa41ea9339568fb25ec55e27

## Challenge Description
What is the SHA-1 hash of the file used to establish persistence on labsrv02?

## Solution Walkthrough

### Initial Analysis
Look for files created in persistence locations on labsrv02. Earlier analysis showed pythonw.exe running from C:\WebService.

### KQL Query
```kql
DeviceFileEvents
| where DeviceName == 'labsrv02.otrf.local'
  and FolderPath contains 'WebService'
  and isnotempty(SHA1)
| project Timestamp, FileName, FolderPath, SHA1
```

### Key Finding
- **WebService.exe** (SHA1: 59a97f9d7c1d6e10fa41ea9339568fb25ec55e27)
- Located in C:\WebService\
- Windows service wrapper that runs pythonw.exe web-svc.py

### Key Learnings
- Windows Services provide persistent execution
- Attackers use service wrappers to run scripts as services
- Check C:\WebService or similar folders for suspicious executables
