# Threat Analysis Report

**Generated:** 2026-08-06 22:07 UTC
**Sample:** `0d9211f55a021885ce606126013fc3e1e0b0090ffa8c1596ed7d7ba509d8e5d5_0d9211f55a021885ce606126013fc3e1e0b0090ffa8c1596ed7d7ba509d8e5d5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d9211f55a021885ce606126013fc3e1e0b0090ffa8c1596ed7d7ba509d8e5d5_0d9211f55a021885ce606126013fc3e1e0b0090ffa8c1596ed7d7ba509d8e5d5.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 451,584 bytes |
| MD5 | `5adc623817f16fde8c2afe2d92dd2938` |
| SHA1 | `940b02ba3a8c226c700d61c558acaef1dc93dbaf` |
| SHA256 | `0d9211f55a021885ce606126013fc3e1e0b0090ffa8c1596ed7d7ba509d8e5d5` |
| Overall entropy | 4.712 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767149535 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 431,104 | 4.649 | No |
| `.rdata` | 11,264 | 4.523 | No |
| `.data` | 5,632 | 7.534 | ⚠️ Yes |
| `.pdata` | 2,048 | 7.016 | ⚠️ Yes |
| `.gehcont` | 512 | 0.143 | No |

### Imports

**KERNEL32.dll**: `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `GetProcAddress`, `GetModuleHandleA`, `VirtualQuery`, `GetModuleHandleExW`, `FreeLibrary`, `GetModuleHandleW`, `IsProcessorFeaturePresent`, `GetStartupInfoW`, `SetUnhandledExceptionFilter`, `UnhandledExceptionFilter`, `QueryPerformanceCounter`, `UpdateProcThreadAttribute`
**ntdll.dll**: `RtlVirtualUnwind`, `RtlLookupFunctionEntry`, `RtlCaptureContext`, `DbgUiSetThreadDebugObject`, `RtlAllocateHeap`, `NtRemoveProcessDebug`, `NtQueryInformationProcess`, `RtlFreeHeap`, `NtClose`, `__C_specific_handler`, `memset`, `wcslen`, `memcpy`, `memmove`, `NtDuplicateObject`
**RPCRT4.dll**: `NdrAsyncClientCall`, `RpcRaiseException`, `RpcAsyncCompleteCall`, `RpcBindingFromStringBindingW`, `RpcStringFreeW`, `RpcBindingFree`, `RpcBindingSetAuthInfoExW`, `RpcAsyncInitializeHandle`, `RpcStringBindingComposeW`
**msvcrt.dll**: `?terminate@@YAXXZ`, `__getmainargs`, `__set_app_type`, `_XcptFilter`, `strlen`, `strcpy_s`, `_msize`, `_initterm_e`, `_initterm`, `_callnewh`, `_time64`, `rand`, `srand`, `realloc`, `wcscpy_s`
**ADVAPI32.dll**: `CreateWellKnownSid`, `CreateProcessAsUserW`
**SHELL32.dll**: `ShellExecuteExA`

## Extracted Strings

