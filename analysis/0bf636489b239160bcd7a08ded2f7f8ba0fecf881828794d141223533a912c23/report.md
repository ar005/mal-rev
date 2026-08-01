# Threat Analysis Report

**Generated:** 2026-07-29 13:21 UTC
**Sample:** `0bf636489b239160bcd7a08ded2f7f8ba0fecf881828794d141223533a912c23_0bf636489b239160bcd7a08ded2f7f8ba0fecf881828794d141223533a912c23.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0bf636489b239160bcd7a08ded2f7f8ba0fecf881828794d141223533a912c23_0bf636489b239160bcd7a08ded2f7f8ba0fecf881828794d141223533a912c23.exe` |
| File type | PE32 executable for MS Windows 6.01 (GUI), Intel i386, 11 sections |
| Size | 12,925,842 bytes |
| MD5 | `7afa30350b5b75db348fdf47360a0166` |
| SHA1 | `eba85d3a046812d91bdfec14564300519482877e` |
| SHA256 | `0bf636489b239160bcd7a08ded2f7f8ba0fecf881828794d141223533a912c23` |
| Overall entropy | 7.981 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4249973913 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 710,144 | 6.398 | No |
| `.itext` | 6,656 | 6.155 | No |
| `.data` | 16,384 | 5.186 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,608 | 4.804 | No |
| `.didata` | 512 | 2.754 | No |
| `.edata` | 512 | 1.246 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.377 | No |
| `.reloc` | 71,168 | 6.713 | No |
| `.rsrc` | 45,056 | 4.944 | No |

### Imports

**kernel32.dll**: `GetACP`, `GetExitCodeProcess`, `CloseHandle`, `LocalFree`, `SizeofResource`, `VirtualProtect`, `QueryPerformanceFrequency`, `VirtualFree`, `GetFullPathNameW`, `GetProcessHeap`, `ExitProcess`, `HeapAlloc`, `GetCPInfoExW`, `RtlUnwind`, `SetFilePointerEx`
**comctl32.dll**: `InitCommonControls`
**user32.dll**: `CreateWindowExW`, `TranslateMessage`, `CharLowerBuffW`, `CallWindowProcW`, `CharUpperW`, `PeekMessageW`, `GetSystemMetrics`, `SetWindowLongW`, `MessageBoxW`, `DestroyWindow`, `CharUpperBuffW`, `CharNextW`, `MsgWaitForMultipleObjects`, `LoadStringW`, `ExitWindowsEx`
**oleaut32.dll**: `SafeArrayPutElement`, `VariantInit`, `VariantClear`, `SysFreeString`, `SafeArrayAccessData`, `SysReAllocStringLen`, `SafeArrayCreate`, `SafeArrayGetElement`, `SysAllocStringLen`, `SafeArrayUnaccessData`, `SafeArrayPtrOfIndex`, `VariantCopy`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `VariantChangeType`
**advapi32.dll**: `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `OpenThreadToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `RegOpenKeyExW`, `OpenProcessToken`, `FreeSid`, `AllocateAndInitializeSid`, `EqualSid`, `RegQueryValueExW`, `GetTokenInformation`, `ConvertSidToStringSidW`, `RegCloseKey`

### Exports

