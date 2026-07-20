# Threat Analysis Report

**Generated:** 2026-07-19 15:07 UTC
**Sample:** `09528e1283f797f4145e746771ada5417a9aa73ec32945fd78afb437700c9563_09528e1283f797f4145e746771ada5417a9aa73ec32945fd78afb437700c9563.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09528e1283f797f4145e746771ada5417a9aa73ec32945fd78afb437700c9563_09528e1283f797f4145e746771ada5417a9aa73ec32945fd78afb437700c9563.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 11 sections |
| Size | 4,559,360 bytes |
| MD5 | `90b699d1c60ed22d25476f35b3cfea86` |
| SHA1 | `cb903f08af602a26a513862ff6af37d9b3881111` |
| SHA256 | `09528e1283f797f4145e746771ada5417a9aa73ec32945fd78afb437700c9563` |
| Overall entropy | 6.841 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763557884 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 710,656 | 6.393 | No |
| `.itext` | 6,144 | 6.214 | No |
| `.data` | 16,384 | 5.178 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,608 | 4.773 | No |
| `.didata` | 512 | 2.754 | No |
| `.edata` | 512 | 1.246 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.377 | No |
| `.reloc` | 71,168 | 6.707 | No |
| `.rsrc` | 81,920 | 4.126 | No |

### Imports

**kernel32.dll**: `GetACP`, `GetExitCodeProcess`, `CloseHandle`, `LocalFree`, `SizeofResource`, `VirtualProtect`, `QueryPerformanceFrequency`, `VirtualFree`, `GetFullPathNameW`, `GetProcessHeap`, `ExitProcess`, `HeapAlloc`, `GetCPInfoExW`, `RtlUnwind`, `SetFilePointerEx`
**comctl32.dll**: `InitCommonControls`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `CharLowerBuffW`, `CallWindowProcW`, `CharUpperW`, `PeekMessageW`, `GetSystemMetrics`, `SetWindowLongW`, `MessageBoxW`, `DestroyWindow`, `CharUpperBuffW`, `CharNextW`, `MsgWaitForMultipleObjects`, `LoadStringW`, `ExitWindowsEx`
**oleaut32.dll**: `SafeArrayPutElement`, `VariantInit`, `VariantClear`, `SysFreeString`, `SafeArrayAccessData`, `SysReAllocStringLen`, `SafeArrayCreate`, `SafeArrayGetElement`, `SysAllocStringLen`, `SafeArrayUnaccessData`, `SafeArrayPtrOfIndex`, `VariantCopy`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `VariantChangeType`
**advapi32.dll**: `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `OpenThreadToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `RegOpenKeyExW`, `OpenProcessToken`, `FreeSid`, `AllocateAndInitializeSid`, `EqualSid`, `RegQueryValueExW`, `GetTokenInformation`, `ConvertSidToStringSidW`, `RegCloseKey`

### Exports

`__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **15358** (showing first 100)

