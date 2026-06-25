# Threat Analysis Report

**Generated:** 2026-06-24 19:01 UTC
**Sample:** `00b9f44d51b242ae47bafbe693921938f563c631af3fc4af8fe1e7aad65c1043_00b9f44d51b242ae47bafbe693921938f563c631af3fc4af8fe1e7aad65c1043.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `00b9f44d51b242ae47bafbe693921938f563c631af3fc4af8fe1e7aad65c1043_00b9f44d51b242ae47bafbe693921938f563c631af3fc4af8fe1e7aad65c1043.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 13,841,383 bytes |
| MD5 | `b33d6f3399715e700a7ffe78c90ac484` |
| SHA1 | `b505a1dbd4458e627857a56535fbc5877ab42227` |
| SHA256 | `00b9f44d51b242ae47bafbe693921938f563c631af3fc4af8fe1e7aad65c1043` |
| Overall entropy | 7.994 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779353443 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 101,888 | 6.247 | No |
| `.data` | 512 | 1.351 | No |
| `.rdata` | 32,256 | 6.452 | No |
| `.pdata` | 3,584 | 4.551 | No |
| `.xdata` | 3,584 | 4.145 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 6,656 | 4.419 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 19,456 | 7.901 | ⚠️ Yes |
| `.reloc` | 512 | 2.169 | No |

### Imports

**ADVAPI32.dll**: `ConvertSidToStringSidW`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `GetTokenInformation`, `OpenProcessToken`
**COMCTL32.dll**: `LoadIconMetric`
**GDI32.dll**: `CreateFontIndirectW`, `DeleteObject`, `SelectObject`
**KERNEL32.dll**: `AreFileApisANSI`, `CloseHandle`, `CreateDirectoryW`, `CreateFileW`, `CreateProcessW`, `CreateSymbolicLinkW`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileExW`, `FindFirstFileW`, `FindNextFileW`, `FormatMessageW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__argc`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `__wargv`, `__wgetmainargs`, `__winitenv`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_fileno`, `_fmode`
**USER32.dll**: `CreateWindowExW`, `DefWindowProcW`, `DestroyIcon`, `DestroyWindow`, `DialogBoxIndirectParamW`, `DispatchMessageW`, `DrawTextW`, `EndDialog`, `GetClientRect`, `GetDC`, `GetDialogBaseUnits`, `GetMessageW`, `GetWindowLongPtrW`, `InvalidateRect`, `MessageBoxA`

## Extracted Strings

Total strings found: **27920** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
@.reloc
AWAVAUATUWVSH
X[^_]A\A]A^A_
8MZuEHcP<H
AWAVAUATUWVSH
[^_]A\A]A^A_
AUATUWVSH
8[^_]A\A]
AUATUWVSH
([^_]A\A]
([^_]A\A]
ATUWVSH
 [^_]A\
 [^_]A\
AUATUWVSH
l$<fD+l$4
H[^_]A\A]
fD+D$df+T$`
ATUWVS
[^_]A\A]
[^_]A\
[^_]A\
[^_]A\
[^_]A\
AVAUATUWVS
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
[^_]A\
[^_]A\
[^_]A\
ATUWVS
[^_]A\A]
AWAVAUATUWVSH
([^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
uNMcJ0E
ATUWVS
[^_]A\A^
AWAVAUATUWVSH
8[^_]A\A]A^A_
O8LcG0H
AVAUATUWVSH
`[^_]A\A]A^
ATUWVSH
 [^_]A\
 [^_]A\
ATUWVSH
 [^_]A\
