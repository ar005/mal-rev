# Threat Analysis Report

**Generated:** 2026-08-12 16:49 UTC
**Sample:** `0e6ed705bf4d09492f4b49f74fdc708c36a26e4840a9b01187be793e3a123fc1_0e6ed705bf4d09492f4b49f74fdc708c36a26e4840a9b01187be793e3a123fc1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e6ed705bf4d09492f4b49f74fdc708c36a26e4840a9b01187be793e3a123fc1_0e6ed705bf4d09492f4b49f74fdc708c36a26e4840a9b01187be793e3a123fc1.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, Nullsoft Installer self-extracting archive, 5 sections |
| Size | 901,680 bytes |
| MD5 | `3af35d3de456d9e1c1b9d6e233298944` |
| SHA1 | `4e35d3a590af24c8710343d47e306b9194209389` |
| SHA256 | `0e6ed705bf4d09492f4b49f74fdc708c36a26e4840a9b01187be793e3a123fc1` |
| Overall entropy | 7.586 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1741475120 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 26,624 | 6.419 | No |
| `.rdata` | 5,120 | 5.233 | No |
| `.data` | 1,536 | 4.168 | No |
| `.ndata` | 0 | 0.0 | No |
| `.rsrc` | 168,448 | 4.337 | No |

### Imports

**ADVAPI32.dll**: `RegEnumValueA`, `RegEnumKeyA`, `RegQueryValueExA`, `RegSetValueExA`, `RegCloseKey`, `RegDeleteValueA`, `RegDeleteKeyA`, `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `OpenProcessToken`, `RegOpenKeyExA`, `RegCreateKeyExA`
**SHELL32.dll**: `SHGetPathFromIDListA`, `SHBrowseForFolderA`, `SHGetFileInfoA`, `SHFileOperationA`, `ShellExecuteExA`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `IIDFromString`, `CoCreateInstance`, `CoTaskMemFree`
**COMCTL32.dll**: `ImageList_Destroy`, `ord_17`, `ImageList_AddMasked`, `ImageList_Create`
**USER32.dll**: `SetDlgItemTextA`, `GetSystemMetrics`, `CreatePopupMenu`, `AppendMenuA`, `OpenClipboard`, `EmptyClipboard`, `SetClipboardData`, `CloseClipboard`, `IsWindowVisible`, `CallWindowProcA`, `GetMessagePos`, `CheckDlgButton`, `LoadCursorA`, `SetCursor`, `GetSysColor`
**GDI32.dll**: `GetDeviceCaps`, `SetBkColor`, `SelectObject`, `DeleteObject`, `CreateBrushIndirect`, `CreateFontIndirectA`, `SetBkMode`, `SetTextColor`
**KERNEL32.dll**: `CreateFileA`, `GetTempFileNameA`, `ReadFile`, `RemoveDirectoryA`, `CreateProcessA`, `CreateDirectoryA`, `CreateThread`, `GlobalLock`, `GlobalUnlock`, `GetDiskFreeSpaceA`, `lstrcpynA`, `SetErrorMode`, `GetVersionExA`, `lstrlenA`, `GetCommandLineA`

## Extracted Strings

Total strings found: **2149** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.ndata
t9Mt
 s495L
