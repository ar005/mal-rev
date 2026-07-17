# Threat Analysis Report

**Generated:** 2026-07-16 20:58 UTC
**Sample:** `07885e0002bbd30d6ce689c1f24df1a25c2eb0c0c9f21d70a58982b61e204c2a_07885e0002bbd30d6ce689c1f24df1a25c2eb0c0c9f21d70a58982b61e204c2a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07885e0002bbd30d6ce689c1f24df1a25c2eb0c0c9f21d70a58982b61e204c2a_07885e0002bbd30d6ce689c1f24df1a25c2eb0c0c9f21d70a58982b61e204c2a.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 11 sections |
| Size | 8,474,112 bytes |
| MD5 | `2a5f86084ceb8cd25f4fe3b2a3bccdba` |
| SHA1 | `d98c6f807e9d17ae6db7da266c6d0b83dbde1405` |
| SHA256 | `07885e0002bbd30d6ce689c1f24df1a25c2eb0c0c9f21d70a58982b61e204c2a` |
| Overall entropy | 6.15 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770053274 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,408,704 | 5.735 | No |
| `.data` | 562,688 | 4.711 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 18,944 | 4.21 | No |
| `.didata` | 4,608 | 3.16 | No |
| `.edata` | 512 | 1.866 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.39 | No |
| `.reloc` | 342,016 | 6.475 | No |
| `.pdata` | 360,448 | 6.448 | No |
| `.rsrc` | 774,656 | 6.27 | No |

### Imports

**oleaut32.dll**: `GetErrorInfo`, `SysFreeString`
**advapi32.dll**: `RegUnLoadKeyW`, `RegSetValueExW`, `RegSaveKeyW`, `RegRestoreKeyW`, `RegReplaceKeyW`, `RegQueryValueExW`, `RegQueryInfoKeyW`, `RegOpenKeyExW`, `RegLoadKeyW`, `RegFlushKey`, `RegEnumValueW`, `RegEnumKeyExW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegCreateKeyExW`
**user32.dll**: `EnumDisplayMonitors`, `GetMonitorInfoW`, `MonitorFromPoint`, `MonitorFromRect`, `MonitorFromWindow`
**kernel32.dll**: `Sleep`
**gdi32.dll**: `UnrealizeObject`, `StretchDIBits`, `StretchBlt`, `StartPage`, `StartDocW`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetRectRgn`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBits`
**version.dll**: `VerQueryValueW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoTaskMemFree`, `CoTaskMemAlloc`, `CoCreateInstance`, `CoUninitialize`, `CoInitialize`, `IsEqualGUID`
**comctl32.dll**: `InitializeFlatSB`, `FlatSB_SetScrollProp`, `FlatSB_SetScrollPos`, `FlatSB_SetScrollInfo`, `FlatSB_GetScrollPos`, `FlatSB_GetScrollInfo`, `_TrackMouseEvent`, `ImageList_GetImageInfo`, `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_GetDragImage`, `ImageList_DragShowNolock`, `ImageList_DragMove`
**shell32.dll**: `Shell_NotifyIconW`
**winspool.drv**: `GetDefaultPrinterW`
**winhttp.dll**: `WinHttpWriteData`, `WinHttpSetOption`, `WinHttpSetCredentials`, `WinHttpSendRequest`, `WinHttpReceiveResponse`, `WinHttpReadData`, `WinHttpQueryOption`, `WinHttpQueryHeaders`, `WinHttpQueryDataAvailable`, `WinHttpQueryAuthSchemes`, `WinHttpOpenRequest`, `WinHttpOpen`, `WinHttpCrackUrl`, `WinHttpConnect`, `WinHttpCloseHandle`

### Exports

`TMethodImplementationIntercept`, `__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **44883** (showing first 100)

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
| `fcn.0067ebe1` | `0x67ebe1` | 107730 | ✓ |
| `fcn.00430869` | `0x430869` | 100629 | ✓ |
| `fcn.0078fca1` | `0x78fca1` | 85650 | ✓ |
| `fcn.0078f90c` | `0x78f90c` | 84914 | ✓ |
| `fcn.00552dc6` | `0x552dc6` | 56818 | ✓ |
| `fcn.0041faf0` | `0x41faf0` | 27976 | ✓ |
| `fcn.005de924` | `0x5de924` | 24751 | ✓ |
| `fcn.00977173` | `0x977173` | 9097 | ✓ |
| `fcn.007f28b0` | `0x7f28b0` | 7632 | ✓ |
| `fcn.00694860` | `0x694860` | 4456 | ✓ |
| `fcn.006913a0` | `0x6913a0` | 4124 | ✓ |
| `fcn.00a197f2` | `0xa197f2` | 4095 | ✓ |
| `fcn.009813e0` | `0x9813e0` | 4006 | ✓ |
| `fcn.00457da0` | `0x457da0` | 3921 | ✓ |
| `fcn.00434370` | `0x434370` | 3874 | ✓ |
| `fcn.00957a90` | `0x957a90` | 3741 | ✓ |
| `fcn.006954fd` | `0x6954fd` | 3653 | ✓ |
| `fcn.00982610` | `0x982610` | 3539 | ✓ |
| `fcn.006c86d0` | `0x6c86d0` | 3456 | ✓ |
| `fcn.00955720` | `0x955720` | 3343 | ✓ |
| `fcn.007eb720` | `0x7eb720` | 3340 | ✓ |
| `fcn.00753109` | `0x753109` | 3312 | ✓ |
| `fcn.00438340` | `0x438340` | 3124 | ✓ |
| `fcn.0075ca6e` | `0x75ca6e` | 3122 | ✓ |
| `fcn.00693cab` | `0x693cab` | 2855 | ✓ |
| `fcn.006bdcc0` | `0x6bdcc0` | 2744 | ✓ |
| `fcn.00452140` | `0x452140` | 2678 | ✓ |
| `fcn.00838350` | `0x838350` | 2610 | ✓ |
| `fcn.00452fa0` | `0x452fa0` | 2552 | ✓ |
| `fcn.00453c00` | `0x453c00` | 2522 | ✓ |

