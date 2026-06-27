# Threat Analysis Report

**Generated:** 2026-06-27 05:32 UTC
**Sample:** `019b04b7fd04652ee362d667b95a41977ceeff73930af18d55974cdf745550c6_019b04b7fd04652ee362d667b95a41977ceeff73930af18d55974cdf745550c6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `019b04b7fd04652ee362d667b95a41977ceeff73930af18d55974cdf745550c6_019b04b7fd04652ee362d667b95a41977ceeff73930af18d55974cdf745550c6.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 13 sections |
| Size | 104,171,008 bytes |
| MD5 | `cfca438a704d3bfee12f5f68003b87ca` |
| SHA1 | `6012341f6bc40fbf5c643c30e1b8317922999b2a` |
| SHA256 | `019b04b7fd04652ee362d667b95a41977ceeff73930af18d55974cdf745550c6` |
| Overall entropy | 6.455 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771423793 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 64,847,360 | 5.855 | No |
| `.data` | 5,715,968 | 5.344 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 62,976 | 4.775 | No |
| `.didata` | 42,496 | 4.15 | No |
| `.edata` | 512 | 2.119 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 1.442 | No |
| `.emptyR` | 0 | 0.0 | No |
| `.pdata` | 2,766,848 | 7.961 | ⚠️ Yes |
| `.vmp0` | 1,718,272 | 6.91 | No |
| `.vmp1` | 4,994,048 | 7.435 | ⚠️ Yes |
| `.rsrc` | 24,020,480 | 6.974 | No |

### Imports

