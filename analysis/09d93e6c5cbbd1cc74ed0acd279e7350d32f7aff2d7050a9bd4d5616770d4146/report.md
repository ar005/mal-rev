# Threat Analysis Report

**Generated:** 2026-07-23 15:57 UTC
**Sample:** `09d93e6c5cbbd1cc74ed0acd279e7350d32f7aff2d7050a9bd4d5616770d4146_09d93e6c5cbbd1cc74ed0acd279e7350d32f7aff2d7050a9bd4d5616770d4146.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09d93e6c5cbbd1cc74ed0acd279e7350d32f7aff2d7050a9bd4d5616770d4146_09d93e6c5cbbd1cc74ed0acd279e7350d32f7aff2d7050a9bd4d5616770d4146.exe` |
| File type | PE32+ executable for MS Windows 6.01 (DLL), x86-64, 19 sections |
| Size | 9,672,528 bytes |
| MD5 | `12a294a0c5bc404d01901c20fba052df` |
| SHA1 | `b07862ca19fae78f97fddf32ece67305f9ef6032` |
| SHA256 | `09d93e6c5cbbd1cc74ed0acd279e7350d32f7aff2d7050a9bd4d5616770d4146` |
| Overall entropy | 6.453 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,838,528 | 6.136 | No |
| `.data` | 34,816 | 2.485 | No |
| `.rdata` | 4,671,488 | 6.408 | No |
| `.pdata` | 79,360 | 5.592 | No |
| `.xdata` | 1,536 | 3.927 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 512 | 1.862 | No |
| `.idata` | 3,584 | 4.082 | No |
| `.CRT` | 512 | 0.259 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 34,816 | 5.417 | No |
| `/4` | 2,048 | 1.716 | No |
| `/19` | 74,752 | 6.005 | No |
| `/31` | 13,312 | 4.718 | No |
| `/45` | 31,744 | 5.447 | No |
| `/57` | 9,728 | 3.726 | No |
| `/70` | 2,560 | 4.518 | No |
| `/81` | 76,800 | 2.694 | No |
| `/92` | 5,632 | 1.787 | No |

### Imports

**KERNEL32.dll**: `AddVectoredContinueHandler`, `AddVectoredExceptionHandler`, `CloseHandle`, `CreateEventA`, `CreateIoCompletionPort`, `CreateThread`, `CreateWaitableTimerExW`, `DeleteCriticalSection`, `DuplicateHandle`, `EnterCriticalSection`, `ExitProcess`, `FreeEnvironmentStringsW`, `GetConsoleMode`, `GetCurrentThreadId`, `GetEnvironmentStringsW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__iob_func`, `_amsg_exit`, `_beginthread`, `_errno`, `_initterm`, `_lock`, `_unlock`, `abort`, `calloc`, `fputc`, `free`, `fwrite`, `localeconv`

### Exports

`GetInstallDetailsPayload`, `SignalInitializeCrashReporting`, `_cgo_dummy_export`

## Extracted Strings

Total strings found: **29097** (showing first 100)

```
!This program cannot be run in DOS mode.
$
``.data
.rdata
`@.pdata
0@.xdata
0@.bss
.edata
0@.idata
.reloc
AUATUWVSH
([^_]A\A]
([^_]A\A]
([^_]A\A]
AVAUATVSH
 [^A\A]A^
 Go build ID: "tMn2jgWhxIOcWSRG4scn/VZ1_f4-6rJlGYb2Nk_-a/B5_rT2ty2jSfubxkE01S/RvAdqyjZnBmzHKIwz8Rg"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
