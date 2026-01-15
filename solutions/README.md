# BluRavenCTF Solutions

## Using Claude Code to Solve CTFs

This project was solved using [Claude Code](https://claude.ai/claude-code) as an AI pair programmer for threat hunting CTF challenges.

### Getting Started

1. **Set up environment:**
   ```bash
   export SESSION_COOKIE="your-ctfd-session-cookie"
   ```

2. **Start Claude Code in project directory:**
   ```bash
   cd /path/to/ctf-solver
   claude
   ```

3. **Give Claude the context:**
   - Claude will read `CLAUDE.md` automatically for project instructions
   - Ask Claude to list challenges: "list the unsolved challenges"
   - Pick a challenge: "solve challenge 5"

4. **Iterate on queries:**
   - Claude will write KQL queries and analyze results
   - Review the queries and suggest refinements
   - Claude submits flags and documents solutions

### Example Prompts

- "List all unsolved challenges"
- "What is challenge 12 asking for?"
- "Query for lateral movement from workstation04"
- "Submit the flag for challenge 8"
- "Document the solution for challenge 15"
- "Create a full attack timeline from all the findings"

### Tips for AI-Assisted CTF Solving

- Let Claude explore the data schema first
- Review queries before running to learn KQL
- Ask Claude to explain its reasoning
- Request documentation after each solve
- Periodically ask Claude to summarize the attack chain

## Summary

| ID | Challenge | Category | Points | Solved | Flag |
|----|-----------|----------|--------|--------|------|
| 1  | C01 - Malicious Service Modification | Threat Hunting | 250 | ✅ | srv03.otrf.local |
| 2  | C02 - Service Name | Threat Hunting | 210 | ✅ | ssh-agent |
| 3  | C03 - Malicious File Hash | Threat Hunting | 210 | ✅ | c3c29cb8ee743c79788d7a9e0347afd2bff1fb67 |
| 4  | C04 - C2 Address | Threat Hunting | 210 | ✅ | telemetry-ingest-prod-weu-01.westeurope.cloudapp.azure.com |
| 13 | C05 - Persistence File | Threat Hunting | 210 | ✅ | d1015f661df95cf76ba58370e520cca86f354515 |
| 5  | C06 - Lateral Movement Source | Threat Hunting | 210 | ✅ | workstation04.otrf.local |
| 6  | C07 - Initial Compromise | Threat Hunting | 216 | ✅ | filezilla.exe |
| 7  | C08 - Malicious DLL Hash | Threat Hunting | 244 | ✅ | bbb9aeac03f97aeb8d6fde1f3a1b01adf31f497c |
| 8  | C09 - Phishing Sender | Threat Hunting | 221 | ✅ | pradeep.gupta@otrflabs.com |
| 9  | C10 - Workstation C2 | Threat Hunting | 235 | ✅ | dl1.fzilla-cdn.org |
| 10 | C11 - Exfiltrated File | Threat Hunting | 226 | ✅ | 20251223162036_december.zip |
| 11 | C12 - Lateral Movement Account | Threat Hunting | 231 | ✅ | svc.winbackup |
| 12 | C13 - Workstation Persistence | Threat Hunting | 242 | ✅ | FileZilla.lnk |
| 14 | C14 - Exfiltration Target | Threat Hunting | 226 | ✅ | C:\Reports |
| 15 | C15 - C2 After Lateral Movement | Threat Hunting | 449 | ✅ | supporttelemetry-eu-dtfbefbwc9h7hphe.z01.azurefd.net |
| 16 | C16 - Lateral Movement Protocol | Threat Hunting | 285 | ✅ | RDP |
| 17 | C17 - Lateral Movement Account (labsrv02) | Threat Hunting | 280 | ✅ | srv_automation |
| 18 | C18 - Persistence on labsrv02 | Threat Hunting | 289 | ✅ | 59a97f9d7c1d6e10fa41ea9339568fb25ec55e27 |
| 20 | C19 - Malicious File (non-.exe) | Threat Hunting | 244 | ✅ | d8ec9eb8b763d89704e426fa3cfe564a499aa09d |
| 19 | C20 - Data Theft Folder | Threat Hunting | 242 | ✅ | \\labsrv01.otrf.local\c$\SHARE\Public\Sales |
| 21 | C21 - C2 After Lateral from labsrv02 | Threat Hunting | 488 | ✅ | upload.forgersonline.org |
| 22 | C22 - Lateral Movement Account (workstation01) | Threat Hunting | 244 | ✅ | j.taylor |
| 23 | C23 - Token Abuse IP Address | Threat Hunting | 493 | ✅ | 57.153.179.81 |
| 24 | C24 - First Malicious Cloud Activity | Threat Hunting | 248 | ✅ | New-InboxRule |
| 25 | C25 - Post-Compromise Cloud Object | Threat Hunting | 298 | ✅ | daily email summaries |

## Statistics

- Total challenges: 25
- Total solved: 25
- Total points: ~6,520

## Attack Chain Summary

```
1. Phishing Email
   pradeep.gupta@otrflabs.com -> z.dickens
   Attachment: FileZilla-3.69.5.zip (trojanized)

2. Initial Compromise (workstation04)
   - User extracts and runs filezilla.exe
   - DLL sideloading: malicious libsqlite3-0.dll
   - C2: dl1.fzilla-cdn.org
   - Persistence: FileZilla.lnk in Startup folder
   - Data collection: 20251223162036_december.zip

3. Lateral Movement to srv03
   - Account: svc.winbackup
   - Method: SMB file copy
   - Payload: ssh-aqent.exe (typosquatted)
   - Exfiltration target: C:\Reports

4. Persistence on srv03
   - Service modification: ssh-agent -> ssh-aqent.exe
   - Scheduled task: Telemetry_Upload (upload_telemetry.exe)
   - C2: telemetry-ingest-prod-weu-01.westeurope.cloudapp.azure.com

5. Lateral Movement to labsrv02
   - Account: srv_automation
   - Protocol: RDP
   - C2: supporttelemetry-eu-dtfbefbwc9h7hphe.z01.azurefd.net
   - Persistence: WebService.exe (Windows service wrapper)
   - Malicious file: python311.dll
   - Data theft target: \\labsrv01.otrf.local\c$\SHARE\Public\Sales

6. Lateral Movement to workstation01
   - Account: j.taylor
   - Method: File copy via pythonw.exe
   - C2: upload.forgersonline.org

7. Cloud Compromise (Token Theft)
   - Stolen token from s.chisholm on workstation01
   - Attacker IP: 57.153.179.81
   - Accessed Azure AD PowerShell
   - Created inbox rule: "backup"
   - Created app registration: "daily email summaries"
   - Added client secret for persistence
```

## Key Techniques Observed (MITRE ATT&CK)

- **Initial Access (TA0001)**: Phishing with trojanized software (T1566.001)
- **Execution (TA0002)**: DLL sideloading (T1574.002), Python scripts
- **Persistence (TA0003)**:
  - Startup folder LNK (T1547.001)
  - Service modification (T1543.003)
  - Scheduled tasks (T1053.005)
  - Windows Services (T1543.003)
  - Cloud app registration (T1098.001)
  - Inbox rules (T1137.005)
- **Credential Access (TA0006)**: Token theft (T1528)
- **Lateral Movement (TA0008)**: SMB file transfer (T1021.002), RDP (T1021.001)
- **Collection (TA0009)**: Archive collected data (T1560.001)
- **Command and Control (TA0011)**:
  - Azure cloudapp domains
  - Azure Front Door
  - Typosquatted domains
- **Exfiltration (TA0010)**: ZIP/TAR archives targeting Sales and Reports folders

## Timeline

| Time | Event |
|------|-------|
| Dec 23 | Phishing email sent to z.dickens |
| Dec 23-24 | workstation04 compromised, FileZilla malware executed |
| Dec 24 | Lateral movement to srv03 via svc.winbackup |
| Dec 24-25 | Persistence established on srv03 (service, scheduled task) |
| Dec 25 | Lateral movement to labsrv02 via srv_automation (RDP) |
| Dec 25 21:26 | Lateral movement to workstation01, C2 contact to upload.forgersonline.org |
| Dec 25 21:57 | Token stolen from s.chisholm, Azure AD PowerShell access from 57.153.179.81 |
| Dec 26 10:06 | Inbox rule "backup" created |
| Dec 26 11:39 | App registration "daily email summaries" created for cloud persistence |

**For detailed attack timeline with IOCs and detection opportunities, see [ATTACK-TIMELINE.md](ATTACK-TIMELINE.md)**
