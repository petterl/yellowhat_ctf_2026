# BluRavenCTF - Complete Attack Timeline

## Executive Summary

A sophisticated multi-stage attack targeting Forgecraft organization, starting with a phishing email containing trojanized FileZilla software. The attack progressed through multiple systems, ultimately compromising cloud resources via token theft.

**Duration:** December 23-26, 2025
**Systems Compromised:** 4 endpoints + Azure AD
**Data Targeted:** Reports folder, Sales data

---

## Phase 1: Initial Access (Dec 23)

### Phishing Email
| Attribute | Value |
|-----------|-------|
| Sender | pradeep.gupta@otrflabs.com |
| Recipient | z.dickens@forgecraft.nl |
| Attachment | FileZilla-3.69.5.zip |
| Technique | T1566.001 - Spearphishing Attachment |

The attacker sent a phishing email with a trojanized version of FileZilla FTP client.

---

## Phase 2: Initial Compromise - workstation04 (Dec 23-24)

### Execution
| Attribute | Value |
|-----------|-------|
| Victim | z.dickens |
| Device | workstation04.otrf.local |
| Malicious File | filezilla.exe |
| Technique | T1204.002 - User Execution |

### DLL Sideloading
| Attribute | Value |
|-----------|-------|
| Legitimate Binary | filezilla.exe |
| Malicious DLL | libsqlite3-0.dll |
| DLL SHA1 | bbb9aeac03f97aeb8d6fde1f3a1b01adf31f497c |
| Technique | T1574.002 - DLL Side-Loading |

### Command & Control
| Attribute | Value |
|-----------|-------|
| C2 Domain | dl1.fzilla-cdn.org |
| Technique | T1071.001 - Web Protocols |

### Persistence
| Attribute | Value |
|-----------|-------|
| Method | Startup folder shortcut |
| File | FileZilla.lnk |
| Location | %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup |
| Technique | T1547.001 - Registry Run Keys / Startup Folder |

### Data Collection
| Attribute | Value |
|-----------|-------|
| Archive | 20251223162036_december.zip |
| Technique | T1560.001 - Archive via Utility |

---

## Phase 3: Lateral Movement to srv03 (Dec 24)

### Credential Usage
| Attribute | Value |
|-----------|-------|
| Account | svc.winbackup |
| Source | workstation04.otrf.local |
| Destination | srv03.otrf.local |
| Method | SMB file copy |
| Technique | T1021.002 - SMB/Windows Admin Shares |

### Payload Deployment
| Attribute | Value |
|-----------|-------|
| File | ssh-aqent.exe (typosquatted) |
| SHA1 | c3c29cb8ee743c79788d7a9e0347afd2bff1fb67 |
| Location | C:\Tooling\ |

---

## Phase 4: Persistence on srv03 (Dec 24-25)

### Service Modification
| Attribute | Value |
|-----------|-------|
| Service Name | ssh-agent |
| Original Binary | (legitimate ssh-agent) |
| Malicious Binary | ssh-aqent.exe |
| Technique | T1543.003 - Windows Service |

### Scheduled Task
| Attribute | Value |
|-----------|-------|
| Task Name | Telemetry_Upload |
| Binary | upload_telemetry.exe |
| SHA1 | d1015f661df95cf76ba58370e520cca86f354515 |
| Technique | T1053.005 - Scheduled Task |

### Command & Control
| Attribute | Value |
|-----------|-------|
| C2 Domain | telemetry-ingest-prod-weu-01.westeurope.cloudapp.azure.com |
| Infrastructure | Azure Cloud App |

### Data Exfiltration Target
| Attribute | Value |
|-----------|-------|
| Target Folder | C:\Reports |
| Method | tar -czvf |

---

## Phase 5: Lateral Movement to labsrv02 (Dec 25)

### Remote Desktop Connection
| Attribute | Value |
|-----------|-------|
| Account | srv_automation |
| Source | srv03.otrf.local |
| Destination | labsrv02.otrf.local |
| Protocol | RDP (port 3389) |
| Technique | T1021.001 - Remote Desktop Protocol |

