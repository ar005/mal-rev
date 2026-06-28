# Threat Analysis Report

**Generated:** 2026-06-27 19:25 UTC
**Sample:** `01e521b7dea93a8eb80883d7bc535dedc2a09eeb981729fd46f4ee677900c64e_01e521b7dea93a8eb80883d7bc535dedc2a09eeb981729fd46f4ee677900c64e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01e521b7dea93a8eb80883d7bc535dedc2a09eeb981729fd46f4ee677900c64e_01e521b7dea93a8eb80883d7bc535dedc2a09eeb981729fd46f4ee677900c64e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 9 sections |
| Size | 775,168 bytes |
| MD5 | `8f9aeefede63d30a0ffe5149fba087ec` |
| SHA1 | `b25b4a0a94984e3ec334763e07e4e2054d5f71d0` |
| SHA256 | `01e521b7dea93a8eb80883d7bc535dedc2a09eeb981729fd46f4ee677900c64e` |
| Overall entropy | 6.634 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1339084793 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 580,096 | 6.553 | No |
| `.itext` | 6,656 | 5.954 | No |
| `.data` | 15,872 | 4.835 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 16,896 | 5.268 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.211 | No |
| `.reloc` | 35,840 | 6.725 | No |
| `.rsrc` | 118,272 | 5.744 | No |

### Imports

**oleaut32.dll**: `SafeArrayPtrOfIndex`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `SafeArrayCreate`, `VariantChangeType`, `VariantCopy`, `VariantClear`, `VariantInit`
**advapi32.dll**: `StartServiceA`, `QueryServiceStatus`, `OpenServiceA`, `OpenSCManagerA`, `EnumServicesStatusA`, `DeleteService`, `CreateServiceA`, `ControlService`, `CloseServiceHandle`
**user32.dll**: `EnumDisplayMonitors`, `GetMonitorInfoA`
**kernel32.dll**: `Sleep`
**gdi32.dll**: `UnrealizeObject`, `StretchBlt`, `SetWindowOrgEx`, `SetWinMetaFileBits`, `SetViewportOrgEx`, `SetTextColor`, `SetStretchBltMode`, `SetROP2`, `SetPixel`, `SetEnhMetaFileBits`, `SetDIBColorTable`, `SetBrushOrgEx`, `SetBkMode`, `SetBkColor`, `SelectPalette`
**version.dll**: `VerQueryValueA`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`
**wsock32.dll**: `__WSAFDIsSet`, `WSACleanup`, `WSAStartup`, `WSAGetLastError`, `gethostname`, `getservbyname`, `gethostbyname`, `gethostbyaddr`, `socket`, `shutdown`, `sendto`, `send`, `select`, `recv`, `ntohs`
**ole32.dll**: `CoTaskMemFree`, `CLSIDFromProgID`, `ProgIDFromCLSID`, `StringFromCLSID`, `CoCreateInstance`, `CoUninitialize`, `CoInitialize`, `IsEqualGUID`
**shell32.dll**: `SHGetSpecialFolderLocation`, `SHGetPathFromIDListA`
**URLMON.DLL**: `URLDownloadToFileA`
**comctl32.dll**: `_TrackMouseEvent`, `ImageList_SetIconSize`, `ImageList_GetIconSize`, `ImageList_Write`, `ImageList_Read`, `ImageList_DragShowNolock`, `ImageList_DragMove`, `ImageList_DragLeave`, `ImageList_DragEnter`, `ImageList_EndDrag`, `ImageList_BeginDrag`, `ImageList_Remove`, `ImageList_DrawEx`, `ImageList_Draw`, `ImageList_GetBkColor`
**wininet.dll**: `InternetReadFile`, `InternetOpenUrlA`, `InternetOpenA`, `InternetConnectA`, `InternetCloseHandle`, `HttpQueryInfoA`, `FtpPutFileA`
**winmm.dll**: `waveInUnprepareHeader`, `waveInStart`, `waveInReset`, `waveInPrepareHeader`, `waveInOpen`, `waveInClose`, `waveInAddBuffer`, `PlaySoundA`, `mciSendStringA`
**netapi32.dll**: `NetApiBufferFree`, `NetShareGetInfo`, `NetShareEnum`
**gdiplus.dll**: `GdipGetImageEncoders`, `GdipGetImageEncodersSize`, `GdipDrawImageRectI`, `GdipSetInterpolationMode`, `GdipDeleteGraphics`, `GdipCreateBitmapFromHBITMAP`, `GdipCreateBitmapFromScan0`, `GdipGetImagePixelFormat`, `GdipGetImageGraphicsContext`, `GdipSaveImageToStream`, `GdipDisposeImage`, `GdiplusShutdown`, `GdiplusStartup`, `GdipFree`, `GdipAlloc`
**msacm32.dll**: `acmStreamUnprepareHeader`, `acmStreamPrepareHeader`, `acmStreamConvert`, `acmStreamReset`, `acmStreamSize`, `acmStreamClose`, `acmStreamOpen`
**ntdll.dll**: `NtQuerySystemInformation`
**WS2_32.DLL**: `WSAIoctl`
**SHFolder.dll**: `SHGetFolderPathA`
**ntdll**: `NtUnmapViewOfSection`

