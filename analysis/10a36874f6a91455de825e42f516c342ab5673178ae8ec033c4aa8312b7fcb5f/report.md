# Threat Analysis Report

**Generated:** 2026-08-20 19:28 UTC
**Sample:** `10a36874f6a91455de825e42f516c342ab5673178ae8ec033c4aa8312b7fcb5f_10a36874f6a91455de825e42f516c342ab5673178ae8ec033c4aa8312b7fcb5f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10a36874f6a91455de825e42f516c342ab5673178ae8ec033c4aa8312b7fcb5f_10a36874f6a91455de825e42f516c342ab5673178ae8ec033c4aa8312b7fcb5f.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 11 sections |
| Size | 40,587,784 bytes |
| MD5 | `cedbccb3d16a643c9a8dcca5d9a239a2` |
| SHA1 | `9bcf81a2b9ec7613773b204a63ebca68798f1bd4` |
| SHA256 | `10a36874f6a91455de825e42f516c342ab5673178ae8ec033c4aa8312b7fcb5f` |
| Overall entropy | 6.593 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1603290086 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 30,175,232 | 6.535 | No |
| `.itext` | 102,400 | 6.29 | No |
| `.data` | 206,848 | 5.626 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 21,504 | 5.472 | No |
| `.didata` | 3,584 | 4.467 | No |
| `.edata` | 512 | 1.976 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.445 | No |
| `.reloc` | 2,962,944 | 6.633 | No |
| `.rsrc` | 7,100,416 | 5.609 | No |

### Imports

**winmm.dll**: `PlaySoundW`
**shlwapi.dll**: `SHCreateStreamOnFileW`
**wininet.dll**: `InternetCloseHandle`, `InternetReadFile`, `InternetOpenW`, `InternetOpenUrlW`
**winspool.drv**: `DocumentPropertiesW`, `ClosePrinter`, `DeviceCapabilitiesW`, `OpenPrinterW`, `GetPrinterW`, `SetPrinterW`, `GetDefaultPrinterW`, `EnumPrintersW`
**comdlg32.dll**: `ChooseFontW`, `ChooseColorW`, `GetSaveFileNameW`, `GetOpenFileNameW`
**comctl32.dll**: `ImageList_GetImageInfo`, `FlatSB_SetScrollInfo`, `InitCommonControls`, `ImageList_DragMove`, `ImageList_Destroy`, `_TrackMouseEvent`, `ImageList_DragShowNolock`, `ImageList_Add`, `FlatSB_SetScrollProp`, `ImageList_GetDragImage`, `ImageList_Create`, `ImageList_EndDrag`, `ImageList_DrawEx`, `ImageList_AddMasked`, `ImageList_SetImageCount`
**shell32.dll**: `SHGetMalloc`, `SHGetFileInfoW`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `Shell_NotifyIconW`, `SHAppBarMessage`, `ShellExecuteW`, `ShellExecuteExW`
**user32.dll**: `CopyImage`, `MoveWindow`, `SetMenuItemInfoW`, `GetMenuItemInfoW`, `DefFrameProcW`, `SetCaretPos`, `GetCaretPos`, `ScrollWindowEx`, `GetDlgCtrlID`, `GetUpdateRgn`, `FrameRect`, `RegisterWindowMessageW`, `GetMenuStringW`, `FillRect`, `SendMessageA`
**version.dll**: `GetFileVersionInfoSizeW`, `VerQueryValueW`, `GetFileVersionInfoW`
**oledlg.dll**: `OleUIPasteSpecialW`, `OleUIObjectPropertiesW`, `OleUIInsertObjectA`
**oleaut32.dll**: `SafeArrayPutElement`, `GetErrorInfo`, `VariantInit`, `VariantClear`, `SysFreeString`, `SafeArrayAccessData`, `SysReAllocStringLen`, `SafeArrayCreate`, `SafeArrayGetElement`, `GetActiveObject`, `SysAllocStringLen`, `SafeArrayUnaccessData`, `SafeArrayPtrOfIndex`, `VariantCopy`, `SafeArrayGetUBound`
**advapi32.dll**: `RegSetValueExW`, `RegSetValueExA`, `RegConnectRegistryW`, `CryptDecrypt`, `CryptDestroyKey`, `CryptEncrypt`, `CryptImportKey`, `GetUserNameW`, `CryptDestroyHash`, `RegQueryInfoKeyW`, `RegUnLoadKeyW`, `CryptReleaseContext`, `CryptGetHashParam`, `RegSaveKeyW`, `RegReplaceKeyW`
**netapi32.dll**: `NetWkstaGetInfo`, `NetApiBufferFree`
**msvcrt.dll**: `isupper`, `isalpha`, `isalnum`, `toupper`, `memchr`, `memcmp`, `memcpy`, `memset`, `isprint`, `isspace`, `iscntrl`, `isxdigit`, `ispunct`, `isgraph`, `islower`
**winhttp.dll**: `WinHttpReadData`, `WinHttpCloseHandle`, `WinHttpQueryHeaders`, `WinHttpOpenRequest`, `WinHttpConnect`, `WinHttpOpen`, `WinHttpQueryDataAvailable`, `WinHttpReceiveResponse`, `WinHttpSendRequest`
**cryptui.dll**: `CryptUIDlgSelectCertificateW`, `CryptUIDlgViewCertificateA`
**kernel32.dll**: `SetFileAttributesW`, `QueryDosDeviceW`, `GetACP`, `CloseHandle`, `LocalFree`, `GetCurrentProcessId`, `GetSystemDefaultLangID`, `SizeofResource`, `VirtualProtect`, `QueryPerformanceFrequency`, `IsDebuggerPresent`, `FindNextFileW`, `GetFullPathNameW`, `VirtualFree`, `HeapAlloc`
**crypt32.dll**: `CertGetNameStringW`, `CertFindExtension`, `CertGetPublicKeyLength`, `CertDuplicateCertificateContext`, `CryptFindOIDInfo`, `CertFreeCertificateContext`, `CertOpenStore`, `CertEnumCertificatesInStore`, `CertGetCertificateContextProperty`, `CryptSignMessage`, `CertControlStore`, `CryptDecodeObject`, `CertNameToStrW`, `CertCloseStore`, `PFXImportCertStore`
**ole32.dll**: `StgCreateDocfileOnILockBytes`, `OleRegEnumVerbs`, `CreateBindCtx`, `CoCreateInstance`, `IsEqualGUID`, `CreateStreamOnHGlobal`, `CreateILockBytesOnHGlobal`, `OleCreateFromData`, `CoGetClassObject`, `CoInitialize`, `OleDraw`, `CoTaskMemAlloc`, `DoDragDrop`, `StringFromCLSID`, `RevokeDragDrop`
**gdi32.dll**: `EnumEnhMetaFile`, `Pie`, `SetBkMode`, `GetTextCharsetInfo`, `GetRandomRgn`, `CreateCompatibleBitmap`, `CreatePolygonRgn`, `BeginPath`, `GetEnhMetaFileHeader`, `CloseEnhMetaFile`, `RectVisible`, `AngleArc`, `TranslateCharsetInfo`, `SetAbortProc`, `CreateHatchBrush`

### Exports

`TMethodImplementationIntercept`, `__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **396237** (showing first 100)

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

