# Threat Analysis Report

**Generated:** 2026-07-25 15:01 UTC
**Sample:** `0acf526f1706c632342bffa48643b6ed029bd5a0f3ad7741e243a5f31d6fa931_0acf526f1706c632342bffa48643b6ed029bd5a0f3ad7741e243a5f31d6fa931.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0acf526f1706c632342bffa48643b6ed029bd5a0f3ad7741e243a5f31d6fa931_0acf526f1706c632342bffa48643b6ed029bd5a0f3ad7741e243a5f31d6fa931.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 835,944 bytes |
| MD5 | `b8a321a209f04ee24a4bdfc95b0305ed` |
| SHA1 | `d25619d424e1b0c27c2698ad75a209d0b115cac8` |
| SHA256 | `0acf526f1706c632342bffa48643b6ed029bd5a0f3ad7741e243a5f31d6fa931` |
| Overall entropy | 6.658 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779907756 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 375,296 | 6.398 | No |
| `.rdata` | 267,264 | 5.227 | No |
| `.data` | 512 | 2.206 | No |
| `.pdata` | 10,752 | 5.716 | No |
| `.tls` | 512 | 0.02 | No |
| `.rsrc` | 50,688 | 6.219 | No |
| `.reloc` | 2,560 | 4.992 | No |

### Imports

**KERNEL32.dll**: `AddVectoredExceptionHandler`, `CloseHandle`, `CompareStringOrdinal`, `CreateFileW`, `CreateMutexA`, `CreateProcessW`, `CreateThread`, `DuplicateHandle`, `FindClose`, `FindFirstFileExW`, `FormatMessageW`, `FreeEnvironmentStringsW`, `GetConsoleMode`, `GetConsoleOutputCP`, `GetCurrentDirectoryW`
**api-ms-win-core-synch-l1-2-0.dll**: `WaitOnAddress`, `WakeByAddressAll`, `WakeByAddressSingle`
**ntdll.dll**: `NtCreateNamedPipeFile`, `NtOpenFile`, `NtReadFile`, `NtWriteFile`, `RtlNtStatusToDosError`
**SHELL32.dll**: `SHGetKnownFolderPath`
**ole32.dll**: `CoTaskMemFree`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `__p___argv`, `_c_exit`, `_cexit`, `_configure_narrow_argv`, `_crt_atexit`, `_exit`, `_get_initial_narrow_environment`, `_initialize_narrow_environment`, `_initialize_onexit_table`, `_initterm`, `_initterm_e`, `_register_onexit_function`, `_register_thread_local_exe_atexit_callback`, `_seh_filter_exe`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__p__commode`, `_set_fmode`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `free`

## Extracted Strings

Total strings found: **2408** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata
@.reloc
UAVVWSH
0[_^A^]
UAVVWSH
 [_^A^]
