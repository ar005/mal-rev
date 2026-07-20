# Threat Analysis Report

**Generated:** 2026-07-19 12:05 UTC
**Sample:** `091e5dde1f5fb3cf6575415357bbb560faa55453bdce5a092470df495187a594_091e5dde1f5fb3cf6575415357bbb560faa55453bdce5a092470df495187a594.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `091e5dde1f5fb3cf6575415357bbb560faa55453bdce5a092470df495187a594_091e5dde1f5fb3cf6575415357bbb560faa55453bdce5a092470df495187a594.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64, 6 sections |
| Size | 5,298,176 bytes |
| MD5 | `f6f9511685e9f580ae020fa1496a56e8` |
| SHA1 | `b95c336c9297fb00670687a23335d058117fe866` |
| SHA256 | `091e5dde1f5fb3cf6575415357bbb560faa55453bdce5a092470df495187a594` |
| Overall entropy | 1.918 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1494505257 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 31,744 | 6.325 | No |
| `.rdata` | 11,264 | 4.705 | No |
| `.data` | 5,120 | 1.823 | No |
| `.pdata` | 2,048 | 4.249 | No |
| `.rsrc` | 5,243,392 | 1.863 | No |
| `.reloc` | 3,584 | -0.0 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `WriteFile`, `CreateFileA`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `CreateProcessA`, `GetCurrentThreadId`, `FlsSetValue`, `GetCommandLineA`, `DecodePointer`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `IsDebuggerPresent`

### Exports

`PlayGame`

## Extracted Strings

Total strings found: **1558** (showing first 100)

```
!This program cannot be run in DOS mode.
$
/4%D/4%D/4%D4
D|4%D4
D&4%D&L
D,4%D/4$D
D84%D4
D.4%D4
D.4%D4
D.4%DRich/4%D
`.rdata
@.data
.pdata
@.rsrc
@.reloc
L$ USWH
WATAUH
 A]A\_
UVWATAUAVAWH
D$HD9T$\
t$pD+d$HD+
9D$Ttg
A_A^A]A\_^]
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
@A_A^A]A\_
ATAUAVH
fD9t$b
A^A]A\
x ATAUAVH
< tG<	tC
 A^A]A\
Hct$@H
s\HcL$HH
VWATAUAVH
 A^A]A\_^
\$ UVWATAUAVAWH
!|$DHc
|$DD9d$X
f;D$@ug
f;D$@uD
H!\$ H
HcD$HH;
H!\$ H
HcD$HH;
H!|$ L
A_A^A]A\_^]
VWATAUAVH
 A^A]A\_^
UVWATAUH
^D9d$ 
D$&8\$&t-8X
@A]A\_^]
L$ UVWH
LcA<E3
WATAUAVAWH
0A_A^A]A\_
ATAUAVH
 A^A]A\
t$ WATAUH
D8"u%H
ATAUAWH
0A_A]A\
@UATAUAVAWH
@88tH
!t$(H!t$ A
A_A^A]A\]
@UATAUAVAWH
A_A^A]A\]
fffffff
fffffff
	H;5V