### Persistence - Windows Service
| Attribute | Value |
|-----------|-------|
| Service Wrapper | WebService.exe |
| SHA1 | 59a97f9d7c1d6e10fa41ea9339568fb25ec55e27 |
| Location | C:\WebService\ |
| Executes | pythonw.exe web-svc.py |
| Technique | T1543.003 - Windows Service |

### Malicious DLL
| Attribute | Value |
|-----------|-------|
| File | python311.dll |
| SHA1 | d8ec9eb8b763d89704e426fa3cfe564a499aa09d |
| Technique | T1574.002 - DLL Side-Loading |

### Command & Control
| Attribute | Value |
|-----------|-------|
| C2 Domain | supporttelemetry-eu-dtfbefbwc9h7hphe.z01.azurefd.net |
| Infrastructure | Azure Front Door |

### Data Theft Target
| Attribute | Value |
|-----------|-------|
| Target | \\\\labsrv01.otrf.local\\c$\\SHARE\\Public\\Sales |
| Method | tar via UNC path |
| Technique | T1039 - Data from Network Shared Drive |

---

## Phase 6: Lateral Movement to workstation01 (Dec 25, 21:09-21:26)

### File Copy
| Attribute | Value |
|-----------|-------|
| Account | j.taylor |
| Source | labsrv02.otrf.local (192.168.16.1) |
| Destination | workstation01.otrf.local |
| Method | pythonw.exe file operations |
| Technique | T1021.002 - SMB/Windows Admin Shares |

### Command & Control
| Timestamp | Event |
|-----------|-------|
| 21:26:36 | pythonw.exe connects to upload.forgersonline.org |

| Attribute | Value |
|-----------|-------|
| C2 Domain | upload.forgersonline.org |
| Victim User | s.chisholm |

---

## Phase 7: Cloud Compromise via Token Theft (Dec 25-26)

### Token Theft
| Attribute | Value |
|-----------|-------|
| Victim | s.chisholm@forgecraft.nl |
| Source Device | workstation01.otrf.local |
| Technique | T1528 - Steal Application Access Token |

### Initial Cloud Access
| Timestamp | Event |
|-----------|-------|
| Dec 25, 21:57:07 | Azure Active Directory PowerShell sign-in |

| Attribute | Value |
|-----------|-------|
| Attacker IP | 57.153.179.81 |
| Location | Netherlands |
| Application | Azure Active Directory PowerShell |

### Email Reconnaissance
| Timestamp | Event |
|-----------|-------|
| Dec 26, 09:56:44 | MailItemsAccessed (reading emails) |

### Inbox Rule Creation
| Timestamp | Event |
|-----------|-------|
| Dec 26, 10:06:51 | New-InboxRule created |

| Attribute | Value |
|-----------|-------|
| Rule Name | backup |
| ActionType | New-InboxRule |
| Technique | T1137.005 - Outlook Rules |

### Application Registration (Persistence)
| Timestamp | Event |
|-----------|-------|
| Dec 26, 11:39:38 | Add application |
| Dec 26, 11:41:02 | Update application (add permissions) |
| Dec 26, 11:42:42 | Add client secret (credential) |

| Attribute | Value |
|-----------|-------|
| App Name | daily email summaries |
| App ID | b1043e13-f703-4883-9e0a-deee1727192f |
| Secret Name | maincred |
| Technique | T1098.001 - Additional Cloud Credentials |

### Permissions Requested
The malicious app requested Microsoft Graph API permissions:
- User.Read (delegated)
- Mail.Read (application)
- Mail.ReadBasic.All (application)
- Mail.ReadWrite (application)
- Mail.Send (application)
- MailboxSettings.Read (application)
- User.Read.All (application)
- User.ReadBasic.All (application)

---

## Attack Flow Diagram