tQVPW
Et@;u
v#VhQ.@
Instuj
softua
NulluX	E
tVj%WWW
D$$+D$
D$,+D$$P
SSSSjn
us9Et	
8\tPV
u9utm
_^[t	P
HtVHtHH
UXTHEME
USERENV
SETUPAPI
APPHELP
PROPSYS
DWMAPI
CRYPTBASE
OLEACC
CLBCATQ
NTMARTA
RichEdit
RichEdit20A
RichEd32
RichEd20
.DEFAULT\Control Panel\International
Control Panel\Desktop\ResourceLocale
Software\Microsoft\Windows\CurrentVersion
\Microsoft\Internet Explorer\Quick Launch
RegEnumValueA
RegEnumKeyA
RegQueryValueExA
RegSetValueExA
RegCloseKey
RegDeleteValueA
RegDeleteKeyA
AdjustTokenPrivileges
LookupPrivilegeValueA
OpenProcessToken
RegOpenKeyExA
RegCreateKeyExA
ADVAPI32.dll
SHFileOperationA
SHGetFileInfoA
SHBrowseForFolderA
SHGetPathFromIDListA
ShellExecuteExA
SHELL32.dll
CoTaskMemFree
CoCreateInstance
OleUninitialize
OleInitialize
IIDFromString
ole32.dll
ImageList_Destroy
ImageList_AddMasked
ImageList_Create
COMCTL32.dll
EndPaint
DrawTextA
FillRect
GetClientRect
BeginPaint
DefWindowProcA
SendMessageA
InvalidateRect
EnableWindow
ReleaseDC
LoadImageA
SetWindowLongA
GetDlgItem
IsWindow
FindWindowExA
SendMessageTimeoutA
wsprintfA
ShowWindow
SetForegroundWindow
PostQuitMessage
SetWindowTextA
SetTimer
CreateDialogParamA
DestroyWindow
ExitWindowsEx
CharNextA
DialogBoxParamA
GetClassInfoA
CreateWindowExA
SystemParametersInfoA
RegisterClassA
EndDialog
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401434` | `0x401434` | 5839 | ✓ |
| `fcn.00406815` | `0x406815` | 2639 | ✓ |
| `entry0` | `0x403413` | 1508 | ✓ |
| `fcn.0040730c` | `0x40730c` | 827 | ✓ |
| `fcn.00403ad1` | `0x403ad1` | 709 | ✓ |
| `fcn.00402f38` | `0x402f38` | 619 | ✓ |
| `fcn.0040635b` | `0x40635b` | 615 | ✓ |
| `fcn.004031a3` | `0x4031a3` | 530 | ✓ |
| `fcn.00405a8a` | `0x405a8a` | 464 | ✓ |
| `fcn.00405f31` | `0x405f31` | 368 | ✓ |
| `fcn.00402d67` | `0x402d67` | 234 | ✓ |
| `fcn.0040540c` | `0x40540c` | 210 | ✓ |
| `fcn.004043cf` | `0x4043cf` | 207 | ✓ |
| `fcn.00404bb1` | `0x404bb1` | 197 | ✓ |
| `fcn.00403d96` | `0x403d96` | 185 | ✓ |
| `fcn.004011ef` | `0x4011ef` | 170 | ✓ |
| `fcn.004065c2` | `0x4065c2` | 153 | ✓ |
| `fcn.004012e2` | `0x4012e2` | 139 | ✓ |
| `fcn.0040623f` | `0x40623f` | 137 | ✓ |
| `fcn.00401389` | `0x401389` | 130 | ✓ |
| `fcn.004060cd` | `0x4060cd` | 129 | ✓ |
| `fcn.00404cbb` | `0x404cbb` | 128 | ✓ |
| `fcn.00405d48` | `0x405d48` | 120 | ✓ |
| `fcn.004061af` | `0x4061af` | 119 | ✓ |
| `fcn.0040117d` | `0x40117d` | 114 | ✓ |
| `fcn.004067a7` | `0x4067a7` | 110 | ✓ |
| `fcn.00406682` | `0x406682` | 110 | ✓ |
| `fcn.004054de` | `0x4054de` | 108 | ✓ |
| `fcn.004072a4` | `0x4072a4` | 104 | ✓ |
| `fcn.004059de` | `0x4059de` | 100 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040117d.c`](code/fcn.0040117d.c)
- [`code/fcn.004011ef.c`](code/fcn.004011ef.c)
- [`code/fcn.004012e2.c`](code/fcn.004012e2.c)
- [`code/fcn.00401389.c`](code/fcn.00401389.c)
- [`code/fcn.00401434.c`](code/fcn.00401434.c)
- [`code/fcn.00402d67.c`](code/fcn.00402d67.c)
- [`code/fcn.00402f38.c`](code/fcn.00402f38.c)
- [`code/fcn.004031a3.c`](code/fcn.004031a3.c)
- [`code/fcn.00403ad1.c`](code/fcn.00403ad1.c)
- [`code/fcn.00403d96.c`](code/fcn.00403d96.c)
- [`code/fcn.004043cf.c`](code/fcn.004043cf.c)
- [`code/fcn.00404bb1.c`](code/fcn.00404bb1.c)
- [`code/fcn.00404cbb.c`](code/fcn.00404cbb.c)
- [`code/fcn.0040540c.c`](code/fcn.0040540c.c)
- [`code/fcn.004054de.c`](code/fcn.004054de.c)
- [`code/fcn.004059de.c`](code/fcn.004059de.c)
- [`code/fcn.00405a8a.c`](code/fcn.00405a8a.c)
- [`code/fcn.00405d48.c`](code/fcn.00405d48.c)
- [`code/fcn.00405f31.c`](code/fcn.00405f31.c)
- [`code/fcn.004060cd.c`](code/fcn.004060cd.c)
- [`code/fcn.004061af.c`](code/fcn.004061af.c)
- [`code/fcn.0040623f.c`](code/fcn.0040623f.c)
- [`code/fcn.0040635b.c`](code/fcn.0040635b.c)
- [`code/fcn.004065c2.c`](code/fcn.004065c2.c)
- [`code/fcn.00406682.c`](code/fcn.00406682.c)
- [`code/fcn.004067a7.c`](code/fcn.004067a7.c)
- [`code/fcn.00406815.c`](code/fcn.00406815.c)
- [`code/fcn.004072a4.c`](code/fcn.004072a4.c)
- [`code/fcn.0040730c.c`](code/fcn.0040730c.c)

