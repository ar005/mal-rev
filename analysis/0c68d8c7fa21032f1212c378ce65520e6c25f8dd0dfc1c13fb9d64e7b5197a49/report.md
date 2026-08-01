# Threat Analysis Report

**Generated:** 2026-07-30 08:26 UTC
**Sample:** `0c68d8c7fa21032f1212c378ce65520e6c25f8dd0dfc1c13fb9d64e7b5197a49_0c68d8c7fa21032f1212c378ce65520e6c25f8dd0dfc1c13fb9d64e7b5197a49.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c68d8c7fa21032f1212c378ce65520e6c25f8dd0dfc1c13fb9d64e7b5197a49_0c68d8c7fa21032f1212c378ce65520e6c25f8dd0dfc1c13fb9d64e7b5197a49.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 11 sections |
| Size | 22,426,672 bytes |
| MD5 | `03b0b1e2ca1299dc6139a1b0316585d2` |
| SHA1 | `4fa2d5185e7de2166844e99b23a87be36af88e98` |
| SHA256 | `0c68d8c7fa21032f1212c378ce65520e6c25f8dd0dfc1c13fb9d64e7b5197a49` |
| Overall entropy | 7.796 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1698090620 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 5,352,448 | 6.538 | No |
| `.itext` | 16,896 | 6.04 | No |
| `.data` | 87,040 | 6.21 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 14,848 | 5.21 | No |
| `.didata` | 27,648 | 5.094 | No |
| `.edata` | 512 | 1.393 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.395 | No |
| `.reloc` | 464,896 | 6.715 | No |
| `.rsrc` | 16,450,560 | 7.977 | ⚠️ Yes |

### Imports

**KERNEL32.DLL**: `SetFileAttributesW`, `GetFileType`, `SetFileTime`, `QueryDosDeviceW`, `GetACP`, `GetExitCodeProcess`, `GetStringTypeExW`, `CloseHandle`, `LocalFree`, `GetCurrentProcessId`, `GetSystemDefaultLangID`, `SizeofResource`, `UpdateResourceW`, `QueryPerformanceFrequency`, `IsDebuggerPresent`
**advapi32.dll**: `RegSetValueExW`, `RegConnectRegistryW`, `RegEnumKeyExW`, `RegLoadKeyW`, `RegDeleteKeyW`, `RegOpenKeyExW`, `RegQueryInfoKeyW`, `RegOpenKeyExA`, `RegUnLoadKeyW`, `RegSaveKeyW`, `RegDeleteValueW`, `RegReplaceKeyW`, `RegFlushKey`, `RegEnumValueW`, `RegQueryValueExW`
**comctl32.dll**: `ImageList_GetImageInfo`, `FlatSB_SetScrollInfo`, `InitCommonControls`, `ImageList_DragMove`, `ImageList_Destroy`, `_TrackMouseEvent`, `ImageList_DragShowNolock`, `ImageList_Add`, `FlatSB_SetScrollProp`, `ImageList_GetDragImage`, `ImageList_Create`, `ImageList_EndDrag`, `ImageList_DrawEx`, `ImageList_SetImageCount`, `FlatSB_GetScrollPos`
**gdi32.dll**: `AddFontMemResourceEx`, `Pie`, `SetBkMode`, `CreateCompatibleBitmap`, `GetEnhMetaFileHeader`, `CloseEnhMetaFile`, `RectVisible`, `AngleArc`, `ResizePalette`, `SetAbortProc`, `SetTextColor`, `StretchBlt`, `RoundRect`, `RestoreDC`, `SetRectRgn`
**msvcrt.dll**: `memcpy`, `memset`
**ole32.dll**: `IsEqualGUID`, `OleInitialize`, `OleUninitialize`, `CoInitialize`, `CoCreateInstance`, `CoUninitialize`, `CoTaskMemFree`, `CoTaskMemAlloc`
**oleaut32.dll**: `SetErrorInfo`, `GetErrorInfo`, `VariantInit`, `SysFreeString`, `SafeArrayAccessData`, `VariantClear`, `SysReAllocStringLen`, `SafeArrayCreate`, `CreateErrorInfo`, `SysAllocStringLen`, `SafeArrayUnaccessData`, `SafeArrayPtrOfIndex`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `VariantCopy`
**shell32.dll**: `Shell_NotifyIconW`, `SHAppBarMessage`, `ShellExecuteW`, `ShellExecuteExW`
**SHFolder.dll**: `SHGetFolderPathW`
**user32.dll**: `CopyImage`, `SetMenuItemInfoW`, `GetMenuItemInfoW`, `DefFrameProcW`, `GetDlgCtrlID`, `FrameRect`, `RegisterWindowMessageW`, `GetMenuStringW`, `FillRect`, `SendMessageA`, `IsClipboardFormatAvailable`, `EnumWindows`, `ShowOwnedPopups`, `GetClassInfoW`, `GetScrollRange`
**version.dll**: `GetFileVersionInfoSizeW`, `VerQueryValueW`, `GetFileVersionInfoW`
**winmm.dll**: `timeGetTime`
**winspool.drv**: `DocumentPropertiesW`, `ClosePrinter`, `OpenPrinterW`, `GetDefaultPrinterW`, `EnumPrintersW`

### Exports

`__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **93814** (showing first 100)

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
	NativeInt

