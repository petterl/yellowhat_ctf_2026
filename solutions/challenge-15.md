# Challenge: C15 - C2 After Lateral Movement
**Category:** Threat Hunting
**Points:** 449
**Flag:** supporttelemetry-eu-dtfbefbwc9h7hphe.z01.azurefd.net

## Challenge Description
After compromising srv03, the attackers moved laterally to another device. What is the C2 hostname on the device they moved to?

## Solution Walkthrough

### Initial Analysis
From earlier analysis, srv03's upload_telemetry.exe made RDP connections to labsrv02 (10.120.116.60). Check labsrv02 for C2.

### KQL Queries

Query 1 - Find lateral movement:
```kql
DeviceNetworkEvents
| where DeviceName contains 'srv03'
  and InitiatingProcessFileName == 'upload_telemetry.exe'
  and RemotePort == 3389
| project RemoteIP
```
Result: 10.120.116.60 (labsrv02)

Query 2 - Find C2 on labsrv02:
```kql
DeviceNetworkEvents
| where DeviceName == 'labsrv02.otrf.local'
  and isnotempty(RemoteUrl)
| summarize count() by RemoteUrl, InitiatingProcessFileName
```

### Key Finding
- Lateral movement via RDP to labsrv02
- C2 on labsrv02: **supporttelemetry-eu-dtfbefbwc9h7hphe.z01.azurefd.net**
- Initiated by pythonw.exe (suspicious)

### Key Learnings
- Azure Front Door domains can be used for C2
- Domain designed to look like legitimate Microsoft telemetry
- Track lateral movement by following network connections
