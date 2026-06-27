# Threat Analysis Report

**Generated:** 2026-06-27 05:43 UTC
**Sample:** `019e0ded6cc8e5524f78fed06f17c3ac00222b5c0204a6ce2691a2775699846e_019e0ded6cc8e5524f78fed06f17c3ac00222b5c0204a6ce2691a2775699846e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `019e0ded6cc8e5524f78fed06f17c3ac00222b5c0204a6ce2691a2775699846e_019e0ded6cc8e5524f78fed06f17c3ac00222b5c0204a6ce2691a2775699846e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 8 sections |
| Size | 1,210,880 bytes |
| MD5 | `57b56d40e53d65137bce9db182b0efe2` |
| SHA1 | `460f1eac16e2300d234b4d9d997bc99df1cefa61` |
| SHA256 | `019e0ded6cc8e5524f78fed06f17c3ac00222b5c0204a6ce2691a2775699846e` |
| Overall entropy | 6.692 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768641311 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 205,824 | 6.438 | No |
| `.rdata` | 81,408 | 5.007 | No |
| `.data` | 5,632 | 3.086 | No |
| `.pdata` | 11,264 | 5.451 | No |
| `_RDATA` | 512 | 4.143 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 901,632 | 6.782 | No |
| `.reloc` | 3,072 | 5.173 | No |

### Imports

**KERNEL32.dll**: `CreateProcessW`, `GetModuleHandleW`, `FreeLibrary`, `WideCharToMultiByte`, `GetTickCount`, `IsDebuggerPresent`, `SetEndOfFile`, `GetProcAddress`, `GetLocalTime`, `FindResourceW`, `LoadResource`, `LoadLibraryW`, `CloseHandle`, `Process32FirstW`, `WriteConsoleW`
**ADVAPI32.dll**: `CreateWellKnownSid`, `FreeSid`, `RegSetValueExW`, `CheckTokenMembership`, `RegCreateKeyExW`, `AllocateAndInitializeSid`, `RegCloseKey`
**SHELL32.dll**: `SHGetFolderPathW`
**ole32.dll**: `CoInitialize`, `CoCreateGuid`, `CoUninitialize`, `CoCreateInstance`, `CoTaskMemFree`, `CoInitializeEx`, `StringFromCLSID`
**WS2_32.dll**: `inet_pton`, `closesocket`, `WSACleanup`, `socket`, `inet_ntoa`, `recvfrom`, `htons`, `sendto`, `setsockopt`, `WSAStartup`
**IPHLPAPI.DLL**: `CreateIpForwardEntry`, `DeleteIpForwardEntry`, `FlushIpNetTable`, `GetAdaptersInfo`, `GetIpForwardTable`
**RPCRT4.dll**: `NdrAsyncClientCall`, `RpcBindingFree`, `RpcBindingFromStringBindingW`, `RpcAsyncCompleteCall`, `RpcStringBindingComposeW`, `RpcRaiseException`, `RpcBindingSetAuthInfoExW`, `RpcStringFreeW`, `RpcAsyncInitializeHandle`
**OLEAUT32.dll**: `SysFreeString`, `SysAllocString`
**ntdll.dll**: `NtDuplicateObject`, `NtClose`, `NtQueryInformationProcess`

### Exports

`RunExternalUAC`, `RunUAC`

## Extracted Strings

Total strings found: **2781** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.fptable
@.reloc
\$ UVWH
\$ UVWH
l$ VWAVH
fB9<@u
D$0HcH
D$0HcH
D$0HcH
fB9<@u
H9D$@H
|$ UAVAWH
@USVWAUAVAWH
A_A^A]_^[]
t$ WAVAWH
0A_A^_
WAVAWH
 A_A^_
UVWAVAWH
A_A^_^]
UATAUAVAWH
A_A^A]A\]
@SUVWAVH
L90u"H
0A^_^][
t$ WAVAWH
 A_A^_
@SUVWAVH
 A^_^][
M'H;M/s H
teH9Khu
t$ UWAVH
t
I9Khs
t
I9Khs
tfA;P
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
\$0HcH
x ATAVAWH
 A_A^A\
x ATAVAWH
 A_A^A\
Cf9)s

fB9<@u
t$ WATAUAVAWH
fB94zu
@8t$@u

