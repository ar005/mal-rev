# Threat Analysis Report

**Generated:** 2026-08-06 16:54 UTC
**Sample:** `0d575a220f37b871feb08638ec9f8b0b8f63124d9cc625dfa00312165b35d372_0d575a220f37b871feb08638ec9f8b0b8f63124d9cc625dfa00312165b35d372.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d575a220f37b871feb08638ec9f8b0b8f63124d9cc625dfa00312165b35d372_0d575a220f37b871feb08638ec9f8b0b8f63124d9cc625dfa00312165b35d372.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 157,184 bytes |
| MD5 | `ae73547b18daccf2c8b4d671edc05bdd` |
| SHA1 | `9d7ffd5700d4755d094c9bc5db0c80245737e65e` |
| SHA256 | `0d575a220f37b871feb08638ec9f8b0b8f63124d9cc625dfa00312165b35d372` |
| Overall entropy | 5.584 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764045479 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 52,224 | 6.408 | No |
| `.rdata` | 41,472 | 4.699 | No |
| `.data` | 3,072 | 1.89 | No |
| `.pdata` | 4,096 | 4.63 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 52,736 | 4.141 | No |
| `.reloc` | 2,048 | 4.846 | No |

### Imports

**KERNEL32.dll**: `WriteConsoleW`, `CreateFileW`, `SetFilePointerEx`, `CreateProcessW`, `GetConsoleOutputCP`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`, `GetProcessHeap`, `GetLocalTime`, `CloseHandle`, `Process32FirstW`, `Process32NextW`, `OpenProcess`, `CreateToolhelp32Snapshot`
**USER32.dll**: `DefWindowProcW`, `CreateWindowExW`, `SendMessageW`, `ShowWindow`, `GetMessageW`, `RegisterClassW`, `MessageBoxA`, `TranslateMessage`, `PostQuitMessage`, `UpdateWindow`, `DispatchMessageW`
**GDI32.dll**: `GetStockObject`, `SetTextColor`, `SetBkColor`, `DeleteObject`, `CreateFontW`
**ADVAPI32.dll**: `FreeSid`, `CheckTokenMembership`, `AllocateAndInitializeSid`

## Extracted Strings

Total strings found: **418** (showing first 100)

```
!This program cannot be run in DOS mode.
$
RichbV
`.rdata
@.data
.pdata
@.fptable
@.reloc
VATAUAWH
A_A]A\^
uxHcH
u0HcH<
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
WATAUAVAWH
A_A^A]A\_
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
G0HcX
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
@SVWATAUAVAWH
A_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
|$$Hc^
@A_A^A]A\_^[
UVWATAUAVAWH
G0Lch
G0HcX
D$hIcu
 A_A^A]A\_^]
99~YHc^
t98t H
tfD9y
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
fA9,@u
fA9,vu
0A_A^_
u3HcH<H
WAVAWH
 A_A^_
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
D$0@8{
UVWATAUAVAWH
H;\$8u
H;\$8u
fD9$Ju
A_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
fD9t$b
K H;j
K(H;`
K0H;V
K8H;L
K@H;B
KHH;8
KhH;F
KpH;<
KxH;2
	H;U
KXH;w
K`H;m
@UATAUAVAWH
e0A_A^A]A\]
t$ WATAUAVAWH
 A_A^A]A\_