ATUWVSH
0[^_]A\
AVAUATUWVS
[^_]A\A]A^A_
AWAVAUATUWVSH
([^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
ATUWVSH
 [^_]A\
 [^_]A\
AVAUATUWVSH
@[^_]A\A]A^
AVAUATUWVS
[^_]A\A]A^A_
AWAVAUATUWVSH
([^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AVWVSH
h[^_A^
AVAUATUWVS
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
AVAUATUWVS
[^_]A\A]A^A_
D$xH+D$hHi
AWAVAUATUWVSH
([^_]A\A]A^A_
D$L;L$
AWAVAUATUWVSH
([^_]A\A]A^A_
L3^ I1
AWAVAUATUWVSH
sL;D$
D9L$,s
H[^_]A\A]A^A_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140001420` | `0x140001420` | 99894 | ✓ |
| `fcn.14000f700` | `0x14000f700` | 58217 | ✓ |
| `fcn.14000ff20` | `0x14000ff20` | 39542 | ✓ |
| `fcn.140005220` | `0x140005220` | 8894 | ✓ |
| `fcn.14000c490` | `0x14000c490` | 7984 | ✓ |
| `fcn.140016840` | `0x140016840` | 7537 | ✓ |
| `fcn.1400021d0` | `0x1400021d0` | 3495 | ✓ |
| `fcn.140015960` | `0x140015960` | 3054 | ✓ |
| `fcn.140012da0` | `0x140012da0` | 2888 | ✓ |
| `fcn.1400030c0` | `0x1400030c0` | 2729 | ✓ |
| `fcn.140015120` | `0x140015120` | 2100 | ✓ |
| `fcn.1400116f0` | `0x1400116f0` | 2084 | ✓ |
| `fcn.1400051a0` | `0x1400051a0` | 1755 | ✓ |
| `fcn.1400071a0` | `0x1400071a0` | 1545 | ✓ |
| `fcn.14000b980` | `0x14000b980` | 1527 | ✓ |
| `fcn.14000edc0` | `0x14000edc0` | 1306 | ✓ |
| `fcn.14000a200` | `0x14000a200` | 1236 | ✓ |
| `fcn.140011220` | `0x140011220` | 1223 | ✓ |
| `fcn.140014480` | `0x140014480` | 1223 | ✓ |
| `fcn.1400128e0` | `0x1400128e0` | 1203 | ✓ |
| `fcn.140014950` | `0x140014950` | 1187 | ✓ |
| `fcn.14000b5b0` | `0x14000b5b0` | 1128 | ✓ |
| `fcn.140012070` | `0x140012070` | 1120 | ✓ |
| `fcn.140013f30` | `0x140013f30` | 1120 | ✓ |
| `fcn.140006540` | `0x140006540` | 1104 | ✓ |
| `fcn.14000afb0` | `0x14000afb0` | 1000 | ✓ |
| `fcn.140001010` | `0x140001010` | 976 | ✓ |
| `fcn.14000fb50` | `0x14000fb50` | 974 | ✓ |
| `fcn.140001490` | `0x140001490` | 964 | ✓ |
| `fcn.140003db0` | `0x140003db0` | 952 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001010.c`](code/fcn.140001010.c)
- [`code/fcn.140001420.c`](code/fcn.140001420.c)
- [`code/fcn.140001490.c`](code/fcn.140001490.c)
- [`code/fcn.1400021d0.c`](code/fcn.1400021d0.c)
- [`code/fcn.1400030c0.c`](code/fcn.1400030c0.c)
- [`code/fcn.140003db0.c`](code/fcn.140003db0.c)
- [`code/fcn.1400051a0.c`](code/fcn.1400051a0.c)
- [`code/fcn.140005220.c`](code/fcn.140005220.c)
- [`code/fcn.140006540.c`](code/fcn.140006540.c)
- [`code/fcn.1400071a0.c`](code/fcn.1400071a0.c)
- [`code/fcn.14000a200.c`](code/fcn.14000a200.c)
- [`code/fcn.14000afb0.c`](code/fcn.14000afb0.c)
- [`code/fcn.14000b5b0.c`](code/fcn.14000b5b0.c)
- [`code/fcn.14000b980.c`](code/fcn.14000b980.c)
- [`code/fcn.14000c490.c`](code/fcn.14000c490.c)
- [`code/fcn.14000edc0.c`](code/fcn.14000edc0.c)
- [`code/fcn.14000f700.c`](code/fcn.14000f700.c)
- [`code/fcn.14000fb50.c`](code/fcn.14000fb50.c)
- [`code/fcn.14000ff20.c`](code/fcn.14000ff20.c)
- [`code/fcn.140011220.c`](code/fcn.140011220.c)
- [`code/fcn.1400116f0.c`](code/fcn.1400116f0.c)
- [`code/fcn.140012070.c`](code/fcn.140012070.c)
- [`code/fcn.1400128e0.c`](code/fcn.1400128e0.c)
- [`code/fcn.140012da0.c`](code/fcn.140012da0.c)
- [`code/fcn.140013f30.c`](code/fcn.140013f30.c)
- [`code/fcn.140014480.c`](code/fcn.140014480.c)
- [`code/fcn.140014950.c`](code/fcn.140014950.c)
- [`code/fcn.140015120.c`](code/fcn.140015120.c)
- [`code/fcn.140015960.c`](code/fcn.140015960.c)
- [`code/fcn.140016840.c`](code/fcn.140016840.c)

