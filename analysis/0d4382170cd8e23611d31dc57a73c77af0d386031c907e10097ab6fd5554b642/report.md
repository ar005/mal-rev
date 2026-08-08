# Threat Analysis Report

**Generated:** 2026-08-05 18:46 UTC
**Sample:** `0d4382170cd8e23611d31dc57a73c77af0d386031c907e10097ab6fd5554b642_0d4382170cd8e23611d31dc57a73c77af0d386031c907e10097ab6fd5554b642.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d4382170cd8e23611d31dc57a73c77af0d386031c907e10097ab6fd5554b642_0d4382170cd8e23611d31dc57a73c77af0d386031c907e10097ab6fd5554b642.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 4 sections |
| Size | 58,880 bytes |
| MD5 | `d03bf3268f96aae74facc150cd24ffd3` |
| SHA1 | `e8e315bcb8213ffdea06a73d85fec3ff76a373a3` |
| SHA256 | `0d4382170cd8e23611d31dc57a73c77af0d386031c907e10097ab6fd5554b642` |
| Overall entropy | 6.709 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1601067097 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,656 | 5.495 | No |
| `.rdata` | 1,024 | 3.466 | No |
| `.data` | 49,664 | 6.86 | No |
| `.reloc` | 512 | 2.065 | No |

### Imports

**ntdll.dll**: `qsort`, `bsearch`, `wcslen`
**KERNEL32.dll**: `VirtualFree`, `Process32Next`, `Process32First`, `CreateToolhelp32Snapshot`, `CloseHandle`, `SetLastError`, `HeapAlloc`, `HeapFree`, `GetProcessHeap`, `ExitProcess`, `VirtualAlloc`, `VirtualProtect`, `VirtualQuery`, `FreeLibrary`, `GetProcAddress`

## Extracted Strings

Total strings found: **161** (showing first 100)

```
`.rdata
.reloc
;Esj
J8;H<t
e1v0k1v
wcslen
bsearch
ntdll.dll
CloseHandle
SetLastError
HeapAlloc
HeapFree
GetProcessHeap
ExitProcess
VirtualAlloc
VirtualFree
VirtualProtect
VirtualQuery
FreeLibrary
GetProcAddress
LoadLibraryA
LoadLibraryW
IsBadReadPtr
CreateToolhelp32Snapshot
Process32First
Process32Next
KERNEL32.dll
Error protecting memory page
GetNativeSystemInfo
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.reloc
D$tj@P
t"=-[
eN-tZ=
L$$QVj
\$)D$
|$D.u"f
L$DQVW
$6d4
L$6d4
t$nJU
$6d4
L$6d4
t$nJU
s_^][

tC=5#%
T$8;D$
4$\M[0
<z~<A|
wtf=kt{
=Q{h3uB
=#pj't
=#'r;t
D$,QPW
3t&=/&
L$Mo&
L$$)D$(
T$ +T$8
3tW=3@
6tE=4%m;u+
D$kD$v
8t7=t]`+
83t_=
L$ SQVh
=eB-,t!=L
d;t,=Ee*
;t2=;9T
".KK[P
4W:9qRv
Vj,-!u
tq,u+;
;0^0g0
2(535W5]5
5'636R6
8&8-8;8I8d8
9=9V9u9
:8:W:`:
;C;O;n;~;
;[<z<:=Y=l=
<0a0j0
1>1I1x1
2;3]3g3
4%5I5{5
5Y6x6~6
7T7v7{7
81878r8
939Z9y9
9D:c:l:
>?&?E?i?
020Q0Z0y0
172V2j2
3!4@4I4h415T5]5|5
8?8Q8|8
9(9G9|9
:1:N:Z:y:
<%<.<M<
G2f2x2
333Q3v3
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **24**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.10001030` | `0x10001030` | 1121 | ✓ |
| `fcn.100021a0` | `0x100021a0` | 551 | ✓ |
| `fcn.10001e80` | `0x10001e80` | 397 | ✓ |
| `fcn.10001d10` | `0x10001d10` | 357 | ✓ |
| `fcn.10001b50` | `0x10001b50` | 356 | ✓ |
| `fcn.10002090` | `0x10002090` | 270 | ✓ |
| `fcn.100016c0` | `0x100016c0` | 243 | ✓ |
| `fcn.10001a90` | `0x10001a90` | 138 | ✓ |
| `fcn.10002010` | `0x10002010` | 119 | ✓ |
| `fcn.10001a20` | `0x10001a20` | 106 | ✓ |
| `fcn.10001cc0` | `0x10001cc0` | 75 | ✓ |
| `fcn.10001930` | `0x10001930` | 71 | ✓ |
| `fcn.100025e0` | `0x100025e0` | 67 | ✓ |
| `fcn.10001980` | `0x10001980` | 66 | ✓ |
| `fcn.10001000` | `0x10001000` | 48 | ✓ |
| `entry0` | `0x100027b0` | 47 | ✓ |
| `fcn.10001900` | `0x10001900` | 39 | ✓ |
| `fcn.100019f0` | `0x100019f0` | 33 | ✓ |
| `fcn.10001b30` | `0x10001b30` | 30 | ✓ |
| `fcn.100019d0` | `0x100019d0` | 28 | ✓ |
| `fcn.100018d0` | `0x100018d0` | 25 | ✓ |
| `fcn.100018b0` | `0x100018b0` | 21 | ✓ |
| `fcn.100018a0` | `0x100018a0` | 16 | ✓ |
| `fcn.100018f0` | `0x100018f0` | 11 | ✓ |
| `sub.ntdll.dll_qsort` | `0x100027f4` | 6 | — |
| `sub.ntdll.dll_bsearch` | `0x100027ee` | 6 | — |
| `sub.KERNEL32.dll_CreateToolhelp32Snapshot` | `0x100027fa` | 6 | — |
| `sub.KERNEL32.dll_Process32First` | `0x10002800` | 6 | — |
| `sub.KERNEL32.dll_Process32Next` | `0x10002806` | 6 | — |
| `sub.ntdll.dll_wcslen` | `0x100027e8` | 6 | — |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.10001000.c`](code/fcn.10001000.c)
- [`code/fcn.10001030.c`](code/fcn.10001030.c)
- [`code/fcn.100016c0.c`](code/fcn.100016c0.c)
- [`code/fcn.100018a0.c`](code/fcn.100018a0.c)
- [`code/fcn.100018b0.c`](code/fcn.100018b0.c)
- [`code/fcn.100018d0.c`](code/fcn.100018d0.c)
- [`code/fcn.100018f0.c`](code/fcn.100018f0.c)
- [`code/fcn.10001900.c`](code/fcn.10001900.c)
- [`code/fcn.10001930.c`](code/fcn.10001930.c)
- [`code/fcn.10001980.c`](code/fcn.10001980.c)
- [`code/fcn.100019d0.c`](code/fcn.100019d0.c)
- [`code/fcn.100019f0.c`](code/fcn.100019f0.c)
- [`code/fcn.10001a20.c`](code/fcn.10001a20.c)
- [`code/fcn.10001a90.c`](code/fcn.10001a90.c)
- [`code/fcn.10001b30.c`](code/fcn.10001b30.c)
- [`code/fcn.10001b50.c`](code/fcn.10001b50.c)
- [`code/fcn.10001cc0.c`](code/fcn.10001cc0.c)
- [`code/fcn.10001d10.c`](code/fcn.10001d10.c)
- [`code/fcn.10001e80.c`](code/fcn.10001e80.c)
- [`code/fcn.10002010.c`](code/fcn.10002010.c)
- [`code/fcn.10002090.c`](code/fcn.10002090.c)
- [`code/fcn.100021a0.c`](code/fcn.100021a0.c)
- [`code/fcn.100025e0.c`](code/fcn.100025e0.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is an analysis of the binary's behavior:

### Core Functionality
The primary purpose of this code is to function as a **Manual Mapper** or a **Reflective Loader**. Instead of using standard Windows OS features to load a DLL or EXE from a file on disk (which would leave traces), this code takes a raw binary blob in memory, parses its internal structure (the Portable Executable or PE format), and manually maps it into the current process's memory space.

### Suspicious and Malicious Behaviors
*   **Manual Mapping / Process Injection:** The code specifically looks for "MZ" (`0x5A4D`) and "PE" (`0x4550`) headers (found in `fcn.10001030`). This indicates it is processing a full Windows executable or DLL as if it were being loaded by the operating system's loader.
*   **Execution of Fileless Payloads:** Because the code handles the parsing of sections, relocation of addresses (`fcn.100021a0`), and resolution of imports, it allows the malware to execute a "second stage" payload entirely in memory without ever saving that payload to a file on disk.
*   **Memory Permission Manipulation:** The function `fcn.10001d10` calls `VirtualProtect`. This is used to change memory pages to be executable (e.g., moving from Read/Write to Execute/Read). This is a hallmark of malware trying to "flip" the permissions of an injected payload so it can run.
*   **Reflective Loading:** By performing its own relocation and import resolution, the code bypasses standard Windows API calls that would typically trigger security alerts for loading suspicious modules.

### Notable Techniques & Patterns
*   **PE Header Parsing:** The loop in `fcn.10001030` iterates through the sections of a PE file (likely looking at the Section Table). It calculates base addresses and sizes to map these segments correctly into memory.
*   **Relocation Processing:** Function `fcn.100021a0` is typical of a custom loader. It iterates through a relocation table to adjust the memory addresses of instructions based on where the payload was loaded in memory—a process normally handled by the Windows Loader (`ntdll.dll`).
*   **Import Resolution:** The code handles "Import Address Table" (IAT) processing. Function `fcn.10002010` and surrounding logic are designed to find the addresses of functions the payload needs (like `GetProcAddress`) and "stitch" them into the jumped-to memory space.
*   **Avoidance of Standard LoadLibrary:** By manually resolving imports and mapping sections, the malware avoids using `LoadLibraryA` or `LoadLibraryW` for the primary payload, which are common triggers for EDR (Endpoint Detection and Response) systems.

### Summary
This code is a **loader module** used in multi-stage malware infections. It is designed to take an encrypted or obfuscated "payload" (a DLL or EXE), unpack it into memory, manually map its headers, fix its internal pointers, and execute it. This technique is highly common in **Trojans, Ransomware loaders, and Cobalt Strike beacons** to maintain a small footprint on the disk while executing complex malicious logic in memory.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1620** | **Reflective Loader** | The code performs manual PE header parsing, relocation processing, and Import Address Table (IAT) resolution to load a payload into memory while bypassing standard Windows API calls like `LoadLibrary`. |
| **T1055** | **Process Injection** | The binary maps a raw executable "blob" directly into the process's memory space, allowing it to execute a second-stage payload without saving it to disk. |
| **T1620 (Implicit)** | **Manual Mapping** | The specific logic of parsing the `MZ` and `PE` headers and calculating base addresses identifies the core behavior as manual mapping of executable code. |
| **T1055** | **Memory Permission Manipulation** | Use of `VirtualProtect` to change memory page permissions (e.g., from Read/Write to Execute) is a primary mechanism for preparing injected payloads for execution. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the extracted list of Indicators of Compromise (IOCs).

**Note:** This specific sample consists primarily of a **Loader Module**. Because it is designed to run "fileless" payloads in memory, many traditional IOCs (like hardcoded C2 IP addresses or file paths) are absent from the static strings.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: `ntdll.dll` and `KERNEL32.dll` were identified but are excluded as standard system files).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified. (The large block of alphanumeric characters in the "EXTRACTED STRINGS" section appears to be obfuscated code or data segments rather than identifiable MD5/SHA hashes).

### **Other artifacts**
*   **Behavioral IOC: Manual Mapping / Reflective Loading**
    *   Identification of `MZ` (0x5A4D) and `PE` (0x4550) header parsing.
    *   Manual relocation processing (`fcn.100021a0`).
    *   Manual Import Address Table (IAT) resolution (`fcn.10002010`).
*   **Behavioral IOC: Memory Manipulation**
    *   Usage of `VirtualProtect` to flip memory permissions from Read/Write to Execute/Read for injected payloads.
*   **Technical Indicators (Internal Labels):** 
    *   The following internal function offsets were identified as core components of the loading logic; while not "network" IOCs, they can be used to fingerprint specific versions of this loader:
        *   `fcn.10001030` (PE Header Parsing)
        *   `fcn.100021a0` (Relocation Processing)
        *   `fcn.10002010` (IAT Resolution)
        *   `fcn.10001d10` (Memory Protection Adjustment)

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Reflective Loading Logic:** The binary exhibits hallmark behaviors of a reflective loader, including manual parsing of MZ/PE headers, relocation processing (`fcn.100021a0`), and Import Address Table (IAT) resolution (`fcn.10002010`) to execute a payload without calling `LoadLibrary`.
* **Memory Manipulation:** The use of `VirtualProtect` to flip memory permissions from Read/Write to Execute/Read is a primary indicator of a loader preparing an injected "fileless" payload for execution.
* **Function as a Delivery Vehicle:** The lack of hardcoded C2 infrastructure or specific malware-branded strings, combined with its robust manual mapping capabilities, confirms its role as a modular component designed to host and execute secondary payloads (such as RATs or ransomware).