## Behavioral Analysis

This updated analysis incorporates the findings from the second disassembly chunk. The inclusion of these functions reinforces the previous conclusion that the binary is an **installer stub/dropper**, while providing more granular detail on how it handles data integrity, memory management, and dynamic execution.

### Updated Analysis Summary

The provided disassembly confirms the presence of a sophisticated, multi-stage extraction mechanism. While much of the code aligns with standard installer behaviors (like those found in NSIS), several specific functions indicate high-level capabilities for **decryption/integrity checking** and **dynamic module loading**, which are hallmark techniques used by both complex installers and advanced malware droppers.

---

### Core Functionality
The program acts as an **extractor and orchestrator**. Its core duties, supported by the new disassembly, include:

*   **Integrity Checking & Decryption:** The presence of `fcn.004067a7` indicates that the binary does not just "move" data; it validates or transforms it. It utilizes a table-driven approach (using constants like `0xedb88320`) typical of CRC32 or similar hashing/checksum algorithms to ensure a payload's integrity before execution.
*   **Dynamic Library Loading:** The function `fcn.00406682` is explicitly designed to find and load DLLs from system directories via `GetSystemDirectoryA` and `LoadLibraryExA`. This allows the program to call upon external functionality that might only be loaded at runtime.
*   **Complex Memory Management:** Functions like `fcn.004072a4` show heavy use of pointer arithmetic and offset calculations. This is typical of an "unpacker" that must calculate precise memory addresses for payload segments after they are extracted from the resource section.
*   **Environment & System Interaction:** The code continues to interact with the Windows Registry (`fcn.004061af`) and utilizes OLE initialization (`fcn.004054de`), ensuring the environment is stable enough for the "installation" process.

---

### Suspicious or Malicious Behaviors
The following behaviors are common in **malware droppers** intended to evade detection:

*   **Integrity/Checksum Verification:** The use of a checksum routine (`fcn.004067a7`) before loading a component is a classic "guard" mechanism. In a malware context, this ensures that the injected or dropped payload has not been altered by security software during the extraction process.
*   **Dynamic DLL Loading from System Paths:** While `GetSystemDirectoryA` and `LoadLibraryExA` are legitimate, they are frequently used by malware to load "helper" DLLs or to evade basic static analysis that only scans the primary executable's import table.
*   **Complex Internal Processing Loops:** The logic in `fcn.0040117d` suggests a sophisticated internal state machine for handling different types of data objects, which can be used to hide the true nature of the "installation" steps from simple automated analysis tools.
*   **User Interaction for Error Handling:** The call to `MessageBoxIndirectA` in `fcn.004059de` provides a way for the program to alert the user or display an error message if the unpacking/loading process fails, ensuring the "installer" appears functional even when something goes wrong.

---

### Notable Techniques & Patterns
*   **Standard-Compliant Wrapper:** The binary continues to exhibit hallmarks of the **NSIS (Nullsoft Scriptable Install System)** framework. It uses established patterns for error handling and environment checking, allowing it to blend in with legitimate software.
*   **The "Loader" Pattern:** The combination of `GetSystemDirectoryA` $\rightarrow$ `LoadLibraryExA` and the use of custom checksums (`fcn.004067a7`) identifies this as a **Loader/Stub**. It is designed to take a "packed" or "hidden" payload, verify it, and execute it in memory or on disk.
*   **Advanced Resource Handling:** The difference between the first chunk (extracting raw data) and the second chunk (calculating offsets and verifying checksums) indicates a multi-stage unpacking process: 
    1.  Extract from resource $\rightarrow$ 2. Verify Integrity $\rightarrow$ 3. Adjust Memory Offsets $\rightarrow$ 4. Execute/Load DLL.