```
This program must be run under Win32
$7
`.itext
`.data
.idata
.didata
.edata
.rdata
@.reloc
B.rsrc
Boolean
System
AnsiChar
ShortInt
SmallInt
Integer
Cardinal
Pointer
UInt64
Single
Extended
Double
Currency
ShortString
	PAnsiChar0
	PWideCharL
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

OleVariant
TClassd
HRESULT
&op_Equality
&op_Inequality
Create
	BigEndian
Create
AStartIndex
	BigEndian
IsEmpty
PInterfaceEntry
TInterfaceEntry
VTable
IOffset

ImplGetter
PInterfaceTable
TInterfaceTable

EntryCount
Entries
TMethod
&op_Equality
&op_Inequality
&op_GreaterThan
&op_GreaterThanOrEqual
&op_LessThan
&op_LessThanOrEqual
TObject&
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
Message
DefaultHandler
Message
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0043e80d` | `0x43e80d` | 131727 | ✓ |
| `fcn.0046e8ac` | `0x46e8ac` | 8906 | — |
| `fcn.0045fa59` | `0x45fa59` | 2806 | ✓ |
| `fcn.0041cab4` | `0x41cab4` | 2633 | ✓ |
| `fcn.00404434` | `0x404434` | 2534 | ✓ |
| `fcn.0041e910` | `0x41e910` | 2206 | ✓ |
| `fcn.004a76a0` | `0x4a76a0` | 2192 | ✓ |
| `fcn.0040423c` | `0x40423c` | 1904 | ✓ |
| `fcn.0041fcd8` | `0x41fcd8` | 1849 | ✓ |
| `fcn.00435d2c` | `0x435d2c` | 1642 | ✓ |
| `fcn.0047ec8e` | `0x47ec8e` | 1599 | — |
| `fcn.00403eb8` | `0x403eb8` | 1500 | ✓ |
| `fcn.00480ce9` | `0x480ce9` | 1464 | ✓ |
| `fcn.0042c770` | `0x42c770` | 1302 | ✓ |
| `fcn.00429af0` | `0x429af0` | 1230 | ✓ |
| `fcn.0042a6dc` | `0x42a6dc` | 1201 | ✓ |
| `fcn.00452730` | `0x452730` | 1188 | ✓ |
| `fcn.0042b790` | `0x42b790` | 1181 | ✓ |
| `fcn.0042c090` | `0x42c090` | 1174 | ✓ |
| `fcn.004369ec` | `0x4369ec` | 1174 | ✓ |
| `fcn.0042b170` | `0x42b170` | 1108 | ✓ |
| `fcn.0042f754` | `0x42f754` | 1086 | ✓ |
| `fcn.00404d2c` | `0x404d2c` | 1034 | ✓ |
| `fcn.0041f3d4` | `0x41f3d4` | 1008 | ✓ |
| `fcn.0040e188` | `0x40e188` | 1007 | ✓ |
| `fcn.0046313c` | `0x46313c` | 996 | ✓ |
| `fcn.004308e4` | `0x4308e4` | 987 | ✓ |
| `fcn.0042068c` | `0x42068c` | 977 | ✓ |
| `fcn.00495954` | `0x495954` | 962 | ✓ |
| `fcn.0042d3a4` | `0x42d3a4` | 921 | ✓ |

### Decompiled Code Files

- [`code/fcn.00403eb8.c`](code/fcn.00403eb8.c)
- [`code/fcn.0040423c.c`](code/fcn.0040423c.c)
- [`code/fcn.00404434.c`](code/fcn.00404434.c)
- [`code/fcn.00404d2c.c`](code/fcn.00404d2c.c)
- [`code/fcn.0040e188.c`](code/fcn.0040e188.c)
- [`code/fcn.0041cab4.c`](code/fcn.0041cab4.c)
- [`code/fcn.0041e910.c`](code/fcn.0041e910.c)
- [`code/fcn.0041f3d4.c`](code/fcn.0041f3d4.c)
- [`code/fcn.0041fcd8.c`](code/fcn.0041fcd8.c)
- [`code/fcn.0042068c.c`](code/fcn.0042068c.c)
- [`code/fcn.00429af0.c`](code/fcn.00429af0.c)
- [`code/fcn.0042a6dc.c`](code/fcn.0042a6dc.c)
- [`code/fcn.0042b170.c`](code/fcn.0042b170.c)
- [`code/fcn.0042b790.c`](code/fcn.0042b790.c)
- [`code/fcn.0042c090.c`](code/fcn.0042c090.c)
- [`code/fcn.0042c770.c`](code/fcn.0042c770.c)
- [`code/fcn.0042d3a4.c`](code/fcn.0042d3a4.c)
- [`code/fcn.0042f754.c`](code/fcn.0042f754.c)
- [`code/fcn.004308e4.c`](code/fcn.004308e4.c)
- [`code/fcn.00435d2c.c`](code/fcn.00435d2c.c)
- [`code/fcn.004369ec.c`](code/fcn.004369ec.c)
- [`code/fcn.0043e80d.c`](code/fcn.0043e80d.c)
- [`code/fcn.00452730.c`](code/fcn.00452730.c)
- [`code/fcn.0045fa59.c`](code/fcn.0045fa59.c)
- [`code/fcn.0046313c.c`](code/fcn.0046313c.c)
- [`code/fcn.00480ce9.c`](code/fcn.00480ce9.c)
- [`code/fcn.00495954.c`](code/fcn.00495954.c)
- [`code/fcn.004a76a0.c`](code/fcn.004a76a0.c)

