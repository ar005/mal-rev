# Threat Analysis Report

**Generated:** 2026-08-23 06:20 UTC
**Sample:** `1144433760a0683413a85da271bc37ff9f296ac287e722825f27577b529b9d27_1144433760a0683413a85da271bc37ff9f296ac287e722825f27577b529b9d27.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1144433760a0683413a85da271bc37ff9f296ac287e722825f27577b529b9d27_1144433760a0683413a85da271bc37ff9f296ac287e722825f27577b529b9d27.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 6 sections |
| Size | 1,015,296 bytes |
| MD5 | `8e8319ef77aa12f2335b339abf0ddadb` |
| SHA1 | `7e0e21949852a56e1179302ecef5898086aef80a` |
| SHA256 | `1144433760a0683413a85da271bc37ff9f296ac287e722825f27577b529b9d27` |
| Overall entropy | 7.67 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773360087 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 145,408 | 6.581 | No |
| `.rdata` | 60,928 | 5.305 | No |
| `.data` | 4,608 | 3.508 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 794,112 | 7.819 | ⚠️ Yes |
| `.reloc` | 8,704 | 6.426 | No |

### Imports

**KERNEL32.dll**: `GetTempPathW`, `WaitForSingleObject`, `Sleep`, `GetLastError`, `LockResource`, `CloseHandle`, `LoadResource`, `GetModuleFileNameW`, `CreateProcessW`, `GetModuleHandleW`, `WideCharToMultiByte`, `GetConsoleWindow`, `IsDebuggerPresent`, `SetEndOfFile`, `WriteConsoleW`
**USER32.dll**: `ShowWindow`
**ADVAPI32.dll**: `RegCreateKeyExW`, `RegSetValueExW`, `RegCloseKey`
**ole32.dll**: `CoUninitialize`, `CoTaskMemFree`, `CoCreateGuid`, `StringFromCLSID`, `CoInitialize`
**ntdll.dll**: `NtQueryInformationProcess`
**WS2_32.dll**: `connect`, `getaddrinfo`, `send`, `setsockopt`, `closesocket`, `WSACleanup`, `freeaddrinfo`, `socket`, `WSAStartup`, `recv`

### Exports

`CreatePlugin`, `GetHandleVerifier`, `GetPluginEffects`, `HostMainLoop`, `RunDLL`, `sqlite3_aggregate_context`, `sqlite3_aggregate_count`, `sqlite3_auto_extension`, `sqlite3_backup_finish`, `sqlite3_backup_init`, `sqlite3_backup_pagecount`, `sqlite3_backup_remaining`, `sqlite3_backup_step`, `sqlite3_bind_blob`, `sqlite3_bind_blob64`, `sqlite3_bind_double`, `sqlite3_bind_int`, `sqlite3_bind_int64`, `sqlite3_bind_null`, `sqlite3_bind_parameter_count`, `sqlite3_bind_parameter_index`, `sqlite3_bind_parameter_name`, `sqlite3_bind_text`, `sqlite3_bind_text16`, `sqlite3_bind_text64`, `sqlite3_bind_value`, `sqlite3_bind_zeroblob`, `sqlite3_bind_zeroblob64`, `sqlite3_blob_bytes`, `sqlite3_blob_close`, `sqlite3_blob_open`, `sqlite3_blob_read`, `sqlite3_blob_reopen`, `sqlite3_blob_write`, `sqlite3_busy_handler`, `sqlite3_busy_timeout`, `sqlite3_cancel_auto_extension`, `sqlite3_changes`, `sqlite3_clear_bindings`, `sqlite3_close`, `sqlite3_close_v2`, `sqlite3_collation_needed`, `sqlite3_collation_needed16`, `sqlite3_column_blob`, `sqlite3_column_bytes`, `sqlite3_column_bytes16`, `sqlite3_column_count`, `sqlite3_column_database_name`, `sqlite3_column_database_name16`, `sqlite3_column_decltype`

## Extracted Strings

Total strings found: **3060** (showing first 100)

```
!This program cannot be run in DOS mode.
$
RichIL
`.rdata
@.data
.fptable
@.reloc
B;0v>f
E+D$
N<9
t2W
t8 9\8$|
Yt
jV
tC97u?j4
uBA;S
PPPPPWS
J9Mr

D$+d$SVW
D$+d$SVW
D$+d$SVW
5ntel
5Genu
QQSVWd
F;Btt
38_^]
E9xt
&9Gv!8E
9~v@k
URPQQh 
kUQPXY]Y[
PVVVVV
PVVVVV
PPPPPPPP
]t-;u
ARPRQh
u9~uj
};GvP
u9^u
uSSSSj
};GvP
< t1<	t-
t	iud
9>tWV
SWt@jU
j.Xf9E
_tnPVj@
uj;Xf9
tG;}r

u9jXWf

u	jZf
PVVVVV
VPPPPP
u Vh0^
PWWWWW
;EuK;U
j
^f93u
sAj
[f9
D8(HXtIf
j
Xf9E
D8(Ht5F
j
_f9;u
PVVVVV
[PVVVVV
j"[WVVVV
PVVVVV
+ERSP
_PSSSSS
j"_VSSSS
WVVVVV
VSRSQV
GVSRj
Swntd+
PP9E u#PPSWP
u9^uj
};GvP
</t
<\t
SSSPSQ
];3t'
f9:t!V
;ut.;
QQSVj8j@
C PjPW
C$PjQW
C*PjTW
C+PjUW
C,PjVW
C-PjWW
C.PjRW
C/PjSW
CHPjPW
CLPjQW
NX9F`t1
j	PjYV
u2Vj@hh
9C`u99C\t4
u29K\t-
E E$j
PPPPPPPP
bad allocation
success
address family not supported
address in use
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.100091f1` | `0x100091f1` | 35014 | ✓ |
| `fcn.1000b79d` | `0x1000b79d` | 17268 | ✓ |
| `fcn.100096f1` | `0x100096f1` | 13783 | ✓ |
| `fcn.1000b7c0` | `0x1000b7c0` | 11295 | ✓ |
| `fcn.1000ce2a` | `0x1000ce2a` | 4929 | ✓ |
| `fcn.100229a8` | `0x100229a8` | 2477 | ✓ |
| `fcn.100027c0` | `0x100027c0` | 2148 | ✓ |
| `fcn.1000c740` | `0x1000c740` | 1396 | ✓ |
| `fcn.10014073` | `0x10014073` | 1371 | ✓ |
| `fcn.10003740` | `0x10003740` | 1369 | ✓ |
| `fcn.100030d0` | `0x100030d0` | 1293 | ✓ |
| `fcn.10021790` | `0x10021790` | 1053 | ✓ |
| `fcn.10005620` | `0x10005620` | 1046 | ✓ |
| `fcn.100173eb` | `0x100173eb` | 1015 | ✓ |
| `fcn.10015727` | `0x10015727` | 982 | ✓ |
| `fcn.1001605a` | `0x1001605a` | 955 | ✓ |
| `fcn.1000e809` | `0x1000e809` | 931 | ✓ |
| `fcn.1001a621` | `0x1001a621` | 922 | ✓ |
| `fcn.10021367` | `0x10021367` | 820 | ✓ |
| `fcn.10019780` | `0x10019780` | 809 | ✓ |
| `fcn.1000ba6e` | `0x1000ba6e` | 794 | ✓ |
| `fcn.10015d6a` | `0x10015d6a` | 752 | ✓ |
| `fcn.10003f50` | `0x10003f50` | 705 | ✓ |
| `fcn.1001b131` | `0x1001b131` | 673 | ✓ |
| `fcn.100043f0` | `0x100043f0` | 669 | ✓ |
| `fcn.1001cb76` | `0x1001cb76` | 652 | ✓ |
| `fcn.100048b0` | `0x100048b0` | 643 | ✓ |
| `fcn.1001b410` | `0x1001b410` | 639 | ✓ |
| `fcn.1001e9f6` | `0x1001e9f6` | 639 | ✓ |
| `method.std::basic_filebuf_char__struct_std::char_traits_char__.virtual_28` | `0x10006170` | 621 | ✓ |

