# Challenge: C08 - Malicious DLL Hash
**Category:** Threat Hunting
**Points:** 244
**Flag:** bbb9aeac03f97aeb8d6fde1f3a1b01adf31f497c

## Challenge Description
What is the SHA-1 hash of the actual malicious file (since filezilla.exe is signed and benign)?

## Solution Walkthrough

### Initial Analysis
FileZilla.exe itself is legitimate. The attack used DLL sideloading - a malicious DLL was included in the package.

### KQL Query
```kql
DeviceImageLoadEvents
| where DeviceName contains 'workstation04'
  and InitiatingProcessFileName == 'filezilla.exe'
  and FolderPath contains 'FileZilla-3.69.5'
| distinct FileName, SHA1
```

### Key Finding
Two sqlite3 DLLs were present (unusual):
- `libsqlite3-0.dll` - SHA1: **bbb9aeac03f97aeb8d6fde1f3a1b01adf31f497c** (MALICIOUS)
- `libsqlite3-1.dll` - SHA1: 697af54320364f4f7c8562b56e731b45e6129590

The malicious `libsqlite3-0.dll` replaced the legitimate DLL (DLL sideloading attack).

### Key Learnings
- DLL sideloading uses legitimate signed executables to load malicious DLLs
- Look for unusual DLL names or duplicate DLLs
- DeviceImageLoadEvents shows which DLLs are loaded by processes
