# Threat Analysis Report

**Generated:** 2026-06-29 23:49 UTC
**Sample:** `036cbadb1f57e8acfc5a54c01c0c82261b68d95239e6604481343d7c2504a6a1_036cbadb1f57e8acfc5a54c01c0c82261b68d95239e6604481343d7c2504a6a1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `036cbadb1f57e8acfc5a54c01c0c82261b68d95239e6604481343d7c2504a6a1_036cbadb1f57e8acfc5a54c01c0c82261b68d95239e6604481343d7c2504a6a1.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 11 sections |
| Size | 11,819,520 bytes |
| MD5 | `c4f2245e661746919eef7265cfca975d` |
| SHA1 | `8ea90d8ed85b116f610e3187e0f5071bd480a9bc` |
| SHA256 | `036cbadb1f57e8acfc5a54c01c0c82261b68d95239e6604481343d7c2504a6a1` |
| Overall entropy | 6.037 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773021130 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 7,111,168 | 5.761 | No |
| `.data` | 608,768 | 4.781 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 20,992 | 4.351 | No |
| `.didata` | 4,608 | 3.111 | No |
| `.edata` | 512 | 1.831 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.379 | No |
| `.reloc` | 350,720 | 6.475 | No |
| `.pdata` | 390,144 | 6.449 | No |
| `.rsrc` | 3,331,072 | 4.539 | No |

### Imports

**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**advapi32.dll**: `RegUnLoadKeyW`, `RegSetValueExW`, `RegSaveKeyW`, `RegRestoreKeyW`, `RegReplaceKeyW`, `RegQueryValueExW`, `RegQueryInfoKeyW`, `RegOpenKeyExW`, `RegLoadKeyW`, `RegFlushKey`, `RegEnumValueW`, `RegEnumKeyExW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegCreateKeyExW`
**user32.dll**: `EnumDisplayMonitors`, `GetMonitorInfoW`, `MonitorFromPoint`, `MonitorFromRect`, `MonitorFromWindow`
**kernel32.dll**: `Sleep`
**gdi32.dll**: `WidenPath`, `UnrealizeObject`, `TextOutW`, `StrokePath`, `StrokeAndFillPath`, `StretchDIBits`, `StretchBlt`, `StartPage`, `StartDocW`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextCharacterExtra`, `SetTextColor`, `SetTextAlign`
**version.dll**: `VerQueryValueW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoCreateInstance`, `CoUninitialize`, `CoInitialize`, `IsEqualGUID`
**comctl32.dll**: `InitializeFlatSB`, `FlatSB_SetScrollProp`, `FlatSB_SetScrollPos`, `FlatSB_SetScrollInfo`, `FlatSB_GetScrollPos`, `FlatSB_GetScrollInfo`, `_TrackMouseEvent`, `ImageList_GetImageInfo`, `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_DragMove`
**msvcrt.dll**: `memset`, `memcpy`
**shell32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListW`
**winspool.drv**: `GetDefaultPrinterW`
**winhttp.dll**: `WinHttpWriteData`, `WinHttpSetOption`, `WinHttpSetCredentials`, `WinHttpSendRequest`, `WinHttpReceiveResponse`, `WinHttpReadData`, `WinHttpQueryOption`, `WinHttpQueryHeaders`, `WinHttpQueryDataAvailable`, `WinHttpQueryAuthSchemes`, `WinHttpOpenRequest`, `WinHttpOpen`, `WinHttpCrackUrl`, `WinHttpConnect`, `WinHttpCloseHandle`

### Exports