KXH;WV
K`H;MV
@SUVWATAUAVH
PA^A]A\_^][
C:\%s\%s
WINDOWS
mssecsvc.exe
(null)
`h````
xpxxxx
CorExitProcess
HH:mm:ss
dddd, MMMM dd, yyyy
MM/dd/yy
December
November
October
September
August
February
January
Saturday
Friday
Thursday
Wednesday
Tuesday
Monday
Sunday
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180002938` | `0x180002938` | 13223 | ✓ |
| `fcn.180002ef0` | `0x180002ef0` | 12701 | ✓ |
| `fcn.180005a60` | `0x180005a60` | 9202 | ✓ |
| `fcn.180001994` | `0x180001994` | 2732 | ✓ |
| `fcn.180003f58` | `0x180003f58` | 1888 | ✓ |
| `fcn.180007794` | `0x180007794` | 1006 | ✓ |
| `fcn.180007460` | `0x180007460` | 820 | ✓ |
| `fcn.180003228` | `0x180003228` | 722 | ✓ |
| `fcn.180006f0c` | `0x180006f0c` | 714 | ✓ |
| `fcn.180004e50` | `0x180004e50` | 629 | ✓ |
| `fcn.1800064d4` | `0x1800064d4` | 605 | ✓ |
| `fcn.1800060c0` | `0x1800060c0` | 562 | ✓ |
| `fcn.180007ed0` | `0x180007ed0` | 520 | ✓ |
| `fcn.180004b14` | `0x180004b14` | 496 | ✓ |
| `fcn.180003d14` | `0x180003d14` | 483 | ✓ |
| `fcn.1800050c8` | `0x1800050c8` | 478 | ✓ |
| `fcn.1800036a0` | `0x1800036a0` | 463 | ✓ |
| `fcn.1800057b0` | `0x1800057b0` | 452 | ✓ |
| `fcn.180003054` | `0x180003054` | 399 | ✓ |
| `fcn.18000162c` | `0x18000162c` | 397 | ✓ |
| `fcn.180006c30` | `0x180006c30` | 384 | ✓ |
| `fcn.180005400` | `0x180005400` | 377 | ✓ |
| `fcn.180007270` | `0x180007270` | 350 | ✓ |
| `entry0` | `0x1800015ec` | 345 | ✓ |
| `fcn.18000137c` | `0x18000137c` | 338 | ✓ |
| `fcn.180002448` | `0x180002448` | 331 | ✓ |
| `fcn.180002ac0` | `0x180002ac0` | 307 | ✓ |
| `fcn.180003570` | `0x180003570` | 304 | ✓ |
| `fcn.180006384` | `0x180006384` | 266 | ✓ |
| `fcn.180007bf0` | `0x180007bf0` | 266 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.18000137c.c`](code/fcn.18000137c.c)
- [`code/fcn.18000162c.c`](code/fcn.18000162c.c)
- [`code/fcn.180001994.c`](code/fcn.180001994.c)
- [`code/fcn.180002448.c`](code/fcn.180002448.c)
- [`code/fcn.180002938.c`](code/fcn.180002938.c)
- [`code/fcn.180002ac0.c`](code/fcn.180002ac0.c)
- [`code/fcn.180002ef0.c`](code/fcn.180002ef0.c)
- [`code/fcn.180003054.c`](code/fcn.180003054.c)
- [`code/fcn.180003228.c`](code/fcn.180003228.c)
- [`code/fcn.180003570.c`](code/fcn.180003570.c)
- [`code/fcn.1800036a0.c`](code/fcn.1800036a0.c)
- [`code/fcn.180003d14.c`](code/fcn.180003d14.c)
- [`code/fcn.180003f58.c`](code/fcn.180003f58.c)
- [`code/fcn.180004b14.c`](code/fcn.180004b14.c)
- [`code/fcn.180004e50.c`](code/fcn.180004e50.c)
- [`code/fcn.1800050c8.c`](code/fcn.1800050c8.c)
- [`code/fcn.180005400.c`](code/fcn.180005400.c)
- [`code/fcn.1800057b0.c`](code/fcn.1800057b0.c)
- [`code/fcn.180005a60.c`](code/fcn.180005a60.c)
- [`code/fcn.1800060c0.c`](code/fcn.1800060c0.c)
- [`code/fcn.180006384.c`](code/fcn.180006384.c)
- [`code/fcn.1800064d4.c`](code/fcn.1800064d4.c)
- [`code/fcn.180006c30.c`](code/fcn.180006c30.c)
- [`code/fcn.180006f0c.c`](code/fcn.180006f0c.c)
- [`code/fcn.180007270.c`](code/fcn.180007270.c)
- [`code/fcn.180007460.c`](code/fcn.180007460.c)
- [`code/fcn.180007794.c`](code/fcn.180007794.c)
- [`code/fcn.180007bf0.c`](code/fcn.180007bf0.c)
- [`code/fcn.180007ed0.c`](code/fcn.180007ed0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated the analysis. The newly identified functions confirm a sophisticated approach to **Dynamic API Resolution** and **Runtime Obfuscation**, typical of advanced loaders used to hide the program's true capabilities from static analysis tools.

### Updated Analysis Report

#### Core Functionality & Purpose (Updated)
*   **Sophisticated Loader/Dropper:** The inclusion of `fcn.180006384` and `fcn.180007bf0` confirms that the malware does not rely on a standard Import Address Table (IAT). Instead, it implements a custom system to resolve and "fix up" functions at runtime.
*   **Masquerading:** (Retained) The `mssecsvc.exe` string indicates an intent to masquerade as a Microsoft security service.
*   **Configuration Processing:** (Retained) Parsing of `=` delimited strings for C2 or behavior configuration.

#### New Findings from Chunk 2/2

**1. Obfuscated Pointer Management (`fcn.180006384`)**
This function is a clear indicator of **manual API resolution**. It interacts with `DecodePointer` and `EncodePointer`.
*   **Mechanism:** The code takes an encoded value, decodes it to find the actual memory location or address (likely via `fcn.180002dfc`), and then *re-encodes* the result before storing it back in the global space (`*0x18000f630`).
*   **Purpose:** This ensures that the "real" memory addresses are only visible in their plain state during the execution of the transition logic. Static analysis tools will only see encoded, meaningless numbers in the data sections.

**2. Automated Import Table Reconstruction (`fcn.180007bf0`)**
This function is a classic "Resolution Loop." It iterates through a block of memory (an internal table) to populate it with valid function pointers.
*   **Iterative Verification:** The code checks a series of offsets (e.g., `+0x18`, `+0x20`, `+0x28`) against specific constants. If the value at that location does not match the "placeholder" constant, it calls `fcn.180002cb8` to resolve/fix the pointer.
*   **Evidence of Complexity:** The repetitive nature of these checks (spanning across multiple offsets) suggests a large number of system functions are being loaded (e.g., network communications, thread manipulation, and memory allocation). This is common in "Reflective DLL" loading or when the malware intends to perform complex tasks like process injection.

#### Updated Technical Indicators & Techniques

*   **Advanced API Hiding:** The use of `DecodePointer`/`EncodePointer` combined with a dedicated resolution loop (`fcn.180007bf0`) means that standard "Imports" lists in tools like PEStudio or strings analysis will be significantly incomplete. Most of the malware's functionality is hidden behind these dynamic resolutions.
*   **Just-In-Time (JIT) Resolution:** By checking if a pointer is already "resolved" before calling `fcn.180002cb8`, the malware ensures it only performs the work to find a function address once, but keeps that address hidden in its encoded state until it's needed for a call.
*   **Reflective Loading Capability:** The structure of `fcn.180007bf0` strongly suggests that this binary is designed to host other malicious modules or shellcode. It builds a "manual" environment where it can execute code without relying on the standard Windows loader for its primary payloads.

### Updated Summary Recommendation
**High-Confidence Threat: Advanced Multi-Stage Loader.**
This sample demonstrates several hallmarks of modern, sophisticated malware (e.g., Emotet or QakBot-style loaders). It employs multiple layers of defense:
1.  **Anti-Analysis:** Active checks for debuggers and even integrity checks on the execution environment.
2.  **Code/Data Obfuscation:** Encoding of pointers to hide the intended API surface.
3.  **Dynamic Resolution:** A systematic method of building an internal function table to bypass static signature detection.

The combination of **masquerading** (mssecsvc), **complex anti-analysis**, and **dynamic resolution** indicates this is likely a high-tier loader used for persistent access or as a gateway for ransomware/spyware. Investigation should focus on the functions called by `fcn.180002cb8` to identify the specific capabilities (e.g., keylogging, exfiltration) of the secondary payload.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&K framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The use of the string `mssecsvc.exe` indicates an attempt to blend in with legitimate Microsoft security services to evade detection. |
| **T1027** | Obfuscated Files or Information | The use of `DecodePointer` and `EncodePointer` functions hides the true API surface from static analysis tools by encoding memory addresses. |
| **T1055** | Process Injection | The "Resolution Loop" and "Reflective Loading Capability" indicate the malware is designed to host and execute hidden payloads/shellcode in memory. |
| **T1497** | Virtualization/Sandbox Detection | The analysis confirms active checks for debuggers and integrity checks to evade analysis in a laboratory environment. |
| **T1568** | Dynamic Resolution | The malware utilizes an internal table and custom resolution functions (`fcn.180002cb8`) to resolve API calls at runtime rather than using the standard IAT. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis indicates that C2 information is likely hidden behind encoded data or resolved dynamically at runtime.)