### Decompiled Code Files

- [`code/fcn.0041faf0.c`](code/fcn.0041faf0.c)
- [`code/fcn.00430869.c`](code/fcn.00430869.c)
- [`code/fcn.00434370.c`](code/fcn.00434370.c)
- [`code/fcn.00438340.c`](code/fcn.00438340.c)
- [`code/fcn.00452140.c`](code/fcn.00452140.c)
- [`code/fcn.00452fa0.c`](code/fcn.00452fa0.c)
- [`code/fcn.00453c00.c`](code/fcn.00453c00.c)
- [`code/fcn.00457da0.c`](code/fcn.00457da0.c)
- [`code/fcn.00552dc6.c`](code/fcn.00552dc6.c)
- [`code/fcn.005de924.c`](code/fcn.005de924.c)
- [`code/fcn.0067ebe1.c`](code/fcn.0067ebe1.c)
- [`code/fcn.006913a0.c`](code/fcn.006913a0.c)
- [`code/fcn.00693cab.c`](code/fcn.00693cab.c)
- [`code/fcn.00694860.c`](code/fcn.00694860.c)
- [`code/fcn.006954fd.c`](code/fcn.006954fd.c)
- [`code/fcn.006bdcc0.c`](code/fcn.006bdcc0.c)
- [`code/fcn.006c86d0.c`](code/fcn.006c86d0.c)
- [`code/fcn.00753109.c`](code/fcn.00753109.c)
- [`code/fcn.0075ca6e.c`](code/fcn.0075ca6e.c)
- [`code/fcn.0078f90c.c`](code/fcn.0078f90c.c)
- [`code/fcn.0078fca1.c`](code/fcn.0078fca1.c)
- [`code/fcn.007eb720.c`](code/fcn.007eb720.c)
- [`code/fcn.007f28b0.c`](code/fcn.007f28b0.c)
- [`code/fcn.00838350.c`](code/fcn.00838350.c)
- [`code/fcn.00955720.c`](code/fcn.00955720.c)
- [`code/fcn.00957a90.c`](code/fcn.00957a90.c)
- [`code/fcn.00977173.c`](code/fcn.00977173.c)
- [`code/fcn.009813e0.c`](code/fcn.009813e0.c)
- [`code/fcn.00982610.c`](code/fcn.00982610.c)
- [`code/fcn.00a197f2.c`](code/fcn.00a197f2.c)

## Behavioral Analysis