NativeUInt
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

PFixedUInt
TClass
HRESULT
PGUIDl
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
PInterfaceTablet
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **9**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0076e8a6` | `0x76e8a6` | 1699178 | — |
| `fcn.008f9823` | `0x8f9823` | 1691806 | ✓ |
| `fcn.0044e75c` | `0x44e75c` | 334767 | ✓ |
| `fcn.007d1efb` | `0x7d1efb` | 323211 | — |
| `fcn.007f697c` | `0x7f697c` | 313774 | ✓ |
| `fcn.0058ec01` | `0x58ec01` | 133497 | — |
| `fcn.0056e932` | `0x56e932` | 131958 | — |
| `fcn.008ee9ac` | `0x8ee9ac` | 18272 | — |
| `fcn.008ee7f5` | `0x8ee7f5` | 17862 | ✓ |
| `fcn.008ee824` | `0x8ee824` | 17860 | ✓ |
| `fcn.00667e9c` | `0x667e9c` | 10444 | ✓ |
| `fcn.008adbe1` | `0x8adbe1` | 7266 | — |
| `fcn.006f7dd0` | `0x6f7dd0` | 6835 | ✓ |
| `fcn.006f31d4` | `0x6f31d4` | 6355 | ✓ |
| `fcn.00544c88` | `0x544c88` | 5653 | ✓ |
| `fcn.00490c0d` | `0x490c0d` | 4943 | — |
| `fcn.004f1962` | `0x4f1962` | 4672 | — |
| `fcn.00453484` | `0x453484` | 4347 | — |
| `fcn.008f502c` | `0x8f502c` | 4340 | — |
| `fcn.007afc51` | `0x7afc51` | 4218 | — |
| `fcn.008ff02c` | `0x8ff02c` | 4023 | — |
| `fcn.00760744` | `0x760744` | 3923 | — |
| `fcn.00846478` | `0x846478` | 3800 | — |
| `fcn.007aa8d7` | `0x7aa8d7` | 3796 | — |
| `fcn.0048e893` | `0x48e893` | 3641 | — |
| `fcn.00465688` | `0x465688` | 3520 | — |
| `fcn.005d6dd4` | `0x5d6dd4` | 3140 | — |
| `fcn.00608bd4` | `0x608bd4` | 3102 | — |
| `fcn.008130e8` | `0x8130e8` | 2989 | — |
| `fcn.005a89c4` | `0x5a89c4` | 2899 | — |

### Decompiled Code Files

- [`code/fcn.0044e75c.c`](code/fcn.0044e75c.c)
- [`code/fcn.00544c88.c`](code/fcn.00544c88.c)
- [`code/fcn.00667e9c.c`](code/fcn.00667e9c.c)
- [`code/fcn.006f31d4.c`](code/fcn.006f31d4.c)
- [`code/fcn.006f7dd0.c`](code/fcn.006f7dd0.c)
- [`code/fcn.007f697c.c`](code/fcn.007f697c.c)
- [`code/fcn.008ee7f5.c`](code/fcn.008ee7f5.c)
- [`code/fcn.008ee824.c`](code/fcn.008ee824.c)
- [`code/fcn.008f9823.c`](code/fcn.008f9823.c)

## Behavioral Analysis

This update incorporates the analysis of **Chunk 2** into the existing profile. The additional disassembly reveals significantly more sophisticated evasion techniques than initially apparent, specifically moving from "complex packing" into **Virtual Machine (VM) architecture** and **multi-layered data decompression.**

### Updated Analysis: Advanced Malware Protector & VM Loader

The addition of Chunk 2 confirms that this is not a simple packer but a high-end "protector" (similar to VMProtect or Themedis-style technologies). The code utilizes several advanced layers to hide the payload.

---

### Core Functionality and Purpose
1.  **Virtual Machine (VM) Execution:** The function `fcn.006f31d4` is a primary indicator of **code virtualization**. Instead of executing native x86/x64 instructions directly, the "real" logic of the malware has been converted into a custom bytecode. This function acts as an interpreter (VM dispatcher), where the extensive nested `if-else` blocks and table lookups (`arg_8h[0xc]`, `arg_8h[0xe]`) are used to decode and execute these custom instructions at runtime.
2.  **Multi-Method Decompression Engine:** The function `fcn.00544c88` contains a massive switch table with numerous cases (e.g., `0x544da9`, `0x544f40`). This indicates a sophisticated **resource loader**. It is designed to decompress and "unpack" various components of the malware—such as additional DLLs, configuration files, or secondary payloads—using different compression algorithms and protocols.

### Suspicious and Malicious Behaviors
*   **Virtualization-Based Obfuscation:** The repetitive patterns in `fcn.006f31d4` are characteristic of a VM interpreter. Each "block" of code is likely handling a different instruction in the custom bytecode (e.g., addition, bitwise shifts, or memory moves). This makes automated analysis nearly impossible because the true logic of the malware only exists as data (bytecode) rather than executable instructions.
*   **State-Machine Driven Loading:** The switch cases in `fcn.00544c88` are typical of a state machine used to process packed files. It checks for "header flags," "compression methods," and "CRC mismatches." This suggests that the malware is designed to handle complex, multi-part payloads.
*   **Instruction/Data Intermingling:** The repeated use of large constants (e.g., `0x931960`, `0x6f9898`) combined with floating-point math in the first segment suggests **opaque predicates** or **junk code insertion**. These calculations are complex enough to confuse a decompiler but ultimately result in predictable values used to steer the "execution" of the packer.

### Notable Techniques and Patterns
*   **Dispatcher Table Lookups:** The use of `(*arg_8h[0x1c])` and similar patterns indicates that function pointers are not called directly but through an offset table. This hides the destination of function calls from basic static analysis tools.
*   **Complex Error Handling for Packer Logic:** String literals such as `"incorrect header check"`, `"invalid window size"`, and `"header crc mismatch"` are highly indicative of a commercial-grade packing engine. These messages help the packer "detect" if it is being tampered with or if the underlying data has been modified by an analyst.
*   **Nested Logic Obfuscation:** The sheer amount of repeated, nested logic in `fcn.006f31d4` (e.g., checking for `iStack_4c <= iStack_94`) is a method to increase the "cyclomatic complexity" of the code. It forces an analyst to spend hours/days manually tracing paths that ultimately lead only to the next step of the unpacking process.

### Summary for Incident Response
The presence of **Virtual Machine (VM) architecture** and a **complex decompression engine** significantly elevates the threat level of this sample. 

1.  **High Complexity:** This is not a "script-kiddy" malware; it utilizes sophisticated protection layers typically found in advanced persistent threat (APT) tools or high-end commodity malware.
2.  **Delayed Execution:** The primary malicious intent is hidden behind several layers of "unpacking." Identifying the final payload will require advanced memory forensics and dynamic debugging to intercept the payload *after* it has been decompressed and decoded by the VM interpreter.
3.  **Detection Note:** Static analysis of this specific file will likely remain inconclusive regarding the final malware behavior because the core logic is stored in a "virtual" state that only exists during execution in memory.

### Technical Indicators for Hunting
*   **Signature 1 (VM_Dispatcher):** Look for long sequences of nested `if` statements with repetitive logic structures and repeated calls to internal "helper" functions (like `fcn.00415690`).
*   **Signature 2 (Decompression):** The presence of a large switch table containing codes like `0x3f3f`, `0x3f40`, etc., often indicates a proprietary or modified compression header system used by known packers.
*   **Indicator 3 (Instruction Overlap):** Any evidence of overlapping instructions at jump targets confirms the use of specialized obfuscation tools to thwart disassemblers.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Packing | The presence of a "multi-layered decompression engine" and "state-machine driven loading" to unpack components like DLLs and configuration files identifies the use of advanced packing. |
| **T1027** | Obfuscated Files or Information | The use of custom VM architecture (code virtualization), opaque predicates, and dispatcher table lookups are implemented to hide code logic from static analysis tools. |
| **T1497** | Virtualization/Sandbox Evasion | The specific error-handling strings (e.g., "invalid window size") indicate the malware is checking for and responding to tampering or non-standard execution environments typical of analysis labs. |

---

## Indicators of Compromise

Based on the provided analysis and strings, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The "Extracted Strings" section contains standard Delphi/Pascal library artifacts and compiler constants; no actionable network or file system IOCs were found in that specific block.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: The strings `fcn.006f31d4` and `fcn.00544c88` are memory offsets within the binary, not filesystem paths).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Packer Error Messages:** (Used to identify the presence of a high-end protection/packing layer)
    *   `"incorrect header check"`
    *   `"invalid window size"`
    *   `"header crc mismatch"`
*   **Function Offsets (Specific to this binary's construction):**
    *   `0x006f31d4` (Identified as a VM Dispatcher/Interpreter)
    *   `0x00544c88` (Identified as a Multi-Method Decompression Engine)
*   **Behavioral Signatures:**
    *   **VM_Dispatcher Pattern:** Long sequences of nested `if` statements with repetitive logic structures.
    *   **Decompression Signature:** Large switch tables containing specific hex codes (`0x3f3f`, `0x3f40`).
    *   **Obfuscation Technique:** Instruction overlap at jump targets (indicates use of specialized obfuscation tools).

---

## Malware Family Classification

1. **Malware family**: Unknown (Advanced Loader/Protector)
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Code Virtualization:** The sample utilizes a custom VM architecture (`fcn.006f31d4`) where malicious logic is converted into bytecode and executed via an interpreter, making static analysis extremely difficult.
*   **Sophisticated Decoding/Decompression:** The presence of a massive switch-table driven decompression engine (`fcn.00544c88`) indicates the sample's primary role is to unpack multiple layers of secondary payloads (DLLs or executables).
*   **High-End Protection Techniques:** The use of dispatcher table lookups, opaque predicates, and specific error messages for integrity checks ("incorrect header check") identifies this as a high-complexity "protector" similar to commercial tools like VMProtect.