`__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **35359** (showing first 100)

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

Functions analyzed: **30** | Decompiled to C: **25**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0046f432` | `0x46f432` | 5759 | ✓ |
| `fcn.00453ca3` | `0x453ca3` | 3165 | — |
| `fcn.0041cbc4` | `0x41cbc4` | 2633 | ✓ |
| `fcn.0040443c` | `0x40443c` | 2534 | ✓ |
| `fcn.0041ea20` | `0x41ea20` | 2206 | ✓ |
| `fcn.00443524` | `0x443524` | 2199 | — |
| `fcn.004a73d0` | `0x4a73d0` | 2192 | ✓ |
| `fcn.00404244` | `0x404244` | 1904 | ✓ |
| `fcn.0041fde8` | `0x41fde8` | 1849 | ✓ |
| `fcn.00435e90` | `0x435e90` | 1642 | ✓ |
| `fcn.00436a00` | `0x436a00` | 1510 | ✓ |
| `fcn.00403ec0` | `0x403ec0` | 1500 | ✓ |
| `fcn.0042c8d4` | `0x42c8d4` | 1302 | ✓ |
| `fcn.00429c54` | `0x429c54` | 1230 | ✓ |
| `fcn.004866c2` | `0x4866c2` | 1219 | — |
| `fcn.0042a840` | `0x42a840` | 1201 | ✓ |
| `fcn.00452894` | `0x452894` | 1188 | ✓ |
| `fcn.0042b8f4` | `0x42b8f4` | 1181 | ✓ |
| `fcn.0042c1f4` | `0x42c1f4` | 1174 | ✓ |
| `fcn.00453484` | `0x453484` | 1154 | — |
| `fcn.0042b2d4` | `0x42b2d4` | 1108 | ✓ |
| `fcn.0042f8b8` | `0x42f8b8` | 1086 | ✓ |
| `fcn.00404d34` | `0x404d34` | 1034 | ✓ |
| `fcn.0041f4e4` | `0x41f4e4` | 1008 | ✓ |
| `fcn.0040e290` | `0x40e290` | 1007 | ✓ |
| `fcn.004632a0` | `0x4632a0` | 996 | ✓ |
| `fcn.00480b33` | `0x480b33` | 996 | — |
| `fcn.00430a48` | `0x430a48` | 987 | ✓ |
| `fcn.0042079c` | `0x42079c` | 977 | ✓ |
| `fcn.00495ab8` | `0x495ab8` | 962 | ✓ |

### Decompiled Code Files

- [`code/fcn.00403ec0.c`](code/fcn.00403ec0.c)
- [`code/fcn.00404244.c`](code/fcn.00404244.c)
- [`code/fcn.0040443c.c`](code/fcn.0040443c.c)
- [`code/fcn.00404d34.c`](code/fcn.00404d34.c)
- [`code/fcn.0040e290.c`](code/fcn.0040e290.c)
- [`code/fcn.0041cbc4.c`](code/fcn.0041cbc4.c)
- [`code/fcn.0041ea20.c`](code/fcn.0041ea20.c)
- [`code/fcn.0041f4e4.c`](code/fcn.0041f4e4.c)
- [`code/fcn.0041fde8.c`](code/fcn.0041fde8.c)
- [`code/fcn.0042079c.c`](code/fcn.0042079c.c)
- [`code/fcn.00429c54.c`](code/fcn.00429c54.c)
- [`code/fcn.0042a840.c`](code/fcn.0042a840.c)
- [`code/fcn.0042b2d4.c`](code/fcn.0042b2d4.c)
- [`code/fcn.0042b8f4.c`](code/fcn.0042b8f4.c)
- [`code/fcn.0042c1f4.c`](code/fcn.0042c1f4.c)
- [`code/fcn.0042c8d4.c`](code/fcn.0042c8d4.c)
- [`code/fcn.0042f8b8.c`](code/fcn.0042f8b8.c)
- [`code/fcn.00430a48.c`](code/fcn.00430a48.c)
- [`code/fcn.00435e90.c`](code/fcn.00435e90.c)
- [`code/fcn.00436a00.c`](code/fcn.00436a00.c)
- [`code/fcn.00452894.c`](code/fcn.00452894.c)
- [`code/fcn.004632a0.c`](code/fcn.004632a0.c)
- [`code/fcn.0046f432.c`](code/fcn.0046f432.c)
- [`code/fcn.00495ab8.c`](code/fcn.00495ab8.c)
- [`code/fcn.004a73d0.c`](code/fcn.004a73d0.c)

## Behavioral Analysis

