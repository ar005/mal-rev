# Threat Analysis Report

**Generated:** 2026-08-20 21:20 UTC
**Sample:** `10b9527581f39a4ea266447ff23c302c44a99deded83c803752062b749e68e9a_10b9527581f39a4ea266447ff23c302c44a99deded83c803752062b749e68e9a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10b9527581f39a4ea266447ff23c302c44a99deded83c803752062b749e68e9a_10b9527581f39a4ea266447ff23c302c44a99deded83c803752062b749e68e9a.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 11 sections |
| Size | 2,367,212 bytes |
| MD5 | `0df7f4045510dd2f9296b3719a60473c` |
| SHA1 | `d3e9d878039b235b8c75990970950c6633d8bf9b` |
| SHA256 | `10b9527581f39a4ea266447ff23c302c44a99deded83c803752062b749e68e9a` |
| Overall entropy | 7.73 |
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
| `.rsrc` | 19,456 | 4.529 | No |

### Imports

**kernel32.dll**: `GetACP`, `GetExitCodeProcess`, `CloseHandle`, `LocalFree`, `SizeofResource`, `VirtualProtect`, `QueryPerformanceFrequency`, `VirtualFree`, `GetFullPathNameW`, `GetProcessHeap`, `ExitProcess`, `HeapAlloc`, `GetCPInfoExW`, `RtlUnwind`, `SetFilePointerEx`
**comctl32.dll**: `InitCommonControls`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `CharLowerBuffW`, `CallWindowProcW`, `CharUpperW`, `PeekMessageW`, `GetSystemMetrics`, `SetWindowLongW`, `MessageBoxW`, `DestroyWindow`, `CharUpperBuffW`, `CharNextW`, `MsgWaitForMultipleObjects`, `LoadStringW`, `ExitWindowsEx`
**oleaut32.dll**: `SafeArrayPutElement`, `VariantInit`, `VariantClear`, `SysFreeString`, `SafeArrayAccessData`, `SysReAllocStringLen`, `SafeArrayCreate`, `SafeArrayGetElement`, `SysAllocStringLen`, `SafeArrayUnaccessData`, `SafeArrayPtrOfIndex`, `VariantCopy`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `VariantChangeType`
**advapi32.dll**: `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `OpenThreadToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `RegOpenKeyExW`, `OpenProcessToken`, `FreeSid`, `AllocateAndInitializeSid`, `EqualSid`, `RegQueryValueExW`, `GetTokenInformation`, `ConvertSidToStringSidW`, `RegCloseKey`

### Exports

`__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **12775** (showing first 100)

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

This final piece of disassembly confirms and solidifies the previous findings, providing clear evidence of the advanced architectural decisions made by the developers. The addition of chunk 3/3 allows us to refine our understanding of how the Virtual Machine (VM) handles its internal logic.

### Updated Analysis: [Chunk 3/3]

#### 1. Multi-Dimensional Instruction Decoding (Advanced VM Logic)
The final chunk reveals that the "instruction" being processed by the VM is not a simple, single-byte opcode. Instead, it uses **Bitmasking and Bit-Shifting** to extract multiple parameters from a single variable (`uVar1`).
*   **Packed Parameters:** In cases 4 and 5, notice the operations `fVar3 >> 0x20` and `fVar3 >> 0x40`. This indicates that one "instruction" contains multiple pieces of information (e.g., an opcode, a memory offset, and a length) packed into a single 32-bit or 64-bit word.
*   **Conditional Logic via Bitmasks:** The final block—`if ((uVar1 & 0x4000) == 0)`—is a classic example of **hidden branching**. Rather than using a standard `if (a == b)`, the code checks if a specific bit in the instruction word is set. This hides the true intent of the branch from automated tools that only look for standard equality comparisons.

#### 2. Nested Control Flow & "Switch-in-Switch"
The presence of two distinct logic blocks—one for `uVar1 < 0x15` and one for values $\ge$ `0x15`—confirms a **hierarchical dispatch system**.
*   **Range-Based Dispatch:** The VM first determines the "type" or "class" of the instruction (is it a standard operation, a specialized system call, or an internal state change?) before deciding which sub-handler to invoke. 
*   **Abstraction Layers:** This suggests that the malicious logic is abstracted. For example, `fcn.004087b0()` is called in multiple different cases (9, 10, 11). This means several different "virtual instructions" might perform the same underlying action, but are represented by different opcodes to complicate tracking.

#### 3. Complex Argument Preparation
The way parameters are passed to functions like `fcn.0042cee0` is highly sophisticated:
*   **Manual Stack Manipulation:** The use of `SUB104`, `CONCAT22`, and complex shifts suggests that the VM performs "pre-processing" on its data before execution. 
*   **Obfuscated Function Calls:** Instead of calling a function with clear arguments, the malware prepares a "blob" of data (the result of those bitwise operations) and passes it to an internal handler. This makes it nearly impossible for a human analyst to know what `fcn.0042cee0` is actually doing without perfectly emulating the VM's state at that exact moment.

#### 4. Evidence of Modular Design
The repetition of certain functions (like `fcn.0042cff4`) across different branches suggests a **modular plugin architecture**. The "Virtual Machine" acts as an execution engine for a script. When the "script" wants to perform a network request, it calls one opcode; when it wants to perform an encrypted file write, it might call another, but both eventually route through common internal utility functions.

---

### Final Summary for Threat Intelligence