```
                                    PHISHING EMAIL
                                          │
                                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 2: workstation04 (z.dickens)                                     │
│  ├─ filezilla.exe + libsqlite3-0.dll (DLL sideload)                    │
│  ├─ C2: dl1.fzilla-cdn.org                                             │
│  ├─ Persistence: FileZilla.lnk                                         │
│  └─ Collected: 20251223162036_december.zip                             │
└─────────────────────────────────────────────────────────────────────────┘
                                          │
                            SMB (svc.winbackup)
                                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 3-4: srv03                                                       │
│  ├─ ssh-aqent.exe (service hijack of ssh-agent)                        │
│  ├─ upload_telemetry.exe (scheduled task)                              │
│  ├─ C2: telemetry-ingest-prod-weu-01.westeurope.cloudapp.azure.com     │
│  └─ Target: C:\Reports                                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                          │
                            RDP (srv_automation)
                                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 5: labsrv02                                                      │
│  ├─ WebService.exe → pythonw.exe web-svc.py                            │
│  ├─ python311.dll (malicious)                                          │
│  ├─ C2: supporttelemetry-eu-dtfbefbwc9h7hphe.z01.azurefd.net          │
│  └─ Target: \\labsrv01\c$\SHARE\Public\Sales                           │
└─────────────────────────────────────────────────────────────────────────┘
                                          │
                            File Copy (j.taylor)
                                          ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 6: workstation01 (s.chisholm)                                    │
│  ├─ pythonw.exe                                                        │
│  ├─ C2: upload.forgersonline.org                                       │
│  └─ TOKEN THEFT ──────────────────────────┐                            │
└───────────────────────────────────────────│────────────────────────────┘
                                            │
                                            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  PHASE 7: Azure AD / Microsoft 365                                      │
│  ├─ Attacker IP: 57.153.179.81                                         │
│  ├─ Azure AD PowerShell access                                         │
│  ├─ Inbox rule: "backup"                                               │
│  └─ App registration: "daily email summaries" + client secret          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Indicators of Compromise (IOCs)

### Domains
| Domain | Purpose |
|--------|---------|
| dl1.fzilla-cdn.org | C2 - workstation04 |
| telemetry-ingest-prod-weu-01.westeurope.cloudapp.azure.com | C2 - srv03 |
| supporttelemetry-eu-dtfbefbwc9h7hphe.z01.azurefd.net | C2 - labsrv02 |
| upload.forgersonline.org | C2 - workstation01 |

### IP Addresses
| IP | Purpose |
|----|---------|
| 57.153.179.81 | Attacker cloud access |

### File Hashes (SHA1)
| Hash | File | Location |
|------|------|----------|
| bbb9aeac03f97aeb8d6fde1f3a1b01adf31f497c | libsqlite3-0.dll | workstation04 |
| c3c29cb8ee743c79788d7a9e0347afd2bff1fb67 | ssh-aqent.exe | srv03 |
| d1015f661df95cf76ba58370e520cca86f354515 | upload_telemetry.exe | srv03 |
| 59a97f9d7c1d6e10fa41ea9339568fb25ec55e27 | WebService.exe | labsrv02 |
| d8ec9eb8b763d89704e426fa3cfe564a499aa09d | python311.dll | labsrv02 |

### Accounts Compromised/Used
| Account | Usage |
|---------|-------|
| z.dickens | Initial victim (phishing) |
| svc.winbackup | Lateral movement to srv03 |
| srv_automation | Lateral movement to labsrv02 |
| j.taylor | Lateral movement to workstation01 |
| s.chisholm | Token theft, cloud access |

### Cloud Artifacts
| Artifact | Value |
|----------|-------|
| Inbox Rule | backup |
| App Registration | daily email summaries |
| App ID | b1043e13-f703-4883-9e0a-deee1727192f |

---

## Detection Opportunities

1. **Phishing**: Email with ZIP attachment from external domain
2. **DLL Sideloading**: Unsigned DLLs loaded by legitimate software
3. **Typosquatting**: ssh-aqent vs ssh-agent
4. **Service Modification**: ImagePath changes in registry
5. **Scheduled Tasks**: New tasks with suspicious binaries
6. **RDP from Servers**: Unusual RDP connections from server to server
7. **Token Theft**: Sign-ins from new IPs shortly after endpoint activity
8. **Inbox Rules**: New rules with generic names like "backup"
9. **App Registrations**: New apps with mail permissions
