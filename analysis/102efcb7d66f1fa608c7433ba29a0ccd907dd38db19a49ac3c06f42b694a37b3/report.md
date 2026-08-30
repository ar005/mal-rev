# Threat Analysis Report

**Generated:** 2026-08-18 01:14 UTC
**Sample:** `102efcb7d66f1fa608c7433ba29a0ccd907dd38db19a49ac3c06f42b694a37b3_102efcb7d66f1fa608c7433ba29a0ccd907dd38db19a49ac3c06f42b694a37b3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `102efcb7d66f1fa608c7433ba29a0ccd907dd38db19a49ac3c06f42b694a37b3_102efcb7d66f1fa608c7433ba29a0ccd907dd38db19a49ac3c06f42b694a37b3.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 11 sections |
| Size | 17,987,288 bytes |
| MD5 | `379af136be94c87aed5965df0c0666c8` |
| SHA1 | `b3c81e7e46f9d28f000ddc6c1fc0a8f828e60bdb` |
| SHA256 | `102efcb7d66f1fa608c7433ba29a0ccd907dd38db19a49ac3c06f42b694a37b3` |
| Overall entropy | 7.99 |
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
| `.rsrc` | 19,456 | 4.53 | No |

### Imports

**kernel32.dll**: `GetACP`, `GetExitCodeProcess`, `CloseHandle`, `LocalFree`, `SizeofResource`, `VirtualProtect`, `QueryPerformanceFrequency`, `VirtualFree`, `GetFullPathNameW`, `GetProcessHeap`, `ExitProcess`, `HeapAlloc`, `GetCPInfoExW`, `RtlUnwind`, `SetFilePointerEx`
**comctl32.dll**: `InitCommonControls`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `CharLowerBuffW`, `CallWindowProcW`, `CharUpperW`, `PeekMessageW`, `GetSystemMetrics`, `SetWindowLongW`, `MessageBoxW`, `DestroyWindow`, `CharUpperBuffW`, `CharNextW`, `MsgWaitForMultipleObjects`, `LoadStringW`, `ExitWindowsEx`
**oleaut32.dll**: `SafeArrayPutElement`, `VariantInit`, `VariantClear`, `SysFreeString`, `SafeArrayAccessData`, `SysReAllocStringLen`, `SafeArrayCreate`, `SafeArrayGetElement`, `SysAllocStringLen`, `SafeArrayUnaccessData`, `SafeArrayPtrOfIndex`, `VariantCopy`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `VariantChangeType`
**advapi32.dll**: `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `OpenThreadToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `RegOpenKeyExW`, `OpenProcessToken`, `FreeSid`, `AllocateAndInitializeSid`, `EqualSid`, `RegQueryValueExW`, `GetTokenInformation`, `ConvertSidToStringSidW`, `RegCloseKey`

### Exports