This final chunk of disassembly provides a definitive look at the **Dispatcher Mechanism** of the Virtual Machine. While the previous segments revealed the "environment," this section shows the "engine"—the specific way the VM processes its internal instruction set.

Below is the updated analysis incorporating Chunk 14/14 into the existing findings.

---

### Updated Analysis Summary (Chunk 14/14)

#### 1. The Core Dispatcher: Opcode Handling
The logic shown in this segment is a classic example of an **Instruction Dispatcher**. 
*   **Opcode Selection:** The variable `uVar2` serves as the "opcode" fetched from the virtualized code. The series of `if (uVar2 == ...)` statements represent the VM’s internal switch table.
*   **Handler Diversity:** Each branch calls a different function (`fcn.00432760`, `fcn.00432780`, `fcn.0040faa0`, etc.). These are individual "handlers." For example, one might handle an addition, another a memory move, and another a conditional jump.
*   **Proximity of Handlers:** Notice that `fcn.00432760` and `fcn.00432780` are only 20 bytes apart in the binary. This suggests the authors use "handler blocks"—small, specialized chunks of code for very specific operations, likely to make manual analysis tedious by forcing the analyst to jump between dozens of tiny functions.

#### 2. Fallback and Default Logic
The block starting at `fcn.00452ca0` acts as a "default" or "common operation" handler. When `uVar2` does not match specific opcodes like `0x13` or `0x100`, the VM falls back to this logic. This is often used for standard operations that don't require specialized handling, or it may be a way to trap and handle "illegal" instructions within the VM’s environment.

#### 3. Abstracting Complexity
The use of hexadecimal constants (e.g., `0x13`, `0x15`, `0x100`) instead of simple integers is an intentional tactic to distance the code from human-readable logic. By using a large, non-linear range of hex values, the author ensures that an analyst cannot easily guess what each instruction does without mapping out every single jump point in the dispatcher.

---

### Updated Technical Analysis of Obfuscated Patterns

| Pattern | Discovery in Chunk 14 | Technical Significance |
| :--- | :--- | :--- |
| **Opcode Dispatching** | `uVar2` comparisons (0x13, 0x15, etc.) | Confirms the existence of a custom Instruction Set Architecture (ISA). This is the primary "gate" between the VM's logic and its actions. |
| **Handler Proximity** | `fcn.00432760` / `fcn.00432780` | Indicates high-density, specialized handlers. This makes "lifting" the code (translating it back to x86) difficult because one logic flow is fragmented into many small pieces. |
| **Non-Linear Opcode Space** | Use of `0x100`, `0x102` | A common anti-analysis technique used to make the instruction set appear sparse and confusing, preventing simple linear analysis of the dispatch table. |
| **Fall-through Logic** | `fcn.00452ca0` section | Indicates a multi-layered handler approach where "common" instructions are grouped separately from specialized ones. |

---

### Finalized Comprehensive Analysis Summary (All Chunks)

| Category | Status | Technical Detail |
| :--- | :--- | :--- |
| **Obfuscation Type** | **Virtual Machine (VM)** | The malware has been ported into a custom, proprietary architecture. It does not run as standard x86; it runs as "instructions" interpreted by the dispatcher shown in Chunk 14. |
| **Protection Level** | **Enterprise / Professional** | The presence of multi-layered dispatch trees, GDI wrappers (Chunk 13), and anti-decompiler "junk code" (Chunk 13) points to a high-end commercial packer or a very sophisticated custom build. |
| **Anti-Analysis** | **High Complexity** | Includes overlapping instructions, broken control flows, and massive dispatcher tables designed to exhaust human resources and break automated tools like Ghidra/IDA. |
| **Complexity Score** | **Critical (Extreme)** | The "truth" of the malware's behavior is hidden deep within the VM. Standard analysis will only reveal the interpreter; it will not reveal the *intent* of the code until the VM is successfully de-virtualized. |

---

### Final Actionable Recommendations for Incident Response