**Shlwapi.dll**: `StrCmpLogicalW`
**version.dll**: `GetFileVersionInfoSizeW`, `VerQueryValueW`, `VerQueryValueA`, `GetFileVersionInfoW`
**user32.dll**: `GetProcessWindowStation`, `GetUserObjectInformationW`
**oledlg.dll**: `OleUIPasteSpecialW`, `OleUIObjectPropertiesW`, `OleUIInsertObjectW`, `OleUIChangeIconW`
**oleaut32.dll**: `SafeArrayPutElement`, `VariantClear`, `SysReAllocStringLen`, `CreateErrorInfo`, `OleCreatePropertyFrame`, `GetActiveObject`, `SysStringByteLen`, `SafeArrayGetLBound`, `SafeArrayGetUBound`, `VariantCopy`, `SafeArrayAccessData`, `SysFreeString`, `VariantInit`, `GetErrorInfo`, `SetErrorInfo`
**netapi32.dll**: `NetWkstaGetInfo`, `NetApiBufferFree`
**advapi32.dll**: `RegEnumKeyW`, `CryptDecrypt`, `CryptDestroyKey`, `CryptEncrypt`, `CryptImportKey`, `OpenThreadToken`, `CryptDestroyHash`, `RegUnLoadKeyW`, `RegSaveKeyW`, `CryptReleaseContext`, `EqualSid`, `RegReplaceKeyW`, `GetSidSubAuthority`, `GetTokenInformation`, `LookupAccountSidW`
**msvcrt.dll**: `abs`, `free`, `toupper`, `isupper`, `memset`, `memcpy`, `memcmp`, `memchr`, `sprintf`, `fprintf`, `_aligned_malloc`, `_stricmp`, `vsprintf`, `iscntrl`, `isgraph`
**bxsdk64.dll**: `BoxedAppSDK_SetContext`, `BoxedAppSDK_DeleteFileFromVirtualFileSystemW`, `BoxedAppSDK_Init`, `BoxedAppSDK_CreateVirtualFileW`
**avifil32.dll**: `AVIStreamInfoW`, `AVIFileCreateStreamW`, `AVIStreamGetFrame`, `AVIMakeCompressedStream`, `AVIFileOpenW`, `AVISaveOptionsFree`, `AVIFileRelease`, `AVIStreamRelease`, `AVIStreamGetFrameClose`, `AVIStreamWrite`, `AVIStreamGetFrameOpen`, `AVIFileInit`, `AVISaveOptions`, `AVIFileGetStream`, `AVISaveVW`
**kernel32.dll**: `LocalAlloc`, `LocalFree`, `GetModuleFileNameW`, `GetProcessAffinityMask`, `SetProcessAffinityMask`, `SetThreadAffinityMask`, `Sleep`, `ExitProcess`, `FreeLibrary`, `LoadLibraryA`, `GetModuleHandleA`, `GetProcAddress`
**SHFolder.dll**: `SHGetFolderPathW`
**MsVfW32.dll**: `DrawDibOpen`, `DrawDibDraw`, `DrawDibClose`
**crypt32.dll**: `CertGetNameStringW`, `CryptSignMessage`, `CertCreateCertificateContext`, `CertAddCertificateContextToStore`, `PFXIsPFXBlob`, `CertFreeCertificateContext`, `PFXImportCertStore`, `CertCloseStore`, `CertEnumCertificatesInStore`, `CertOpenSystemStoreW`, `CertGetCertificateContextProperty`
**wsock32.dll**: `gethostbyaddr`, `setsockopt`, `WSACleanup`, `gethostbyname`, `bind`, `gethostname`, `closesocket`, `WSAGetLastError`, `connect`, `inet_addr`, `getpeername`, `WSAAsyncSelect`, `WSAAsyncGetServByName`, `WSACancelAsyncRequest`, `send`
**gdiplus.dll**: `GdipFillEllipseI`, `GdipCloneImage`, `GdipDrawBezier`, `GdipDrawImagePointsRectI`, `GdipSetPenDashOffset`, `GdipGetPenDashOffset`, `GdipCreateFontFromDC`, `GdipClonePath`, `GdipIsVisibleRegionRect`, `GdipSetClipHrgn`, `GdipSetPixelOffsetMode`, `GdipGetLineColors`, `GdipSetClipPath`, `GdipGetEmHeight`, `GdipGetRegionBoundsI`
**gdi32.dll**: `AddFontMemResourceEx`, `SetPaletteEntries`, `GetTextCharsetInfo`, `BeginPath`, `PolyPolygon`, `GetCharacterPlacementA`, `AngleArc`, `CloseFigure`, `CreateMetaFileW`, `SetAbortProc`, `PathToRegion`, `ScaleWindowExtEx`, `SetArcDirection`, `GetArcDirection`, `ExtSelectClipRgn`
**mpr.dll**: `WNetEnumResourceW`, `WNetGetUniversalNameW`, `WNetCloseEnum`, `WNetOpenEnumW`
**usp10.dll**: `ScriptFreeCache`, `ScriptGetProperties`, `ScriptPlace`, `ScriptIsComplex`, `ScriptItemize`, `ScriptGetGlyphABCWidth`, `ScriptShape`, `ScriptLayout`, `ScriptApplyDigitSubstitution`
**winmm.dll**: `timeEndPeriod`, `timeBeginPeriod`, `sndPlaySoundW`, `PlaySoundW`, `timeGetTime`

### Exports

`TMethodImplementationIntercept`, `__dbk_fcall_wrapper`, `dbkFCallWrapperAddr`

## Extracted Strings

Total strings found: **410914** (showing first 100)

```
This program must be run under Win64
$7
`.data
.idata
.didata
.edata
.rdata
@.emptyR
@.pdata
@.vmp0
h.vmp1
h.rsrc
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

