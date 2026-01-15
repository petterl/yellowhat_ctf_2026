# Challenge: C23 - Token Abuse IP Address
**Category:** Threat Hunting
**Points:** 493
**Flag:** 57.153.179.81

## Challenge Description
The attackers performed token stealing from workstation01 and used the stolen token to access cloud resources. What is the IP address used by the attackers?

## Solution Walkthrough

### Initial Analysis
Check Azure AD sign-in logs for s.chisholm (the user on workstation01) for anomalous IP addresses.

### KQL Query
```kql
SigninLogs
| where UserPrincipalName contains 's.chisholm'
| project TimeGenerated, UserPrincipalName, IPAddress, AppDisplayName, Location
| order by TimeGenerated desc
```

### Key Finding
- Normal corporate IP: 81.19.208.92
- Attacker IP: **57.153.179.81**
- Sign-in to Azure Active Directory PowerShell at 2025-12-25 21:57
- This was shortly after the C2 connection on workstation01 (21:26)

### Key Learnings
- Token theft allows attackers to access cloud resources
- Look for sign-ins from unusual IPs shortly after endpoint compromise
- Azure AD PowerShell access is a red flag for reconnaissance/persistence
