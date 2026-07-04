# Threat Analysis Report

**Generated:** 2026-07-02 20:44 UTC
**Sample:** `03c96da8c86912c31beb2819fec2b6fe11cc844da2089dbf1d17004ee71ae133_03c96da8c86912c31beb2819fec2b6fe11cc844da2089dbf1d17004ee71ae133.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03c96da8c86912c31beb2819fec2b6fe11cc844da2089dbf1d17004ee71ae133_03c96da8c86912c31beb2819fec2b6fe11cc844da2089dbf1d17004ee71ae133.exe` |
| File type | PE32+ executable for MS Windows 10.00 (GUI), x86-64, 7 sections |
| Size | 698,368 bytes |
| MD5 | `c90fa058651c12abb38620be9e96060e` |
| SHA1 | `3a4a826549ac67beda76b4bea24def24192fd933` |
| SHA256 | `03c96da8c86912c31beb2819fec2b6fe11cc844da2089dbf1d17004ee71ae133` |
| Overall entropy | 7.891 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4135487301 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 58,368 | 6.09 | No |
| `.rdata` | 22,528 | 4.457 | No |
| `.data` | 1,024 | 2.966 | No |
| `.pdata` | 3,584 | 4.759 | No |
| `.didat` | 512 | 1.654 | No |
| `.rsrc` | 8,192 | 5.508 | No |
| `.reloc` | 603,136 | 7.983 | ⚠️ Yes |

### Imports

**msvcrt.dll**: `_fmode`, `?terminate@@YAXXZ`, `_wcmdln`, `_initterm`, `??1type_info@@UEAA@XZ`, `_lock`, `__setusermatherr`, `_cexit`, `_exit`, `exit`, `_unlock`, `__dllonexit`, `_onexit`, `memmove`, `_commode`
**api-ms-win-core-synch-l1-1-0.dll**: `SetEvent`, `DeleteCriticalSection`, `InitializeCriticalSection`, `EnterCriticalSection`, `LeaveCriticalSection`, `CreateEventW`, `WaitForSingleObject`
**api-ms-win-core-libraryloader-l1-2-0.dll**: `FindResourceExW`, `SizeofResource`, `GetModuleFileNameW`, `LoadResource`, `GetModuleHandleW`, `LoadLibraryExW`, `GetProcAddress`, `FreeLibrary`
**api-ms-win-core-string-l2-1-0.dll**: `CharPrevW`, `CharNextW`
**api-ms-win-core-errorhandling-l1-1-0.dll**: `SetUnhandledExceptionFilter`, `RaiseException`, `GetLastError`, `UnhandledExceptionFilter`
**api-ms-win-core-registry-l1-1-0.dll**: `RegNotifyChangeKeyValue`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegQueryInfoKeyW`, `RegDeleteValueW`, `RegSetValueExW`, `RegEnumKeyExW`, `RegEnumValueW`, `RegCloseKey`, `RegCreateKeyExW`
**api-ms-win-core-memory-l1-1-0.dll**: `VirtualAlloc`, `VirtualQuery`, `VirtualProtect`
**api-ms-win-core-sysinfo-l1-1-0.dll**: `GetSystemInfo`, `GetTickCount`, `GetSystemTimeAsFileTime`
**api-ms-win-core-string-l1-1-0.dll**: `MultiByteToWideChar`
**api-ms-win-core-handle-l1-1-0.dll**: `DuplicateHandle`, `CloseHandle`
**api-ms-win-core-synch-l1-2-1.dll**: `WaitForMultipleObjects`
**api-ms-win-core-synch-l1-2-0.dll**: `Sleep`
**api-ms-win-core-heap-l1-1-0.dll**: `HeapFree`, `GetProcessHeap`, `HeapSetInformation`, `HeapAlloc`, `HeapDestroy`
**api-ms-win-core-processthreads-l1-1-0.dll**: `GetCurrentThreadId`, `TerminateProcess`, `GetCurrentProcessId`, `CreateThread`, `GetCurrentProcess`, `GetStartupInfoW`
**api-ms-win-core-profile-l1-1-0.dll**: `QueryPerformanceCounter`
**api-ms-win-core-rtlsupport-l1-1-0.dll**: `RtlLookupFunctionEntry`, `RtlCaptureContext`, `RtlVirtualUnwind`
**api-ms-win-core-threadpool-legacy-l1-1-0.dll**: `CreateTimerQueue`, `DeleteTimerQueueTimer`, `CreateTimerQueueTimer`, `DeleteTimerQueueEx`
**api-ms-win-core-string-obsolete-l1-1-0.dll**: `lstrcmpiW`, `lstrcpynW`
**CRYPTBASE.dll**: `SystemFunction036`
**MSWSOCK.dll**: `AcceptEx`, `GetAcceptExSockaddrs`

## Extracted Strings

Total strings found: **1518** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.didat
@.reloc
UAUAWH
VWATAVAWH
 A_A^A\_^
UVWATAUAVAWH
A_A^A]A\_^]
t$ WATAUAVAWH
 A_A^A]A\_
t$ WAVAWH
 A_A^_
t$ WATAUAVAWH
 A_A^A]A\_
t$ WATAUAVAWH
 A_A^A]A\_
VWATAUAVH
C8H!C@L
 A^A]A\_^
VWATAVAWH
 A_A^A\_^
UVWATAUAVAWH
0A_A^A]A\_^]
WAVAWH
9A98u6A9x
C9Eu)H
0A_A^_
WATAUAVAWH
 A_A^A]A\_
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
@UATAUAVAWH
e@A_A^A]A\]
WAVAWH
 A_A^_
@USVWATAUAVAWH
fD94Fu
A_A^A]A\_^[]
WATAUAVAWH
A_A^A]A\_
@UATAUAVAWH
e0A_A^A]A\]
UAVAWH
D9|$8~AI
D;t$8|
D8|$ht
|$ ATAVAWH
C8H!C@L
 A_A^A\
WATAUAVAWH
 A_A^A]A\_
WATAVH
` AUAVAWH
A_A^A]
UVWATAUAVAWH
A_A^A]A\_^]
@VWATAVAWH
0A_A^A\_^
VWATAVAWH
 A_A^A\_^