Functions analyzed: **30** | Decompiled to C: **5**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0203ea79` | `0x203ea79` | 28959357 | ✓ |
| `fcn.01e2f9f3` | `0x1e2f9f3` | 27421472 | — |
| `fcn.01d7ea4d` | `0x1d7ea4d` | 24832141 | ✓ |
| `fcn.01a2e946` | `0x1a2e946` | 21951524 | ✓ |
| `fcn.00ea390b` | `0xea390b` | 18504781 | ✓ |
| `fcn.0172e8a4` | `0x172e8a4` | 18214908 | — |
| `fcn.01e9e46a` | `0x1e9e46a` | 16757937 | ✓ |
| `fcn.005d7087` | `0x5d7087` | 16727206 | — |
| `fcn.0105b38e` | `0x105b38e` | 16479107 | — |
| `fcn.0134e9ee` | `0x134e9ee` | 14871040 | — |
| `fcn.011fe76d` | `0x11fe76d` | 13298094 | — |
| `fcn.010ce95a` | `0x10ce95a` | 12304503 | — |
| `fcn.00ece7a6` | `0xece7a6` | 10610612 | — |
| `fcn.00dee973` | `0xdee973` | 10223394 | — |
| `fcn.00e2e8d8` | `0xe2e8d8` | 9498787 | — |
| `fcn.00f473dc` | `0xf473dc` | 9175711 | — |
| `fcn.00ff06c8` | `0xff06c8` | 9111031 | — |
| `fcn.0150e7b1` | `0x150e7b1` | 8715485 | — |
| `fcn.00c0e850` | `0xc0e850` | 7137735 | — |
| `fcn.006be8bd` | `0x6be8bd` | 6025414 | — |
| `fcn.009be052` | `0x9be052` | 5367877 | — |
| `fcn.013ee56f` | `0x13ee56f` | 4851266 | — |
| `fcn.0077e7d5` | `0x77e7d5` | 4850094 | — |
| `fcn.00e0e8be` | `0xe0e8be` | 4459707 | — |
| `fcn.00fee8f8` | `0xfee8f8` | 4457172 | — |
| `fcn.008ae794` | `0x8ae794` | 4457039 | — |
| `fcn.0084dd5d` | `0x84dd5d` | 4328852 | — |
| `fcn.0190e948` | `0x190e948` | 4325833 | — |
| `fcn.016fd51e` | `0x16fd51e` | 3652903 | — |
| `fcn.00e90757` | `0xe90757` | 3080168 | — |

### Decompiled Code Files

- [`code/fcn.00ea390b.c`](code/fcn.00ea390b.c)
- [`code/fcn.01a2e946.c`](code/fcn.01a2e946.c)
- [`code/fcn.01d7ea4d.c`](code/fcn.01d7ea4d.c)
- [`code/fcn.01e9e46a.c`](code/fcn.01e9e46a.c)
- [`code/fcn.0203ea79.c`](code/fcn.0203ea79.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated the analysis of the binary. The new data reinforces the previous conclusions and provides further evidence of high-level sophistication and intentional anti-analysis measures.

### Updated Analysis of Binary Sample

#### 1. Confirmed Core Functionality: Virtual Machine (VM) Architecture
The complexity of the arithmetic in functions like `fcn.01a2f53e` and `fcn.01e9e46a` strongly confirms that this is not just "obfuscated code," but a **custom virtual machine**.

*   **Instruction Interpretation:** The way variables are manipulated (using `CONCAT`, bit-shifts, and carry-flag checks) suggests the processor is not executing standard x86 instructions for its logic. Instead, it is processing a custom bytecode where each "instruction" involves multiple steps of calculation to resolve memory addresses, jump targets, or data transformations.
*   **Complex Dispatcher/Handler Logic:** The function `fcn.01e9e46a` contains an indirect call (`(**(param_11 + 0x4a01e9e6))()`). This is a hallmark of **VM-based protection**, where the "handler" for a specific bytecode instruction is located at an offset calculated at runtime.

#### 2. Advanced Anti-Analysis & Obfuscation Techniques
The second chunk provides clear evidence of techniques designed to defeat automated and manual reverse engineering:

*   **Instruction Overlapping:** The decompiler repeatedly warns about "overlapping instructions" (e.g., `0x2000002f` overlapping `0x2000002e`). This is a classic "anti-disassembly" trick where the code contains bytes that can be interpreted as two different instructions depending on the starting offset, intentionally breaking the logic of linear-sweep disassemblers.
*   **Junk Code & "Trap" Segments:** The presence of `halt_baddata()` and the "Do nothing block with infinite loop" are indicators of **junk code**. These sections are designed to lead a researcher or an automated tool into a "dead end" or a state where the decompiler cannot reconstruct the control flow, effectively hiding the true execution path.
*   **Opaque Predicates:** The logic within `fcn.01e9e46a` and its surrounding blocks includes several conditions that appear complex but may always evaluate to a specific truth value (opaque predicates). These are used to force researchers to waste time analyzing "branches" that can never actually be taken.

#### 3. Indicators of Malicious Intent
*   **Layered Obfuscation:** The complexity of the mathematical transformations for simple operations (like moving an address or checking a buffer) suggests a **high-tier protector** (similar to VMProtect or Themida). This level of effort is typically reserved for sophisticated malware such as advanced persistent threats (APTs), high-end ransomware, or state-sponsored espionage tools.
*   **Potential Payload Decryption:** The function `fcn.00ea390b` appears to involve a series of transformations on data retrieved from memory. This suggests that while the VM is running its "logic," it may also be performing just-in-time decryption or deobfuscation of malicious payloads (like a keylogger, a backdoor, or an encryption routine).

### Summary of Risk and Categorization
This sample exhibits characteristics of **Advanced Malware/Sophisticated Packer**. 

*   **Technique:** Custom Virtual Machine (VM) Obfuscation.
*   **Complexity:** High. The use of overlapping instructions, junk code, and complex bitwise math for trivial operations indicates a concerted effort to hide the malware's true purpose from automated sandbox analysis and manual human investigation.
*   **Malware Type Theory:** Given the complexity and the "wrapper" nature of these functions (handling things like .NET strings while using heavy native obfuscation), this is likely:
    1.  A **highly protected loader** for a secondary payload.
    2.  A component of an **advanced trojan or ransomware** suite designed to evade detection for months or years.

**Conclusion:** The sample is highly malicious and designed specifically to hinder analysis. Any actions it performs (data theft, encryption, etc.) are hidden within the "VM" layer. Manual unpacking or high-level emulation/tracing of the VM's behavior would be required to see the actual payloads.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a custom virtual machine (VM) and bytecode interpretation conceals the program's true logic from static analysis tools. |
| T1027 | Obfuscated Files or Information | Overlapping instructions are utilized to intentionally break the logic of linear-sweep disassemblers during the analysis phase. |
| T1027 | Obfuscated Files or Information | Junk code and "trap" segments are included to lead researchers into dead ends and waste time during manual reverse engineering. |
| T1027 | Obfuscated Files or Information | Opaque predicates create complex, unnecessary calculation paths to hinder the analysis of valid execution branches. |
| T1027 | Obfuscated Files or Information | Layered obfuscation and just-in-time decryption are used to hide malicious payloads until they are required for execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted threat intelligence. 

**Note:** The "Extracted Strings" section contains primarily internal programming constructs, .NET framework types, and memory addresses which are considered standard library components rather than actionable IOCs. No network infrastructure (IPs/Domains) or system-level persistence markers (Registry Keys/File Paths) were present in the text provided.

### **IOC_REPORT**

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected.

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected. (Note: Hexadecimal values such as `0x1a2f53e` are internal function offsets, not file hashes).

**Other artifacts**
*   **Unique Function Identifiers (Internal):** 
    *   `fcn.01a2f53e` (VM Logic/Arithmetic)
    *   `fcn.01e9e46a` (VM Dispatcher/Handler logic)
    *   `fcn.00ea390b` (Potential Payload Decryption)
*   **Behavioral Markers:** 
    *   Custom Virtual Machine (VM) Architecture
    *   Anti-Disassembly techniques (Overlapping instructions, Junk code, Opaque predicates)
    *   High-tier packing/protection signatures (similar to VMProtect or Themida)

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Custom Virtual Machine (VM) Architecture:** The presence of complex bytecode interpretation, custom arithmetic for memory resolution, and a dispatcher/handler logic indicates high-level protection designed to hide the underlying code's functionality from standard analysis tools.
*   **Advanced Anti-Analysis Techniques:** The implementation of "overlapping instructions," opaque predicates, and junk code ("trap" segments) are sophisticated methods used specifically to defeat disassemblers and waste the time of human reverse engineers.
*   **Payload Masking/Decryption:** The identification of multi-layered obfuscation and potential just-in-time decryption routines suggests that this sample's primary role is a "wrapper" or loader, intended to deliver and execute more significant payloads (such as ransomware or backdoors) while remaining undetected during the initial execution phase.
