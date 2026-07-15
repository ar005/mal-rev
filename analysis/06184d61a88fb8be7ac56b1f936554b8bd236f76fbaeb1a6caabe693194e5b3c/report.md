# Threat Analysis Report

**Generated:** 2026-07-14 21:16 UTC
**Sample:** `06184d61a88fb8be7ac56b1f936554b8bd236f76fbaeb1a6caabe693194e5b3c_06184d61a88fb8be7ac56b1f936554b8bd236f76fbaeb1a6caabe693194e5b3c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `06184d61a88fb8be7ac56b1f936554b8bd236f76fbaeb1a6caabe693194e5b3c_06184d61a88fb8be7ac56b1f936554b8bd236f76fbaeb1a6caabe693194e5b3c.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 12,617,397 bytes |
| MD5 | `adbbd801874c45f63e594f0d2302911d` |
| SHA1 | `63097303ef0dad26e9c8a17ce38cd23bea6b0709` |
| SHA256 | `06184d61a88fb8be7ac56b1f936554b8bd236f76fbaeb1a6caabe693194e5b3c` |
| Overall entropy | 7.993 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771759106 |
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
| `.rsrc` | 19,968 | 7.911 | ⚠️ Yes |
| `.reloc` | 512 | 2.169 | No |

### Imports

**ADVAPI32.dll**: `ConvertSidToStringSidW`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `GetTokenInformation`, `OpenProcessToken`
**COMCTL32.dll**: `LoadIconMetric`
**GDI32.dll**: `CreateFontIndirectW`, `DeleteObject`, `SelectObject`
**KERNEL32.dll**: `AreFileApisANSI`, `CloseHandle`, `CreateDirectoryW`, `CreateFileW`, `CreateProcessW`, `CreateSymbolicLinkW`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileExW`, `FindFirstFileW`, `FindNextFileW`, `FormatMessageW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__argc`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `__wargv`, `__wgetmainargs`, `__winitenv`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_fileno`, `_fmode`
**USER32.dll**: `CreateWindowExW`, `DefWindowProcW`, `DestroyIcon`, `DestroyWindow`, `DialogBoxIndirectParamW`, `DispatchMessageW`, `DrawTextW`, `EndDialog`, `GetClientRect`, `GetDC`, `GetDialogBaseUnits`, `GetMessageW`, `GetWindowLongPtrW`, `InvalidateRect`, `MessageBoxA`

## Extracted Strings

Total strings found: **25325** (showing first 100)

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

This final chunk of disassembly completes the technical picture of the binary's architecture. It confirms that this is not just a simple wrapper, but a sophisticated **multi-stage loader** capable of unpacking and preparing complex data in memory before executing the primary logic.

Here is the final updated analysis including all findings from chunks 1 through 4.

---

# Final Analysis Report: PyInstaller Wrapper & Tcl/Tk Integration

### **1. Executive Summary**
The binary is a high-complexity **PyInstaller "OneFile" bundle**. It functions as a multi-stage loader designed to host a Python environment, extract its internal components (libraries and scripts), and manage a graphical user interface (via Tcl/Tk). 

From a security perspective, the binary acts as a **sophisticated container**. While the wrapper itself is standard for Python distribution, it provides a significant layer of "cloaking": the actual malicious logic (if any) resides in compressed segments that are only unpacked and decrypted into memory during runtime.

---

### **2. Detailed Technical Analysis**

#### **A. The Extraction Engine (`fcn.140001490`)**
This is a critical find in the final chunk. This function handles the extraction of internal data:
*   **Decompression Logic:** The presence of `inflateInit()` and `inflate()` (typical zlib/gzip functions) confirms that the binary contains a **packed archive**. 
*   **Mechanism:** It reads raw data from an internal buffer, decompresses it using `inflate` algorithms, and "inflates" it into usable segments. 
*   **Significance:** This is the core of the PyInstaller "OneFile" mechanism. It confirms that the Python bytecode (`.pyc`) and any necessary `.dll` or `.so` files are compressed inside this `.exe`.

#### **B. Memory Manipulation & Protection (`fcn.14000fb50`)**
This function manages the memory space where the unpacked data is stored:
*   **VirtualProtect Usage:** The loop iterating through memory addresses to call `VirtualProtect` indicates that the binary is changing permissions on memory pages (e.g., moving from Read-Only to Execute). 
*   **Dynamic Loading:** This is common when a loader prepares "just-in-time" code for execution. It ensures that once the decompressor (from Step A) finishes its job, the resulting machine code or bytecode has the permissions necessary for the processor to execute it.

#### **C. Tcl/Tk & UI Construction (`fcn.140003db0`)**
This function manages the graphical interface:
*   **Win32 API Integration:** It calls `CreateWindowExW`, `GetClientRect`, and `SendMessageW` to create standard Windows elements like "STATIC" (labels), "EDIT" (text boxes), and "BUTTON".
*   **Tcl/Tk Backend:** These calls are typical of the Tcl/Tk toolkit's interaction with the Windows API. It confirms that if a GUI is shown, it uses standard Win32 controls, likely rendered via the Tk wrapper.