t$ WATAUAVAWH
D!|$xA
A_A^A]A\_
L$ VWAVH
fD94H}aD
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140005d78` | `0x140005d78` | 15595 | ✓ |
| `fcn.140005d64` | `0x140005d64` | 15554 | ✓ |
| `fcn.14000d080` | `0x14000d080` | 1677 | ✓ |
| `fcn.140007474` | `0x140007474` | 1421 | ✓ |
| `fcn.14000321c` | `0x14000321c` | 1213 | ✓ |
| `fcn.14000b3dc` | `0x14000b3dc` | 1171 | ✓ |
| `fcn.14000ccc0` | `0x14000ccc0` | 920 | ✓ |
| `fcn.14000a960` | `0x14000a960` | 920 | ✓ |
| `fcn.14000acf8` | `0x14000acf8` | 817 | ✓ |
| `fcn.14000bd28` | `0x14000bd28` | 815 | ✓ |
| `fcn.140007d00` | `0x140007d00` | 712 | ✓ |
| `fcn.140001fc8` | `0x140001fc8` | 667 | ✓ |
| `fcn.140001840` | `0x140001840` | 660 | ✓ |
| `fcn.140004830` | `0x140004830` | 642 | ✓ |
| `fcn.14000795c` | `0x14000795c` | 623 | ✓ |
| `fcn.140009c04` | `0x140009c04` | 604 | ✓ |
| `fcn.1400052d4` | `0x1400052d4` | 597 | ✓ |
| `fcn.1400036dc` | `0x1400036dc` | 584 | ✓ |
| `fcn.140003c7c` | `0x140003c7c` | 557 | ✓ |
| `fcn.140009028` | `0x140009028` | 555 | ✓ |
| `fcn.140008bf0` | `0x140008bf0` | 518 | ✓ |
| `fcn.1400029a0` | `0x1400029a0` | 517 | ✓ |
| `fcn.140007764` | `0x140007764` | 501 | ✓ |
| `fcn.140002e90` | `0x140002e90` | 499 | ✓ |
| `fcn.140001640` | `0x140001640` | 493 | ✓ |
| `fcn.14000747c` | `0x14000747c` | 462 | ✓ |
| `fcn.14000a4ec` | `0x14000a4ec` | 445 | ✓ |
| `fcn.14000a6f4` | `0x14000a6f4` | 437 | ✓ |
| `fcn.140009434` | `0x140009434` | 434 | ✓ |
| `fcn.1400058ac` | `0x1400058ac` | 430 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001640.c`](code/fcn.140001640.c)
- [`code/fcn.140001840.c`](code/fcn.140001840.c)
- [`code/fcn.140001fc8.c`](code/fcn.140001fc8.c)
- [`code/fcn.1400029a0.c`](code/fcn.1400029a0.c)
- [`code/fcn.140002e90.c`](code/fcn.140002e90.c)
- [`code/fcn.14000321c.c`](code/fcn.14000321c.c)
- [`code/fcn.1400036dc.c`](code/fcn.1400036dc.c)
- [`code/fcn.140003c7c.c`](code/fcn.140003c7c.c)
- [`code/fcn.140004830.c`](code/fcn.140004830.c)
- [`code/fcn.1400052d4.c`](code/fcn.1400052d4.c)
- [`code/fcn.1400058ac.c`](code/fcn.1400058ac.c)
- [`code/fcn.140005d64.c`](code/fcn.140005d64.c)
- [`code/fcn.140005d78.c`](code/fcn.140005d78.c)
- [`code/fcn.140007474.c`](code/fcn.140007474.c)
- [`code/fcn.14000747c.c`](code/fcn.14000747c.c)
- [`code/fcn.140007764.c`](code/fcn.140007764.c)
- [`code/fcn.14000795c.c`](code/fcn.14000795c.c)
- [`code/fcn.140007d00.c`](code/fcn.140007d00.c)
- [`code/fcn.140008bf0.c`](code/fcn.140008bf0.c)
- [`code/fcn.140009028.c`](code/fcn.140009028.c)
- [`code/fcn.140009434.c`](code/fcn.140009434.c)
- [`code/fcn.140009c04.c`](code/fcn.140009c04.c)
- [`code/fcn.14000a4ec.c`](code/fcn.14000a4ec.c)
- [`code/fcn.14000a6f4.c`](code/fcn.14000a6f4.c)
- [`code/fcn.14000a960.c`](code/fcn.14000a960.c)
- [`code/fcn.14000acf8.c`](code/fcn.14000acf8.c)
- [`code/fcn.14000b3dc.c`](code/fcn.14000b3dc.c)
- [`code/fcn.14000bd28.c`](code/fcn.14000bd28.c)
- [`code/fcn.14000ccc0.c`](code/fcn.14000ccc0.c)
- [`code/fcn.14000d080.c`](code/fcn.14000d080.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis of the sample's functionality.

### Updated Analysis Summary
The addition of this second set of functions reinforces the conclusion that this is a **highly engineered system-level library or middleware**. The code demonstrates sophisticated handling of internationalization (i18n), internal memory management, and dynamic linking. While one function includes an administrative check—a common "gate" in certain types of software—the overall structure remains consistent with complex application frameworks rather than typical malware.

---

### New Findings & Detailed Analysis

#### 1. Advanced Unicode and Encoding Logic
Several functions (`fcn.14000747c`, `fcn.14000a4ec`, `fcn.14000a6f4`) are dedicated to processing multi-byte characters and validating Unicode points.
*   **UTF-8 Decoding:** The logic for checking ranges (e.g., `uVar3 & 0x3f` and bitwise shifts) is characteristic of a robust **UTF-8/Unicode transcoding engine**. It handles surrogate pairs (the range `0xd800` to `0x110000`) and ensures that multi-byte characters are correctly parsed into individual code points.
*   **Code Page Mapping:** The presence of `GetCPInfo` and the subsequent loop in `fcn.140007764` suggests the software maps system-specific codepages to an internal standard, ensuring consistent behavior across different regional settings.

#### 2. Windows System Interaction & UI
The function `fcn.140001640` provides a glimpse into how the application interacts with the OS:
*   **Privilege Verification:** The code calls `AllocateAndInitializeSid` and `CheckTokenMembership`. If the user lacks administrative privileges, it triggers a **MessageBoxA** stating: *"This system must be run as Administrator."*
*   **Standard Windowing logic:** If permissions are met, it proceeds to register a window class (`RegisterClassW`), create a window (`CreateWindowExW`) with a title containing a Discord link (e.g., "My Discord: .gg/pvgc"), and enters a standard **Win32 message loop** (`GetMessageW`, `TranslateMessage`, `DispatchMessageW`). 
*   *Note:* While the "Run as Admin" check is sometimes used by malware to gain higher privileges, its implementation here follows standard Windows desktop application patterns.

#### 3. Dynamic Loading and Memory Management
The function `fcn.140009434` reveals a sophisticated **Dynamic Loader**:
*   **Symbol Resolution:** It iterates through a table of names/indices and uses `LoadLibraryExW` and `GetProcAddress` to resolve functions at runtime. This is common in "plugin" architectures or software that needs to load optional features dynamically.
*   **Memory Protection:** It utilizes `VirtualProtect` on specific memory regions before resolving symbols, a standard practice when preparing memory for execution or modification by the system's loader.

#### 4. Advanced Memory Manipulation
The function `fcn.1400058ac` contains complex arithmetic and bit-shifting involving global state variables (e.g., `*0x140019000`). This is typical of **custom memory allocators** or internal data structure management within a large C++ framework (like the Unreal Engine, Unity, or a specialized database engine).

---

### Revised Behavior Summary

| Category | Observation | Significance |
| :--- | :--- | :--- |
| **I18N/Unicode** | Extensive multi-byte character parsing and Codepage conversion. | Indicates high-quality software intended for global use. |
| **System Access** | Check for Administrator privileges before launching a GUI. | Typical of tools requiring system-level hooks or installation rights. |
| **Dynamics** | Automated `LoadLibrary` / `GetProcAddress` loops. | Suggests a modular architecture (plugin support/dynamic features). |
| **Complex Logic** | Extensive use of bitmasking, multi-stage decoding, and stateful logic. | Consistent with professional software engineering (e.g., game engines or drivers). |

### Conclusion Update
The inclusion of chunk 2 confirms the sample's complexity but does not introduce new evidence of malicious intent. The code is heavily invested in **robustness**—handling edge cases for Unicode, ensuring system-level permissions are present before launching a UI, and dynamically loading necessary components. 

This behavior profile is consistent with **specialized enterprise software, game engine middleware, or anti-cheat systems**, which often require high-privilege checks and robust encoding handling to ensure stability across different hardware and localizations. There is no evidence of "hidden" malicious actions (e.g., keylogging, stealthy file encryption, or remote shell behavior) in this specific sample.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1548 | Privilege Escalation | The code performs checks for administrator privileges (via `AllocateAndInitializeSid` and `CheckTokenMembership`) before initiating standard UI logic. |
| T1027 | Obfuscated Imports | The use of `LoadLibraryExW` and `GetProcAddress` in a loop to resolve functions at runtime is a common method used to hide the application's imported functions from static analysis. |
| T1055 | Process Injection | The utilization of `VirtualProtect` to modify memory page permissions before execution/resolution is a standard technique for preparing memory regions for code injection or manipulation. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `.gg/pvgc` (Note: This is part of a Discord invite link; while it points to a legitimate platform, such links are often used by threat actors for community coordination or distribution.)

**File paths / Registry keys**
*   *None identified.*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **C2/Communication Patterns:** The presence of a Discord invite link within the UI window title suggests a potential channel for actor communication or community building.
*   **Privilege Escalation Behavior:** A mandatory "Run as Administrator" check is implemented via `AllocateAndInitializeSid` and `CheckTokenMembership`. While common in legitimate system tools, it is a notable behavior for elevated access.
*   **Dynamic Loading:** The use of an automated loop involving `LoadLibraryExW` and `GetProcAddress` suggests the application dynamically resolves and loads functions at runtime to facilitate modularity or evasion.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: Medium

**Key evidence**:
*   **Loader Characteristics:** The sample utilizes advanced techniques such as `LoadLibraryExW` and `GetProcAddress` within automated loops, along with `VirtualProtect` to manage memory permissions. These are standard methods for a loader to resolve and execute functions dynamically.
*   **Lack of Explicit Malice:** No evidence of common malware behaviors (e.g., file encryption, keylogging, or unauthorized data exfiltration) was found. The complexity of the code suggests it may be a legitimate but highly engineered system-level application, such as an anti-cheat system or game engine middleware.
*   **Ambiguous Indicators:** While the "Run as Administrator" check and Discord link are common in both high-end security software/gaming tools and malware, they do not provide sufficient evidence to categorize it into a specific known malicious family.