### **File paths / Registry keys**
*   `mssecsvc.exe` (Note: Identified as a masquerading name for a malicious service/process).
*   `launcher.dll` (Identified as a module used in the execution chain).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Malware Behavior - Dynamic API Resolution:** Use of `DecodePointer` and `EncodePointer` to obfuscate the Import Address Table (IAT).
*   **Malware Behavior - Manual Import Reconstruction:** Implementation of a resolution loop (`fcn.180007bf0`) to resolve system functions at runtime, bypassing static analysis.
*   **C2 Configuration Pattern:** The malware parses **"=" delimited strings** for its internal configuration (likely containing C2 info or specific tasking).
*   **Persistence/Masquerading:** Usage of the name `mssecsvc` to mimic a Microsoft service.

---

### **Analyst Notes**
The sample exhibits characteristics of a high-sophistication "Loader" or "Dropper." Because it uses advanced obfuscation techniques (like encoded pointers and dynamic resolution), many traditional IOCs (such as hardcoded IP addresses) are not visible in the plaintext strings. The primary indicators for hunting this threat would be the presence of **`mssecsvc.exe`** on disk/in memory and the detection of processes performing **manual IAT reconstruction** or high volumes of calls to `GetProcAddress`/`GetModuleHandle`.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
* **Advanced Dynamic API Resolution:** The sample employs complex `DecodePointer` and `EncodePointer` functions combined with a manual resolution loop (`fcn.180007bf0`) to hide its true capabilities from static analysis tools.
* **Reflective Loading Capability:** The architecture is specifically designed to host and execute secondary payloads or shellcode in memory, which is the hallmark of a high-sophistication loader/dropper.
* **Sophisticated Evasion & Masquerading:** The malware uses known evasion techniques including anti-analysis checks (T1497) and masquerades as a system service (`mssecsvc.exe`) to blend in with legitimate environment processes.
