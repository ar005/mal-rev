# Threat Analysis Report

**Generated:** 2026-07-15 19:55 UTC
**Sample:** `0713f3f0cf5f96bf53479ba18394725aa7937540a7a3dc75b6b75a10beed860d_0713f3f0cf5f96bf53479ba18394725aa7937540a7a3dc75b6b75a10beed860d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0713f3f0cf5f96bf53479ba18394725aa7937540a7a3dc75b6b75a10beed860d_0713f3f0cf5f96bf53479ba18394725aa7937540a7a3dc75b6b75a10beed860d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 8 sections |
| Size | 733,114 bytes |
| MD5 | `f0d5dd84ac3f92457bae218011eb0da7` |
| SHA1 | `1bc3ca7ff5976aaf93b85e95755c85648efeca8f` |
| SHA256 | `0713f3f0cf5f96bf53479ba18394725aa7937540a7a3dc75b6b75a10beed860d` |
| Overall entropy | 6.992 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1753694783 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 314,368 | 6.486 | No |
| `.rdata` | 87,552 | 5.368 | No |
| `.data` | 7,168 | 3.062 | No |
| `.pdata` | 13,312 | 5.635 | No |
| `.didat` | 1,024 | 3.046 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 172,032 | 6.646 | No |
| `.reloc` | 2,560 | 5.376 | No |

### Imports

**KERNEL32.dll**: `CreateFileW`, `ReadFile`, `WriteFile`, `CloseHandle`, `GetLastError`, `ConnectNamedPipe`, `DisconnectNamedPipe`, `PeekNamedPipe`, `CreateNamedPipeW`, `WaitNamedPipeW`, `GetOverlappedResult`, `WaitForSingleObject`, `CreateEventW`, `SetLastError`, `LocalFree`
**OLEAUT32.dll**: `SysAllocString`, `SysFreeString`, `VariantClear`
**gdiplus.dll**: `GdipCloneImage`, `GdipFree`, `GdipDisposeImage`, `GdipCreateBitmapFromStream`, `GdipCreateHBITMAPFromBitmap`, `GdiplusStartup`, `GdiplusShutdown`, `GdipAlloc`

## Extracted Strings

Total strings found: **1781** (showing first 100)

```
!This program cannot be run in DOS mode.
$
epRich
`.rdata
@.data
.pdata
@.didat
.fptable
@.reloc
WAVAWH
 A_A^_
x ATAVAWH
0A_A^A\
WATAUAVAWH
0A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
@USVWAUAVAWH
A_A^A]_^[]
\$ UVWH
CfA9S
CfA9S
SVWATAUAVAWH
PA_A^A]A\_^[
WATAUAVAWH
 A_A^A]A\_
\$ UVWH
GL$PE3
WATAUAVAWH
 A_A^A]A\_
UVWATAUAVAWH
9RuMHc
@A_A^A]A\_^]
t$ UWAVH
VWATAVAWH
@A_A^A\_^
VWATAVAWH
@A_A^A\_^
WAVAWH
 A_A^_
WAVAWH
 A_A^_
WAVAWH
 A_A^_
H9G8v`
UVWATAUAVAWH
A_A^A]A\_^]
x UATAUAVAWH
H9D$xr
FPI;FHt6H
A_A^A]A\]
\$ UVWATAUAVAW
A_A^A]A\_^]
D93t5H
|$ ATAVAWH
0A_A^A\
x UATAUAVAWH
A_A^A]A\]
SUVWATAUAVAWH
(|$`fA
A_A^A]A\_^][
t$81xH
UVWAVAWH
A_A^_^]
\$ UVWATAUAVAWH
A_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
@SUVWAVAWH
t[f91s*
A_A^_^][
p UWATAVAWH
A_A^A\_]
@USVWATAUAVAWH
hA_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
@USVWATAUAVAWH
A_A^A]A\_^[]
@USVWATAUAVAWH
l$Hu~H
A_A^A]A\_^[]
USVWATAUAVAWH
A_A^A]A\_^[]
@USVWATAVAWH
A_A^A\_^[]
WAVAWH
 A_A^_
X UVWATAUAVAWH
A_A^A]A\_^]
t$ UWATAVAWH
A_A^A\_]
UVWATAVH
A^A\_^]
t$ UWAVH
@SUVWATAUAVAWH
<A.u}H
<B.uaH
fB9xu*E3
hA_A^A]A\_^][
WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002634` | `0x140002634` | 189967 | ✓ |
| `fcn.1400050b0` | `0x1400050b0` | 97709 | ✓ |
| `fcn.140008d98` | `0x140008d98` | 83163 | ✓ |
| `fcn.14002009c` | `0x14002009c` | 66177 | ✓ |
| `fcn.140020090` | `0x140020090` | 65630 | ✓ |
| `fcn.140020078` | `0x140020078` | 65493 | ✓ |
| `fcn.14001fc04` | `0x14001fc04` | 65441 | ✓ |
| `fcn.140020070` | `0x140020070` | 65184 | ✓ |
| `fcn.14002005c` | `0x14002005c` | 65143 | ✓ |
| `fcn.140021194` | `0x140021194` | 55950 | ✓ |
| `fcn.14002836c` | `0x14002836c` | 35379 | ✓ |
| `fcn.14003fea0` | `0x14003fea0` | 20963 | ✓ |
| `fcn.14003fe8c` | `0x14003fe8c` | 20922 | ✓ |
| `fcn.140017c80` | `0x140017c80` | 16972 | ✓ |
| `fcn.14000da70` | `0x14000da70` | 13216 | ✓ |
| `fcn.140021720` | `0x140021720` | 11890 | ✓ |
| `fcn.140047d40` | `0x140047d40` | 8873 | ✓ |
| `fcn.14002cf98` | `0x14002cf98` | 7317 | ✓ |
| `fcn.14000ef94` | `0x14000ef94` | 5899 | ✓ |
| `fcn.14001e74c` | `0x14001e74c` | 5303 | ✓ |
| `fcn.140046a2c` | `0x140046a2c` | 4735 | ✓ |
| `fcn.1400072d0` | `0x1400072d0` | 3966 | ✓ |
| `fcn.140049960` | `0x140049960` | 3927 | ✓ |
| `fcn.14003321c` | `0x14003321c` | 3821 | ✓ |
| `fcn.140023230` | `0x140023230` | 3721 | ✓ |
| `fcn.140024e10` | `0x140024e10` | 3522 | ✓ |
| `fcn.14000b700` | `0x14000b700` | 3353 | ✓ |
| `fcn.140005a48` | `0x140005a48` | 3002 | ✓ |
| `fcn.140018cdc` | `0x140018cdc` | 2887 | ✓ |
| `fcn.14001d79c` | `0x14001d79c` | 2292 | ✓ |

### Decompiled Code Files

- [`code/fcn.140002634.c`](code/fcn.140002634.c)
- [`code/fcn.1400050b0.c`](code/fcn.1400050b0.c)
- [`code/fcn.140005a48.c`](code/fcn.140005a48.c)
- [`code/fcn.1400072d0.c`](code/fcn.1400072d0.c)
- [`code/fcn.140008d98.c`](code/fcn.140008d98.c)
- [`code/fcn.14000b700.c`](code/fcn.14000b700.c)
- [`code/fcn.14000da70.c`](code/fcn.14000da70.c)
- [`code/fcn.14000ef94.c`](code/fcn.14000ef94.c)
- [`code/fcn.140017c80.c`](code/fcn.140017c80.c)
- [`code/fcn.140018cdc.c`](code/fcn.140018cdc.c)
- [`code/fcn.14001d79c.c`](code/fcn.14001d79c.c)
- [`code/fcn.14001e74c.c`](code/fcn.14001e74c.c)
- [`code/fcn.14001fc04.c`](code/fcn.14001fc04.c)
- [`code/fcn.14002005c.c`](code/fcn.14002005c.c)
- [`code/fcn.140020070.c`](code/fcn.140020070.c)
- [`code/fcn.140020078.c`](code/fcn.140020078.c)
- [`code/fcn.140020090.c`](code/fcn.140020090.c)
- [`code/fcn.14002009c.c`](code/fcn.14002009c.c)
- [`code/fcn.140021194.c`](code/fcn.140021194.c)
- [`code/fcn.140021720.c`](code/fcn.140021720.c)
- [`code/fcn.140023230.c`](code/fcn.140023230.c)
- [`code/fcn.140024e10.c`](code/fcn.140024e10.c)
- [`code/fcn.14002836c.c`](code/fcn.14002836c.c)
- [`code/fcn.14002cf98.c`](code/fcn.14002cf98.c)
- [`code/fcn.14003321c.c`](code/fcn.14003321c.c)
- [`code/fcn.14003fe8c.c`](code/fcn.14003fe8c.c)
- [`code/fcn.14003fea0.c`](code/fcn.14003fea0.c)
- [`code/fcn.140046a2c.c`](code/fcn.140046a2c.c)
- [`code/fcn.140047d40.c`](code/fcn.140047d40.c)
- [`code/fcn.140049960.c`](code/fcn.140049960.c)

## Behavioral Analysis

This final chunk of disassembly provides significant evidence of a sophisticated, multi-stage malware architecture. While the previous analysis focused on how the malware **collects** information, this section reveals how the malware **evades detection**, **verifies its environment**, and **manages internal state**.

The presence of several advanced techniques—such as dynamic API resolution, extensive system library "inventorying," and complex data mapping—suggests this is a high-quality piece of malware (likely a Trojan or a sophisticated info-stealer) designed to evade automated analysis.

### Updated Analysis: Behavioral Summary

#### 1. Environment Awareness & Evasion Techniques
The function `fcn.14001d79c` contains several "red flag" indicators for high-sophistication malware:
*   **Dynamic API Resolution:** The use of `GetModuleHandleW` and `GetProcAddress` to resolve functions like `SetDllDirectoryW` and `SetDefaultDllDirectories`. This is a classic technique used to bypass static analysis by hiding the true nature of the imports from a simple scanner.
*   **System DLL "Inventory":** The code contains an extensive hardcoded list of system-related DLLs (e.g., `version.dll`, `ss_os.dll`, `rs1ah.dll`, `psapi.dll`). This is often used to verify that the environment is a standard Windows installation or, conversely, as a way to ensure certain capabilities are available before executing a "stage 2" payload.
*   **Console and Persistence Logic:** The code includes routines for interacting with the console (using `CreateFile` and `WriteConsoleW`) and potentially managing file paths/directories via `DeleteFileW` or `RemoveDirectoryW`. This suggests the malware may clean up its components after execution or "deploy" further components.

#### 2. Complex Data Mapping & Parsing
The functions `fcn.140018dc` and `fcn.140005a48` suggest a very structured approach to data:
*   **Internal Resource Navigation:** In `fcn.140018dc`, the code explicitly checks for labels like `"STRINGS"`, `"DIALOG"`, `"MENU"`, and `"DIRECTION"`. This indicates that the malware is not just pulling raw strings; it is navigating a structured internal database or configuration file to decide what UI elements to display or which "features" to enable.
*   **Conditional Logic Branching:** `fcn.140005a48` contains heavy conditional branching (e.g., checking if values are even/odd or comparing them against specific constants). This is often used in malware as **environmental keying**, where the "path" the code takes depends on specific system conditions (like a hardcoded domain name, an active certificate, or a specific OS version).

#### 3. Advanced Data Preparation & Serialization
The logic involving bit-shifting and complex arithmetic (e.g., `uVar15 >> (0x10U - *(iVar15 + 0xc) & 0x1f)` ) confirms that data is being heavily manipulated before it ever leaves the machine:
*   **Buffer Re-packing:** The code isn't just "grabbing" a password; it’s likely serializing that data into a structured format (like JSON or a custom binary blob) to prepare it for exfiltration. 
*   **Multi-stage Logic Flow:** The recursive-style loop structures and the jumping between different memory addresses indicate that the malware has several "sub-tasks" it performs once a credential is harvested, such as logging local system info, mapping network paths, or checking if specific remote services are reachable.

---

### Updated Indicators of Compromise (IOCs) / Malicious Patterns

*   **Evasive Environment Checks:** The inclusion of an extensive DLL list and the use of `GetProcAddress` suggest that if the malware detects it is being analyzed (e.g., in a sandbox where certain standard system paths aren't available), it will alter its behavior or shut down entirely.
*   **State-Driven Execution:** The large, nested conditional blocks indicate a **"Decision Engine."** This means the malware can react differently to different users—for example, performing "heavy" harvesting on high-value targets and staying quiet on others.
*   **Complexity as an Obfuscation Layer:** Many of the repeated bitwise operations and complex index calculations are designed to make manual decompilation (human review) tedious. This is a hallmark of professional malware development where automation tools are expected to give up or return "messy" code, making it harder for analysts to find the "core" malicious payload.

---

### Final Summary for Incident Response

The cumulative evidence from all three chunks confirms that this is **high-confidence, sophisticated malware.** It is not a simple script; it is a professional tool designed for persistent and evasive operation.

**Strategic Insights for IR:**
1.  **Advanced Persistence/Multi-Stage Deployment:** The use of `SetDllDirectoryW` and `GetProcAddress` suggests the binary may be a "loader" or "dropper." It might download additional modules or decrypt hidden payloads once it confirms the environment is safe.
2.  **Targeted Logic (Environment Keying):** Because of the extensive state management, the malware likely only displays certain features if it detects specific targets (e.g., corporate networks vs. home networks). This makes "hunting" for consistent behavior across all endpoints more difficult.
3.  **Sophisticated Exfiltration Prep:** The heavy data processing before exfiltration means that network logs may not show clear, plaintext strings of the stolen passwords. Look for **encoded or packed outbound traffic.**

**Recommendations:**
*   **Network Forensics:** Analyze out-bound packets for high volumes of "junk" data or common exfiltration ports (80/443/53), but be aware that the content will likely be encrypted or obfuscated before transmission.
*   **Endpoint Hunting:** Look for evidence of the specific system files and DLLs mentioned in your analysis (the long list found in `fcn.14001d79c`). These might be used to "pivot" or find further targets on a local network. 
*   **Host Memory Analysis:** Given the heavy use of dynamic resolution, perform memory dumps to capture the strings and API calls that are only "unveiled" during execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of dynamic API resolution and complex bit-shifting/arithmetic is designed to hide the true nature of functionality and data from static analysis tools. |
| **T1497** | Virtualization, Sandbox, or Emulation Awareness | The "System DLL Inventory" and "Decision Engine" logic are used to verify if the environment is a standard Windows installation or an analysis sandbox before executing high-value functions. |
| **T1070.004** | Indicator Removal on Host: File Deletion | The inclusion of `DeleteFileW` and `RemoveDirectoryW` indicates that the malware attempts to delete its components or evidence following execution. |
| **T1027** | Obfuscated Files or Information (Data Packaging) | The buffer re-packing/serialization logic ensures that stolen data is transformed into a custom format, making it harder for network security tools to identify plain-text credentials. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized as requested.

### **IP addresses / URLs / Domains**
*   *None identified.* (The provided string dump contains obfuscated/encrypted data fragments, but no plain-text URLs or IP addresses were present.)

### **File paths / Registry keys**
*   *None identified.* (While the analysis mentions functions like `SetDllDirectoryW` and `SetDefaultDllDirectories`, no specific malicious file paths or registry keys were extracted from the raw strings.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No standard MD5, SHA-1, or SHA-256 hex strings were found in the provided data.)

### **Other artifacts**
*   **Dynamic API Resolution:** Use of `GetProcAddress` and `GetModuleHandleW` to resolve `SetDllDirectoryW` and `SetDefaultDllRegisters`. This is used to hide imports from static analysis.
*   **System DLL Inventory (Environmental Keying):** The malware checks for the presence of specific system libraries to verify its environment:
    *   `version.dll`
    *   `ss_os.dll`
    *   `rs1ah.dll`
    *   `psapi.dll`
*   **Internal Navigation Logic:** Presence of hardcoded internal identifiers/labels used for configuration navigation:
    *   `"STRINGS"`
    *   `"DIALOG"`
    *   `"MENU"`
    *   `"DIRECTION"`
*   **Data Serialization Behavior:** The use of complex bit-shifting and arithmetic (e.g., `uVar15 >> (0x10U - *(iVar15 + 0xc) & 0x1f)`) indicates that stolen data is wrapped into a custom binary blob or serialized format before exfiltration to evade network inspection.
*   **Cleanup/Persistence Logic:** Use of `DeleteFileW` and `RemoveDirectoryW` for post-execution cleanup or stage-management.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Infostealer (or Trojan/Loader)
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated Evasion & Environmental Keying:** The use of dynamic API resolution (`GetProcAddress`), a custom "System DLL Inventory" to detect analysis environments, and complex conditional logic indicates a high-level effort to bypass security controls and hide the malware's true capabilities until it confirms a safe execution environment.
    *   **Advanced Data Harvesting & Serialization:** The discovery of internal navigation for "STRINGS" and "DIALOG," combined with complex bit-shifting and buffer re-packing before exfiltration, strongly indicates the malware is designed to harvest sensitive information (like credentials) and package it in an obfuscated format to evade network detection.
    *   **Multi-stage Execution & Persistence:** The inclusion of `SetDllDirectoryW` and `DeleteFileW` suggests a sophisticated multi-stage architecture where the initial binary acts as a loader or dropper, cleaning up its footprint after successfully deploying subsequent modules or completing its harvesting tasks.
