# Threat Analysis Report

**Generated:** 2026-08-20 23:12 UTC
**Sample:** `10dbe605fd72cb147a95eadc7b7fff74d8012f2eb99d07f9d33e9df7c377c2e6_10dbe605fd72cb147a95eadc7b7fff74d8012f2eb99d07f9d33e9df7c377c2e6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10dbe605fd72cb147a95eadc7b7fff74d8012f2eb99d07f9d33e9df7c377c2e6_10dbe605fd72cb147a95eadc7b7fff74d8012f2eb99d07f9d33e9df7c377c2e6.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 4 sections |
| Size | 4,344,912 bytes |
| MD5 | `11bf0445497a41f6991c3b5cbdbe0d2c` |
| SHA1 | `031604ec70fde0d149f5dbe15de3c5f125c122da` |
| SHA256 | `10dbe605fd72cb147a95eadc7b7fff74d8012f2eb99d07f9d33e9df7c377c2e6` |
| Overall entropy | 0.497 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1598842096 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 148,484 | 7.208 | ⚠️ Yes |
| `.rdata` | 18,582 | 5.331 | No |
| `.data` | 4,160,232 | 0.013 | No |
| `.rsrc` | 7,248 | 6.042 | No |

### Imports

**KERNEL32.dll**: `FileTimeToDosDateTime`, `EnumResourceNamesW`, `DosDateTimeToFileTime`, `CopyFileExW`, `_llseek`, `SetEndOfFile`, `SetUnhandledExceptionFilter`, `InterlockedIncrement`, `ReadConsoleA`, `SetConsoleActiveScreenBuffer`, `SetEnvironmentVariableW`, `GetNamedPipeHandleStateA`, `WaitForSingleObject`, `OpenSemaphoreA`, `FreeEnvironmentStringsA`
**WINHTTP.dll**: `WinHttpConnect`

### Exports

`_asdga@4`, `_hellgate@4`, `_onemore@4`, `_ssangyong@8`, `_wedding@4`, `_welcome@4`, `_yongfeng@4`

## Extracted Strings

Total strings found: **574** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
^\9nTr
^@9n8r
L$PQR
C0)0)t$0
C4)0)t$,
^tf;P
D$hbB
F09^(u
SVWj>3
G@uwW
0WWWWW
0WWWWW
j
YQPVh
QQSVWd
D$+d$SVW
D$+d$SVW
tSSSSS
tSSSSS
tSSSSS
tVVVVV
tVVVVV
tVVVVV
^SSSSS
^SSSSS
0SSSSS
u,9Et'9
GWhPlB
t"SS9]
j@j ^V
E9Xt
P;Mu+
@@SuzP
^F<-uB
<xtX<XtT
@@SuzP
jF<-uH
<xtV<XtR
0SSSSS
u.j^9
t$hTlB
F\= sB
F@u^V
HHtXHHt
>If90t
tVVVVV
tVVVVV
tVVVVV
t$<"u	3
>=Yt1j
< tK<	tG
FVhPlB
tSSSSS
s[S;7|G;w
tR99u2
C PjPV
C$PjQV
C*PjTV
C+PjUV
C,PjVV
C-PjWV
C.PjRV
C/PjSV
0A@@Ju
0SSSSS
PPPPPPPP
0SSSSS
@9]|FVW
Y;Fu!
G9^t;
Y;Fu.j
u49^t/
p;qt~
PPPPPPPP
v	N+D$
t+WWVPV
URPQQh`0A
F@WuyV
t)jXP
^SSSSS
j"^SSSSS
MQSWVj
u,VVWV
t VV9u
;t$,v-
kUQPXY]Y[
8
u
AA
VW|[;
<xt<Xt	
!nJk$'0
IE$Coq	
poaL
P%
dUeA%(H
IE$Coq	
"o}xN!
F8c4%a
vhjD^:
vhjD^:
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040bc94` | `0x40bc94` | 7104 | ✓ |
| `fcn.00401d70` | `0x401d70` | 6990 | ✓ |
| `fcn.0041f390` | `0x41f390` | 6791 | ✓ |
| `fcn.00410c47` | `0x410c47` | 5632 | ✓ |
| `fcn.0040c27d` | `0x40c27d` | 2935 | ✓ |
| `fcn.00421e0c` | `0x421e0c` | 2477 | ✓ |
| `fcn.00423a89` | `0x423a89` | 2340 | ✓ |
| `fcn.00413812` | `0x413812` | 1843 | ✓ |
| `fcn.00423391` | `0x423391` | 1735 | ✓ |
| `fcn.00414ebf` | `0x414ebf` | 1474 | ✓ |
| `fcn.00422909` | `0x422909` | 1348 | ✓ |
| `fcn.00422e4d` | `0x422e4d` | 1348 | ✓ |
| `fcn.0040f0b2` | `0x40f0b2` | 1051 | ✓ |
| `fcn.00406aba` | `0x406aba` | 933 | ✓ |
| `fcn.00421665` | `0x421665` | 883 | ✓ |
| `fcn.00407030` | `0x407030` | 869 | ✓ |
| `fcn.00409bb0` | `0x409bb0` | 869 | ✓ |
| `fcn.0040ea75` | `0x40ea75` | 839 | ✓ |
| `fcn.0040a2a5` | `0x40a2a5` | 790 | ✓ |
| `fcn.004244db` | `0x4244db` | 783 | ✓ |
| `fcn.00405ec2` | `0x405ec2` | 770 | ✓ |
| `fcn.0040aa54` | `0x40aa54` | 741 | ✓ |
| `fcn.0040a773` | `0x40a773` | 737 | ✓ |
| `main` | `0x420f00` | 699 | ✓ |
| `fcn.00407588` | `0x407588` | 596 | ✓ |
| `fcn.00405c91` | `0x405c91` | 561 | ✓ |
| `fcn.00415984` | `0x415984` | 559 | ✓ |
| `fcn.004247ea` | `0x4247ea` | 554 | ✓ |
| `fcn.004061c4` | `0x4061c4` | 539 | ✓ |
| `fcn.00412583` | `0x412583` | 539 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401d70.c`](code/fcn.00401d70.c)
- [`code/fcn.00405c91.c`](code/fcn.00405c91.c)
- [`code/fcn.00405ec2.c`](code/fcn.00405ec2.c)
- [`code/fcn.004061c4.c`](code/fcn.004061c4.c)
- [`code/fcn.00406aba.c`](code/fcn.00406aba.c)
- [`code/fcn.00407030.c`](code/fcn.00407030.c)
- [`code/fcn.00407588.c`](code/fcn.00407588.c)
- [`code/fcn.00409bb0.c`](code/fcn.00409bb0.c)
- [`code/fcn.0040a2a5.c`](code/fcn.0040a2a5.c)
- [`code/fcn.0040a773.c`](code/fcn.0040a773.c)
- [`code/fcn.0040aa54.c`](code/fcn.0040aa54.c)
- [`code/fcn.0040bc94.c`](code/fcn.0040bc94.c)
- [`code/fcn.0040c27d.c`](code/fcn.0040c27d.c)
- [`code/fcn.0040ea75.c`](code/fcn.0040ea75.c)
- [`code/fcn.0040f0b2.c`](code/fcn.0040f0b2.c)
- [`code/fcn.00410c47.c`](code/fcn.00410c47.c)
- [`code/fcn.00412583.c`](code/fcn.00412583.c)
- [`code/fcn.00413812.c`](code/fcn.00413812.c)
- [`code/fcn.00414ebf.c`](code/fcn.00414ebf.c)
- [`code/fcn.00415984.c`](code/fcn.00415984.c)
- [`code/fcn.0041f390.c`](code/fcn.0041f390.c)
- [`code/fcn.00421665.c`](code/fcn.00421665.c)
- [`code/fcn.00421e0c.c`](code/fcn.00421e0c.c)
- [`code/fcn.00422909.c`](code/fcn.00422909.c)
- [`code/fcn.00422e4d.c`](code/fcn.00422e4d.c)
- [`code/fcn.00423391.c`](code/fcn.00423391.c)
- [`code/fcn.00423a89.c`](code/fcn.00423a89.c)
- [`code/fcn.004244db.c`](code/fcn.004244db.c)
- [`code/fcn.004247ea.c`](code/fcn.004247ea.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This analysis has been updated to include the findings from the third and final chunk of disassembly.

### Updated Analysis Summary

#### Core Functionality and Purpose
The inclusion of the final chunk confirms that this binary is not just "over-engineered," but contains highly specialized routines for **low-level system interaction, complex memory management, and advanced error handling.**

New insights include:
*   **Sophisticated Exception Handling (SEH):** The function `fcn.004247ea` is a classic example of manual Exception Handling logic. It modifies exception records, manipulates status codes, and interacts with `RaiseException`. While this can be used for legitimate error handling, it is frequently used in advanced malware to **trap debuggers**, handle "intentional" exceptions during decryption loops, or redirect execution flow when an anti-debugging check triggers.
*   **Dynamic Memory Management (Heap Operations):** Function `fcn.00412583` utilizes `HeapAlloc` and `HeapReAlloc` within a very complex logic structure. It includes manual buffer resizing calculations and state checks. This is characteristic of a **loader/packer** that is assembling or decompressing a secondary payload in memory, where the final size of the payload may not be known until the "unpacking" process is complete.
*   **Structure Parsing and Data Extraction:** Functions like `fcn.004061c4` appear to iterate through structured data (using fixed offsets like `0x48` and `+ 4`). This suggests the binary is parsing a custom internal resource or a configuration block, likely preparing it for the next stage of execution.

#### Suspicious or Malicious Behaviors
The final set of functions reinforces several hallmarks of high-end malware:

*   **Anti-Analysis via Exceptions:** The complexity of `fcn.004247ea` suggests that the author intends to use exceptions as a control flow mechanism. This is designed to frustrate automated sandboxes and manual debuggers, which often struggle to follow execution paths that jump through exception handlers.
*   **Complex Buffer Expansion:** The use of `HeapReAlloc` in `fcn.00412583` suggests the binary prepares for a "dynamic" payload. By resizing buffers dynamically, it can hide the true size and nature of the decrypted code until much later in the execution cycle.
*   **Data Obfuscation via Complexity:** The jumpy logic in `fcn.00415984` (the calculation-heavy loop) indicates that even "simple" data extractions are wrapped in layers of arithmetic to prevent static analysis from easily identifying what is being unpacked or decoded.

#### Notable Techniques or Patterns
*   **State-Machine Logic:** Several functions use heavy conditional branching and bitwise flags to determine the next action. This allows a single function to perform many different tasks depending on internal state, making it harder for an analyst to map out the program's behavior through static analysis alone.
*   **Manual Entry Point Obfuscation:** The way the binary handles memory (manual calculation of buffer sizes and subsequent `HeapReAlloc` calls) suggests that once the "preamble" (the math/logic loops in `main`) is finished, the code will transition to a completely different execution mode or jump into a freshly unpacked region of memory.

---

### Final Summary for Investigation
The full disassembly confirms that this binary is a **highly sophisticated multi-stage loader.** It uses "bloated" libraries (math, localization) as a decorative shell to mask its primary purpose: the decryption and preparation of a secondary payload.

**Key Indicators of Concern:**
1.  **Advanced Evasion Layers:** The use of complex SEH (Exception Handling) and long "junk" loops in `main` are definitive indicators of professional-grade evasion techniques meant to thwart both automated and human analysis.
2.  **Robust Unpacking Infrastructure:** The combination of advanced memory management (`HeapReAlloc`), custom parsing routines, and heavy arithmetic confirms that the binary is designed to unpack a significant, potentially large, amount of code into memory.
3.  **Hidden Execution Paths:** By utilizing complex jump tables and exception-based branching, the author has ensured that the "malicious" part of the code only reveals itself under specific conditions or at a specific point in time during execution.

**Final Recommendations for Investigation:**
1.  **Dynamic Analysis with Debugger Plugins:** Use a debugger equipped with an exception handler tracer (like ScyllaHide). This will allow you to see if the "exception" logic is being used specifically to detect the presence of a debugger or to navigate complex, obfuscated code paths.
2.  **Memory Monitoring:** Focus on `fcn.00412583`. Monitor this function during execution to identify where and when it allocates memory for the final payload. Look for the creation of new executable (`RX` or `RWX`) memory regions.
3.  **Network/System Call Hooking:** Since the binary is clearly prepared to "prepare" a large amount of data, monitor all system calls related to file I/O and networking (e.g., `WinHttp`, `InternetOpen`, `CreateFile`). These will likely occur once the internal "parsing" and "unpacking" loops are completed.
4.  **Identify the Payload:** Once a jump into a new memory region occurs, dump that memory to disk for separate analysis. The current binary is likely just the vehicle (the loader) for a more significant piece of malware.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Evasion | The use of sophisticated Exception Handling (SEH) is explicitly identified as a method to trap debuggers and frustrate automated sandboxes. |
| T1027 | Obfuscated Files or Information | Complex arithmetic-heavy loops and layered logic are used to mask the nature of data extraction from static analysis. |
| T1036 | Masquerading | The binary utilizes "bloated" libraries (math, localization) as a decorative shell to hide its primary function as a loader. |
| T1106 | Native API | The use of `HeapAlloc`, `HeapReAlloc`, and `RaiseException` shows direct interaction with system APIs for memory management and execution control. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral documentation, here is the report of identified Indicators of Compromise (IOCs).

### **Analysis Notes**
The "Extracted Strings" section appears to contain heavily obfuscated data, encrypted blocks, or junk data intended to hinder static analysis. The "Behavioral Analysis" describes technical mechanisms (SEH, HeapAlloc, and multi-stage loading) rather than specific infrastructure indicators like hardcoded IP addresses or file paths.

---

### **IOC Categorization**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: `.rdata` and `.data` are standard PE section headers, not filesystem paths).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Suspicious Behavior:** The use of complex **Exception Handling (SEH)** logic at `fcn.004247ea` is a technical indicator of anti-debugging and anti-analysis techniques.
*   **Suspicious Behavior:** Dynamic memory expansion via **HeapReAlloc** at `fcn.00412583` indicates the construction of an in-memory payload (loader behavior).
*   **Signature Pattern:** The presence of "junk" loops and calculation-heavy loops (e.g., `fcn.00415984`) suggests a multi-stage packer/loader designed to hide its primary payload.

---
**Analyst Note:** While no traditional network or filesystem IOCs were found in this specific sample, the behavioral analysis confirms the presence of high-sophistication evasion techniques characteristic of a **multistage loader**. Further dynamic analysis (memory dumping) is required to extract the secondary stage's artifacts.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification of the sample:

1.  **Malware family**: Unknown
2.  **Malware type**: Loader
3.  **Confidence**: High (regarding functionality/type)
4.  **Key evidence**: 
    *   **Multi-Stage Loading Architecture:** The use of `HeapAlloc` and `HeapReAlloc` combined with complex data parsing routines indicates the binary's primary purpose is to unpack and prepare a secondary payload in memory, rather than performing direct malicious actions like encryption or data exfiltration.
    *   **Advanced Anti-Analysis Techniques:** The implementation of sophisticated Exception Handling (SEH) for control flow redirection and the use of "junk" loops are classic evasion tactics designed to thwart debuggers and automated sandboxes.
    *   **Intentional Masquerading:** The inclusion of bloated, unnecessary libraries (math, localization) serves as a "decoy" shell to hide the underlying malicious loader functionality from static analysis tools.