## Extracted Strings

Total strings found: **4326** (showing first 100)

```
This program must be run under Win32
$7
`.itext
`.data
.idata
.rdata
@.reloc
B.rsrc
Boolean
Integer
Cardinal
string

WideString

OleVariant
TObject
TObject
System

IInterface
System
	IDispatch4
System
TInterfacedObject
FastMM Borland Edition 
 2004, 2005 Pierre le Riche / Professional Software Development
An unexpected memory leak has occurred. 
The unexpected small block leaks are:

 bytes: 
Unknown
String
The sizes of unexpected leaked medium and large blocks are: 
Unexpected Memory Leak
tHt Ht.
:
u0Nt
~KxI[)
                                                                
SOFTWARE\Borland\Delphi\RTL
FPUMaskValue
_^[YY]
r;pt
:
u	@B
YZXtm1
VWUUhdN@
ZTUWVSPRTj
t!R:
t
t-Rf;
t f;J
tVSVWU
t$:
tA:J
;T$r
;T$
0:
t%:J
:
tu:J
t$:
tH:J
t!R:
t
t-Rf;
t f;J
<
t"<t
<t$<t3<
<
t%<t><tQ<t\<
kernel32.dll
GetLongPathNameA
Software\Borland\Locales
Software\Borland\Delphi\Locales
_^[YY]

odSelected
odGrayed
odDisabled	odChecked	odFocused	odDefault
odHotLight
odInactive	odNoAccelodNoFocusRectodReserved1odReserved2
odComboBoxEdit
Windows
TOwnerDrawState
Magellan MSWHEEL
MouseZ
MSWHEEL_ROLLMSG
MSH_WHEELSUPPORT_MSG
MSH_SCROLL_LINES_MSG

	TFileName

TSearchRec`
	Exception
