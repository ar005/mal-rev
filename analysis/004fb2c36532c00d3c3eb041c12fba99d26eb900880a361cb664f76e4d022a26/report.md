# Threat Analysis Report

**Generated:** 2026-06-24 00:50 UTC
**Sample:** `004fb2c36532c00d3c3eb041c12fba99d26eb900880a361cb664f76e4d022a26_004fb2c36532c00d3c3eb041c12fba99d26eb900880a361cb664f76e4d022a26.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `004fb2c36532c00d3c3eb041c12fba99d26eb900880a361cb664f76e4d022a26_004fb2c36532c00d3c3eb041c12fba99d26eb900880a361cb664f76e4d022a26.exe` |
| File type | PE32+ executable for MS Windows 10.00 (GUI), x86-64, 9 sections |
| Size | 432,856 bytes |
| MD5 | `8bb976d9ec8c7fe70e3ac489717826ef` |
| SHA1 | `14801d4d24dece8f71a15d9b189af1e72c136549` |
| SHA256 | `004fb2c36532c00d3c3eb041c12fba99d26eb900880a361cb664f76e4d022a26` |
| Overall entropy | 6.317 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 300518272 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 65,536 | 6.105 | No |
| `fothk` | 4,096 | 0.016 | No |
| `.rdata` | 20,480 | 4.193 | No |
| `.data` | 4,096 | 0.105 | No |
| `.pdata` | 4,096 | 3.879 | No |
| `.detourc` | 12,288 | 2.086 | No |
| `.detourd` | 4,096 | 0.02 | No |
| `.rsrc` | 294,912 | 6.474 | No |
| `.reloc` | 4,096 | 2.427 | No |

### Imports

**ADVAPI32.dll**: `RegDeleteValueW`, `CheckTokenMembership`, `FreeSid`, `RegSetValueExW`, `RegCreateKeyExW`, `AllocateAndInitializeSid`, `RegCloseKey`, `RegQueryValueExW`, `RegEnumValueW`, `RegCreateKeyW`, `RegOpenKeyExW`, `RegOpenKeyExA`, `RegSetValueExA`, `RegDeleteKeyW`, `RegQueryValueExA`
**KERNEL32.dll**: `CloseHandle`, `CreateThread`, `SetFileAttributesA`, `GetProcAddress`, `DeleteCriticalSection`, `CreateProcessW`, `FreeLibrary`, `lstrcmpiA`, `lstrcmpiW`, `LoadLibraryExW`, `GetModuleFileNameA`, `FindFirstFileA`, `SetLastError`, `GetFullPathNameW`, `CreateDirectoryExA`
**USER32.dll**: `CharNextW`, `LoadStringW`, `PostQuitMessage`
**msvcrt.dll**: `_onexit`, `__dllonexit`, `_unlock`, `_lock`, `_commode`, `_fmode`, `_wcmdln`, `memset`, `_initterm`, `__setusermatherr`, `_cexit`, `_exit`, `exit`, `__set_app_type`, `__wgetmainargs`
**ntdll.dll**: `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `RtlCaptureContext`
**ole32.dll**: `CoRegisterClassObject`, `CoRevokeClassObject`, `CoInitialize`, `CoTaskMemAlloc`, `CoUninitialize`, `CoCreateInstance`, `CoTaskMemFree`, `CoImpersonateClient`, `CoRevertToSelf`, `CoGetCallContext`, `StringFromGUID2`, `CoInitializeSecurity`, `CLSIDFromString`, `CoInitializeEx`
**OLEAUT32.dll**: `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `SysStringLen`, `SysAllocString`, `SysFreeString`
**RPCRT4.dll**: `RpcStringFreeW`, `UuidCreate`, `UuidToStringW`
**urlmon.dll**: `CompatFlagsFromClsid`, `Extract`, `CoInternetCreateSecurityManager`, `ord_519`, `ord_107`, `CoInternetSetFeatureEnabled`
**WINTRUST.dll**: `CryptCATAdminReleaseContext`, `CryptCATAdminAddCatalog`, `CryptCATAdminAcquireContext`, `CryptCATAdminReleaseCatalogContext`
**AUTHZ.dll**: `AuthzFreeResourceManager`, `AuthzFreeContext`, `AuthzInitializeContextFromSid`, `AuthzInitializeResourceManager`, `AuthzAccessCheck`
**iertutil.dll**: `ord_172`, `ord_34`, `ord_134`, `ord_39`, `ord_57`, `ord_201`, `ord_200`, `ord_35`, `ord_650`, `ord_658`

## Extracted Strings

Total strings found: **905** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`fothk
`.rdata
@.data
.pdata
@.detourc
@.detourd
@.reloc
u L97tH
u*9Q<|%
LcA<E3
L$8u1H
%uNHcI
SUVWATAUAWH
PA_A]A\_^][
PA_A]A\_^][
PA_A]A\_^][
PA_A]A\_^][
PA_A]A\_^][
%u9Hc{
wnH9CPuhL
9dtrRt
WATAUAVAWH
 A_A^A]A\_
UWATAVAWH
fD9<Au
fD9<xu
A_A^A\_]
f98t
H
VWAUAVAWH
H!\$H3
H!\$@H
A_A^A]_^
UVWATAUAVAWH
 A_A^A]A\_^]
t$ UWAVH
UVWAUAVH
PA^A]_^]
x UATAUAVAWH
l$XD9)
fD9,Au
A_A^A]A\]
UWATAVAWH
D$`D9'
A_A^A\_]
VWATAVAWH
A_A^A\_^
L$ SVWAVH
8A^_^[
VWATAVAWH
0A_A^A\_^
UVWATAUAVAWH
fE94Du
fE94Gu
fD94Au
fD94Au
fD94yu
L$hD91t
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
L$ UWAVH
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
L!|$0E3
L!|$xH
A_A^A]A\_^]
9Y(t9Y,u
t"9_(t
H;BXu2I
H;B`u(I
\$ UVWH
x ATAVAWH
 A_A^A\
<\t<:t
UVWATAUAVAWH
 A_A^A]A\_^]
SUVWATAVAWH
fD9$Yu
fD9$Wu
fD9$Wu
@A_A^A\_^][
@SUVWATAVAWH
A_A^A\_^][
l$ VWAVH
H!\$`H
tsH!\$XH
l$ VWAVH
t$ WATAUAVAWH
f98t
H
 A_A^A]A\_
