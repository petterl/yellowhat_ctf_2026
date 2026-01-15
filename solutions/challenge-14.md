# Challenge: C14 - Exfiltration Target
**Category:** Threat Hunting
**Points:** 226
**Flag:** C:\Reports

## Challenge Description
What is the full folder path that the attackers attempted to exfiltrate on srv03?

## Solution Walkthrough

### Initial Analysis
Need to find what folder the malware on srv03 was targeting for data exfiltration. Look for file archiving or compression activity.

### KQL Query
```kql
DeviceProcessEvents
| where DeviceName contains 'srv03'
  and (FileName in ('upload_telemetry.exe', 'ssh-aqent.exe')
       or InitiatingProcessFileName in ('upload_telemetry.exe', 'ssh-aqent.exe'))
| project Timestamp, FileName, ProcessCommandLine, InitiatingProcessFileName
```

### Key Finding
- upload_telemetry.exe spawned tar.exe with command:
  `tar -czvf C:/Reports/reports.tar.gz C:/Reports`
- Target folder: **C:\Reports**

### Key Learnings
- Look for archiving tools (tar, zip, 7z) spawned by suspicious processes
- Command line arguments reveal exfiltration targets
- Attackers compress data before exfiltration to reduce transfer size
