# Challenge: C25 - Post-Compromise Cloud Object
**Category:** Threat Hunting
**Points:** 298
**Flag:** daily email summaries

## Challenge Description
After creating a New InboxRule, the attackers created another object unrelated to email in the cloud. What is the name of what they created?

## Solution Walkthrough

### Initial Analysis
Query CloudAppEvents for application creation activities from s.chisholm after the InboxRule.

### KQL Query
```kql
CloudAppEvents
| where ActionType contains 'application'
| project Timestamp, ActionType, Application, AccountDisplayName, ObjectName
| order by Timestamp desc
```

### Key Finding
- ActionType: "Add application." at 2025-12-26 11:39:38
- Application name: **daily email summaries**
- Created by: Samantha Chisholm (compromised account)
- Later added credentials (client secret) for persistence

### Key Learnings
- App registrations provide persistent access to cloud resources
- Attackers create apps with innocuous names to blend in
- Look for: App creation → Permission grants → Credential addition
- This is a common cloud persistence technique (T1098.001)