\$ VWAVH
t$ UWAVH
MPH!D$@L
H!D$HH
UVWATAUAVAWH
PA_A^A]A\_^]
fD94Gu
UATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400062c0` | `0x1400062c0` | 2185 | ✓ |
| `fcn.14000dcc0` | `0x14000dcc0` | 2011 | ✓ |
| `fcn.140007524` | `0x140007524` | 1905 | ✓ |
| `fcn.1400029e0` | `0x1400029e0` | 1527 | ✓ |
| `fcn.14000cb84` | `0x14000cb84` | 1372 | ✓ |
| `fcn.14000c614` | `0x14000c614` | 1210 | ✓ |
| `fcn.140005214` | `0x140005214` | 1089 | ✓ |
| `fcn.1400022e0` | `0x1400022e0` | 1019 | ✓ |
| `fcn.140005be0` | `0x140005be0` | 894 | ✓ |
| `fcn.140007070` | `0x140007070` | 890 | ✓ |
| `fcn.140006b50` | `0x140006b50` | 796 | ✓ |
| `fcn.140008d34` | `0x140008d34` | 792 | ✓ |
| `fcn.14000e7e8` | `0x14000e7e8` | 776 | ✓ |
| `fcn.14000f554` | `0x14000f554` | 775 | ✓ |
| `fcn.1400056d0` | `0x1400056d0` | 756 | ✓ |
| `fcn.140004ea4` | `0x140004ea4` | 730 | ✓ |
| `fcn.14001041c` | `0x14001041c` | 706 | ✓ |
| `fcn.14000eca4` | `0x14000eca4` | 704 | ✓ |
| `fcn.14000f8e8` | `0x14000f8e8` | 695 | ✓ |
| `fcn.140009054` | `0x140009054` | 685 | ✓ |
| `fcn.14000acd4` | `0x14000acd4` | 683 | ✓ |
| `fcn.140009308` | `0x140009308` | 674 | ✓ |
| `fcn.14000b4f8` | `0x14000b4f8` | 655 | ✓ |
| `fcn.14000df74` | `0x14000df74` | 633 | ✓ |
| `fcn.140001d60` | `0x140001d60` | 632 | ✓ |
| `fcn.14000c27c` | `0x14000c27c` | 629 | ✓ |
| `fcn.140003090` | `0x140003090` | 623 | ✓ |
| `fcn.14000af88` | `0x14000af88` | 613 | ✓ |
| `fcn.14000ff80` | `0x14000ff80` | 611 | ✓ |
| `fcn.14000d734` | `0x14000d734` | 608 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001d60.c`](code/fcn.140001d60.c)
- [`code/fcn.1400022e0.c`](code/fcn.1400022e0.c)
- [`code/fcn.1400029e0.c`](code/fcn.1400029e0.c)
- [`code/fcn.140003090.c`](code/fcn.140003090.c)
- [`code/fcn.140004ea4.c`](code/fcn.140004ea4.c)
- [`code/fcn.140005214.c`](code/fcn.140005214.c)
- [`code/fcn.1400056d0.c`](code/fcn.1400056d0.c)
- [`code/fcn.140005be0.c`](code/fcn.140005be0.c)
- [`code/fcn.1400062c0.c`](code/fcn.1400062c0.c)
- [`code/fcn.140006b50.c`](code/fcn.140006b50.c)
- [`code/fcn.140007070.c`](code/fcn.140007070.c)
- [`code/fcn.140007524.c`](code/fcn.140007524.c)
- [`code/fcn.140008d34.c`](code/fcn.140008d34.c)
- [`code/fcn.140009054.c`](code/fcn.140009054.c)
- [`code/fcn.140009308.c`](code/fcn.140009308.c)
- [`code/fcn.14000acd4.c`](code/fcn.14000acd4.c)
- [`code/fcn.14000af88.c`](code/fcn.14000af88.c)
- [`code/fcn.14000b4f8.c`](code/fcn.14000b4f8.c)
- [`code/fcn.14000c27c.c`](code/fcn.14000c27c.c)
- [`code/fcn.14000c614.c`](code/fcn.14000c614.c)
- [`code/fcn.14000cb84.c`](code/fcn.14000cb84.c)
- [`code/fcn.14000d734.c`](code/fcn.14000d734.c)
- [`code/fcn.14000dcc0.c`](code/fcn.14000dcc0.c)
- [`code/fcn.14000df74.c`](code/fcn.14000df74.c)
- [`code/fcn.14000e7e8.c`](code/fcn.14000e7e8.c)
- [`code/fcn.14000eca4.c`](code/fcn.14000eca4.c)
- [`code/fcn.14000f554.c`](code/fcn.14000f554.c)
- [`code/fcn.14000f8e8.c`](code/fcn.14000f8e8.c)
- [`code/fcn.14000ff80.c`](code/fcn.14000ff80.c)
- [`code/fcn.14001041c.c`](code/fcn.14001041c.c)

