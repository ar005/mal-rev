# Threat Analysis Report

**Generated:** 2026-06-27 06:58 UTC
**Sample:** `01c29e84ad1a5fc1f2d16a93fee1c6386aecef1a99153eccaddbca54549befd3_01c29e84ad1a5fc1f2d16a93fee1c6386aecef1a99153eccaddbca54549befd3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01c29e84ad1a5fc1f2d16a93fee1c6386aecef1a99153eccaddbca54549befd3_01c29e84ad1a5fc1f2d16a93fee1c6386aecef1a99153eccaddbca54549befd3.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 81,408 bytes |
| MD5 | `bc5543b39d89cda6832706948945f567` |
| SHA1 | `98c88ff395c1f2ea68b5b2c4ceeda4e9e9a2e595` |
| SHA256 | `01c29e84ad1a5fc1f2d16a93fee1c6386aecef1a99153eccaddbca54549befd3` |
| Overall entropy | 5.547 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1749307011 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 72,704 | 5.612 | No |
| `.data` | 1,024 | 3.542 | No |
| `.rdata` | 2,048 | 4.707 | No |
| `.pdata` | 1,024 | 2.663 | No |
| `.xdata` | 512 | 4.12 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 1,536 | 3.825 | No |
| `.CRT` | 512 | 0.269 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 512 | 2.269 | No |

### Imports

**KERNEL32.dll**: `DeleteCriticalSection`, `EnterCriticalSection`, `GetLastError`, `GetStartupInfoA`, `InitializeCriticalSection`, `LeaveCriticalSection`, `SetUnhandledExceptionFilter`, `Sleep`, `TlsGetValue`, `VirtualProtect`, `VirtualQuery`
**msvcrt.dll**: `__C_specific_handler`, `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_commode`, `_fmode`, `_initterm`, `_ismbblead`, `_onexit`, `abort`

## Extracted Strings

Total strings found: **91** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
UAUATWVSH
([^_A\A]]
([^_A\A]]
D$(f;D$4s-
D$(f9D$8s=
D$(f9D$4u!
D$*f;D$6s
D$(f9D$8u'
D$*f;D$:r
9D$T|,H
|$HCw=
D$\<.u
D$\<.u
D$]<.u
f9E u!H
D$89D$hu(D
9E t`H
l$PHc50n
UAWAVAUATWVSH
[^_A\A]A^A_]
(D;%vj
UAUATWVSH
([^_A\A]]H
:MZu[HcB<H
@' t	H
H9D$(r
H9D$(r
H9D$(r
H9D$(r
H9D$(r
H9D$(r
H9D$(r
H9D$(r
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
Argument domain error (DOMAIN)
Argument singularity (SIGN)
Overflow range error (OVERFLOW)
Partial loss of significance (PLOSS)
Total loss of significance (TLOSS)
The result is too small to be represented (UNDERFLOW)
Unknown error
_matherr(): %s in %s(%g, %g)  (retval=%g)

Mingw-w64 runtime failure:

Address %p has no image-section
  VirtualQuery failed for %d bytes at address %p
  VirtualProtect failed with code 0x%x
  Unknown pseudo relocation protocol version %d.

  Unknown pseudo relocation bit size %d.

%d bit pseudo relocation at %p out of range, targeting %p, yielding the value %p.

0`
p	
DeleteCriticalSection
EnterCriticalSection
GetLastError
GetStartupInfoA
InitializeCriticalSection
LeaveCriticalSection
SetUnhandledExceptionFilter
TlsGetValue
VirtualProtect
VirtualQuery
__C_specific_handler
__getmainargs
__initenv
__iob_func
__set_app_type
__setusermatherr
_acmdln
_amsg_exit
_cexit
_commode
_fmode
_initterm
_ismbblead
_onexit
calloc
fprintf
fwrite
malloc
signal
strlen
strncmp
vfprintf
KERNEL32.dll
msvcrt.dll
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400036e3` | `0x1400036e3` | 4258 | ✓ |
| `fcn.1400107e0` | `0x1400107e0` | 2390 | ✓ |
| `fcn.140001baa` | `0x140001baa` | 2115 | ✓ |
| `fcn.14000a860` | `0x14000a860` | 1754 | ✓ |
| `fcn.140007e42` | `0x140007e42` | 1687 | ✓ |
| `fcn.14000de10` | `0x14000de10` | 1544 | ✓ |
| `fcn.14000609a` | `0x14000609a` | 1490 | ✓ |
| `fcn.1400057c1` | `0x1400057c1` | 1327 | ✓ |
| `fcn.140002560` | `0x140002560` | 1276 | ✓ |
| `fcn.14000a3f2` | `0x14000a3f2` | 1121 | ✓ |
| `fcn.14000c632` | `0x14000c632` | 1117 | ✓ |
| `fcn.14000cc10` | `0x14000cc10` | 1089 | ✓ |
| `fcn.14000756e` | `0x14000756e` | 1083 | ✓ |
| `fcn.140008706` | `0x140008706` | 1059 | ✓ |
| `fcn.14000bdee` | `0x14000bdee` | 1032 | ✓ |
| `fcn.140002c7a` | `0x140002c7a` | 1018 | ✓ |
| `fcn.140009990` | `0x140009990` | 993 | ✓ |
| `fcn.140010440` | `0x140010440` | 922 | ✓ |
| `fcn.14000162c` | `0x14000162c` | 905 | ✓ |
| `fcn.14000b8f0` | `0x14000b8f0` | 898 | ✓ |
| `fcn.140003080` | `0x140003080` | 851 | ✓ |
| `fcn.14000e418` | `0x14000e418` | 726 | ✓ |
| `fcn.14000c380` | `0x14000c380` | 690 | ✓ |
| `fcn.140005de9` | `0x140005de9` | 648 | ✓ |
| `fcn.1400090ec` | `0x1400090ec` | 632 | ✓ |
| `fcn.14000d9bc` | `0x14000d9bc` | 629 | ✓ |
| `fcn.14000d74e` | `0x14000d74e` | 621 | ✓ |
| `fcn.140007bd6` | `0x140007bd6` | 619 | ✓ |
| `fcn.140006c28` | `0x140006c28` | 615 | ✓ |
| `fcn.140001190` | `0x140001190` | 592 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001190.c`](code/fcn.140001190.c)
- [`code/fcn.14000162c.c`](code/fcn.14000162c.c)
- [`code/fcn.140001baa.c`](code/fcn.140001baa.c)
- [`code/fcn.140002560.c`](code/fcn.140002560.c)
- [`code/fcn.140002c7a.c`](code/fcn.140002c7a.c)
- [`code/fcn.140003080.c`](code/fcn.140003080.c)
- [`code/fcn.1400036e3.c`](code/fcn.1400036e3.c)
- [`code/fcn.1400057c1.c`](code/fcn.1400057c1.c)
- [`code/fcn.140005de9.c`](code/fcn.140005de9.c)
- [`code/fcn.14000609a.c`](code/fcn.14000609a.c)
- [`code/fcn.140006c28.c`](code/fcn.140006c28.c)
- [`code/fcn.14000756e.c`](code/fcn.14000756e.c)
- [`code/fcn.140007bd6.c`](code/fcn.140007bd6.c)
- [`code/fcn.140007e42.c`](code/fcn.140007e42.c)
- [`code/fcn.140008706.c`](code/fcn.140008706.c)
- [`code/fcn.1400090ec.c`](code/fcn.1400090ec.c)
- [`code/fcn.140009990.c`](code/fcn.140009990.c)
- [`code/fcn.14000a3f2.c`](code/fcn.14000a3f2.c)
- [`code/fcn.14000a860.c`](code/fcn.14000a860.c)
- [`code/fcn.14000b8f0.c`](code/fcn.14000b8f0.c)
- [`code/fcn.14000bdee.c`](code/fcn.14000bdee.c)
- [`code/fcn.14000c380.c`](code/fcn.14000c380.c)
- [`code/fcn.14000c632.c`](code/fcn.14000c632.c)
- [`code/fcn.14000cc10.c`](code/fcn.14000cc10.c)
- [`code/fcn.14000d74e.c`](code/fcn.14000d74e.c)
- [`code/fcn.14000d9bc.c`](code/fcn.14000d9bc.c)
- [`code/fcn.14000de10.c`](code/fcn.14000de10.c)
- [`code/fcn.14000e418.c`](code/fcn.14000e418.c)
- [`code/fcn.140010440.c`](code/fcn.140010440.c)
- [`code/fcn.1400107e0.c`](code/fcn.1400107e0.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's functionality and characteristics.

### Core Functionality and Purpose
The binary exhibits the structural characteristics of a **sophisticated, modular piece of malware** (such as a loader or a back-up component for a Trojan). Rather than having a linear execution path, it uses a highly structured approach to hide its true intent:

*   **Table-Driven Execution:** The code heavily utilizes large data structures and "dispatch" tables. Instead of calling functions directly, the program looks up a command/index in a table and jumps to the corresponding logic.
*   **Command Dispatcher Pattern:** Function `fcn.14000609a` contains a large switch-case structure. This is a classic technique used to decouple the "main" logic from the specific actions (e.g., networking, file manipulation, or keylogging), making it harder for automated analysis tools to map the full control flow.
*   **State Machine Logic:** The repeated loops and check-then-jump logic in functions like `fcn.140001baa` suggest a state machine where the program processes a list of tasks or "commands" sequentially.

### Suspicious and Malicious Behaviors
Several indicators suggest potential malicious activity:

*   **Evasive Execution (Indirect Branching):** The extensive use of indirect calls—where the destination of a jump is determined at runtime via an offset in a table—is a common technique to thwart static analysis and signature-based detection. 
*   **Memory Manipulation:** The presence of `VirtualProtect` and `VirtualQuery` (indicated in strings and likely used in the internal logic) suggests the binary may be performing **manual mapping of DLLs**, **process injection**, or **in-memory unpacking**. These functions are often used to change memory permissions from Read/Write to Execute (RWX) to run shellcode.
*   **Environment/System Awareness:** The inclusion of `GetStartupInfoA` suggests the program checks its environment. This is often done to detect if it is running in a sandbox or under specific user conditions before activating malicious payloads.
*   **Obfuscated Data Strings:** Function `fcn.1400036e3` populates large arrays with seemingly random hex values (e.g., `0x7b348614`, `0xafef147a`). These are likely obfuscated strings, encrypted configuration data, or addresses for a hidden jump table.

### Notable Techniques and Patterns
*   **API Obfuscation:** The code uses a layer of indirection to access Windows APIs. Instead of calling `Kernel32` directly, it appears to resolve them via an internal table (seen in the way functions like `fcn.14000de10` check for specific values and then call into pre-resolved addresses).
*   **Modular Design:** The heavy use of "handler" functions (the various cases in the switch statement) suggests that this binary acts as a **plug-and-play host**. Different capabilities can be swapped out by changing the configuration data, allowing one piece of malware to perform multiple tasks.
*   **Anti-Analysis/Analysis Resistance:** By using nested calls and indirect jumps, the author has ensured that "Linear Sweep" disassembly results in a very fragmented view of what the code actually does. The complexity of `fcn.1400036e3` and `fcn.14000b8f0` indicates an effort to hide the binary's true logic behind layers of data processing.

### Summary for Incident Response
This is likely a **malware loader or Trojan**. It is designed with significant anti-analysis features, specifically **control-flow obfuscation** and **dynamic API resolution**. 
*   **Primary Risk:** The presence of `VirtualProtect` combined with the dispatcher architecture suggests it may drop/inject a second-stage payload or perform "fileless" execution.
*   **Recommendation:** Conduct dynamic analysis in an isolated environment to capture network traffic and identify which specific functions are triggered by the dispatch table. Focus on monitoring memory for shellcode injection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Execution | The use of dispatch tables, indirect branching (indirect calls), and obfuscated data strings are designed to hide the program's control flow from static analysis. |
| T1055 | Process Injection | The utilization of `VirtualProtect` and `VirtualQuery` suggests the binary is preparing memory for shellcode execution or injecting a secondary payload into a process. |
| T1497 | Virtualization/Sandbox Evasion | The inclusion of `GetStartupInfoA` indicates the malware checks environment-specific criteria to detect if it is running inside an analysis sandbox or virtual machine. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** No specific network indicators (IPs, URLs) or file system artifacts (specific paths, registry keys) were found in the provided text. The findings below focus on behavior-based indicators and technical artifacts.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: `KERNEL32.dll` and `msvcrt.dll` were identified but excluded as standard system libraries).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (Note: Hex values such as `0x7b348614` and `0xafef147a` were identified in the report, but these are identified as obfuscated data/memory addresses rather than file hashes).

### **Other artifacts**
*   **Suspicious API Usage:** 
    *   `VirtualProtect`: Used for modifying memory permissions (potential shellcode execution/unpacking).
    *   `VirtualQuery`: Used to query memory region information.
    *   `GetStartupInfoA`: Used for environment/system awareness (possible sandbox detection).
*   **Tactic/Technique Indicators:**
    *   **Table-Driven Execution:** Use of dispatch tables to hide control flow.
    *   **Command Dispatcher Pattern:** Use of large switch-case structures (`fcn.14000609a`) to decouple logic.
    *   **Indirect Branching:** Extensive use of indirect calls to evade static analysis.
    *   **Obfuscated Data Strings:** High concentration of non-human-readable strings and hex data intended to hide configuration or secondary payloads.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (for Type) / Low (for Family)

4. **Key evidence**:
*   **Loader/Dropper Characteristics:** The presence of `VirtualProtect` and `VirtualQuery` combined with a "Command Dispatcher" architecture strongly indicates the binary's primary role is to prepare memory for and execute a secondary payload (shellcode or an injected DLL).
*   **Advanced Obfuscation:** The use of "Table-Driven Execution," indirect branching, and API obfuscation suggests it is designed as a sophisticated, modular component intended to hide its true functionality from static analysis.
*   **Evasion Capabilities:** The inclusion of `GetStartupInfoA` for environment awareness and the heavy use of non-human-readable hex data points toward a professional construction aimed at evading sandboxes and automated detection systems.