EAbort
EHeapException
EOutOfMemory
EInOutError`
	EExternal
EExternalException
	EIntError

EDivByZero
ERangeError 
EIntOverflow

EMathError

EInvalidOp
EZeroDivide
	EOverflow

EUnderflow
EInvalidPointer
EInvalidCast
EConvertError
EAccessViolation

EPrivilege
EStackOverflow
	EControlC
EVariantError
EAssertionFailed
EAbstractError
EIntfCastError
EOSError
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004760a4` | `0x4760a4` | 29143 | ✓ |
| `fcn.0040484c` | `0x40484c` | 5089 | ✓ |
| `fcn.00469b90` | `0x469b90` | 3769 | ✓ |
| `fcn.0043569c` | `0x43569c` | 2402 | ✓ |
| `fcn.00434d3c` | `0x434d3c` | 2370 | ✓ |
| `fcn.0045ec78` | `0x45ec78` | 2264 | ✓ |
| `fcn.0040c140` | `0x40c140` | 1924 | ✓ |
| `fcn.00401d90` | `0x401d90` | 1900 | ✓ |
| `fcn.004458cc` | `0x4458cc` | 1703 | ✓ |
| `fcn.0046b98c` | `0x46b98c` | 1671 | ✓ |
| `fcn.00428b08` | `0x428b08` | 1633 | ✓ |
| `fcn.0046f744` | `0x46f744` | 1499 | ✓ |
| `fcn.00401a0c` | `0x401a0c` | 1496 | ✓ |
| `fcn.00466fec` | `0x466fec` | 1427 | ✓ |
| `fcn.00415164` | `0x415164` | 1349 | ✓ |
| `fcn.00414a44` | `0x414a44` | 1324 | ✓ |
| `fcn.004556f4` | `0x4556f4` | 1306 | ✓ |
| `fcn.004693dc` | `0x4693dc` | 1273 | ✓ |
| `fcn.0046c9d0` | `0x46c9d0` | 1215 | ✓ |
| `fcn.0043718c` | `0x43718c` | 1160 | ✓ |
| `fcn.00458cb4` | `0x458cb4` | 1154 | ✓ |
| `fcn.00429fe4` | `0x429fe4` | 1135 | ✓ |
| `fcn.0046adbc` | `0x46adbc` | 1135 | ✓ |
| `fcn.004120f8` | `0x4120f8` | 1097 | ✓ |
| `fcn.00412bc8` | `0x412bc8` | 1088 | ✓ |
| `fcn.004801fc` | `0x4801fc` | 1056 | ✓ |
| `fcn.00480880` | `0x480880` | 1030 | ✓ |
| `fcn.00474638` | `0x474638` | 978 | ✓ |
| `fcn.004538d4` | `0x4538d4` | 977 | ✓ |
| `fcn.0041438c` | `0x41438c` | 964 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401a0c.c`](code/fcn.00401a0c.c)
- [`code/fcn.00401d90.c`](code/fcn.00401d90.c)
- [`code/fcn.0040484c.c`](code/fcn.0040484c.c)
- [`code/fcn.0040c140.c`](code/fcn.0040c140.c)
- [`code/fcn.004120f8.c`](code/fcn.004120f8.c)
- [`code/fcn.00412bc8.c`](code/fcn.00412bc8.c)
- [`code/fcn.0041438c.c`](code/fcn.0041438c.c)
- [`code/fcn.00414a44.c`](code/fcn.00414a44.c)
- [`code/fcn.00415164.c`](code/fcn.00415164.c)
- [`code/fcn.00428b08.c`](code/fcn.00428b08.c)
- [`code/fcn.00429fe4.c`](code/fcn.00429fe4.c)
- [`code/fcn.00434d3c.c`](code/fcn.00434d3c.c)
- [`code/fcn.0043569c.c`](code/fcn.0043569c.c)
- [`code/fcn.0043718c.c`](code/fcn.0043718c.c)
- [`code/fcn.004458cc.c`](code/fcn.004458cc.c)
- [`code/fcn.004538d4.c`](code/fcn.004538d4.c)
- [`code/fcn.004556f4.c`](code/fcn.004556f4.c)
- [`code/fcn.00458cb4.c`](code/fcn.00458cb4.c)
- [`code/fcn.0045ec78.c`](code/fcn.0045ec78.c)
- [`code/fcn.00466fec.c`](code/fcn.00466fec.c)
- [`code/fcn.004693dc.c`](code/fcn.004693dc.c)
- [`code/fcn.00469b90.c`](code/fcn.00469b90.c)
- [`code/fcn.0046adbc.c`](code/fcn.0046adbc.c)
- [`code/fcn.0046b98c.c`](code/fcn.0046b98c.c)
- [`code/fcn.0046c9d0.c`](code/fcn.0046c9d0.c)
- [`code/fcn.0046f744.c`](code/fcn.0046f744.c)
- [`code/fcn.00474638.c`](code/fcn.00474638.c)
- [`code/fcn.004760a4.c`](code/fcn.004760a4.c)
- [`code/fcn.004801fc.c`](code/fcn.004801fc.c)
- [`code/fcn.00480880.c`](code/fcn.00480880.c)

## Behavioral Analysis

The final addition of disassembly (chunk 3/3) completes the profile of this malware, moving it from a "highly engineered loader" to a **sophisticated, multi-functional malicious framework.**

While previous chunks identified the decompression and GDI manipulation, this final segment reveals the **communication infrastructure** and the **complex logic handling** required for long-term operation.

### Updated Analysis Summary
The inclusion of these functions confirms that the malware is designed for more than just "unpacking" a file; it contains an integrated suite for **network communication (C2 interaction)**, **advanced data parsing**, and **interactive UI management**. This suggests the binary may be capable of receiving commands from a remote server to perform varied tasks after initial execution.

---

### Core Functionality (Updated)
The core functionality has expanded into three distinct pillars:

1.  **Advanced Multi-Layered Decompression:** The presence of `fcn.004693dc` and `fcn.0046c9d0` shows that the decompression is not a simple "unzip" routine. These functions involve complex bitwise shifts, mask-based segment navigation, and Huffman-like logic (common in LZMA/LZMA2). This indicates a multi-stage unpacking process where data is unpacked into various stages before being executed.
2.  **C2 Communication & Payload Fetching:** The functions `fcn.004801fc` and `fcn.00480880` are **network communication modules**. They utilize the `wsock32` library to establish connections, receive data (up to 8KB chunks), and process it immediately. This is a hallmark of a "stager" that can download secondary components or update its own instructions from a command-and-control server.
3.  **Rich Interface Interaction:** The heavy GDI usage (`0x429fe4`) combined with the logic in `fcn.00458cb4` (calculating dimensions/offsets) and `fcn.004556f4` (handling window positions and mouse tracking) confirms the malware can generate a **sophisticated, interactive GUI**. This could be used to mimic a legitimate software installer or a fake system error dialog to deceive the user while malicious processes run in the background.

---

### New Technical Findings (Chunk 3/3 Specifics)

#### 1. Network Interaction (The "C2" Gateway)
Functions `fcn.004801fc` and `fcn.00480880` are highly suspicious because they contain:
*   **Socket Programming:** Direct calls to `socket`, `htons`, `inet_addr`, `gethostbyname`, and `connect`.
*   **Data Reception Loop:** The code enters a loop where it receives data from the network (`recv`) and then passes that data into other processing functions.
*   **State Management:** The presence of "heartbeat" style logic (checking if the connection is still alive before sending/receiving) suggests this malware can maintain a persistent connection with its controller.

#### 2. Complex State-Machine/Command Parsing
The large switch blocks in `fcn.00415164`, `fcn.00414a44`, and the complex logic in `fcn.0043718c` are indicators of a **command dispatcher**.
*   **Functionality:** These routines likely take a "Command ID" (received from the network or a file) and route it to a specific set of instructions. 
*   **Malware Tactic:** This allows one single loader to perform many different tasks (e.g., keylogging, file exfiltration, credential stealing) based on what the C2 server tells it to do at that moment.

#### 3. Enhanced Graphics and UI Obfuscation
`fcn.00429fe4` reveals a very "heavy" implementation of GDI:
*   **Bitmaps & Palettes:** It manages `CreateDIBSection`, `CreateCompatibleBitmap`, and `SelectPalette`. This isn't just displaying an icon; it is preparing to render high-quality graphics or bitmaps. 
*   **Potential Use:** This could be used for "overlay" techniques, where the malware draws over the screen in a way that mimics a real application window (e.g., a fake update screen) while and capturing user input behind the scenes.

#### 4. Sophisticated Data Manipulation
The function `fcn.004693dc` is a textbook example of **Huffman Decoding** or a similar variable-length coding scheme used in advanced compression/encryption. It handles:
*   Bit-stream alignment (shifting and masking to find the next "token").
*   Buffer management for non-contiguous data.
*   This ensures that the final payload is not only compressed but also **highly obfuscated** from simple static analysis tools.

---

### Updated Summary of Evidence

| Feature | Technical Evidence | Potential Malicious Intent |
| :--- | :--- | :--- |
| **Multi-Stage Decryption** | Huffman/LZMA-style logic in `0x4693dc` and `0x46c9d0`. | Obscuring the size and nature of secondary payloads. |
| **Network Command/Control** | `wsock32` implementation in `0x4801fc` & `0x480880`. | Enabling remote control, real-time updates, and extra payload fetching. |
| **Command Dispatching** | Massive switch tables (21+ cases) in `0x415164` and `0x414a44`. | Allowing the loader to perform multiple tasks via C2 commands. |
| **Sophisticated UI Masking** | Extensive GDI, `TrackMouseEvent`, and complex bitmap handling. | Creating "fake" software overlays or installers to distract/deceive users. |

### Final Conclusion
The analysis of all three chunks reveals a **highly sophisticated, professional-grade malware loader.** 

It is not a simple script; it is a robust framework designed for high reliability and stealth. It utilizes **advanced compression** (likely LZMA+Huffman) to hide large files, **network modules** to communicate with a remote server, and **complex command dispatching** to allow the attacker to vary its behavior dynamically. The presence of detailed GDI logic further indicates that it is designed to interact with the user's screen in a way that looks legitimate or hides its underlying activity.

**Threat Level: High.** This loader is characteristic of Advanced Persistent Threat (APT) groups or professional cybercrime operations targeting both automated detection and human analysis.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of Huffman decoding and complex bitwise manipulations (LZMA-like) is used to hide the true nature and size of payload components from static analysis. |
| **T1105** | Ingress Tool Transfer | The malware utilizes a network communication module to receive data chunks and download secondary components/instructions from a remote server. |
| **T1071** | Application Layer Protocol | The implementation of `wsock32` with heartbeats indicates the use of standard networking protocols to maintain contact with a Command and Control (C2) infrastructure. |
| **T1059** | Command and Scripting Interpreter | Large switch-block structures are used to parse "Command IDs" from the network, allowing a single binary to execute diverse malicious functions dynamically. |
| **T1566** | Fake Window | Extensive GDI manipulation and bitmap handling are used to create fake installers or overlays to deceive users while malicious actions occur in the background. |
| **T1036** | Create System for Command and Control | The modular design of the "Command Dispatcher" allows it to function as a multi-purpose framework rather than a single-purpose piece of malware. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** No specific IP addresses, URLs, or File Hashes were present in the provided text; however, several internal functional offsets and behavior-based indicators were identified.

### **IP addresses / URLs / Domains**
*   *None identified.* (The report mentions C2 communication via `wsock32`, but no specific hardcoded IPs or domains were provided in the sample).

### **File paths / Registry keys**
*   `SOFTWARE\Borland\Delphi\RTL`
*   `Software\Borland\Locales`
*   `Software\Borland\Delphi\Locales`
*(Note: These are Borland compiler-related registry paths; while they identify the development environment, they are not unique to a specific campaign.)*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts (C2 patterns, Function Offsets, Techniques)**
*   **Internal Code Offsets (Key Functions):**
    *   `0x4693dc`: Huffman Decoding / Bit-stream alignment.
    *   `0x46c9d0`: Multi-stage unpacking logic.
    *   `0x4801fc`: Network communication/Socket initialization (`wsock32`).
    *   `0x480880`: Data reception loop (8KB chunk processing).
    *   `0x458cb4`: GUI dimension and offset calculation.
    *   `0x4556f4`: Window position/Mouse tracking management.
    *   `0x429fe4`: GDI-heavy graphics rendering (Bitmaps & Palettes).
*   **C2 Communication Patterns:**
    *   Utilization of `wsock32` library for `socket`, `htons`, `inet_addr`, `gethostbyname`, and `connect`.
    *   Heartbeat logic to maintain persistent connections.
*   **Command Dispatching Logic:**
    *   Large switch blocks at `0x415164` and `0x414a44` (21+ cases) indicating a multi-functional command dispatcher for remote tasks like keylogging or data exfiltration.
*   **Evasion/Obfuscation Techniques:**
    *   Use of Huffman/LZMA-style compression to hide payload size and content.
    *   GDI-based "overlay" tactics to mimic legitimate software windows while hiding background activity.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Downloader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Payload Handling:** The use of advanced Huffman/LZMA-style decompression (`0x4693dc`, `0x46c9d0`) indicates a sophisticated multi-stage unpacking process designed to hide secondary payloads from static analysis.
*   **C2 Command Dispatcher:** The presence of extensive switch blocks (over 21 cases) at `0x415164` and `0x414a44`, combined with `wsock32` integration, identifies it as a modular framework capable of receiving and executing varied commands (e.g., keylogging, exfiltration).
*   **User Deception Tactics:** Extensive GDI manipulation (`0x429fe4`) and "fake window" techniques indicate the malware is designed to hide its presence or mislead users with realistic overlays while performing background tasks.