#### **D. Standard Loader Boilerplate (Entry Point)**
The entry point shows several common behaviors:
*   **Wait Loops:** Use of `Sleep(1000)` and time-checking logic can be used for simple delay tactics or to ensure system resources are initialized before starting the heavy lifting of the decompression engine.
*   **Error Handling:** The use of `SetUnhandledExceptionFilter` is a standard practice in professional software to prevent "crash dumps" from appearing to the user when the internal Python interpreter encounters an error.

---

### **3. Summary of Indicators and Behaviors**

| Feature | Observation | Security Significance |
| :--- | :--- | :--- |
| **Packaging** | PyInstaller OneFile Bundle | High-level obfuscation; hides the true logic of the script inside a bundled archive. |
| **Decompression** | `inflate()` / `inflateInit()` | Confirms that the core "payload" is compressed/hidden within the binary until execution. |
| **Memory Management** | `VirtualProtect` loops | Indicates the program is preparing memory for dynamic code execution (standard in Python, but also common in packers). |
| **GUI Layer** | Tcl/Tk / Win32 `CreateWindowExW` | Shows the tool has a visual component. While not inherently malicious, it's used to provide a user interface for whatever the script performs. |
| **Evasion Potential** | Hidden Windows (`ShowWindow(0)`) | The logic in chunk 3 indicated that some windows are intentionally hidden from the user while still functioning. |

---

### **4. Final Recommendation for Incident Response**

**Risk Assessment: High (Due to Obfuscation Capability)**
The binary is a "Black Box." Because it uses PyInstaller, standard static analysis of this `.exe` will only ever reveal the *loader* and not the *payload*. 

**Action Plan:**
1.  **Extract the Payload:** Do not rely on static analysis of the EXE alone. Use **`pyinstxtractor.py`** to unpack the binary. This will pull out the `.pyc` files and the Python library folder.
2.  **Decompile Pyc Files:** Once extracted, use a tool like **`pycdc`** or **`uncompyl6`** on the resulting `.pyc` files (specifically looking for `main.pyc` or similar). This is the only way to see the actual Python source code and identify C2 addresses, file paths, or encryption keys.
3.  **Memory Forensics:** If extraction fails, run the sample in a sandbox and perform a memory dump during execution. The "unpacked" bytecode will reside in memory after `fcn.140001490` finishes its routine.

**Conclusion:** This binary is a sophisticated container. To find out what it *actually does* to the system, you must break through the PyInstaller wrapper to reach the underlying Python script.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a PyInstaller "OneFile" bundle and `inflate` decompression logic hides the core payload within a compressed archive to avoid static detection. |
| **T1055** | Packer | The usage of `VirtualProtect` to transition memory pages from read-only to executable indicates a multi-stage loader preparing code for execution in memory. |
| **T1036** | Masquerading | The intentional hiding of windows via `ShowWindow(0)` allows the application to perform tasks while concealing its activity from the user. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*None identified.* (Note: While various Win32 API calls were mentioned, no specific malicious file paths or registry keys were present in the provided text.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.* (The strings provided appear to be fragmented assembly data/garbage bytes and do not contain recognizable MD5, SHA1, or SHA256 hashes.)

### **Other artifacts**
*   **Packer/Wrapper:** PyInstaller "OneFile" bundle (used as a wrapper to hide the actual Python payload).
*   **Decompression Routine:** `inflateInit()` and `inflate()` (indicates zlib/gzip decompression of internal assets/scripts).
*   **Memory Manipulation:** Frequent use of `VirtualProtect` (used to change memory permissions from read-only to executable for dynamic code execution).
*   **GUI Framework:** Tcl/Tk integration (detected via Win32 API calls like `CreateWindowExW`, `GetClientRect`, and `SendMessageW`).
*   **Evasion Behavior:** Use of `ShowWindow(0)` (logic intended to hide windows from the user during operation).
*   **Technical Signature:** Presence of internal data extraction logic in function `fcn.140001490`.

---
**Analyst Note:** The analysis indicates this is a **multi-stage loader**. The primary malicious logic is not contained within the initial executable but is packed and compressed inside the PyInstaller wrapper. To find network IOCs (IPs/Domains), you must extract the internal `.pyc` files using `pyinstxtractor.py`.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (for its role as a loader; lower for the ultimate payload)
4. **Key evidence**: 
    *   **Multi-stage Packaging:** The use of a PyInstaller "OneFile" bundle combined with `inflate` decompression routines indicates it is designed to hide and extract a secondary payload (Python bytecode) from static analysis.
    *   **Dynamic Memory Manipulation:** The repeated use of `VirtualProtect` to transition memory permissions to "Executable" is a hallmark behavior of loaders preparing hidden code for execution in memory.
    *   **Evasion Tactics:** The inclusion of `ShowWindow(0)` and the sophisticated wrapping layers indicate an intent to mask malicious activities from both the user and automated security tools during the unpacking process.