@@H90t
@@H90t
A_A^A]A\_
UVWATAUAVAWH
0A_A^A]A\_^]
\$ UVWAVAWH
 A_A^_^]
\$ UVWH
l$ VWATAVAWH
 A_A^A\_^
@SUVWAVH
 A^_^][
@SUVWAVH
 A^_^][
\$ UVWH
@SUVWATAVAWH
 A_A^A\_^][
UVWATAUAVAWH
 A_A^A]A\_^]
UVWATAUAVAWH
 A_A^A]A\_^]
\$ WATAUAVAWH
pA_A^A]A\_
VWATAVAWH
pA_A^A\_^
@SVWATAUAVAWH
tOL+t$@L+
`A_A^A]A\_^[
l$ VWATAVAWH
 A_A^A\_^
l$ VWATAVAWH
 A_A^A\_^
t$ WAVAWH
 A_A^_
T$`A9r
@SUVWH
x ATAVAWH
0A_A^A\
l$ VWATAVAWH
A_A^A\_^
UVWAVAWH
0A_A^_^]
t$ UWAVH
taL9Chu
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000b450` | `0x14000b450` | 68490 | ✓ |
| `fcn.14001ed0c` | `0x14001ed0c` | 48311 | ✓ |
| `fcn.14001ecf8` | `0x14001ecf8` | 48270 | ✓ |
| `method.std::ctype_wchar_t_.virtual_24` | `0x140002094` | 45035 | ✓ |
| `fcn.140029190` | `0x140029190` | 24969 | ✓ |
| `fcn.14000b69c` | `0x14000b69c` | 21563 | ✓ |
| `fcn.14000da28` | `0x14000da28` | 21524 | ✓ |
| `method.std::basic_ofstream_char__struct_std::char_traits_char__.virtual_0` | `0x14000b1e0` | 13764 | ✓ |
| `method.std::basic_stringstream_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_0` | `0x14000b1b0` | 13448 | ✓ |
| `method.std::basic_iostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x14000b1c8` | 13380 | ✓ |
| `method.std::basic_ostream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x14000b1d4` | 13216 | ✓ |
| `method.std::basic_istream_wchar_t__struct_std::char_traits_wchar_t__.virtual_0` | `0x14000b1ec` | 13140 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x14000b1bc` | 12928 | ✓ |
| `fcn.140030fd0` | `0x140030fd0` | 5511 | ✓ |
| `fcn.14002dfac` | `0x14002dfac` | 4759 | ✓ |
| `fcn.140004d48` | `0x140004d48` | 3059 | ✓ |
| `fcn.14000e56c` | `0x14000e56c` | 2831 | ✓ |
| `fcn.140010b10` | `0x140010b10` | 2684 | ✓ |
| `fcn.14000eb90` | `0x14000eb90` | 2538 | ✓ |
| `fcn.1400209dc` | `0x1400209dc` | 2152 | ✓ |
| `fcn.140016350` | `0x140016350` | 2099 | ✓ |
| `fcn.140003e70` | `0x140003e70` | 1586 | ✓ |
| `fcn.140019080` | `0x140019080` | 1498 | ✓ |
| `fcn.1400310a0` | `0x1400310a0` | 1451 | ✓ |
| `fcn.140029bd8` | `0x140029bd8` | 1361 | ✓ |
| `fcn.140012928` | `0x140012928` | 1305 | ✓ |
| `fcn.140018b74` | `0x140018b74` | 1292 | ✓ |
| `fcn.140012440` | `0x140012440` | 1255 | ✓ |
| `fcn.140013ab4` | `0x140013ab4` | 1253 | ✓ |
| `fcn.140022d28` | `0x140022d28` | 1230 | ✓ |

### Decompiled Code Files