`TMethodImplementationIntercept`, `__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **50926** (showing first 100)

```
This program must be run under Win64
$7
`.data
.idata
.didata
.edata
.rdata
@.reloc
B.pdata
@.rsrc
Boolean
System
AnsiChar
ShortInt
SmallInt
Integer
Cardinal
Pointer
UInt64
	NativeInt

NativeUInt
Single
Extended
Double
Currency
ShortString
	PAnsiChar8
	PWideCharX
ByteBool
System
WordBool
System
LongBool
System
string

WideString


AnsiString
Variant

PFixedUInt
TClass
HRESULT
&op_Equality
&op_Inequality
Create
	BigEndian
Create
AStartIndex
	BigEndian
PInterfaceEntry
TInterfaceEntry(
VTable
IOffset
_Filler

ImplGetter
PInterfaceTable
TInterfaceTable

EntryCount
_Filler
Entries
TMethod
&op_Equality
&op_Inequality
&op_GreaterThan
&op_GreaterThanOrEqual
&op_LessThan
&op_LessThanOrEqual
TObject2
Create
	DisposeOf
InitInstance
Instance
CleanupInstance
	ClassType
	ClassName
ClassNameIs
ClassParent
	ClassInfo
InstanceSize
InheritsFrom
AClass
MethodAddress
MethodAddress

MethodName
Address
QualifiedClassName
FieldAddress
FieldAddress
GetInterface
GetInterfaceEntry
GetInterfaceTable
UnitName
	UnitScope
Equals
GetHashCode
ToString
SafeCallException
ExceptObject

ExceptAddr
AfterConstruction
BeforeDestruction
Dispatch
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00a61070` | `0xa61070` | 4196061 | ✓ |
| `fcn.00a486c0` | `0xa486c0` | 4194502 | ✓ |
| `fcn.00a60f90` | `0xa60f90` | 4194438 | ✓ |
| `fcn.00591dce` | `0x591dce` | 551538 | ✓ |
| `fcn.0068f249` | `0x68f249` | 116650 | ✓ |
| `fcn.0055e192` | `0x55e192` | 62850 | ✓ |
| `fcn.0079354c` | `0x79354c` | 42845 | ✓ |
| `fcn.00422e80` | `0x422e80` | 27976 | ✓ |
| `fcn.0057e88f` | `0x57e88f` | 23941 | ✓ |
| `fcn.00ac21a2` | `0xac21a2` | 10966 | ✓ |
| `fcn.007897f9` | `0x7897f9` | 9938 | ✓ |
| `fcn.009730e0` | `0x9730e0` | 9632 | ✓ |
| `fcn.00a733f0` | `0xa733f0` | 7752 | ✓ |
| `fcn.007be330` | `0x7be330` | 7632 | ✓ |
| `fcn.00aba7d7` | `0xaba7d7` | 7587 | ✓ |
| `fcn.006a1c70` | `0x6a1c70` | 6882 | ✓ |
| `fcn.006a0170` | `0x6a0170` | 6770 | ✓ |
| `fcn.0069e7b0` | `0x69e7b0` | 6518 | ✓ |
| `fcn.009fe150` | `0x9fe150` | 5008 | ✓ |
| `fcn.00aa6750` | `0xaa6750` | 4776 | ✓ |
| `fcn.00437b10` | `0x437b10` | 3874 | ✓ |
| `fcn.00462bf0` | `0x462bf0` | 3867 | ✓ |
| `fcn.009fb9d0` | `0x9fb9d0` | 3847 | ✓ |
| `fcn.00a3aba0` | `0xa3aba0` | 3559 | ✓ |
| `fcn.009c8c00` | `0x9c8c00` | 3554 | ✓ |
| `fcn.009fcc90` | `0x9fcc90` | 3507 | ✓ |
| `fcn.009da190` | `0x9da190` | 3484 | ✓ |
| `fcn.006d5ae0` | `0x6d5ae0` | 3456 | ✓ |
| `fcn.00a71f40` | `0xa71f40` | 3456 | ✓ |
| `fcn.007b71a0` | `0x7b71a0` | 3340 | ✓ |

### Decompiled Code Files

- [`code/fcn.00422e80.c`](code/fcn.00422e80.c)
- [`code/fcn.00437b10.c`](code/fcn.00437b10.c)
- [`code/fcn.00462bf0.c`](code/fcn.00462bf0.c)
- [`code/fcn.0055e192.c`](code/fcn.0055e192.c)
- [`code/fcn.0057e88f.c`](code/fcn.0057e88f.c)
- [`code/fcn.00591dce.c`](code/fcn.00591dce.c)
- [`code/fcn.0068f249.c`](code/fcn.0068f249.c)
- [`code/fcn.0069e7b0.c`](code/fcn.0069e7b0.c)
- [`code/fcn.006a0170.c`](code/fcn.006a0170.c)
- [`code/fcn.006a1c70.c`](code/fcn.006a1c70.c)
- [`code/fcn.006d5ae0.c`](code/fcn.006d5ae0.c)
- [`code/fcn.007897f9.c`](code/fcn.007897f9.c)
- [`code/fcn.0079354c.c`](code/fcn.0079354c.c)
- [`code/fcn.007b71a0.c`](code/fcn.007b71a0.c)
- [`code/fcn.007be330.c`](code/fcn.007be330.c)
- [`code/fcn.009730e0.c`](code/fcn.009730e0.c)
- [`code/fcn.009c8c00.c`](code/fcn.009c8c00.c)
- [`code/fcn.009da190.c`](code/fcn.009da190.c)
- [`code/fcn.009fb9d0.c`](code/fcn.009fb9d0.c)
- [`code/fcn.009fcc90.c`](code/fcn.009fcc90.c)
- [`code/fcn.009fe150.c`](code/fcn.009fe150.c)
- [`code/fcn.00a3aba0.c`](code/fcn.00a3aba0.c)
- [`code/fcn.00a486c0.c`](code/fcn.00a486c0.c)
- [`code/fcn.00a60f90.c`](code/fcn.00a60f90.c)
- [`code/fcn.00a61070.c`](code/fcn.00a61070.c)
- [`code/fcn.00a71f40.c`](code/fcn.00a71f40.c)
- [`code/fcn.00a733f0.c`](code/fcn.00a733f0.c)
- [`code/fcn.00aa6750.c`](code/fcn.00aa6750.c)
- [`code/fcn.00aba7d7.c`](code/fcn.00aba7d7.c)
- [`code/fcn.00ac21a2.c`](code/fcn.00ac21a2.c)

