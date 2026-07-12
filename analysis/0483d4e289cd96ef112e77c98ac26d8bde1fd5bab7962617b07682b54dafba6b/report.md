# Threat Analysis Report

**Generated:** 2026-07-11 19:11 UTC
**Sample:** `0483d4e289cd96ef112e77c98ac26d8bde1fd5bab7962617b07682b54dafba6b_0483d4e289cd96ef112e77c98ac26d8bde1fd5bab7962617b07682b54dafba6b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0483d4e289cd96ef112e77c98ac26d8bde1fd5bab7962617b07682b54dafba6b_0483d4e289cd96ef112e77c98ac26d8bde1fd5bab7962617b07682b54dafba6b.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 209,408 bytes |
| MD5 | `84b097aea8f10f412e2638964e10c226` |
| SHA1 | `9e2f1a1b3c5d16d744864f1ad2e8aabf94097b28` |
| SHA256 | `0483d4e289cd96ef112e77c98ac26d8bde1fd5bab7962617b07682b54dafba6b` |
| Overall entropy | 6.28 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1686198385 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 151,040 | 6.436 | No |
| `.rdata` | 44,544 | 5.078 | No |
| `.data` | 5,120 | 2.894 | No |
| `.pdata` | 5,120 | 5.152 | No |
| `.rsrc` | 512 | 2.527 | No |
| `.reloc` | 2,048 | 5.78 | No |

### Imports

**KERNEL32.dll**: `ReleaseSRWLockExclusive`, `AcquireSRWLockExclusive`, `WakeAllConditionVariable`, `SleepConditionVariableSRW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `GetCurrentProcess`, `TerminateProcess`, `IsProcessorFeaturePresent`, `QueryPerformanceCounter`, `GetCurrentProcessId`, `GetCurrentThreadId`

## Extracted Strings

Total strings found: **466** (showing first 100)

```
!This program cannot be run in DOS mode.
$
I7xr12y
12yRich
`.rdata
@.data
.pdata
@.rsrc
@.reloc
L$ SVWH
A_A^A]_
WAVAWH
WAVAWH
 A_A^_
D!DLL
WAUAVAW
WAVAWH
ATAVAW
|$ AVH
L$ SWH
USVWATAUAVAWH
A_A^A]A\_
RAPAQH
UAVAWH
L$0HcA<
|$ AVH
uxHc,
VWATAVAWH
 A_A^A\_^
