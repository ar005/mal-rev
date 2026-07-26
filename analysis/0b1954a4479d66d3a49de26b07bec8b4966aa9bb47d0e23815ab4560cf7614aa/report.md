# Threat Analysis Report

**Generated:** 2026-07-25 19:38 UTC
**Sample:** `0b1954a4479d66d3a49de26b07bec8b4966aa9bb47d0e23815ab4560cf7614aa_0b1954a4479d66d3a49de26b07bec8b4966aa9bb47d0e23815ab4560cf7614aa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b1954a4479d66d3a49de26b07bec8b4966aa9bb47d0e23815ab4560cf7614aa_0b1954a4479d66d3a49de26b07bec8b4966aa9bb47d0e23815ab4560cf7614aa.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 39,424 bytes |
| MD5 | `c19cc92ed0eebefb1201fd06a7af9bf5` |
| SHA1 | `397ee881df2f00dd9748dcb25fc7238faf71bb9e` |
| SHA256 | `0b1954a4479d66d3a49de26b07bec8b4966aa9bb47d0e23815ab4560cf7614aa` |
| Overall entropy | 6.562 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778937951 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 18,432 | 6.008 | No |
| `.data` | 16,384 | 6.944 | No |
| `.pdata` | 512 | 3.548 | No |
| `.idata` | 2,048 | 4.001 | No |
| `.rsrc` | 1,024 | 3.03 | No |

### Imports

**KERNEL32.dll**: `HeapFree`, `GetProcessHeap`, `CreateMutexW`, `OpenMutexW`, `Sleep`, `GetCurrentProcess`, `ExitProcess`, `CreateThread`, `OpenProcess`, `GetSystemDirectoryW`, `VirtualProtect`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `LoadLibraryW`
**USER32.dll**: `wsprintfW`
**ADVAPI32.dll**: `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`, `GetUserNameW`, `GetTokenInformation`
**ole32.dll**: `CoCreateInstance`, `CoUninitialize`, `CoInitializeEx`
**OLEAUT32.dll**: `SysFreeString`, `SysAllocString`, `VariantInit`

## Extracted Strings

Total strings found: **140** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Richgt
`.data
.pdata
@.idata
@.rsrc
45BBFD7B4C624718
RtlGetVersion
.rdata
.rdata$voltmd
.rdata$zzzdbg
.text$mn
.xdata
.pdata
.idata$5
.idata$2
.idata$3
.idata$4
.idata$6
.rsrc$01
.rsrc$02
t$ UWATAVAWH
A_A^A\_]
@SUVWH
D f9,Kt
UWATAVAWH
A_A^A\_]
@USVWATAUAVAWH
A_A^A]A\_^[]
@USVWAVH
A^_^[]
tSHcA<E3
@SUVWAVAWH
(A_A^_^][
@USVWATAUAVAWH
A_A^A]A\_^[]
UVWATAUAVAWH
`A_A^A]A\_^]
UVWATAUAVAWH
?,t
fA9
A_A^A]A\_^]
@USVWATAVAWH
PA_A^A\_^[]
SUVWATAUAVAWH
A_A^A]A\_^][
@USVWATAUAVAWH
@SUVWH
UAVAWH
UVWATAUAVAWH
@A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
SUVWATAUAVAWH
8A_A^A]A\_^][
@SUVWAVH
0A^_^][
@SUVWH
@SUVWAVAWH
(A_A^_^][
@SUVWATAVAWH
PA_A^A\_^][
@SUVWH
p`P
0
mO!&kG
yemWE4K>
?"cVHe
d@!GN 
.4Up'@
Cr7vpI(
G :cg
|kOGR0

4_=U&H
)e}}uv
+6)3Ml
E!	av4|
T-(+kJtSk
S-7I!`
TYd0B{
os7HnT
IbAdxH{
Xl<
oJ
%/u\Hi+!
gxsI)i
B@+:CO
F	N,By
p}v~Asw
CreateFileW
DeleteFileW
GetFileSize
GetFileTime
ReadFile
SetFileTime
CloseHandle
GetLastError
HeapAlloc
HeapFree
GetProcessHeap
CreateMutexW
OpenMutexW
GetCurrentProcess
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000466c` | `0x14000466c` | 1775 | ✓ |
| `fcn.140002658` | `0x140002658` | 1433 | ✓ |
| `fcn.140003bec` | `0x140003bec` | 893 | ✓ |
| `fcn.140002ec8` | `0x140002ec8` | 861 | ✓ |
| `fcn.1400036e0` | `0x1400036e0` | 756 | ✓ |
| `fcn.140001a14` | `0x140001a14` | 697 | ✓ |
| `fcn.1400040a4` | `0x1400040a4` | 642 | ✓ |
| `fcn.140003228` | `0x140003228` | 638 | ✓ |
| `fcn.14000131c` | `0x14000131c` | 631 | ✓ |
| `fcn.140004328` | `0x140004328` | 631 | ✓ |
| `fcn.140001cd0` | `0x140001cd0` | 569 | ✓ |
| `fcn.1400034a8` | `0x1400034a8` | 566 | ✓ |
| `entry0` | `0x14000238c` | 565 | ✓ |
| `fcn.140002c10` | `0x140002c10` | 522 | ✓ |
| `fcn.140001818` | `0x140001818` | 507 | ✓ |
| `fcn.140004d5c` | `0x140004d5c` | 427 | ✓ |
| `fcn.140001f90` | `0x140001f90` | 416 | ✓ |
| `fcn.140005378` | `0x140005378` | 278 | ✓ |
| `fcn.14000513c` | `0x14000513c` | 278 | ✓ |
| `fcn.140001594` | `0x140001594` | 273 | ✓ |
| `fcn.14000221c` | `0x14000221c` | 271 | ✓ |
| `fcn.140003f9c` | `0x140003f9c` | 263 | ✓ |
| `fcn.140001714` | `0x140001714` | 260 | ✓ |
| `fcn.140005254` | `0x140005254` | 183 | ✓ |
| `fcn.1400045a0` | `0x1400045a0` | 168 | ✓ |
| `fcn.1400025c4` | `0x1400025c4` | 146 | ✓ |
| `fcn.140002e1c` | `0x140002e1c` | 145 | ✓ |
| `fcn.140001f0c` | `0x140001f0c` | 132 | ✓ |
| `fcn.14000505c` | `0x14000505c` | 125 | ✓ |
| `fcn.1400016a8` | `0x1400016a8` | 108 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.14000131c.c`](code/fcn.14000131c.c)
- [`code/fcn.140001594.c`](code/fcn.140001594.c)
- [`code/fcn.1400016a8.c`](code/fcn.1400016a8.c)
- [`code/fcn.140001714.c`](code/fcn.140001714.c)
- [`code/fcn.140001818.c`](code/fcn.140001818.c)
- [`code/fcn.140001a14.c`](code/fcn.140001a14.c)
- [`code/fcn.140001cd0.c`](code/fcn.140001cd0.c)
- [`code/fcn.140001f0c.c`](code/fcn.140001f0c.c)
- [`code/fcn.140001f90.c`](code/fcn.140001f90.c)
- [`code/fcn.14000221c.c`](code/fcn.14000221c.c)
- [`code/fcn.1400025c4.c`](code/fcn.1400025c4.c)
- [`code/fcn.140002658.c`](code/fcn.140002658.c)
- [`code/fcn.140002c10.c`](code/fcn.140002c10.c)
- [`code/fcn.140002e1c.c`](code/fcn.140002e1c.c)
- [`code/fcn.140002ec8.c`](code/fcn.140002ec8.c)
- [`code/fcn.140003228.c`](code/fcn.140003228.c)
- [`code/fcn.1400034a8.c`](code/fcn.1400034a8.c)
- [`code/fcn.1400036e0.c`](code/fcn.1400036e0.c)
- [`code/fcn.140003bec.c`](code/fcn.140003bec.c)
- [`code/fcn.140003f9c.c`](code/fcn.140003f9c.c)
- [`code/fcn.1400040a4.c`](code/fcn.1400040a4.c)
- [`code/fcn.140004328.c`](code/fcn.140004328.c)
- [`code/fcn.1400045a0.c`](code/fcn.1400045a0.c)
- [`code/fcn.14000466c.c`](code/fcn.14000466c.c)
- [`code/fcn.140004d5c.c`](code/fcn.140004d5c.c)
- [`code/fcn.14000505c.c`](code/fcn.14000505c.c)
- [`code/fcn.14000513c.c`](code/fcn.14000513c.c)
- [`code/fcn.140005254.c`](code/fcn.140005254.c)
- [`code/fcn.140005378.c`](code/fcn.140005378.c)

## Behavioral Analysis

Based on the provided disassembly and string list, this binary functions as a **multi-stage loader/dropper** designed to unpack, decode, and execute a malicious payload while employing several evasion and anti-analysis techniques.

### Core Functionality
*   **Loader & Decryptor:** The primary purpose of the code is to serve as a "stub." It contains an embedded (likely encrypted) payload. It performs in-memory decryption (using XOR loops) and manual mapping of these components before executing them.
*   **Persistence & Configuration:** It interacts with the Windows Registry (`RegCreateKeyExW`, `RegSetValueExW`) to establish persistence or store configuration data for subsequent stages of the infection.
*   **Payload Deployment:** The code includes logic to move files across the system, potentially "dropping" a secondary executable into a folder and renaming it (seen in functions involving `MoveFileExW` and `SetFileAttributesW`).

### Suspicious & Malicious Behaviors
*   **Process Injection / Reflective Loading:** 
    *   The use of `CreateFileMappingW`, `MapViewOfFile`, and `VirtualProtect` in `fcn.140002c10` is a hallmark of **Process Hollowing** or **Reflective DLL Injection**. It maps a file into memory, modifies its permissions to executable, and manipulates the code segment directly.
    *   The creation of multiple threads via `CreateThread` in `entry0` indicates the loader spawns separate threads for different tasks (e.g., one thread for network communication, one for the main payload).
*   **Timestomping:** 
    *   In `fcn.14000221c`, the code retrieves file timestamps from a system file and applies them to a target file using `SetFileTime`. This is used to hide the presence of dropped files by making them appear as if they have existed on the system for a long time.
*   **Evasive File Manipulation:** 
    *   The code uses `SetFileAttributesW` (to potentially make a file hidden) and `MoveFileExW`. 
    *   In `fcn.140001cd0`, it checks if files exist and moves them to specific paths, often following the "drop" sequence used by malware to hide in system folders.
*   **Anti-Analysis & Obfuscation:**
    *   **Memory Manipulation:** Multiple instances of `VirtualProtect` are used to change memory segments from read-only/execute to **RWX (Read-Write-Execute)**, allowing the loader to "unpack" and execute code directly in memory.
    *   **Decryption Loops:** Several functions contain XOR operations (e.g., `^ 0x75` in `fcn.140003f9c`, `^ 0x42` in `fcn.140003228`). This is used to decrypt strings and the secondary payload's code before execution.
    *   **Dynamic API Resolution:** The frequent use of `GetProcAddress` and `GetModuleHandleW` suggests the binary attempts to hide its true capabilities from static analysis by resolving imports at runtime.

### Notable Techniques & Patterns
*   **Single Instance Control:** The use of `CreateMutexW` ensures that only one instance of the loader/malware runs at a time on the system, which is standard behavior for persistent malware.
*   **MZ Header Check:** Several functions check if a buffer starts with "MZ" (the signature for a Windows executable). This confirms it is searching through its own memory or loaded files to find and extract executable components.
*   **Resource/Memory-Based Extraction:** The code frequently allocates heap memory (`HeapAlloc`) to process data, likely extracting hidden resources and decrypting them into the allocated space before passing them to execution functions.

### Summary of Findings for Incident Response:
The sample is highly suspicious and characteristic of a **sophisticated Trojan or Loader**. It uses classic evasion techniques including:
1.  **Timestomping** to evade forensic detection of new files.
2.  **Process Hollowing/Reflective Loading** to execute code in memory without touching the disk with an "active" malicious file.
3.  **Multi-stage decryption** (XOR loops) to hide its final payload from static signature scanners.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1070.004** | Timestomping | The use of `SetFileTime` to apply system file timestamps to newly dropped files is used to evade detection during forensic analysis. |
| **T1055.016** | Process Hollowing | The combination of `CreateFileMappingW`, `MapViewOfFile`, and `VirtualProtect` indicates the injection of a payload into another process's memory space. |
| **T1547.001** | Registry Run Keys / Startup Folder | Interaction with `RegCreateKeyExW` and `RegSetValueExW` is used to establish persistence for the malware on the host system. |
| **T1036** | Hide Files and Directories | The use of `SetFileAttributesW` (to set hidden flags) and moving files into system folders are standard techniques to conceal malicious binaries. |
| **T1027** | Obfuscated Files or Information | XOR decryption loops and the use of dynamic API resolution (`GetProcAddress`) are used to hide strings and payload functionality from static analysis. |
| **T1106** | Unified Process Injection (Reflective Loading) | The "multi-stage" loading process where components are manually mapped into memory for execution indicates reflective loading techniques. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many of the items in the "Strings" section are standard Windows API calls or assembly artifacts; therefore, they have been excluded as false positives per your instructions.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None specifically defined.* (While the analysis notes that the malware interacts with the Registry and moves files to "system folders," no specific paths or registry keys were listed in the provided strings.)

### **Mutex names / Named pipes**
*   *None identified.* (The use of `CreateMutexW` is noted for single instance control, but no specific mutex string was provided.)

### **Hashes**
*   *None identified.* (The string `45BBFD7B4C624718` appears to be a memory address or internal constant rather than a standard file hash.)

### **Other artifacts**
*   **Decryption Keys:** 
    *   `0x75` (XOR key)
    *   `0x42` (XOR key)
*   **Malicious Techniques / Behavioral Signatures:**
    *   **Process Hollowing / Reflective Loading:** Identified via `CreateFileMappingW`, `MapViewOfFile`, and `VirtualProtect`.
    *   **Timestomping:** Use of `SetFileTime` to modify file timestamps.
    *   **Dynamic API Resolution:** Frequent use of `GetProcAddress` and `GetModuleHandleW` to obfuscate functionality from static analysis.
    *   **Evasive File Manipulation:** Usage of `MoveFileExW` and `SetFileAttributesW` to hide dropped components.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High

**Key evidence**:
*   **Multi-stage Execution & Obfuscation:** The binary functions as a "stub" that utilizes XOR decryption loops and dynamic API resolution (`GetProcAddress`) to hide its true functionality and secondary payloads from static analysis.
*   **Advanced Evasion Techniques:** It employs sophisticated anti-forensic methods, specifically **timestomping** (via `SetFileTime`) to mask the creation of files and **process hollowing/reflective loading** (via `VirtualProtect` and `CreateFileMappingW`) to execute code in memory.
*   **Persistence & File Manipulation:** The sample demonstrates classic post-exploitation behavior by modifying Windows Registry keys for persistence and using `SetFileAttributesW` and `MoveFileExW` to hide dropped components in system directories.