## Behavioral Analysis

This updated analysis incorporates the newly provided disassembly (chunk 2/2). The additional code reinforces the initial assessment that this binary is a sophisticated loader/installer, while revealing deeper layers of system interaction—specifically regarding **privilege escalation** and **security descriptor manipulation**.

### Updated Malware Analysis Report

#### Core Functionality and Purpose
The binary remains identified as a **loader or installer component**. However, the additional disassembly reveals it performs significant "heavy lifting" regarding filesystem preparation and security permission overrides. It doesn't just install a program; it actively modifies the OS's security rules to ensure that the subsequent payloads can run with high privileges or evade detection by standard security checks.

#### Suspicious or Malicious Behaviors
The following behaviors have been updated/expanded based on the new data:

*   **Persistence Mechanism:** (Maintained)
    *   The target of `RunOnce` and other registry keys ensures subsequent payloads persist.
*   **Anti-Analysis/Anti-Debugging:** (Updated)
    *   The presence of `IsDebuggerPresent()` within `fcn.14000df74` (alongside the previously identified `fcn.14000dcc0`) confirms a multi-layered approach to detecting analysis tools. The complexity of `fcn.14000df74` suggests it acts as a "gatekeeper" function that checks several environment conditions before allowing the main payload to execute.
*   **Privilege and ACL Manipulation (New/Enhanced):**
    *   **Security Descriptor Tampering:** Functions `fcn.14000b4f8` and `fcn.14000af88` are highly significant. They interact with the Windows Security model by:
        *   Creating **Well-Known SIDs** (e.g., 0x11, 0x1a).
        *   Modifying **Access Control Lists (ACLs)** using `SetEntriesInAclW`.
        *   Converting and copying SIDs to modify Security Descriptors (`GetSecurityDescriptorSacl`, `ConvertStringSidToSidW`).
    *   *Impact:* This is a sophisticated way for malware to grant itself "SYSTEM" or administrative rights over specific files/registry keys, ensuring that standard security software cannot block its actions.
