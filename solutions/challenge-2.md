# Challenge: C02 - Service Name
**Category:** Threat Hunting
**Points:** 210
**Flag:** ssh-agent

## Challenge Description
What is the name of the Windows service that was maliciously modified on srv03?

## Solution Walkthrough

### Initial Analysis
From C01, we identified suspicious registry modifications on srv03. The registry key path reveals the service name.

### KQL Query
```kql
DeviceRegistryEvents
| where DeviceName contains 'srv03'
  and RegistryKey contains 'Services'
  and RegistryValueName == 'ImagePath'
  and isnotempty(PreviousRegistryValueData)
| project RegistryKey
```

### Key Finding
The registry key was: `HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\ssh-agent`

The service name is **ssh-agent** - the OpenSSH Authentication Agent service.

### Key Learnings
- Service names can be extracted from registry key paths
- Attackers often target legitimate Windows services for persistence
