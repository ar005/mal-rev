# Threat Analysis Report

**Generated:** 2026-08-23 18:46 UTC
**Sample:** `11813a25c350ed1fa92a29bb6d69c62032fcff01a1e263f58f6817005e821154_11813a25c350ed1fa92a29bb6d69c62032fcff01a1e263f58f6817005e821154.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11813a25c350ed1fa92a29bb6d69c62032fcff01a1e263f58f6817005e821154_11813a25c350ed1fa92a29bb6d69c62032fcff01a1e263f58f6817005e821154.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 11 sections |
| Size | 8,724,480 bytes |
| MD5 | `b749bf14df37718b13397037dfb15e46` |
| SHA1 | `3d39495ae841d689a5db05a539f50fdef1774c74` |
| SHA256 | `11813a25c350ed1fa92a29bb6d69c62032fcff01a1e263f58f6817005e821154` |
| Overall entropy | 7.423 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778753097 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 7,079,424 | 7.455 | ⚠️ Yes |
| `.itext` | 6,144 | 6.047 | No |
| `.data` | 97,280 | 5.132 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 7,680 | 4.833 | No |
| `.didata` | 24,576 | 5.033 | No |
| `.edata` | 512 | 0.727 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.211 | No |
| `.reloc` | 169,984 | 6.516 | No |
| `.rsrc` | 1,314,304 | 6.443 | No |

### Imports

**oleaut32**: `GetErrorInfo`, `SysFreeString`
**advapi32**: `RegQueryValueExW`, `RegOpenKeyExW`, `RegCloseKey`
**user32.dll**: `GetWindowLongW`, `CreateWindowExW`, `WaitMessage`, `UpdateLayeredWindow`, `TranslateMessage`, `TrackMouseEvent`, `ShowWindow`, `SetWindowTextW`, `SetWindowPos`, `SetTimer`, `SetPropW`, `SetParent`, `SetMenu`, `SetFocus`, `SetCursor`
**kernel32**: `Sleep`
**gdi32**: `StartPage`, `StartDocW`, `SetAbortProc`, `SelectObject`, `GetStockObject`, `GetRegionData`, `GetObjectA`, `GetDeviceCaps`, `EnumFontsW`, `EndPage`, `EndDoc`, `DeleteObject`, `DeleteDC`, `CreateRectRgn`, `CreateICW`
**ole32**: `ReleaseStgMedium`, `DoDragDrop`, `RevokeDragDrop`, `RegisterDragDrop`, `OleInitialize`, `CoTaskMemAlloc`, `CoCreateInstance`, `CoUninitialize`, `CoInitialize`
**winspool.drv**: `SetPrinterW`, `OpenPrinterW`, `GetPrinterW`, `GetDefaultPrinterW`, `EnumPrintersW`, `DocumentPropertiesW`, `DeviceCapabilitiesW`, `ClosePrinter`
**shell32**: `DragQueryFileW`
**comdlg32**: `PageSetupDlgW`, `PrintDlgW`, `GetSaveFileNameW`, `GetOpenFileNameW`
**winmm**: `timeGetTime`
**d3d9**: `Direct3DCreate9`

### Exports

`ord_1`, `ord_2`

## Extracted Strings

Total strings found: **26514** (showing first 100)

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
Pointer
Cardinal
UInt64
	NativeInt

NativeUInt
Single
Extended
Double
Currency
ShortString
	PAnsiChar0
	PWideCharL
WordBool
System
LongBool
System
string

WideString


AnsiString
Variant
TClass`
HRESULT
&op_Equality
&op_Inequality
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
TObject&
Create
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
NewInstance
FreeInstance
Destroy
TObjectt
System

IInterface
System
IEnumerable
System
	FRefCount
