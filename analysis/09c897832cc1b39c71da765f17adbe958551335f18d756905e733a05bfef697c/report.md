# Threat Analysis Report

**Generated:** 2026-07-23 13:38 UTC
**Sample:** `09c897832cc1b39c71da765f17adbe958551335f18d756905e733a05bfef697c_09c897832cc1b39c71da765f17adbe958551335f18d756905e733a05bfef697c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09c897832cc1b39c71da765f17adbe958551335f18d756905e733a05bfef697c_09c897832cc1b39c71da765f17adbe958551335f18d756905e733a05bfef697c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 33,405,576 bytes |
| MD5 | `c7a6f220f2ff7d6718a5b2f0e85f13dd` |
| SHA1 | `f253dff01948c778b45aedc2e5654bfc432f8627` |
| SHA256 | `09c897832cc1b39c71da765f17adbe958551335f18d756905e733a05bfef697c` |
| Overall entropy | 7.999 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778095938 |
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

Total strings found: **72851** (showing first 100)

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

This final piece of disassembly provides significant insight into how the loader handles internal memory management, data decoding, and environment interaction. These functions confirm that while this is a PyInstaller-based bootloader, it includes robust mechanisms to handle complex data structures and "invisible" execution environments.

### **Final Integrated Analysis**

The analysis confirms the binary is a sophisticated, high-fidelity **PyInstaller bootloader**. It is designed to host complex Python applications, potentially including graphical interfaces (Tcl/Tk) and heavy memory manipulation. The core logic is structured to create a complete, isolated environment where the "real" payload can reside in an encoded state until execution.

---

### **Final Core Functionality & Purpose**

*   **Full-Scale Python C-API Integration:** (Confirmed) The loader maps the extensive Python C-API (memory management, string handling, and module loading), allowing it to host any standard or complex Python library.
*   **Tcl/Tk Environment Support:** (Confirmed) Evidence of `Tcl_Init` and related symbols indicates support for GUIs and complex scripting interactions.
*   **Data Decoding & Decompression (`fcn.14000ad20`):** This is a critical finding. The presence of bitwise-heavy decoding routines suggests that the loader is capable of "unpacking" or "decoding" internal data on the fly. In a malware context, this means a malicious payload can be stored in a heavily obfuscated/compressed format inside the `.exe` and only decoded into memory at the moment it is needed by the Python interpreter.
*   **Sophisticated Memory Management (`fcn.14000b1c0`, `fcn.140023094`):** These functions manage internal data structures, potentially for "interning" strings or managing a custom memory pool. The error messages found in the code (e.g., `"invalid literal/length code"` and `"invalid distance code"`) are characteristic of an internal scripting engine’s logic to handle complex object types.
*   **Hidden Window & Console Management (`fcn.140009fe0`):** This is a key behavior for stealth. The loader creates a window titled **"PyInstallerOnefileHiddenWindow"** and utilizes `ShowWindow(..., 0)`. It also implements complex logic to manage console input/output (via `ReadConsoleW`) in the background. This allows the "real" payload to run without a visible terminal or window, which is common in trojans and miners to remain unnoticed by the user.
*   **Environment Manipulation:** The use of `SetEnvironmentVariableW` suggests that the loader can dynamically configure the environment for different stages of execution, ensuring that all dependencies (including those of the "hidden" payload) are correctly mapped.

---

### **Technical Observations (Final Highlights)**

*   **Advanced Payload Wrapping:** By using a standard PyInstaller framework, the author provides an excellent layer of **"security through obscurity."** To an automated scanner, it looks like a valid Python bundle; to a human analyst, it is clearly capable of hosting complex-logic.
*   **Multi-Stage Reconstruction:** The code shows a progression from:
    1.  Allocating and decoding raw data (the "loader" phase).
    2.  Constructing internal objects (like strings or custom types) in memory.
    3.  Setting up a "hidden" environment to prevent the user from seeing typical console outputs.
    4.  Executing the final Python payload.
*   **Robustness:** The inclusion of specialized logic for handling "dist-far" errors and length checks suggests that this loader is intended for high-reliability applications, making it a perfect host for sophisticated malware requiring heavy dependencies (like `requests`, `scapy`, or encryption libraries).

---

### **Final Risk Profile**

*   **High Capability as a Wrapper:** This is not just a simple script runner. It is a "full feature" environment bootloader. It supports multi-threading, hidden windows, and complex data structures.
*   **Obfuscation Strategy:** The payload's primary logic is **not** in this executable; it resides within the compressed/encoded blocks that are processed by functions like `fcn.14000ad20`. By the time the malicious behavior begins, the code will be "unpacked" and running as a legitimate-looking Python process.
*   **Evasion Potential:** The "Hidden Window" logic specifically targets the evasion of manual user detection, allowing the malware to persist in the background while performing network communication or data exfiltration.

---

### **Final Conclusion & Recommendation**

The analysis confirms that this is a high-end Python environment loader. It provides all the necessary infrastructure (Tcl/Tk, robust C-API mapping, and background operation capabilities) required for complex malicious activities.

**Recommended Actions:**
1.  **Dynamic Analysis / Memory Dump:** Since much of the complexity lies in how it handles internal memory objects and "hidden" windows, **run this in a sandbox with memory monitoring.** Perform a memory dump once the Python environment is fully initialized but before the payload executes its primary routine.
2.  **Identify Embedded Payloads:** Extract any large high-entropy sections or `.pyc` files from the data segments. These are the likely locations of the actual malicious script.
3.  **Behavioral Monitoring (Host/Network):** Monitor for:
    *   Creation of hidden windows.
    *   Files created in `\AppData\` or `\Temp\` (common for unpacked Python components).
    *   Outbound connections to non-standard ports, which may indicate C2 communication from the "inner" script.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1631** | Data Encoding | The use of bitwise-heavy decoding routines (`fcn.14000ad20`) indicates that the payload is encoded/obfuscated to hide its true nature during transit or storage. |
| **T1027** | Obfuscated Files or Information | The loader utilizes a PyInstaller wrapper and complex internal memory management to shield the primary malicious logic from static analysis tools. |
| **T1036** | Masquerading | The implementation of `ShowWindow(..., 0)` and "Hidden Window" logic is intended to hide terminal interactions and avoid detection by the end-user. |
| **T1059** | Command and Scripting Interpreter | The loader provides a full Python C-API environment, allowing it to execute complex scripts (and any associated libraries) as its primary method of execution. |
| **T1105** | Ingress Tool Transfer (Optional/Related Context) | While not directly in the text, the "Advanced Payload Wrapping" highlights how standard tools are repurposed to deliver malicious functionality under the guise of a legitimate utility. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Because the provided text describes a **bootloader framework** (PyInstaller) rather than a specific, hardcoded malware campaign, many traditional IOCs (like specific IP addresses or unique file hashes) were not present in the raw strings. The available indicators are primarily behavioral and environmental.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. *(Note: While \AppData\ and \Temp\ were mentioned in recommendations, these are standard system paths and were excluded as per instructions.)*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Window Title:** `PyInstallerOnefileHiddenWindow` (Identifies the use of a PyInstaller bootloader to hide the console/GUI).
*   **Internal Function Offsets (Behavioral Indicators):** 
    *   `fcn.14000ad20` (Data decoding/decompression routine)
    *   `fcn.14000b1c0` (Memory management/string interning)
    *   `fcn.140023094` (Internal data structures)
    *   `fcn.140009fe0` (Window and console management logic)
*   **Library/Environment Indicators:** 
    *   Usage of **Tcl/Tk** libraries for potential GUI interaction or complex scripting.
    *   Use of `SetEnvironmentVariableW` to manage environment states during multi-stage execution.
*   **Decoding Patterns:** The presence of high-entropy, repetitive string segments (e.g., `SUVWAVAWH`, `A_A^[]`) suggests a heavy use of **layered obfuscation** or packed data within the `.exe`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High
4. **Key evidence**:
    * **PyInstaller Bootloader Framework:** The sample utilizes a sophisticated PyInstaller wrapper to host a Python environment, enabling it to execute complex scripts and libraries (like `requests` or `scapy`) while providing "security through obscurity."
    * **Payload Decapsulation & Obfuscation:** The analysis identified specific decoding routines (e.g., `fcn.14000ad20`) designed to unpack and decompress a hidden payload into memory, ensuring the primary malicious logic remains hidden from static analysis.
    * **Anti-Analysis/Stealth Features:** The implementation of "Hidden Window" logic (`PyInstallerOnefileHiddenWindow` combined with `ShowWindow(..., 0)`) specifically aims to hide terminal outputs and console windows to ensure the payload runs undetected by the user in the background.