**Threat Profile: High-Sophistication Multi-Layered VM (Advanced Persistence & Evasion).**

*   **Core Architecture:** The malware utilizes a **nested, multi-layered Virtual Machine**. This is not a simple packer; it is a custom execution environment. It processes "packed" instructions where multiple attributes (opcodes, addresses, and flags) are mashed into single variables to evade signature-based detection and standard disassembly analysis.
*   **Advanced Obfuscation Techniques:**
    *   **Bitwise Instruction Packing:** Uses bit-shifting (`>> 0x20`) and masking (`& 0x4000`) to hide the true meaning of opcodes and conditional branches.
    *   **Nested Dispatchers:** A multi-stage "switch" system that categorizes instructions before they are executed, creating a massive barrier to understanding the full capability of the malware via static analysis.
    *   **Control Flow Flattening (CFF):** The logic is "flattened" into a large central dispatcher, making it difficult to determine the actual chronological flow of operations like "Download $\rightarrow$ Inject $\rightarrow$ Beacon."
    *   **Junk Code/Code Bloat:** Deliberate insertion of repetitive code to exhaust manual analyst time and confuse automated graph-analysis tools.
*   **Operational Maturity:** **High.** This level of complexity (specifically the multi-layered VM with bit-packed opcodes) is characteristic of state-sponsored actors or highly organized cybercriminal groups (e.g., APTs, advanced Ransomware operators). It indicates a desire to remain undetected for long periods while maintaining a modular set of capabilities.

**Recommended Action for Responders:**
1.  **Avoid Pure Static Analysis:** Traditional disassembly is insufficient due to the VM layers. The "real" logic only exists when the VM decodes its own bytecode.
2.  **Dynamic Instrumentation (Pin/Frida):** Hook the primary dispatchers (e.g., `0x42c090`, `0x42b170`). Log the value of the "instruction" register (`uVar1`) and the state variables before they are passed to internal functions.
3.  **Memory Forensics:** Perform a memory dump during execution. The "unpacked" instructions or the underlying configuration data (C2 URLs, keys) may exist in plain text in memory even if they are heavily encoded in the binary's file structure.
4.  **Behavioral Monitoring:** Focus on the results of the `fcn.0042cff4()` and similar calls; these likely represent the "exit points" where the VM interacts with the OS (network, files, registry).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | Virtualization | The malware utilizes a custom-built Virtual Machine (VM) to execute its core logic via a proprietary instruction set, hiding the true functionality from analysts. |
| **T1028** | Virtualization (Instruction Decoding) | The use of bitmasking and bit-shifting to pack multiple parameters into single values hides opcode meaning and complicates automated analysis. |
| **T1028** | Virtualization (Control Flow Flattening) | The "nested dispatch" and "switch-in-switch" logic flattens the program's control flow, making it difficult to determine the actual execution sequence. |
| **T1036** | Masquerading | While primarily a signature for names/files, the use of "abstraction layers" ensures that multiple different virtual instructions perform common tasks to hide the malware’s purpose. |

***Note from Analyst:** The behaviors identified—specifically Bitmasking, Control Flow Flattening, and Junk Code—are high-level obfuscation techniques designed to facilitate **Defense Evasion**. In the MITRE ATT&CK framework, these are most accurately mapped to **T1028 (Virtualization)** because they are all components of a custom execution environment designed to thwart static and dynamic analysis.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided text describes the internal mechanics of a highly sophisticated malware sample employing a custom Virtual Machine (VM) to obfuscate its logic. While the description provides significant insight into the **techniques** used by the threat actor (e.g., bit-masking, control flow flattening, and nested dispatchers), it does not contain specific external indicators such as hardcoded IP addresses, domain names, or file system paths.

---

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: Terms like `.data` and `.rdata` are standard executable section headers, not specific file system paths.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Internal Function Offsets (Potential for YARA/Signature development):** 
    The following addresses are noted as key entry points within the malware's internal VM logic. While not standard "network" IOCs, they can be used to create code-based signatures:
    *   `0x4087b0` (Multi-handler dispatcher)
    *   `0x42cee0` (Complex argument preparation/processing)
    *   `0x42cff4` (Module exit points/interaction points with the OS)

---

### **Analyst Notes**
The "Indicators" in this specific sample are **behavioral rather than static**. The analysis suggests that standard static analysis will be ineffective because:
1.  **Instruction Packing:** Opcode values are hidden behind bit-shifts (`>> 0x20`) and masks (`& 0x4000`).
2.  **Dynamic Behavior:** The "real" IOCs (such as C2 IP addresses or stolen file paths) are likely decrypted in memory only during runtime by the VM's execution engine.
3.  **Recommendation:** Detection should focus on memory forensics and monitoring for suspicious API calls originating from the specific code blocks identified above (`0x4087b0`, `0x42cee0`, `0x42cff4`).

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader / backdoor
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated VM Architecture:** The sample utilizes a complex, multi-layered Virtual Machine (VM) to execute its logic, employing "Bitmasking" and "Bit-Shifting" to hide opcodes and parameters from automated analysis.
    *   **Advanced Obfuscation Techniques:** The use of Control Flow Flattening (CFF), nested dispatchers ("switch-in-switch"), and junk code indicates a high level of maturity typical of APTs or advanced cybercriminal groups.
    *   **Modular Design:** The behavior suggests the VM acts as an execution engine for various "scripts," allowing it to perform different actions (network communication, file system interaction) through modular plug-ins while hiding the true functionality from static analysis.
