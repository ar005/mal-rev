# Threat Analysis Report

**Generated:** 2026-06-28 04:11 UTC
**Sample:** `02510b782a3f47a2cfce0b721a1530c325be15c3f540304681a92032ce22ee26_02510b782a3f47a2cfce0b721a1530c325be15c3f540304681a92032ce22ee26.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02510b782a3f47a2cfce0b721a1530c325be15c3f540304681a92032ce22ee26_02510b782a3f47a2cfce0b721a1530c325be15c3f540304681a92032ce22ee26.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 105,984 bytes |
| MD5 | `756d7ac8307cd3baa55b3e451e956d09` |
| SHA1 | `50f1cb0a33768f32e43ff39950d65ddfe00b889f` |
| SHA256 | `02510b782a3f47a2cfce0b721a1530c325be15c3f540304681a92032ce22ee26` |
| Overall entropy | 5.911 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768016438 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 55,296 | 6.42 | No |
| `.rdata` | 39,936 | 4.729 | No |
| `.data` | 3,072 | 2.065 | No |
| `.pdata` | 4,096 | 4.734 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.845 | No |

### Imports

**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`
**KERNEL32.dll**: `TerminateProcess`, `WriteConsoleW`, `CreateFileW`, `CreateFileA`, `GetFileSize`, `ReadFile`, `IsDebuggerPresent`, `CloseHandle`, `AddVectoredExceptionHandler`, `Sleep`, `GetCurrentProcess`, `GetCurrentThread`, `GetThreadContext`, `SetThreadContext`, `GlobalMemoryStatusEx`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **405** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
UVWAVAWH
A_A^_^]
t$ WAVAWH
T$@fA;Q
8.texu_A
D$0amsi
D$4.dll
D$$E;C
D$Hnpwp
D$Lw|m7
D$P}uu
D$`4~vv
D$h}BY_
D$l^JGj
D$pGGDH
D$xcD^Of
D$|XDO^
|$ AVH
WATAUAVAWH
A_A^A]A\_
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
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
u3HcH<H
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
D$0@8{
u$D8r(tH
D81u`L9r
uPD8r(tH
vWD8s(tH
u$D8r(tH
fD91u_L9r
uPD8r(tH
vVD8s(tH
UVWATAUAVAWH
PA_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
@USVWATAUAVH
,/<-w
H
D8t$ht
H
D8t$ht
H
A^A]A\_^[]
f9)u4H9j
u%@8j(t
v@8k(t
8D$@tH
l$ VWATAVAWH
L$&8\$&t,8Y
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180005de0` | `0x180005de0` | 13511 | ✓ |
| `fcn.180005da8` | `0x180005da8` | 13506 | ✓ |
| `fcn.1800025ac` | `0x1800025ac` | 11391 | ✓ |
| `fcn.1800024ac` | `0x1800024ac` | 2310 | ✓ |
| `fcn.18000263c` | `0x18000263c` | 2032 | ✓ |
| `fcn.1800078e4` | `0x1800078e4` | 1985 | ✓ |
| `fcn.18000d790` | `0x18000d790` | 1677 | ✓ |
| `fcn.180003c98` | `0x180003c98` | 1213 | ✓ |
| `fcn.18000bc90` | `0x18000bc90` | 1171 | ✓ |
| `fcn.180001ab0` | `0x180001ab0` | 1022 | ✓ |
| `fcn.18000acd0` | `0x18000acd0` | 922 | ✓ |
| `fcn.18000de40` | `0x18000de40` | 920 | ✓ |
| `fcn.18000a760` | `0x18000a760` | 920 | ✓ |
| `fcn.180002070` | `0x180002070` | 892 | ✓ |
| `fcn.1800074e8` | `0x1800074e8` | 862 | ✓ |
| `fcn.18000b2b4` | `0x18000b2b4` | 817 | ✓ |
| `fcn.18000c5dc` | `0x18000c5dc` | 815 | ✓ |
| `fcn.1800083b0` | `0x1800083b0` | 712 | ✓ |
| `section..text` | `0x180001000` | 689 | ✓ |
| `fcn.180002898` | `0x180002898` | 667 | ✓ |
| `fcn.18000800c` | `0x18000800c` | 623 | ✓ |
| `fcn.180009444` | `0x180009444` | 604 | ✓ |
| `fcn.180005ab0` | `0x180005ab0` | 589 | ✓ |
| `fcn.180004158` | `0x180004158` | 584 | ✓ |
| `fcn.180001620` | `0x180001620` | 570 | ✓ |
| `fcn.1800046f8` | `0x1800046f8` | 557 | ✓ |
| `fcn.18000a30c` | `0x18000a30c` | 555 | ✓ |
| `fcn.180002b58` | `0x180002b58` | 517 | ✓ |
| `fcn.180007e14` | `0x180007e14` | 501 | ✓ |
| `fcn.18000390c` | `0x18000390c` | 499 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001620.c`](code/fcn.180001620.c)
- [`code/fcn.180001ab0.c`](code/fcn.180001ab0.c)
- [`code/fcn.180002070.c`](code/fcn.180002070.c)
- [`code/fcn.1800024ac.c`](code/fcn.1800024ac.c)
- [`code/fcn.1800025ac.c`](code/fcn.1800025ac.c)
- [`code/fcn.18000263c.c`](code/fcn.18000263c.c)
- [`code/fcn.180002898.c`](code/fcn.180002898.c)
- [`code/fcn.180002b58.c`](code/fcn.180002b58.c)
- [`code/fcn.18000390c.c`](code/fcn.18000390c.c)
- [`code/fcn.180003c98.c`](code/fcn.180003c98.c)
- [`code/fcn.180004158.c`](code/fcn.180004158.c)
- [`code/fcn.1800046f8.c`](code/fcn.1800046f8.c)
- [`code/fcn.180005ab0.c`](code/fcn.180005ab0.c)
- [`code/fcn.180005da8.c`](code/fcn.180005da8.c)
- [`code/fcn.180005de0.c`](code/fcn.180005de0.c)
- [`code/fcn.1800074e8.c`](code/fcn.1800074e8.c)
- [`code/fcn.1800078e4.c`](code/fcn.1800078e4.c)
- [`code/fcn.180007e14.c`](code/fcn.180007e14.c)
- [`code/fcn.18000800c.c`](code/fcn.18000800c.c)
- [`code/fcn.1800083b0.c`](code/fcn.1800083b0.c)
- [`code/fcn.180009444.c`](code/fcn.180009444.c)
- [`code/fcn.18000a30c.c`](code/fcn.18000a30c.c)
- [`code/fcn.18000a760.c`](code/fcn.18000a760.c)
- [`code/fcn.18000acd0.c`](code/fcn.18000acd0.c)
- [`code/fcn.18000b2b4.c`](code/fcn.18000b2b4.c)
- [`code/fcn.18000bc90.c`](code/fcn.18000bc90.c)
- [`code/fcn.18000c5dc.c`](code/fcn.18000c5dc.c)
- [`code/fcn.18000d790.c`](code/fcn.18000d790.c)
- [`code/fcn.18000de40.c`](code/fcn.18000de40.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This second batch of disassembly significantly deepens the profile of this binary, moving it from a "suspicious downloader" to a **highly sophisticated loader or "packer" for advanced malware.**

The new code reveals advanced techniques for bypassing security software and preparing a decrypted payload in memory. Here is the updated analysis:

### 1. Advanced Evasion & Payload Unpacking (High-Risk)
The most critical discovery in this chunk is found in **`fcn.180001620`**. This function exhibits behavior typical of advanced "loaders" designed to bypass Endpoint Detection and Response (EDR) systems:

*   **System DLL Manipulation:** The code explicitly targets `ntdll.dll`. It uses `GetModuleHandleA`, `CreateFileA`, and `ReadFile` to pull a copy of the system's primary low-level library into its own memory space.
*   **Manual Memory Mapping & Patching:** After reading `ntdll.dll` into a buffer, it checks for the "MZ" header and looks for specific patterns (likely the `.text` section). It then calls **`VirtualProtect`**. 
*   **Dynamic Code Execution:** It identifies a specific memory region within its own copy of `ntdll._t_` (or a similar segment) and passes it to **`fcn.18000d790`**. Based on the previous analysis, `fcn.18000d790` is the decryption/unpacking routine.
*   **The Strategy:** By loading its own copy of `ntdll`, modifying it in memory, and "unpacking" a payload into that space, the malware seeks to execute its primary malicious functions (like process injection or API hooking) from a region that security software may not monitor as closely than the original system library.

### 2. Sophisticated Environment Awareness
Several functions (**`fcn.1800083b0`**, **`fcn.180009444`**, and **`fcn.180007e14`**) suggest the binary is "environment aware":

*   **Locale & Compatibility Checks:** The heavy use of `GetCPInfo` (Code Page) and multiple nested if-statements in `fcn.180009444` indicate that the program is checking for specific system configurations or localized settings before proceeding.
*   **Fallback Logic:** In `fcn.180009444`, there are numerous "fallback" routes (e.g., if a certain condition isn't met, jump to another block). This is often used by malware to ensure it can run on various versions of Windows or different localized systems while maintaining its hidden functionality.

### 3. Complex Data Management and "Staging"
The functions **`fcn.18000b2b4`** and **`fcn.18000390c`** show evidence of a sophisticated internal management system:

*   **Internal State Tracking:** The code uses complex offset calculations and custom data structures (e.g., `auStack_248`). It manages internal "pointers" to different stages of its execution.
*   **Contextual Execution:** These functions appear to be part of a wrapper that decides *how* to process certain blocks of data depending on what the malware has discovered during its environment checks. This helps prevent static analysis tools from easily identifying the primary "malicious" path through the code.

### 4. Enhanced Risk Assessment (Updated Summary)
The addition of this disassembly confirms and escalates the threat level of this binary:

*   **From Downloader to Loader/Unpacker:** The inclusion of `ntdll` manipulation and `VirtualProtect` usage indicates that this is not just a simple downloader; it is an **orchestrator**. Its primary job is to "unpack" and "de-obfuscate" the actual malicious payload (the "Stage 2" threat) directly in memory.
*   **Evasion of Security Products:** The deliberate use of `ntdll` as a landing zone for the unpacked code is a known technique used to evade EDR solutions that monitor standard API calls but might have blind spots when code is modified within private copies of system DLLs.
*   **Complexity & Professionalism:** The high level of nested logic, state management, and environmental checks suggests this was created by a sophisticated threat actor (e.g., an APT group or a professional malware developer).

### Conclusion for Incident Response:
This binary is **extremely dangerous**. It is designed to be the "front door" for a sophisticated infection. 
*   **Indicator of Compromise (IoC) Note:** Any detection of this binary should trigger an immediate, high-priority incident response.
*   **Behavioral Alert:** Security tools should look for:
    1.  `VirtualProtect` calls on memory regions associated with `ntdll.dll` or other system DLLs.
    2.  The process reading the physical file path of `ntdll.dll` to perform a manual copy into its own memory space.
    3.  Network connections to the previously identified domain (`tbox.moe`).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The binary utilizes a decryption/unpacking routine (`fcn.18000d790`) to de-obfuscate the primary payload in memory. |
| **T1497** | Virtualization/Sandbox Detection | The use of `GetCPInfo` and extensive "fallback" logic suggests the binary checks for specific hardware/OS configurations to detect and evade analysis environments. |
| **T1621** | Reflective Code Loading | The manual mapping, memory modification (`VirtualProtect`), and execution from a private copy of `ntdll.dll` indicate loading code without using standard OS loaders. |
| **T1055** | Process Injection | The binary acts as a "loader," moving the primary malicious payload into its own memory space to facilitate execution. |
| **T1106** | Native API | The deliberate use of `ntdll` manipulation is a known tactic to bypass EDR security products that monitor higher-level Win32 APIs. |
| **T1562.001** | Impair Defenses: Disable or Modify System Artifacts | By creating a private copy of `ntdll.dll` and modifying it in memory, the malware seeks to evade monitoring hooks placed on system artifacts. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `tbox.moe` (Identified as a C2 domain)
*   `https://files.cabE_NYEN_d[NE~YGj` (Potential malicious URL fragment/path)

**File paths / Registry keys**
*   *(None identified. Note: `C:\Windows\System32\ntdll.dll` was omitted as it is a standard system path.)*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36`
*   **C2 Pattern/Behavioral Indicator:** Usage of `VirtualProtect` to modify memory regions associated with `ntdll.dll`.
*   **C2 Pattern/Behavioral Indicator:** Manual loading and modification of `ntdll.dll` into a buffer for payload de-obfuscation.

---

## Malware Family Classification

1. **Malware family**: Unknown (Potential custom loader/orchestrator)
2. **Malware type**: Loader / Packer
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Evasion Tactics:** The sample utilizes a sophisticated "Loader" strategy by copying `ntdll.dll` into its own memory space and using `VirtualProtect` to unpack payloads; this is a deliberate technique designed to bypass EDR (Endpoint Detection and Response) systems that monitor standard API calls.
*   **Sophisticated Orchestration:** Analysis reveals the transition from a simple downloader to an "orchestrator" capable of complex state management, internal tracking, and multi-stage de-obfuscation of "Stage 2" payloads.
*   **Anti-Analysis/Evasion Features:** The inclusion of `GetCPInfo` calls combined with extensive "fallback" logic indicates a high level of environmental awareness designed to detect sandbox environments and ensure execution across varied localizations.
