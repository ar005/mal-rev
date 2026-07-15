# Threat Analysis Report

**Generated:** 2026-07-12 08:29 UTC
**Sample:** `04e30f37e062b97c5c6045d64ca501c1e91f1b65bc5961abef7428002bb48075_04e30f37e062b97c5c6045d64ca501c1e91f1b65bc5961abef7428002bb48075.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04e30f37e062b97c5c6045d64ca501c1e91f1b65bc5961abef7428002bb48075_04e30f37e062b97c5c6045d64ca501c1e91f1b65bc5961abef7428002bb48075.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 7 sections |
| Size | 69,329,920 bytes |
| MD5 | `371b046cfbd11ce12f3eed67c77b2a20` |
| SHA1 | `d36fa7770e330cf3adb47da7cec68e26e0c793fc` |
| SHA256 | `04e30f37e062b97c5c6045d64ca501c1e91f1b65bc5961abef7428002bb48075` |
| Overall entropy | 7.951 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769288479 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 92,160 | 6.494 | No |
| `.rdata` | 45,568 | 5.024 | No |
| `.data` | 3,072 | 2.05 | No |
| `.pdata` | 5,120 | 4.91 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 69,180,416 | 7.951 | ⚠️ Yes |
| `.reloc` | 2,048 | 4.928 | No |

### Imports

**KERNEL32.dll**: `CreateFileA`, `CreateFileW`, `FlushFileBuffers`, `WriteFile`, `GetTempPathW`, `CloseHandle`, `GetLastError`, `CreateProcessW`, `FreeLibrary`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `LoadResource`, `LockResource`, `SizeofResource`

### Exports

`curl_easy_cleanup`, `curl_easy_init`, `curl_easy_perform`, `curl_easy_setopt`

## Extracted Strings

Total strings found: **247405** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
L$ SVWH
L$ SVWH
L$ SVWH
|$ AVH
WATAUAVAWH
A_A^A]A\_
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
G0HcX
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
@SVWATAUAVAWH
A_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
|$$Hc^
@A_A^A]A\_^[
UVWATAUAVAWH
G0Lch
G0HcX
D$hIcu
 A_A^A]A\_^]
99~YHc^
@USVWATAVAWH
A_A^A\_^[]
@USVWATAVAWH
A_A^A\_^[]
WATAUAVAWH
0A_A^A]A\_
UVWATAUAVAWH
rsf;\$d
r_f;\$l
rKf;\$t
r7f;\$|
f;\$4r
f;\$<r
f;\$Dr
rvf;\$d
rbf;\$l
rNf;\$t
r:f;\$|
A_A^A]A\_^]
S(HcS0
S(HcS0
S(HcS0
S(HcS0
S(HcS0
S(HcS0
D$0u3
\$8t	H
D$@H;F
D$@H;F
sL@8w(u
<htl<jt\<lt4<tt$<wt
UWATAVAWH
A_A^A\_]
UATAUAVAWH
A_A^A]A\]
|$ AWH
D$18F(u
{4t-A
WAVAWH
 A_A^_
t98t H
u3HcH<H
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
L3
H3B
 A_A^_
D$0@8{
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180002908` | `0x180002908` | 30143 | ✓ |
| `fcn.18000aa7c` | `0x18000aa7c` | 20695 | ✓ |
| `fcn.18000aa44` | `0x18000aa44` | 20690 | ✓ |
| `fcn.180011fd0` | `0x180011fd0` | 11897 | ✓ |
| `fcn.180010cbc` | `0x180010cbc` | 4735 | ✓ |
| `fcn.1800147c0` | `0x1800147c0` | 4727 | ✓ |
| `fcn.180002810` | `0x180002810` | 2946 | ✓ |
| `fcn.180002998` | `0x180002998` | 2676 | ✓ |
| `fcn.180001120` | `0x180001120` | 2557 | ✓ |
| `fcn.18000e414` | `0x18000e414` | 1985 | ✓ |
| `fcn.180005dc0` | `0x180005dc0` | 1898 | ✓ |
| `fcn.180016750` | `0x180016750` | 1677 | ✓ |
| `fcn.180014890` | `0x180014890` | 1451 | ✓ |
| `fcn.180008834` | `0x180008834` | 1397 | ✓ |
| `fcn.1800043d8` | `0x1800043d8` | 1213 | ✓ |
| `fcn.1800139e4` | `0x1800139e4` | 1171 | ✓ |
| `fcn.180010830` | `0x180010830` | 1164 | ✓ |
| `fcn.1800083c4` | `0x1800083c4` | 1133 | ✓ |
| `fcn.1800022e8` | `0x1800022e8` | 1112 | ✓ |
| `fcn.1800022f0` | `0x1800022f0` | 1109 | ✓ |
| `fcn.180001e80` | `0x180001e80` | 990 | ✓ |
| `fcn.180002390` | `0x180002390` | 960 | ✓ |
| `fcn.180012f10` | `0x180012f10` | 922 | ✓ |
| `fcn.180016e00` | `0x180016e00` | 920 | ✓ |
| `fcn.1800129a0` | `0x1800129a0` | 920 | ✓ |
| `fcn.18000b660` | `0x18000b660` | 915 | ✓ |
| `fcn.180007a68` | `0x180007a68` | 871 | ✓ |
| `fcn.18000e018` | `0x18000e018` | 862 | ✓ |
| `fcn.180001b20` | `0x180001b20` | 850 | ✓ |
| `fcn.180013364` | `0x180013364` | 817 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001120.c`](code/fcn.180001120.c)
- [`code/fcn.180001b20.c`](code/fcn.180001b20.c)
- [`code/fcn.180001e80.c`](code/fcn.180001e80.c)
- [`code/fcn.1800022e8.c`](code/fcn.1800022e8.c)
- [`code/fcn.1800022f0.c`](code/fcn.1800022f0.c)
- [`code/fcn.180002390.c`](code/fcn.180002390.c)
- [`code/fcn.180002810.c`](code/fcn.180002810.c)
- [`code/fcn.180002908.c`](code/fcn.180002908.c)
- [`code/fcn.180002998.c`](code/fcn.180002998.c)
- [`code/fcn.1800043d8.c`](code/fcn.1800043d8.c)
- [`code/fcn.180005dc0.c`](code/fcn.180005dc0.c)
- [`code/fcn.180007a68.c`](code/fcn.180007a68.c)
- [`code/fcn.1800083c4.c`](code/fcn.1800083c4.c)
- [`code/fcn.180008834.c`](code/fcn.180008834.c)
- [`code/fcn.18000aa44.c`](code/fcn.18000aa44.c)
- [`code/fcn.18000aa7c.c`](code/fcn.18000aa7c.c)
- [`code/fcn.18000b660.c`](code/fcn.18000b660.c)
- [`code/fcn.18000e018.c`](code/fcn.18000e018.c)
- [`code/fcn.18000e414.c`](code/fcn.18000e414.c)
- [`code/fcn.180010830.c`](code/fcn.180010830.c)
- [`code/fcn.180010cbc.c`](code/fcn.180010cbc.c)
- [`code/fcn.180011fd0.c`](code/fcn.180011fd0.c)
- [`code/fcn.1800129a0.c`](code/fcn.1800129a0.c)
- [`code/fcn.180012f10.c`](code/fcn.180012f10.c)
- [`code/fcn.180013364.c`](code/fcn.180013364.c)
- [`code/fcn.1800139e4.c`](code/fcn.1800139e4.c)
- [`code/fcn.1800147c0.c`](code/fcn.1800147c0.c)
- [`code/fcn.180014890.c`](code/fcn.180014890.c)
- [`code/fcn.180016750.c`](code/fcn.180016750.c)
- [`code/fcn.180016e00.c`](code/fcn.180016e00.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated and extended the analysis. The new code confirms several behaviors previously suspected, specifically regarding the complexity of its loading sequence and the explicit nature of its internal debugging/tracking.

### **Updated Analysis Summary**

The binary is a sophisticated **multistage loader/dropper**. The second chunk of disassembly reveals that it doesn't just "drop" a file; it performs complex buffer manipulations, handles specific memory offsets for internal data structures, and follows a rigid execution path to transition from its initial state to the final payload.

---

### **Core Functionality (Updated)**
The binary acts as a sophisticated **pre-loader** for a secondary malicious component. 
*   **Sophisticated Resource Handling:** The inclusion of functions like `fcn.1800129a0` and `fcn.1800139e4` indicates that the payload is not simply moved from memory to disk; it undergoes significant buffer manipulation and formatting before being written via `WriteFile`.
*   **Dependency/Library Resolution:** The code specifically attempts to find, load, and resolve function pointers (using `GetProcAddress`) from an external library (appearing as `msvcr_27574.dll`). This is a common technique used by malware to ensure it has the necessary environment or to "link" with a specific version of a system DLL that provides specialized functionality.
*   **Staged Execution Path:** The logs found in the code (`ExtractAndRunFromTemp`, `Loading real libcurl`) confirm a transition from Stage 1 (Loader) $\rightarrow$ Stage 2 (Environment/Library Setup) $\rightarrow$ Stage 3 (Payload Execution).

---

### **Suspicious & Malicious Behaviors (Updated)**
The following behaviors are confirmed or further detailed in the new disassembly:

*   **Sophisticated Payload Extraction (`fcn.1800139e4`):**
    Instead of using high-level copy functions, the binary uses complex loop logic to iterate through memory buffers and write them using `WriteFile`. This manual approach is often used to bypass heuristic scanners that monitor standard "File Copy" API patterns.
*   **Internal Tracking/Debugging Logging (`fcn.180001e80`):**
    The binary writes highly descriptive status messages to `C:\Users\Public\debug_libcurl.txt`. These include:
    *   *"DllMain: PROCESS_ATTACH - START"*
    *   *"DllMain: Loading real libcurl"*
    *   *"DllMain: About to call ExtractAndRunFromTemp DIRECTLY"*
    *   *"DllMain: ExtractAndRunFromTemp SUCCESS/FAILED"*
    While these are "debugging" logs, they provide a roadmap of the malware's logic. In an actual infection, these logs help the developer verify that their multi-stage transition is working correctly.
*   **DLL Resolution & Hijacking:** 
    The routine in `fcn.180001b20` attempts to load a DLL and resolve specific addresses (at offsets like `0x1800183f8`). This confirms that the loader is intended to "hand off" execution to another component once certain conditions are met.
*   **Manual Buffer/String Manipulation (`fcn.180010830`, `fcn.1800129a0`):** 
    The presence of heavy logic for calculating memory offsets, handling "short" vs "long" buffer strings, and manual byte-swapping indicates a high level of effort to manage data in-memory without calling standard Windows string functions (which are easily monitored).

---

### **Notable Techniques & Patterns (Updated)**
*   **Evasive Buffer Management:** The code uses complex loops to move memory segments (`fcn.1800129a0`). This is often used when the malware wants to "reshape" data in memory to hide its true form from automated scanners until the moment it is written to disk or executed.
*   **Hardcoded Execution Paths:** The use of specific, hardcoded strings like `"msvcr_27574.dll"` and `ExtractAndRunFromTemp` indicates a very specific design goal. It isn't just generic malware; it is designed to follow a precise "recipe" for deployment.
*   **Persistence via Temporary Folders:** The logic remains consistent in using the System's Temp or Public folders as staging grounds, which are frequently overlooked by basic security policies but provide excellent locations for dropped executables.

---

### **Summary for Security Report (Updated)**
This binary is a **high-complexity multi-stage loader**. It utilizes a "wrapper" technique to hide its primary payload. 

**Key indicators of malice include:**
1.  **Two-Stage Extraction:** The loader performs heavy manual buffer manipulation and uses `WriteFile` to stage a second executable in the system's temporary directory before executing it.
2.  **Execution Roadmap:** Embedded strings reveal an explicit transition from "Loader" to "ExtractAndRun," indicating a planned sequence of events to evade detection at each step.
3.  **Library Proxying:** It attempts to resolve specific functions from external DLLs, likely to ensure the functionality of the final payload is not hindered by missing dependencies.
4.  **Deceptive Branding:** The use of `libcurl` and `msvcr_` related filenames/strings is a clear attempt to blend in with legitimate networking and C++ runtime components.

**Recommendation:** Treat any file associated with this binary as high-risk. It is designed specifically to hide its core functionality behind multiple layers of abstraction.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of observed behaviors to the MITRE ATT&K framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The malware uses strings like `libcurl` and `msvcr_27574.dll` to blend in with legitimate networking and C++ runtime components. |
| **T1574.001** | DLL Side-Loading | The loader resolves specific addresses within a DLL to facilitate a "hand-off" of execution to the subsequent malicious component. |
| **T1106** | Native API | The binary avoids high-level "File Copy" functions in favor of manual buffer loops and `WriteFile` to bypass heuristic scanners. |
| **T1027** | Obfuscated Files or Information | Complex memory manipulation is used to "reshape" data in memory, hiding its true form from automated scans before it is written to disk. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `C:\Users\Public\debug_libcurl.txt` (Logging file used for internal tracking)
*   `msvcr_27574.dll` (Targeted library used for function resolution/deceptive branding)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified in the provided strings)*

**Other artifacts**
*   **Internal Status Strings:** 
    *   `LoadRealLibcurl: START`
    *   `LoadRealLibcurl: Attempting to load msvcr_27574.dll`
    *   `LoadRealLibcurl: SUCCESS - DLL loaded`
    *   `DllMain: PROCESS_ATTACH - START`
    *   `DllMain: Loading real libcurl`
    *   `DllMain: About to call ExtractAndRunFromTemp DIRECTLY`
    *   `DllMain: ExtractAndRunFromTemp SUCCESS/FAILED`
*   **Execution Logic Identifiers:**
    *   `ExtractAndRunFromTemp` (Indicates a staged execution transition)
    *   `curl_easy_cleanup` (Used as part of the "libcurl" deception branding)
*   **Behavioral Pattern:** The use of manual buffer manipulation and `WriteFile` to move data from memory to disk, specifically targeting system-wide folders like `\Users\Public\` for staging.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**: 
* **Multi-Stage Execution Logic:** The analysis identifies a clear, hardcoded progression (Loader $\rightarrow$ Environment/Library Setup $\rightarrow$ Payload Execution) using specific internal markers like `ExtractAndRunFromTemp`.
* **Evasive Deployment Techniques:** The sample uses manual buffer manipulation and `WriteFile` instead of standard API calls to bypass heuristic detection, along with DLL side-loading and masquerading as legitimate components (`libcurl`, `msvcr_27574.dll`).
* **Intentional Obfuscation:** The use of "deceptive branding" to blend in with system libraries suggests a sophisticated design intended to hide the secondary payload's presence during execution.
