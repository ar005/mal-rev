# Threat Analysis Report

**Generated:** 2026-08-15 08:45 UTC
**Sample:** `0ede0addd8755f41164a6ca36c350440c567a51843d57443185c61120fdf14ad_0ede0addd8755f41164a6ca36c350440c567a51843d57443185c61120fdf14ad.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ede0addd8755f41164a6ca36c350440c567a51843d57443185c61120fdf14ad_0ede0addd8755f41164a6ca36c350440c567a51843d57443185c61120fdf14ad.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 13,866,891 bytes |
| MD5 | `2388a567dfabcac2361109dc3f1126f4` |
| SHA1 | `8e463abe03e1d965d34f6b04b7640b04fb2debef` |
| SHA256 | `0ede0addd8755f41164a6ca36c350440c567a51843d57443185c61120fdf14ad` |
| Overall entropy | 7.994 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779072207 |
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
| `.rsrc` | 19,456 | 7.898 | ⚠️ Yes |
| `.reloc` | 512 | 2.169 | No |

### Imports

**ADVAPI32.dll**: `ConvertSidToStringSidW`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `GetTokenInformation`, `OpenProcessToken`
**COMCTL32.dll**: `LoadIconMetric`
**GDI32.dll**: `CreateFontIndirectW`, `DeleteObject`, `SelectObject`
**KERNEL32.dll**: `AreFileApisANSI`, `CloseHandle`, `CreateDirectoryW`, `CreateFileW`, `CreateProcessW`, `CreateSymbolicLinkW`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileExW`, `FindFirstFileW`, `FindNextFileW`, `FormatMessageW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__argc`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `__wargv`, `__wgetmainargs`, `__winitenv`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_fileno`, `_fmode`
**USER32.dll**: `CreateWindowExW`, `DefWindowProcW`, `DestroyIcon`, `DestroyWindow`, `DialogBoxIndirectParamW`, `DispatchMessageW`, `DrawTextW`, `EndDialog`, `GetClientRect`, `GetDC`, `GetDialogBaseUnits`, `GetMessageW`, `GetWindowLongPtrW`, `InvalidateRect`, `MessageBoxA`

## Extracted Strings

Total strings found: **27603** (showing first 100)

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

The analysis has been updated with findings from Chunk 4. This final segment confirms several critical behaviors regarding how the binary handles its internal payload and manages system resources during execution.

### Updated Analysis Report (Cumulative)

#### Core Functionality and Purpose
The binary is confirmed as a **multi-stage PyInstaller wrapper**. This chunk provides concrete evidence of the "loader" phase, where the executable prepares the environment, decompresses the Python bytecode, and modifies memory permissions to execute the hidden payload.

#### Behavior Details
*   **Extraction & Decompression Engine (`fcn.140001490`):** 
    *   This function is a significant find. It utilizes `inflateInit`, `fread`, and `fwrite` (common in zlib/deflate implementations).
    *   **Purpose:** This confirms the "OneFile" nature of the PyInstaller bundle. The binary isn't just running a script; it is actively extracting and decompressing internal data (the Python interpreter components and scripts) into memory or temporary buffers before execution.
*   **Memory Management & Permission Manipulation (`fcn.14000fb50`):** 
    *   This function calls `VirtualProtect`.
    *   **Purpose:** In the context of a loader, this is used to change the protection of memory pages (e.g., from "Read-Only" or "No-Execute" to "Execute") after the payload has been unpacked into memory. This is a standard but high-priority indicator for security tools as it is often used by packers to facilitate the execution of injected code.
*   **Argument Parsing & Environment Setup:** 
    *   The inclusion of `_sym.msvcrt.dll___wgetmainargs` indicates that the loader is designed to process command-line arguments correctly. This allows the underlying Python script to receive inputs (such as target IPs, configuration paths, or filenames) directly from a calling script or a shortcut.
*   **GUI Component Construction (`fcn.140003db0`):**
    *   This function creates standard Windows controls: `STATIC`, `EDIT`, and `BUTTON`. 
    *   **Analysis:** While the "Hidden Window" logic (from Chunk 3) suggests a background operation, the existence of GUI code can serve two purposes: it may be part of a standard library used by the Python script (e.g., Tkinter or PySide), or it could be a small, decoy interaction window intended to distract the user while the primary malicious actions occur in the background.

#### Suspicious or Malicious Behaviors (Updated)
*   **Automated Unpacking Logic:** The transition from `inflateInit` to `VirtualProtect` confirms a sophisticated "unpack-then-execute" workflow. This makes it harder for static scanners to find the actual malicious logic, as the code only exists in its "true" form in memory after the loader performs these actions.
*   **Execution Stealth:** The combination of **Hidden Windows**, **Unhandled Exception Filtering** (`SetUnhandledExceptionFilter`), and **Memory Protection Manipulation** suggests a highly professional implementation designed to ensure the malware remains stable and invisible while transitioning from the wrapper to the payload.
*   **Argument-Driven Execution:** Because it handles `wgetmainargs`, the malware is likely modular; the attacker can pass different parameters to change its behavior without modifying the binary itself.

#### Notable Techniques/Patterns
*   **zlib/Decompression Utility:** The use of standard decompression libraries makes the loader look like a "legitimate" packer, which helps it blend in with thousands of other legitimate PyInstaller-based tools.
*   **Persistence of Method:** The logic used to check for `.MZ` headers and process execution types suggests that the code is designed to be robust—ensuring that even if integrated into different environments, the unpacking routine will succeed.

---

### Summary for Incident Response

The analysis of all four chunks confirms that this file is a **sophisticated, multi-stage loader** wrapped in the PyInstaller framework. 

**Technical Conclusion:**
The binary acts as a "shell" that performs three primary functions:
1.  **Environment Masking:** Using hidden windows and standard library signatures to hide from the user and basic heuristics.
2.  **Payload Extraction:** Actively decompressing (zlib) and unpacking a hidden payload into memory.
3.  **Memory Modification:** Using `VirtualProtect` to prepare that unpacked code for execution.

**Updated Risk Assessment:**
*   **Complexity Level:** High. The use of standard Python tooling as a "shield" is an effective way to bypass basic signature-based detection.
*   **Evasion Strategy:** The malware utilizes **dynamic unpacking**. This means the malicious payload (the part that steals data or provides backdoors) might not even exist in a readable state until the EXE is actually running.
*   **Behavioral Trigger:** Look for the process attempting to modify its own memory permissions (`VirtualProtect`) or suddenly spawning new processes/threads after an initial period of "quiet" decompression.

**Refined Action Plan:**
1.  **Dynamic Analysis (Memory Forensics):** Because the code is unpacked into memory, perform a memory dump *after* execution has begun but before it finishes its routine. This may capture the decrypted Python scripts or C-extensions.
2.  **Extraction via Tools:** Use `pyinstxtractor` on the EXE immediately. This will bypass the "unpacking" logic of Chunk 4 and give you direct access to the `.pyc` files, which contain the actual malicious logic.
3.  **Network Monitoring:** Monitor for traffic starting *after* the decompression loop is completed; this is the point where the loader finishes its job and the payload begins its primary function (C2 communication, exfiltration, etc.).

--- 
*End of Final Analysis.*

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Packing | The use of `inflateInit` and zlib/deflate routines to decompress internal Python bytecode into memory is a classic indicator of packing to hide the primary payload. |
| **T1610** | Reflective Code Loading | The use of `VirtualProtect` to change memory permissions from "Read-Only" or "No-Execute" to "Execute" indicates that code is being prepared for execution directly in memory. |
| **T1027** | Obfuscated Files or Information | The multi-stage PyInstaller wrapper and the use of standard library signatures are used to mask the true functionality and identity of the underlying malicious scripts. |
| **T1059** | Command and Scripting Interpreter | The inclusion of `_sym.msvcrt.dll___wgetmainargs` confirms the loader is designed to pass command-line arguments (such as IPs or paths) directly to the inner Python script. |
| **T1203** | Exploitation for Defense Evasion | The use of "Hidden Windows" and `SetUnhandledExceptionFilter` are specific tactics used to evade user notice and standard error-handling telemetry during execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: The "Strings" section contains largely obfuscated data, standard library error messages, and junk padding. No high-fidelity network indicators (IPs/URLs) were present in that specific section.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (The analysis mentions "temporary buffers," but no specific file paths were disclosed).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Memory Manipulation:** `VirtualProtect` (Used to transition memory pages from Read-Only/No-Execute to Execute for unpacked code).
*   **Decompression Logic:** `inflateInit`, `fread`, and `fwrite` (Indicates a zlib/deflate implementation used for unpacking the internal Python payload).
*   **Application Framework:** PyInstaller (Identified as a multi-stage PyInstaller wrapper).
*   **Environment Context:** `msvcrt.dll___wgetmainargs` (Indicates standard MSVCRT library usage for command-line argument parsing).
*   **Behavioral Pattern:** "unpack-then-execute" workflow (Detected via the transition from decompression routines to memory protection changes).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Unpacking Workflow:** The transition from `inflateInit` (decompression) to `VirtualProtect` (changing memory permissions to "Execute") confirms a classic "unpack-then-execute" routine used by loaders to hide payloads in memory.
*   **PyInstaller Wrapper & Obfuscation:** The use of a PyInstaller wrapper combined with hidden windows and custom exception filtering demonstrates an intentional effort to mask the underlying Python scripts from both the user and automated security tools.
*   **Modular Design:** The integration of `_sym.msvcrt.dll___wgetmainargs` indicates the loader is designed to accept command-line arguments, allowing a single binary to be used to deploy different payloads or configurations.
