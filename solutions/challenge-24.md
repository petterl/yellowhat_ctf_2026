# Challenge: C24 - First Malicious Cloud Activity
**Category:** Threat Hunting
**Points:** 248
**Flag:** New-InboxRule

## Challenge Description
After gaining access to cloud resources from IP 57.153.179.81, what is the first malicious activity the attackers performed?

## Solution Walkthrough

### Initial Analysis
Query CloudAppEvents for activities from the attacker IP, looking for suspicious actions.

### KQL Query
```kql
CloudAppEvents
| where IPAddress == '57.153.179.81'
| project Timestamp, ActionType, Application, AccountDisplayName
| order by Timestamp asc
```

### Key Finding
- First activities: MailItemsAccessed (reading emails - reconnaissance)
- First malicious action: **New-InboxRule** at 2025-12-26 10:06:51
- Rule name: "backup"
- Account: Samantha Chisholm

### Key Learnings
- Inbox rules are commonly used for:
  - Hiding phishing responses
  - Forwarding emails to attacker
  - Deleting security alerts
- New-InboxRule is a key indicator of BEC attacks