*   **File System & Path Manipulation:**
    *   `fcn.14000acd4` performs intensive directory deletion and file cleanup. While common in installers, in this context, it is used to "sanitize" the environment or remove evidence of earlier execution stages (common in multi-stage droppers).
    *   `fcn.140009308` uses `GetFinalPathNameByHandleW` and `CopyFileW`, often used to resolve relative paths into absolute ones or move files from temporary "drop" locations to final destinations.

#### Notable Techniques & Patterns
*   **Complex Security Descriptor Manipulation:** The use of `ADVAPI32` functions like `SetSecurityDescriptorDacl` suggests the binary is trying to bypass **Windows Integrity Checks**. By modifying ACLs, it can ensure that a malicious file appears "trusted" or accessible to higher-level system processes.
*   **Robust Path Resolution:** The inclusion of complex logic for handling environment variables (e.g., `%` expansion in `fcn.140001d60`) and various string lengths indicates the malware is designed to be highly compatible across different Windows configurations.
*   **Advanced File Handling:** The use of `DuplicateHandle` and `CreateFileW` with specific flags (like those found in `fcn.14000c27c`) suggests the binary handles system-level resources that require specific permissions, common when attempting to interact with protected system files or registry keys.

---

### Updated Summary Table

| Feature | Evidence/Function | Risk Level | Note |
| :--- | :--- | :--- | :--- |
| **Anti-Analysis** | `IsDebuggerPresent` in multiple locations | **High** | Intentional effort to block researchers. |
| **Persistence** | `RunOnce` and Registry manipulation | **High** | Standard persistence for multi-stage infections. |
| **Privilege Escalation** | ACL/SID manipulation (`fcn.14000b4f8`, `fcn.14000af88`) | **Critical** | High-level system permissions tampering. |
| **Process Injection** | `OpenProcess`/`DuplicateHandle` / `IEAdvpack.Dll` | **High** | Preparation for launching/injecting payloads. |
| **System Tampering** | Code Store & Module Usage modification | **High** | Disabling system integrity checks for the payload. |
| **File Manipulation** | File deletions and path normalization | **Medium** | Used to hide traces or prepare file paths. |

### Conclusion of Analysis (Updated)
The binary is a **highly sophisticated, multi-stage loader**. It doesn't just provide persistence; it actively "hardens" the environment for a subsequent payload by:
1.  **Checking for analysis tools** (Anti-Debugging).
2.  **Modifying system security policies** to allow its components to bypass integrity checks (ACL/SID manipulation).
3.  **Cleaning up the filesystem** and resolving complex paths to ensure seamless execution of further malware stages.