## Behavioral Analysis

This updated analysis incorporates the findings from **chunk 4/4**. This final set of disassembly provides a clear look into the "unpacking" mechanism, memory management, and underlying library support that allows the binary to function as a standalone container for a Python environment.

---

### Updated Analysis of Binary Functionality

#### 1. Decompression & Extraction (New)
The function `fcn.140001490` provides high-confidence evidence of how the payload is "unpacked" from the single executable:
*   **Zlib/Inflate Logic:** The code explicitly references decompression routines (`inflateInit`, `inflate`). 
*   **In-Memory Decompression:** Instead of writing a full installer to disk, the logic suggests it decompresses data into allocated memory buffers.
*   **Success/Failure Logging:** It includes specific error strings like `"Failed to extract %s: inflateInit() failed..."` and `"decompression resulted in return code..."`.
*   **Significance:** This is the core mechanism of PyInstaller's "OneFile" mode. The actual Python interpreter and scripts are compressed inside the EXE; this function extracts them into memory so they can be executed without a permanent installation on the disk.

#### 2. Memory Manipulation (New)
The function `fcn.14000fb50` reveals how the loader prepares segments for execution:
*   **VirtualProtect Calls:** The code calls `VirtualProtect` at the end of its processing loop.
*   **Permissions Management:** This is used to change the memory permissions of a buffer (e.g., from Read/Write to Read/Execute). 
*   **Significance:** This ensures that after the "unpacking" logic has finished, the memory space containing the decompressed Python code is flagged as executable by the Windows OS.

#### 3. Advanced Data Handling & Parsing (Updated)
The logic in `fcn.14000fb50` and the main entry block shows highly structured data handling:
*   **Complex Type Mapping:** The switch-like behavior (checking if a value is 8, 0x20, or 0x40) suggests it is processing a table of "objects" or "symbols."
*   **Length Calculation & Memory Allocation:** There is significant logic dedicated to calculating string lengths and performing `memcpy` operations into newly allocated memory blocks. This is typical of the internal Python/Tcl library handling various types of data structures.

#### 4. GUI Component Initialization (Updated)
The function `fcn.140003db0` provides further insight into the environment:
*   **Standard Window Controls:** It interacts with standard Windows widgets (`STATIC`, `EDIT`, `BUTTON`).
*   **Tcl/Tk Interaction:** While we previously identified the Tcl/Tk presence, this confirms that the underlying library is preparing for potential graphical interactions (e.g., if the script uses a GUI).

---

### Updated Summary of Risks and Behaviors

| Feature | Observation | Risk Significance |
| :--- | :--- | :--- |
| **In-Memory Decompression** | Use of `inflate` logic to unpack data into memory rather than extracting files to disk. | **High:** This allows the "real" malicious payload to remain hidden from traditional file-based scanners. |
| **Execution Prep (VirtualProtect)** | Changing memory permissions to allow execution of unpacked segments. | **High:** A core signature of self-extracting loaders; indicates where the transition from "loader" to "payload" occurs. |
| **Robust Argument Parsing** | Logic for handling `__wmarg` and manual string allocations for command-line arguments. | **Low:** Standard behavior, but confirms the loader can pass complex instructions/arguments to the underlying script. |
| **Resource Management** | Extensive use of memory allocation and copying (`memcpy`) during initialization. | **Medium:** Indicates a heavy internal library (Python/Tcl) is being initialized to host the payload. |

---

### Updated Technical Findings & Indicators

*   **Packaging Signature:** The presence of `inflate` logic, `VirtualProtect`, and specific "Extract" error strings confirms this is not a custom-written loader but a standard PyInstaller "OneFile" construction.
*   **Memory Behavior:** 
    1.  The binary loads and decompresses compressed data into memory (via `fcn.140001490`).
    2.  It maps out the internal structure of the loaded data (`fcn.14000fb50`).
    3.  It sets appropriate permissions for those memory regions using `VirtualProtect`.
*   **Process Flow:** The loader acts as a "pre-processor." It does the heavy lifting of unpacking and preparing the environment so that the malicious script can run in a clean, pre-configured Python environment.

---

### Updated Recommendations for Incident Response