UVWATAUAVAWH
A_A^A]A\_^]
UVWAVAWH
@A_A^_^]
UVWAVAWH
pA_A^_^]
?H;{0t
VWATAVAWH
?H;{0t2I
A_A^A\_^
u%9D$ t
H;_0t!H
H!\$XH!\$`H!\$HH
H9Q r&H
SVWAVH
hA^_^[
u!f9tC
9w@t
H
D9v@u{H
H;_0t!H
9yDt
H
9y@t
H
D9s@t|H
VWATAVAWH
PA_A^A\_^
VWATAVAWH
 A_A^A\_^
H;_0t!H
?H;{0tTH
H;_0t!H
D9BDtH
fD9rL~
@WATAUAVAWH
D9s@ufD9cDu
9SXt
H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000e13e` | `0x14000e13e` | 53571 | ✓ |
| `method.H_HH.virtual_0` | `0x140003360` | 2982 | ✓ |
| `fcn.140004bc4` | `0x140004bc4` | 2156 | ✓ |
| `method.H_HH.virtual_16` | `0x140003350` | 2073 | ✓ |
| `method.H_HH.virtual_8` | `0x140003370` | 1961 | ✓ |
| `fcn.14000dbb0` | `0x14000dbb0` | 1889 | ✓ |
| `fcn.140003e14` | `0x140003e14` | 1452 | ✓ |
| `fcn.140007f94` | `0x140007f94` | 1011 | ✓ |
| `fcn.1400055dc` | `0x1400055dc` | 722 | ✓ |
| `fcn.14000bb34` | `0x14000bb34` | 711 | ✓ |
| `fcn.14000398c` | `0x14000398c` | 679 | ✓ |
| `entry0` | `0x14000db80` | 642 | ✓ |
| `fcn.14000c7bc` | `0x14000c7bc` | 616 | ✓ |
| `fcn.14000b33c` | `0x14000b33c` | 540 | ✓ |
| `fcn.14000ca2c` | `0x14000ca2c` | 528 | ✓ |
| `fcn.1400049e8` | `0x1400049e8` | 467 | ✓ |
| `fcn.140001424` | `0x140001424` | 462 | ✓ |
| `fcn.14000a6c8` | `0x14000a6c8` | 460 | ✓ |
| `fcn.14000643c` | `0x14000643c` | 444 | ✓ |
| `fcn.14000cde8` | `0x14000cde8` | 438 | ✓ |
| `fcn.14000b908` | `0x14000b908` | 433 | ✓ |
| `fcn.14000c608` | `0x14000c608` | 428 | ✓ |
| `fcn.1400037d8` | `0x1400037d8` | 426 | ✓ |
| `fcn.140007a34` | `0x140007a34` | 415 | ✓ |
| `fcn.140005438` | `0x140005438` | 411 | ✓ |
| `fcn.14000b674` | `0x14000b674` | 400 | ✓ |
| `fcn.14000cfa8` | `0x14000cfa8` | 390 | ✓ |
| `fcn.140009ffc` | `0x140009ffc` | 389 | ✓ |
| `fcn.14000beac` | `0x14000beac` | 386 | ✓ |
| `fcn.14000340c` | `0x14000340c` | 378 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001424.c`](code/fcn.140001424.c)
- [`code/fcn.14000340c.c`](code/fcn.14000340c.c)
- [`code/fcn.1400037d8.c`](code/fcn.1400037d8.c)
- [`code/fcn.14000398c.c`](code/fcn.14000398c.c)
- [`code/fcn.140003e14.c`](code/fcn.140003e14.c)
- [`code/fcn.1400049e8.c`](code/fcn.1400049e8.c)
- [`code/fcn.140004bc4.c`](code/fcn.140004bc4.c)
- [`code/fcn.140005438.c`](code/fcn.140005438.c)
- [`code/fcn.1400055dc.c`](code/fcn.1400055dc.c)
- [`code/fcn.14000643c.c`](code/fcn.14000643c.c)
- [`code/fcn.140007a34.c`](code/fcn.140007a34.c)
- [`code/fcn.140007f94.c`](code/fcn.140007f94.c)
- [`code/fcn.140009ffc.c`](code/fcn.140009ffc.c)
- [`code/fcn.14000a6c8.c`](code/fcn.14000a6c8.c)
- [`code/fcn.14000b33c.c`](code/fcn.14000b33c.c)
- [`code/fcn.14000b674.c`](code/fcn.14000b674.c)
- [`code/fcn.14000b908.c`](code/fcn.14000b908.c)
- [`code/fcn.14000bb34.c`](code/fcn.14000bb34.c)
- [`code/fcn.14000beac.c`](code/fcn.14000beac.c)
- [`code/fcn.14000c608.c`](code/fcn.14000c608.c)
- [`code/fcn.14000c7bc.c`](code/fcn.14000c7bc.c)
- [`code/fcn.14000ca2c.c`](code/fcn.14000ca2c.c)
- [`code/fcn.14000cde8.c`](code/fcn.14000cde8.c)
- [`code/fcn.14000cfa8.c`](code/fcn.14000cfa8.c)
- [`code/fcn.14000dbb0.c`](code/fcn.14000dbb0.c)
- [`code/fcn.14000e13e.c`](code/fcn.14000e13e.c)
- [`code/method.H_HH.virtual_0.c`](code/method.H_HH.virtual_0.c)
- [`code/method.H_HH.virtual_16.c`](code/method.H_HH.virtual_16.c)
- [`code/method.H_HH.virtual_8.c`](code/method.H_HH.virtual_8.c)

## Behavioral Analysis

Based on my analysis of the decompiled code, here is a summary of what the binary does:

### Core Functionality and Purpose
The binary appears to be a **sophisticated backend service** designed for network communication and system integration. It acts as a "listener" or "proxy," likely intended to handle incoming connections (possibly related to FTP/File Transfer protocols, as suggested by internal strings).

### Suspicious and Malicious Behaviors

*   **Windows Service Persistence:**
    The function `fcn.140001424` explicitly calls `RegisterServiceCtrlHandlerW` and `SetServiceStatus`. This indicates the binary is designed to run as a **Windows Service**, allowing it to start automatically on boot and run in the background without a visible user interface.
*   **Network Communication & Listener:**
    Several functions (`fcn.14000ca2c`, `fcn.14000643c`, `fcn.14000bb34`) interact with the `WS2_32.dll` (Winsock) library. Specifically:
    *   It implements logic to **bind and listen** on specific ports.
    *   It contains a dedicated routine for parsing "PORT" strings and handling IP/port conversions (`ntohs`, `htons`), which is common in protocols like FTP.
    *   It sets up socket options to manage connections effectively at the system level.
*   **Registry Manipulation:**
    The binary extensively interacts with the Windows Registry via `RegOpenKeyExW`, `RegCreateKeyExW`, and `RegSetValueExW`. It looks for specific configuration strings, including:
    *   `"FTP Client/Server Protocol"`
    *   Specific CLSIDs (e.g., `{6E590D61-F6BC-4dad-AC21-7DC40D304059}`). 
    This is often used by malware to store configuration data, such as C2 server addresses or persistence settings, in a way that appears integrated with the OS.
*   **Resource Extraction & DLL Loading:**
    Function `fcn.1400055dc` utilizes `LoadLibraryExW`, `FindResourceExW`, and `LoadResource`. This is a common technique used to **extract and load an embedded payload or configuration module** from memory after the initial execution, potentially to hide the primary malicious functionality from static analysis.

### Notable Techniques Observed
*   **COM Integration:** The code heavily utilizes COM (Component Object Model) components (`CoTaskMemAlloc`, `CoCreateInstance`). This is often used by sophisticated malware to interact with Windows components in a "legitimate" way, making it harder for basic heuristic scanners to flag the behavior.
*   **Dynamic String Handling:** Many functions involve complex logic to handle and compare registry keys and configuration strings at runtime, suggesting a flexible configuration system (likely defined in the modified registry keys).
*   **Robust Error Handling/Exception Traps:** The use of `RtlCaptureContext` and `RtlLookupFunctionEntry` (in `fcn.14000dbb0`) indicates that the author implemented advanced, low-level exception handling to ensure the service remains stable even if an operation is interrupted or fails.

### Summary for Intelligence Purposes
The binary is likely a **malicious agent designed for a persistent backdoor or a proxy server.** It utilizes standard Windows Service features for persistence, uses COM and Registry keys to hide its configuration, and contains a robust networking stack capable of handling multiple connections in the background.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1543.003** | Create or Modify System Process: Windows Service | The use of `RegisterServiceCtrlHandlerW` and `SetServiceStatus` indicates the binary is designed to run as a persistent Windows service. |
| **T1071.001** | Application Layer Protocol: FTP | The implementation of "PORT" string parsing, IP/port conversion, and binding logic suggests the use of standard application layer protocols for communication. |
| **T1112** | Modify Registry Configuration | The binary extensively interacts with registry keys to store configuration data (like C2 settings) in a way that mimics legitimate system integration. |
| **T1027** | Software Packing | The use of `FindResourceExW` and `LoadLibraryExW` to extract and load embedded modules suggests an attempt to hide the primary payload from static analysis. |
| **T1106** | Native API | The usage of COM components and `Rtl` functions (like `RtlCaptureContext`) demonstrates the use of native Windows APIs to ensure stability and blend in with legitimate system behavior. |

---

## Indicators of Compromise

Based on the provided data, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `{6E590D61-F6BC-4dad-AC21-7DC40D304059}` (Specific CLSID utilized for configuration/persistence via the Windows Registry)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Configuration Strings:** "FTP Client/Server Protocol" (Used to determine communication parameters).
*   **Persistence Mechanism:** Use of `RegisterServiceCtrlHandlerW` and `SetServiceStatus` to establish the binary as a background Windows Service.
*   **Evasion/Loading Technique:** Utilization of `FindResourceExW`, `LoadResource`, and `LoadLibraryExW` to extract and load embedded modules into memory (suggesting a multi-stage loader or hidden payload).
*   **Network Behavior Pattern:** Specific routines for parsing "PORT" strings and performing IP/port conversions (`ntohs`, `htons`) characteristic of FTP-based proxying or tunneling.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom 
2. **Malware type**: backdoor / loader
3. **Confidence**: Medium

**Key evidence**:
*   **Persistent Backend Architecture:** The use of `RegisterServiceCtrlHandlerW` and `SetServiceStatus` confirms it is designed to run as a persistent Windows Service, which is a hallmark of a backdoor or high-level proxy agent.
*   **Evasive Loading Techniques:** The combination of `FindResourceExW`, `LoadResource`, and `LoadLibraryExW` indicates a "loader" functionality where the primary malicious payload or configuration is hidden in the resource section to bypass static analysis.
*   **Network Infrastructure Logic:** The implementation of specific networking routines (parsing "PORT" strings, `ntohs`/`htos` conversions) suggests it functions as a listener or proxy, facilitating remote communication and likely serving as an entry point for further exploitation.