The addition of the third disassembly chunk provides a critical "smoking gun" regarding how this packer handles logic flow and evades automated analysis tools. This segment reinforces the previous conclusions about **Virtual Machine (VM)** architecture and **Control-Flow Flattening**, while introducing new evidence of **intentional anti-decompiler tactics.**

Here is the updated and extended analysis:

### 1. Advanced Obfuscation Architectures
*   **State Machine & Dispatcher Logic:**
    The sequence involving `uStack_64` assignments (e.g., `0x495e5a`, `0x495e62`) followed by function calls is a classic implementation of a **Finite State Machine (VM Dispatcher)**. 
    *   Each unique hex value assigned to `uStack_64` represents a specific "state" or "instruction" in the custom bytecode. 
    *   The repetitive nature of these assignments suggests that the code is transitioning through different stages of a decoding process, where each state determines which logic branch the interpreter should execute next.

*   **Extreme Control-Flow Flattening (CFF):**
    The warning `Too many branches` at `0x00495e78` is a significant indicator of **intentional complexity**. In professional-grade packers, this happens when the obfuscator purposefully creates a jump table so large or complex that standard decompiler tools (like IDA Pro or Ghidra) cannot resolve the destination of the jumps.
    *   By making the control flow "undecipherable" to the tool, the author ensures that an analyst cannot simply click a button to see the "true" path of the code. 

### 2. Anti-Analysis & Decompiler Sabotage
*   **Indirect Jump Obfuscation:**
    The note `Treating indirect jump as call` is a fallback by the decompiler because it cannot resolve where the code is jumping. In this context, **indirect jumps are the backbone of the VM.** Instead of a direct `JMP 0x1234`, the code calculates a destination at runtime. This prevents static analysis from mapping out the execution path, as the "next step" only exists in memory during execution.

*   **Tool-Breaking Techniques:**
    The "Too many branches" error indicates that the author is using techniques designed to **exhaust or break automated analysis.** By creating a "branching explosion," they force a human analyst to perform "manual devirtualization"—manually tracing every possible jump—which is time-prohibitive and prone to human error.

### 3. Data Manipulation & State Tracking
*   **Persistence of State:**
    The use of `uStack_64` as a primary vehicle for state tracking suggests that the VM maintains a "context" as it processes its bytecode. Even if the code is broken into hundreds of small pieces, the internal state variable ensures the program knows where it is in the malicious logic (e.g., *Step 1: Decrypt; Step 2: Check for Debugger; Step 3: Inject Payload*).

---

### Updated Risk Assessment & Conclusions
*   **Sophistication Level:** **Extreme.** The presence of "branching explosions" and indirect jumps that break decompiler logic confirms this is a high-tier packer. It isn't just trying to hide from humans; it is actively designed to defeat the automated tools that researchers rely on.
*   **Primary Function:** This is a **highly resilient wrapper.** Its purpose is to insulate the malicious payload so thoroughly that even an experienced reverse engineer would struggle to extract the "Stage 2" code without significant manual labor and custom scripting.
*   **Analysis Difficulty:** **Very High.** The transition from "obfuscated" to "virtually protected" means that standard static analysis is insufficient. To fully understand this threat, one must move to dynamic analysis (memory dumping) or write a custom script to "trace" the `uStack_64` values and map them to their respective actions.

### Updated Summary Table of Technical Indicators
| Feature | Observed Function(s) / Markers | Significance |
| :--- | :--- | :--- |
| **VM Dispatcher** | `fcn.0041fde8`, `uStack_64` assignments | Uses a state-based machine to process custom bytecode rather than x86 instructions. |
| **Control-Flow Flattening** | `fcn.00429c54`, `fcn.0042a840` | Destroys the linear logic of the program, making it hard to follow the "story" of the code. |
| **Branch Explosion** | `0x00495e78` (Too many branches) | Intentional design to break decompiler tools and force manual, time-consuming analysis. |
| **Indirect Jumps** | `UNRECOVERED_JUMPTABLE_00` | Ensures the path of execution is only known at runtime, hiding the true logic from static scanners. |
| **Bitwise Transformation** | `fcn.00435e90` | Used to peel back layers of encryption on configuration data or subsequent payloads. |

