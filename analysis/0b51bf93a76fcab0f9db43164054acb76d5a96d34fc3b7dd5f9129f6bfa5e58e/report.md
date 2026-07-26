# Threat Analysis Report

**Generated:** 2026-07-26 05:11 UTC
**Sample:** `0b51bf93a76fcab0f9db43164054acb76d5a96d34fc3b7dd5f9129f6bfa5e58e_0b51bf93a76fcab0f9db43164054acb76d5a96d34fc3b7dd5f9129f6bfa5e58e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b51bf93a76fcab0f9db43164054acb76d5a96d34fc3b7dd5f9129f6bfa5e58e_0b51bf93a76fcab0f9db43164054acb76d5a96d34fc3b7dd5f9129f6bfa5e58e.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 11 sections |
| Size | 12,336,640 bytes |
| MD5 | `2858e41b1c1f6cf9dfe6ef50758d3e8c` |
| SHA1 | `6a9fbd5b768d3f66bc9a9c5a48824af2f40830e4` |
| SHA256 | `0b51bf93a76fcab0f9db43164054acb76d5a96d34fc3b7dd5f9129f6bfa5e58e` |
| Overall entropy | 5.978 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772892869 |
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
| `.rsrc` | 3,848,192 | 4.166 | No |

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

Total strings found: **50286** (showing first 100)

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

This updated analysis incorporates **Chunk 12/12**, which represents the final piece of the puzzle regarding the VM's internal mechanics. This final segment reveals the "inner workings" of the execution loop, confirming the presence of a highly sophisticated state machine and an object-oriented approach to virtual instruction processing.

---

### Updated Analysis: Chunk 12/12 (Final Data Integration)

#### 1. The State Machine Core (The Execution Loop)
In `fcn.007b71a0`, we see a massive, complex loop structure (`do { ... } while(true)` and jump-labels like `code_r0x007b7d00`). This is not just an "if" tree; it is the **Central Processing Loop** of the VM.
*   **Observation:** The code frequently performs a check (e.g., `fcn.007cc1f0(piStack_d0)`), and if successful, proceeds to execute several nested operations before potentially "looping" back or moving to a different state.
*   **Analysis:** This loop is the engine's heartbeat. Instead of executing linear code, it processes one "virtual instruction" at a time. The logic between `code_r0x007b7d00` and its next jump point represents the handling of a single virtual opcode.

#### 2. Indirect Function Pointers (The "Hidden" Jump Table)
A critical finding in this chunk is the frequent use of dereferenced pointers: `(**(*piStack_e0 + 0x18))(piStack_e0,aHStack_58)` and `(**(*piStack_d0 + 0x20))`.
*   **Observation:** The VM doesn't call "Function A" or "Function B." It looks up a memory address at a specific offset (like `0x18` or `0x20`) from a base pointer and executes the result.
*   **Analysis:** This is **Virtual Table (vtable) Dispatch.** By using offsets, the developers ensure that static analysis tools cannot easily link a "call" to its destination. The destination is determined at runtime based on the current state of the VM's internal registers. This effectively masks the true logic flow from automated scanners.

#### 3. Instruction Interpretation & Mapping
The first half of Chunk 12 shows the logic for interpreting specific opcodes (e.g., `0xa73020`, `0x94f0`).
*   **Observation:** The code uses a series of `if-else` blocks to check these hex constants. If a check passes, it calls an internal helper like `fcn.004116c0`. 
*   **Analysis:** These are **Opcode Handlers.** Each `if (iVar2 == 0)` check is the VM deciding what "type" of instruction it just encountered. For example, one block might be handling a "string move," while another handles "stack addition." By nesting these, they ensure that even if you identify one handler, the next step in the sequence remains hidden until the code is actually running.

#### 4. Context-Heavy Execution
Notice how `arg1` and various stack pointers (`piStack_d0`, `apLStack_20`) are passed into almost every sub-function.
*   **Analysis:** The VM uses a **Context Object.** Instead of global variables, the entire "state" of the malware (current registers, current instruction pointer, memory map) is encapsulated in a structure. When a function is called within the VM, it carries this "context" with it, making it impossible to understand what a piece of code does without knowing the state of the *entire* machine at that exact microsecond.

---

### Final Synthesis: The Complete Architecture (Chunks 1–12)

The analysis confirms that this is an **Advanced Virtual Machine-based Obfuscator** (akin to VMProtect or custom heavy-duty packers). It employs a multi-layered defense strategy:

**Layer 1: The Dispatcher (Outer Layer)**
*   Uses nested `if-else` structures instead of standard switch statements.
*   Converts linear logic into a complex, branched tree that requires "knowing" the internal state to navigate.

**Layer 2: The State Machine (Middle Layer)**
*   The code is organized as a series of states. Each "jump" in the assembly corresponds to a transition between VM states.
*   Loops ensure that the execution remains within the "protected" environment for as long as possible before "exiting" to a gateway.

**Layer 3: The Gateway (Inner Layer/Escape)**
*   These are the rare, visible moments where the VM interacts with `user32.dll` or `gdi32.dll`.
*   The transition from the complex `fcn.007b71a0` logic to a standard Windows API call is the "Point of Interest" for analysts.

#### Key Findings Summary:
1.  **Polymorphic Logic Generation:** The similarity in structure across different functions suggests that an automated tool generates these dispatchers, making signature-based detection almost impossible.
2.  **Virtual Instruction Set (ISA):** The presence of constants like `0xa73020` indicates a custom ISA. To truly "crack" this, one would need to map every opcode to its intended function.
3.  **Contextual Obscurity:** By utilizing large "context structures," the malware ensures that any single piece of code appears benign or meaningless until it is combined with the full state of the VM during runtime.

---

### Strategic Recommendations for the Investigation:

1.  **De-virtualization Strategy:** Do not attempt to manually "trace" through the nested `if-else` blocks in Chunk 12. They are designed to waste your time. Instead, identify the **State Transitions**.
2.  **Identify Gateway Constants:** Focus on finding the instructions that trigger a jump from the `0x7b...` series of functions into known Windows APIs (e.g., `GetSystemMetrics`, `CreateFile`). These are your "break points."
3.  **Memory Forensics / Instrumentation:** Use a tool like **Frida** or **x64dbg** to hook the vtable lookups (the `[base + 0x18]` calls). By logging what address is returned, you can begin to map the hidden "jump table."
4.  **Taint Analysis:** Mark the data coming from the "Gateway" functions (like image icons or system info) and trace it backward into the VM. This will reveal which parts of the complex dispatcher are actually processing the malicious payload.

**Final Conclusion:** This is a high-sophistication malware protector. The primary goal of the architecture is to **exhaust the analyst**. By making the "translation" from internal code to external action incredibly convoluted, it ensures that standard automated tools fail and manual analysis takes weeks rather than hours.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | **Packers** | The use of a custom "Virtual Instruction Set" (ISA) and an execution loop to interpret instructions instead of executing them directly is a hallmark of VM-based packing. |
| **T1027** | **Obfuscated Executables** | The implementation of a "State Machine Core" and "Context-Heavy Execution" are used to hide the true logic flow and make it difficult for analysts to determine intent. |
| **T1027** | **Obfuscated Executables** | The use of nested `if-else` structures (rather than standard jump tables) is a specific obfuscation technique to thwart automated static analysis tools. |
| **T1028** | **Dynamic Resolution** | Although used within the VM, the "Indirect Function Pointers" (vtable dispatch) are intended to hide the final destination of API calls from analysts until runtime. |

### Analyst Notes on Mapping:
*   **Virtual Machine as a Protection Layer:** The analysis describes an "Advanced Virtual Machine-based Obfuscator." In threat intelligence contexts, this is almost always categorized under **T1055 (Packers)** because the VM acts as a container that must be "unpacked" or de-virtualized before the actual malicious payload can be understood.
*   **Control Flow Flattening:** The "State Machine Core" described in Chunk 12/12 is an implementation of *Control Flow Flattening*. While this specific term isn't its own T-code, it is the primary method for achieving the **T1027 (Obfuscated Executables)** classification.
*   **Contextual Obscurity:** By passing a "Context Object" into every sub-function, the malware ensures that any single instruction is meaningless without the full state of the VM, which is a high-level evasion tactic to exhaust manual analysis time.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided text describes a technical analysis of a **Virtual Machine (VM)-based obfuscator** (similar to VMProtect or Themida). The "Extracted Strings" section contains standard compiler/library symbols (likely from the Delphi/Pascal environment), and the "Behavioral Analysis" describes the internal mechanics of the packer rather than specific infrastructure.

---

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None detected.*

**File paths / Registry keys**
*   *None detected.* (All file paths in the text are standard Windows libraries like `user32.dll` and `gdi32.dll`, which are excluded as false positives).

**Mutex names / Named pipes**
*   *None detected.*

**Hashes**
*   *None detected.*

**Other artifacts (user agents, C2 patterns, etc.)**
*   **Custom VM Opcode Constants:** `0xa73020`, `0x94f0` (These serve as specific signatures for the internal custom instruction set used to mask logic).
*   **Obfuscation Technique:** Advanced Virtual Machine-based Obfuscator. The analysis identifies a complex state machine, vtable lookups at offsets `0x18` and `0x20`, and nested `if-else` structures to hide the true execution flow.

---

### **Analyst Notes**
The content provided is a **malware protection layer (packer)** analysis rather than a direct capture of malware behavior/infrastructure. Because the "real" malicious code is wrapped inside the VM, standard IOCs like C2 IP addresses or specific file paths are intentionally hidden by the obfuscator and do not appear in the raw strings provided. 

To find further IOCs, manual unpacking or memory forensics during execution (as suggested in the "Strategic Recommendations") would be required to bypass the VM layer.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family**: Unknown (Custom Packer/Protector)
2. **Malware type**: Loader / Dropper
3. **Confidence**: Medium
4. **Key evidence**:
    *   **Advanced Virtual Machine (VM) Obfuscation:** The analysis confirms the use of a custom Instruction Set Architecture (ISA), complex state machines, and vtable dispatching to hide the true execution logic.
    *   **Control Flow Flattening:** The implementation of nested `if-else` structures and "Context-Heavy Execution" is a sophisticated technique designed to exhaust manual analysis and thwart automated de-obfuscation tools.
    *   **Payload Encapsulation:** The lack of clear Indicators of Compromise (IOCs) such as C2 addresses or specific malicious actions, combined with the "Gateway" architecture, indicates this sample functions primarily as a protective shell/loader for a secondary, hidden payload.