1.  **Identify the "Unpacker" Moment:** The dispatcher (Chunk 14) is the current hurdle. To find the actual payload, look for where the Dispatcher loop finishes its initial setup and begins executing "malicious" instructions. This often occurs after a long period of repeated calls to the `fcn.00432760` style handlers.
2.  **Scripted Trace Mapping:** Use an emulator (like Unicorn) or a debugger script to log every value of `uVar2`. By mapping every hex code to its corresponding handler, you can create a "Map" of the VM. This allows you to see which opcodes are used most frequently—these are the core logic of the malware.
3.  **Dynamic Instrumentation (Frida/Pin):** Since static analysis of the dispatcher is intentionally "broken," use dynamic instrumentation to hook the entry points of the handlers. If a handler calls `DrawEdge` or `SetFocus`, log those parameters in real-time. This bypasses the complexity of the VM by observing its outputs.
4.  **Memory Dump/Snapshotting:** Instead of trying to decode the VM logic, run the sample in a "heavy" sandbox and dump memory at intervals. Often, even within a VM, the underlying code must eventually move data or call system APIs that can be captured via memory forensics.
5.  **YARA & IOC Generation:** Create YARA rules based on the *dispatcher's* unique signature (the specific sequence of `uVar2` checks). While this won't tell you what the malware does, it will allow you to identify other and variants of the same "packer" family across your network.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behavior observed in your analysis to the corresponding MITRE ATT&CK techniques.

The core behavior identified—the use of a custom Virtual Machine (VM) to hide the malware's true intent—is a sophisticated form of software obfuscation primarily used to hinder both automated tools and manual reverse engineering.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | **Obfuscated Executables** | The use of a custom Instruction Set Architecture (ISA), an instruction dispatcher, and non-linear opcode mapping is a classic technique to hide the program's true logic from static analysis. |
| **T1027.001** | **Packed Executable** | While technically a "packer," the multi-layered dispatcher and "junk code" mentioned are hallmark features of high-end packers (like VMProtect) used to shield malicious code. |

### Analyst Notes:
*   **Virtual Machine Obfuscation:** The specific behavior described (Chunk 14/14) is categorized under **T1027**. In this context, "Virtualization" refers to the software engineering technique where the original x86 instructions are converted into a custom bytecode. This forces an analyst to first de-virtualize the code before the actual malicious behavior can be identified.
*   **Anti-Analysis Correlation:** The "Junk Code," "Broken Control Flows," and "Non-Linear Opcode Space" described in your analysis are specific methods used to achieve the goal of **T1027**. They are designed specifically to exhaust human resources (analyst fatigue) and break automated decompilers like Ghidha or IDA Pro.
*   **Strategic Impact:** Because the behavior is mapped primarily to T1027, any indicators of compromise (IOCs) derived from this sample will likely only relate to the *packer/loader* rather than the *payload*, unless successful de-virtualization occurs.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted threat intelligence. 

Note that while the raw strings contain many terms related to programming libraries (e.g., `AnsiChar`, `HRESULT`), these are flagged as false positives per your instructions and have been excluded.

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Internal Function Offsets (Instruction Dispatcher):** 
    *   `0x00432760`
    *   `0x00432780`
    *   `0x0040faa0`
    *   `0x00452ca0`
*   **VM Opcode Constants:** 
    *   `0x13`
    *   `0x15`
    *   `0x100`
    *   `0x102`
*   **Malware Behavior/Signature:**
    *   **Custom Virtual Machine (VM) Architecture:** The sample utilizes a non-linear opcode space to hide intent. 
    *   **High-Density Handler Blocks:** Use of closely packed functions (e.g., `0x432760` and `0x432780` being only 20 bytes apart) suggests an intentional attempt to hinder automated decompilation.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High (on technical behavior) / Medium (on final payload)

4. **Key evidence**:
*   **Advanced Virtual Machine (VM) Obfuscation:** The sample utilizes a sophisticated custom Instruction Set Architecture (ISA). By running the actual malicious logic inside a proprietary interpreter rather than native x86, it successfully hides its true "intent" from standard decompilers and static analysis tools.
*   **Sophisticated Dispatcher Mechanism:** The identification of a non-linear opcode space (e.g., `0x13`, `0x100`), high-density handler blocks, and "junk code" indicates the use of high-end protection layers (similar to VMProtect or Themida) designed to exhaust human resources during manual analysis.
*   **Loader Characteristic:** Because the core malicious payload is currently encapsulated within a complex VM layer, the sample's immediate function is that of a loader/protector—it acts as a gatekeeper to deliver and hide the final functionality (be it a RAT, Stealer, or Backdoor) until the VM is successfully de-virtualized.