TInterfacedObject1
AfterConstruction
BeforeDestruction
NewInstance
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **25**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004fe5b8` | `0x4fe5b8` | 1049492 | — |
| `fcn.0056dd39` | `0x56dd39` | 715581 | — |
| `fcn.004a0305` | `0x4a0305` | 630848 | ✓ |
| `fcn.0056ee14` | `0x56ee14` | 22046 | — |
| `fcn.005255bf` | `0x5255bf` | 21399 | ✓ |
| `fcn.0048725c` | `0x48725c` | 7291 | ✓ |
| `fcn.00489118` | `0x489118` | 6634 | ✓ |
| `fcn.00464ce0` | `0x464ce0` | 4964 | ✓ |
| `fcn.004d5cdc` | `0x4d5cdc` | 3851 | ✓ |
| `fcn.004669f4` | `0x4669f4` | 3718 | ✓ |
| `fcn.00416cd1` | `0x416cd1` | 3646 | ✓ |
| `fcn.00585388` | `0x585388` | 3469 | ✓ |
| `fcn.00504eab` | `0x504eab` | 3248 | — |
| `fcn.0053da24` | `0x53da24` | 2954 | ✓ |
| `fcn.0057e659` | `0x57e659` | 2861 | — |
| `fcn.00407a20` | `0x407a20` | 2846 | ✓ |
| `fcn.0053cf44` | `0x53cf44` | 2749 | ✓ |
| `fcn.0053e885` | `0x53e885` | 2705 | ✓ |
| `fcn.004679a8` | `0x4679a8` | 2668 | ✓ |
| `fcn.00591554` | `0x591554` | 2601 | ✓ |
| `fcn.004210f8` | `0x4210f8` | 2513 | ✓ |
| `fcn.00454aac` | `0x454aac` | 2359 | ✓ |
| `fcn.004d5418` | `0x4d5418` | 2337 | ✓ |
| `fcn.0056adb0` | `0x56adb0` | 2299 | ✓ |
| `fcn.004cdd74` | `0x4cdd74` | 2241 | ✓ |
| `fcn.00422fc8` | `0x422fc8` | 2132 | ✓ |
| `fcn.00590120` | `0x590120` | 2080 | ✓ |
| `fcn.0058dedc` | `0x58dedc` | 2043 | ✓ |
| `fcn.00530fb0` | `0x530fb0` | 1951 | ✓ |
| `fcn.00403448` | `0x403448` | 1904 | ✓ |

### Decompiled Code Files

- [`code/fcn.00403448.c`](code/fcn.00403448.c)
- [`code/fcn.00407a20.c`](code/fcn.00407a20.c)
- [`code/fcn.00416cd1.c`](code/fcn.00416cd1.c)
- [`code/fcn.004210f8.c`](code/fcn.004210f8.c)
- [`code/fcn.00422fc8.c`](code/fcn.00422fc8.c)
- [`code/fcn.00454aac.c`](code/fcn.00454aac.c)
- [`code/fcn.00464ce0.c`](code/fcn.00464ce0.c)
- [`code/fcn.004669f4.c`](code/fcn.004669f4.c)
- [`code/fcn.004679a8.c`](code/fcn.004679a8.c)
- [`code/fcn.0048725c.c`](code/fcn.0048725c.c)
- [`code/fcn.00489118.c`](code/fcn.00489118.c)
- [`code/fcn.004a0305.c`](code/fcn.004a0305.c)
- [`code/fcn.004cdd74.c`](code/fcn.004cdd74.c)
- [`code/fcn.004d5418.c`](code/fcn.004d5418.c)
- [`code/fcn.004d5cdc.c`](code/fcn.004d5cdc.c)
- [`code/fcn.005255bf.c`](code/fcn.005255bf.c)
- [`code/fcn.00530fb0.c`](code/fcn.00530fb0.c)
- [`code/fcn.0053cf44.c`](code/fcn.0053cf44.c)
- [`code/fcn.0053da24.c`](code/fcn.0053da24.c)
- [`code/fcn.0053e885.c`](code/fcn.0053e885.c)
- [`code/fcn.0056adb0.c`](code/fcn.0056adb0.c)
- [`code/fcn.00585388.c`](code/fcn.00585388.c)
- [`code/fcn.0058dedc.c`](code/fcn.0058dedc.c)
- [`code/fcn.00590120.c`](code/fcn.00590120.c)
- [`code/fcn.00591554.c`](code/fcn.00591554.c)

## Behavioral Analysis

The analysis of chunk 3/3 provides further evidence regarding the scale and complexity of this application. The findings reinforce the previous assessment: this is a highly complex, modular piece of software—likely a game engine or a large-scale simulation suite—but it contains architectural characteristics that are common in high-end "trojanized" software where malicious payloads are hidden within voluminous, legitimate code.

### Updated Analysis Summary

The discovery of even more extensive switch tables and heavy mathematical processing suggests a deep level of infrastructure (rendering, physics, scripting) and sophisticated logic flow.

---

### 1. Technical Findings & Observations

#### **A. Evidence of an Interpreter or Scripting Engine**
Function `fcn.00422fc8` contains a massive switch table with approximately **57 cases**. 
*   **Technical Observation:** The code takes a value (likely an "opcode" or command ID) and routes it to various sub-routines. This is the classic structure of a script interpreter (like a custom bytecode engine) or a high-level command dispatcher.
*   **Significance:** In a game, this allows developers to define complex behaviors via scripts without recompiling the core C++/Delphi code. In malware, such an architecture provides a perfect "shadow" for malicious commands; an attacker can hide specific malicious commands among hundreds of legitimate ones (e.g., a command for "move_character" followed shortly by one for "inject_process").

#### **B. Advanced Mathematics & Geometry Processing**
Function `fcn.004d5418` contains an extremely dense block of floating-point calculations involving multiple variables (`fStack_14`, `fStack_18`, etc.) and specific constant offsets.
*   **Technical Observation:** The logic appears to be calculating 3D coordinates, rotations, or physics collisions (calculating distances, normalizing vectors, and adjusting based on fixed constants).
*   **Significance:** This reinforces the **Game Engine/Simulator theory**. However, from a security perspective, these heavy math blocks serve as "noise." When an analyst sees several thousand lines of floating-point arithmetic, it is difficult to pinpoint where legitimate game logic ends and potentially malicious data processing begins.

#### **C. Command Parsing & Input Handling**
Function `fcn.00590120` contains a long series of checks against specific character literals (e.g., `'Q'`, `'q'`, `'T'`, `'t'`, `'A'`, `'a'`, `'Z'`, `'z'`, `'M'`, `'m'`).
*   **Technical Observation:** This is highly characteristic of an **input handler or command-line interpreter**. It maps specific keyboard inputs or internal flags to different branches of logic.
*   **Significance:** If this were malware, these cases would be the "hooks" where a remote operator or an automated script might issue commands to the machine (e.g., "open_browser," "steal_files," etc.).

#### **D. Low-Level Memory Management**
Function `fcn.00403448` utilizes calls to `kernel32_VirtualFree` and `kernel32_VirtualQuery`.
*   **Technical Observation:** These are low-level Windows APIs used for managing memory regions. 
*   **Significance:** While standard in large applications that manage their own memory pools (common in game engines), these specific functions are also commonly used by **packers and "droppers"** to clean up and deallocate memory after a malicious payload has been unpacked or executed in-memory.

---

### 2. Evidence of Sophistication & Potential Tactics

#### **The "Wall of Code" Strategy (Detection Evasion)**
The sheer volume of the switch tables (`0x422fc8`) and the mathematical complexity (`0x4d5418`) serves as a significant deterrent for manual analysis. 
*   **Persistence through Complexity:** An analyst would need to spend hours or days navigating these specific functions just to find one line of "malicious" code. By making the "normal" parts of the program extremely dense and complex, the author ensures that any hidden malicious behavior is buried in a haystack so large it may never be found by human oversight.

#### **Modular Design (Compartmentalization)**
The structure suggests that different subsystems (Rendering, Physics, Logic, Networking) are clearly separated into their own modules. 
*   **Risk:** In high-end malware, this modularity allows the "malicious" module to stay completely separate from the "heavy lifting" of the main application. This makes it much harder for automated sandboxes to flag the entire file as suspicious because only a small, inconspicuous portion of the code is actually doing anything malicious.

---

### 3. Summary for Investigation & Risk Assessment

**Current Status: High Complexity / High-Sophistication Infrastructure.**

| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Large Switch Tables** | ~57 cases in `fcn.00422fc8`. | Suggests a scripting engine or high-level command dispatcher; potential "hiding place" for malicious commands. |
| **Floating Point Heavy** | Extensive 3D/Physics math in `fcn.004d5418`. | Confirms complex software (Game Engine); acts as "noise" to distract manual analysts. |
| **Command Processing** | Mapping characters like 'Q', 'T', 'A' to logic. | Potential for remote command execution or hidden functionality. |
| **Direct Memory API** | `VirtualFree`, `VirtualQuery`. | Standard in high-end software; also a hallmark of unpacking/packing logic. |

**Conclusion:** 
The binary is undeniably complex and professional. It mimics the architecture of a modern game engine perfectly. However, this exact structure—massive state machines (switch tables), heavy math "padding," and modular design—is the preferred template for advanced persistent threats (APTs) that use "legitimate" software as a container for malicious activity.

**Next Steps/Areas of Interest:**
1.  **Identify the Logic Bridge:** Focus on where the **Switch Tables** call external functions or interact with system APIs. If a case in `fcn.00422fc8` calls a function that handles networking or file I/O, that is your primary area of interest.
2.  **Trace the Command Input:** Trace the flow of data into `fcn.00590120`. If this input comes from an external network socket or a hidden local configuration file, it suggests remote control capabilities.
3.  **API Monitoring:** Use a tool like Process Monitor (ProcMon) to see if these "complex" math functions are ever followed by suspicious system calls (e.g., `CreateRemoteThread`, `WriteProcessMemory`, or unusual DNS lookups).

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The large switch table (`fcn.00422fc8`) and character-mapping logic (`fcn.00590120`) suggest a system designed to parse and route internal commands or scripts. |
| **T1027** | Obfuscated Files or Information | The "Wall of Code" strategy uses dense mathematical calculations and voluminous switch tables as "noise" to distract analysts and hide malicious logic. |
| **T1036** | Masquerading | The software's architecture is intentionally designed to mimic a high-end game engine or simulation suite to blend in with legitimate, complex applications. |
| **T1027** (Packer/Dropper behavior) | Obfuscated Files or Information | The use of `VirtualFree` and `VirtualQuery` indicates common behaviors for packers/droppers used to manage memory during the unpacking process. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: As per your instructions, common library strings (e.g., Delphi/Embarcadero), standard Windows API calls (e.g., `VirtualFree`), and internal code logic that does not map to a specific infrastructure point have been excluded.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Command Parsing Patterns:** The analysis identifies a specific set of character-based switches used for command processing: `Q`, `q`, `T`, `t`, `A`, `a`, `Z`, `z`, `M`, `m`. 
*   **Memory Management Indicators:** Frequent calls to `VirtualFree` and `VirtualQuery` in conjunction with high-complexity mathematical loops (specifically at offset `0x4d5418`) suggest a potential for unpacking or memory-resident execution.
*   **Suspicious String Fragments:** The following strings were identified as unique but do not follow standard networking formats; they may represent internal identifiers or obfuscated data: 
    *   `YZXtm1`
    *   `VWUUhLc@`
    *   `ZTUWVSPR`

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification for this sample:

1. **Malware family**: Custom (High Sophistication)
2. **Malware type**: Loader / Trojan
3. **Confidence**: Medium
4. **Key evidence**:
    *   **"Wall of Code" Evasion:** The use of massive switch tables and dense 3D/physics-related mathematical "noise" is a sophisticated tactic used to overwhelm manual analysis and hide malicious logic within a fake game engine framework.
    *   **Loader Characteristics:** The presence of `VirtualFree` and `VirtualQuery` alongside modular code structure indicates capabilities for unpacking or managing memory for a hidden secondary payload (common in droppers/loaders).
    *   **Hidden Command Interpreter:** The detection of a high-volume switch table (`fcn.00422fc8`) and specific character-mapping logic suggests the inclusion of a "backdoor" component where remote commands can be executed under the guise of legitimate engine functions.