## Behavioral Analysis

Based on the addition of chunk 3/3, I have integrated and updated the analysis. The new disassembly provides further granular detail regarding the **Virtual Machine (VM) Dispatcher** and the complexity of its **Instruction Mapping**.

### Updated Analysis of Chunk 3

#### 1. Multi-Level Instruction Mapping & Aliasing
The latest snippet confirms a high degree of "Instruction Alias" logic within the VM.
*   **Overlapping Handlers:** Note how `case 4` and `case 5` perform identical operations, calling `fcn.0042cee0`. Similarly, several cases (e.g., `0x10`, `0x11`) map to `fcn.004087b0()`.
*   **Analysis:** This indicates that the VM doesn't just have one handler per opcode; it uses a mapping layer where multiple "virtual" instructions are resolved to a single "native" logic block. This is a hallmark of **VMProtect-style protection**, designed to make it difficult for an analyst to map the original assembly to the virtualized instruction set because the 1:1 relationship between code and function is intentionally broken.

#### 2. Bitwise Register Manipulation & Data Packing
The logic within cases 4 and 5—`fcn.0042cee0(SUB104(fVar3,0), fVar3 >> 0x20, CONCAT22(in_stack_ffffffea, fVar3 >> 0x40))`—is highly significant.
*   **Packed Data Extraction:** Instead of passing a single value, the VM is extracting multiple components from a single register (`fVar3`) using bitwise shifts (`>> 0x20`, `>> 0x40`).
*   **Purpose:** This suggests that the "Virtual Machine" registers are not standard x86_64 registers but are **packed structures**. The VM pulls multiple pieces of data (e.g., an opcode, a memory offset, and a length) from a single 64-bit word before passing them to the handler. This complicates analysis because it obscures what individual variables are actually being manipulated.

#### 3. Obscure Branching & Range Checks
The code `if (uVar1 < 0x15)` followed by a series of nested checks (like `0x14`, `0x10` through `0x13`) indicates **Branch Obfuscation**.
*   **Condition Hiding:** By using complex comparisons to decide which handler to jump to, the packer prevents a researcher from seeing a linear flow. Even if an analyst knows "Opcode X" is being executed, they cannot easily see what follows it because the next step is determined by this nested switch/if-else structure.

#### 4. Interpretation of `fcn.0042d054()` and `fcn.0042d144()`
The final block involving `(uVar1 & 0x4000) == 0` is a **Dynamic Branching** check.
*   **State-Dependent Logic:** The bitwise AND (`& 0x4000`) suggests that the VM tracks its own internal state (the "Instruction Pointer" or "Status Register"). The logic flow of the program changes based on these hidden internal flags, making it nearly impossible to trace the malware's execution path without full emulation of the VM's memory state.

---

### Updated Summary of Findings

*   **Type:** Advanced VM-based Packer / Protector (High Complexity).
*   **Malware Status:** High risk; highly professional-grade obfuscation.

#### Advanced Techniques Identified:
1.  **Complex Code Virtualization:** A multi-layered dispatcher where several virtual instructions map to a single internal handler, creating an "alias" layer that hides the actual logic.
2.  **Control Flow Flattening (CFF):** Extensive use of large switch tables (`uVar1`) to break linear logic into fragmented blocks managed by a central dispatcher.
3.  **Instruction Mutation & Data Packing:** Use of bitwise shifts and "Concats" to extract multiple parameters from single registers, masking the intent of the data being processed.
4.  **Anti-Analysis (Exception Handling):** Verified use of `swi` calls for exception-based flow control and debugger detection (from previous chunks).
5.  **State-Dependent Execution:** The use of bitwise masks on internal state variables (`uVar1 & 0x4000`) to determine the next jump, ensuring that static analysis cannot predict the execution path.

### Conclusion (Updated)
The presence of **Instruction Aliasing** and **Data Packing** in Chunk 3 confirms that this is not a simple packer but a sophisticated VM-based protection engine. The "true" malicious logic is buried behind several layers: first, a translation layer from original instructions to the VM's bytecode; second, a mapping layer where multiple bytecodes point to one handler; and third, a packing layer where data is stored in bit-shifted formats.

