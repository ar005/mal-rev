# Threat Analysis Report

**Generated:** 2026-08-10 17:45 UTC
**Sample:** `0def8fbbe23b25adbc523fcb7245f7fbbdc7fe570dd4a4ce03b46ce6e07b195b_0def8fbbe23b25adbc523fcb7245f7fbbdc7fe570dd4a4ce03b46ce6e07b195b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0def8fbbe23b25adbc523fcb7245f7fbbdc7fe570dd4a4ce03b46ce6e07b195b_0def8fbbe23b25adbc523fcb7245f7fbbdc7fe570dd4a4ce03b46ce6e07b195b.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 6,495,850 bytes |
| MD5 | `c6b3ee5430bc8e86c8ad38b97e3dcaad` |
| SHA1 | `80122ad801fce61f4f51459bda43fa6768b0d2f2` |
| SHA256 | `0def8fbbe23b25adbc523fcb7245f7fbbdc7fe570dd4a4ce03b46ce6e07b195b` |
| Overall entropy | 5.606 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1732707660 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 58,368 | 6.458 | No |
| `.rdata` | 40,960 | 4.633 | No |
| `.data` | 3,072 | 2.416 | No |
| `.pdata` | 4,096 | 4.81 | No |
| `.rsrc` | 6,326,272 | 5.502 | No |
| `.reloc` | 2,048 | 4.958 | No |
| `.idata` | 4,608 | 4.648 | No |

### Imports

**KERNEL32.dll**: `LockResource`, `SizeofResource`, `LoadLibraryA`, `FindResourceA`, `GlobalMemoryStatusEx`, `GetComputerNameW`, `GetDiskFreeSpaceExW`, `GetSystemDirectoryW`, `GetTempPathW`, `GetLogicalDrives`, `LoadResource`, `CloseHandle`, `CreateFileW`, `SetFilePointerEx`, `GetConsoleMode`
**USER32.dll**: `MonitorFromWindow`, `GetCursorPos`, `SystemParametersInfoW`, `GetSystemMetrics`, `GetWindowTextW`, `GetForegroundWindow`, `GetDesktopWindow`
**SHELL32.dll**: `SHGetFolderPathW`, `ShellExecuteW`
**ADVAPI32.dll**: `GetUserNameW`
**GDI32.dll**: `CreateCompatibleDC`, `GetDeviceCaps`, `DeleteDC`
**ole32.dll**: `CoUninitialize`
**SHLWAPI.dll**: `PathFileExistsW`, `PathCombineW`
**USERENV.dll**: `GetUserProfileDirectoryW`
**VERSION.dll**: `GetFileVersionInfoW`, `GetFileVersionInfoSizeW`
**WS2_32.dll**: `gethostname`, `WSAStartup`
**WTSAPI32.dll**: `WTSEnumerateSessionsW`
**advapi32.dll**: `RegOpenKeyExW`, `LookupAccountSidW`, `GetCurrentHwProfileW`
**winmm.dll**: `timeBeginPeriod`
**user32.dll**: `GetClientRect`, `IsWindow`
**crypt32.dll**: `CertOpenSystemStoreW`, `CertGetNameStringW`
**gdi32.dll**: `GetObjectW`, `GetStockObject`
**comctl32.dll**: `PropertySheetW`, `InitCommonControlsEx`, `CreateStatusWindowW`
**shlwapi.dll**: `PathIsDirectoryW`, `SHGetValueW`
**kernel32.dll**: `GetSystemInfo`, `GetLocalTime`, `GetUserDefaultLCID`
**oleaut32.dll**: `VariantClear`, `SafeArrayDestroy`

## Extracted Strings

Total strings found: **3869** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
B.idata
UVWATAUAVAWH
L+O0tw
 A_A^A]A\_^]
t$ WATAUAVAW
A_A^A]A\_
u0HcH<
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
t$ WATAUAVAWH
~ND;t;
 A_A^A]A\_
WATAUAVAWH
A_A^A]A\_
H;XXs
H;xXu5
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
L$pHcX
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
@SVWATAUAVAWH
D$0HcH
pA_A^A]A\_^[
A9	upA
B(I9A(u
A9	u;A
SVWATAUAVAWH
|$ Hc^
0A_A^A]A\_^[
UVWATAUAVAWH
F0Hcx
|$hHcX
 A_A^A]A\_^]
t98t H
WATAUAVAWH
< t=<	t9
 A_A^A]A\_
UVWAVAWH
H9:tH
0A_A^_^]
	H;:`
