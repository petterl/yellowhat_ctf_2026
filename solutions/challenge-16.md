# Challenge: C16 - Lateral Movement Protocol
**Category:** Threat Hunting
**Points:** 289
**Flag:** RDP

## Challenge Description
What protocol was used to move laterally to labsrv02 from srv03?

## Solution Walkthrough

### Initial Analysis
Check network connections from srv03 to labsrv02, looking at the port number.

### KQL Query
```kql
DeviceNetworkEvents
| where DeviceName contains 'srv03'
  and InitiatingProcessFileName == 'upload_telemetry.exe'
| project RemoteIP, RemotePort
| where RemotePort == 3389
```

### Key Finding
- Connection to labsrv02 (10.120.116.60) on port **3389**
- Port 3389 = **RDP** (Remote Desktop Protocol)

### Key Learnings
- Port 3389 indicates RDP lateral movement
- Malware using RDP for lateral movement is common
- upload_telemetry.exe has RDP capabilities built-in