Total strings found: **477** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.gehcont
$H;D$0s&H
;D$}8H
HcT$(H
HcL$(H
q>&*s~&*hU`+D
qbfBq|$
s~&DcU`;B
qOfBQKZ
n7Q4El
4a	i/q~#
~&9q~&
b/Q~&B
n&q~&&
>&=q~&
Ka}h/Q~!
qC&BoP
ExitProcess
GetModuleHandleA
GetModuleHandleW
GetProcAddress
LoadLibraryA
KERNEL32.dll
HqGags`olx[~h}j~e
!&)*8;/8?
;)64 S
rogo77(cde

3-7!&2
!;>>-!
*=> *T
C}bNwoLL&
"|	]14
[0IU
~
RZ(0>L
(7D4#/
y@@1(M
1Q@eWs
Z|C=@3
M!t_w,BgN
DO ;o\
O-a$`
I.(|K/
9>|AE|m

M=pH
H<ON&@
h[	$34
)Hw@ sQ
5F;P5J
w|IvU|A
|aDq?7
c,S02

"yW
 A
s92V[c
lu.n,M
A^Zw:<
[\x5(U
vI(
md
A"r#Rf
 y7K>@1
rTb7%

`@XFq]
=s	cxO
V&GV.B#
pYpJe1HC
D#T"o
 kv#,w
s_Tf4
15:$N^
z:<S[IL
cWA;~
A?3kf1=I
p@i!/
r@l7z
F_ESR/
\^EOuuBc

Mf:'~4
xNYQ~E
9}yY1N
wEDp"D
RBaX%E
]vbXoW
5voD>O
[mx *u'
x9$l"=
TPOa50
>R$cBE
]uewc%
h:nuN{P
oRZkF;v
<	}G,~
nvZEO3
HzEG$v
;>=MwDk
)L65v8q
nf~X#!
:?&g~z
```

## Disassembly Overview

Functions analyzed: **25** | Decompiled to C: **25**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140008da0` | `0x140008da0` | 16025 | ✓ |
| `fcn.140005060` | `0x140005060` | 15276 | ✓ |
| `fcn.14000ccc0` | `0x14000ccc0` | 15201 | ✓ |
| `fcn.140001200` | `0x140001200` | 15143 | ✓ |
| `fcn.140004f00` | `0x140004f00` | 345 | ✓ |
| `fcn.140008c90` | `0x140008c90` | 266 | ✓ |
| `fcn.140004e50` | `0x140004e50` | 163 | ✓ |
| `fcn.140004db0` | `0x140004db0` | 157 | ✓ |
| `fcn.140001010` | `0x140001010` | 109 | ✓ |
| `fcn.140004d30` | `0x140004d30` | 62 | ✓ |
| `fcn.140008c50` | `0x140008c50` | 62 | ✓ |
| `fcn.140008c10` | `0x140008c10` | 60 | ✓ |
| `fcn.140010870` | `0x140010870` | 53 | ✓ |
| `fcn.140004d70` | `0x140004d70` | 51 | ✓ |
| `fcn.14000cc40` | `0x14000cc40` | 51 | ✓ |
| `fcn.14000cc80` | `0x14000cc80` | 51 | ✓ |
| `fcn.140010830` | `0x140010830` | 51 | ✓ |
| `fcn.1400108b0` | `0x1400108b0` | 34 | ✓ |
| `entry0` | `0x140001000` | 15 | ✓ |
| `fcn.140010950` | `0x140010950` | 3 | ✓ |
| `fcn.140010960` | `0x140010960` | 3 | ✓ |
| `fcn.140010970` | `0x140010970` | 3 | ✓ |
| `fcn.140010980` | `0x140010980` | 3 | ✓ |
| `fcn.140010990` | `0x140010990` | 3 | ✓ |
| `fcn.1400109a0` | `0x1400109a0` | 3 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001010.c`](code/fcn.140001010.c)
- [`code/fcn.140001200.c`](code/fcn.140001200.c)
- [`code/fcn.140004d30.c`](code/fcn.140004d30.c)
- [`code/fcn.140004d70.c`](code/fcn.140004d70.c)
- [`code/fcn.140004db0.c`](code/fcn.140004db0.c)
- [`code/fcn.140004e50.c`](code/fcn.140004e50.c)
- [`code/fcn.140004f00.c`](code/fcn.140004f00.c)
- [`code/fcn.140005060.c`](code/fcn.140005060.c)
- [`code/fcn.140008c10.c`](code/fcn.140008c10.c)
- [`code/fcn.140008c50.c`](code/fcn.140008c50.c)
- [`code/fcn.140008c90.c`](code/fcn.140008c90.c)
- [`code/fcn.140008da0.c`](code/fcn.140008da0.c)
- [`code/fcn.14000cc40.c`](code/fcn.14000cc40.c)
- [`code/fcn.14000cc80.c`](code/fcn.14000cc80.c)
- [`code/fcn.14000ccc0.c`](code/fcn.14000ccc0.c)
- [`code/fcn.140010830.c`](code/fcn.140010830.c)
- [`code/fcn.140010870.c`](code/fcn.140010870.c)
- [`code/fcn.1400108b0.c`](code/fcn.1400108b0.c)
- [`code/fcn.140010950.c`](code/fcn.140010950.c)
- [`code/fcn.140010960.c`](code/fcn.140010960.c)
- [`code/fcn.140010970.c`](code/fcn.140010970.c)
- [`code/fcn.140010980.c`](code/fcn.140010980.c)
- [`code/fcn.140010990.c`](code/fcn.140010990.c)
- [`code/fcn.1400109a0.c`](code/fcn.1400109a0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and extended the analysis. The new data confirms the earlier suspicions and reveals a much more complex internal structure typical of high-end commercial packers or advanced malware loaders.

### Updated Analysis Report

#### 1. Core Functionality and Purpose
The binary is confirmed to be a **multi-stage execution stub/packer**. Its primary role is to act as a "gatekeeper." It performs several critical tasks before the actual payload is allowed to run:
*   **Massive Data Decryption:** The extremely long function `fcn.140001200` appears to be a large loop designed to decrypt or de-obfuscate a significant internal data structure (likely an encrypted string table, configuration block, or the actual payload's entry point logic).
*   **Environment/Integrity Checks:** The logic in `fcn.1400108b0` suggests a "pass/fail" gate; if the decryption of the internal components fails or is tampered with (detected by the math-heavy opaque predicates), the program calls `ExitProcess`, preventing the payload from ever reaching memory.
*   **Dynamic API Environment Setup:** The functions `fcn.140004f00` and `fcn.140008c90` are dedicated to building a "hidden" table of resolved function pointers, allowing the program to call system APIs without them appearing in the Import Address Table (IAT).

#### 2. Suspicious or Malicious Behaviors
*   **Anti-Analysis via Integrity Gates:** The repeated use of `ExitProcess` following complex mathematical checks indicates that the loader is checking for "correct" execution paths. If a debugger's presence or an analyst’s modification of the code changes the result of these calculations, the process terminates immediately.
*   **Advanced Memory Manipulation:** Functions like `fcn.140004db0` and `fcn.140001010` are used to move/shift memory blocks. This is often seen in **"In-Memory Unpacking,"** where the payload's size or location in memory is changed dynamically to evade scanners that look for specific signatures at fixed offsets.
*   **Delayed Execution / Junk Loop Padding:** The sheer volume of code in `fcn.140001200` that involves repetitive mathematical logic serves two purposes: it exhausts the analyst's time and creates a massive "dead zone" in the disassembly to hide the transition between the loader and the actual malicious payload.

#### 3. Notable Techniques or Patterns
*   **Automated API Resolver (Custom IAT):** `fcn.140004f00` is a classic implementation of an **API Resolver**. It iterates through a list of encrypted strings, resolves them using `GetProcAddress`, and stores the resulting pointers in a table. The bitwise check (`& 0x8000...`) suggests it can handle both standard API names and "obfuscated" names (where the first byte is modified to hide the true name).
*   **XOR/Bitwise Transformation:** `fcn.140004e50` performs a loop-based transformation using an XOR operation and addition (`^ ... + uStack_20`). This is a standard method for **de-obfuscating strings or data blocks** in-memory immediately before use.
*   **Code Flattening / Control Flow Obfuscation:** The structure of `fcn.140001200` (with many nearly identical branches and repeated logic) suggests "Control Flow Flattening." This is a common technique used by protectors like **VMProtect or Themida** to break the linear flow of code, making it incredibly difficult for an analyst to follow the logical progression of the program.
*   **Stub/Gadget Functions:** The numerous small functions (e.g., `fcn.140010950`, `fcn.140010960`) that return constant values are likely **"junk" or "filler" code**. These are often generated by compilers when a program is intentionally obfuscated to break the decompiler’s ability to merge consecutive instructions into coherent logic.

#### 4. Summary of Logic Flow (Revised)
1.  **Entry:** The program starts at `entry0` $\rightarrow$ `fcn.1400108b0`.
2.  **Stage 1 (Decryption):** It enters the massive `fcn.140001200` routine, which processes large blocks of data using heavy mathematical gates to ensure "correct" decryption.
3.  **Stage 2 (Environment Prep):** The code calls `fcn.140008c90`, which invokes the API resolver (`fcn.140004f00`) to populate a custom function table.
4.  **Stage 3 (Payoff):** Once the internal state is "validated" and the APIs are resolved, the code jumps to the de-obfuscated payload (the actual malware).

### Conclusion for Security Context
This sample is a **sophisticated packer/loader**. The primary goal of this specific binary is to **protect the payload's signature.** It uses high-level obfuscation techniques (Control Flow Flattening, Opaque Predicates, and Custom IAT) to hide its true intentions from automated analysis tools and human researchers. If this sample is part of a malware campaign, the "real" malicious behavior (e.g., keylogging, data exfiltration, or ransomware encryption) is likely hidden inside the payload that only exists in memory after the long decryption loops are completed.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1137** | Software Packing | The binary functions as a multi-stage execution stub/packer designed to hide the primary payload from detection. |
| **T1027** | Obfuscated Files or Information | The use of XOR transformations, Control Flow Flattening, and junk loop padding is intended to hinder manual and automated analysis. |
| **T1497** | Virtualization/Sandbox Detection | The "integrity gates" and opaque predicates are designed to detect the presence of debuggers or analyst interference and terminate the process. |
| **T1036** | Masquerading | (Optional context) While not explicitly a "masquerade," the use of a custom IAT is a specific technique to hide the true functional capabilities of the code from static analysis tools. |

***Note for Analyst:** In most reporting contexts, T1027 and T1137 are the primary techniques for this behavior. T1497 is specifically mapped here because the "integrity gates" described are a direct method to identify and evade analysis environments.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: `KERNEL32.dll` was detected in the strings but is a standard Windows system library and has been excluded as a false positive.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Internal Function Offsets (Behavioral Indicators):** While not traditional network IOCs, the following internal offsets are used for tracking specific malicious logic within the packer:
    *   `fcn.140001200` (Massive data decryption/de-obfuscation loop)
    *   `fcn.1400108b0` (Integrity gate/Anti-analysis check)
    *   `fcn.140004f00` (Custom API Resolver)
    *   `fcn.140008c90` (Hidden table construction)
    *   `fcn.140004db0` / `fcn.140001010` (In-memory unpacking/memory shifting)
    *   `fcn.140004e50` (XOR/Bitwise transformation logic)
*   **Malware Techniques:**
    *   Custom IAT (Import Address Table) construction to hide API calls.
    *   Control Flow Flattening and Opaque Predicates (used for anti-analysis).
    *   In-Memory Unpacking (payload exists only in memory after the decryption phase).

---
**Analyst Note:** The sample is a sophisticated packer/loader. Because it utilizes heavy obfuscation (like those seen in VMProtect or Themida), there are no static network indicators (IPs/Domains) present in the initial stage. The "true" malicious activity remains hidden until the decryption loops (`fcn.140001200`) and API resolutions are complete.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    * **Multi-stage Unpacking:** The binary functions as a "gatekeeper" utilizing heavy decryption loops and in-memory unpacking to hide a secondary payload from static analysis.
    * **Advanced Anti-Analysis:** It employs high-level obfuscation techniques such as Control Flow Flattening, Opaque Predicates (integrity gates), and Junk Loop Padding to exhaust analyst time and bypass automated detection.
    * **Stealthy Execution:** The use of a custom IAT (Import Address Table) and XOR/Bitwise transformations ensures that the program's true functionality and API calls are not visible until execution reaches a specific point in memory.
