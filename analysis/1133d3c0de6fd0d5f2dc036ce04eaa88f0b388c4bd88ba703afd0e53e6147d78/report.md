# Threat Analysis Report

**Generated:** 2026-08-23 05:49 UTC
**Sample:** `1133d3c0de6fd0d5f2dc036ce04eaa88f0b388c4bd88ba703afd0e53e6147d78_1133d3c0de6fd0d5f2dc036ce04eaa88f0b388c4bd88ba703afd0e53e6147d78.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1133d3c0de6fd0d5f2dc036ce04eaa88f0b388c4bd88ba703afd0e53e6147d78_1133d3c0de6fd0d5f2dc036ce04eaa88f0b388c4bd88ba703afd0e53e6147d78.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 4 sections |
| Size | 57,344 bytes |
| MD5 | `0ee875c8232d83dd7d487a5d019d633e` |
| SHA1 | `9fdc9995121e86918ce9c9d34cad2c95cbc7e0a6` |
| SHA256 | `1133d3c0de6fd0d5f2dc036ce04eaa88f0b388c4bd88ba703afd0e53e6147d78` |
| Overall entropy | 5.489 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1777407533 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 49,664 | 5.388 | No |
| `.rdata` | 3,584 | 6.451 | No |
| `.data` | 512 | 0.122 | No |
| `.pdata` | 2,560 | 4.096 | No |

### Imports

**KERNEL32.dll**: `GetCurrentDirectoryA`, `GetFileAttributesA`, `GetTickCount64`
**USER32.dll**: `ChildWindowFromPointEx`, `DefWindowProcA`, `FindWindowExA`, `GetCursorPos`, `GetUpdateRgn`, `GetWindowLongA`, `GetWindowTextLengthW`, `KillTimer`, `MapWindowPoints`, `MessageBoxA`, `MoveWindow`, `PostMessageW`, `ReleaseDC`, `ScreenToClient`, `TranslateMessage`
**GDI32.dll**: `BitBlt`, `CreateBitmap`, `CreateCompatibleDC`, `CreateFontIndirectW`, `GetROP2`, `SaveDC`

## Extracted Strings

Total strings found: **119** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
D$cr,H
HcD$hH
<$_s+H
|$P=u
D$iD$
L$@HcT$4
L$@HcT$,
L$8HcT$,H
L$@HcT$,
L$@HcT$0
L$@HcT$,
L$@HcT$0
D$8H;D$X
L$HHcT$D
L$HHcT$D
L$HHcT$@
L$HHcT$D
L$HHcT$@
L$HHcT$D
L$HHcT$@
L$HHcT$0
D$@H;D$HtzH
D$,;D$lu
D$ H;D$8s9H
D$,iD$,
D$ H;D$8s:H
D$,iD$,
;D$HuFH
;D$Lu(H
L$hHcI<H
;D$|ukH
D$ ;D$\r(
;D$PuNH
;D$Tu0H
D$/t)H
D$/tH
&kD$8
H
D$`H;D$p
L$HHcI<H
D$ ;D$<r%
D$GsGH
D$PH;A
D$XH;A
H+D$PH
D$ H;D$0t]H
D$HH;A
D$8H;D$Hs
H
H;D$8s
D$HH;A
D$8H;D$Hs
H
H;D$8s
D$'t}H
D$'thH
D$'tSH
D$'t>H
D$'t)H
D$0H;D$8tRH
<$s+H
<$s+H
ffffff.
ffffff.
ffffff.
ffffff.
ffffff.
ffffff.
ffffff.
fffff.
ffffff.
D$0H;D$(u
D$0H;D$(s
T[irNv
3}'
.m
T2@_ h
 RthK~
load_clr_from_memory
  -> E_FAIL (load/entry/Invoke); check assembly and entry point
hresult
hc_clr_loader
instance::bind_heap
instance::ensure
hc_clr_loader: empty URL after decode
stager::download
VirtualAlloc (decode buffer)
base64_decode: invalid (check URL returns raw Base64, not a web page/JSON wrap)
  -> CLR v4 not loadable (install .NET Framework 4.x, x64 host for x64 build)
  -> COM/CLR surfaces not resolved (ole32/oleaut/mscoree, or instance::ensure failed)
VirtualAlloc (raw PE)
base64: empty (only whitespace/blank body?)
GetCurrentDirectoryA
GetFileAttributesA
GetTickCount64
ChildWindowFromPointEx
DefWindowProcA
FindWindowExA
GetCursorPos
GetUpdateRgn
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140009270` | `0x140009270` | 6089 | ✓ |
| `fcn.1400077b0` | `0x1400077b0` | 2626 | ✓ |
| `fcn.14000baa0` | `0x14000baa0` | 2489 | ✓ |
| `fcn.140001320` | `0x140001320` | 2041 | ✓ |
| `fcn.14000ac00` | `0x14000ac00` | 1915 | ✓ |
| `fcn.140008bf0` | `0x140008bf0` | 1535 | ✓ |
| `fcn.1400061e0` | `0x1400061e0` | 1244 | ✓ |
| `fcn.1400023c0` | `0x1400023c0` | 1174 | ✓ |
| `fcn.140005e00` | `0x140005e00` | 759 | ✓ |
| `fcn.140004360` | `0x140004360` | 757 | ✓ |
| `fcn.140004d50` | `0x140004d50` | 618 | ✓ |
| `fcn.140002000` | `0x140002000` | 594 | ✓ |
| `fcn.1400032c0` | `0x1400032c0` | 567 | ✓ |
| `fcn.140002b70` | `0x140002b70` | 549 | ✓ |
| `fcn.140003eb0` | `0x140003eb0` | 529 | ✓ |
| `fcn.140005990` | `0x140005990` | 489 | ✓ |
| `fcn.140002900` | `0x140002900` | 487 | ✓ |
| `fcn.1400084b0` | `0x1400084b0` | 479 | ✓ |
| `fcn.140005b80` | `0x140005b80` | 442 | ✓ |
| `fcn.1400039b0` | `0x1400039b0` | 426 | ✓ |
| `fcn.140006ce0` | `0x140006ce0` | 417 | ✓ |
| `fcn.140003820` | `0x140003820` | 395 | ✓ |
| `fcn.140003150` | `0x140003150` | 359 | ✓ |
| `fcn.14000c8e0` | `0x14000c8e0` | 355 | ✓ |
| `fcn.140004fc0` | `0x140004fc0` | 354 | ✓ |
| `fcn.1400067d0` | `0x1400067d0` | 345 | ✓ |
| `fcn.140003d50` | `0x140003d50` | 341 | ✓ |
| `fcn.1400048a0` | `0x1400048a0` | 321 | ✓ |
| `fcn.140004b10` | `0x140004b10` | 321 | ✓ |
| `fcn.140003020` | `0x140003020` | 296 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001320.c`](code/fcn.140001320.c)
- [`code/fcn.140002000.c`](code/fcn.140002000.c)
- [`code/fcn.1400023c0.c`](code/fcn.1400023c0.c)
- [`code/fcn.140002900.c`](code/fcn.140002900.c)
- [`code/fcn.140002b70.c`](code/fcn.140002b70.c)
- [`code/fcn.140003020.c`](code/fcn.140003020.c)
- [`code/fcn.140003150.c`](code/fcn.140003150.c)
- [`code/fcn.1400032c0.c`](code/fcn.1400032c0.c)
- [`code/fcn.140003820.c`](code/fcn.140003820.c)
- [`code/fcn.1400039b0.c`](code/fcn.1400039b0.c)
- [`code/fcn.140003d50.c`](code/fcn.140003d50.c)
- [`code/fcn.140003eb0.c`](code/fcn.140003eb0.c)
- [`code/fcn.140004360.c`](code/fcn.140004360.c)
- [`code/fcn.1400048a0.c`](code/fcn.1400048a0.c)
- [`code/fcn.140004b10.c`](code/fcn.140004b10.c)
- [`code/fcn.140004d50.c`](code/fcn.140004d50.c)
- [`code/fcn.140004fc0.c`](code/fcn.140004fc0.c)
- [`code/fcn.140005990.c`](code/fcn.140005990.c)
- [`code/fcn.140005b80.c`](code/fcn.140005b80.c)
- [`code/fcn.140005e00.c`](code/fcn.140005e00.c)
- [`code/fcn.1400061e0.c`](code/fcn.1400061e0.c)
- [`code/fcn.1400067d0.c`](code/fcn.1400067d0.c)
- [`code/fcn.140006ce0.c`](code/fcn.140006ce0.c)
- [`code/fcn.1400077b0.c`](code/fcn.1400077b0.c)
- [`code/fcn.1400084b0.c`](code/fcn.1400084b0.c)
- [`code/fcn.140008bf0.c`](code/fcn.140008bf0.c)
- [`code/fcn.140009270.c`](code/fcn.140009270.c)
- [`code/fcn.14000ac00.c`](code/fcn.14000ac00.c)
- [`code/fcn.14000baa0.c`](code/fcn.14000baa0.c)
- [`code/fcn.14000c8e0.c`](code/fcn.14000c8e0.c)

## Behavioral Analysis

### Analysis Summary
The binary appears to be a **multi-stage malware loader (stager)** designed to download, decrypt, and execute a secondary payload in memory—specifically one utilizing the .NET Framework (CLR). The presence of complex switch-like logic, hidden state tables, and specific system calls suggests it is engineered to evade detection by security products.

### Core Functionality
*   **Staging & Execution:** The presence of strings like `stager::download` and `load_clr_from_memory` indicates that this program's primary role is not the final payload but rather preparing a "stage" for it. It likely downloads a remote file (or an embedded resource) and loads it into a memory buffer.
*   **In-Memory PE Loading:** The use of `VirtualAlloc` specifically for a "raw PE" suggests **Reflective DLL Injection** or **Process Hollowing**. Instead of saving the final payload to disk, the loader prepares memory spaces to host the actual malicious logic.
*   **CLR Integration:** The code explicitly references `.NET Framework 4.x` and `mscoree.dll`. This implies that the ultimate payload is a .NET assembly (C# or VB.NET), which often allows malware authors to perform complex tasks while staying "hidden" inside a managed memory space.

### Suspicious & Malicious Behaviors
*   **Process/Memory Injection:** The code identifies and prepares memory blocks using `VirtualAlloc` to host decrypted payloads. This is a hallmark of "fileless" malware techniques.
*   **Decryption/De-obfuscation Routine:** Function `fcn.140003150` contains a loop performing bitwise XOR operations on data buffers, which is a standard method for decrypting configuration blocks or the secondary payload in memory.
*   **Anti-Analysis & Sandbox Evasion:** 
    *   The inclusion of `GetTickCount64`, `GetCursorPos`, and `GetWindowLongA` are common indicators of anti-debugging. The malware checks if the system clock is being manipulated (timing attacks) or if there is "human" interaction like mouse movement before proceeding.
    *   **Complexity as Obfuscation:** The heavy use of switch-case style logic (e.g., `fcn.1400077b0`) and indirect function calls suggests an attempt to frustrate static analysis by making the control flow difficult to follow.
*   **Network Activity (Inferred):** While no direct `connect` call is shown in this snippet, the "stager" naming convention and base64 decoding logic strongly imply that the sample reaches out to a Command & Control (C2) server or an intermediary host to fetch the second stage.

### Notable Techniques & Patterns
*   **Reflective Loading Logic:** The code uses extensive lookup tables (e.g., `fcn.140005990` and `fcn.1400067d0`) to navigate data structures that appear to be internal "command" or "resource" lists.
*   **State Machine Behavior:** Functions like `fcn.1400077b0` utilize a series of hardcoded hex values (e.g., `0xac990cd8`, `0xffbe85fa`) to drive the execution flow. This is often used in custom packers to determine which "task" the loader should perform next based on environmental checks.
*   **Configuration Obfuscation:** The high density of intermediate functions (`fcn.1400039b0` through `fcn.140004f0`) that register different "capabilities" suggests a modular architecture where the malware determines its capabilities at runtime (e.g., checking if it has admin privileges or can find specific windows).
*   **Import Obfuscation/Indirection:** The code frequently interacts with values fetched from offset-heavy structures, suggesting that the primary API calls are being "wrapped" to hide their true intent from simple scanners.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055.001** | Reflective DLL Injection | The use of `VirtualAlloc` to host a "raw PE" in memory rather than on disk indicates the malware is injecting and executing code directly from memory buffers. |
| **T1027** | Obfuscated Files or Information | The use of XOR loops (fcn.140003150) and extensive lookup tables to hide configuration blocks and internal logic is a clear attempt to evade static analysis. |
| **T1497** | Virtualization/Sandbox Evasion | The inclusion of `GetTickCount64` and `GetCursorPos` are classic indicators used to detect if the malware is running in an automated sandbox or under human observation. |
| **T1138** | Dynamic Resolution | The use of "wrapped" API calls and offset-heavy structures indicates a technique to hide the intended functionality from security tools that scan for standard import tables. |
| **T1059** | Command and Scripting Interpreter | The explicit integration with `mscoree.dll` and `.NET Framework 4.x` allows the malware to execute complex logic within a managed environment. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The source text contains high levels of obfuscation; while many internal function names were identified, specific infrastructure details (like hardcoded IPs or clear-text URLs) were not present in the provided snippet.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes a "stager::download" and "base64_decode" process, implying that network indicators are likely hidden within obfuscated data blocks or derived at runtime).

### **File paths / Registry keys**
*   *None identified.* (Standard Windows API calls such as `GetCurrentDirectoryA` were present, but no specific malicious file paths or registry keys were listed).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Malware Techniques/Patterns:**
    *   **Reflective Loading:** Use of `VirtualAlloc` to host "raw PE" and the specific function `load_clr_from_memory`.
    *   **Staging Logic:** Identification of a stager component (`stager::download`) used to fetch secondary payloads.
    *   **De-obfuscation Routine:** Evidence of an XOR-based decryption loop (referenced in analysis as `fcn.140003150`).
    *   **Anti-Analysis/Evasion:** 
        *   Use of `GetTickCount64` and `GetCursorPos` to detect debugger presence or lack of human interaction.
        *   Use of `GetWindowLongA` for environment checking.
    *   **Execution Environment:** Target usage of .NET Framework (`mscoree.dll`, `CLR v4`).

---
**Analyst Note:** The malware utilizes a "fileless" approach, where the primary malicious behavior (the .NET assembly) is loaded directly into memory to evade disk-based scanners. Detection should focus on **memory forensics** and **behavioral monitoring** of processes calling `VirtualAlloc` followed by `load_clr_from_memory`.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Staging & Reflective Loading:** The binary is explicitly identified as a "stager" that utilizes `VirtualAlloc` and `load_clr_from_memory` to execute .NET-based payloads directly in memory, bypassing traditional disk-based detection.
*   **Multi-Stage Execution & Decryption:** The presence of XOR-based decryption routines (`fcn.140003150`) and logic to host "raw PE" files indicates its primary role is to decrypt and unpack a second-stage payload.
*   **Evasion Tactics:** The inclusion of anti-analysis techniques (e.g., `GetTickCount64` for timing attacks, `GetCursorPos` to detect human interaction) combined with complex switch-case logic shows it is designed to evade automated sandboxes and static analysis.