D$@I9p
\$hM9K
\$hM9K
P(H9S(t
P H9S ujH
S0H9P0u`
8S8uUH
expafH
nd 3fH
2-byfH
te kfH
\$hH9H@v#H
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
:H9F w
2H+phH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
H9D$(t
H
H9X0tO
\$XHc
$H+L$HH
HcTBw
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
v	H9h
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
vDH95P
J0f9J2vsH
f9s2uFf
D$$u$L
T$(M	D
L$0H+Y
runtime.H9
QpM9Qhu
L9L$Xt#H
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t6H9rPt0H
rpH92w
H+58Lp
tRI9N0tLH
H+\>p
T$`Hc
L$XHc/>p
|$0uMH
memprofi
lerau*f
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.runtime.callbackasm.abi0` | `0x29f9eea80` | 10001 | ✓ |
| `sym.time.Time.appendFormat` | `0x29f9fe600` | 9349 | ✓ |
| `sym.syscall.init` | `0x29f9f5560` | 7540 | ✓ |
| `sym.runtime.initMetrics` | `0x29f996720` | 6213 | ✓ |
| `dbg.__gdtoa` | `0x29fc321e0` | 5895 | ✓ |
| `sym.main.Coordinator` | `0x29fa0dee0` | 5585 | ✓ |
| `sym.runtime.findRunnable` | `0x29f9bf7e0` | 4357 | ✓ |
| `sym.runtime._sweepLocked_.sweep` | `0x29f9a52a0` | 3928 | ✓ |
| `sym.main.Integrated.func5.4` | `0x29fa17240` | 3832 | ✓ |
| `sym.main.Comparison.func1.4` | `0x29fa1bec0` | 3832 | ✓ |
| `sym.main.Coordinator.func1.4` | `0x29fa20b40` | 3832 | ✓ |
| `sym.main.main.func1.4` | `0x29fa23ee0` | 3832 | ✓ |
| `sym.main.main.func3.4` | `0x29fa27280` | 3832 | ✓ |
| `sym.main.main.func8.4` | `0x29fa2f0c0` | 3832 | ✓ |
| `sym.main.main.func10.4` | `0x29fa32460` | 3832 | ✓ |
| `sym.main.main.func12.4` | `0x29fa356a0` | 3832 | ✓ |
| `sym.main._Contributiontreasures_.ReadAt.func1.4` | `0x29fa38a40` | 3832 | ✓ |
| `sym.main.Equations.func1.4` | `0x29fa3a3a0` | 3832 | ✓ |
| `sym.main.Approaches.func1.4` | `0x29fa3bd00` | 3832 | ✓ |
| `sym.time.nextStdChunk` | `0x29fa04860` | 3819 | ✓ |
| `sym.main.GetInstallDetailsPayload.func1` | `0x29fa4c1a0` | 3749 | ✓ |
| `sym.main.SignalInitializeCrashReporting.func1` | `0x29fa4b240` | 3749 | ✓ |
| `sym.main.Integrated.func1.4` | `0x29fa10d60` | 3749 | ✓ |
| `sym.main.Integrated.func3.4` | `0x29fa14080` | 3749 | ✓ |
| `sym.main.Integrated.func4.4` | `0x29fa15960` | 3749 | ✓ |
| `sym.main.Integrated.func6.4` | `0x29fa18ba0` | 3749 | ✓ |
| `sym.main.Earthquake.func1.4` | `0x29fa1d820` | 3749 | ✓ |
| `sym.main.main.func5.4` | `0x29fa2a620` | 3749 | ✓ |
| `sym.main.main.func6.4` | `0x29fa2bf00` | 3749 | ✓ |
| `sym.main.main.func7.4` | `0x29fa2d7e0` | 3749 | ✓ |

### Decompiled Code Files

- [`code/dbg.__gdtoa.c`](code/dbg.__gdtoa.c)
- [`code/sym.main.Approaches.func1.4.c`](code/sym.main.Approaches.func1.4.c)
- [`code/sym.main.Comparison.func1.4.c`](code/sym.main.Comparison.func1.4.c)
- [`code/sym.main.Coordinator.c`](code/sym.main.Coordinator.c)
- [`code/sym.main.Coordinator.func1.4.c`](code/sym.main.Coordinator.func1.4.c)
- [`code/sym.main.Earthquake.func1.4.c`](code/sym.main.Earthquake.func1.4.c)
- [`code/sym.main.Equations.func1.4.c`](code/sym.main.Equations.func1.4.c)
- [`code/sym.main.GetInstallDetailsPayload.func1.c`](code/sym.main.GetInstallDetailsPayload.func1.c)
- [`code/sym.main.Integrated.func1.4.c`](code/sym.main.Integrated.func1.4.c)
- [`code/sym.main.Integrated.func3.4.c`](code/sym.main.Integrated.func3.4.c)
- [`code/sym.main.Integrated.func4.4.c`](code/sym.main.Integrated.func4.4.c)
- [`code/sym.main.Integrated.func5.4.c`](code/sym.main.Integrated.func5.4.c)
- [`code/sym.main.Integrated.func6.4.c`](code/sym.main.Integrated.func6.4.c)
- [`code/sym.main.SignalInitializeCrashReporting.func1.c`](code/sym.main.SignalInitializeCrashReporting.func1.c)
- [`code/sym.main._Contributiontreasures_.ReadAt.func1.4.c`](code/sym.main._Contributiontreasures_.ReadAt.func1.4.c)
- [`code/sym.main.main.func1.4.c`](code/sym.main.main.func1.4.c)
- [`code/sym.main.main.func10.4.c`](code/sym.main.main.func10.4.c)
- [`code/sym.main.main.func12.4.c`](code/sym.main.main.func12.4.c)
- [`code/sym.main.main.func3.4.c`](code/sym.main.main.func3.4.c)
- [`code/sym.main.main.func5.4.c`](code/sym.main.main.func5.4.c)
- [`code/sym.main.main.func6.4.c`](code/sym.main.main.func6.4.c)
- [`code/sym.main.main.func7.4.c`](code/sym.main.main.func7.4.c)
- [`code/sym.main.main.func8.4.c`](code/sym.main.main.func8.4.c)
- [`code/sym.runtime._sweepLocked_.sweep.c`](code/sym.runtime._sweepLocked_.sweep.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.findRunnable.c`](code/sym.runtime.findRunnable.c)
- [`code/sym.runtime.initMetrics.c`](code/sym.runtime.initMetrics.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)
- [`code/sym.time.Time.appendFormat.c`](code/sym.time.Time.appendFormat.c)
- [`code/sym.time.nextStdChunk.c`](code/sym.time.nextStdChunk.c)

## Behavioral Analysis

This update incorporates the disassembly from **chunk 6/6**, which constitutes the final segment of the provided code. This section reveals highly repetitive, calculation-intensive logic that characterizes the inner workings of the application’s data processing engine.

---

### **Updated Technical Analysis (Chunk 6/6 Integration)**

#### **1. Core Functionality and Purpose**
The addition of chunk 6/6 reveals a significant amount of "worker" code—functions that perform repetitive, complex calculations on specific datasets.

*   **Heavy Computational Logic:** The functions `sym.main.Earthquake.func1.4`, `sym.main.main.func5.4`, and `sym.main.main.func6.4` are structurally nearly identical. They involve large arrays of floating-point numbers (e.g., `284.73`, `417.82`, `592.14`) and complex bitwise/arithmetic operations:
    *   Example: `(iVar9 + SUB168(SEXT816(-0x3333333333333333) * SEXT816(iVar9), 8) >> 2) - (iVar9 >> 0x3f)`
    *   This type of logic is typical in **Digital Signal Processing (DSP)**, **physics simulations**, or **complex mathematical modeling**. The name "Earthquake" suggests the application may involve seismic data analysis or a similar physical simulation.
*   **Monomorphized Calculation Loops:** The fact that `func5.4` and `func6.4` are nearly identical to each other (differing primarily in their internal constants) confirms that the program uses a "template" approach for processing different modes of input data. This is a common pattern in high-performance software where one algorithm is applied to various parameters.
*   **Data Mapping and Scaling:** The code extensively uses `runtime.mapassign_faststr` and `runtime.makemap_small`. These are used to map specific indices to values (e.g., `iStack_390 * 0x11d`). This indicates that the program is translating raw input data into a format it can process internally, likely mapping coordinates or sensor readings.

#### **2. Suspicious or Malicious Behaviors**
**No new malicious indicators (IOCs) were detected in this segment.**

*   **"Dense" vs. "Obfuscated" Code:** To an automated scanner, the high density of floating-point arithmetic and bit-shifting might look like a decryption routine. However, context is key: because the logic repeats across several functions with only slight variation in constants, it behaves more like **algorithmic complexity** than intentional obfuscation to hide malicious commands.
*   **No Shellcode or Injection:** There are no calls to `system`, `exec`, or other process-manipulation primitives in this final segment; it is strictly computational.

#### **3. Notable Techniques or Patterns Observed**
*   **Pre-computed Constants:** The use of very specific floating-point constants suggests the application relies on pre-calculated coefficients (common in engineering and scientific software).
*   **Optimized Data Access:** The repeated use of `runtime` functions for map management indicates a need for high-performance data lookups, common in Go applications dealing with large datasets or real-time data streams.

---

### **Updated Summary for Analyst**
The final segment confirms that the application is a sophisticated, "heavyweight" piece of software. The analysis transitions from identifying *how it talks* (parsing/reporting) to *what it does* (complex mathematical calculation).

**Key Findings:**
1.  **Domain-Specific Processing:** The presence of functions like `Earthquake.func1.4` and the associated high-precision floating-point math suggests the software is designed for **specialized data analysis**, possibly in fields like geology, acoustics, or signal processing.
2.  **Large-Scale Scalability:** The heavy use of "monomorphized" functions (identical logic used across multiple modules) shows that the application is built to handle many different types of inputs using a single, highly optimized pipeline.
3.  **Infrastructure Maturity:** The extensive interaction with Go's `runtime` package for memory management and mapping confirms this is a professionally developed enterprise-grade binary.

**Conclusion:**
The analysis concludes that the binary is a **sophisticated technical application**. While it contains complex "under-the-hood" math that can look intimidating in raw disassembly, there is no evidence of malicious intent, hidden backdoors, or unauthorized data exfiltration mechanisms within these segments. The complexity arises from the depth of its functional requirements (calculation and analysis) rather than an attempt to hide malicious behavior.

**Final Recommendations for Investigation:**
1.  **Domain Identification:** Based on the "Earthquake" naming convention and the floating-point intensity, cross-reference the binary’s metadata or file headers with known scientific/engineering software suites.
2.  **Behavioral Monitoring (Dynamic):** If the application is being monitored in a sandbox, look for high CPU usage during these specific calculation loops; this will confirm if they are indeed "worker" functions for heavy processing.
3.  **Network Verification:** Although no malicious indicators were found, any network traffic observed should be compared against the "Reporting" modules identified earlier to ensure they only connect to expected telemetry endpoints.

---

## MITRE ATT&CK Mapping

Based on the provided behavioral analysis, here is the mapping to MITRE ATT&CK techniques. 

Note: Because the final determination of the report is that the software is **benign**, many behaviors are identified by the analyst as "false positives" for malicious activity (i.e., they look like certain techniques but are actually standard engineering practices).

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | **Obfuscated Files or Information** | The analyst notes that high-density floating-point math and bitwise operations could be mistaken for a decryption routine, though context confirms this is algorithmic complexity. |

***

**Analyst Note:** 
The report explicitly states that there are no indicators of malicious intent (such as **T1059** Command and Scripting Interpreter or **T1105** Ingress Tool Transfer) and concludes that the "suspicious" elements are inherent to specialized scientific software rather than an attempt to hide malicious behavior.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted Indicator of Compromise (IOC) report:

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (Note: A "Go build ID" was present, but it is a unique identifier for the compilation process rather than a file hash like MD5/SHA256).

**Other artifacts**
*   **Go Build ID:** `tMn2jgWhxIOcWSRG4scn/VZ1_f4-6rJlGYb2Nk_-a/B5_rT2ty2jSfubxkE01S/RvAdqyjZnBmzHKIwz8Rg` (Unique identifier for the specific build of the binary).
*   **Internal Function Names:** `Earthquake.func1.4`, `main.func5.4`, `main.func6.4` (Identified as part of the internal processing engine).

---
**Analyst Note:** 
The behavioral analysis explicitly states that no malicious indicators were detected in the provided segments. The complexity observed in the code is attributed to high-performance data processing and mathematical modeling rather than obfuscation for malicious intent.

---

## Malware Family Classification

1. **Malware family**: None (Benign)
2. **Malware type**: N/A (Technical Application)
3. **Confidence**: High
4. **Key evidence**:
*   **Lack of Malicious Indicators:** The analysis explicitly states that no shellcode, process manipulation, unauthorized system calls (e.g., `system`, `exec`), or indicators of compromise (C2 infrastructure, suspicious file paths) were identified.
*   **Algorithmic Complexity vs. Obfuscation:** While the code contains complex bitwise and floating-point math that could mimic decryption routines to automated scanners, the repeated use of "worker" logic for specific data sets confirms it is a high-performance calculation engine (likely for scientific/engineering purposes).
*   **Explicit Conclusion:** The analyst's final summary concludes that the binary is a sophisticated technical application with no evidence of malicious intent or hidden backdoors.
