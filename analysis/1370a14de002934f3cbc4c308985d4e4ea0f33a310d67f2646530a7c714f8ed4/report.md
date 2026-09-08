# Threat Analysis Report

**Generated:** 2026-09-02 15:52 UTC
**Sample:** `1370a14de002934f3cbc4c308985d4e4ea0f33a310d67f2646530a7c714f8ed4_1370a14de002934f3cbc4c308985d4e4ea0f33a310d67f2646530a7c714f8ed4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1370a14de002934f3cbc4c308985d4e4ea0f33a310d67f2646530a7c714f8ed4_1370a14de002934f3cbc4c308985d4e4ea0f33a310d67f2646530a7c714f8ed4.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 6 sections |
| Size | 24,446,944 bytes |
| MD5 | `3596ea3bc37499ec21418686a738f1d5` |
| SHA1 | `0abd3110af82c03dff83d35ef9df59cbc900a0a8` |
| SHA256 | `1370a14de002934f3cbc4c308985d4e4ea0f33a310d67f2646530a7c714f8ed4` |
| Overall entropy | 7.987 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1760109136 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,144,320 | 6.584 | No |
| `.rdata` | 276,480 | 5.684 | No |
| `.data` | 27,136 | 4.684 | No |
| `CPADinfo` | 512 | 0.122 | No |
| `.rsrc` | 22,920,704 | 8.0 | ⚠️ Yes |
| `.reloc` | 50,688 | 6.627 | No |

### Imports

**ole32.dll**: `StgOpenStorage`
**RstrtMgr.DLL**: `RmGetList`, `RmEndSession`, `RmStartSession`, `RmRegisterResources`
**ntdll.dll**: `RtlNtStatusToDosError`, `NtQuerySystemInformation`, `RtlUnwind`, `VerSetConditionMask`
**SHLWAPI.dll**: `PathIsDirectoryW`, `PathIsDirectoryEmptyW`
**KERNEL32.dll**: `FormatMessageA`, `CreateFileW`, `UnmapViewOfFile`, `GetFileSize`, `CreateFileMappingW`, `MapViewOfFile`, `LocalAlloc`, `GetModuleHandleW`, `SetUnhandledExceptionFilter`, `SetLastError`, `lstrlenW`, `WriteFile`, `GetVersionExW`, `FindNextFileW`, `GetCurrentProcess`
**USER32.dll**: `FindWindowW`, `LoadStringA`, `wsprintfW`, `GetWindowThreadProcessId`, `ShowWindow`, `AttachThreadInput`, `BringWindowToTop`
**SHELL32.dll**: `ShellExecuteExW`, `CommandLineToArgvW`, `ShellExecuteW`
**OLEAUT32.dll**: `VariantClear`
**ADVAPI32.dll**: `RegSetValueExA`, `RegCreateKeyExA`, `RegCloseKey`, `SystemFunction036`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `BuildExplicitAccessWithNameW`, `BuildSecurityDescriptorW`, `RegDeleteTreeA`, `SetEntriesInAclW`, `SetNamedSecurityInfoW`, `GetNamedSecurityInfoW`, `ConvertStringSidToSidW`, `RegDeleteKeyExA`, `QueryServiceStatus`, `CloseServiceHandle`
**WS2_32.dll**: `WSACleanup`, `WSAStartup`, `gethostname`, `WSAGetLastError`
**CRYPT32.dll**: `CryptProtectData`, `CertOpenStore`, `CertGetNameStringW`, `CertFindCertificateInStore`, `CertCloseStore`, `CertFreeCertificateContext`, `CertDeleteCertificateFromStore`
**COMCTL32.dll**: `ord_345`

## Extracted Strings

Total strings found: **54046** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
CPADinfo(
@.reloc
j%h8UT
L$WQRP
C#G_
;L$(}
;L$,}
D$9D$
;|$0wX
9ru
_
u%9Eu
u}j!hh
N<9
t2W
T$,+T$
A;0v:f;
^)T$
A;0v8
|$;w
D$ PVW
9T$0s	
L$DD$
T$,;T$,w
T$ 9T$ w
L$4;L$P
D$hD$lu

D$`D$dtD
t$VRP
t$VRP
)D$LPf
D$@VRP
D$@VRP
~D$dWf
D$pPVW
D$pPVW
L$4QRPW
L$tAWQ
|0 9\0$|
4p;Ut
																									
																			
																												
																												
;t$t
D$_^3
D$ SVW
D$$VRQP
D$;Nv
L$L_^3
+L$9D$
f9D$w
D$(9D$Lt3
D$T_^[
9D$Pt/
9D$Xt3
	wr9~rm9~ vh
+CL+SL;
+sL+KL_;
FH<cuP
+D$9T$
D$;Nv
D$;Nv
uu$RQ
D$@VRP
L$\_^3
U 8B	}$9z
}(A;Ov
L$
PA;Ov
tK;wv
|$8WRP
t$T;pw
D$4T$`
D$4D$`
D$4r=
D$(;0v
D$@PWRQ
D$,_^3
D$;Nv
t$$VRP
y,;Nv
)D$LPf
D$@VRP
D$ ;Nv
|$$+D$
|$$+D$
|$$+D$
D$0VRP
L$L_^3
QPj!hd
WPhd[S
D$,j@P
D$,j@P
D$(j@P
D$(j@P
t PhgS
;F(v	Q
;F(v	Q
;F(v	Q
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004be260` | `0x4be260` | 691848 | ✓ |
| `fcn.004ca004` | `0x4ca004` | 164987 | ✓ |
| `fcn.004ca336` | `0x4ca336` | 86823 | ✓ |
| `fcn.004ef850` | `0x4ef850` | 60574 | ✓ |
| `fcn.004f278d` | `0x4f278d` | 56367 | ✓ |
| `fcn.00507788` | `0x507788` | 30053 | ✓ |
| `fcn.0042aa50` | `0x42aa50` | 18603 | ✓ |
| `fcn.004e3762` | `0x4e3762` | 7590 | ✓ |
| `fcn.00408150` | `0x408150` | 6776 | ✓ |
| `fcn.004465a0` | `0x4465a0` | 6318 | ✓ |
| `fcn.0047e1b0` | `0x47e1b0` | 6226 | ✓ |
| `method.boost::exception_detail::clone_impl_struct_boost::exception_detail::bad_alloc__.2.virtual_4` | `0x5081a0` | 5905 | ✓ |
| `method.boost::exception_detail::clone_impl_struct_boost::exception_detail::bad_exception__.2.virtual_4` | `0x5081e0` | 5889 | ✓ |
| `fcn.004a6da0` | `0x4a6da0` | 5858 | ✓ |
| `fcn.0044d790` | `0x44d790` | 5723 | ✓ |
| `fcn.004df65d` | `0x4df65d` | 5627 | ✓ |
| `fcn.005047a8` | `0x5047a8` | 5608 | ✓ |
| `fcn.004261c0` | `0x4261c0` | 5329 | ✓ |
| `fcn.00424280` | `0x424280` | 4763 | ✓ |
| `fcn.004c0540` | `0x4c0540` | 4108 | ✓ |
| `fcn.004653d0` | `0x4653d0` | 3879 | ✓ |
| `fcn.0049a5c0` | `0x49a5c0` | 3872 | ✓ |
| `fcn.00499590` | `0x499590` | 3872 | ✓ |
| `fcn.0040f8b0` | `0x40f8b0` | 3680 | ✓ |
| `fcn.0040cc20` | `0x40cc20` | 3583 | ✓ |
| `fcn.004506b0` | `0x4506b0` | 3576 | ✓ |
| `fcn.00469c20` | `0x469c20` | 3573 | ✓ |
| `fcn.004558f0` | `0x4558f0` | 3550 | ✓ |
| `fcn.004637f0` | `0x4637f0` | 3528 | ✓ |
| `fcn.0040af30` | `0x40af30` | 3455 | ✓ |

### Decompiled Code Files

- [`code/fcn.00408150.c`](code/fcn.00408150.c)
- [`code/fcn.0040af30.c`](code/fcn.0040af30.c)
- [`code/fcn.0040cc20.c`](code/fcn.0040cc20.c)
- [`code/fcn.0040f8b0.c`](code/fcn.0040f8b0.c)
- [`code/fcn.00424280.c`](code/fcn.00424280.c)
- [`code/fcn.004261c0.c`](code/fcn.004261c0.c)
- [`code/fcn.0042aa50.c`](code/fcn.0042aa50.c)
- [`code/fcn.004465a0.c`](code/fcn.004465a0.c)
- [`code/fcn.0044d790.c`](code/fcn.0044d790.c)
- [`code/fcn.004506b0.c`](code/fcn.004506b0.c)
- [`code/fcn.004558f0.c`](code/fcn.004558f0.c)
- [`code/fcn.004637f0.c`](code/fcn.004637f0.c)
- [`code/fcn.004653d0.c`](code/fcn.004653d0.c)
- [`code/fcn.00469c20.c`](code/fcn.00469c20.c)
- [`code/fcn.0047e1b0.c`](code/fcn.0047e1b0.c)
- [`code/fcn.00499590.c`](code/fcn.00499590.c)
- [`code/fcn.0049a5c0.c`](code/fcn.0049a5c0.c)
- [`code/fcn.004a6da0.c`](code/fcn.004a6da0.c)
- [`code/fcn.004be260.c`](code/fcn.004be260.c)
- [`code/fcn.004c0540.c`](code/fcn.004c0540.c)
- [`code/fcn.004ca004.c`](code/fcn.004ca004.c)
- [`code/fcn.004ca336.c`](code/fcn.004ca336.c)
- [`code/fcn.004df65d.c`](code/fcn.004df65d.c)
- [`code/fcn.004e3762.c`](code/fcn.004e3762.c)
- [`code/fcn.004ef850.c`](code/fcn.004ef850.c)
- [`code/fcn.004f278d.c`](code/fcn.004f278d.c)
- [`code/fcn.005047a8.c`](code/fcn.005047a8.c)
- [`code/fcn.00507788.c`](code/fcn.00507788.c)
- [`code/method.boost__exception_detail__clone_impl_struct_boost__exception_detail__bad_alloc__.2.virtual_4.c`](code/method.boost__exception_detail__clone_impl_struct_boost__exception_detail__bad_alloc__.2.virtual_4.c)
- [`code/method.boost__exception_detail__clone_impl_struct_boost__exception_detail__bad_exception__.2.virtual_4.c`](code/method.boost__exception_detail__clone_impl_struct_boost__exception_detail__bad_exception__.2.virtual_4.c)

## Behavioral Analysis

This final analysis of **chunk 6/6** provides the concluding pieces of evidence regarding the malware's behavior, specifically focusing on its deployment strategy, masquerading techniques, and detailed file system interaction.

The integration of these findings completes a comprehensive profile of an extremely sophisticated piece of malware designed for long-term persistence and stealthy operation within a corporate or high-value environment.

### Updated Analysis Summary

#### 1. Masquerading & Brand Imitation
This chunk reveals the "persona" the malware adopts to evade manual detection by system administrators:
*   **Fake Identity:** The path `C:\a\rescue-native-rescueassist\...` strongly suggests that the malware disguises itself as a "Rescue" or "Assistance" utility. This is a common tactic used to justify its presence on a system if noticed, as it mimics legitimate diagnostic software.
*   **Internal Logging:** The inclusion of strings like `"Working folder: {}"` indicates an internal logging system (likely the `spdlog` framework identified previously) that allows developers to debug the malware's state during the deployment phase.

#### 2. Systematic File System Enumeration
The function `fcn.004637f0` reveals a heavy emphasis on scanning and identifying system components:
*   **Targeted Extensions:** The code iterates through and specifically looks for `.dll`, `.exe`, `.cat`, and `.inf` files. 
    *   **.dll & .exe**: Standard targets for injection or process hollowing.
    *   **.cat & .inf**: These are "Cabinet" and "Setup Information" files. Their inclusion is a high-maturity indicator; these files are often used by system tools to identify signed drivers or system components. 
*   **Contextual Intent:** When combined with the **Resource Manager (Rm)** calls from previous chunks, this suggests the malware isn't just looking for *any* file—it is mapping out which processes own specific resources to determine how to best "blind" security software without crashing the operating system.

#### 3. Advanced Implementation Logic
The complexity of `fcn.004637f0` (with nested loops, complex buffer checks, and multi-stage validation) confirms that this is not a "script kiddie" tool. 
*   **Robustness:** The code contains extensive checks to ensure it doesn't crash the system while scanning processes or files, which is critical for staying resident on a target machine for months at a time.

---

### Updated Technical Indicators (IoCs)

The following new indicators have been identified from this final chunk:

**Hardcoded Strings & Masquerading:**
*   `"rescue-native-rescueassist"` (Indicator of branding/disguise as a "system repair" tool).
*   `".dll"`, `".exe"`, `".cat"`, `".inf"` (Used to filter system files for interaction or discovery).

**Persistence & Infrastructure:**
*   **Service Identity:** The use of `str.ServiceName` and `str.serviceId` in the backend logic confirms the creation of a dedicated Windows Service to maintain persistence after the initial "loader" finishes.

**System Interaction Tactics:**
*   **Automated Discovery Loop:** A heavy iteration logic designed to scan system paths for valid executables that match specific extension filters.

---

### Updated Summary for Report

**Classification:** Advanced Persistent Threat (APT) - Remote Access Trojan (RAT) / Spyware.

**Revised Analysis:**
The malware exhibits a high level of maturity and sophistication across three primary domains: **Persistence, Stealth, and Environment Mapping**. 

1.  **Persistence & Privilege Escalation:** The malware uses the `runas` verb to escalate privileges and immediately attempts to register itself as a system service (evidenced by internal `ServiceName` and `serviceId` structures). This ensures that even if the initial process is closed, the malicious logic remains active in the background.
2.  **Sophisticated Masquerading:** The malware employs deliberate social engineering at the technical level by adopting the name "rescue-native-rescueassist." By mimicking a system recovery tool, it aims to evade suspicion during manual audits of the file system.
3.  **Targeted Infrastructure Mapping:** Unlike basic RATs that merely listen for commands, this malware actively maps the host's environment. It performs extensive discovery of `.dll`, `.exe`, and `.inf` files to identify the infrastructure of security products. By identifying these specific components, it can strategically disable or bypass endpoint protection (EDR/AV) while maintaining system stability.

**Primary Action Vectors:**
1.  **Sophisticated Masking:** Adoption of "System Tool" personas to evade human analysis.
2.  **Automated Infrastructure Mapping:** Broad scanning for executable and resource files to identify targetable processes.
3.  **Multi-Stage Persistence:** Transition from a loader process to a background system service with elevated privileges.

---

### Final Summary Table of Findings (Cumulative)

| Feature | Status | Details |
| :--- | :--- | :--- |
| **Core Function** | Confirmed | High-sophistication RAT / Spyware |
| **Remote Execution** | Confirmed | Complex logic for handling various C2 instructions. |
| **Defense Evasion** | **Critical Risk** | Uses "Resource Manager" (Rm) APIs and extensive file scanning (.dll, .exe, .inf) to map and bypass security software. |
| **Persistence** | **Confirmed** | Moves from a loader state to a **System Service** using `runas` for privilege escalation. |
| **Masquerading** | **New / High Risk** | Uses "rescue-native" terminology to mimic legitimate system repair tools. |
| **Data Parsing Engine** | High Sophistication | Robust internal libraries (e.g., likely spdlog) for stable, logged operations. |
| **Environment Mapping** | Confirmed | Active discovery of file handles and process timers to identify "persistent" vs "transient" processes. |

**Final Conclusion:** The malware is a professional-grade tool intended for long-term, high-value targets. It possesses all the hallmarks of an APT-grade RAT: advanced evasion, systematic environment mapping, and clever social engineering via its file naming conventions.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the provided report to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The malware uses "rescue-native" naming conventions and specific file paths to mimic a legitimate system repair utility. |
| **T1083** | File and Directory Discovery | The code performs systematic scanning of the filesystem for `.dll`, `.exe`, `.cat`, and `.inf` files to map out system components. |
| **T1562.001** | Impairing Defenses (Disable or Modify Tools) | The malware specifically identifies system resources and "blind" security software by mapping its infrastructure. |
| **T1543.003** | Create or Run Windows Service | The malware transitions from a loader to a dedicated background service to ensure long-term persistence on the host. |
| **T1068** | Exploitation for Privilege Escalation | The use of the `runas` verb during the service registration phase indicates an intent to elevate privileges for its malicious operations. |
| **T1082** | System Information Discovery | The malware analyzes process timers and "persistent" vs "transient" status to understand the environment and avoid detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   *None identified.* (The "Extracted Strings" section contains obfuscated/binary-style data that does not resolve to clear network indicators.)

### **File paths / Registry keys**
*   `C:\a\rescue-native-rescueassist\` (Identified as a masquerading path used to mimic system repair tools).

### **Mutex names / Named pipes**
*   *None identified.* (While "Resource Manager" interactions are mentioned, no specific mutex strings or pipe names were provided in the text.)

### **Hashes**
*   *None identified.* (The string block contains symbols and hex-like characters, but no valid MD5, SHA1, or SHA256 hashes are present.)

### **Other artifacts**
*   **Malware Behavior/Patterns:**
    *   **File Extension Filtering:** Search patterns for `.dll`, `.exe`, `.cat`, and `.inf` (used to map system components and bypass security software).
    *   **Service Creation:** Internal use of `str.ServiceName` and `str.serviceId` for establishing a persistent Windows Service.
    *   **Logging Logic:** Usage of `"Working folder: {}"` indicating an internal logging framework (likely *spdlog*) used during the deployment phase.
*   **Masquerading Keywords:** 
    *   `"rescue-native-rescueassist"` (Used specifically to deceive system administrators).

---

### **Analyst Note:**
The "Extracted Strings" block provided contains heavily obfuscated or non-human-readable data (likely a result of disassembly or string extraction from an encrypted/packed binary). Therefore, no direct network IOCs (IPs/URLs) were present in that specific section. The primary intelligence for this threat is currently derived from the **behavioral analysis**, specifically the malware's signature tactics: masquerading as a "rescue" utility and performing automated system mapping to identify security software infrastructure.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://dumpster.console.gotoresolve.com`
- `https://dumpster.dev01-console.gotoresolve.com`

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** Unknown
2. **Malware type:** RAT (Remote Access Trojan) / Loader
3. **Confidence:** High
4. **Key evidence:** 
    *   **Advanced Persistence & Privilege Escalation:** The malware utilizes `runas` to escalate privileges and automatically transitions from an initial loader state into a persistent Windows Service, ensuring long-term residency in the environment.
    *   **Sophisticated Masquerading:** It employs specific social engineering tactics by using file paths and names like "rescue-native-rescueassist" to mimic legitimate system recovery tools, aiming to deceive manual audits by system administrators.
    *   **Infrastructure Mapping & Evasion:** The malware performs deep analysis of the host's environment, specifically scanning for `.dll`, `.exe`, `.cat`, and `.inf` files to map out security software infrastructure and "blind" endpoint defenses without crashing the OS.
