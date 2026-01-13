# CTF Solver Project

## Tools Available

- `./ctfd.sh challenges` - list all challenges
- `./ctfd.sh challenge <id>` - get challenge details
- `./ctfd.sh submit <id> <flag>` - submit a flag (handles CSRF automatically)
- `./ctfd.sh scoreboard` - view top 10 scoreboard
- `./query-kusto.py "<KQL query>"` - run KQL against Azure Data Explorer

## Workflow

1. List challenges with `./ctfd.sh challenges`
2. Pick an unsolved challenge and read its details
3. Analyze what's being asked
4. Write and iterate on KQL queries to find the answer
5. Submit the flag
6. **Document the solution** (see below)

## Solution Documentation

After solving each challenge, create/update these files:

### solutions/challenge-<id>.md

Write a detailed walkthrough:

```
# Challenge: <name>
**Category:** <category>
**Points:** <points>
**Flag:** <flag>

## Challenge Description
<paste the challenge text>

## Solution Walkthrough

### Initial Analysis
<what did the challenge ask for, what tables/data would be relevant>

### KQL Queries

Query 1 - <purpose>:
```kql
<query>
```
Result: <what this showed>

Query 2 - <purpose>:
```kql
<query>
```
Result: <what this revealed>

### Final Query
```kql
<the query that found the flag>
```

### Key Learnings
- <what techniques were useful>
- <what to remember for similar challenges>
```

### solutions/README.md

Keep a summary table:

| ID | Challenge | Category | Points | Solved | Flag |
|----|-----------|----------|--------|--------|------|
| 1  | Name      | Category | 100    | ✅     | FLAG{...} |

## Useful KQL Tables (Threat Hunting)

| Table | Purpose |
|-------|---------|
| DeviceProcessEvents | Process creation, command lines, parent processes |
| DeviceNetworkEvents | Network connections, C2 traffic, DNS |
| DeviceFileEvents | File creation, modification, deletion |
| DeviceLogonEvents | User logins, lateral movement detection |
| DeviceRegistryEvents | Registry modifications, persistence |
| DeviceImageLoadEvents | DLL loading, sideloading detection |
| SigninLogs | Azure AD sign-ins, token usage |
| CloudAppEvents | M365/Azure activities (inbox rules, app registrations) |

## Common Attack Patterns

- **DLL Sideloading**: Check `DeviceImageLoadEvents` for unsigned DLLs loaded by legitimate apps
- **Service Modification**: Look for `ImagePath` changes in `DeviceRegistryEvents`
- **Scheduled Tasks**: Search `DeviceProcessEvents` for `schtasks.exe` or task creation
- **Lateral Movement**: Check `DeviceLogonEvents` for unusual account/source combinations
- **Token Theft**: Look for `SigninLogs` from new IPs after endpoint compromise
- **Cloud Persistence**: Check `CloudAppEvents` for `New-InboxRule` or app registrations

## Tips

- Start with broad queries to understand the data schema
- Use `| take 10` to preview results
- Check table names with `.show tables` or `TableName | getschema`
- Document failed approaches too - they're useful for learning
- For backslash paths in submissions, escape properly: `C:\\Reports`
- If network errors occur, retry with delays between queries
- Reference `solutions/ATTACK-TIMELINE.md` for complete attack chain with IOCs
