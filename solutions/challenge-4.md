# Challenge: C04 - C2 Address
**Category:** Threat Hunting
**Points:** 210
**Flag:** telemetry-ingest-prod-weu-01.westeurope.cloudapp.azure.com

## Challenge Description
What is the C2 address (FQDN) that the malicious file on srv03 is communicating with?

## Solution Walkthrough

### Initial Analysis
Look for network connections from the malicious process `ssh-aqent.exe` on srv03.

### KQL Query
```kql
DeviceNetworkEvents
| where DeviceName contains 'srv03'
  and InitiatingProcessFileName contains 'ssh-aqent'
| project Timestamp, RemoteIP, RemoteUrl, RemotePort
```

### Key Finding
The malicious executable communicated with:
- **telemetry-ingest-prod-weu-01.westeurope.cloudapp.azure.com** on port 443

The C2 domain is designed to look like legitimate Azure telemetry infrastructure.

### Key Learnings
- Attackers use legitimate-looking domain names to blend in
- Azure cloudapp domains can be easily created by attackers
- Port 443 (HTTPS) is commonly used to evade detection