**Final Conclusion:** This binary is a sophisticated piece of engineering. It functions as a high-grade "shield" for malicious code, utilizing VM architecture and anti-decompiler techniques to maximize the time and effort required for an analyst to uncover its true intent.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&K techniques. 

The majority of these behaviors fall under **T1029 (Obfuscated Files or Information)** because they are specifically designed to hinder static analysis, evade automated tools, and hide the true logic of the malware’s execution.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1029 | Obfuscated Files or Information (VM/CFF) | The use of a custom VM Dispatcher and Control-Flow Flattening masks the program's logic by replacing linear instructions with complex, state-based bytecode. |
| T1029 | Obfuscated Files or Information (Indirect Jumps) | Utilizing indirect jumps ensures that jump targets are only resolved at runtime, preventing automated tools from mapping out the execution path. |
| T1029 | Obfuscated Files or Information (Branch Explosion) | Creating an overwhelming number of branches is a deliberate "decompiler sabotage" tactic intended to exhaust tool resources and force time-consuming manual analysis. |
| T1401 | Data Encoding (Bitwise Transformation) | The use of bitwise operations indicates the obfuscation of configuration data or payloads, requiring the analyst to decode these values before they can be analyzed. |

### Analyst Notes:
*   **Complexity Level:** The combination of **T1029** and **T1401** suggests a high-tier threat actor or sophisticated malware developer targeting an audience that includes professional reverse engineers. 
*   **Anti-Analysis Strategy:** The "Branch Explosion" at `0x00495e78` is a specific form of anti-analysis aimed at creating a "time wall," forcing the analyst to spend significantly more man-hours on manual devirtualization than would be required by standard obfuscation.
*   **Detection Gap:** Because these techniques are designed to defeat **static analysis**, signature-based detection and automated sandboxing may fail to identify the underlying payload without dynamic memory dumping or manual de-obfuscation.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The provided text describes the **architecture of a packer/protector** rather than specific active campaign infrastructure (like hardcoded C2 IPs or file paths). Therefore, most standard network indicators are absent.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 strings were present in the data).

### **Other artifacts**
The following are technical indicators of the malware's packer/protection layer:

*   **VM Dispatcher Logic:** Use of `uStack_64` with specific state transitions (e.g., `0x495e5a`, `0x495e62`) to facilitate custom bytecode execution.
*   **Control-Flow Flattening (CFF) Markers:** 
    *   `fcn.00429c54`
    *   `fcn.0042a840`
*   **Branch Explosion Point:** `0x00495e78` (Identified as a point of intentional complexity to break decompiler tools).
*   **Bitwise Transformation Logic:** `fcn.00435e90` (Used for unpacking/decryption).
*   **Unsupported Jump Tables:** `UNRECOVERED_JUMPTABLE_00` (Indicates use of indirect jumps to hide execution paths).
*   **Custom VM Dispatcher:** `fcn.0041fde8` (Specific function entry point for the virtual machine dispatcher).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
*   **Advanced Protective Layer:** The sample utilizes a sophisticated VM-based protection system involving custom bytecode execution (State Machine/Dispatcher logic) and Control-Flow Flattening to hide its true functionality.
*   **Decompiler Sabotage:** The presence of "Branch Explosion" at `0x00495e78` and extensive use of indirect jumps are intentional tactics designed to break automated analysis tools, a hallmark of high-tier loaders/packers.
*   **Wrapper Functionality:** The report explicitly identifies the binary as a "highly resilient wrapper" or "shield," whose primary purpose is to obfuscate and decrypt a hidden Stage 2 payload rather than performing immediate malicious actions like data theft or file encryption.
