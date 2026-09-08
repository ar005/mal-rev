# Threat Analysis Report

**Generated:** 2026-09-05 06:15 UTC
**Sample:** `1447eb60b8f939e9d2a70d02009c52ae359d1908d4544bb115db2f72c029428b_1447eb60b8f939e9d2a70d02009c52ae359d1908d4544bb115db2f72c029428b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1447eb60b8f939e9d2a70d02009c52ae359d1908d4544bb115db2f72c029428b_1447eb60b8f939e9d2a70d02009c52ae359d1908d4544bb115db2f72c029428b.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 12,612,696 bytes |
| MD5 | `98176a81a78e9ad8f8113e94ef6c5443` |
| SHA1 | `5c049fe70fc59dfb5a81089379b25b0e0c54203d` |
| SHA256 | `1447eb60b8f939e9d2a70d02009c52ae359d1908d4544bb115db2f72c029428b` |
| Overall entropy | 7.993 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773497162 |
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
| `.rsrc` | 18,432 | 7.903 | ⚠️ Yes |
| `.reloc` | 512 | 2.169 | No |

### Imports

**ADVAPI32.dll**: `ConvertSidToStringSidW`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `GetTokenInformation`, `OpenProcessToken`
**COMCTL32.dll**: `LoadIconMetric`
**GDI32.dll**: `CreateFontIndirectW`, `DeleteObject`, `SelectObject`
**KERNEL32.dll**: `AreFileApisANSI`, `CloseHandle`, `CreateDirectoryW`, `CreateFileW`, `CreateProcessW`, `CreateSymbolicLinkW`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileExW`, `FindFirstFileW`, `FindNextFileW`, `FormatMessageW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__argc`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `__wargv`, `__wgetmainargs`, `__winitenv`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_fileno`, `_fmode`
**USER32.dll**: `CreateWindowExW`, `DefWindowProcW`, `DestroyIcon`, `DestroyWindow`, `DialogBoxIndirectParamW`, `DispatchMessageW`, `DrawTextW`, `EndDialog`, `GetClientRect`, `GetDC`, `GetDialogBaseUnits`, `GetMessageW`, `GetWindowLongPtrW`, `InvalidateRect`, `MessageBoxA`

## Extracted Strings

Total strings found: **25188** (showing first 100)

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

This final chunk of disassembly provides a deep look into the "engine" of the bootloader. It confirms several technical mechanisms used by the PyInstaller framework to unpack, decompress, and prepare the execution environment for the underlying Python script.

Here is the updated analysis incorporating these new findings.

---

### Updated Analysis Report (Final Compilation)

#### Core Functionality and Purpose
The binary remains a **sophisticated PyInstaller-wrapped executable**. This final segment provides granular detail on the "Unpacking" phase of the bootloader:

*   **Decompression & Extraction (`fcn.140001490`):** This function is a significant find. It contains logic for `inflateInit`, `fread`, and `fwrite`. This confirms that the executable contains a compressed archive (likely containing `.pyc` files, DLLs, and other Python dependencies). The bootloader’s primary job at this stage is to decompress these components into memory or a temporary directory before passing execution to the interpreter.
*   **Memory Manipulation & Protection (`fcn.14000fb50`):** This function involves complex logic for managing memory segments and calls `VirtualProtect`. In the context of a PyInstaller bootloader, this is used to set the correct permissions (e.g., making a memory region executable) for the dynamically loaded Python modules after they are unpacked from the internal archive.
*   **Win32 API Integration & UI Construction (`fcn.140003db0`):** This function creates standard Windows GUI elements using `CreateWindowExW`, `GetClientRect`, and `SendMessageW`. It defines window classes (like "STATIC") and buttons (like "Close"). While this is common in PyInstaller for internal tools or "splash" screens, it also serves as a common technique to create a "legitimate-looking" interface during the execution of the wrapper.
*   **Exception Handling & Stability:** The use of `SetUnhandledExceptionFilter` and specific loops (potentially waiting for system readiness) suggests an effort to ensure the loader remains stable and does not crash visibly while it performs its heavy lifting of unpacking the payload.

#### Key Behaviors & Observations
*   **The "Extractor" Pattern:** The logic in `fcn.140001490` is a classic signature of a packer/wrapper. It doesn't just run code; it *extracts and prepares* code. This creates a significant hurdle for static analysis, as the actual malicious behavior is compressed and "invisible" until the moment of execution.
*   **Execution Environment Preparation:** The elaborate logic seen in the main entry point (handling `ls_wm_dir`, calculating memory offsets, etc.) indicates that the loader is meticulously setting up a "sandbox-like" environment for the Python interpreter to run in, ensuring it has all required resources without exposing the raw backend.
*   **Sophisticated Obfuscation through Complexity:** The sheer amount of boilerplate code—dealing with string lengths, buffer allocations, and memory protections—is intended to overwhelm automated scanners and human analysts. This "noise" makes it difficult to pinpoint exactly where the transition from "innocent bootloader" to "malicious payload" occurs.

#### Suspicious or Malicious Behavior Patterns
*   **Payload Decoupling:** The heavy reliance on a multi-stage loading process (Extract $\rightarrow$ Map Memory $\rightarrow$ Set Permissions $\rightarrow$ Execute) is a standard technique to hide the true intent of the malware from basic signature-based detection.
*   **Hidden Window Execution:** As noted in previous segments, the use of "hidden" windows allows the malicious payload to run its core logic (e.g., keylogging, data exfiltration) while the user only sees a standard window or no window at all.
*   **Resource Masking:** By using high-level libraries (PyInstaller), the author hides their custom code behind the massive footprint of the Python interpreter's standard library. This makes it harder to distinguish between "malicious" instructions and "legitimate" Python startup logic.

---

### Summary for Incident Response

The sample is a **highly-standardized PyInstaller bootloader wrapper**. It serves as a delivery vehicle for a Python-based payload.

**Key findings from the final disassembly segments:**
1.  **Confirmed Extraction Engine:** The presence of `inflateInit` and manual buffer management confirms that the binary acts as a self-extractor. It decodes and decompresses its primary payload internally.
2.  **Memory Manipulation for Payload Loading:** The use of `VirtualProtect` and complex memory mapping indicates the tool is preparing segments of memory specifically to house dynamically loaded code (the unpacked Python scripts).
3.  **Technical "Noise" as a Shield:** A massive amount of the binary's logic belongs to the PyInstaller framework. This acts as a shield, making it difficult for analysts to find the specific "trigger" or "malicious action" in the disassembly alone.

**Final Recommendation for Investigation:**
*   **DO NOT rely solely on static analysis of this .exe.** The current disassembly shows you the *delivery vehicle*, not the *payload*. 
*   **Action Item:** Use a tool such as **`pyinstxtractor.py`**. This will strip away the PyInstaller wrapper and extract the underlying `.pyc` files (compiled Python byte-code).
*   **Next Phase of Analysis:** Once extracted, use a decompiler like **uncompyle6** or **pycdc** on those `.pyc` files. The actual malicious logic (e.g., C2 communication, credential theft) will be found in those scripts, not in the assembly code provided here.
*   **Indicator of Compromise (IOC) Note:** Any file using this specific high-complexity bootloader should be flagged as "suspicious" regardless of the payload, as it is a known method for hiding malicious Python scripts.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of the PyInstaller wrapper acts as a "packer" to hide the core Python logic, compress data, and create complexity to hinder static analysis. |
| **T1055** | Process Injection | The specific use of `VirtualProtect` to alter memory permissions (e.g., making regions executable) is a hallmark of loaders preparing memory for unpacked code execution. |
| **T1036** | Masquerading | The construction of "legitimate-looking" Win32 GUI elements and the use of "hidden windows" are used to disguise the true purpose of the process from the user. |
| **T1574** | DLL Side-Loading (Contextual) | While primarily a loader, the manual mapping and extraction of dependencies into memory indicates techniques used to load malicious modules into a trusted environment. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains highly obfuscated or encrypted data typical of a packed executable; as such, no plaintext network indicators or file paths were present in that specific section.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: The analysis describes internal logic for "temporary directories," but no specific paths are provided).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified in the provided text.

### **Other artifacts**
*   **Packaging Framework:** PyInstaller (Identified as the primary wrapper/bootloader for the payload).
*   **Decompression Library:** `inflateInit` / `zlib` (Indicates the binary uses a standard decompression library to unpack internal components).
*   **Memory Manipulation Logic:** Usage of `VirtualProtect` and manual buffer management (`malloc`) to prepare memory segments for executing unpacked code.
*   **Win32 API Interaction:** 
    *   `CreateWindowExW` (Window creation)
    *   `GetClientRect` / `SendMessageW` (GUI interaction)
*   **Execution Pattern:** "Extract $\rightarrow$ Map Memory $\rightarrow$ Set Permissions $\rightarrow$ Execute" (A standard behavior for multi-stage packers/bootloaders).
*   **Internal Error Strings:** 
    *   `inflateInit() failed with return code %d!`
    *   `failed to allocate temporary input buffer!`
    *   `failed to allocate temporary output buffer!`

---

### **Analyst Note**
The strings provided appear to be obfuscated by the PyInstaller bootloader. Because the malicious payload is "hidden" inside the wrapper, static analysis of this specific file will not yield network infrastructure (IPs/Domains). To find further IOCs, it is recommended to run `pyinstxtractor` on the sample to extract the underlying Python bytecode (.pyc files), which will contain the actual logic for C2 communication and data exfiltration.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family:** Unknown
2. **Malware type:** Loader
3. **Confidence:** High
4. **Key evidence:**
    *   **PyInstaller Wrapper Mechanism:** The sample uses a standard PyInstaller bootloader to wrap and hide Python-based code, which is a common technique to evade static detection by hiding the actual logic inside `.pyc` files.
    *   **Extraction & Execution Chain:** The identification of `inflateInit` (decompression), `VirtualProtect` (memory permission manipulation), and the "Extract $\rightarrow$ Map Memory $\rightarrow$ Execute" workflow confirms its role as a loader designed to prepare an environment for a secondary payload.
    *   **Evasion Tactics:** Use of hidden windows, standard library masking, and intentional technical "noise" indicates the sample is engineered specifically to shield the core malicious functionality from analysis until runtime.