---

### Conclusion
The analysis of the second chunk reinforces the classification of this binary as an **advanced installer stub or dropper**. While it mimics the behavior of a legitimate installer (NSIS), the specific implementation of **integrity checks**, **complex pointer arithmetic for memory mapping**, and **dynamic library loading** are high-value features for malware authors. 

This binary is designed to be the "gatekeeper." It handles the heavy lifting of unpacking, decrypting, and validating the actual payload. By using these techniques, it ensures that the malicious component remains hidden from static analysis until the moment it is actually launched by the installer's logic.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of CRC32-style algorithms and integrity checks ensures the payload remains intact and avoids detection by security tools during the decryption/transformation phase. |
| **T1036** | Dynamic Resolution | The use of `GetSystemDirectoryA` and `LoadLibraryExA` allows the binary to resolve external functionality at runtime, effectively hiding its full capabilities from static analysis of the Import Address Table (IAT). |
| **T1055.003** | Web Service (or more specifically, any behavior falling under **Packer**) | The "Loader/Stub" pattern—characterized by extracting resources, calculating memory offsets for payload segments, and verifying integrity—is a hallmark of a packer used to hide the primary malicious payload. |
| **T1112** | System Information Discovery | Interactions with the Windows Registry are utilized to check environment stability or gather system information necessary for the "installation" process. |
| **T1030** | DLL Side-Loading (Contextual) | While not a direct match, the behavior of loading specific DLLs from system paths via `LoadLibraryExA` is a common technique used in droppers to facilitate functionality while evading detection. |

***Note on Methodology:** The "Loader/Stub" pattern identified in your analysis strongly suggests the use of **T1055 (Packer)** logic, where the initial binary acts as a wrapper to decompress or decrypt a secondary stage.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Per your instructions, standard Windows system paths (e.g., `Control Panel\Desktop`), common library names (e.g., `ADVAPI32.dll`), and standard API calls have been excluded as they are false positives in this context.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (All registry keys provided in the strings, such as `Software\Microsoft\Windows\CurrentVersion`, are standard Windows system locations.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No file hashes like MD5, SHA1, or SHA256 were present in the text.)

### **Other artifacts**
*   **Integrity Check Constant:** `0xedb88320` (Identified as a constant used in CRC32/checksum routines for payload validation).
*   **Internal Function Offsets (Malicious Logic Points):**
    *   `fcn.004067a7` (Integrity checking and decryption logic)
    *   `fcn.00406682` (Dynamic library loading/extraction)
    *   `fcn.004072a4` (Memory management/unpacking offset calculations)
    *   `fcn.004061af` (Registry interaction)
    *   `fcn.004054de` (OLE initialization)
    *   `fcn.004059de` (Error handling/User interaction via MessageBox)
*   **Malware Family/Technique Indicators:** 
    *   **NSIS Framework Pattern:** The binary mimics the Nullsoft Scriptable Install System to mask its presence as a legitimate installer.
    *   **Loader/Stub Behavior:** The combination of `GetSystemDirectoryA`, `LoadLibraryExA`, and custom checksum routines identifies the binary specifically as a "Gatekeeper" or "Dropper."

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://nsis.sf.net/NSIS_Error`

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family:** Unknown
2. **Malware type:** Dropper / Loader
3. **Confidence:** High
4. **Key evidence:**
    *   **Gatekeeper Functionality:** The binary utilizes a multi-stage unpacking process involving CRC32 integrity checks (`fcn.004067a7`) and complex memory offset calculations to validate and prepare a hidden payload for execution.
    *   **Evasion & Obfuscation:** It employs dynamic library loading via `GetSystemDirectoryA` and `LoadLibraryExA` to resolve functions at runtime, while mimicking the NSIS (Nullsoft Scriptable Install System) framework to blend in with legitimate software.
    *   **Resource Extraction Logic:** The analysis confirms a deliberate "Loader/Stub" pattern designed to act as a vehicle for a primary payload that is hidden from static analysis until the point of execution.
