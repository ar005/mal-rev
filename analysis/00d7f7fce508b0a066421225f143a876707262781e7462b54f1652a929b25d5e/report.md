# Threat Analysis Report

**Generated:** 2026-06-25 13:17 UTC
**Sample:** `00d7f7fce508b0a066421225f143a876707262781e7462b54f1652a929b25d5e_00d7f7fce508b0a066421225f143a876707262781e7462b54f1652a929b25d5e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00d7f7fce508b0a066421225f143a876707262781e7462b54f1652a929b25d5e_00d7f7fce508b0a066421225f143a876707262781e7462b54f1652a929b25d5e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 7 sections |
| Size | 15,179,834 bytes |
| MD5 | `6ea297cdbfb445cfc3ab950a0d02c119` |
| SHA1 | `33ca19ce26afa43924428d4b7c2d2b012d16ec29` |
| SHA256 | `00d7f7fce508b0a066421225f143a876707262781e7462b54f1652a929b25d5e` |
| Overall entropy | 7.996 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765667669 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 184,832 | 6.484 | No |
| `.rdata` | 79,872 | 5.755 | No |
| `.data` | 3,584 | 1.826 | No |
| `.pdata` | 9,728 | 5.328 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 3,072 | 4.152 | No |
| `.reloc` | 2,048 | 5.271 | No |

### Imports

**USER32.dll**: `TranslateMessage`, `ShutdownBlockReasonCreate`, `GetWindowThreadProcessId`, `SetWindowLongPtrW`, `GetWindowLongPtrW`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `CreateWindowExW`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `GetMessageW`
**KERNEL32.dll**: `GetTimeZoneInformation`, `GetProcessHeap`, `FreeEnvironmentStringsW`, `GetEnvironmentStringsW`, `GetCPInfo`, `GetOEMCP`, `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetLastError`, `FreeLibrary`, `GetProcAddress`, `LoadLibraryExW`, `FormatMessageW`, `GetModuleFileNameW`
**ADVAPI32.dll**: `ConvertSidToStringSidW`, `GetTokenInformation`, `OpenProcessToken`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`

## Extracted Strings

Total strings found: **33456** (showing first 100)

