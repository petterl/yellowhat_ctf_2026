# Challenge: C01 - Malicious Service Modification
**Category:** Threat Hunting
**Points:** 250
**Flag:** srv03.otrf.local

## Challenge Description
Hunt for suspicious service-related activity and identify where the compromise occurred. Determine on which device a malicious Windows service modification took place.

## Solution Walkthrough

### Initial Analysis
Windows services can be modified via registry changes to `HKLM\SYSTEM\CurrentControlSet\Services\`. Look for ImagePath modifications with previous values indicating a change to an existing service.

### KQL Queries

Query 1 - Find ImagePath modifications:
```kql
DeviceRegistryEvents
| where RegistryKey contains 'Services'
  and RegistryValueName == 'ImagePath'
  and ActionType == 'RegistryValueSet'
  and isnotempty(PreviousRegistryValueData)
| project Timestamp, DeviceName, RegistryKey, RegistryValueData, PreviousRegistryValueData
```

### Key Finding
Two suspicious registry changes on **srv03.otrf.local** for the ssh-agent service:

| Timestamp | Change |
|-----------|--------|
| 2025-12-24 18:00:14 | Changed from `%SystemRoot%\System32\OpenSSH\ssh-agent.exe` to `cmd.exe /c C:\Windows\system32\OpenSSH\ssh-aqent.exe` |
| 2025-12-24 18:00:44 | Reverted to legitimate path |

**Malicious indicators:**
- Typosquatting: `ssh-aqent.exe` (with 'q') instead of `ssh-agent.exe` (with 'g')
- Using `cmd.exe /c` wrapper
- Quick reversion to hide tracks

### Key Learnings
- Service ImagePath modifications are a common persistence/execution technique
- Look for typosquatting in executable names
- Attackers often revert changes quickly to hide their tracks