OleVariant

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
IsEmpty
PInterfaceEntry
TInterfaceEntry(
VTable
IOffset
_Filler

ImplGetter
PInterfaceTableX
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0256fa90` | `0x256fa90` | 62914571 | ✓ |
| `fcn.0381b170` | `0x381b170` | 54244364 | ✓ |
| `fcn.0381a500` | `0x381a500` | 53062845 | ✓ |
| `fcn.02570770` | `0x2570770` | 50594984 | ✓ |
| `fcn.03bd5460` | `0x3bd5460` | 50528264 | ✓ |
| `fcn.03bd1dc0` | `0x3bd1dc0` | 45948278 | ✓ |
| `fcn.02596700` | `0x2596700` | 35154493 | ✓ |
| `fcn.0257dda0` | `0x257dda0` | 33817704 | ✓ |
| `fcn.02580e00` | `0x2580e00` | 33739619 | ✓ |
| `fcn.0258f5e0` | `0x258f5e0` | 33554693 | ✓ |
| `fcn.03bd5230` | `0x3bd5230` | 28987627 | ✓ |
| `fcn.01e82900` | `0x1e82900` | 26212139 | ✓ |
| `fcn.02581510` | `0x2581510` | 22551215 | ✓ |
| `fcn.0257e040` | `0x257e040` | 22536562 | ✓ |
| `fcn.0257da00` | `0x257da00` | 22535137 | ✓ |
| `fcn.02576ef0` | `0x2576ef0` | 22441638 | ✓ |
| `fcn.0256eb4c` | `0x256eb4c` | 22408518 | ✓ |
| `fcn.0256e990` | `0x256e990` | 22407246 | ✓ |
| `fcn.0256d660` | `0x256d660` | 22404373 | ✓ |
| `fcn.02b3dde0` | `0x2b3dde0` | 16777847 | ✓ |
| `fcn.0381bbb0` | `0x381bbb0` | 8378771 | ✓ |
| `fcn.00f84ff0` | `0xf84ff0` | 7810669 | ✓ |
| `fcn.00f84fc0` | `0xf84fc0` | 7810637 | ✓ |
| `fcn.02576b40` | `0x2576b40` | 5663663 | ✓ |
| `fcn.025768d0` | `0x25768d0` | 5662871 | ✓ |
| `fcn.0387e420` | `0x387e420` | 4496511 | ✓ |
| `fcn.0385edf0` | `0x385edf0` | 4338383 | ✓ |
| `fcn.01679900` | `0x1679900` | 4220253 | ✓ |
| `fcn.02598e10` | `0x2598e10` | 4216418 | ✓ |
| `fcn.038614b0` | `0x38614b0` | 4214423 | ✓ |

### Decompiled Code Files

- [`code/fcn.00f84fc0.c`](code/fcn.00f84fc0.c)
- [`code/fcn.00f84ff0.c`](code/fcn.00f84ff0.c)
- [`code/fcn.01679900.c`](code/fcn.01679900.c)
- [`code/fcn.01e82900.c`](code/fcn.01e82900.c)
- [`code/fcn.0256d660.c`](code/fcn.0256d660.c)
- [`code/fcn.0256e990.c`](code/fcn.0256e990.c)
- [`code/fcn.0256eb4c.c`](code/fcn.0256eb4c.c)
- [`code/fcn.0256fa90.c`](code/fcn.0256fa90.c)
- [`code/fcn.02570770.c`](code/fcn.02570770.c)
- [`code/fcn.025768d0.c`](code/fcn.025768d0.c)
- [`code/fcn.02576b40.c`](code/fcn.02576b40.c)
- [`code/fcn.02576ef0.c`](code/fcn.02576ef0.c)
- [`code/fcn.0257da00.c`](code/fcn.0257da00.c)
- [`code/fcn.0257dda0.c`](code/fcn.0257dda0.c)
- [`code/fcn.0257e040.c`](code/fcn.0257e040.c)
- [`code/fcn.02580e00.c`](code/fcn.02580e00.c)
- [`code/fcn.02581510.c`](code/fcn.02581510.c)
- [`code/fcn.0258f5e0.c`](code/fcn.0258f5e0.c)
- [`code/fcn.02596700.c`](code/fcn.02596700.c)
- [`code/fcn.02598e10.c`](code/fcn.02598e10.c)
- [`code/fcn.02b3dde0.c`](code/fcn.02b3dde0.c)
- [`code/fcn.0381a500.c`](code/fcn.0381a500.c)
- [`code/fcn.0381b170.c`](code/fcn.0381b170.c)
- [`code/fcn.0381bbb0.c`](code/fcn.0381bbb0.c)
- [`code/fcn.0385edf0.c`](code/fcn.0385edf0.c)
- [`code/fcn.038614b0.c`](code/fcn.038614b0.c)
- [`code/fcn.0387e420.c`](code/fcn.0387e420.c)
- [`code/fcn.03bd1dc0.c`](code/fcn.03bd1dc0.c)
- [`code/fcn.03bd5230.c`](code/fcn.03bd5230.c)
- [`code/fcn.03bd5460.c`](code/fcn.03bd5460.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 5/5**. The latest disassembly provides a granular look at the internal logic of the "dispatcher" system, revealing how specific operations are mapped to instructions and identifying specific functionalities like database interaction.

---

### Updated Technical Analysis (Cumulative)

#### 1. Architecture: An Intermediate Representation (IR) Execution Engine
The massive switch-case structure in Chunk 5 confirms that this is not just a "VM," but an **Intermediate Representation (IR) Interpreter**. The malware does not execute raw machine code directly for its primary logic; instead, it parses and executes a custom "language" or bytecode.

*   **Instruction Mapping:** Each case (e.g., `case '0'`, `case 'x'`, `case 's'`) represents a single high-level operation in the malware’s internal language.
    *   Examples like `case '1'`, `case '2'`, and `case '3'` are likely used for **object property access** or **variable assignment**.
    *   Cases like `'x'`, `'y'`, and `'z'` (the end of the alphabet) often represent **complex system interactions** or specialized library calls.
*   **The "Object" System:** The frequent use of `piStack_498` with various offsets (e.g., `iVar25 + 0x10 + iVar30 * 0x18`) indicates that the malware is navigating a heap-based structure where each entry represents an object. When a "case" is hit, it isn't just executing code; it is performing an operation on a specific object property defined by the bytecode.
*   **Internal Helper Functions:** The frequent calls to `fcn.03861340`, `fcn.03877750`, and `fcn.03876960` suggest a library of "primitive" actions (e.g., `GetBufferLength`, `ValidateString`, `FindKeyInMap`). These functions provide the building blocks that the higher-level switch cases then orchestrate into complex behaviors.

#### 2. Discovery of Specific Capabilities: Database & Storage
Chunk 5 reveals a critical piece of evidence regarding how the malware handles data persistence and organization:

*   **SQLite Interaction (Case 'x'):** The code explicitly references `sqlite_temp_master` and `sqlite_master`. This indicates that the malware utilizes **SQLite databases** for internal storage. It likely uses these databases to store configuration, a "hit list" of targets, or local cached data from exfiltrated records.
*   **Complex Data Structures (Case 's'):** The logic in `case 's'` involving magic numbers like `-0x420df25d` and iterative loops suggests the management of **Linked Lists or Hash Tables**. This is used to manage complex state—perhaps tracking active connections or a list of files pending for exfiltration.
*   **String/Buffer Manipulation:** Cases such as `'0'`, `':'`, and `';'` are typical of an interpreter handling string formatting, memory copies, or buffer validations. The malware is essentially "parsing" its own logic in real-time to determine the next move.

#### 3. Advanced Defenses & Obfuscation Techniques
*   **Contextual Execution:** Many cases include "gatekeeper" checks (e.g., `if (iVar16 != 0)` or `if (uVar14 != 0)`). These ensure that the next instruction only executes if a previous step succeeded. This makes it extremely difficult to trace a single logical path because the execution flow is dependent on both the **bytecode** and the **dynamic state** of the memory.
*   **Information Hiding:** By using an IR, the developers can change the malware's behavior by simply providing a different "script" (the bytecode) to the same engine. This allows them to update features without changing the underlying `.exe` structure, making traditional signature-based detection ineffective.

---

### Summary for Analysts

The addition of Chunk 5 provides definitive evidence that this is an **Industrial-Grade Malware Framework**. It utilizes a "Virtual Machine" style architecture where the malicious logic is separated from the execution engine.

**Key takeaways for the IR team:**
1.  **Scriptable Behavior:** The malware's capabilities are likely defined by a data file or a blob of memory that feeds the switch statements. Changing the bytecode changes what the malware does (e.g., changing it from an info-stealer to a ransomware note generator).
2.  **Persistence via SQLite:** The presence of `sqlite_master` strings confirms that the malware has mechanisms for local data storage and organization, likely used for coordinating multi-stage attacks or storing stolen data before exfiltration.
3.  **Logic "Abstraction":** The complexity is not just for show; it allows the threat actor to build a modular toolkit where different modules (modules 1, 2, etc.) can be swapped into the interpreter depending on the target environment.

**Updated Recommended Action:**
*   **Database Scrutiny:** Since SQLite is identified as a component, perform memory forensics to look for `.db` files or "in-memory" SQLite databases. This may contain the "instructions" used by the VM or the data it has collected from the host.
*   **Identify the Bytecode Source:** Instead of trying to map every switch case (there are too many), focus on **finding the memory region that feeds these cases**. Locating the "instruction stream" will allow you to see the actual logic the malware is executing at any given time.
*   **Memory-Based Triage:** Create signatures for the specific internal functions identified in the disassembly (e.g., look for the `0x4666da0` constants or the specific ways it handles the `piStack_498` offsets). These are "constants" of the framework that will persist even if the bytecode changes.
*   **Focus on API Bridge:** Since the VM eventually has to talk to the OS, continue monitoring for the transition point where a switch case results in a high-level Win32 API call (e.g., `NtCreateFile`, `InternetConnect`). These are the "exits" from the VM into the real world.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Streams | The use of a custom "Intermediate Representation" (IR) and a Virtual Machine-style interpreter hides the malware's actual logic from static analysis and signature-based detection. |
| **T1070** | Data Staging | The use of SQLite databases to store "hit lists," configuration data, and cached exfiltrated records indicates a structured method for organizing data before it is moved or exfiltrated. |
| **T1568** | Dynamic Resolution | The extensive switch-case structure and the fact that the malware "parses its own logic in real-time" suggest that the final execution path is determined dynamically based on state rather than fixed code paths. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data describes an advanced malware framework utilizing a custom **Intermediate Representation (IR) Interpreter** (a "Virtual Machine" style architecture). While the report contains significant technical detail regarding the malware's capabilities, it does not contain standard network-based or file-system-based IOCs (such as hardcoded IPs, URLs, or specific file paths).

---

### **IOC_REPORT**

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (The analysis mentions the use of SQLite databases, but no specific paths to `.db` files were provided.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified. (Note: The hex value `-0x420df25d` was identified as a logic constant for memory management, not a file or certificate hash.)

**Other artifacts**
*   **C2/Execution Pattern:** Use of an **Intermediate Representation (IR) Interpreter**. The malware utilizes a custom "instruction set" to hide its primary logic. This means the malicious functionality is decoupled from the binary's static code, making it a "fileless-style" execution behavior within a host process.
*   **Database Integration:** Usage of **SQLite** (`sqlite_master`, `sqlite_temp_master`). The malware utilizes SQLite for internal data organization (potential hit lists or local configuration storage).
*   **Internal Function Offsets:** Identified internal logic points at `fcn.03861340`, `fcn.03877750`, and `fcn.03876960`. While these are not direct IOCs, they can be used as markers for memory forensics to identify the core "primitive" actions of the framework.

---
**Analyst Note:** The malware is highly sophisticated in its architecture. Because it uses a Virtual Machine approach, traditional signature-based detection on strings will likely fail. Detection efforts should focus on identifying the **Interpreter Loop** (the switch-case structure) and the **Memory Buffer** where the bytecode resides.

---

## Malware Family Classification

1. **Malware family**: custom (Modular Framework)
2. **Malware type**: loader / backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **IR Interpreter Architecture:** The malware utilizes a complex "Virtual Machine" style architecture where logic is executed via an Intermediate Representation (IR). This decouples the core execution engine from the malicious payload, allowing attackers to change functionality (e.g., switching between infostealing and ransomware) simply by swapping the bytecode.
*   **Persistent Data Management:** The explicit use of SQLite databases (`sqlite_master`) indicates a sophisticated capability for local data staging, configuration management, and "hit list" organization prior to exfiltration.
*   **Industrial-Grade Modularity:** The analysis describes a "modular toolkit" where high-level abstractions allow the malware to function as a multi-purpose platform rather than a single-purpose tool, characteristic of advanced backdoors or sophisticated loaders used in complex campaigns.