```
!This program cannot be run in DOS mode.
$
}RichCZ
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
L$ SUVWH
L$ SVWH
L$ SVWH
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
@UVWAT
L9t$0t
tM@8(tHH
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
t);\$8u#3
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
u0HcH<
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
t$ WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140018c5c` | `0x140018c5c` | 40457 | ✓ |
| `fcn.14001ca40` | `0x14001ca40` | 38835 | ✓ |
| `fcn.14001ca2c` | `0x14001ca2c` | 38794 | ✓ |
| `main` | `0x140001000` | 14511 | ✓ |
| `fcn.140028080` | `0x140028080` | 12889 | ✓ |
| `fcn.14000a620` | `0x14000a620` | 6161 | ✓ |
| `fcn.140003e40` | `0x140003e40` | 5935 | ✓ |
| `fcn.14002ac50` | `0x14002ac50` | 5703 | ✓ |
| `fcn.140026d6c` | `0x140026d6c` | 4735 | ✓ |
| `fcn.140001c80` | `0x140001c80` | 2338 | ✓ |
| `fcn.140023d0c` | `0x140023d0c` | 2201 | ✓ |
| `fcn.14001822c` | `0x14001822c` | 1946 | ✓ |
| `fcn.140011400` | `0x140011400` | 1898 | ✓ |
| `fcn.140017c3c` | `0x140017c3c` | 1777 | ✓ |
| `fcn.14002cbb0` | `0x14002cbb0` | 1661 | ✓ |
| `fcn.140014f04` | `0x140014f04` | 1532 | ✓ |
| `fcn.14000c310` | `0x14000c310` | 1468 | ✓ |
| `fcn.14002ad20` | `0x14002ad20` | 1451 | ✓ |
| `fcn.140002880` | `0x140002880` | 1422 | ✓ |
| `fcn.140024a0c` | `0x140024a0c` | 1421 | ✓ |
| `fcn.140015500` | `0x140015500` | 1397 | ✓ |
| `fcn.140023d14` | `0x140023d14` | 1353 | ✓ |
| `fcn.14001455c` | `0x14001455c` | 1336 | ✓ |
| `fcn.140005230` | `0x140005230` | 1325 | ✓ |
| `fcn.14000edec` | `0x14000edec` | 1263 | ✓ |
| `fcn.14000a140` | `0x14000a140` | 1238 | ✓ |
| `fcn.140009ca0` | `0x140009ca0` | 1179 | ✓ |
| `fcn.14001ec90` | `0x14001ec90` | 1171 | ✓ |
| `fcn.1400268e0` | `0x1400268e0` | 1164 | ✓ |
| `fcn.140008ee0` | `0x140008ee0` | 1152 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001c80.c`](code/fcn.140001c80.c)
- [`code/fcn.140002880.c`](code/fcn.140002880.c)
- [`code/fcn.140003e40.c`](code/fcn.140003e40.c)
- [`code/fcn.140005230.c`](code/fcn.140005230.c)
- [`code/fcn.140008ee0.c`](code/fcn.140008ee0.c)
- [`code/fcn.140009ca0.c`](code/fcn.140009ca0.c)
- [`code/fcn.14000a140.c`](code/fcn.14000a140.c)
- [`code/fcn.14000a620.c`](code/fcn.14000a620.c)
- [`code/fcn.14000c310.c`](code/fcn.14000c310.c)
- [`code/fcn.14000edec.c`](code/fcn.14000edec.c)
- [`code/fcn.140011400.c`](code/fcn.140011400.c)
- [`code/fcn.14001455c.c`](code/fcn.14001455c.c)
- [`code/fcn.140014f04.c`](code/fcn.140014f04.c)
- [`code/fcn.140015500.c`](code/fcn.140015500.c)
- [`code/fcn.140017c3c.c`](code/fcn.140017c3c.c)
- [`code/fcn.14001822c.c`](code/fcn.14001822c.c)
- [`code/fcn.140018c5c.c`](code/fcn.140018c5c.c)
- [`code/fcn.14001ca2c.c`](code/fcn.14001ca2c.c)
- [`code/fcn.14001ca40.c`](code/fcn.14001ca40.c)
- [`code/fcn.14001ec90.c`](code/fcn.14001ec90.c)
- [`code/fcn.140023d0c.c`](code/fcn.140023d0c.c)
- [`code/fcn.140023d14.c`](code/fcn.140023d14.c)
- [`code/fcn.140024a0c.c`](code/fcn.140024a0c.c)
- [`code/fcn.1400268e0.c`](code/fcn.1400268e0.c)
- [`code/fcn.140026d6c.c`](code/fcn.140026d6c.c)
- [`code/fcn.140028080.c`](code/fcn.140028080.c)
- [`code/fcn.14002ac50.c`](code/fcn.14002ac50.c)
- [`code/fcn.14002ad20.c`](code/fcn.14002ad20.c)
- [`code/fcn.14002cbb0.c`](code/fcn.14002cbb0.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This third segment of disassembly provides significant confirmation regarding the binary’s architecture and reveals several technical layers common in sophisticated multi-stage malware that utilizes Python as an execution engine.

The analysis has been updated below to incorporate these new findings into the existing report.

---

### Updated Analysis Report (Chunk 3/3)

#### 1. Core Functionality and Purpose
The binary continues to behave as a **PyInstaller-based wrapper**, but this segment specifically highlights the infrastructure used to manage "headless" operations and the decoding of internal data structures.

*   **Bootloader Characteristics:** The presence of the string `PyInstallerOnefileHiddenWindow` and the surrounding logic (using `RegisterClassW`, `CreateWindowExW`, and `ShowWindow`) confirms that the application is designed to run a background process while hiding its console window. While common in legitimate tools, this is also a standard technique for malware to hide command-line activity from the user.
*   **Complex String Decoding/Dispatch:** The functions `fcn.140015500` and `fcn.14001455c` contain massive conditional blocks that branch based on character codes (e.g., checking for 'd', 'S', 'A', 'C'). This is characteristic of a **lexer or interpreter logic** used to parse internal commands or decode string literals within the Python environment.
*   **Decoding and Transformation:** The function `fcn.140009ca0` utilizes complex bitwise operations and lookups (e.g., `x ^ 0x1400324b0`). This is a hallmark of **Base64 decoding or a similar custom encoding/decoding algorithm**. It indicates the application is prepared to process "packed" or "hidden" data at runtime.
*   **System and File Interaction:** The use of `WriteFile`, `GetConsoleOutputCP`, and `SetEnvironmentVariableW` suggests that while the script is "hidden," it still interacts with the filesystem and environment variables, potentially for logging, configuration retrieval, or staging files for exfiltration.

#### 2. Suspicious or Malicious Behaviors
*   **Evasion Techniques:** The logic used to handle windows (hiding the console) and wait for hidden processes (`WaitForSingleObject` on a hidden window handle) is a standard "stealth" technique. It ensures that even if the script performs actions like downloading files or executing shell commands, there are no visual indicators to the user.
*   **Payload Unpacking/Decoding:** The high complexity of the decoding routine (`fcn.140009ca0`) and the intricate memory management in `fcn.1400268e0` suggest that the "malicious" part of the code is not immediately visible in the `.exe`. It is likely hidden within a data blob that only gets decoded/interpreted after the PyInstaller bootloader successfully initializes the environment.

#### 3. Notable Techniques and Patterns
*   **Sophisticated Memory Management:** The disassembly shows very precise memory manipulation, including tracking offsets and buffer sizes (e.g., `fcn.1400268e0`). This is typical of high-performance Python libraries but also allows an attacker to hide a large amount of code/data in a small, seemingly innocuous wrapper.
*   **Automated Execution Sequence:** The sequence involving `CreateProcessW`, followed by a window management loop that "waits" for the process while hiding the interface, is typical for **droppers**. It ensures that the actual heavy lifting (the Python script) runs in a controlled, hidden environment.

#### 4. Summary for Triage (Updated)
This sample is a **highly sophisticated PyInstaller-wrapped container.** 

The final disassembly segment confirms that the binary isn't just a "simple" wrapper; it contains robust logic for:
1.  **Stealth:** Explicitly hiding windows and managing background processes.
2.  **Decoding:** Processing encoded data (likely via Base64 or similar).
3.  **Environment Manipulation:** Interacting with environment variables to configure the runtime.

**Conclusion for Incident Response:** The "malicious" logic is almost certainly contained within a **dynamic payload**. The loader's job is to create a "safe haven" for the Python interpreter, where it can then unpack and run a script (the primary threat) that performs info-stealing, keylogging, or other malicious activities. 

**Recommendation:** Do not rely solely on static analysis of this `.exe`. To find the actual malware's capabilities, you must **dynamically execute it in a controlled sandbox** to capture the unpacked Python scripts and memory strings, or manually extract the `.pyz` and `.pyc` files from its internal structure.

---

### New Indicators Added
*   **Stealth Mechanism:** `PyInstallerOnefileHiddenWindow` (Confirms intent to hide UI/Console).
*   **Decoding Logic:** `fcn.140009ca0` (Evidence of Base64 or similar decoding of "hidden" payloads).
*   **Infrastructure for Complexity:** Robust memory management and string dispatch tables, indicating a large, feature-rich internal script.
*   **Process Management:** Usage of `CreateProcessW` with hidden window handles to manage the transition from loader to payload.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&C framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Valid Code/Scripts | The use of a PyInstaller wrapper and complex decoding routines (like `fcn.140009ca0`) to hide "packed" or "hidden" data is a classic method for hiding malicious scripts from static analysis. |
| **T1114** | Modify Environment Variables | The analyst specifically notes the use of `SetEnvironmentVariableW` as a mechanism for system interaction, configuration retrieval, or logging. |
| **T1059** | Command and Scripting Interpreter | The identification of Python as the primary "execution engine" used to parse internal commands and handle lexer logic confirms the use of a scripting interpreter. |
| **T1036.005** | Masquerading | The specific use of `PyInstallerOnefileHiddenWindow` and window management functions to hide console activity from the user is a method to mask the application's true purpose. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: The "EXTRACTED STRINGS" section contains high amounts of obfuscated data and internal memory addresses. While these provide context for analysts during reverse engineering, most do not qualify as direct IOCs like C2 infrastructure or specific file paths.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The analysis mentions interactions with the filesystem and environment variables but does not provide specific paths or keys).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Stealth Identifier:** `PyInstallerOnefileHiddenWindow` (Indicates the use of a PyInstaller wrapper to hide console windows and facilitate "headless" execution).
*   **Decoding Logic Indicator:** `fcn.140009ca0` (Specifically associated with XOR-based decoding: `x ^ 0x1400324b0`).
*   **Tactic / Technique:** Multi-stage loading via `CreateProcessW` for hidden process management.
*   **Decoding Pattern:** Use of complex bitwise operations and lookup tables to de-obfuscate internal scripts/payloads at runtime.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High (regarding the type)

**Key evidence**:
*   **PyInstaller Wrapper & Evasion:** The use of `PyInstallerOnefileHiddenWindow` and specific window-management functions to hide console activity confirms the intent to operate "headlessly," a common trait for loaders meant to evade user detection.
*   **Multi-Stage Decoding Logic:** The identification of complex decoding routines (e.g., `fcn.140009ca0`) and large conditional dispatch tables indicates that this binary is designed to unpack or de-obfuscate a secondary, more malicious payload at runtime.
*   **Loader Architecture:** The analysis explicitly identifies the sample as a "launcher" for a Python interpreter environment where it manages hidden processes via `CreateProcessW` to create a "safe haven" for subsequent malicious actions like information theft or command execution.
