# Challenge: C20 - Data Theft Folder (labsrv02)
**Category:** Threat Hunting
**Points:** 244
**Flag:** \\labsrv01.otrf.local\c$\SHARE\Public\Sales

## Challenge Description
What is the full path of the folder they attempted to steal from labsrv02?

## Solution Walkthrough

### Initial Analysis
Look for file archiving or data collection activity from pythonw.exe on labsrv02.

### KQL Query
```kql
DeviceProcessEvents
| where DeviceName == 'labsrv02.otrf.local'
  and (FileName == 'tar.exe' or ProcessCommandLine contains 'tar')
| project Timestamp, FileName, ProcessCommandLine, InitiatingProcessFileName
```

### Key Finding
- tar command: `tar -czvf C:/WebService/Sales.tar.gz \\labsrv01.otrf.local\c$\SHARE\Public\Sales`
- Target: **\\labsrv01.otrf.local\c$\SHARE\Public\Sales** (remote share on labsrv01)

### Key Learnings
- Attackers target file shares for data theft
- UNC paths (\\server\share) indicate remote access
- Admin shares (c$) require elevated privileges