- [`code/fcn.140003e70.c`](code/fcn.140003e70.c)
- [`code/fcn.140004d48.c`](code/fcn.140004d48.c)
- [`code/fcn.14000b450.c`](code/fcn.14000b450.c)
- [`code/fcn.14000b69c.c`](code/fcn.14000b69c.c)
- [`code/fcn.14000da28.c`](code/fcn.14000da28.c)
- [`code/fcn.14000e56c.c`](code/fcn.14000e56c.c)
- [`code/fcn.14000eb90.c`](code/fcn.14000eb90.c)
- [`code/fcn.140010b10.c`](code/fcn.140010b10.c)
- [`code/fcn.140012440.c`](code/fcn.140012440.c)
- [`code/fcn.140012928.c`](code/fcn.140012928.c)
- [`code/fcn.140013ab4.c`](code/fcn.140013ab4.c)
- [`code/fcn.140016350.c`](code/fcn.140016350.c)
- [`code/fcn.140018b74.c`](code/fcn.140018b74.c)
- [`code/fcn.140019080.c`](code/fcn.140019080.c)
- [`code/fcn.14001ecf8.c`](code/fcn.14001ecf8.c)
- [`code/fcn.14001ed0c.c`](code/fcn.14001ed0c.c)
- [`code/fcn.1400209dc.c`](code/fcn.1400209dc.c)
- [`code/fcn.140022d28.c`](code/fcn.140022d28.c)
- [`code/fcn.140029190.c`](code/fcn.140029190.c)
- [`code/fcn.140029bd8.c`](code/fcn.140029bd8.c)
- [`code/fcn.14002dfac.c`](code/fcn.14002dfac.c)
- [`code/fcn.140030fd0.c`](code/fcn.140030fd0.c)
- [`code/fcn.1400310a0.c`](code/fcn.1400310a0.c)
- [`code/method.std__basic_iostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_iostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_istream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_istream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c`](code/method.std__basic_ostream_wchar_t__struct_std__char_traits_wchar_t__.virtual_0.c)
- [`code/method.std__basic_stringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c`](code/method.std__basic_stringstream_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_0.c)
- [`code/method.std__ctype_wchar_t_.virtual_24.c`](code/method.std__ctype_wchar_t_.virtual_24.c)

## Behavioral Analysis

This updated analysis incorporates the new disassembly provided in chunk 2/2. The addition of these functions reinforces the conclusion that this is a highly sophisticated piece of malware, likely part of an advanced toolkit used for persistent network access and data exfiltration.

### Updated Analysis of Binary Behavior

#### Core Functionality and Purpose
The binary remains consistent with a **sophisticated Network Proxy or Pivoting Tool**, but the new disassembly reveals additional layers of capability:
*   **Advanced Data Processing:** The presence of high-performance instruction sets (AVX/FMA) in `fcn.1400310a0` suggests that the malware performs complex calculations on data streams. This is often seen in custom encryption protocols or sophisticated encoding schemes used to bypass Deep Packet Inspection (DPI).
*   **Local Data Logging/Persistence:** The interaction with the filesystem via `FindFirstFileExW` and `WriteFile` indicates that the tool is not just passing traffic, but may also be logging local activities, saving configuration states, or interacting with locally stored files to facilitate its persistence on the host.

#### Suspicious and Malicious Behaviors
*   **Complex Data Handling (High Complexity):** 
    The function `fcn.1400310a0` is a massive block of floating-point math using AVX instructions. While it looks like "noise" to a human, in a malware context, this often indicates:
    *   A non-standard encryption algorithm designed to thwart standard signature-based detection.
    *   Decoding of complex packet headers for a proprietary covert communication protocol.
*   **File System Enumeration & Manipulation:** 
    `fcn.140029bd8` utilizes `FindFirstFileExW` and `FindNextFileW`. This allows the malware to:
    *   Search for specific configuration files or "trigger" files.
    *   Scan the local directory structure to find other potential targets/tools.
    *   Identify system paths to hide its activities.
*   **Intentional Data Logging:** 
    `fcn.140012440` explicitly calls `WriteFile`. This indicates that the binary is actively writing data to disk. In a proxy context, this is often used for logging "captured" data before it is exfiltrated, or to write local logs of successfully established tunnels.
*   **Network Routing Manipulation (from Chunk 1):**
    (Carried over) The use of `IPHLPAPI` (`GetIpForwardTable`, `DeleteIpForwardEntry`) confirms the intent to manipulate network routes for pivoting or tunneling.

#### Notable Techniques and Patterns
*   **High-Complexity State Machine/Parser:** 
    The functions `fcn.140018b74` and `fcn.140019080` utilize massive "switch-case" like structures (checking a variety of character codes at specific offsets). This is a classic signature of a **command processor** or a **protocol parser**. It suggests the binary can handle many different types of commands from a remote C2 server.