1.  **Memory Forensics (Critical):** 
    *   Because much of the "malicious" content is decompressed into memory only *after* `VirtualProtect` is called, **memory dumps** are essential. Scan the process memory for strings or code that appears after the execution begins but was not visible in the initial file on disk.
2.  **Behavioral Monitoring:** 
    *   Monitor for processes calling `VirtualProtect` with `PAGE_EXECUTE_READWRITE` (or similar) followed by a jump into those newly allocated regions. This is a common indicator of a loader handing over execution to a payload.
3.  **Advanced Alerting:**
    *   Create alerts for the presence of strings like `inflateInit`, `PyInstallerOnefileHiddenWindow`, and `_wmarg` in portable executables. While these are "benign" (part of PyInstaller), they identify tools frequently used by threat actors to wrap malicious Python scripts.
4.  **Static Analysis Bypass:**
    *   As confirmed across all four chunks, **standard static analysis is likely to fail** to find the "true" payload because the core logic is compressed and only exists in its usable form in memory. Use `pyinstxtractor` or a debugger to capture the state of the process after the decompression functions have completed.

**Final Conclusion:** The analysis confirms that this binary is a **highly standardized PyInstaller "OneFile" wrapper.** It successfully hides the primary payload by unpacking it into memory and using hidden windows to mask the script's execution. Every significant "malicious" behavior (the theft, the backconnect, etc.) is contained within the Python environment initialized by these functions. The loader is the vessel; the script inside is the weapon.

---

## MITRE ATT&CK Mapping

Based on the provided behavior analysis, here is the mapping of observed behaviors to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Packer | The use of `inflate` logic and `VirtualProtect` indicates a packer-based architecture designed to decompress and execute a payload in memory. |
| **T1059.003** | Command and Scripting Interpreter: Python | The analysis confirms the binary acts as a container for a Python environment to host and run the primary script logic. |
| **T1027** | Obfuscated Files or Information | The use of in-memory decompression ensures that the "real" malicious payload remains hidden from traditional file-based security scanners. |
| **T1106** | Native API | The use of `VirtualProtect` is a specific Windows API call used to manipulate memory permissions for executing unpacked code. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** As this is a PyInstaller "OneFile" wrapper, many of the indicators are "behavioral" or "structural" rather than hard indicators like specific IP addresses, as the malicious payload is unpacked into memory at runtime.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (the analysis notes that payloads are extracted to memory rather than disk).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   No MD5, SHA-1, or SHA-256 hashes were present in the provided strings.

### **Other artifacts (Behavioral & Structural)**
The following indicators relate to the construction and execution patterns of the loader:

*   **Known Framework Artifacts:**
    *   `inflateInit()` (Indicates Zlib decompression logic)
    *   `PyInstallerOnefileHiddenWindow` (Identifies the specific use of PyInstaller's "OneFile" mode)
    *   `__wmarg` (Internal variable for handling command-line arguments in bundled scripts)

*   **Error Strings (Detection Signatures):**
    *   `Failed to extract %s: inflateInit() failed with return code %d!`
    *   `Failed to extract %s: failed to allocate temporary input buffer!`
    *   `Failed to extract %s: failed to allocate temporary output buffer!`

*   **Suspicious Behavior/TTPs:**
    *   **Memory Manipulation:** Use of `VirtualProtect` to change memory permissions (specifically transitioning from Read/Write to Execute) following the decompression of data.
    *   **In-Memory Execution:** Extraction and execution of code into allocated memory buffers rather than local disk storage.
    *   **Obfuscation Strategy:** Usage of "OneFile" packing to hide Python scripts, third-party libraries (like Tcl/Tk), and potential malicious payloads from standard static scanners.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family:** PyInstaller Wrapper (or "Custom" if referring to a specific threat actor campaign, as one is not identified)
2.  **Malware type:** Loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Signature Construction:** The presence of specific strings (`inflateInit`, `PyInstallerOnefileHiddenWindow`, and `_wmarg`) and the use of Zlib decompression logic confirm this is a standard PyInstaller "OneFile" bundle used to wrap Python scripts into a single executable.
    *   **Evasive Execution:** The use of `VirtualProtect` to transition memory from Read/Write to Execute, combined with in-memory decompression (avoiding writing files to disk), is a classic technique used by loaders to hide the final payload from static analysis.
    *   **Function as a "Container":** The analysis confirms the binary acts as a pre-processor that prepares a Python environment; the malicious behaviors (backconnect, theft) are hosted within the hidden script rather than the loader itself.