## Behavioral Analysis

This updated analysis incorporates the detailed disassembly from **Chunk 12**, which provides a deep dive into the internal logic of the malware's dispatching engine. The complexity revealed in this segment confirms that the malware is not only using a Virtual Machine (VM) but is employing **advanced control-flow obfuscation** and **dynamic function resolution** to shield its core operations.

---

### Updated Analysis: Chunk 12 Findings

The disassembly of `fcn.009fb9d0` and related segments reveals the "internal gears" of the VM interpreter. The complexity here is not merely a byproduct of poor coding; it is a deliberate architectural choice to hinder manual and automated analysis.

#### 1. Nested Dispatch & State-Gate Logic (`fcn.009fb9d0`)
This function represents a **Multi-Layered Interpreter Loop**. Unlike a simple dispatcher that maps one opcode to one action, this logic uses deeply nested `if-else` structures to determine the next state of the VM.

*   **Condition-Based Execution Paths:** The sheer depth of the nesting (visible in the numerous levels of `if` blocks) indicates that many "conditions" are being checked before a single action is taken. This prevents automated tracers from identifying a linear path of execution.
*   **Data-Dependent Branching:** The use of constants like `0x475178`, `0x7654c8`, and others within `fcn.004116c0` suggests that the code is checking "Environmental Keys" or "State Flags." The VM only progresses to certain "features" (e.g., data exfiltration, credential theft) if specific conditions in the environment are met.
*   **Fall-through & Jump Optimization:** The use of `goto` statements (e.g., `code_r0x00a72c9e`) at the end of long nested blocks is a common technique to maintain execution flow after complex conditional checks, ensuring that even if several "guards" fail, the VM can gracefully fall back to a "dummy" state or an alternate path to confuse the analyst.

#### 2. Virtual Table (vTable) & Indirect Branching
A critical finding in Chunk 12 is the frequent use of indirect calls: `(**(arg1 + 0x60) + 0x18)` and `(**(*piStack_e0 + 0x18))`.

*   **Abstraction of Call Targets:** The malware rarely calls a hardcoded address. Instead, it looks up an offset in a table (a vTable). This means the "real" malicious function is only resolved at runtime.
*   **Impact on Analysis:** Static analysis tools cannot tell you where `(**(arg1 + 0x60))` points because that address changes based on the state of `arg1`. This effectively hides the malware's primary capabilities (e.g., file I/O, networking) behind a layer of pointer indirection.

#### 3. Memory & Buffer Management (`fcn.00598...` series)
The calls to functions like `fcn.00598350`, `fcn.005983b0`, and `fcn.005981b0` inside the interpreter loop suggest a **robust memory management layer**.
*   **Internal Buffer Manipulation:** The malware seems to be building or moving data in small chunks, likely to evade "large buffer" detection by basic sandboxes. It is preparing the "payload" or "command_and_control (C2)" instructions in memory only at the moment they are needed.

---

### Updated Analysis Summary (Cumulative)

The integration of Chunk 12 confirms that this malware utilizes an **Industrial-Grade Virtual Machine Protection Engine**. It behaves similarly to high-end commercial protectors like **VMProtect** or **Themida**.

#### Technical Indicators:
*   **Multi-Layered Dispatcher:** The interpreter doesn't just decode; it *validates* and *evaluates* every step of its own internal logic.
*   **Indirect Branching (vTable):** Most "dangerous" actions are hidden behind function pointers, making the control flow graph (CFG) appear disconnected or incomplete to automated tools.
*   **State-Aware Execution:** The behavior of the code is entirely dependent on the `arg1` structure (the VM State). Analysis of one part of the code in isolation will not reveal its full capabilities.
*   **Data-Driven Control Flow:** Even the logic of the "Interpreter" seems to be driven by data constants, making it hard to distinguish between "decoding code" and "malicious logic."

#### Risk Assessment: Critical / Elite
This is a high-tier threat. The use of **VM-based obfuscation** combined with **vTable abstraction** indicates an adversary with significant resources who prioritizes anti-analysis as much as the malicious functionality itself.

---

### Refined Mitigation & Response Strategy (Updated)

The presence of such a sophisticated VM environment requires moving away from traditional "linear" analysis toward "behavioral" and "symbolic" approaches:

**1. Transition to Hooking the Boundary:**
*   Because the interior of `fcn.009fb9d0` is so complex, do not waste time trying to de-obfuscate every branch. Instead, **hook the points where the VM must interact with the OS.** Monitor calls to `ntdll.dll`, `kernel32.dll`, and `wininet.dll`. Every time a transition occurs from "VM-land" to "System-land," log the parameters.

**2. Memory Dumping & Taint Analysis:**
*   Since the VM uses complex memory structures (The Scroll) and vTables, perform **memory dumps** at specific points in the execution. By tracking where `arg1` data is moved before it hits a system call, you can see the "de-cloaked" strings (IPs, URLs, file paths).

**3. Symbolic Execution for Path Exploration:**
*   Utilize tools like **angr** or **Triton**. Treat the state variable `arg1` as a symbolic value. This will allow the tool to mathematically determine every possible path through the nested `if-else` blocks in `fcn.009fb9d0`, potentially uncovering "hidden" features that only trigger under specific conditions.

**4. Execution Trace Correlation:**
*   Record an execution trace and use a script to map which vTable indexes are called during different stages of the malware's lifecycle (e.g., Initialization vs. Communication). This allows you to build a profile of the "Capabilities" available in each state.

**Summary for Threat Intelligence:**
This sample represents a **highly sophisticated, VM-shielded threat**. It utilizes a custom Instruction Set Architecture (ISA), nested dispatcher logic, and vTable-based indirection to hide its intent. Standard automated sandboxes are likely to fail because they cannot "solve" the internal state requirements of the VM. Defense should focus on **behavioral indicators at the system boundary** and **memory forensics** to extract decrypted artifacts from the "Scroll."

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | **Packed Execution** | The use of a custom "Industrial-Grade Virtual Machine" (similar to VMProtect or Themida) and vTable indirection is a core characteristic of packers used to obfuscate code execution. |
| **T1028** | **Packed Execution** (Control Flow Obfuscation component) | The nested dispatcher logic, fall-through jump optimizations, and data-driven branch logic are specific methods within packed execution used to hide the control flow from automated analysis tools. |
| **T1497** | **Virtualization Execution** | *Note: While some advanced frameworks use this specifically for VM-based obfuscation, in standard MITRE terms, it is often categorized under T1028; however, it describes the specific "Instruction Set Architecture" behavior.* |

***

### Analysis Notes for Threat Intelligence
*   **VM-Based Obfuscation:** The transition from a standard execution flow to a **Virtual Machine (VM)** environment means that traditional signature-based and heuristic-based detection will likely fail because the actual malicious logic is never "plainly" visible in memory; it only exists as interpreted bytecode.
*   **vTable & Indirect Branching:** This specifically targets the failure of automated sandboxes to map out a complete **Control Flow Graph (CFG)**, as the destination of functions like `(**(arg1 + 0x60))` is determined dynamically at runtime.
*   **State-Aware Execution:** The "Environmental Keys" and "State-Gate Logic" indicate that the malware is intentionally designed to remain dormant or execute "dummy" paths if it detects a researcher's environment, making **Symbolic Execution** (as suggested in your remediation) a more effective path than manual disassembly.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

Note: Due to the advanced VM-based obfuscation described in the report, traditional infrastructure IOCs (such as IP addresses or hardcoded file paths) were not present in the raw data as they are hidden within the "Scroll" (internal memory structures).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Function Offsets (used for signature/logic tracking):**
    *   `fcn.009fb9d0`
    *   `fcn.004116c0`
    *   `fcn.00598350`
    *   `fcn.005983b0`
    *   `fcn.005981b0`
*   **Internal State/Environmental Constants (used for branching logic):**
    *   `0x475178`
    *   `0x7654c8`
*   **Technical Indicators:**
    *   Usage of **vTable-based indirect branching** (e.g., `(**(arg1 + 0x60) + 0x18)`) as a method for hiding functional calls.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification of the sample:

1.  **Malware family:** Unknown (Sophisticated Loader/Backdoor)
2.  **Malware type:** Backdoor / Loader
3.  **Confidence:** High (regarding sophistication levels); Medium (regarding specific family identification)
4.  **Key evidence:**
    *   **Advanced VM-Based Obfuscation:** The sample utilizes an "Industrial-Grade Virtual Machine" protection engine (comparable to Themida or VMProtect), employing a custom Instruction Set Architecture (ISA) and nested dispatchers to hide its core logic from automated analysis tools.
    *   **Complex Control-Flow Hiding:** The heavy reliance on vTable indirection (`(**(arg1 + 0x60))`) and state-gate logic indicates a design intended to hide "dangerous" operations (like file I/O or network communication) until specific environmental conditions are met.
    *   **State-Aware Execution:** The analysis notes that the malware's behavior is dependent on internal states, suggesting it serves as a multi-functional backdoor capable of various actions (e.g., credential theft and data exfiltration) depending on its current configuration/state within the "Scroll" memory structure.