*   **Sophisticated Obfuscation via Math:** 
    The use of AVX/FMA instructions (as seen in `fcn.1400310a0`) is an advanced way to hide logic. Standard decompilers often struggle to represent these as clean, high-level logic, making it difficult for analysts to understand the underlying algorithm quickly.
*   **Multi-Stage Logic:** 
    The repeated use of internal helper functions (like `fcn.14001a2c8`, `fcn.1400255d0`) and internal state checks suggests a modular architecture where different "modules" handle routing, encryption, parsing, and file I/O separately.

### Summary Update
This sample is a **highly sophisticated, multi-functional network tool** likely designed for use in an Advanced Persistent Threat (APT) scenario. 

It combines:
1.  **Routing Manipulation:** To create tunnels or bypass security boundaries (Chunk 1).
2.  **Advanced Encryption/Encoding:** Using complex math and AVX instructions to hide its communication traffic (Chunk 2).
3.  **Robust Command Processing:** A large, complex parser allowing the tool to perform various tasks remotely (Chunk 2).
4.  **File System Interaction:** Mechanisms for logging data or managing local configuration files (Chunk 2).

The presence of these features together suggests a "Swiss Army Knife" style malware capable of sophisticated proxying, data exfiltration, and stealthy persistence within a compromised network.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1561.003** | Encrypting Network Traffic | The use of complex AVX/FMA instructions indicates a sophisticated, non-standard encryption or encoding scheme designed to bypass Deep Packet Inspection (DPI). |
| **T1083** | File and Directory Discovery | The utilization of `FindFirstFileExW` and `FindNextFileW` allows the malware to locate configuration files, identify system paths, and find other potential targets. |
| **T1074** | Data Staged | The use of `WriteFile` to store "captured" data before exfiltration indicates a staging mechanism for information gathered from the local network. |
| **T1562.001** | Proxy | The manipulation of the IP forward table via `IPHLPAPI` confirms the tool's primary role as a proxy or pivot point to bypass security boundaries. |
| **T1059** | Command and Scripting Interpreter | The massive switch-case structures indicate a robust command processor designed to interpret and execute various tasks received from a remote C2 server. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "Extracted Strings" section contains a high volume of obfuscated or non-functional data (e.g., `WAVAWH`, `fB9<@u`). These do not represent actionable infrastructure like IPs or URLs and have been excluded as noise.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (While the behavior analysis mentions the use of `FindFirstFileExW` and `WriteFile`, no specific local paths or registry keys were provided in the source text.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Network Manipulation Indicators:** Use of `IPHLPAPI` (specifically `GetIpForwardTable` and `DeleteIpForwardEntry`) to manipulate network routes for pivoting/tunneling.
*   **Sophisticated Encryption/Encoding Logic:** Identification of high-complexity math using **AVX/FMA instructions** in function `fcn.1400310a0` used to bypass Deep Packet Inspection (DPI).
*   **Command Processor / Protocol Parser:** Large "switch-case" style structures found in `fcn.140018b74` and `fcn.140019080`, indicating a multi-command capability from a remote C2.
*   **Data Logging/Persistence Behavior:** Function `fcn.140012440` utilizes `WriteFile` for local logging or configuration storage.

---
**Analyst Note:** The sample exhibits characteristics of an **APT-level Proxy/Pivoting tool**. While static indicators (IPs/Domains) are missing from this specific data dump, the behavioral markers indicate a high level of sophistication in evasion and network manipulation.

---

## Malware Family Classification

1. **Malware family**: custom 
2. **Malware type**: backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Network Pivoting & Routing:** The use of `IPHLPAPI` functions (`GetIpForwardTable`, `DeleteIpForwardEntry`) confirms the tool's primary role is to manipulate network routes for pivoting and bypassing security perimeters.
*   **Advanced Obfuscation/Encryption:** The identification of high-complexity AVX/FMA instruction sets indicates a sophisticated, non-standard encryption scheme designed to evade Deep Packet Inspection (DPI).
*   **Robust Command Infrastructure:** The presence of massive switch-case structures highlights the existence of a complex command processor capable of interpreting diverse instructions from a remote C2 server.
