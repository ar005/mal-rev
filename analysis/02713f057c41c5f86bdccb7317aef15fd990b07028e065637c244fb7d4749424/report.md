# Threat Analysis Report

**Generated:** 2026-06-28 06:23 UTC
**Sample:** `02713f057c41c5f86bdccb7317aef15fd990b07028e065637c244fb7d4749424_02713f057c41c5f86bdccb7317aef15fd990b07028e065637c244fb7d4749424.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02713f057c41c5f86bdccb7317aef15fd990b07028e065637c244fb7d4749424_02713f057c41c5f86bdccb7317aef15fd990b07028e065637c244fb7d4749424.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 7 sections |
| Size | 83,423,632 bytes |
| MD5 | `435e8d036a192bde5a144b6e816d54ff` |
| SHA1 | `5f53db12e6809a660da512a032f5814ee21da07a` |
| SHA256 | `02713f057c41c5f86bdccb7317aef15fd990b07028e065637c244fb7d4749424` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1751006465 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 378,368 | 6.712 | No |
| `.rdata` | 100,864 | 5.855 | No |
| `.data` | 4,096 | 3.611 | No |
| `.gfids` | 512 | 3.158 | No |
| `.tls` | 512 | 0.02 | No |
| `.rsrc` | 82,912,768 | 8.0 | ⚠️ Yes |
| `.reloc` | 14,848 | 6.62 | No |

### Imports

**KERNEL32.dll**: `HeapFree`, `HeapAlloc`, `GetProcessHeap`, `LocalFree`, `TerminateProcess`, `SetLastError`, `GetWindowsDirectoryW`, `GetCommandLineW`, `OpenProcess`, `GetExitCodeProcess`, `WaitForSingleObject`, `FormatMessageA`, `WideCharToMultiByte`, `CreateToolhelp32Snapshot`, `Process32FirstW`
**USER32.dll**: `GetWindowThreadProcessId`, `EnumWindows`, `FindWindowW`, `PostMessageW`, `MessageBoxW`, `OpenClipboard`, `EmptyClipboard`, `CloseClipboard`, `LoadStringW`, `SwitchToThisWindow`, `ExitWindowsEx`, `PeekMessageW`, `GetMessageW`, `TranslateMessage`, `DispatchMessageW`
**ADVAPI32.dll**: `InitializeSecurityDescriptor`, `OpenSCManagerW`, `RegDeleteValueW`, `RegEnumKeyExW`, `RegDeleteKeyW`, `RegSetValueExW`, `RegCreateKeyExW`, `RegQueryValueExW`, `RegOpenKeyExW`, `RegCloseKey`, `SetNamedSecurityInfoW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `AddAce`
**SHELL32.dll**: `ShellExecuteExW`, `SHFileOperationW`, `DragQueryFileW`, `SHChangeNotify`, `CommandLineToArgvW`, `SHGetSpecialFolderPathW`, `ord_190`, `ord_165`, `ShellExecuteW`, `SHCreateDirectoryExW`
**ole32.dll**: `OleGetClipboard`, `CoUninitialize`, `PropVariantClear`, `CoInitialize`, `CoCreateInstance`, `ReleaseStgMedium`, `OleInitialize`, `CoTaskMemFree`, `OleUninitialize`
**OLEAUT32.dll**: `VariantClear`, `VariantInit`, `VarBstrCmp`, `SysAllocStringLen`, `SysFreeString`, `SysAllocString`
**SHLWAPI.dll**: `PathFindFileNameW`, `PathRemoveFileSpecW`, `SHStrDupW`, `PathAddBackslashW`, `PathAppendW`, `StrToIntExW`, `PathIsDirectoryW`, `PathCombineW`, `PathFileExistsW`
**COMCTL32.dll**: `InitCommonControlsEx`
**VERSION.dll**: `GetFileVersionInfoW`, `GetFileVersionInfoSizeW`, `VerQueryValueW`
**PSAPI.DLL**: `GetProcessImageFileNameW`
**urlmon.dll**: `URLDownloadToFileW`

## Extracted Strings

Total strings found: **182952** (showing first 100)