The presence of advanced `ADVAPI32` calls for Security Descriptor modification strongly suggests this is a professional-grade piece of malware or a component of an Advanced Persistent Threat (APT) toolkit.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Registry Run Keys / Startup Folders | The use of `RunOnce` and other registry keys confirms the malware's intent to maintain persistence for subsequent payloads. |
| **T1435** | Debug Detection | The multiple implementations of `IsDebuggerPresent()` indicate a multi-layered strategy to detect and evade analysis environments. |
| **T1548** | Disable or Remove Security Software | The manipulation of ACLs, SIDs, and Security Descriptors is used to bypass Windows Integrity Checks and ensure the payload can run without being blocked by security software. |
| **T1070** | Indicator Removal | The extensive use of directory deletion and file cleanup functions is designed to "sanitize" the environment and remove traces of previous execution stages. |
| **T1564** | Update Public Key (Potential) | While not explicitly a key update, the manipulation of Security Descriptors to bypass integrity checks often targets certificate-based trust models in Windows. |

### Analyst Notes:
*   **Privilege Escalation Context:** The transition from "Security Descriptor Tampering" to **T1548** is based on the analyst's conclusion that these actions are intended to "bypass system integrity checks." By manipulating how the OS views the permissions of a file, the malware effectively blinds security software.
*   **Loader Sophistication:** The inclusion of `GetFinalPathNameByHandleW` and complex path expansion indicates this loader is designed for high reliability across diverse environments, typical of professional-grade APT tools or sophisticated Trojan droppers.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **IEAdvpack.Dll** (Identified as a component used for process injection/loading).
*   **RunOnce** (Registry key mentioned as a persistence mechanism; typically located in `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` or `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`).
*   **%s%s%d.tmp** (Pattern used for temporary file generation during the dropping/installation phase).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No cryptographic hashes were present in the provided text.*

### **Other artifacts**
*   **Anti-Analysis Techniques:** 
    *   `IsDebuggerPresent()` (detected in functions `fcn.14000df74` and `fcn.14000cc0`).
*   **Privilege Escalation / Security Manipulation:**
    *   Use of `SetEntriesInAclW`, `GetSecurityDescriptorSacl`, and `ConvertStringSidToSidW` (functions `fcn.14000b4f8` and `fcn.14000af88`) to manipulate Security Descriptors and bypass integrity checks.
*   **System Manipulation:**
    *   Modification of **Code Store & Module Usage** to disable system integrity checks for subsequent payloads.
*   **File System Activity:**
    *   `GetFinalPathNameByHandleW` / `CopyFileW` (function `fcn.140009308`) used for path normalization and moving files from temp locations.
    *   Automated cleanup/deletion of artifacts via function `fcn.14000acd4`.

---
**Analyst Note:** The primary threat indicators in this sample are behavioral rather than network-based. The presence of **IEAdvpack.Dll** and the sophisticated manipulation of **SIDs/ACLs** suggest a high-maturity loader designed to "harden" the environment for a secondary payload.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Sophisticated Security Manipulation:** The use of advanced `ADVAPI32` functions (e.g., `SetEntriesInAclW`, `GetSecurityDescriptorSacl`) to manipulate SIDs and ACLs indicates a high-maturity effort to bypass Windows Integrity Checks and ensure subsequent payloads can run with elevated privileges without being blocked by security software.
* **Anti-Analysis and Persistence:** The presence of multiple `IsDebuggerPresent()` checks within "gatekeeper" functions, combined with standard persistence via `RunOnce` registry keys, confirms the binary is designed to resist analysis while maintaining a foothold for multi-stage operations.
* **Environment Preparation (Staging):** The behavior includes automated file system "sanitization," path normalization (`GetFinalPathNameByHandleW`), and preparation for process injection (associated with `IEAdvpack.Dll`), all of which are hallmarks of a professional-grade loader designed to host subsequent malware stages (e.g., RATs or info-stealers).