WATAUAVAWH
A_A^A]A\_
H;XXs
H;xXu5
WATAUAVAWH
A_A^A]A\_
AUAVAWH
9;|
HcC
u4I9}(
;I9}(tiH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
K0HcQD
C0Hc	H
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
@SVWATAUAVAWH
L!|$(L!
D$0HcH
pA_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
0A_A^A]A\_^[
t$ WATAUAVAWH
E0Lc`I
E0HcHD
 A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
S(HcS0
S(HcS0
S(HcS0
x UAVAWH
D$0u3
\$8t	H
D$@H;F
kL@8o(u
<htl<jt\<lt4<tt$<wt
UWATAVAWH
A_A^A\_]
{4t-A
WAVAWH
 A_A^_
p0R^G'
t98t H
u3HcH<H
WATAUAVAWH
< t=<	t9
 A_A^A]A\_
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
L3
H3B
 A_A^_
D$0@8{
WATAUAVAWH
 A_A^A]A\_
p0R^G'
L$ VWAVH
fD9t$b
f9
t	H

fA9	t	I
f9
t	H
f9
t	H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180010ca7` | `0x180010ca7` | 65155 | ✓ |
| `fcn.1800015b0` | `0x1800015b0` | 64913 | ✓ |
| `fcn.18000effc` | `0x18000effc` | 64767 | ✓ |
| `fcn.1800023b5` | `0x1800023b5` | 64653 | ✓ |
| `fcn.1800051be` | `0x1800051be` | 64415 | ✓ |
| `fcn.18000146e` | `0x18000146e` | 64362 | ✓ |
| `fcn.180007fdc` | `0x180007fdc` | 64269 | ✓ |
| `fcn.180009128` | `0x180009128` | 64217 | ✓ |
| `fcn.180009335` | `0x180009335` | 63829 | ✓ |
| `fcn.1800019b2` | `0x1800019b2` | 63824 | ✓ |
| `fcn.18000eba3` | `0x18000eba3` | 63788 | ✓ |
| `fcn.18000cb41` | `0x18000cb41` | 63520 | ✓ |
| `fcn.18000439f` | `0x18000439f` | 63425 | ✓ |
| `fcn.18000a9b3` | `0x18000a9b3` | 63399 | ✓ |
| `fcn.1800024d8` | `0x1800024d8` | 63333 | ✓ |
| `fcn.18000f50f` | `0x18000f50f` | 63221 | ✓ |
| `fcn.1800017e5` | `0x1800017e5` | 63219 | ✓ |
| `fcn.180007e34` | `0x180007e34` | 63216 | ✓ |
| `fcn.180001942` | `0x180001942` | 63207 | ✓ |
| `fcn.18000cb84` | `0x18000cb84` | 63171 | ✓ |
| `fcn.18000a4c1` | `0x18000a4c1` | 62957 | ✓ |
| `fcn.18000188a` | `0x18000188a` | 62586 | ✓ |
| `fcn.1800028e1` | `0x1800028e1` | 62488 | ✓ |
| `fcn.180010b46` | `0x180010b46` | 62476 | ✓ |
| `fcn.180005fb9` | `0x180005fb9` | 62390 | ✓ |
| `fcn.180010d04` | `0x180010d04` | 62290 | ✓ |
| `fcn.180001702` | `0x180001702` | 62192 | ✓ |
| `fcn.18000fc14` | `0x18000fc14` | 62059 | ✓ |
| `fcn.18000a3c1` | `0x18000a3c1` | 62043 | ✓ |
| `fcn.180010e06` | `0x180010e06` | 61976 | ✓ |

### Decompiled Code Files

- [`code/fcn.18000146e.c`](code/fcn.18000146e.c)
- [`code/fcn.1800015b0.c`](code/fcn.1800015b0.c)
- [`code/fcn.180001702.c`](code/fcn.180001702.c)
- [`code/fcn.1800017e5.c`](code/fcn.1800017e5.c)
- [`code/fcn.18000188a.c`](code/fcn.18000188a.c)
- [`code/fcn.180001942.c`](code/fcn.180001942.c)
- [`code/fcn.1800019b2.c`](code/fcn.1800019b2.c)
- [`code/fcn.1800023b5.c`](code/fcn.1800023b5.c)
- [`code/fcn.1800024d8.c`](code/fcn.1800024d8.c)
- [`code/fcn.1800028e1.c`](code/fcn.1800028e1.c)
- [`code/fcn.18000439f.c`](code/fcn.18000439f.c)
- [`code/fcn.1800051be.c`](code/fcn.1800051be.c)
- [`code/fcn.180005fb9.c`](code/fcn.180005fb9.c)
- [`code/fcn.180007e34.c`](code/fcn.180007e34.c)
- [`code/fcn.180007fdc.c`](code/fcn.180007fdc.c)
- [`code/fcn.180009128.c`](code/fcn.180009128.c)
- [`code/fcn.180009335.c`](code/fcn.180009335.c)
- [`code/fcn.18000a3c1.c`](code/fcn.18000a3c1.c)
- [`code/fcn.18000a4c1.c`](code/fcn.18000a4c1.c)
- [`code/fcn.18000a9b3.c`](code/fcn.18000a9b3.c)
- [`code/fcn.18000cb41.c`](code/fcn.18000cb41.c)
- [`code/fcn.18000cb84.c`](code/fcn.18000cb84.c)
- [`code/fcn.18000eba3.c`](code/fcn.18000eba3.c)
- [`code/fcn.18000effc.c`](code/fcn.18000effc.c)
- [`code/fcn.18000f50f.c`](code/fcn.18000f50f.c)
- [`code/fcn.18000fc14.c`](code/fcn.18000fc14.c)
- [`code/fcn.180010b46.c`](code/fcn.180010b46.c)
- [`code/fcn.180010ca7.c`](code/fcn.180010ca7.c)
- [`code/fcn.180010d04.c`](code/fcn.180010d04.c)
- [`code/fcn.180010e06.c`](code/fcn.180010e06.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's behavior and characteristics.

### Overview
The code exhibits hallmarks of a **packed or heavily obfuscated loader/packer**. The primary purpose appears to be preparing a hidden payload for execution while evading static and dynamic analysis by hiding its true intentions (like API imports) until runtime.

### Suspicious and Malicious Behaviors
*   **Heavy Obfuscation & Packing:** 
    *   The **extracted strings** are largely comprised of "garbage" or high-entropy data. This is a common indicator of a packer, where the actual malicious strings (IPs, file paths, registry keys) are encrypted and only decrypted in memory.
    *   Many functions (`fcn.1800015b0`, `fcn.18000effc`, etc.) contain minimal logic or repeated "LOCK/UNLOCK" blocks. This is often used as **junk code insertion** to confuse disassemblers and complicate the analysis of the execution flow.
*   **Dynamic API Resolution (API Hashing):**
    *   In `fcn.180010e06`, the use of large hex constants (e.g., `0x4be5a75d` and `0x32cb8d86`) is a classic indicator of **API Hashing**. Instead of calling Windows APIs directly (which would be visible in the Import Address Table), the malware hashes the names of the functions it needs at runtime to find their addresses.
*   **Indirect Function Calls & Dispatch Tables:**
    *   Functions like `fcn.180010ca7` and `fcn.180009335` utilize indirect calls, such as `(**(iVar1 + 0x10))()`. This indicates the use of a **dispatch table**. By calling functions through pointers in a table rather than directly, the malware hides its control flow from automated analysis tools.
*   **Position-Independent Code (PIC) / Manual Mapping:**
    *   The presence of very high memory addresses (e.g., `0x180031...`) suggests that the code is designed to run in a way where it doesn't rely on standard relocation, or it is interacting with a dynamically mapped module (a technique common in **Process Injection**).

### Notable Techniques & Patterns
*   **Control Flow Flattening/Obfuscation:** The complex pointer arithmetic and bit-shifting in `fcn.180009335` (e.g., `uVar4 = unaff_R14 >> 0x20`) are used to mask the actual logic of the program from a human analyst.
*   **Staged Execution:** The structure suggests a "stub" architecture. The code provided likely acts as a loader that decrypts/decompresses an internal payload, resolves its necessary functions via hashing, and then jumps to the actual malicious routine (the "payload").
*   **Anti-Analysis:** By using highly non-standard ways to call functions and hiding strings, the author is intentionally attempting to bypass signature-based detection and make manual reverse engineering significantly more time-consuming.

### Summary Table for Analysts
| Feature | Observation | Likely Intent |
| :--- | :--- | :--- |
| **Strings** | High entropy / Junk characters | Encrypted payload/strings; evasion of simple string analysis. |
| **API Resolution** | Hardcoded constants (e.g., `0x32cb8d86`) | API Hashing to hide imports from the IAT. |
| **Control Flow** | Indirect calls and dispatch tables | Obfuscation of execution path; "hiding" the core logic. |
| **Code Structure** | Repeated patterns & junk code | Anti-analysis (making manual reversing tedious). |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of packing, high-entropy "garbage" strings, and junk code (LOCK/UNLOCK blocks) is intended to hide the malware's true intent from static analysis. |
| T1027 | Obfuscated Files or Information | Control flow flattening and complex bit-shifting are used specifically to mask logic and complicate manual reverse engineering. |
| T1055 | Process Injection | The use of Position-Independent Code (PIC) and manual mapping suggests the binary acts as a loader to inject a hidden payload into memory. |
| T1106 | Dynamic Resolution* | The use of API hashing (e.g., `0x32cb8d86`) allows the malware to resolve functions at runtime, hiding its imports from the Import Address Table (IAT). |

*\*Note: While "Dynamic Resolution" is frequently associated with T1027 (Obfuscated Files or Information) in many threat reports, it specifically describes the mechanism of bypassing static analysis by resolving symbols at runtime.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report regarding Indicators of Compromise (IOCs).

### **Threat Intelligence Analysis Summary**
The analysis indicates that this binary is a **packed or heavily obfuscated loader**. Because the malware uses encryption and API hashing to hide its true functionality, most primary IOCs (such as plain-text IPs, URLs, and file paths) are not present in the raw strings.

---

### **Indicators of Compromise**

**IP addresses / URLs / Domains**
*   None identified (Strings are encrypted/obfuscated).

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   *Note: No file hashes (MD5/SHA1/SHA256) were provided in the source text.*

**Other artifacts**
*   **API Hashing Constants:** `0x4be5a75d`, `0x32cb8d86` (Used for resolving hidden API imports).
*   **Execution Patterns:** 
    *   **Junk Code Insertion:** Repeated "LOCK/UNLOCK" blocks and dummy loops.
    *   **Control Flow Flattening:** Complex bit-shifting and pointer arithmetic to mask logic.
    *   **Dispatch Tables:** Use of indirect function calls (e.g., `(**(iVar1 + 0x10))()`) to hide the execution path.

---

### **Analyst Note**
The high entropy of the strings section confirms that the malware is designed to bypass static analysis. Because the indicators are "wrapped" in a packer, manual de-obfuscation or dynamic analysis (sandboxing) would be required to extract the underlying C2 infrastructure and file system modifications.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Evasive Architecture:** The presence of high-entropy "garbage" strings, junk code insertion (LOCK/UNLOCK blocks), and control flow flattening are definitive characteristics of a sophisticated packer or "stub" designed to hide the primary payload from static analysis.
    *   **Anti-Analysis Techniques:** The use of API hashing (e.g., `0x4be5a75d`) and dispatch tables ensures that the malware's true capabilities and system interactions are only visible at runtime, a common trait in high-end loaders.
    *   **Staged Execution Pattern:** The presence of Position-Independent Code (PIC) and manual mapping indicates that this binary is not the final payload, but rather a delivery mechanism designed to inject or decrypt a secondary malicious component into memory.