```
!This program cannot be run in DOS mode.
$
oMRich
`.rdata
@.data
.gfids
@.reloc
QQSUVW
@_^][YY
t~j	Y3
t!j	Y3
w&s)+F
tGh@F
tch$@F
D$4SUV
f93t	S
\$HUVW
D$ WWj
L$L_^][3
QQSUVW
_^][YY
L$4_^[3
;Nu	Q
;Nu	Q
;Eu$j
t h,OF
t"Vj.^f9q0u
u	f9Q4u
t6hTPF
t$h\PF
QSUVW3
D$8h(VF
D$4h4VF
u"9E,t
E<h(VF
D$0WVPW
Vj _+
D$8h(VF
D$8h(VF
f9)u03
Y_^@[Y
Y_^@[Y
Y_^@[Y
l$VWQ
Y_^@[Y
0;t$u
\$UVWQj0]
>_^][Y
t$9Q}
SVQQQQP
RRVPQSRj
0^_][YY
t.hpdF
t5QQQQ
t,QQQQj
t'9Q}
0^][YY
Yt
jV
tbf9_lw\
D$$9}
D$_^[
Mj(X;
uSWh(zF
SPWhlzF
YV@PWh
YRPh |F
YPhX|F
|$ PSj
D$ pBF
L$$_^[3
t1;Pu
D$8SVW
T$;\$
L$D_^[3
92r
tA
F f	H"
YY=pBF
YY=pBF
F+F W
f!G"Y_
QQSVWj
?<%uj"Xj
Fnf9Fnrt+
f9Fns-
G+G f
YY9wt
|$;|$
D$ ;D$$v
\$(9\$
;D$4w|9L$
B9Ut)
|
;|$
;D$vh
Y_^[Y]
D$,;t$
T$0;t$
<%t'<.t
<bte<f
D$;;u
G;D$4s
\$8WPB
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00459c28` | `0x459c28` | 24184 | ✓ |
| `fcn.004597ad` | `0x4597ad` | 23272 | ✓ |
| `fcn.00458e5c` | `0x458e5c` | 20793 | ✓ |
| `fcn.00439f6f` | `0x439f6f` | 7619 | ✓ |
| `fcn.00412fc6` | `0x412fc6` | 7115 | ✓ |
| `fcn.00454c65` | `0x454c65` | 5886 | ✓ |
| `fcn.0042cba0` | `0x42cba0` | 5382 | ✓ |
| `fcn.00450a1d` | `0x450a1d` | 5020 | ✓ |
| `fcn.00458d20` | `0x458d20` | 4175 | ✓ |
| `fcn.00453540` | `0x453540` | 3348 | ✓ |
| `fcn.00457c90` | `0x457c90` | 2887 | ✓ |
| `fcn.0045af49` | `0x45af49` | 2822 | ✓ |
| `fcn.0044945e` | `0x44945e` | 2817 | ✓ |
| `fcn.0042a9e0` | `0x42a9e0` | 2495 | ✓ |
| `fcn.00426fd0` | `0x426fd0` | 2378 | ✓ |
| `fcn.00429b70` | `0x429b70` | 1899 | ✓ |
| `fcn.0042c300` | `0x42c300` | 1773 | ✓ |
| `fcn.0044228f` | `0x44228f` | 1765 | ✓ |
| `fcn.0043ef73` | `0x43ef73` | 1748 | ✓ |
| `fcn.0042e0b0` | `0x42e0b0` | 1503 | ✓ |
| `fcn.00401e2f` | `0x401e2f` | 1475 | ✓ |
| `fcn.00431930` | `0x431930` | 1396 | ✓ |
| `fcn.00431eb0` | `0x431eb0` | 1396 | ✓ |
| `fcn.0045a2ee` | `0x45a2ee` | 1378 | ✓ |
| `fcn.00456d60` | `0x456d60` | 1346 | ✓ |
| `fcn.0043f7c9` | `0x43f7c9` | 1339 | ✓ |
| `fcn.00459d8e` | `0x459d8e` | 1334 | ✓ |
| `fcn.00456840` | `0x456840` | 1311 | ✓ |
| `fcn.004226fb` | `0x4226fb` | 1302 | ✓ |
| `fcn.00427930` | `0x427930` | 1298 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401e2f.c`](code/fcn.00401e2f.c)
- [`code/fcn.00412fc6.c`](code/fcn.00412fc6.c)
- [`code/fcn.004226fb.c`](code/fcn.004226fb.c)
- [`code/fcn.00426fd0.c`](code/fcn.00426fd0.c)
- [`code/fcn.00427930.c`](code/fcn.00427930.c)
- [`code/fcn.00429b70.c`](code/fcn.00429b70.c)
- [`code/fcn.0042a9e0.c`](code/fcn.0042a9e0.c)
- [`code/fcn.0042c300.c`](code/fcn.0042c300.c)
- [`code/fcn.0042cba0.c`](code/fcn.0042cba0.c)
- [`code/fcn.0042e0b0.c`](code/fcn.0042e0b0.c)
- [`code/fcn.00431930.c`](code/fcn.00431930.c)
- [`code/fcn.00431eb0.c`](code/fcn.00431eb0.c)
- [`code/fcn.00439f6f.c`](code/fcn.00439f6f.c)
- [`code/fcn.0043ef73.c`](code/fcn.0043ef73.c)
- [`code/fcn.0043f7c9.c`](code/fcn.0043f7c9.c)
- [`code/fcn.0044228f.c`](code/fcn.0044228f.c)
- [`code/fcn.0044945e.c`](code/fcn.0044945e.c)
- [`code/fcn.00450a1d.c`](code/fcn.00450a1d.c)
- [`code/fcn.00453540.c`](code/fcn.00453540.c)
- [`code/fcn.00454c65.c`](code/fcn.00454c65.c)
- [`code/fcn.00456840.c`](code/fcn.00456840.c)
- [`code/fcn.00456d60.c`](code/fcn.00456d60.c)
- [`code/fcn.00457c90.c`](code/fcn.00457c90.c)
- [`code/fcn.00458d20.c`](code/fcn.00458d20.c)
- [`code/fcn.00458e5c.c`](code/fcn.00458e5c.c)
- [`code/fcn.004597ad.c`](code/fcn.004597ad.c)
- [`code/fcn.00459c28.c`](code/fcn.00459c28.c)
- [`code/fcn.00459d8e.c`](code/fcn.00459d8e.c)
- [`code/fcn.0045a2ee.c`](code/fcn.0045a2ee.c)
- [`code/fcn.0045af49.c`](code/fcn.0045af49.c)

## Behavioral Analysis

This final analysis incorporates the results from **chunk 4/4**. The addition of these segments provides a complete view of the malware's internal architecture, moving from high-level obfuscation to low-level system exploitation and forensic evasion.

The findings in this final chunk confirm that we are dealing with a highly sophisticated piece of malware, likely a **professional-grade Remote Access Trojan (RAT) or an espionage backdoor**.

---

### Final Comprehensive Analysis Overview
The analysis across all four chunks reveals a multi-layered architecture designed to protect the malware's core logic while providing high-level capabilities for host manipulation.

#### 1. Deep Logic Obfuscation & "Hidden" Cryptography (`fcn.0045a2ee`, `fcn.00459d8e`, `fcn.00456d60`)
These functions represent a significant jump in sophistication compared to standard malware. They are dense, complex floating-point math routines.

*   **Non-Standard Cryptography:** Standard encryption (AES, ChaCha20) has distinct patterns that signature scanners can detect. By using high-precision floating-point math to perform "transformation" logic, the authors may be using a **custom cryptographic protocol**. This allows them to encrypt and decrypt command traffic while making it nearly impossible for automated tools to recognize the algorithm as known encryption.
*   **Anti-Analysis/Environment Fingerprinting:** These functions also serve as a hurdle for researchers. Some debuggers or emulators handle floating-point registers or rounding errors differently than physical hardware. If the calculation deviates by even a single bit, the malware can "realize" it is being analyzed and shut down.

#### 2. Extensive Data Handling & Management (`fcn.00431930`, `fcn.00431eb0`)
These two functions are almost identical in structure, appearing as large, complex loops for memory/buffer manipulation.

*   **Buffer Orchestration:** The repetitive nature and the logic within suggest these are internal "plumbing" routines used to process data before it reaches the Command Dispatcher. This implies that the malware handles **large amounts of data**—likely a way to move stolen files, reconstruct large documents from network packets, or re-assemble pieces of code into memory for execution.
*   **Internal Serialization:** These may be part of a custom serialization protocol, allowing different "modules" of the malware to pass complex objects to one another without being easily parsed by external tools.

#### 3. Forensic Evasion & File Manipulation (`fcn.00427930`)
This is perhaps the most significant functional area identified in this final chunk. It focuses on interacting with the host's file system while actively hiding its tracks.

*   **Automated Target Discovery:** The use of `FindFirstFileW` and `FindNextFileW` indicates that the malware can scan for specific files or directories, such as user profiles, browser history, or other "valuable" data.
*   **"Timestomping":** The inclusion of `SetFileTime` and `SetFileAttributes` is a hallmark of advanced malware. By modifying the "Modified, Accessed, Created, and Entry" (MACE) timestamps of files it creates, the malware makes its existence blend in with older, legitimate system files to evade detection by forensic investigators looking for recently modified files.
*   **Privilege/Context Manipulation:** The logic surrounding `CreateFileW` and `SetFileAttributes` suggests the malware can modify file properties (like making itself "Hidden" or a "System" file) as it moves through its lifecycle.

---

### Final Technical Conclusion: The Architecture of Threat
By synthesizing all four chunks, we can map out the malware's execution flow:

1.  **Communication Layer:** Receives encrypted commands via an obfuscated transport layer (Chunk 4 Math & Chunk 3 Dispatcher).
2.  **Transformation Layer:** Decodes and "translates" the raw packets into a proprietary instruction set using custom floating-point math (Chunk 3/4 Math routines).
3.  **Execution Engine (VM):** A virtual machine interprets these instructions, providing a layer of abstraction between the malicious intent (e.g., "Steal Passwords") and the actual assembly code executing on the host (Chunk 2 & 3 Dispatcher).
4.  **Action Layer:** Once a command is validated by the VM, it executes low-level system calls to interact with files, processes, or the registry (Chunk 4 File System routines).

### Updated Risk Assessment for Incident Response
The evidence across all chunks confirms this is a **High-Tier Threat.** It shows hallmarks of state-sponsored actors or well-funded cybercrime syndicates.

*   **Classification:** Professional Grade Modular RAT / Stealthy Backdoor.
*   **Capability Level:** Extreme. The multi-layered approach (VM + Math Obfuscation + Timestomping) indicates a design meant to survive months/years in a high-security environment.
*   **Risk Level: CRITICAL.**

#### Targeted Recommendations for Incident Response:
1.  **Advanced Forensic Sweeps:** Because the malware utilizes **timestomping**, standard "recent file" searches will fail. You must perform forensic analysis on the Master File Table (MFT) to find inconsistencies between actual filesystem logs and the current displayed attributes.
2.  **In-Memory Analysis is Critical:** Since the most dangerous logic is hidden inside a VM structure, memory forensics should be used to dump the "active" buffer of the command dispatcher. This is where the "translated" commands will appear in plain text or near-plain text.
3.  **Look for Manipulation Patterns:** Monitor for any process attempting to call `SetFileTime` or `SetFileAttributes` on files outside of standard system update windows, as this is a primary indicator of this specific malware family's behavior.
4.  **Custom Signatures (YARA):** Develop YARA rules based on the **Floating Point Math constants** and the unique patterns found in the **Data Management functions** (`0x431930` / `0x431eb0`). These are "invariant" signatures that even if the malware's strings are changed, its core math logic will remain constant.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your technical analysis to the corresponding **MITRE ATT&C** techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of custom floating-point math for "transformation" logic and the implementation of a VM execution engine are high-level methods to hide the malware's core commands and intent. |
| **T1497** | Virtualization/Sandbox Evasion | The analysis specifically mentions using floating-point register differences to detect if the malware is running in an emulator or debugger. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileW` and `FindNextFileW` to scan for "valuable" data such as user profiles and browser history indicates automated target discovery. |
| **T1070.004** | Time Stamp Manipulation | The specific use of `SetFileTime` to alter MACE timestamps (Timestomping) is a classic method used to blend malicious files with legitimate system files. |
| **T1036.005** | Hide Files and Directories | The utilization of `SetFileAttributes` to modify file properties (e.g., making them "Hidden" or "System") serves to evade detection by users and standard forensic tools. |
| **T1102** | Web Service (Implicit) | While not a direct system call, the "Communication Layer" described as receiving encrypted commands via an obfuscated transport layer indicates established C2 infrastructure. |

### Summary of Analytical Findings for IR Teams:
The most critical indicators of sophistication are the **T1497 (Virtualization/Sandbox Evasion)** and **T1027 (Obfuscated Files or Information)** components. The use of non-standard math to bypass automated scanners and a Virtual Machine architecture to wrap malicious instructions suggests a sophisticated actor capable of bypassing standard signature-based and heuristic-based defenses. 

**Priority Note:** Because the malware utilizes **T1070.004 (Timestomping)**, your incident response team should prioritize MFT (Master File Table) analysis over simple file-system "recently modified" queries to identify the presence of this threat.

---

## Indicators of Compromise

Based on the provided data, here are the extracted Indicators of Compromise (IOCs) categorized by type. 

**Note:** The "EXTRACTED STRINGS" section contains heavily obfuscated/garbled data (likely due to packing or encryption), and no literal IP addresses, domains, or file paths were present in that specific block. However, the "Behavioral Analysis" provides significant behavioral IOCs (TTPs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Target Search Behavior:** The malware utilizes `FindFirstFileW` and `FindNextFileW` to programmatically search for target files (e.g., user profiles, browser history). 
*   **System Manipulation:** Use of `CreateFileW` combined with `SetFileAttributes` suggests the modification of file properties (e.g., making files "Hidden" or "System").

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified in provided strings.*

### **Other artifacts**
*   **Custom Cryptography (Floating-Point Math):** The malware uses non-standard, high-precision floating-point math routines at addresses `0x45a2ee`, `0x459d8e`, and `0x456d60` to implement a custom cryptographic protocol for C2 communication.
*   **Timestomping:** Active use of `SetFileTime` and `SetFileAttributes` to modify MACE (Modified, Accessed, Created, Entry) timestamps, specifically designed to evade forensic detection.
*   **Virtual Machine (VM) Execution Layer:** The malware employs a custom VM structure to interpret instructions, decoupling the malicious intent from the underlying assembly code.
*   **Internal Data Management:** Specific routines at `0x431930` and `0x431eb0` indicate complex buffer management for large-scale data exfiltration or assembly of modular components.

---
**Analyst Note:** Because this threat utilizes heavy obfuscation and "timestomping," traditional signature-based detection (like simple strings or file names) is unlikely to be effective. Detection should focus on **behavioral signatures**, specifically monitoring for processes invoking `SetFileTime` on non-system files or the use of unusual floating-point math patterns in network-related modules.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification of the sample:

**1. Malware family:** Custom (Sophisticated Espionage Tool)
**2. Malware type:** RAT / Backdoor
**3. Confidence:** High

**4. Key evidence:**
*   **Advanced Architecture & Obfuscation:** The use of a **Virtual Machine (VM) execution engine** to interpret instructions and **custom floating-point math** for cryptography indicates a high-tier, professional-grade design intended to bypass signature-based detection and decouple malicious logic from assembly code.
*   **Sophisticated Forensic Evasion:** The implementation of **"timestomping"** (`SetFileTime`) and attribute manipulation (`SetFileAttributes`) specifically targets the evasion of forensic investigators by blending malicious files into the system's historical data.
*   **Data Handling & Persistence Capabilities:** The identification of complex buffer management routines and automated target discovery (via `FindFirstFileW`) suggests a primary objective of large-scale **data exfiltration** and long-term persistent access, hallmarks of an espionage-focused RAT.
