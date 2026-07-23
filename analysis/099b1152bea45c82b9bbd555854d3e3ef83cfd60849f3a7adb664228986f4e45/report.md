# Threat Analysis Report

**Generated:** 2026-07-22 16:21 UTC
**Sample:** `099b1152bea45c82b9bbd555854d3e3ef83cfd60849f3a7adb664228986f4e45_099b1152bea45c82b9bbd555854d3e3ef83cfd60849f3a7adb664228986f4e45.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `099b1152bea45c82b9bbd555854d3e3ef83cfd60849f3a7adb664228986f4e45_099b1152bea45c82b9bbd555854d3e3ef83cfd60849f3a7adb664228986f4e45.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 23,525,376 bytes |
| MD5 | `9edcd207c071410e8361f1bddd250bc4` |
| SHA1 | `521cd3cf06acaed9d433da2e37e08069aab1c336` |
| SHA256 | `099b1152bea45c82b9bbd555854d3e3ef83cfd60849f3a7adb664228986f4e45` |
| Overall entropy | 6.057 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1722942349 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 23,058,944 | 5.997 | No |
| `.data` | 359,936 | 4.156 | No |
| `.rdata` | 5,120 | 5.007 | No |
| `.pdata` | 2,048 | 4.725 | No |
| `.xdata` | 1,536 | 3.674 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 2,048 | 4.007 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 2,720 | 2.566 | No |
| `.reloc` | 91,136 | 5.437 | No |

### Imports

**KERNEL32.dll**: `DeleteCriticalSection`, `EnterCriticalSection`, `FreeLibrary`, `GetLastError`, `GetModuleHandleA`, `GetProcAddress`, `GetStartupInfoA`, `GetTickCount`, `InitializeCriticalSection`, `IsDBCSLeadByte`, `LeaveCriticalSection`, `LoadLibraryA`, `MultiByteToWideChar`, `SetUnhandledExceptionFilter`, `Sleep`
**msvcrt.dll**: `__C_specific_handler`, `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_commode`, `_fmode`, `_initterm`, `abort`, `atexit`, `calloc`

## Extracted Strings

