# Challenge: C10 - Workstation C2
**Category:** Threat Hunting
**Points:** 235
**Flag:** dl1.fzilla-cdn.org

## Challenge Description
What is the C2 hostname on workstation04?

## Solution Walkthrough

### Initial Analysis
Look for network connections from filezilla.exe on workstation04 to suspicious domains.

### KQL Query
```kql
DeviceNetworkEvents
| where DeviceName contains 'workstation04'
  and InitiatingProcessFileName == 'filezilla.exe'
  and isnotempty(RemoteUrl)
| project Timestamp, RemoteUrl, RemotePort
```

### Key Finding
Connections to fake FileZilla CDN domains:
- **dl1.fzilla-cdn.org**
- dl2.fzilla-cdn.org
- dl3.fzilla-cdn.org

These domains mimic legitimate FileZilla infrastructure but are attacker-controlled C2.

### Key Learnings
- Attackers create typosquatted/lookalike domains for C2
- `fzilla-cdn.org` vs legitimate `filezilla-project.org`
- Multiple C2 domains provide redundancy