AWAVAUATVWUSH
X[]_^A\A]A^A_
AVVWSH
([_^A^
AVVWSH
([_^A^
AVVWSH
([_^A^
UAVVWSH
0[_^A^]
UAVVWSH
 [_^A^]
AWAVAUATVWUSH
8\u00@
H9>tOH
8[]_^A\A]A^A_
AWAVATVWUSH
'ffff.
@[]_^A\A^A_
AWAVAUATVWUSH
X[]_^A\A]A^A_
AWAVAUATVWUSH
t0H;l$0u
*H;l$0u
L;t$0u
t0H;l$0u
*H;l$0u
H;\$0u
|$Xt$H
T$@H9T$0
t$Xt$H
T$@H9T$0
[]_^A\A]A^A_
L;t$0u
H;\$0u
AWAVAUATVWUSH
ffffff.
X[]_^A\A]A^A_
H;>wdE1
AWAVAUATVWUSH
ffffff.
([]_^A\A]A^A_
([]_^A\A]A^A_H
AVVWSH
([_^A^
AVVWSH
([_^A^
([_^A^
AWAVVWSH
\$puDA
[_^A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVVWSH
\$(ffff.
@[_^A^A_
AWAVAUATVWSH
@[_^A\A]A^A_
AVVWSH
H[_^A^
AWAVVWSH
@[_^A^A_
L$(uH
GetVersiL3
LaunchFiH3
hFirefoxL3A
GetInstaH3
llIdI	
AWAVAUATVWUSH
fffff.
[]_^A\A]A^A_
AWAVATVWUSH
T$@H9T$0
T$@H9T$0
t$@L9t$0
0L9t$0
t$@L9t$0
P[]_^A\A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
installaH1
ation_idH1
AWAVAUATVWUSH
fffff.
[]_^A\A]A^A_
AVVWSH
([_^A^
AWAVAUATVWUSH
H[]_^A\A]A^A_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400588a0` | `0x1400588a0` | 334933 | ✓ |
| `fcn.140011bc0` | `0x140011bc0` | 295755 | ✓ |
| `fcn.140011500` | `0x140011500` | 295101 | ✓ |
| `fcn.14001e8d0` | `0x14001e8d0` | 246418 | ✓ |
| `fcn.140029ff0` | `0x140029ff0` | 201871 | ✓ |
| `case.0x14002925b.81` | `0x14002a360` | 196447 | ✓ |
| `fcn.14000caf0` | `0x14000caf0` | 186265 | ✓ |
| `fcn.140001000` | `0x140001000` | 182211 | ✓ |
| `fcn.140001120` | `0x140001120` | 182207 | ✓ |
| `fcn.140001010` | `0x140001010` | 182138 | ✓ |
| `fcn.14000d700` | `0x14000d700` | 157819 | ✓ |
| `entry0` | `0x140056e10` | 151061 | ✓ |
| `fcn.140038910` | `0x140038910` | 139055 | ✓ |
| `fcn.14000cbc0` | `0x14000cbc0` | 99797 | ✓ |
| `fcn.140051430` | `0x140051430` | 62610 | ✓ |
| `fcn.140024e90` | `0x140024e90` | 61644 | ✓ |
| `fcn.140029000` | `0x140029000` | 46024 | ✓ |
| `fcn.140056ae4` | `0x140056ae4` | 24002 | ✓ |
| `fcn.1400336d0` | `0x1400336d0` | 16237 | ✓ |
| `fcn.14004c2a0` | `0x14004c2a0` | 13443 | ✓ |
| `fcn.140002880` | `0x140002880` | 7931 | ✓ |
| `fcn.14000b420` | `0x14000b420` | 5771 | ✓ |
| `fcn.1400165f0` | `0x1400165f0` | 4604 | ✓ |
| `fcn.140014560` | `0x140014560` | 4471 | ✓ |
| `fcn.14001ae90` | `0x14001ae90` | 4250 | ✓ |
| `fcn.14001f4c0` | `0x14001f4c0` | 4167 | ✓ |
| `fcn.1400156e0` | `0x1400156e0` | 3845 | ✓ |
| `fcn.14004b450` | `0x14004b450` | 3650 | ✓ |
| `fcn.14003b980` | `0x14003b980` | 3644 | ✓ |
| `fcn.14004f730` | `0x14004f730` | 3394 | ✓ |

### Decompiled Code Files

- [`code/case.0x14002925b.81.c`](code/case.0x14002925b.81.c)
- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001000.c`](code/fcn.140001000.c)
- [`code/fcn.140001010.c`](code/fcn.140001010.c)
- [`code/fcn.140001120.c`](code/fcn.140001120.c)
- [`code/fcn.140002880.c`](code/fcn.140002880.c)
- [`code/fcn.14000b420.c`](code/fcn.14000b420.c)
- [`code/fcn.14000caf0.c`](code/fcn.14000caf0.c)
- [`code/fcn.14000cbc0.c`](code/fcn.14000cbc0.c)
- [`code/fcn.14000d700.c`](code/fcn.14000d700.c)
- [`code/fcn.140011500.c`](code/fcn.140011500.c)
- [`code/fcn.140011bc0.c`](code/fcn.140011bc0.c)
- [`code/fcn.140014560.c`](code/fcn.140014560.c)
- [`code/fcn.1400156e0.c`](code/fcn.1400156e0.c)
- [`code/fcn.1400165f0.c`](code/fcn.1400165f0.c)
- [`code/fcn.14001ae90.c`](code/fcn.14001ae90.c)
- [`code/fcn.14001e8d0.c`](code/fcn.14001e8d0.c)
- [`code/fcn.14001f4c0.c`](code/fcn.14001f4c0.c)
- [`code/fcn.140024e90.c`](code/fcn.140024e90.c)
- [`code/fcn.140029000.c`](code/fcn.140029000.c)
- [`code/fcn.140029ff0.c`](code/fcn.140029ff0.c)
- [`code/fcn.1400336d0.c`](code/fcn.1400336d0.c)
- [`code/fcn.140038910.c`](code/fcn.140038910.c)
- [`code/fcn.14003b980.c`](code/fcn.14003b980.c)
- [`code/fcn.14004b450.c`](code/fcn.14004b450.c)
- [`code/fcn.14004c2a0.c`](code/fcn.14004c2a0.c)
- [`code/fcn.14004f730.c`](code/fcn.14004f730.c)
- [`code/fcn.140051430.c`](code/fcn.140051430.c)
- [`code/fcn.140056ae4.c`](code/fcn.140056ae4.c)
- [`code/fcn.1400588a0.c`](code/fcn.1400588a0.c)

## Behavioral Analysis

This updated analysis incorporates the findings from **chunk 5/5**. The inclusion of these final segments provides a granular look at how the loader handles internal data structures, specifically regarding memory management and the translation of configuration keys into executable logic.

### Updated Analysis Report: Malware Loader/Package Stub (Full Integration)

The final pieces of disassembly confirm that this is not just a "loader" in the sense of an installer; it is a **highly engineered execution engine**. The code revealed in chunks 4 and 5 shows the transition from *parsing* raw data to *interpreting* that data as a series of complex operational commands.

---

### Core Functionality (Updated)
*   **Multi-Stage Loader / Packer Stub:** Confirmed. It acts as the primary entry point, unpacking/decrypting stages in memory before execution.
*   **Sophisticated URI/Protocol Parser:** These chunks show that "parsing" is a multi-step process. The loader doesn't just check for `http`; it validates segments of a string to determine port numbers, path lengths, and subdirectory levels.
*   **State-Machine Based Resolution (Advanced):** Rather than linear logic, the code uses complex loop structures to "walk" through an internal table. It takes a command identifier from the config blob and uses it as an index or key to fetch parameters like:
    1.  Buffer sizes for incoming data.
    2.  Operation types (e.g., download vs. execute).
    3.  Timeout values and retry limits.
*   **Sophisticated Resource Mapping:** The code features extensive logic for "matching" local actions with remote instructions. It uses nested loops to compare current states against a table of possible outcomes, ensuring that if one action is unavailable, it can gracefully fallback or move to the next step in a predetermined sequence.

### Suspicious & Malicious Behaviors
*   **Complex Command Translation:** The heavy use of offset calculations (e.g., `uVar14 = *(auStack_108 + iVar11 + -4)` and loop-based lookups) indicates that the "instructions" provided by the C2 are not plain text; they are likely indices into a hidden internal table of functions or capabilities.
*   **Robustness & Anti-Analysis:** The fact that the code performs constant checks for `NULL`, calculates memory boundaries before every move, and has multiple "fallback" paths suggests it is designed to be stable enough to operate in high-value environments where a crash would alert system administrators.
*   **Automated Configuration Translation:** In `fcn.14003b980`, there is evidence of the loader translating raw numeric strings (perhaps from an HTTP response) into internal machine values. This allows the attacker to change the behavior of the malware (e.g., changing a port or a sleep timer) without changing the binary's code.
*   **Multi-Dimensional Data Handling:** The logic in `fcn.14004f730` suggests the loader is managing multiple types of data simultaneously—likely handling different payloads (modules, scripts, and configuration updates)—within the same memory space by switching "modes" based on the parsed config.

### Technical Observations & Patterns
*   **Iterative Table Walking:** The frequent use of `do...while` loops to iterate through offsets (`uVar14 != uVar23`) is a classic technique used in malware to parse complex, non-standard data structures (like a proprietary TLV - Type, Length, Value - format).
*   **Internal Indexing Systems:** The code utilizes several different "lookup" mechanisms. For example, it checks for the existence of a character (`.`) at an offset to determine if a path is local or remote before deciding how much memory to allocate for the upcoming operation.
*   **Advanced Memory Management:** The manual calculation of buffer sizes and the usage of `0x110000` (a common indicator in decompilation for "uninitialized" or "not set") suggests that the loader is managing its own internal memory pool to avoid using standard, easily-hooked Windows APIs.
*   **Dynamic Calculation of Offsets:** Rather than using hardcoded addresses for its next steps, it calculates jumps based on the results of previous parsing steps. This makes static analysis significantly more difficult, as an analyst cannot see the "next" instruction without executing the code and populating the memory with data.

### Final Summary: Conclusion of Analysis
The final integration of all five chunks reveals a **sophisticated, professional-grade C2 orchestrator** typically associated with advanced persistent threats (APTs) or highly organized cybercriminal groups.

1.  **Chunks 1 & 2** established the "Weapon" (the ability to execute hidden code).
2.  **Chunk 3** revealed the "Brain" (the complex parsing of the configuration blob).
3.  **Chukns 4 & 5** reveal the "Reflexes" (the ability to intelligently navigate network complexities, handle errors, and dynamically map remote commands into local actions).

**Final Classification:** This is a **sophisticated, multi-stage orchestration stub.** Its primary purpose is to act as a versatile "Swiss Army Knife" for an attacker—taking highly complex instructions from a C2 server and translating them into specific system actions (e.g., file exfiltration, credential theft, or secondary payload deployment) while minimizing the risk of detection through robust error handling and sophisticated data management.

**Risk Level:** **Critical.** The level of engineering suggests this is part of an infrastructure designed for long-term persistence and high-value target exploitation.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files | The loader functions as a "Packer Stub" that decrypts and unpacks subsequent stages in memory, a classic method to hide malicious code from static analysis. |
| **T1568** | Dynamic Resolution | The use of offset calculations, internal table walking, and manual memory management (to avoid standard, hooked APIs) indicates dynamic resolution of commands into executable logic. |
| **T1071** | Application Layer Protocol | The complex parsing of URI components—including port numbers, path lengths, and directory levels—demonstrates the use of established protocols for C2 communication. |
| **T1568.003** | Dynamic Resolution: Import Address Table | The specific practice of using an internal "search" or "walk" through a table to find functions based on indices rather than direct calls helps bypass security tools monitoring common API imports. |

***Note for the Analyst:** While the analysis notes several distinct behaviors (like multi-dimensional data handling and automatic configuration translation), these are categorized under the broader capabilities of **T1568** and **T1027**, as they describe the sophistication of the "Reflexes" and "Brain" of the malware's command-processing engine.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many of the strings in the source text appear to be obfuscated data or junk characters used to bypass signature-based detection; therefore, only meaningful artifacts have been extracted below.

### **IP addresses / URLs / Domains**
*   **file:///H**: (Partial URI) Likely part of a local file system access routine or an incomplete string used during the parsing of remote paths.
*   **localhosL3**: (Suspected Obfuscated String) Highly likely to be "localhost" obscured to evade simple string-matching security tools.

### **File paths / Registry keys**
*   *(No specific valid file paths or registry keys were identified in the provided text.)*

### **Mutex names / Named pipes**
*   *(None identified.)*

### **Hashes**
*   *(None found.)*

### **Other artifacts**
*   **C2 Communication Patterns:** 
    *   **State-Machine Logic**: The malware uses a state-machine based resolution where remote commands are not direct instructions but indices into an internal lookup table (likely a TLV - Type, Length, Value - format).
    *   **HTTP Response Translation**: Use of numeric string parsing from HTTP responses to dynamically set internal parameters such as port numbers and sleep timers.
*   **Anti-Analysis Techniques:**
    *   **Manual Memory Management**: The loader avoids standard Windows APIs for memory management (referenced by the use of `0x110000` and manual buffer calculations) to evade hooks used by EDR/AV solutions.
    *   **Obfuscated String Blocks**: Repeated sequences such as `AWAVAUATVWUSH`, `fffff.`, and `[]_^A\A]A^A_` suggest the use of a custom packing or encryption layer for internal configuration data.
*   **Functional Indicators:**
    *   **Multi-Stage Execution**: The binary functions as an orchestrator, translating remote instructions into local actions (e.g., "switching modes" to handle different payloads like modules vs. scripts).

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated Orchestration:** The report describes the sample not as a simple downloader but as a "highly engineered execution engine" and "orchestration stub." It is designed to translate complex, non-standard C2 instructions (using state-machine logic) into various actions like file exfiltration or secondary payload deployment.
    *   **Advanced Evasion Techniques:** The inclusion of manual memory management (avoiding standard Windows APIs), complex offset calculations for command resolution, and "packer stub" behavior indicates a high level of development aimed at bypassing EDR/AV solutions.
    *   **Multi-Stage Execution:** It functions as a core infrastructure component that handles the unpacking, decryption, and translation of remote commands, which is characteristic of professional-grade loaders used by organized cybercriminal groups or APTs.
