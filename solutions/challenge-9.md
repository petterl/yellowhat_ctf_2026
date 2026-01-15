# Challenge: C09 - Phishing Sender
**Category:** Threat Hunting
**Points:** 221
**Flag:** pradeep.gupta@otrflabs.com

## Challenge Description
Who sent the malicious FileZilla package to the victim?

## Solution Walkthrough

### Initial Analysis
The FileZilla ZIP was sent via email. Check EmailAttachmentInfo for the sender.

### KQL Query
```kql
EmailAttachmentInfo
| where RecipientEmailAddress contains 'dickens'
  and FileName contains 'FileZilla'
| project Timestamp, FileName, SenderFromAddress, RecipientEmailAddress
```

### Key Finding
| Timestamp | Attachment | Sender |
|-----------|------------|--------|
| 2025-12-23 15:09:09 | FileZilla-3.69.5.zip | pradeep.gupta@otrflabs.com |

The malicious FileZilla package was sent from **pradeep.gupta@otrflabs.com** to z.dickens.

### Key Learnings
- EmailAttachmentInfo table tracks email attachments
- Phishing attacks often use legitimate-looking internal email addresses
- Software updates/downloads via email are suspicious