### Decompiled Code Files

- [`code/fcn.100027c0.c`](code/fcn.100027c0.c)
- [`code/fcn.100030d0.c`](code/fcn.100030d0.c)
- [`code/fcn.10003740.c`](code/fcn.10003740.c)
- [`code/fcn.10003f50.c`](code/fcn.10003f50.c)
- [`code/fcn.100043f0.c`](code/fcn.100043f0.c)
- [`code/fcn.100048b0.c`](code/fcn.100048b0.c)
- [`code/fcn.10005620.c`](code/fcn.10005620.c)
- [`code/fcn.100091f1.c`](code/fcn.100091f1.c)
- [`code/fcn.100096f1.c`](code/fcn.100096f1.c)
- [`code/fcn.1000b79d.c`](code/fcn.1000b79d.c)
- [`code/fcn.1000b7c0.c`](code/fcn.1000b7c0.c)
- [`code/fcn.1000ba6e.c`](code/fcn.1000ba6e.c)
- [`code/fcn.1000c740.c`](code/fcn.1000c740.c)
- [`code/fcn.1000ce2a.c`](code/fcn.1000ce2a.c)
- [`code/fcn.1000e809.c`](code/fcn.1000e809.c)
- [`code/fcn.10014073.c`](code/fcn.10014073.c)
- [`code/fcn.10015727.c`](code/fcn.10015727.c)
- [`code/fcn.10015d6a.c`](code/fcn.10015d6a.c)
- [`code/fcn.1001605a.c`](code/fcn.1001605a.c)
- [`code/fcn.100173eb.c`](code/fcn.100173eb.c)
- [`code/fcn.10019780.c`](code/fcn.10019780.c)
- [`code/fcn.1001a621.c`](code/fcn.1001a621.c)
- [`code/fcn.1001b131.c`](code/fcn.1001b131.c)
- [`code/fcn.1001b410.c`](code/fcn.1001b410.c)
- [`code/fcn.1001cb76.c`](code/fcn.1001cb76.c)
- [`code/fcn.1001e9f6.c`](code/fcn.1001e9f6.c)
- [`code/fcn.10021367.c`](code/fcn.10021367.c)
- [`code/fcn.10021790.c`](code/fcn.10021790.c)
- [`code/fcn.100229a8.c`](code/fcn.100229a8.c)
- [`code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_28.c`](code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_28.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and extended the analysis of the binary. The new data confirms several sophisticated behaviors that reinforce the classification of this file as a high-capability **malware agent (trojan/downloader)**.

### Updated Analysis Summary
The second portion of the disassembly reveals advanced capabilities in **anti-analysis (VM evasion), complex command parsing, and robust string/path manipulation.** The code is not just moving data; it is processing highly structured commands and checking the environment to ensure it isn't being monitored by security researchers.

---

### New Suspicious Behaviors & Advanced Techniques

#### 1. Anti-Analysis / Environment Fingerprinting
*   **Function `fcn.1000ba6e`**: This function is a strong indicator of **anti-VM or anti-debugging behavior**. 
    *   It uses the `GetProcessorFeaturePresent` and `cpuid` instructions to query hardware capabilities.
    *   It specifically checks for "GenuineIntel" strings and specific CPU features (like those used in virtualization).
    *   **Significance:** Malware authors use these checks to detect if it is running inside a virtual machine (e.g., VMware, VirtualBox) or a sandboxed environment. If the environment is deemed "safe" (i.e., not a sandbox), the malware proceeds; otherwise, it may cease operations to avoid detection.

#### 2. Complex Command Parsing & Protocol Decoding
*   **Function `fcn.1001b410`**: This is an intricate **parsing engine**. It iterates through strings and uses various logic branches based on specific character values (e.g., checking for 'a', 'r', 'w', etc.) and potentially handling escaped characters or special symbols like `%`.
*   **Function `fcn.10021790`**: This long routine handles complex **buffer manipulations**. It appears to be a robust way of building strings or constructing memory blocks from segments received over the network.
*   **Significance:** These functions suggest that the binary receives non-trivial commands from its Command & Control (C2) server. Instead of simple "on/off" commands, it likely parses complex instructions for file paths, system queries, or multi-step injection routines.

#### 3. Advanced File System Interaction
*   **Function `fcn.1001cb76`**: This function performs **path normalization**. It handles different slash types (`/`, `\`) and converts relative paths to absolute ones.
*   **Function `fcn.10021367`**: This involves **file handle management** and checking file types (e.g., via `GetFileType`). 
*   **Significance:** These capabilities suggest the malware is designed to navigate the local filesystem effectively, potentially looking for specific files to exfiltrate or preparing paths for downloading and "dropping" secondary payloads.

#### 4. Advanced String/Data Processing
*   **Functions `fcn.10015727` and `fcn.10015d6a`**: These functions appear to be part of a high-level library (likely **C++ Standard Library**) for handling "wide" strings (`wchar_t`) and large buffer extractions.
*   **Function `fcn.10019780`**: This performs complex logic involving bitwise operations and adjustments on values that could be used for **checksumming, encryption parameters, or internal state tracking**.

---

### Updated Summary Table of Evidence

| Feature | Function(s) | Significance |
| :--- | :--- | :--- |
| **Anti-Analysis / VM Evasion** | `fcn.1000ba6e` | Detects if the software is running in a sandbox/VM; used to hide from researchers. |
| **C2 Command Parsing** | `fcn.1001b410`, `fcn.10021790` | Decodes complex instructions sent by a remote server into actionable tasks. |
| **File System Manipulation** | `fcn.1001cb76`, `fcn.10021367` | Normalizes paths and handles files; essential for dropping payloads or exfiltration. |
| **Robust Data Handling** | `fcn.10015727`, `fcn.1001e9f6` | Uses complex logic to manage large buffers/strings, typical of a "mature" malware project. |
| **Network Interaction** | `fcn.100027c0` (from chunk 1) | Established communication with remote servers. |
| **Persistence / Execution** | `fcn.10003740` (from chunk 1) | Registry manipulation and secondary process launching. |

---

### Conclusion of Analysis
The inclusion of **anti-VM checks**, **complex command parsing**, and **sophisticated string/path management** confirms that this binary is a high-quality piece of malware. It is likely a **module or "dropper"** designed to:
1.  Verify the environment isn't being analyzed (Anti-Analysis).
2.  Connect to a C2 server to receive and parse complex commands (Command & Control).
3.  Navigate the local filesystem to deposit payloads or steal data (Data Exfiltration/Persistence).

The use of structured code (likely C++) suggests this is part of a professional malware "framework" rather than a simple standalone script.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the identified functionalities to the MITRE ATT&CK framework.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Evasion | The use of `GetProcessorFeaturePresent` and `cpuid` to check for "GenuineIntel" strings is a classic method to determine if the malware is running in an analysis environment. |
| **T1030** | Data Obfuscation | The complex parsing engines (`fcn.1001b410`) and bitwise operations (`fcn.10019780`) indicate the decoding of obfuscated C2 instructions and internal state tracking. |
| **T1083** | File and Directory Discovery | Function `fcn.1001cb76` (path normalization) and `fcn.10021367` (file type checking) indicate the malware is actively mapping/navigating the filesystem to locate targets or drop payloads. |
| **T1071** | Application Layer Protocol | The identification of network interactions (`fcn.100027c0`) confirms established communication with remote servers using standard or custom protocols for command retrieval. |
| **T1112** | Modify Registry | Evidence found in `fcn.10003740` specifically points to the modification of registry keys, which is a common method for achieving persistence or configuring environment variables. |

***Note on Mapping Strategy:*** 
*   *While "Anti-VM" does not always have a singular unique sub-technique in every version of the MITRE catalog, it falls squarely under the **Defense Evasion** tactic.*
*   *The complex parsing and bitwise logic used to interpret C2 commands are categorized as **Data Obfuscation (T1030)** because the malware is de-obfuscating/decoding data received from the network before execution.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Many standard system error messages (e.g., "bad allocation," "connection refused") were excluded as they are common library/system artifacts and not specific to a unique threat actor or campaign.*

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   *None identified. (The analysis mentions "path normalization" and "registry manipulation" capabilities, but no specific malicious paths or keys were listed).*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Anti-Analysis/VM Evasion Indicators:**
    *   **GenuineIntel Detection:** The code contains references to `5ntel` and `5Genu`, which are part of a routine (`fcn.1000ba6e`) checking for "GenuineIntel" strings and specific CPU features via `cpuid` and `GetProcessorFeaturePresent`. This is used to detect virtualized environments.
*   **C2 Communication Patterns:** 
    *   **Complex Command Parsing:** The routines `fcn.1001b410` and `fcn.10021790` indicate a sophisticated C2 architecture where the malware interprets complex, non-standard instructions (potentially including escaped characters or special symbols like `%`) rather than simple commands.
    *   **Buffer Manipulation:** The presence of large buffer construction routines suggests the ability to handle multi-step injection scripts or remote file reconstruction from the C2.
*   **File System Behavior:**
    *   **Path Normalization:** Function `fcn.1001cb76` indicates the malware is designed to resolve and traverse paths across different systems (handling both `/` and `\`).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `ip-api.com`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Advanced Anti-Analysis:** The presence of `fcn.1000ba6e` utilizing `cpuid` and `GetProcessorFeaturePresent` indicates a sophisticated effort to detect virtualized environments, common in high-end malware to evade automated sandboxes.
*   **Robust C2 Architecture:** The complex command parsing logic (`fcn.1001b410`) and large buffer manipulation routines suggest the binary is designed to handle multifaceted instructions from a remote server, rather than simple static commands.
*   **Loader Capabilities:** Evidence of path normalization, file type checking, and registry-based persistence confirms its role as a "loader" or "trojan," capable of navigating the filesystem to drop and execute secondary payloads.
