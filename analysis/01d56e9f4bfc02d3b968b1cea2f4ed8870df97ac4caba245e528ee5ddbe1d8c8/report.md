# Threat Analysis Report

**Generated:** 2026-06-27 14:14 UTC
**Sample:** `01d56e9f4bfc02d3b968b1cea2f4ed8870df97ac4caba245e528ee5ddbe1d8c8_01d56e9f4bfc02d3b968b1cea2f4ed8870df97ac4caba245e528ee5ddbe1d8c8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01d56e9f4bfc02d3b968b1cea2f4ed8870df97ac4caba245e528ee5ddbe1d8c8_01d56e9f4bfc02d3b968b1cea2f4ed8870df97ac4caba245e528ee5ddbe1d8c8.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 4 sections |
| Size | 28,160 bytes |
| MD5 | `63b37292ab95fe1a8262b74392d7ab3f` |
| SHA1 | `211595d337cbb4ff2dbd2e9a030dc36a41e55877` |
| SHA256 | `01d56e9f4bfc02d3b968b1cea2f4ed8870df97ac4caba245e528ee5ddbe1d8c8` |
| Overall entropy | 5.754 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769959513 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 17,920 | 6.084 | No |
| `.rdata` | 8,192 | 5.011 | No |
| `.data` | 512 | 0.216 | No |
| `.pdata` | 512 | 3.896 | No |

### Imports

**KERNEL32.dll**: `GetProcAddress`, `LoadLibraryW`, `GetModuleHandleW`, `GlobalFree`, `GlobalUnlock`, `GlobalHandle`, `GlobalLock`, `GlobalAlloc`, `lstrlenW`, `GetSystemDirectoryW`, `RtlCompareMemory`, `UnmapViewOfFile`, `VirtualProtect`, `lstrcmpA`, `MapViewOfFile`
**WS2_32.dll**: `recv`, `send`, `connect`, `closesocket`, `gethostbyname`, `socket`, `WSAStartup`, `htons`, `WSACleanup`
**SHLWAPI.dll**: `StrStrA`

## Extracted Strings

Total strings found: **139** (showing first 100)

```
`.rdata
@.data
.pdata
x ATAUAVH
 A^A]A\
WATAUAVAWH
cuLD8W
<Lt!<Mt
cuID8W
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
WATAUH
 A]A\_
WATAUH
 A]A\_
@SUVWATAUAVAWH
A_A^A]A\_^][
UVWATAUAVAWH
93tPH9s
H9|$(t&
A_A^A]A\_^]
UVWATAUAVAWH
9D$@u%L
A_A^A]A\_^]
< t<	t
< t<	t
VWATAUAVH
A^A]A\_^
UVWATAUAVAWH
A_A^A]A\_^]
x ATAUAVH
A^A]A\
t$ UWATH
@USVWATH
0A\_^[]
UATAUH
|$D
uI
fD9l$T
t$ WATAUAVAWH
A_A^A]A\_
fffffff
fffffff
strtol
msvcrt.dll
%s%s%s
%s\%s%s
?9/8yxd.&&x
ojxo~g=< jbb~b
tn~vv4~vv
QFZ_WZW
MfehkfKffei
29$?:45
8:95=/dyd8d
rMVPQEHeHHKGa\
= ,*<<|}	&=<;
kLVGPLGVmRGLwPNcxf
Rpa@fpg[txpB
Liro~]rw~
rCTPETeYCTPU
J{py}Hjx|`{lJfg}lq}H
ir}_N|UV^_Hj[NR{
 ?6	&#*
dRCq^[RvCCE^UBCRDv
1'0#/'
x[[_ADuWW[AZ@zUYQu
;?<>%"8*
6).(6?4
fy~xizsdK
%#5">1=5mu#v8'94mu#v?#mu#v1"38mu4
Mo|zp|'=sr0~|~ux
^rsixsi0idmx'=ixei2uipq
^rssx~itrs'=~qrnx
Hnxo0\zxsi'=Prgtqq|2(3-=5Jtsyrjn=SI=,-3-&=Jts+)&=e+)4=\mmqxJx
Vti2(.*3.+=5VUIPQ1=qtvx=Zx~vr4=^uorpx2,-$3-3-3-=N|{|ot2(.*3.
cfrwbsrzz
#"8)"8a
R:&&"]C\C
4)!4'+
mA@ZK@Z
O^^BGMOZGA@
[\BK@MAJKJ#$
jXBRZZ
ywnr2ydy
xsitv~5~c~
wxctw~i?tit
"?7+(5"5i"?"
uEVARh
]vlqs{A
RZUMQVRMRSTMRPS
;-0//:;
ra~hzv|
LSUYCX
5?.3/3:(|5283+/|	,8=(9/
<M.(O
pjt`_^
@tvU]pv
YOk[bCetdOw
ZU_d4h
ZE<i5Oi}KCbO:iy
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002064` | `0x140002064` | 3200 | ✓ |
| `fcn.14000301c` | `0x14000301c` | 1590 | ✓ |
| `fcn.140003d84` | `0x140003d84` | 1005 | ✓ |
| `fcn.1400050a0` | `0x1400050a0` | 820 | ✓ |
| `fcn.140001274` | `0x140001274` | 713 | ✓ |
| `fcn.140004ad8` | `0x140004ad8` | 677 | ✓ |
| `fcn.140001dcc` | `0x140001dcc` | 663 | ✓ |
| `fcn.140003a30` | `0x140003a30` | 656 | ✓ |
| `fcn.140002de4` | `0x140002de4` | 568 | ✓ |
| `section..text` | `0x140001000` | 555 | ✓ |
| `fcn.1400045e8` | `0x1400045e8` | 473 | ✓ |
| `fcn.1400047c4` | `0x1400047c4` | 469 | ✓ |
| `fcn.140003654` | `0x140003654` | 454 | ✓ |
| `fcn.140004d80` | `0x140004d80` | 415 | ✓ |
| `fcn.1400041a8` | `0x1400041a8` | 378 | ✓ |
| `fcn.140001964` | `0x140001964` | 366 | ✓ |
| `fcn.140001ad4` | `0x140001ad4` | 316 | ✓ |
| `fcn.140004f20` | `0x140004f20` | 299 | ✓ |
| `fcn.140001c10` | `0x140001c10` | 292 | ✓ |
| `fcn.140001540` | `0x140001540` | 278 | ✓ |
| `fcn.14000381c` | `0x14000381c` | 277 | ✓ |
| `fcn.140001658` | `0x140001658` | 247 | ✓ |
| `fcn.140001750` | `0x140001750` | 237 | ✓ |
| `fcn.1400053f0` | `0x1400053f0` | 234 | ✓ |
| `fcn.1400043a8` | `0x1400043a8` | 223 | ✓ |
| `fcn.140004510` | `0x140004510` | 213 | ✓ |
| `fcn.140004a24` | `0x140004a24` | 179 | ✓ |
| `entry0` | `0x140002d34` | 175 | ✓ |
| `fcn.140001d34` | `0x140001d34` | 150 | ✓ |
| `fcn.140004488` | `0x140004488` | 134 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001274.c`](code/fcn.140001274.c)
- [`code/fcn.140001540.c`](code/fcn.140001540.c)
- [`code/fcn.140001658.c`](code/fcn.140001658.c)
- [`code/fcn.140001750.c`](code/fcn.140001750.c)
- [`code/fcn.140001964.c`](code/fcn.140001964.c)
- [`code/fcn.140001ad4.c`](code/fcn.140001ad4.c)
- [`code/fcn.140001c10.c`](code/fcn.140001c10.c)
- [`code/fcn.140001d34.c`](code/fcn.140001d34.c)
- [`code/fcn.140001dcc.c`](code/fcn.140001dcc.c)
- [`code/fcn.140002064.c`](code/fcn.140002064.c)
- [`code/fcn.140002de4.c`](code/fcn.140002de4.c)
- [`code/fcn.14000301c.c`](code/fcn.14000301c.c)
- [`code/fcn.140003654.c`](code/fcn.140003654.c)
- [`code/fcn.14000381c.c`](code/fcn.14000381c.c)
- [`code/fcn.140003a30.c`](code/fcn.140003a30.c)
- [`code/fcn.140003d84.c`](code/fcn.140003d84.c)
- [`code/fcn.1400041a8.c`](code/fcn.1400041a8.c)
- [`code/fcn.1400043a8.c`](code/fcn.1400043a8.c)
- [`code/fcn.140004488.c`](code/fcn.140004488.c)
- [`code/fcn.140004510.c`](code/fcn.140004510.c)
- [`code/fcn.1400045e8.c`](code/fcn.1400045e8.c)
- [`code/fcn.1400047c4.c`](code/fcn.1400047c4.c)
- [`code/fcn.140004a24.c`](code/fcn.140004a24.c)
- [`code/fcn.140004ad8.c`](code/fcn.140004ad8.c)
- [`code/fcn.140004d80.c`](code/fcn.140004d80.c)
- [`code/fcn.140004f20.c`](code/fcn.140004f20.c)
- [`code/fcn.1400050a0.c`](code/fcn.1400050a0.c)
- [`code/fcn.1400053f0.c`](code/fcn.1400053f0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

### Malware Analysis Report

#### **Core Functionality**
The provided code describes a sophisticated piece of malware, likely acting as a **Command and Control (C2) agent or a downloader/loader**. The primary purpose is to establish a connection with a remote server, receive instructions or data, and potentially download or execute secondary malicious components.

#### **Suspicious & Malicious Behaviors**
The binary exhibits several behaviors consistent with advanced malware:

*   **Command and Control (C2) Communication:** 
    *   In `fcn.14000301c`, the code utilizes the Windows Socket API (`WS2_32.dll`) to perform a full network cycle: it initializes the environment, resolves a hostname via `gethostbyname`, establishes a connection (`connect`), and sends/receives data over the wire.
    *   The logic includes a loop that parses incoming network packets, looking for specific signatures or "commands" (e.g., checking for specific string lengths and patterns) to decide how to handle the received information.

*   **Process & Module Hunting:**
    *   In `fcn.140001dcc`, the code performs a check for **MZ/PE headers** (`0x5A4D` and `0x4550`). This indicates that the malware is scanning files or memory regions to identify other executable programs (likely looking for targets to inject code into).
    *   It uses `CreateFileMappingW` and `MapViewOfFile`, which are common techniques used to interact with, modify, or extract data from the memory of other processes.

*   **Memory Manipulation:**
    *   The use of **`VirtualProtect`** (visible in `fcn.140001dcc`) is a significant red flag. It is typically used to change page permissions (e.g., making a Read-Only section Executable) before injecting code or modifying the memory of another process.

*   **Anti-Analysis and Evasion:**
    *   **Execution Delays:** The inclusion of `Sleep(1000)` in several loops suggests an attempt to bypass automated sandbox analysis by slowing down the execution timing.
    *   **Dynamic API Resolution:** Instead of using a standard Import Address Table (IAT), the code uses functions like `fcn.140002064` and `fcn.140001dcc` to manually resolve function addresses via `GetProcAddress`. This hides its true capabilities from basic static analysis tools.

*   **Data De-obfuscation:**
    *   The function `fcn.1400041a8` contains complex bitwise operations and loops over byte arrays. This is a classic signature for a **custom decryption or de-obfuscation routine**, likely used to decode configuration data, C2 URLs, or the next stage of the payload received from the internet.

#### **Notable Techniques & Patterns**
*   **Manual PE Parsing:** The code doesn't just open files; it manually checks headers and memory offsets, suggesting a high degree of "awareness" regarding how Windows handles executables.
*   **Layered Complexity:** The presence of several different logic paths for network responses (seen in `fcn.14000301c` and `fcn.140003654`) indicates a complex state machine to handle various C2 instructions.
*   **Custom Memory Copying/Manipulation:** The routine `fcn.1400050a0` appears to be an optimized or custom-implemented memory move, common in malware that avoids using standard library functions like `memcpy` to evade detection by simple heuristic scanners.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071** | Application Layer Protocol | The malware uses standard Windows Socket APIs to establish a connection and parse remote commands through an established communication loop. |
| **T1638** | Dynamic Resolution | The use of `GetProcAddress` instead of a standard Import Address Table (IAT) is used to hide the true functionality from static analysis tools. |
| **T1055** | Process Injection | The combination of `VirtualProtect`, `CreateFileMappingW`, and `MapViewOfFile` indicates an intent to manipulate or inject code into other processes. |
| **T1497** | Virtualization/Sandbox Detection | The deliberate inclusion of `Sleep()` calls is a common tactic to stall execution and bypass automated sandbox analysis environments. |
| **T1027** | Encrypted Payload | The presence of complex bitwise operations and custom loops indicates the use of decryption routines for configuration data or downstream payloads. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided text contains several **TTPs (Tactics, Techniques, and Procedures)**, but very few, if any, "atomic" IOCs (such as specific IP addresses or unique file hashes) are present in the raw strings. The strings provided appear to be a mix of standard Windows API calls, junk data/obfuscated code blocks, and internal function offsets.

---

### **IOC_REPORT**

**IP addresses / URLs / Domains**
*   *None identified.* (The behavioral analysis notes that C2 communication occurs via `WS2_32.dll`, but no specific domains or IP addresses were extracted from the strings).

**File paths / Registry keys**
*   *None identified.* (Standard system paths like `KERNEL32.dll` and `SHLWAPI.dll` were skipped as false positives per instructions).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (No MD5, SHA1, or SHA-256 hashes were present in the provided string data).

**Other artifacts**
*   **C2 Patterns:** The analysis identifies a pattern of using `gethostbyname` and `connect` via `WS2_32.dll` to establish a C2 connection. While not a specific IP, this characterizes the communication method.
*   **Injection Indicators:** Use of `CreateFileMappingW`, `MapViewOfFile`, and `VirtualProtect` indicates a routine for code injection/memory manipulation.
*   **Obfuscation Techniques:** 
    *   **Dynamic API Resolution:** The use of `GetProcAddress` to resolve functions at runtime is used to hide the malware's capabilities from static analysis.
    *   **Custom Decryption:** The presence of a specialized routine (`fcn.1400041a8`) performing bitwise operations indicates that the payload or configuration is encrypted/obfuscated on disk.
*   **Evasion Logic:** Use of `Sleep(1000)` to bypass automated sandbox "time-out" checks.

---

### **Analyst Notes**
The strings provided (e.g., `x ATAUAVH`, `93tPH9s`, `?9/8yxd.&&x`) appear to be high-entropy, obfuscated data or filler bytes. These do not constitute actionable IOCs for blocking but indicate the presence of a packer or a custom encryption layer over the malware's configuration.

---

## Malware Family Classification

1. **Malware family**: Unknown (or Custom)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **C2 Infrastructure & Payload Delivery:** The analysis identifies a sophisticated command-processing loop using `WS2_32.dll`. The ability to parse specific data signatures and execute instructions indicates it serves as a primary communication hub (Backdoor) or a vehicle for fetching subsequent modules (Loader).
*   **Advanced Injection Techniques:** The use of `VirtualProtect`, `CreateFileMappingW`, and manual MZ/PE header scanning reveals an intent to inject malicious code into other processes, which is a hallmark of sophisticated loaders used to hide the malware's presence.
*   **Sophisticated Evasion Tactics:** The malware employs multiple layers of defense against analysis, including dynamic API resolution (via `GetProcAddress`) to hide its import table, custom decryption routines for its configuration/payload, and intentional sleep cycles to bypass automated sandbox detection.