**Analyst Note:** To break this, static analysis alone will likely fail. The most effective path forward is **Symbolic Execution** (using tools like Triton or Miasm) or **Dynamic Binary Instrumentation (DBI)** to trace the execution of `uVar1` and log the transitions between handlers. This will allow you to map which "Virtual Instructions" correspond to actual system API calls.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques. 

The core of this behavior is **Defense Evasion**, specifically utilizing a sophisticated "VM-based" protection layer to hide the malicious intent and logic of the payload.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | **Packed_Data** | The use of a VM Dispatcher, multi-level instruction mapping (aliasing), and complex "bit-packed" register manipulation are hallmark characteristics of high-complexity packers used to hide the original code's execution path. |
| **T1055.001** | **Packer** | The specific implementation of a VM protection engine (similar to VMProtect) hides the 1:1 relationship between instructions and logic, requiring specialized tools or symbolic execution for analysis. |
| **(N/A)** | **Control Flow Flattening** | While not a standalone MITRE ID, "Obscure Branching" and "Dynamic Branching" are components of obfuscation that directly support the **T1055 (Packer)** goal by breaking linear logic into a fragmented switch-table structure. |
| **(N/A)** | **Data Obfuscation** | The use of bitwise shifts (`>>`) and concatenations to extract multiple values from one register is an obfuscation technique used to hide the purpose of data being manipulated during execution. |

### Analyst Summary of Mapping
The analysis describes a sophisticated **Defense Evasion** strategy. Specifically:
*   **T1055 (Packer)** is the primary applicable category. The "Instruction Mapping," "Data Packing," and "Control Flow Flattening" are all internal mechanisms used by advanced packers to ensure that static analysis tools cannot easily reconstruct the malware's true behavior or API calls. 
*   The **Anti-Analysis** components (specifically the `swi` instructions for debugger detection) serve as the primary gatekeepers, designed to crash or stall analysis tools before they can reach the core logic hidden behind the VM Dispatcher.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the organized list of Indicators of Compromise (IOCs).

### **1. IP addresses / URLs / Domains**
*   *None identified.*

### **2. File paths / Registry keys**
*   *None identified.* (The strings provided are internal program data types and memory references, not filesystem or registry paths.)

### **3. Mutex names / Named pipes**
*   *None identified.*

### **4. Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 hashes were present in the provided text.)

### **5. Other artifacts**
*   **Malware Type/Behavior:** Advanced VM-based Packer / Protection Engine (identified as potentially "VMProtect-style").
*   **Internal Function Offsets (Tracking/Signature markers):**
    *   `0x42cee0` (fcn.0042cee0) - Shared instruction handler.
    *   `0x4087b0` (fcn.004087b0) - Mapping point for multiple virtual instructions.
    *   `0x42d054` (fcn.0042d054) - State-dependent logic handler.
    *   `0x42d144` (fcn.0042d144) - State-dependent logic handler.
*   **Known Techniques:** 
    *   Control Flow Flattening (CFF).
    *   Instruction Aliasing.
    *   Data Packing/Bitwise Register Manipulation.
    *   Exception-based flow control (`swi` calls).

---
**Analyst Note:** The provided data contains no network or file-system indicators. This sample is heavily obfuscated using a custom virtualization layer. Detection should rely on **behavioral signatures** (e.g., identifying the specific VM-dispatch logic and instruction aliasing) rather than static indicators like IPs or File Paths.

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family**: Unknown (Protector-heavy)
2. **Malware type**: loader
3. **Confidence**: High (regarding functionality; Medium regarding final payload)
4. **Key evidence**:
    *   **Complex VM-based Protection:** The sample utilizes a sophisticated Virtual Machine Dispatcher with "Instruction Aliasing" and "Control Flow Flattening," characteristic of high-end protectors like VMProtect to hide the actual malicious logic.
    *   **Advanced Obfuscation Techniques:** The use of bitwise shift operations for data packing (extracting multiple parameters from single registers) and state-dependent dynamic branching makes static analysis nearly impossible.
    *   **Sophisticated Anti-Analysis:** The integration of `swi` calls for exception-based flow control and detection of debugger environments indicates a professional-grade effort to evade security researchers.
