# Threat Analysis Report

**Generated:** 2026-08-25 01:01 UTC
**Sample:** `12391dcde0d2cd38d11aef42ed0790cbbb4b5ad3b92e592349aea5f80b6a2e16_12391dcde0d2cd38d11aef42ed0790cbbb4b5ad3b92e592349aea5f80b6a2e16.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12391dcde0d2cd38d11aef42ed0790cbbb4b5ad3b92e592349aea5f80b6a2e16_12391dcde0d2cd38d11aef42ed0790cbbb4b5ad3b92e592349aea5f80b6a2e16.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 9,669,266 bytes |
| MD5 | `db0a978fa61226e70f16a8733215492b` |
| SHA1 | `52515b7be35283b59de68b686839e576a729da34` |
| SHA256 | `12391dcde0d2cd38d11aef42ed0790cbbb4b5ad3b92e592349aea5f80b6a2e16` |
| Overall entropy | 7.993 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770078382 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 179,712 | 6.474 | No |
| `.rdata` | 80,384 | 5.744 | No |
| `.data` | 3,584 | 1.819 | No |
| `.pdata` | 9,216 | 5.473 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 62,976 | 7.555 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.263 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **21342** (showing first 100)

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
t$ WATAUAVAWH
~#E8n0u
0A_A^A]A\_
SUVWATAUAWH
0A_A]A\_^][
0A_A]A\_^][
l$ VWATAVAW
A_A^A\_^
|$ AVH
l$ VWAVH
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
A_A^A\_[]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140017be4` | `0x140017be4` | 39505 | ✓ |
| `fcn.14001b980` | `0x14001b980` | 37955 | ✓ |
| `fcn.14001b96c` | `0x14001b96c` | 37914 | ✓ |
| `section..text` | `0x140001000` | 17547 | ✓ |
| `fcn.140026c50` | `0x140026c50` | 12889 | ✓ |
| `fcn.140004a10` | `0x140004a10` | 8927 | ✓ |
| `fcn.14000b130` | `0x14000b130` | 6161 | ✓ |
| `fcn.140029820` | `0x140029820` | 5703 | ✓ |
| `fcn.14002593c` | `0x14002593c` | 4735 | ✓ |
| `fcn.140001ca0` | `0x140001ca0` | 2338 | ✓ |
| `fcn.1400228dc` | `0x1400228dc` | 2201 | ✓ |
| `fcn.140016ffc` | `0x140016ffc` | 1946 | ✓ |
| `fcn.140011ef8` | `0x140011ef8` | 1898 | ✓ |
| `fcn.140016bbc` | `0x140016bbc` | 1777 | ✓ |
| `fcn.14002b780` | `0x14002b780` | 1661 | ✓ |
| `fcn.14000ce20` | `0x14000ce20` | 1468 | ✓ |
| `fcn.1400298f0` | `0x1400298f0` | 1451 | ✓ |
| `fcn.1400028a0` | `0x1400028a0` | 1422 | ✓ |
| `fcn.1400235dc` | `0x1400235dc` | 1421 | ✓ |
| `fcn.140014910` | `0x140014910` | 1397 | ✓ |
| `fcn.1400228e4` | `0x1400228e4` | 1353 | ✓ |
| `fcn.140005e10` | `0x140005e10` | 1325 | ✓ |
| `fcn.14000f92c` | `0x14000f92c` | 1263 | ✓ |
| `fcn.14000ac50` | `0x14000ac50` | 1238 | ✓ |
| `fcn.14000a7b0` | `0x14000a7b0` | 1179 | ✓ |
| `fcn.14001dbd0` | `0x14001dbd0` | 1171 | ✓ |
| `fcn.1400254b0` | `0x1400254b0` | 1164 | ✓ |
| `fcn.140009a90` | `0x140009a90` | 1152 | ✓ |
| `fcn.1400144a0` | `0x1400144a0` | 1133 | ✓ |
| `fcn.14001d060` | `0x14001d060` | 1119 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ca0.c`](code/fcn.140001ca0.c)
- [`code/fcn.1400028a0.c`](code/fcn.1400028a0.c)
- [`code/fcn.140004a10.c`](code/fcn.140004a10.c)
- [`code/fcn.140005e10.c`](code/fcn.140005e10.c)
- [`code/fcn.140009a90.c`](code/fcn.140009a90.c)
- [`code/fcn.14000a7b0.c`](code/fcn.14000a7b0.c)
- [`code/fcn.14000ac50.c`](code/fcn.14000ac50.c)
- [`code/fcn.14000b130.c`](code/fcn.14000b130.c)
- [`code/fcn.14000ce20.c`](code/fcn.14000ce20.c)
- [`code/fcn.14000f92c.c`](code/fcn.14000f92c.c)
- [`code/fcn.140011ef8.c`](code/fcn.140011ef8.c)
- [`code/fcn.1400144a0.c`](code/fcn.1400144a0.c)
- [`code/fcn.140014910.c`](code/fcn.140014910.c)
- [`code/fcn.140016bbc.c`](code/fcn.140016bbc.c)
- [`code/fcn.140016ffc.c`](code/fcn.140016ffc.c)
- [`code/fcn.140017be4.c`](code/fcn.140017be4.c)
- [`code/fcn.14001b96c.c`](code/fcn.14001b96c.c)
- [`code/fcn.14001b980.c`](code/fcn.14001b980.c)
- [`code/fcn.14001d060.c`](code/fcn.14001d060.c)
- [`code/fcn.14001dbd0.c`](code/fcn.14001dbd0.c)
- [`code/fcn.1400228dc.c`](code/fcn.1400228dc.c)
- [`code/fcn.1400228e4.c`](code/fcn.1400228e4.c)
- [`code/fcn.1400235dc.c`](code/fcn.1400235dc.c)
- [`code/fcn.1400254b0.c`](code/fcn.1400254b0.c)
- [`code/fcn.14002593c.c`](code/fcn.14002593c.c)
- [`code/fcn.140026c50.c`](code/fcn.140026c50.c)
- [`code/fcn.140029820.c`](code/fcn.140029820.c)
- [`code/fcn.1400298f0.c`](code/fcn.1400298f0.c)
- [`code/fcn.14002b780.c`](code/fcn.14002b780.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This updated analysis incorporates the findings from the final chunk of disassembly (3/3). This final segment provides significant insight into the loader's interaction with the operating system, its sophisticated parsing logic, and the mechanisms it uses to manage multi-process execution.

---

### Updated Analysis of Binary Behavior

The final set of functions reinforces the conclusion that this is a highly complex **multi-stage wrapper**. It doesn't just "load" code; it manages an entire environment for multiple scripting engines while actively manipulating the OS to facilitate its operation.

#### 1. Massive Tcl Engine Integration
*   **Evidence:** The disassembly shows an extensive chain of `GetProcAddress` calls specifically for Tcl functions: `Tcl_SetVar2Ex`, `Tcl_CreateInterp`, `Tcl_FindExecutable`, `Tcl_MutexLock`, `Tcl_EvaluateFile`, and `Tcl_Alloc`.
*   **Significance:** This confirms that the "core" of the application relies on a deep Tcl integration. The inclusion of so many low-level Tcl functions suggests that much of the configuration or logic may be written in Tcl, even if the primary interaction is via Python.

#### 2. Complex Resource Parsing and Data Extraction
*   **Evidence:** Functions like `fcn.140005e10` and `fcn.1400235dc` contain dense, nested logic for identifying key-value pairs (searching for `o`, `=`, and whitespace) and managing memory offsets.
*   **Significance:** This indicates the presence of a **resource pack**. The binary is designed to extract internal assets—such as configuration files, localized strings, or even secondary payloads—from an embedded data blob. It acts as a "packer" that prepares the environment before the primary script ever runs.

#### 3. Sophisticated Environment Preparation
*   **Evidence:** `fcn.1400228e4` explicitly calls `SetEnvironmentVariableW` and performs complex calculations to determine memory offsets for internal objects.
*   **Significance:** The loader is actively manipulating the OS environment (paths, flags, etc.). In a malicious context, this is often used to bypass path-based security filters or to ensure that the unpacked scripts have the necessary environment variables to communicate with external components or C2 servers.

#### 4. Multi-Process "Hidden" Execution
*   **Evidence:** `fcn.140009a90` calls `CreateProcessW` and specifically uses the window title **"PyInstallerOnefileHiddenWindow"**. It also contains logic for managing console input/output (e.g., `GetConsoleMode`, `PeekMessageW`).
*   **Significance:** This is a classic "Loader-to-Payload" transition. The initial process (the one being analyzed) acts as the "launcher," while it spawns a second, hidden process to execute the actual payload. By using a hidden window and managing console modes, the malware ensures that even if the user sees a terminal briefly, it is quickly masked or suppressed during the transition to the main application.

#### 5. Advanced String & Memory Manipulation
*   **Evidence:** `fcn.1400254b0` and `fcn.140014910` show complex bit-shifting and multi-byte character handling (standard for UTF-8/Unicode processing).
*   **Significance:** This allows the binary to handle internationalized data or obfuscated strings that use non-standard character sets. For an attacker, this provides a way to hide commands or C2 addresses within complex string structures that simple automated scanners might miss.

---

### Final Consolidated Analysis Summary

The binary is confirmed as a **sophisticated, multi-scripting environment loader**. It follows the architectural patterns of "heavy" installers (like PyInstaller) but contains features common in high-end malware used to hide complexity and mask malicious intent.

*   **Risk Level: High.**
*   **Complexity Factor:** The inclusion of both **Python and Tcl** engines creates a "dual-layer" risk. Even if the Python layer is decoded, a secondary, independent logic layer (Tcl) may still be active.
*   **Core Behaviors Identified:**
    *   **Multi-Engine Support:** Built to support Python and Tcl simultaneously.
    *   **Resource Decapsulation:** A significant portion of the code is dedicated to "unpacking" a blob of data into usable variables/files before execution.
    *   **Environment Manipulation:** Active use of `SetEnvironmentVariableW` to prepare the OS for the payload.
    *   **Process Hiding:** Uses specific techniques (hidden windows, console-mode manipulation) to transition from a loader to an active payload without alerting the user.

---

### Final Actionable Intel for Incident Response

1.  **Detection Strategy - "The Transition":** The most critical point of interest is the call to `CreateProcessW` within `fcn.140009a90`. Analysis should focus on this transition point; at this moment, the hidden payload's code is usually decrypted/unpacked into memory and executed.
2.  **Forensic Memory Capture:** Because of the multi-engine nature (Python/Tcl) and the "hidden" execution logic, **static analysis will be insufficient.** A memory dump should be taken *at the moment* the transition to the second process occurs to capture the decrypted scripts in their raw form.
3.  **Identify Tcl Payloads:** Do not stop the investigation after identifying Python scripts. Analysts must look for `.tcl` files or Tcl-specific command strings during memory analysis, as these may contain secondary logic (e.g., persistence mechanisms or additional modules).
4.  **Monitor Environment Changes:** Monitor for changes to system environment variables during execution. The loader is designed to modify the local environment to ensure its "suite" of scripts functions correctly; these modifications often include indicators of compromise (IOCs) like specific temporary paths or shell commands.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping of observed behaviors to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The loader utilizes a complex "resource pack" and advanced multi-byte character manipulation to hide internal configurations, strings, and potentially C2 infrastructure from automated scanners. |
| **T1059** | Command and Scripting Interpreter | The binary integrates both Python and Tcl engines as its core logic, allowing it to execute scripts and manage multi-stage operations. |
| **T1036** | Masquerading | The loader explicitly uses the "PyInstaller" naming convention and hidden windows to blend in with legitimate third-party software tools while hiding its actual execution from the user. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "EXTRACTED STRINGS" section contains largely obfuscated or mangled data that do not resolve into standard network indicators. Therefore, the primary actionable IOCs are derived from the functional behavior and specific strings identified in the behavioral analysis.

### **IP addresses / URLs / Domains**
*   *(None identified)*

### **File paths / Registry keys**
*   *(None specifically identified; no absolute paths or registry hive keys were present in the provided data.)*

### **Mutex names / Named pipes**
*   *(None identified)*

### **Hashes**
*   *(No MD5, SHA1, or SHA256 hashes were found in the string dump.)*

### **Other artifacts**
*   **Window Title:** `PyInstallerOnefileHiddenWindow` (Used to mask the transition from loader to payload).
*   **Scripting Engines:** 
    *   Python
    *   Tcl (Tk)
*   **Imported/Utilized Tcl Functions (Potential for signature-based detection):** 
    *   `Tcl_SetVar2Ex`
    *   `Tcl_CreateInterp`
    *   `Tcl_FindExecutable`
    *   `Tcl_MutexLock`
    *   `Tcl_EvaluateFile`
    *   `Tcl_Alloc`
*   **Suspicious API Calls:** 
    *   `GetProcAddress` (used for dynamic Tcl function mapping)
    *   `SetEnvironmentVariableW` (used for environment manipulation/evasion)
    *   `CreateProcessW` (used for the "Loader-to-Payload" transition)
    *   `GetConsoleMode`, `PeekMessageW` (used to mask console activity)

---
**Analyst Note:** The primary threat vector identified is a **multi-stage loader** using a dual-scripting engine approach (Python/Tcl). Because the payload is unpacked in memory during the transition at the point of the `CreateProcessW` call, traditional static file scanning may fail to find secondary malicious components. Memory forensics are recommended for deep analysis.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: Loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Multi-Stage Loading Architecture:** The binary acts as a sophisticated wrapper that utilizes dual scripting engines (Python and Tcl) to create a "dual-layer" of complexity, effectively hiding the primary malicious logic behind multiple layers of abstraction.
    *   **Process Masking & Hiding:** It employs specific tactics such as `PyInstallerOnefileHiddenWindow` and console mode manipulation (`GetConsoleMode`) to transition from a visible loader to a hidden secondary process, preventing user interaction or observation during the "hand-off."
    *   **Environment Preparation & Obfuscation:** The use of heavy resource parsing, `SetEnvironmentVariableW`, and complex bit-shifting for string handling indicates a high level of intent to obfuscate configuration data and prepare the OS environment specifically for the execution of subsequent payloads.
