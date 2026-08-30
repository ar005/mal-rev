# Threat Analysis Report

**Generated:** 2026-08-23 06:00 UTC
**Sample:** `113b3a45cdbf001ff8b80cb77874a423b87b7601838e041cda2e6f2b7091a28b_113b3a45cdbf001ff8b80cb77874a423b87b7601838e041cda2e6f2b7091a28b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `113b3a45cdbf001ff8b80cb77874a423b87b7601838e041cda2e6f2b7091a28b_113b3a45cdbf001ff8b80cb77874a423b87b7601838e041cda2e6f2b7091a28b.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 13,851,390 bytes |
| MD5 | `ff09e627105a6c72b6c4ead218b34f6a` |
| SHA1 | `9685dcbf2dc1e470b9a1a38d120b82caff1fb367` |
| SHA256 | `113b3a45cdbf001ff8b80cb77874a423b87b7601838e041cda2e6f2b7091a28b` |
| Overall entropy | 7.994 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779050304 |
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
| `.rsrc` | 18,944 | 7.916 | ⚠️ Yes |
| `.reloc` | 512 | 2.169 | No |

### Imports

**ADVAPI32.dll**: `ConvertSidToStringSidW`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `GetTokenInformation`, `OpenProcessToken`
**COMCTL32.dll**: `LoadIconMetric`
**GDI32.dll**: `CreateFontIndirectW`, `DeleteObject`, `SelectObject`
**KERNEL32.dll**: `AreFileApisANSI`, `CloseHandle`, `CreateDirectoryW`, `CreateFileW`, `CreateProcessW`, `CreateSymbolicLinkW`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `ExpandEnvironmentStringsW`, `FindClose`, `FindFirstFileExW`, `FindFirstFileW`, `FindNextFileW`, `FormatMessageW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__argc`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `__wargv`, `__wgetmainargs`, `__winitenv`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_fileno`, `_fmode`
**USER32.dll**: `CreateWindowExW`, `DefWindowProcW`, `DestroyIcon`, `DestroyWindow`, `DialogBoxIndirectParamW`, `DispatchMessageW`, `DrawTextW`, `EndDialog`, `GetClientRect`, `GetDC`, `GetDialogBaseUnits`, `GetMessageW`, `GetWindowLongPtrW`, `InvalidateRect`, `MessageBoxA`

## Extracted Strings

Total strings found: **27531** (showing first 100)

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

Based on the final chunk of disassembly provided, I have updated the analysis once more. This concluding segment provides significant insight into how the loader extracts its payload and introduces a very specific, suspicious behavioral component regarding potential user interaction or decoy functionality.

### Updated Analysis of Findings (Chunk 4)

#### 1. Payload Extraction & Decompression (`fcn.140001490`)
This function is a critical piece of the "Unpacking" puzzle.
*   **Decompression Engine:** The code explicitly calls `inflateInit` and includes logic that mirrors common decompression libraries (like zlib/deflate). It allocates memory, reads raw data from an internal source (`fread`), and then enters a loop to decompress it into a buffer.
*   **"On-the-Fly" Loading:** This confirms that the malicious Python code is not merely "stored" in the binary; it is **compressed and packed**. The loader extracts and decompresses the payload into memory (or a temporary buffer) only at the moment of execution.
*   **Significance:** This technique is used to bypass static signature-based detection. Because the actual malicious instructions are compressed, they remain "invisible" to many basic antivirus scanners until the loader actually runs and unpacks them.

#### 2. Entry Point & Bootstrapping Logic (Initial Block)
The code segment starting with `while(true)` and `_sym.imp.KERNEL32.dll_Sleep` represents the standard Windows environment initialization for a high-level runtime.
*   **Stability/Wait Loops:** The loop using `Sleep(1000)` is likely a check to ensure system resources or threads are ready before handing over control to the Python interpreter. 
*   **Exception Handling:** The use of `SetUnhandledExceptionFilter` ensures that if the script crashes, it does so quietly without popping up a standard Windows "Application has stopped working" dialog, further supporting the **Stealth Execution** profile identified in earlier chunks.

#### 3. Potential Interaction/Decoy GUI (`fcn.140003db0`)
This is perhaps the most significant discovery in this final chunk from an Incident Response perspective:
*   **Windows UI Construction:** This function constructs a standard Windows dialog box using `CreateWindowExW`. It creates several components:
    *   `STATIC`: Text labels.
    *   `EDIT`: A text input field (often used for passwords or user input).
    *   `BUTTON`: Specifically, a button labeled **"Close"**.
*   **Contextual Analysis:** Why would a Python-based backend process need a GUI? There are two primary possibilities in a malware context:
    1.  **Decoy/Social Engineering:** The loader might display this window only if something goes wrong (e.g., "Update Failed, Click Close to Restart"), designed to look like a legitimate system error message to keep the user from investigating the process.
    2.  **Interactive Component:** If the script is a credential harvester or an info-stealer, this code may be used to prompt the user for information in a way that looks "official."
*   **Significance:** The presence of an `EDIT` box and a `BUTTON` suggests the author prepared for potential interaction with the end-user.

---

### Final Updated Summary for Incident Response

#### **Confirmed Architecture:**
The binary is a highly professional, **PyInstaller-wrapped multi-stage loader**. It uses a robust "unpack and execute" model where the payload remains compressed until execution.

#### **New Intelligence Items (Cumulative):**
*   **Multilayered Stealth:** The combination of `_pyi_main_co` (hidden Python logic), `PyInstallerOnefileHiddenWindow` (no console), and a custom decompression routine (`inflateInit`) shows an intent to hide both the *logic* and the *presence* of the malware.
*   **Active Decompression:** The loader actively decompresses its internal resources before execution. This means memory forensics is superior to disk-based analysis for this specific sample.
*   **Potential Interaction Point:** The presence of a `CreateWindowExW` call with an `EDIT` field suggests that while the primary operation is "hidden," there is functionality built-in to interact with or deceive the user via a GUI if necessary.

#### **Risk Assessment Update:**
The risk remains **High/Critical**. This final chunk confirms that the malware author has invested effort into making the delivery mechanism robust and potentially interactive. The presence of an "Edit" field in the underlying code suggests potential for credential theft or sophisticated social engineering tactics.

#### **Final Recommendations for IR:**
1.  **Advanced Memory Forensics (High Priority):** Because the loader uses a decompression routine (`fcn.140001490`) to unpack its payload, standard disk scans are less effective here. **Perform memory dumps** of any process associated with this file. The unpacked `.pyc` or Python bytecode will be visible in memory and can be extracted for full analysis.
2.  **Behavioral Blocklisting:** Monitor for processes that:
    *   Attempt to use `inflateInit` or similar decompression routines immediately followed by execution of a high-level language interpreter (Python).
    *   Create "Hidden Windows" while simultaneously performing network activity.
3.  **Indicator Search:** Extract the strings and byte sequences related to the `fcn.140001490` (the decompressor) and use them as signatures for **YARA rules**. This can identify other variants of the same loader even if the underlying Python script changes.
4.  **Network Isolation:** Given the "Hidden Window" and "Decompression" architecture, any instance of this process should be strictly isolated from the network to prevent data exfiltration or Command & Control (C2) communication.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Packed Executables | The use of a decompression engine (`inflateInit`) to unpack a hidden Python payload into memory at runtime is a classic method to bypass static signature-based detection. |
| **T1566** | Social Engineering | The construction of a GUI with `EDIT` and `BUTTON` components indicates the potential for deceptive user prompts or "dummy" error messages to mask malicious activity. |
| **T1027** | Obfuscated Files or Information | The use of `PyInstallerOnefileHiddenWindow` combined with custom decompression ensures that both the logic and presence of the script remain hidden from standard analysis tools. |
| **T1036** | Masquerading | The creation of a "standard Windows dialog box" suggests an attempt to blend in with legitimate system messages or software prompts to deceive the user. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contained a high volume of obfuscated data and standard library artifacts which were excluded as per your instructions to skip false positives.

### **IP addresses / URLs / Domains**
*   None identified in the provided text.

### **File paths / Registry keys**
*   None identified (The report mentions "temporary buffers," but no specific file paths or registry keys are hardcoded in the provided strings).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified (No MD5, SHA1, or SHA256 hashes were present in the string dump).

### **Other artifacts (Behavioral IOCs & Technical Artifacts)**
These represent functional indicators and signatures that can be used for detection of this specific loader family:

*   **PyInstaller Artifacts:** 
    *   `_pyi_main_co`: Used as a signature for PyInstaller-wrapped scripts.
    *   `PyInstallerOnefileHiddenWindow`: A specific flag/function indicating the intentional hiding of the console window during execution.
*   **Decompression Indicators:**
    *   `inflateInit`: The use of this specific function call (associated with zlib/deflate) is a primary indicator for the unpacking stage of this malware.
    *   **Error Strings:** 
        *   `Failed to extract %s: inflateInit() failed with return code %d!`
        *   `Failed to extract %s: failed to allocate temporary input buffer!`
        *   `Failed to extract %s: failed to allocate temporary output buffer!`
    *   *Analysis:* These strings can be used as YARA signatures to identify the specific decompression routine used by this loader.
*   **GUI/Interaction Artifacts:**
    *   `CreateWindowExW`: Used to construct a GUI containing `STATIC`, `EDIT`, and `BUTTON` (labeled "Close"). 
    *   **Behavioral Signature:** The presence of an `EDIT` field within a hidden or background process is a high-confidence indicator of potential credential harvesting.
*   **Function Offsets (Memory Forensics):**
    *   `fcn.140001490`: Identified as the core decompression/unpacking logic.
    *   `fcn.140003db0`: Identified as the GUI construction/potential decoy interaction point.

---
**Analyst Note:** The primary value of this sample for defense lies in its **behavioral indicators**. Because the payload is compressed and loaded "on-the-fly," traditional file-based signatures will likely fail against variants of this loader. Detection should focus on the `inflateInit` routine and the usage of `PyInstallerOnefileHiddenWindow`.

---

## Malware Family Classification

1. **Malware family:** custom
2. **Malware type:** loader (with potential infostealer functionality)
3. **Confidence:** High
4. **Key evidence:**
    *   **Multi-stage Loader Architecture:** The sample is a professional PyInstaller-wrapped binary that uses a "on-the-fly" decompression routine (`inflateInit`) to unpack and execute its payload in memory, specifically designed to bypass static signature detection.
    *   **Stealth & Evasion Tactics:** It employs `PyInstallerOnefileHiddenWindow` to hide the console during execution and utilizes custom exception handling to ensure failures do not alert the user with standard Windows error messages.
    *   **Interactive Component for Data Theft:** The inclusion of a GUI constructed via `CreateWindowExW` containing an `EDIT` field strongly suggests functionality geared toward credential harvesting or sophisticated social engineering.