Total strings found: **100465** (showing first 100)

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
	PSQY[XQYH
AVWVSH
X[^_A^
	PQYXH
?ASA[M
PSQY[XM
AWA_PS[X
ARASA[AZH
PSQY[X
PSQY[XATA\
ATA\ATA\
PSQY[XH
PSQY[XH
ARASA[AZVV^^ATM
A\QRZYH
W_S[PH
XAVA^H
VW_^RH
AUA]AUA]
A$DE3A
HM9OP3I
tRHL$D
 D;tpH
AfE;jM9OP
L$DEXr
tRHDE3
tRt_fD
 D_fD;
L$DtdA
tRM9OPH
fE;t_fD
;t$XDE3
t3IDE3
t$XrDE3
t_fD5k
Ht_fDt
E$DE3pH
t_ftRH
t?At?A
H_fD;H
H D;tF
_fD;t$XrH
M9O;t$XR
t3It_fD
AD;t$H
t?L$DE
AM9OPI
9OPtDE3
tdAtRH
tdAD;t$
L$DEtdA
;t$XtRH
 D;t;j
tRHL$D
$DE3L$D
]_fD;D$H
C_fD;H
D;t$Pt
]D;t$ 
D$t$XrA
t?9OPtH
t9OPtt3I
5t_fDI
t$DE3$D
D;t$pH
 D;?Xr
t_fD D;t
D$HtdA
tR9OPt
t_fDt_fD5k
LD;t$L$D
L$DE3$Xr
D$H$DE3
tR9OPt
M9OPD$H
L$D9OPtfD;
L$DtdA
t D;tf;
tRM9OPA
!kD;t$5k
!M9OPt$XrE
t_fDdA
D$L$DE
HfE;j3
9OPtt?A
D$HDE3
t$Xr?A
?Xt$Xr
Lt$XrH
t3I?Xr
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1415fe920` | `0x1415fe920` | 23057587 | ✓ |
| `fcn.1415fd620` | `0x1415fd620` | 23057390 | ✓ |
| `fcn.1415fd520` | `0x1415fd520` | 23048942 | ✓ |
| `fcn.14106723d` | `0x14106723d` | 17751874 | ✓ |
| `fcn.14037adf6` | `0x14037adf6` | 17703488 | ✓ |
| `fcn.1400d49f5` | `0x1400d49f5` | 17703275 | ✓ |
| `fcn.14053b380` | `0x14053b380` | 17703260 | ✓ |
| `fcn.14049e3d1` | `0x14049e3d1` | 17703204 | ✓ |
| `fcn.1402ae244` | `0x1402ae244` | 17703195 | ✓ |
| `fcn.14040fccf` | `0x14040fccf` | 17703188 | ✓ |
| `fcn.140250c89` | `0x140250c89` | 16375338 | ✓ |
| `fcn.14027a6a4` | `0x14027a6a4` | 16375198 | ✓ |
| `int.1402ef870` | `0x1402ef870` | 16375039 | ✓ |
| `fcn.1405dd852` | `0x1405dd852` | 16375001 | ✓ |
| `fcn.1403356e0` | `0x1403356e0` | 16374979 | ✓ |
| `fcn.14037d9cb` | `0x14037d9cb` | 16374942 | ✓ |
| `fcn.1403b8036` | `0x1403b8036` | 15523456 | ✓ |
| `fcn.14032a0f0` | `0x14032a0f0` | 15523259 | ✓ |
| `fcn.14037438c` | `0x14037438c` | 15523220 | ✓ |
| `fcn.1401c742c` | `0x1401c742c` | 15523193 | ✓ |
| `fcn.1402e7184` | `0x1402e7184` | 15511229 | ✓ |
| `int.1401c82fc` | `0x1401c82fc` | 15510793 | ✓ |
| `fcn.1406a8285` | `0x1406a8285` | 15510423 | ✓ |
| `fcn.1401160c9` | `0x1401160c9` | 15510351 | ✓ |
| `fcn.140740683` | `0x140740683` | 15270686 | ✓ |
| `fcn.14117cb8a` | `0x14117cb8a` | 13597057 | ✓ |
| `fcn.140cd8175` | `0x140cd8175` | 12492050 | ✓ |
| `fcn.14125bfdd` | `0x14125bfdd` | 12491878 | ✓ |
| `fcn.14129a42a` | `0x14129a42a` | 12491824 | ✓ |
| `fcn.140ec22fc` | `0x140ec22fc` | 12491766 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400d49f5.c`](code/fcn.1400d49f5.c)
- [`code/fcn.1401160c9.c`](code/fcn.1401160c9.c)
- [`code/fcn.1401c742c.c`](code/fcn.1401c742c.c)
- [`code/fcn.140250c89.c`](code/fcn.140250c89.c)
- [`code/fcn.14027a6a4.c`](code/fcn.14027a6a4.c)
- [`code/fcn.1402ae244.c`](code/fcn.1402ae244.c)
- [`code/fcn.1402e7184.c`](code/fcn.1402e7184.c)
- [`code/fcn.14032a0f0.c`](code/fcn.14032a0f0.c)
- [`code/fcn.1403356e0.c`](code/fcn.1403356e0.c)
- [`code/fcn.14037438c.c`](code/fcn.14037438c.c)
- [`code/fcn.14037adf6.c`](code/fcn.14037adf6.c)
- [`code/fcn.14037d9cb.c`](code/fcn.14037d9cb.c)
- [`code/fcn.1403b8036.c`](code/fcn.1403b8036.c)
- [`code/fcn.14040fccf.c`](code/fcn.14040fccf.c)
- [`code/fcn.14049e3d1.c`](code/fcn.14049e3d1.c)
- [`code/fcn.14053b380.c`](code/fcn.14053b380.c)
- [`code/fcn.1405dd852.c`](code/fcn.1405dd852.c)
- [`code/fcn.1406a8285.c`](code/fcn.1406a8285.c)
- [`code/fcn.140740683.c`](code/fcn.140740683.c)
- [`code/fcn.140cd8175.c`](code/fcn.140cd8175.c)
- [`code/fcn.140ec22fc.c`](code/fcn.140ec22fc.c)
- [`code/fcn.14106723d.c`](code/fcn.14106723d.c)
- [`code/fcn.14117cb8a.c`](code/fcn.14117cb8a.c)
- [`code/fcn.14125bfdd.c`](code/fcn.14125bfdd.c)
- [`code/fcn.14129a42a.c`](code/fcn.14129a42a.c)
- [`code/fcn.1415fd520.c`](code/fcn.1415fd520.c)
- [`code/fcn.1415fd620.c`](code/fcn.1415fd620.c)
- [`code/fcn.1415fe920.c`](code/fcn.1415fe920.c)
- [`code/int.1401c82fc.c`](code/int.1401c82fc.c)
- [`code/int.1402ef870.c`](code/int.1402ef870.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C code, here is a professional analysis of the binary sample:

### Core Functionality and Purpose
The binary appears to be a **malicious loader or an automated spam/trojan component**. It utilizes heavy obfuscation techniques to hide its actual execution path while preparing to interact with system-level components—specifically those related to email services.

### Suspicious and Malicious Behaviors
*   **Potential Email Manipulation (Spyware/Trojans):** 
    The function `fcn.1415fd520` explicitly calls `LoadLibraryA("mapi32.dll")`. The MAPI (Messaging Application Programming Interface) is used by applications like Microsoft Outlook to interact with email accounts. Its presence in a sample typically indicates functionality for sending spam, exfiltrating emails, or interacting with the user's mail system.
*   **Anti-Analysis & Anti-Debugging:** 
    The code makes frequent calls to `GetTickCount` (multiple times across different functions). This is a common technique used to detect if a debugger is being attached or if the code is running in a sandbox, as debuggers and emulators often cause measurable delays in execution timing.
*   **Advanced Obfuscation:** 
    A significant portion of the disassembly is littered with "bad instruction" warnings, "too many branches," and complex pointer arithmetic (e.g., `CONCAT` macros). This indicates that the code has been processed by a **packer or protector** (such as VMProtect or Themida) or utilizes a custom "virtual machine" (VM)-based obfuscation technique to hide its true logic from automated analysis tools.

### Notable Techniques and Patterns
*   **Control-Flow Obfuscation:** Many functions contain complex, non-linear jumps and junk code. This is designed to frustrate decompilers and human analysts by making the logical flow of the program difficult to follow.
*   **Dynamic API Resolution/Loading:** The use of `LoadLibraryA` for specific libraries like `mapi32.dll` suggests the malware tries to keep its imports table "clean" to evade simple static analysis.
*   **Junk Code Insertion:** The recurring "bad instruction" warnings and overlapping instructions suggest that the binary contains a high volume of code intended solely to confuse scanners and automated tools, which is characteristic of sophisticated modern malware families.

### Summary Recommendation
The presence of **MAPI interaction** combined with **high-level protection/obfuscation** suggests this is a malicious sample, likely a Trojan designed for mail-related activities (such as spamming or credential theft) that employs advanced evasion techniques to bypass security software and manual analysis.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Evasion | The use of `GetTickCount` is a classic technique to detect timing discrepancies caused by the presence of debuggers or automated analysis environments. |
| **T1027** | Obfuscated Files or Information | The integration of packers (e.g., VMProtect), junk code insertion, and complex pointer arithmetic are used to hinder both manual and automated reverse engineering. |
| **T1048** | Exfiltration | The interaction with `mapi32.dll` indicates the capability to exfiltrate data or interact with email services for spamming or information theft. |

### Analyst Notes:
*   **Dynamic API Resolution:** While the use of `LoadLibraryA` is a common method to hide imports from the IAT, it falls under the broader umbrella of **T1027 (Obfuscated Files or Information)** as it conceals the program's actual functionality from static analysis.
*   **Control-Flow Obfuscation:** The "non-linear jumps" and "junk code" mentioned are specific indicators of high-effort evasion intended to frustrate human analysts, also falling under **T1027**.
*   **Contextual Intelligence:** The combination of **T1497** (Evasion) and **T1048** (Exfiltration) strongly suggests a sophisticated threat actor or a highly automated malware suite designed for data theft via mail-based infrastructure.

---

## Indicators of Compromise

Based on the provided string dump and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "EXTRACTED STRINGS" section contains heavily obfuscated or encoded data typical of packed binaries; no plain-text IP addresses, URLs, or file paths were identifiable within that specific block.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **mapi32.dll** (Note: While a standard Windows DLL, its inclusion in the behavioral report identifies it as the primary target for mail-related functionality.)

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Anti-Analysis Technique:** Use of `GetTickCount` for timing checks to detect debuggers or sandboxes.
*   **Evasion Technique:** Evidence of heavy packing/protection (likely VMProtect or Themida) and "junk code" insertion.
*   **Malicious Capability:** Integration with the MAPI (Messaging Application Programming Interface) to interact with email clients (e.g., Outlook).
*   **Obfuscation Style:** Control-flow obfuscation, dynamic API resolution, and non-linear jump instructions.

---

## Malware Family Classification

1. **Malware family**: custom (or potentially an obfuscated component of a larger campaign like Emotet/Qakbot)
2. **Malware type**: loader / trojan
3. **Confidence**: Medium (High for "type", but lack of specific C2 infrastructure or unique strings prevents a definitive "family" identification)
4. **Key evidence**: 
    *   **MAPI Integration:** The explicit use of `mapi32.dll` is a strong indicator of mail-related malicious activity, such as automated spamming, credential harvesting from email clients (Outlook), or using the mail system for exfiltration.
    *   **Advanced Anti-Analysis:** The frequent calls to `GetTickCount` combined with evidence of "VMProtect" style packing and junk code insertion indicate a high-effort attempt to bypass sandboxes and manual reverse engineering.
    *   **Loader Behavior:** The use of dynamic API resolution (`LoadLibraryA`) and heavy control-flow obfuscation suggests the primary role of this specific binary is to act as a protective "wrapper" or loader to deliver further capabilities while hiding its true footprint from static scanners.