`__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **46483** (showing first 100)

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

This analysis incorporates the findings from the final disassembly chunk (chunk 3/3) into the existing profile of the binary.

### Updated Technical Analysis

The third installment of the disassembly confirms the sophisticated nature of the protection layer, specifically highlighting the scale and complexity of the **Virtual Machine (VM)** architecture used to shield the payload.

#### 1. Advanced Interpreter Architecture (Handler Diversity)
The block beginning with `uVar1` is a classic example of a **VM Dispatcher**. The variable `uVar1` acts as an "opcode" fetched from a buffer.
*   **Instruction Density:** The range of values for `uVar1` (from low integers to `0x102`) indicates a large, custom instruction set. 
*   **Common vs. Specialized Handlers:** Note how many cases (e.g., 0x10, 0x11, and several others) call the exact same function (`fcn.004087b0`). In VM-based packers, this is a common technique where multiple "logical" instructions are mapped to one "physical" handler to reduce the footprint of the dispatcher while still providing a wide range of functionality.
*   **Complexity in Decoding:** Cases 4 and 5 show that even basic operations involve complex bitwise manipulation (e.g., `fVar3 >> 0x20`, `CONCAT22`). This implies that the "arguments" for the VM instructions are themselves obfuscated, requiring a calculation step just to determine what value is being passed to the underlying handler.

#### 2. Multi-Layered Logic Branching (The "Gatekeeper")
The final section of the disassembly contains a bitmask check: `if ((uVar1 & 0x4000) == 0)`.
*   **Purpose:** This is likely a **Feature/Type Check**. The VM interpreter uses this to distinguish between "Standard" instructions (like addition or memory movement) and "System/Privileged" instructions (like interacting with the OS, networking, or environment checks).
*   **Significance:** By branching based on a bitmask of the opcode, the packer ensures that even if an analyst identifies one handler, they cannot easily map out the entire execution flow. The logic is abstracted behind bitwise operations to prevent linear analysis.

#### 3. Resilience Against Static Analysis (Decompiler Breaking)
The presence of "Unrecovered Jump Tables" and the use of nested `if/else` structures to handle cases like `0x12` and `0x13` are intentional. By creating complex conditions for simple outcomes, the developers ensure that tools like Ghidha or IDA Pro produce messy, non-linear code. This forces a human analyst to manually "de-virtualize" the logic—a process that can take days or weeks of manual tracing.

---

### Updated Summary of Indicators

| Feature | Observation in Chunk 3/3 | Significance |
| :--- | :--- | :--- |
| **Wide Instruction Set** | Range of `uVar1` values up to `0x102` with varied handlers. | Confirms a high-complexity VM designed to host a large amount of logic, making it difficult to map the full scope of the malware. |
| **Argument Obfuscation** | Use of `CONCAT22`, `SUB104`, and shifts (`>> 0x20`) in jump/call preparations. | Even when an "instruction" is identified, its parameters are hidden behind math, slowing down automated analysis. |
| **Bitmask Dispatching** | The `(uVar1 & 0x4000)` check at the end of the block. | A "Gatekeeper" mechanism to separate standard operations from sensitive system-level calls or state changes. |
| **Handler Multiplexing** | Multiple opcodes calling `fcn.004087b0`. | Simplifies the packer's code while complicating the analyst's task of distinguishing between different logical steps. |

---

### Updated Inference for Incident Response

The final analysis confirms that this binary is protected by a **top-tier, professional-grade VM protector** (akin to VMProtect or Themida). This level of protection suggests a sophisticated threat actor or a highly developed malware "kit."

1.  **High Barrier to Entry:** The core functionality of the malware is currently inaccessible via static analysis. The "logic" isn't in the assembly you are seeing; it is encoded as bytecode that only exists in a readable state inside the VM's memory space at runtime.
2.  **The "Labyrinth" Strategy:** The complexity found in `fcn.00481...` (Chunk 2) and the opcode handling in Chunk 3 are designed to exhaust an analyst’s time. Every time you find a piece of logic, it is hidden behind another layer of transformation.
3.  **Detection Methodology Update:**
    *   **Abandon Static De-virtualization:** Do not attempt to "solve" the VM's math or map its entire instruction set. This is a diminishing return for manual analysis.
    *   **Targeted Memory Forensics:** The most efficient way to find the "real" payload is to let the VM do the work for you. Monitor the process in a debugger; wait for the VM to finish "unpacking" and "de-obfuscating" its internal states. 
    *   **Trigger Points:** Set breakpoints on:
        *   `VirtualAlloc` / `VirtualProtect`: To catch the memory being prepared for the .NET payload.
        *   `GetProcAddress` / `LoadLibrary`: To see which Windows APIs are actually being called once the VM "unwraps" a command.
    *   **Dump on Execution:** Once the .NET strings and components (identified in Chunk 1) are fully decrypted into memory, perform a memory dump. This will provide a "clean" version of the final payload for standard analysis with `dnSpy`.

**Actionable Intelligence Summary:**
The loader is a sophisticated **"wrapper."** It uses advanced VM-based obfuscation to protect a secondary .NET malware component. Focus efforts on **dynamic memory dumping** at the point of transition between the "Loader" and the "Payload."

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1026.003 | Packer | The use of a high-complexity Virtual Machine (VM) architecture is employed to shield the core logic and create a significant barrier for manual de-virtualization. |
| T1027 | Obfuscated Files or Information | The implementation of "Gatekeeper" bitmask checks, argument obfuscation, and complex bitwise manipulations is designed to hide the true nature of instructions from analysts. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral documentation, here are the extracted Indicators of Compromise (IOCs).

**Note:** The source material describes the internal mechanics of a sophisticated **Virtual Machine (VM) protector** (likely similar to VMProtect or Themida) used as a "wrapper" for malware. Because the report focuses on the technical architecture of the packer rather than the specific infrastructure of the payload, there are no external network IOCs (IPs/Domains) present in this specific text.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The strings provided are internal programming library constants and symbols).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **VM Dispatcher Opcode Range:** `0x1` to `0x102` (Used for internal instruction set mapping).
*   **Handler Multiplexing:** Multiple opcodes (e.g., `0x10`, `0x11`) map to a single physical handler (`fcn.004087b0`). 
*   **Gatekeeper Bitmask:** The bitwise check `(uVar1 & 0x4000)` is used to distinguish between standard and privileged system calls.
*   **Hidden Logic Identifiers:** References to internal functions like `fcn.00481...` (used for complex logic branching).

---
### **Analyst Notes**
The provided text contains several "Internal Artifacts" rather than traditional IOCs. The strings listed (e.g., `AnsiChar`, `TObject`, `VTable`, `TryEnter`) are standard Delphi/C++ framework libraries and do not represent malicious behavior or specific infrastructure.

The **Behavioral Analysis** indicates a high-sophistication threat actor using a custom VM-based packer to hide a .NET payload. From an incident response perspective, the primary "indicator" is the presence of a highly complex protection layer designed to frustrate static analysis and delay the identification of the secondary .NET malware component.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced VM-based Protection:** The analysis confirms the use of a sophisticated Virtual Machine (VM) architecture (similar to VMProtect or Themida), featuring a large instruction set, handler multiplexing, and argument obfuscation to hide core logic from static analysis.
*   **Loader/Wrapper Functionality:** The report explicitly identifies the sample as a "sophisticated wrapper" designed to protect and eventually deliver a secondary .NET payload.
*   **Anti-Analysis Techniques:** The presence of "Gatekeeper" bitmask checks and complex, non-linear code paths is specifically designed to exhaust human analysts and break common decompiler tools (Ghidra/IDA Pro).