p0R^G'
u3HcH<H
WAVAWH
 A_A^_
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
D$0@8{
u$D8r(tH
D81uUL9r
uED8r(tH
vAD8s(tH
u$D8r(tH
fD91uTL9r
uED8r(tH
v@D8s(tH
UVWATAUAVAWH
PA_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
@USVWATAUAVH
,/<-w
H
D8t$ht
H
D8t$ht
H
A^A]A\_^[]
f9)u4H9j
u%@8j(t
v@8k(t
8D$@tH
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
fD9t$b
K H;^
K(H;T
K0H;J
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140005efc` | `0x140005efc` | 16846 | ✓ |
| `fcn.140005ee8` | `0x140005ee8` | 16796 | ✓ |
| `fcn.140007a68` | `0x140007a68` | 1977 | ✓ |
| `fcn.14000e410` | `0x14000e410` | 1661 | ✓ |
| `fcn.140003838` | `0x140003838` | 1263 | ✓ |
| `fcn.14000bc70` | `0x14000bc70` | 1141 | ✓ |
| `fcn.14000abc0` | `0x14000abc0` | 1038 | ✓ |
| `fcn.14000b160` | `0x14000b160` | 937 | ✓ |
| `fcn.14000eab0` | `0x14000eab0` | 920 | ✓ |
| `fcn.140001660` | `0x140001660` | 915 | ✓ |
| `fcn.14000767c` | `0x14000767c` | 845 | ✓ |
| `fcn.14000b5c4` | `0x14000b5c4` | 817 | ✓ |
| `fcn.14000c598` | `0x14000c598` | 774 | ✓ |
| `fcn.140008524` | `0x140008524` | 701 | ✓ |
| `fcn.1400021cc` | `0x1400021cc` | 661 | ✓ |
| `fcn.14000a1e4` | `0x14000a1e4` | 633 | ✓ |
| `fcn.140008180` | `0x140008180` | 623 | ✓ |
| `fcn.14000ddb8` | `0x14000ddb8` | 614 | ✓ |
| `fcn.140003d28` | `0x140003d28` | 609 | ✓ |
| `fcn.140005404` | `0x140005404` | 585 | ✓ |
| `fcn.1400042dc` | `0x1400042dc` | 565 | ✓ |
| `fcn.140009688` | `0x140009688` | 555 | ✓ |
| `fcn.140001134` | `0x140001134` | 545 | ✓ |
| `fcn.140002470` | `0x140002470` | 535 | ✓ |
| `fcn.1400034ac` | `0x1400034ac` | 499 | ✓ |
| `fcn.140007f98` | `0x140007f98` | 487 | ✓ |
| `fcn.14000d478` | `0x14000d478` | 473 | ✓ |
| `fcn.140007cb0` | `0x140007cb0` | 462 | ✓ |
| `fcn.140004e10` | `0x140004e10` | 453 | ✓ |
| `fcn.140009a94` | `0x140009a94` | 444 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001134.c`](code/fcn.140001134.c)
- [`code/fcn.140001660.c`](code/fcn.140001660.c)
- [`code/fcn.1400021cc.c`](code/fcn.1400021cc.c)
- [`code/fcn.140002470.c`](code/fcn.140002470.c)
- [`code/fcn.1400034ac.c`](code/fcn.1400034ac.c)
- [`code/fcn.140003838.c`](code/fcn.140003838.c)
- [`code/fcn.140003d28.c`](code/fcn.140003d28.c)
- [`code/fcn.1400042dc.c`](code/fcn.1400042dc.c)
- [`code/fcn.140004e10.c`](code/fcn.140004e10.c)
- [`code/fcn.140005404.c`](code/fcn.140005404.c)
- [`code/fcn.140005ee8.c`](code/fcn.140005ee8.c)
- [`code/fcn.140005efc.c`](code/fcn.140005efc.c)
- [`code/fcn.14000767c.c`](code/fcn.14000767c.c)
- [`code/fcn.140007a68.c`](code/fcn.140007a68.c)
- [`code/fcn.140007cb0.c`](code/fcn.140007cb0.c)
- [`code/fcn.140007f98.c`](code/fcn.140007f98.c)
- [`code/fcn.140008180.c`](code/fcn.140008180.c)
- [`code/fcn.140008524.c`](code/fcn.140008524.c)
- [`code/fcn.140009688.c`](code/fcn.140009688.c)
- [`code/fcn.140009a94.c`](code/fcn.140009a94.c)
- [`code/fcn.14000a1e4.c`](code/fcn.14000a1e4.c)
- [`code/fcn.14000abc0.c`](code/fcn.14000abc0.c)
- [`code/fcn.14000b160.c`](code/fcn.14000b160.c)
- [`code/fcn.14000b5c4.c`](code/fcn.14000b5c4.c)
- [`code/fcn.14000bc70.c`](code/fcn.14000bc70.c)
- [`code/fcn.14000c598.c`](code/fcn.14000c598.c)
- [`code/fcn.14000d478.c`](code/fcn.14000d478.c)
- [`code/fcn.14000ddb8.c`](code/fcn.14000ddb8.c)
- [`code/fcn.14000e410.c`](code/fcn.14000e410.c)
- [`code/fcn.14000eab0.c`](code/fcn.14000eab0.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and extended the technical analysis. The new code confirms several high-level malicious techniques, specifically regarding **manual PE loading**, **dynamic API resolution**, and **advanced state machine management**.

### Updated Technical Analysis

#### 1. Core Functionality and Purpose: "Manual Loader & Payload Injector"
The addition of `fcn.140001134` provides a "smoking gun" for the binary's primary purpose. This function implements a **manual PE loader**.
*   **Mechanism:** It validates the `MZ` header and `PE` signature, maps memory sections using `VirtualAlloc`, processes the relocation table (relocations), and manually resolves imports via `LoadLibraryA` and `GetProcAddress`.
*   **Significance:** This indicates that the binary is not just an interpreter; it is a **loader designed to inject another executable or DLL into memory**. By mapping the payload manually, it avoids the standard Windows loader (Ldr), making it significantly harder for traditional EDR (Endpoint Detection Response) tools to detect the transition from the loader to the malicious payload.

#### 2. Sophisticated Malicious Behaviors
In addition to the previously identified behaviors, the new code reveals:

*   **Manual PE Mapping & Reflection (`fcn.140001134`):**
    As described above, this is a classic technique for **Reflective DLL Injection**. The binary takes an embedded payload (likely encrypted or compressed) and manually constructs its memory space to make it executable without touching the disk as a separate file.

*   **Dynamic API Resolution & Obfuscation (`fcn.140009a14`):**
    The code includes a sophisticated wrapper for `GetProcAddress`. It doesn't just call the API; it checks if the library is already mapped, handles potential errors, and potentially uses offsets/hashes to find functions. This technique is used to **hide the true capabilities of the malware** from static analysis tools by ensuring that sensitive API names are not stored as plain text in the binary's import table.

*   **Exception Handling Manipulation (`fcn.14000ddb8` & `fcn.140002470`):**
    The code explicitly constructs complex structures for `RaiseException`. The logic involves setting specific flags (like `0x16`, `0x8f`, etc.) and performing bitwise operations on arguments before calling the system's exception handler. This is often used to **detect debuggers or "hook" anti-debugging checks**, where the malware intentionally triggers an exception that it handles internally, but a debugger would intercept.

*   **Resource Tracking & State Management (`fcn.140009688`):**
    The use of `LOCK()` and `UNLOCK()` around memory offsets (e.g., `0x10`, `0xf0`) suggests the binary manages a **thread-safe global state machine**. It tracks how many times specific modules, strings, or internal "handlers" are accessed. This indicates a highly modular design where different components of the malware communicate through a centralized coordinator.

*   **Data Decryption/Normalization (`fcn.140007f98` & `fcn.14000d478`):**
    These functions process large blocks of memory (e.g., 256 bytes or 1024-byte buffers) and perform transformations on them. The presence of a **Unicode/UTF-8 validation loop** in `fcn.14000d478` suggests that after "unpacking" the data, it ensures the resulting strings are properly formatted before they are passed to system APIs.

#### 3. Advanced Technical Patterns
*   **Manual String & Path Parsing (`fcn.140004e10`):** Instead of using standard library functions like `GetCommandLineW` or `PathFindNextPart`, the binary uses a custom, complex loop to handle escape characters (e.g., `\\`), quotes, and tabs. This is a common **anti-analysis technique** used to avoid being "hooked" by security software at the API level.
*   **Multi-Layered Dispatching:** The code frequently uses nested logic to check "Type IDs" (seen in `fcn.1400042dc` and `fcn.1400034ac`) before deciding which internal function to call. This makes it very difficult for a human analyst to follow the linear flow of execution without active debugging.
*   **Trap States via Software Interrupts:** The repeated use of `swi(3)` (as seen in several locations) confirms that the code is designed to "fail-closed." If any internal state check fails—such as an invalid command, a missing resource, or a detected debugger—the program will crash itself instantly to prevent further analysis.

### Updated Summary Table for Threat Intelligence

| Feature | Observation | Potential Impact / Goal |
| :--- | :--- | :--- |
| **In-Memory Loading** | Manual PE Mapping (`fcn.140001134`) | Execute payload without writing to disk (Fileless). |
| **API Obfuscation** | Custom `GetProcAddress` wrapper | Hide imports and evade static analysis. |
| **Anti-Analysis** | Complex `RaiseException` manipulation | Detect/evade debuggers and sandboxes. |
| **State Management** | Thread-safe resource tracking | Support complex, multi-functional C2 capabilities. |
| **Parsing Logic** | Custom String/Path parsing | Bypass hooks on standard Windows APIs. |
| **Data Processing** | Transformation & Unicode validation | Handle "noisy" or packed data from remote servers. |

**Conclusion:** The binary is a highly sophisticated, professional-grade **malware loader**. It is designed to reside in memory, evade detection by avoiding common API patterns, and host a complex payload (likely a modular RAT or backdoor) that it will load dynamically using its internal "Reflective" logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1620** | Reflective Loader | The binary manually maps, processes relocations, and resolves imports to load an executable payload directly into memory without using the standard Windows loader. |
| **T1027** | Obfuscated Files or Information | The use of dynamic API resolution (via custom GetProcAddress wrappers) and manual string/path parsing masks the true capabilities and intended targets from static analysis. |
| **T1497** | Virtualization Detection | The construction of complex structures for `RaiseException` is used to detect, evade, or "trap" debuggers and automated sandbox environments during execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contains a significant amount of obfuscated data and standard compiler artifacts which do not constitute actionable network or host-based IOCs. The most relevant intelligence is found within the behavioral analysis regarding technical maneuvers.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While "Manual String & Path Parsing" was observed as a behavior, no specific malicious paths were listed in the report.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The `fcn.XXXXX` notations are internal memory offsets from a disassembler, not file hashes.)

### **Other artifacts (Behavioral Indicators & Technical Patterns)**
These items represent the "behavioral" IOCs derived from the analysis:

*   **Reflective DLL Injection / Manual PE Mapping:** The sample contains a manual loader (`fcn.140001134`) designed to map MZ/PE headers into memory and resolve imports manually to evade standard Windows loaders.
*   **Dynamic API Resolution (GetProcAddress Wrapper):** Use of `fcn.140009a14` to hide sensitive API calls from static analysis by avoiding plain-text strings in the import table.
*   **Anti-Debugging / Anti-Analysis:** Specific manipulation of `RaiseException` using non-standard flags (e.g., `0x16`, `0x8f`) via `fcn.14000ddb8` and `fcn.140002470`.
*   **Custom Parsing Logic:** Implementation of custom string/path parsing (`fcn.140004e10`) to bypass hooks placed on standard Windows API functions (like `GetCommandLineW`).
*   **State Machine Management:** Use of mutex-like locking logic (`LOCK()` and `UNLOCK()`) at specific memory offsets (e.g., `0x10`, `0xf0`) for internal thread-safe communication.
*   **Software Interrupts:** Repeated use of `swi(3)` to force a "fail-closed" state if a debugger or invalid command is detected.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Reflective Loading Capabilities:** The sample implements manual PE mapping (processing MZ/PE headers, relocation tables, and manual import resolution), which allows it to inject and execute a payload entirely in memory while bypassing standard Windows loading mechanisms.
*   **Advanced Anti-Analysis & Obfuscation:** The binary employs sophisticated evasive maneuvers, including custom `GetProcAddress` wrappers to hide API usage from static analysis and complex `RaiseException` manipulation designed specifically to detect or bypass debuggers and sandboxes.
*   **Stealthy Execution Architecture:** The use of "fail-closed" software interrupts (`swi(3)`), a thread-safe state machine, and custom string/path parsing indicates a professional-grade design intended to evade security hooks and provide a stable environment for a hosted payload (likely a RAT).
