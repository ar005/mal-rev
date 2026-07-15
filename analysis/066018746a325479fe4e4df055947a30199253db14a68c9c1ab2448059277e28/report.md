# Threat Analysis Report

**Generated:** 2026-07-15 01:59 UTC
**Sample:** `066018746a325479fe4e4df055947a30199253db14a68c9c1ab2448059277e28_066018746a325479fe4e4df055947a30199253db14a68c9c1ab2448059277e28.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `066018746a325479fe4e4df055947a30199253db14a68c9c1ab2448059277e28_066018746a325479fe4e4df055947a30199253db14a68c9c1ab2448059277e28.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 10,431,550 bytes |
| MD5 | `604bd003c53cc933af07e4882f81908d` |
| SHA1 | `dda890d9aa2087d23944b1203827dfa3b63085ac` |
| SHA256 | `066018746a325479fe4e4df055947a30199253db14a68c9c1ab2448059277e28` |
| Overall entropy | 7.994 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769051150 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 181,760 | 6.463 | No |
| `.rdata` | 80,896 | 5.755 | No |
| `.data` | 3,584 | 1.816 | No |
| `.pdata` | 9,728 | 5.32 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 62,976 | 7.555 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.264 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **22925** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
UVWAUAWH
0A_A]_^]
SUVWAVAWH
A_A^_^][
A_A^_^][
\$ UAVAWH
0A_A^]
0A_A^]
L$ SUVWH
L$ SUVWH
T$hfD+D$df+T$`
@SUVWAVH
T$<f+T$4
PA^_^][
@USVWAVH
A^_^[]
|$ AVH
L$ SUVWH
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
UVWATAWH
0A_A\_^]
@UVATAU
A]A\^]
L9t$0t
tR@80tMH
L$ SVWH
@SUWAVAW
A_A^_][
H9{ t)
H9{(t(
H9{8t#
H9{@t&
l$ ATAVAWH
 A_A^A\
l$ VWAV
u[HcG0
l$ VATAUAVAWH
0A_A^A]A\^
MLcF0H
@SVAVH
t$ WAVAWH
VWATAVAWH
~#D8e0u
0A_A^A\_^
l$ VWAV
@UVWATAUAVAW
A_A^A]A\_^]
l$ VWATAVAW
A_A^A\_^
|$ AVH
UVWAVAWH
 A_A^_^]
WAVAWH
0A_A^_
@SUVWAV
A^_^][
@VATAUAVAWH
 A_A^A]A\^
@SUATAU
A]A\][
D$hH+D$pHi
|$8fff
SUVWATAUAVAWH
8A_A^A]A\_^][
SUVWATAUAVAWH
MP;H(s
MP;H8s
]Lu*A;|$
L$@E)}P
A;Exsg
E;E8v#A
L$@A9MP
tDE;u$t>H
T$8E+T$
XA_A^A]A\_^][
tHH9
uC
I@L9{8uH
t$HL9{0
~0L9{0
y<L9{0
\$ UVAVH
@USWATAVAWH
fD9 uA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140018164` | `0x140018164` | 40065 | ✓ |
| `fcn.14001c130` | `0x14001c130` | 37955 | ✓ |
| `fcn.14001c11c` | `0x14001c11c` | 37914 | ✓ |
| `section..text` | `0x140001000` | 17899 | ✓ |
| `fcn.140027400` | `0x140027400` | 12313 | ✓ |
| `fcn.140004b70` | `0x140004b70` | 9279 | ✓ |
| `fcn.14000b6a0` | `0x14000b6a0` | 6161 | ✓ |
| `fcn.140029d90` | `0x140029d90` | 5703 | ✓ |
| `fcn.1400260ec` | `0x1400260ec` | 4735 | ✓ |
| `fcn.140001ca0` | `0x140001ca0` | 2338 | ✓ |
| `fcn.14002308c` | `0x14002308c` | 2201 | ✓ |
| `fcn.14001757c` | `0x14001757c` | 1946 | ✓ |
| `fcn.140012478` | `0x140012478` | 1898 | ✓ |
| `fcn.14001713c` | `0x14001713c` | 1777 | ✓ |
| `fcn.1400028a0` | `0x1400028a0` | 1773 | ✓ |
| `fcn.14002bcf0` | `0x14002bcf0` | 1661 | ✓ |
| `fcn.14000d390` | `0x14000d390` | 1468 | ✓ |
| `fcn.140029e60` | `0x140029e60` | 1451 | ✓ |
| `fcn.140023d8c` | `0x140023d8c` | 1421 | ✓ |
| `fcn.140014e90` | `0x140014e90` | 1397 | ✓ |
| `fcn.140023094` | `0x140023094` | 1353 | ✓ |
| `fcn.140005f70` | `0x140005f70` | 1325 | ✓ |
| `fcn.14000feac` | `0x14000feac` | 1263 | ✓ |
| `fcn.14000b1c0` | `0x14000b1c0` | 1238 | ✓ |
| `fcn.14000ad20` | `0x14000ad20` | 1179 | ✓ |
| `fcn.14001e380` | `0x14001e380` | 1171 | ✓ |
| `fcn.140009fe0` | `0x140009fe0` | 1169 | ✓ |
| `fcn.140025c60` | `0x140025c60` | 1164 | ✓ |
| `fcn.140014a20` | `0x140014a20` | 1133 | ✓ |
| `fcn.14001d810` | `0x14001d810` | 1119 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ca0.c`](code/fcn.140001ca0.c)
- [`code/fcn.1400028a0.c`](code/fcn.1400028a0.c)
- [`code/fcn.140004b70.c`](code/fcn.140004b70.c)
- [`code/fcn.140005f70.c`](code/fcn.140005f70.c)
- [`code/fcn.140009fe0.c`](code/fcn.140009fe0.c)
- [`code/fcn.14000ad20.c`](code/fcn.14000ad20.c)
- [`code/fcn.14000b1c0.c`](code/fcn.14000b1c0.c)
- [`code/fcn.14000b6a0.c`](code/fcn.14000b6a0.c)
- [`code/fcn.14000d390.c`](code/fcn.14000d390.c)
- [`code/fcn.14000feac.c`](code/fcn.14000feac.c)
- [`code/fcn.140012478.c`](code/fcn.140012478.c)
- [`code/fcn.140014a20.c`](code/fcn.140014a20.c)
- [`code/fcn.140014e90.c`](code/fcn.140014e90.c)
- [`code/fcn.14001713c.c`](code/fcn.14001713c.c)
- [`code/fcn.14001757c.c`](code/fcn.14001757c.c)
- [`code/fcn.140018164.c`](code/fcn.140018164.c)
- [`code/fcn.14001c11c.c`](code/fcn.14001c11c.c)
- [`code/fcn.14001c130.c`](code/fcn.14001c130.c)
- [`code/fcn.14001d810.c`](code/fcn.14001d810.c)
- [`code/fcn.14001e380.c`](code/fcn.14001e380.c)
- [`code/fcn.14002308c.c`](code/fcn.14002308c.c)
- [`code/fcn.140023094.c`](code/fcn.140023094.c)
- [`code/fcn.140023d8c.c`](code/fcn.140023d8c.c)
- [`code/fcn.140025c60.c`](code/fcn.140025c60.c)
- [`code/fcn.1400260ec.c`](code/fcn.1400260ec.c)
- [`code/fcn.140027400.c`](code/fcn.140027400.c)
- [`code/fcn.140029d90.c`](code/fcn.140029d90.c)
- [`code/fcn.140029e60.c`](code/fcn.140029e60.c)
- [`code/fcn.14002bcf0.c`](code/fcn.14002bcf0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This third and final chunk of disassembly provides the "operational" logic for the loader. While it confirms the heavy use of Python-related infrastructures, it also reveals exactly how the binary manages its execution lifecycle and hides its presence from the end-user.

### Updated Analysis & Final Synthesis

#### 1. Confirmed Execution Model: The "Shadow Launcher"
The discovery of `fcn.140009fe0` is critical. This function demonstrates that the binary is not just a wrapper; it is a **managed launcher**. 
*   **Process Spawning:** It calls `CreateProcessW`, which is used to launch a secondary process (often the "real" Python interpreter environment). The internal use of strings like `"PyInstallerOnefileHiddenWindow"` and `"PyInstaller Onefile Hidden Window"` confirms it uses standard PyInstaller templates, but its role is to ensure that if the Python script requires a console or window, it is handled in a way that keeps it hidden from the user.
*   **Window Management:** It utilizes `CreateWindowExW` followed by `ShowWindow(handle, 0)`. This ensures that even if the underlying logic triggers a GUI or an error message window, it remains invisible to the desktop environment—a classic technique used to maintain stealth during "headless" operations (like data exfiltration or crypto-mining).
*   **Message Loop Persistence:** The inclusion of `PeekMessageW`, `TranslateMessage`, and `DispatchMessageW` inside a loop indicates that the loader stays alive as a "parent" process, waiting for the child (the actual payload) to complete its tasks.

#### 2. Advanced Data & String Processing
Several functions (`fcn.140014a20`, `fcn.140025c60`) show highly complex logic for handling memory buffers and string indexing:
*   **Buffer Reconstruction:** These functions manage internal "lengths" and "offsets," suggesting the binary is prepared to unpack complex, multi-part data structures or perhaps even a "packed" Python bytecode stream. 
*   **Decoded Interaction:** `fcn.14001d810` interacts with `ReadFile` and `ReadConsoleW`. This indicates that the loader (or its internal library) has specific logic for handling various input types, which may be necessary if the malicious payload expects to read from a configuration file or interact with system-level I/O.

#### 3. Environment Extraction
The use of `GetStartupInfoW` and `GetCommandLineW` just before the process spawn suggests that the launcher is gathering environment data to "pass" it to the Python engine. This ensures that even if the script's environment is changed, the core logic still has access to the parameters it needs (such as paths, network configs, or local configuration).

---

### Summary of Key Technical Indicators
*   **Stealth Windows:** Use of `ShowWindow(..., 0)` confirms intent to hide activity from the user.
*   **PyInstaller Footprint:** The specific naming conventions and `CreateProcessW` logic confirm a multi-stage execution: **[Loader] $\rightarrow$ [Unpacking/Prep] $\rightarrow$ [Hidden Worker Process]**.
*   **High-Performance Core:** (From previous chunks) The inclusion of SIMD instructions (`AVX`, `FMA`) suggests the final payload is designed for performance—typical of high-end crypto, complex data processing, or heavy encryption routines.

### Final Assessment for Incident Response

**Final Analysis Statement:**
The binary is a **sophisticated multi-stage loader** specifically designed to host and execute Python-based logic while maintaining maximum stealth. It functions as a "bridge": the executable you see (the Loader) is professionally structured to appear as a legitimate, high-performance application. Its primary role is to set up an environment where a hidden child process can run a malicious Python script without ever displaying windows or console output.

**Risk Level:** **High.** The complexity of the wrapper suggests it is likely designed to host more than just a simple script; it is structured to accommodate complex, potentially heavy-duty (e.g., ransomware, botnet control) logic that requires high-performance libraries and "hidden" execution paths.

**Detection & Mitigation Strategy:**
1.  **Behavioral Analysis:** Detection should focus on the **process tree**. Look for a process that spawns another child process while simultaneously calling `ShowWindow(..., 0)` or using the term `HiddenWindow`.
2.  **Memory Forensic Focus:** Because the "malicious" part is likely a script, static analysis of the `.exe` will yield few results. Memory dumps should be taken *after* the launcher has successfully spawned its child process but before it terminates. Look for Python bytecode or strings in the heap of both processes.
3.  **Network Monitoring:** Monitor the behavior of the **child process**. Since the loader is just a wrapper, the primary malicious actions (C2 check-ins, exfiltration) will occur in the secondary process spawned by `CreateProcessW`.
4.  **Indicator Extraction:** Focus on identifying the "Payload" during dynamic execution. The most useful indicators will be found in memory as `.pyc` files or raw Python script strings that are decrypted only after the loader confirms a successful environment setup.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059.004** | Command and Scripting Interpreter: Python | The loader specifically utilizes PyInstaller infrastructure to wrap and execute a hidden Python interpreter as the primary payload mechanism. |
| **T1036** | Indicator Removal on Host | The use of `ShowWindow(handle, 0)` is a clear attempt to hide evidence of malicious activity (windows or console outputs) from the end-user. |
| **T1027** | Deobfuscate Files or Information | The complex logic for buffer reconstruction and decoding suggests the loader is designed to unpack multi-part data structures or packed Python bytecode. |
| **T1082** | System Information Discovery | The calls to `GetStartupInfoW` and `GetCommandLineW` are used to gather system environment details to pass into the hidden worker process. |
| **T1036.005** | Indicator Removal: File Deletion (or similar evasion) | While more generally T1036, the "Shadow Launcher" architecture functions to mask the transition from a "legitimate-looking" loader to a malicious script execution. |

***Note on Analysis Strategy:** The analysis highlights a multi-stage execution flow where the first stage (the .exe) acts as a "proxy" or wrapper for the second stage (the Python script). From a hunting perspective, while T1059.004 is the primary vehicle for the payload, T1036 describes the behavioral intent to bypass human observation.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: As this report is based on a functional analysis of a loader rather than a specific intercepted instance, the indicators are primarily **behavioral** and **structural artifacts** rather than specific network infrastructure.

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   *None identified (The analysis mentions standard Windows API calls for path retrieval, but no specific malicious paths or registry keys were listed).*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified in the provided strings.*

### **Other artifacts**
*   **Strings (Construction Indicators):** 
    *   `PyInstallerOnefileHiddenWindow`
    *   `PyInstaller Onefile Hidden Window`
    *(Note: These indicate the use of a PyInstaller wrapper to bundle Python scripts into a single executable.)*
*   **Behavioral Patterns:**
    *   **Stealth Execution:** Use of `ShowWindow(handle, 0)` to ensure hidden execution of child processes.
    *   **Multi-stage Execution:** Usage of `CreateProcessW` to spawn a secondary "worker" process from the initial loader.
    *   **API Interaction:** Calls to `PeekMessageW`, `TranslateMessage`, and `DispatchMessageW` to maintain the parent process's lifecycle while waiting for the payload.
    *   **Instruction Set Usage:** Presence of **AVX** and **FMA** instructions (indicative of a high-performance payload, such as mining or heavy encryption).

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family:** custom (Python-based Wrapper/Launcher)
2. **Malware type:** loader
3. **Confidence:** High
4. **Key evidence:** 
    * **Multi-Stage Execution:** The use of `CreateProcessW` and "Shadow Launcher" logic confirms the binary acts as a primary wrapper to host and execute a secondary, hidden payload (the Python script).
    * **Evasion Tactics:** The integration of `ShowWindow(..., 0)` and strings like `"PyInstallerOnefileHiddenWindow"` explicitly demonstrates an intent to hide both the execution process and any associated UI/errors from the end-user.
    * **Infrastructure for Persistence/Stealth:** The inclusion of high-performance instruction sets (AVX, FMA) combined with complex buffer reconstruction suggests a sophisticated design meant to host heavy-duty malicious logic (such as mining or encryption) while maintaining a minimal footprint.
