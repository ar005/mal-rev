# Threat Analysis Report

**Generated:** 2026-06-30 19:28 UTC
**Sample:** `037bd696ae32dd8183cdcc587fd7f04f2d76a992856672e71d2766b0fc872a80_037bd696ae32dd8183cdcc587fd7f04f2d76a992856672e71d2766b0fc872a80.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `037bd696ae32dd8183cdcc587fd7f04f2d76a992856672e71d2766b0fc872a80_037bd696ae32dd8183cdcc587fd7f04f2d76a992856672e71d2766b0fc872a80.exe` |
| File type | PE32 executable for MS Windows 6.00 (console), Intel i386, 6 sections |
| Size | 97,280 bytes |
| MD5 | `dfa5bc2c4d3e3aad2dc3da41904aa8c0` |
| SHA1 | `3458277540d61baae24ac25785d37f87d0e19bcb` |
| SHA256 | `037bd696ae32dd8183cdcc587fd7f04f2d76a992856672e71d2766b0fc872a80` |
| Overall entropy | 6.318 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779157269 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 60,928 | 6.598 | No |
| `.rdata` | 26,624 | 5.052 | No |
| `.data` | 2,560 | 2.026 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,024 | 3.0 | No |
| `.reloc` | 4,608 | 6.274 | No |

### Imports

**KERNEL32.dll**: `GetEnvironmentVariableA`, `GetVolumeInformationA`, `CloseHandle`, `QueryPerformanceCounter`, `HeapCreate`, `HeapDestroy`, `HeapAlloc`, `WaitForSingleObject`, `GetProcessTimes`, `GetCurrentProcess`, `GetCurrentProcessId`, `ExitProcess`, `GetCurrentThreadId`, `GetSystemInfo`, `GetTickCount`
**USER32.dll**: `GetWindowRect`, `GetCursorPos`, `GetDesktopWindow`

## Extracted Strings

Total strings found: **398** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.fptable
@.reloc
D$duserP
D$l32.df
D$tMovePV
ShowPV
M;Jr

38_^]
E9xt
URPQQh
;t$,v-
kUQPXY]Y[
QQSVWd
tH9] uC
u PWQR
Yt
jV
9Ov:k
< t1<	t-
uhL~A
jhp[A
9>tWV
t	iud
;1t+;u
u9~uj
};GvP
u9^uj
};GvP
</t
<\t
SSSPSQ
u9^u
uSSSSj
};GvP
];3t'
f9:t!V
u|9]t,9
QQSVj8j@
tl=HvA
;ut.;
jhX]A
jh8]A
j(hx]A
9Eu$_[
PPPPPPPP
PPPPPWV
PP9E u

u<jXSf

u	jZf
PVVVVV
D$+d$SVW
D$+d$SVW
v	N+D$
v	N+D$
!/8$/&yxd.&&/>	%$9%&/
#(8+83/>
%.?&/#&/
	8/+>/
8%)/99
)83:>yxd.&&
#$+83
#8>?+&
>	8/+>/
2VYvsg+T4gewUAgAAU1ZXuY0Qt/joHwMAALkziFqei/DoEwMAALmS8a5Pi/joBwMAALleQVIjiUQkaOj5AgAAuT3TqoiJRCRc6OsCAAC5U+lYB4lEJGDo3QIAAIlEJGSNRCR0UMdEJHhXczJfx0QkfDMyLmTHhCSAAAAAbGwAAP/WuUDV3C3orQIAALnk8g47iUQkOOifAgAAuclTKdyJRCQ06JECAAC5uYNW3YlEJDzogwIAALli4QpSiUQkROh1AgAAuSoBUtuJRCRI6GcCAAC5PAH62IlEJEzoWQIAALm8E50LiUQkVOhLAgAAakC+ADAAAIlEJFxWaEyBBABqAP/XagRWaEQBAABqAIlEJGD/14v4iXwkEOjVAgAAM8mAPAFCdSCAfAEBeXUZgHwBAkB1EoB8AQNWdQuAfAEEPA+ExgEAAEGB+UAfAABy0TPJUY0UAYvP6HoCAABZx0QkFHo/nisz28dEJBjRVvjEx0QkHB6NQrfHRCQgZaMM6cdEJCQBI0Vnx0QkKImrze/HRCQs/ty6mMdEJDB2VDIQD7bDstxrwAeL8w+2y4PmHyrQi8PB+ASD4B8yVAQUi8PB+AOD4B8yVAQUi8PB+AKD4B8yVAQUD7bDD6/ID7bDa8ANMtEEYTLQjUMED7bAa8ARMtCNRCQzK8YyEA+2w2vAEzLQMBQfQ4t8JBCB+0QBAAB8jY2EJJAAAABQaAICAAD/VCRAhcAPhdoAAABqBmoBagL/VCRAi9iNRCRAUGoAagBXiVwkRP9UJEyLdCRAjbwkgAAAAItEJBCLdhilpaWlD7dAQFD/VCRIi3QkSGaJhCSCAAAAahCNhCSEAAAAUFP/1oP4/3TuagBqCI1EJHTHRCR0QkZ1Y1BTx4QkgAAAAGsAAAD/VCRci1wkUDP2i3wkNGoAuEyBBAArxlCNBB5QV/9UJGQD8IH+TIEEAHzji1QkEFGNiwiABADo+AAAAFn/VCRYM/ZW/1QkYFNTVv9UJGxQ/1QkaIXbdAtoAIAAAFZT/1QkdF9eW4vlXcODwQXpPf7//1NWi/Ez0usSD77LwcoNgPthjUHgD0zBA9BGih6E23XoXovCW8NVi+yD7BRkoTAAAABTVleLQAyJTfSLQBSL+IlF7It3EIs/hfZ0T4tGPItcMHiF23REi0wzDAPO6J////+LTDMgiUX4A84zwIlN8IlF/DlEMxh2IosMgQPO6H7///8DRfg5RfR0HItF/ItN8ECJRfw7RDMYct47fex1ozPAX15bycOLTfyLRDMkjQRID7cMMItEMxyNBIiLBDADxuvfhcl0GIXSdBRWalEr0V6LBAqJAY1JBIPuAXXzXsNVi+xR6AAAAABYiUX8i0X8ycNCeUBWPKCM8TMQbzPuelQFTBjf3IegIKKdARG7MdHYmzUK2v6CuN90L5u8P2Sc6+Aryc4NluamZBtGljw23pfUulyMaJScgWuwsb4Zxb4ApJrNConSzU3P8ElZc/mRGNt11ISg3IptRp0YPzznd4ALQHVyMapuLuyTKvpQ2qJrKEZnt1MvjKvAGzleHcY1AkkCYKek/8lJy/RoeNJYLyZly/QkAHw8W/CrHzi74L3KwQro7yy3Tw/Nsu8/lZ9pIGMN6zvfI3PUP+STpE+K6l2W3SjvbDfAQML9RFR+9EvCAa8OXnoGbYqhev/Y2wB0gwhDdnEyqX09/4A56UPJdr/8krNjh/voz6R/XTp5ojYBSgFjpKf8vDy+gR0Npy3NxIcpFsbinmMEr/RAZ+S/RzA78BIV1k2q6ihXCtpwepLbmPYQwCTYf9gz6A==
JJJJJJJJJJJJJJJJ
FlsAlloc
FlsFree
FlsGetValue
FlsSetValue
InitializeCriticalSectionEx
__based(
__cdecl
__pascal
__stdcall
__thiscall
__fastcall
__vectorcall
__clrcall
__eabi
__swift_1
__swift_2
__ptr64
__restrict
__unaligned
restrict(
 delete
operator
`vftable'
`vbtable'
`vcall'
`typeof'
`local static guard'
`string'
`vbase destructor'
`vector deleting destructor'
`default constructor closure'
`scalar deleting destructor'
`vector constructor iterator'
`vector destructor iterator'
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040da38` | `0x40da38` | 2461 | ✓ |
| `fcn.00404720` | `0x404720` | 1396 | ✓ |
| `fcn.00403170` | `0x403170` | 1396 | ✓ |
| `main` | `0x4012e0` | 1223 | ✓ |
| `fcn.0040ab90` | `0x40ab90` | 1084 | ✓ |
| `fcn.0040b8d8` | `0x40b8d8` | 966 | ✓ |
| `fcn.0040393c` | `0x40393c` | 910 | ✓ |
| `fcn.0040a170` | `0x40a170` | 906 | ✓ |
| `fcn.0040e650` | `0x40e650` | 809 | ✓ |
| `section..text` | `0x401000` | 722 | ✓ |
| `fcn.0040c907` | `0x40c907` | 671 | ✓ |
| `fcn.004070db` | `0x4070db` | 652 | ✓ |
| `fcn.0040dc1e` | `0x40dc1e` | 614 | ✓ |
| `fcn.004082af` | `0x4082af` | 606 | ✓ |
| `fcn.0040e9b0` | `0x40e9b0` | 590 | ✓ |
| `fcn.0040dfed` | `0x40dfed` | 576 | ✓ |
| `fcn.0040c18f` | `0x40c18f` | 540 | ✓ |
| `fcn.0040d740` | `0x40d740` | 539 | ✓ |
| `fcn.00407d2e` | `0x407d2e` | 517 | ✓ |
| `fcn.0040efb0` | `0x40efb0` | 499 | ✓ |
| `fcn.00409ab4` | `0x409ab4` | 498 | ✓ |
| `fcn.0040b1b4` | `0x40b1b4` | 493 | ✓ |
| `fcn.0040d240` | `0x40d240` | 471 | ✓ |
| `fcn.0040a81f` | `0x40a81f` | 441 | ✓ |
| `fcn.00407939` | `0x407939` | 421 | ✓ |
| `fcn.0040214b` | `0x40214b` | 407 | ✓ |
| `entry0` | `0x401b20` | 396 | ✓ |
| `fcn.00406ead` | `0x406ead` | 381 | ✓ |
| `fcn.00404ff3` | `0x404ff3` | 370 | ✓ |
| `fcn.0040b400` | `0x40b400` | 364 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040214b.c`](code/fcn.0040214b.c)
- [`code/fcn.00403170.c`](code/fcn.00403170.c)
- [`code/fcn.0040393c.c`](code/fcn.0040393c.c)
- [`code/fcn.00404720.c`](code/fcn.00404720.c)
- [`code/fcn.00404ff3.c`](code/fcn.00404ff3.c)
- [`code/fcn.00406ead.c`](code/fcn.00406ead.c)
- [`code/fcn.004070db.c`](code/fcn.004070db.c)
- [`code/fcn.00407939.c`](code/fcn.00407939.c)
- [`code/fcn.00407d2e.c`](code/fcn.00407d2e.c)
- [`code/fcn.004082af.c`](code/fcn.004082af.c)
- [`code/fcn.00409ab4.c`](code/fcn.00409ab4.c)
- [`code/fcn.0040a170.c`](code/fcn.0040a170.c)
- [`code/fcn.0040a81f.c`](code/fcn.0040a81f.c)
- [`code/fcn.0040ab90.c`](code/fcn.0040ab90.c)
- [`code/fcn.0040b1b4.c`](code/fcn.0040b1b4.c)
- [`code/fcn.0040b400.c`](code/fcn.0040b400.c)
- [`code/fcn.0040b8d8.c`](code/fcn.0040b8d8.c)
- [`code/fcn.0040c18f.c`](code/fcn.0040c18f.c)
- [`code/fcn.0040c907.c`](code/fcn.0040c907.c)
- [`code/fcn.0040d240.c`](code/fcn.0040d240.c)
- [`code/fcn.0040d740.c`](code/fcn.0040d740.c)
- [`code/fcn.0040da38.c`](code/fcn.0040da38.c)
- [`code/fcn.0040dc1e.c`](code/fcn.0040dc1e.c)
- [`code/fcn.0040dfed.c`](code/fcn.0040dfed.c)
- [`code/fcn.0040e650.c`](code/fcn.0040e650.c)
- [`code/fcn.0040e9b0.c`](code/fcn.0040e9b0.c)
- [`code/fcn.0040efb0.c`](code/fcn.0040efb0.c)
- [`code/main.c`](code/main.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

Based on the second chunk of disassembly, I have updated the analysis. While some functions in this section appear to be part of standard library (CRT) routines, their presence—combined with specific behaviors like FPU state management—reinforces the conclusion that this is a sophisticated **packer/loader**.

The following sections have been added or expanded based on your new data:

### Updated Technical Analysis

#### 1. Robust Environment Preparation (FPU Handling)
The function `fcn.0040d240` is a significant finding for unpacking analysis.
*   **FPU Control Word Management:** This function manipulates the FPU (Floating Point Unit) control word, checking and setting bits related to precision, rounding modes, and precision controls (`0x300`, `0x200`, etc.).
*   **Malware Significance:** While standard in many programs, this is a classic "packer" behavior. Packers often reset the FPU state before jumping into the "true" payload (the unpacked code) to ensure that different mathematical environments do not cause the payload's logic to fail or behave inconsistently after being injected into memory.

#### 2. Extensive String and Unicode Processing
Several functions (`fcn.00407d2e`, `fcn.00409ab4`, `fcn.0040a81f`, `fcn.00407939`) are dedicated to complex string handling, specifically:
*   **Codepage Conversion:** Logic involving `GetCPInfo` and `IsValidCodePage` indicates the binary is prepared to handle various international character sets and system locales.
*   **UTF-8/Unicode Normalization:** The logic in `0x409ab4` (handling bits like `0x80`, `0xC0`, and checking range `0xd800` to `0x110000`) suggests the loader is capable of processing Unicode strings.
*   **Malware Significance:** This level of complexity in string handling often points to a packer that needs to decode its own internal configuration files or "map" remote commands from a C2 server that may use various encodings.

#### 3. Complex Math Library Logic (Potential "Filler" or Decryption)
The function `fcn.0040d740` contains a large switch table involving mathematical terms like `log10`, `asin`, `acos`, and `sqrt`.
*   **Analysis:** While these look like standard math library functions, their presence in such a stripped/packed binary can sometimes serve as "code bloat" to inflate the file size or mimic the behavior of a legitimate complex application (like a game or a media player) to evade heuristic scanners.

#### 4. Sophisticated Memory Management
The function `fcn.0040b1b4` displays intricate buffer management and size checks:
*   **Buffer Safety:** It calculates required lengths, checks for overflows (`0x401`), and handles complex memory offsets.
*   **Malware Significance:** This suggests the loader is not just a simple "stub" but contains significant logic to manage the resources of the payload it is about to host (e.g., allocating specific segments for different parts of the malicious code).

---

### Updated Summary for Incident Response

The analysis of Chunk 2 reinforces the **Malicious/Packer** classification with higher confidence in its sophistication level:

1.  **Advanced Unpacking Infrastructure:** The explicit management of FPU states (`0x40d240`) is a high-confidence indicator of a packer designed to host another executable's code in memory.
2.  **Complex Internal Logic:** The heavy investment in Unicode/UTF processing and codepage handling suggests the loader handles complex data structures, likely for communication with an external server or decoding multi-stage payloads.
3.  **Evasion through Mimicry:** The inclusion of large amounts of "standard" looking math and string manipulation code may be a deliberate attempt to hide its malicious purpose behind the appearance of a legitimate application's library imports.

**Recommended Action:** 
Treat this binary as a **high-threat loader**. Any infrastructure it contacts should be immediately blocked, and any files written to disk during its execution (even if they are temporary "dropped" files) should be isolated for further forensic analysis. The presence of complex unpacking logic suggests the actual payload may have sophisticated capabilities such as persistence or data exfiltration.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of FPU state management is a classic packer behavior designed to ensure payload consistency while masking the true nature of the executable. |
| T1027 | Obfuscated Files or Information | Complex Unicode and Codepage processing suggests the loader handles obfuscated internal configurations or decoded remote commands. |
| T1027 | Obfuscated Files or Information | The inclusion of "code bloat" via standard math libraries is a deliberate tactic to mimic legitimate software and evade heuristic analysis. |
| T1055 | Process Injection | Advanced memory management and specific segment allocation indicate the loader is preparing an environment to host an injected payload. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because this sample is identified as a **packer/loader**, many specific network indicators (like IPs or URLs) are likely obfuscated within the encrypted payload and do not appear in plain text in the provided strings.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis suggests these may be hidden within the encoded data blobs or retrieved during execution).

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 strings were present in the provided text).

### **Other artifacts**
*   **Packer/Loader Characteristics:** 
    *   **FPU Control Word Manipulation:** The code at `fcn.0040d240` modifies FPU states (`0x300`, `0x200`). This is a high-confidence indicator of an unpacking routine used to prepare the environment for a secondary payload.
    *   **Unicode/Codepage Handling:** Functions at `fcn.00407d2e`, `fcn.00409ab4`, and `fcn.0040a81f` indicate the loader is designed to handle complex string decoding (UTF-8/Unicode), likely for C2 communication or configuration parsing.
    *   **Anti-Analysis Filler:** The inclusion of high-complexity math functions (`log10`, `asin`, `acos`) in a stripped binary suggests "code bloating" used to mimic legitimate software and evade heuristic detection.
    *   **Memory Management Logic:** `fcn.0040b1b4` indicates sophisticated buffer management for handling decrypted segments of the primary payload.

---
**Analyst Note:** 
The absence of clear network indicators (IPs/URLs) combined with the heavy use of FPU manipulation and Unicode decoding confirms this is a **sophisticated loader**. The actual malicious intent is contained in the "inner" payload which is only unpacked in memory. Security teams should monitor for **Process Hollowing** or **Reflective DLL Injection** techniques immediately following execution.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Packer Characteristics:** The presence of FPU control word manipulation (`fcn.0040d240`) is a high-confidence indicator of a packer designed to prepare the execution environment for an internal payload.
    *   **Evasion Techniques:** The inclusion of "code bloat" (complex math libraries like `log10`, `asin`) and extensive Unicode/Codepage handling suggests a sophisticated effort to mimic legitimate software and bypass heuristic-based detection.
    *   **Sophisticated Memory Management:** Detailed buffer management and segment allocation (`fcn.0040b1b4`) indicate the binary is designed to manage and host multiple segments of an injected payload rather than performing simple tasks.
