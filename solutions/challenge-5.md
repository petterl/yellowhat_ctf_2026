# Challenge: C05 - Persistence File
**Category:** Threat Hunting
**Points:** 210
**Flag:** d1015f661df95cf76ba58370e520cca86f354515

## Challenge Description
What is the SHA-1 hash of the file used to establish persistence on srv03?

## Solution Walkthrough

### Initial Analysis
The service modification was one form of persistence. Need to look for additional persistence mechanisms like scheduled tasks.

### KQL Queries

Query 1 - Find scheduled tasks:
```kql
DeviceEvents
| where DeviceName contains 'srv03'
  and ActionType == 'ScheduledTaskCreated'
| project Timestamp, ActionType, AdditionalFields
```

Result: Found `\Telemetry_Upload` task running `C:\Tooling\upload_telemetry.exe` every 60 minutes.

Query 2 - Get file hash:
```kql
DeviceFileEvents
| where DeviceName contains 'srv03'
  and FileName == 'upload_telemetry.exe'
| project FileName, SHA1, InitiatingProcessFileName
```

### Key Finding
- **upload_telemetry.exe** was dropped by ssh-aqent.exe
- SHA1: **d1015f661df95cf76ba58370e520cca86f354515**
- Scheduled task runs every 60 minutes for persistence

### Key Learnings
- Attackers often establish multiple persistence mechanisms
- Scheduled tasks are a common persistence technique
- Look at DeviceEvents for ScheduledTaskCreated action type
