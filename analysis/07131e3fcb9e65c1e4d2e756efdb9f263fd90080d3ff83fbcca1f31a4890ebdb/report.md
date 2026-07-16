# Threat Analysis Report

**Generated:** 2026-07-15 19:47 UTC
**Sample:** `07131e3fcb9e65c1e4d2e756efdb9f263fd90080d3ff83fbcca1f31a4890ebdb_07131e3fcb9e65c1e4d2e756efdb9f263fd90080d3ff83fbcca1f31a4890ebdb.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07131e3fcb9e65c1e4d2e756efdb9f263fd90080d3ff83fbcca1f31a4890ebdb_07131e3fcb9e65c1e4d2e756efdb9f263fd90080d3ff83fbcca1f31a4890ebdb.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 151,552 bytes |
| MD5 | `fe9db3aed6a04c762472afdf2face254` |
| SHA1 | `94e98b714bfb102d143957cf1e00bd45b5b8fa4d` |
| SHA256 | `07131e3fcb9e65c1e4d2e756efdb9f263fd90080d3ff83fbcca1f31a4890ebdb` |
| Overall entropy | 6.251 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771254577 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 99,328 | 6.283 | No |
| `.rdata` | 42,496 | 5.407 | No |
| `.data` | 2,560 | 2.969 | No |
| `.pdata` | 5,120 | 5.042 | No |
| `.rsrc` | 512 | 4.712 | No |
| `.reloc` | 512 | 4.014 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `GlobalLock`, `ExitProcess`, `GlobalMemoryStatusEx`, `GetModuleHandleW`, `WideCharToMultiByte`, `CreateProcessA`, `GetDiskFreeSpaceExA`, `GlobalUnlock`, `GetComputerNameA`, `DeleteFileA`, `GetVersionExA`, `GetSystemTimeAsFileTime`, `GetCurrentThreadId`, `GetCurrentProcessId`
**USER32.dll**: `GetDesktopWindow`, `SwapMouseButton`, `ReleaseDC`, `ToUnicode`, `GetKeyState`, `MapVirtualKeyW`, `DestroyWindow`, `GetDC`, `SendMessageW`, `CallNextHookEx`, `GetSystemMetrics`, `GetKeyboardState`, `GetClipboardData`, `CloseClipboard`, `SetWindowsHookExA`
**GDI32.dll**: `CreateCompatibleDC`, `SelectObject`, `GetDIBits`, `DeleteDC`, `DeleteObject`, `CreateCompatibleBitmap`, `BitBlt`
**ADVAPI32.dll**: `RegSetValueExA`, `RegCloseKey`, `RegQueryValueExA`, `RegCreateKeyExA`, `GetUserNameA`, `RegDeleteTreeA`, `RegOpenKeyExA`, `RegDeleteValueA`
**SHELL32.dll**: `SHGetFolderPathA`, `ShellExecuteA`
**ole32.dll**: `CoUninitialize`, `CoCreateInstance`, `CoInitialize`
**MSVCP140.dll**: `?_Decref@facet@locale@std@@UEAAPEAV_Facet_base@3@XZ`, `?_Getcoll@_Locinfo@std@@QEBA?AU_Collvec@@XZ`, `??1_Locinfo@std@@QEAA@XZ`, `??0_Locinfo@std@@QEAA@PEBD@Z`, `?_Incref@facet@locale@std@@UEAAXXZ`, `??0facet@locale@std@@IEAA@_K@Z`, `??1facet@locale@std@@MEAA@XZ`, `?always_noconv@codecvt_base@std@@QEBA_NXZ`, `?tolower@?$ctype@D@std@@QEBADD@Z`, `?tolower@?$ctype@D@std@@QEBAPEBDPEADPEBD@Z`, `?_Getcat@?$ctype@D@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z`, `??Bios_base@std@@QEBA_NXZ`, `_Strxfrm`, `??1_Lockit@std@@QEAA@XZ`, `??0_Lockit@std@@QEAA@H@Z`
**WININET.dll**: `InternetCloseHandle`, `HttpOpenRequestA`, `InternetConnectA`, `InternetOpenA`, `InternetReadFile`, `InternetOpenUrlA`, `HttpSendRequestA`
**AVICAP32.dll**: `capCreateCaptureWindowA`
**WINMM.dll**: `mciSendStringA`
**VCRUNTIME140_1.dll**: `__CxxFrameHandler4`
**VCRUNTIME140.dll**: `memmove`, `__std_exception_destroy`, `__std_exception_copy`, `__std_terminate`, `strchr`, `memcmp`, `memcpy`, `memset`, `__current_exception`, `__current_exception_context`, `__C_specific_handler`, `_CxxThrowException`
**api-ms-win-crt-stdio-l1-1-0.dll**: `_set_fmode`, `fputc`, `__p__commode`, `fflush`, `_get_stream_buffer_pointers`, `_fseeki64`, `fread`, `fsetpos`, `ungetc`, `setvbuf`, `fgetpos`, `fwrite`, `fclose`, `__stdio_common_vsprintf_s`, `fgetc`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `realloc`, `free`, `_callnewh`, `_set_new_mode`
**api-ms-win-crt-runtime-l1-1-0.dll**: `terminate`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `_initialize_onexit_table`, `system`, `_crt_atexit`, `_invoke_watson`, `_seh_filter_exe`, `_set_app_type`, `_errno`, `_get_initial_narrow_environment`, `_initterm`, `_initterm_e`, `exit`, `_exit`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy_s`, `isalnum`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_unlock_file`, `_lock_file`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtol`, `atoi`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-locale-l1-1-0.dll**: `_configthreadlocale`

## Extracted Strings

Total strings found: **685** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
udH;~ u^
t$ UWATAVAWH
A_A^A\_]
@SUVWATAVAWH
A_A^A\_^][
\$ UVWAVAWH
A_A^_^]
|$ UATAUAVAWH
A_A^A]A\]
@USVWATAVAWH
A_A^A\_^[]
@USVWATAVAWH
A_A^A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
t$ UWATAVAWH
A_A^A\_]
\$ UVWH
|$ UATAUAVAWH
Unknown
A_A^A]A\]
|$ UATAUAVAWH
A_A^A]A\]
|$ UATAUAVAWH
A_A^A]A\]
t$ UWATAVAWH
A_A^A\_]
UVWATAUAVAWH
A_A^A]A\_^]
t$ WATAUAVAWH
|$PH;=T
A_A^A]A\_
x UATAUAVAWH
A_A^A]A\]
UVWATAUAVAWH
A_A^A]A\_^]
l$ VWATH
L$ SVWH
VWATAVAWH
0A_A^A\_^
@SUVWAVAWH
HA_A^_^][
HA_A^_^][
HA_A^_^][
l$ VWAVH
@SUVWAWH
PA__^][
@SUVWAWH
PA__^][
@SUVWAVH
L90u"H
0A^_^][
@UVAVH
0A^^]H
WPLc
J
@SUVWAVH
0A^_^][
0A^_^][
0A^_^][
\$ UVWATAUAVAWH
@A_A^A]A\_^]
UVWATAUAVAWH
D$HI;F0
A_A^A]A\_^]
@UVWAVH
8A^_^]
8A^_^]
@VWAVH
UVWATAUAVAWH
0A_A^A]A\_^]
UVWATAUAVAWH
0A_A^A]A\_^]
@SUVWAVAWH
XA_A^_^][
XA_A^_^][
@SUATAVAWH
@A_A^A\][
@SUVAWH
8A_^][
SUVAWH
XA_^][
@SUVAWH
8A_^][
SUVAUH
HA]^][
SVATAUH
HA]A\^[
@VWAUAWH
t$Pfff
hA_A]_^
ukM;J ueA
VWATAVAWH
@A_A^A\_^
t$ WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.std::basic_ofstream_char__struct_std::char_traits_char__.virtual_0` | `0x140016634` | 40896 | ✓ |
| `method.std::basic_ifstream_char__struct_std::char_traits_char__.virtual_0` | `0x140016628` | 40820 | ✓ |
| `fcn.140010f40` | `0x140010f40` | 12168 | ✓ |
| `fcn.14000d9d0` | `0x14000d9d0` | 7685 | ✓ |
| `fcn.140003c40` | `0x140003c40` | 5458 | ✓ |
| `fcn.140013240` | `0x140013240` | 5141 | ✓ |
| `fcn.140017040` | `0x140017040` | 4098 | ✓ |
| `fcn.140016f80` | `0x140016f80` | 2373 | ✓ |
| `fcn.14000ffe0` | `0x14000ffe0` | 2105 | ✓ |
| `fcn.140002ab0` | `0x140002ab0` | 1811 | ✓ |
| `fcn.140011cb0` | `0x140011cb0` | 1522 | ✓ |
| `fcn.140005b50` | `0x140005b50` | 1497 | ✓ |
| `fcn.14000f7e0` | `0x14000f7e0` | 1327 | ✓ |
| `fcn.140003290` | `0x140003290` | 1317 | ✓ |
| `fcn.140014660` | `0x140014660` | 1315 | ✓ |
| `fcn.140015140` | `0x140015140` | 1172 | ✓ |
| `fcn.140006130` | `0x140006130` | 1010 | ✓ |
| `fcn.140015860` | `0x140015860` | 958 | ✓ |
| `fcn.140005340` | `0x140005340` | 895 | ✓ |
| `fcn.140002670` | `0x140002670` | 878 | ✓ |
| `main` | `0x14000a870` | 848 | ✓ |
| `fcn.140015f90` | `0x140015f90` | 836 | ✓ |
| `fcn.140012f10` | `0x140012f10` | 801 | ✓ |
| `fcn.140010b80` | `0x140010b80` | 757 | ✓ |
| `fcn.140002370` | `0x140002370` | 754 | ✓ |
| `fcn.140001880` | `0x140001880` | 717 | ✓ |
| `fcn.140001fc0` | `0x140001fc0` | 710 | ✓ |
| `fcn.140011840` | `0x140011840` | 710 | ✓ |
| `fcn.14000dca0` | `0x14000dca0` | 691 | ✓ |
| `fcn.14000e9a0` | `0x14000e9a0` | 690 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001880.c`](code/fcn.140001880.c)
- [`code/fcn.140001fc0.c`](code/fcn.140001fc0.c)
- [`code/fcn.140002370.c`](code/fcn.140002370.c)
- [`code/fcn.140002670.c`](code/fcn.140002670.c)
- [`code/fcn.140002ab0.c`](code/fcn.140002ab0.c)
- [`code/fcn.140003290.c`](code/fcn.140003290.c)
- [`code/fcn.140003c40.c`](code/fcn.140003c40.c)
- [`code/fcn.140005340.c`](code/fcn.140005340.c)
- [`code/fcn.140005b50.c`](code/fcn.140005b50.c)
- [`code/fcn.140006130.c`](code/fcn.140006130.c)
- [`code/fcn.14000d9d0.c`](code/fcn.14000d9d0.c)
- [`code/fcn.14000dca0.c`](code/fcn.14000dca0.c)
- [`code/fcn.14000e9a0.c`](code/fcn.14000e9a0.c)
- [`code/fcn.14000f7e0.c`](code/fcn.14000f7e0.c)
- [`code/fcn.14000ffe0.c`](code/fcn.14000ffe0.c)
- [`code/fcn.140010b80.c`](code/fcn.140010b80.c)
- [`code/fcn.140010f40.c`](code/fcn.140010f40.c)
- [`code/fcn.140011840.c`](code/fcn.140011840.c)
- [`code/fcn.140011cb0.c`](code/fcn.140011cb0.c)
- [`code/fcn.140012f10.c`](code/fcn.140012f10.c)
- [`code/fcn.140013240.c`](code/fcn.140013240.c)
- [`code/fcn.140014660.c`](code/fcn.140014660.c)
- [`code/fcn.140015140.c`](code/fcn.140015140.c)
- [`code/fcn.140015860.c`](code/fcn.140015860.c)
- [`code/fcn.140015f90.c`](code/fcn.140015f90.c)
- [`code/fcn.140016f80.c`](code/fcn.140016f80.c)
- [`code/fcn.140017040.c`](code/fcn.140017040.c)
- [`code/main.c`](code/main.c)
- [`code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c)

## Behavioral Analysis

This update incorporates the second batch of disassembly into the previous analysis. The new code confirms several suspicions from the first pass—specifically regarding **persistent communication (heartbeats)**, **remote payload retrieval**, and **active surveillance** capabilities.

### Updated Analysis: System Profiling & Malware Behavior

#### 1. Core Functionality and Purpose
The binary's role is expanded from "initial discovery" to a **fully-featured persistence and command-and-control (C2) agent**. It not only gathers information but also maintains a heartbeat with a remote server, can download additional components based on unique identifiers, and possesses the capability to capture visual data.

#### 2. Suspicious or Malicious Behaviors
*   **Heartbeat & Log Reporting:**
    *   The functions `fcn.140002370` and `fcn.140001880` build specific HTTP GET requests to a remote server:
        *   `/notify?event=heartbeat&user=[ID]`
        *   `/notify?event=log&msg=[Data]`
    *   **Analysis:** This indicates the malware is designed to stay active in the background. The "heartbeat" tells the attacker that the infection is still active, while the "log" feature allows the attacker to see errors or status updates from the local environment.

*   **Remote Payload/Resource Retrieval:**
    *   The function `fcn.140002670` constructs a specific URL for downloading content: `.../client-download?user=[ID]&filename=[Name]`.
    *   **Analysis:** This suggests that the malware is designed to fetch additional modules or "plugins" from the C2 server. The use of unique identifiers (likely the fingerprinting data collected in step 1) ensures that the attacker can deliver specific payloads tailored to different victims.

*   **Active Screen Scraping/Spyware:**
    *   The function `fcn.140001fc0` utilizes a sequence of GDI (Graphics Device Interface) calls: `GetDC(0)`, `CreateCompatibleDC`, `CreateCompatibleBitmap`, and **`BitBlt`**.
    *   **Analysis:** This is a classic implementation for screen capturing. `BitBlt` copies the pixel data from the desktop's device context to a memory buffer. Combined with the previous finding regarding "webcap.bmp" and the `AVICap32` library, this strongly indicates the malware can take screenshots or capture window content for exfiltration.

*   **Process Hiding & Execution:**
    *   The function `fcn.140005340` uses **Anonymous Pipes (`CreatePipe`)** and **`CreateProcessA`** to spawn `cmd.exe`, while concurrently starting a worker thread via `BeginThreadEx`.
    *   **Analysis:** This technique is often used to execute system commands or scripts in the background, potentially using the pipe to "hijack" the input/output of the child process so it does not interact directly with the user's console.

*   **Persistence Logic:**
    *   The `main` function contains a loop that executes every 2 seconds (e.g., `Sleep(2000)`).
    *   **Analysis:** This confirms the malware is designed to run as a persistent background service or resident process, constantly checking in with its home server.

---

### Updated Summary Table

| Feature | Technical Observation | Risk Level | Impact |
| :--- | :--- | :--- | :--- |
| **System Fingerprinting** | Collects CPU ID, RAM/Disk stats, and Hostname for "User" identification. | Medium | Identification of target environment. |
| **Heartbeat & Logging** | Sends periodic `heartbeat` and `log` signals via HTTP POST/GET. | High | Continuous C1 communication; indicates active command capability. |
| **Payload Delivery** | Constructing URLs with `client-download?user=...` to fetch files. | High | Ability to download secondary malware or remote tools. |
| **Screen Scraping** | Uses `BitBlt`, `GetDIBits`, and `CreateCompatibleBitmap`. | Critical | Active spyware; ability to capture visual information from the screen. |
| **Process Manipulation** | Spawns `cmd.exe` with pipes for background command execution. | High | Execution of arbitrary commands hidden from the user. |
| **Network Communication** | Uses `WinInet` (HTTP) to blend in with standard web traffic. | High | Difficulty in detection via simple network monitoring. |

### Final Conclusion
The binary is a **sophisticated backdoor/trojan**. It employs modular tactics: it identifies the host, establishes a persistent communication loop (heartbeat), can retrieve additional instructions or files from a remote server based on unique IDs, and contains functionality to visually "spy" on the user via screen scraping. The presence of multi-threaded logic suggest that it is designed to perform these tasks silently in the background without interrupting the user's experience.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the corresponding MITRE ATT&K techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071.001** | Web Protocols | The malware uses HTTP GET requests for "heartbeat" and "log" reporting to communicate with the C2 server via standard web traffic. |
| **T1105** | Ingress Tool Transfer | The malware constructs specific, ID-based URLs to download additional modules or "plugins" from a remote server. |
| **T1113** | Screen Capture | The use of GDI functions such as `BitBlt` and `GetDC` indicates the capability to capture screen data for spying/surveillance. |
| **T1059.003** | Windows Command Shell | The malware executes commands via `cmd.exe`, potentially using anonymous pipes to hide output from the user's console. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contained largely obfuscated or non-functional data; therefore, the primary actionable IOCs were derived from the Behavioral Analysis report regarding C2 infrastructure patterns and malicious functionality.

### **IP addresses / URLs / Domains**
*   **C2 Path Patterns:**
    *   `/notify?event=heartbeat&user=[ID]` (Heartbeat signal)
    *   `/notify?event=log&msg=[Data]` (Log reporting)
    *   `.../client-download?user=[ID]&filename=[Name]` (Payload retrieval)

### **File paths / Registry keys**
*   **Files:** 
    *   `webcap.bmp` (Identified as a resource for screen capture storage).

### **Mutex names / Named pipes**
*   **Pipes:** Anonymous Pipes (utilized via `CreatePipe` to hide the output of `cmd.exe`).

### **Hashes**
*   *(None identified in provided data)*

### **Other artifacts**
*   **C2 Patterns/Communication:** 
    *   HTTP GET/POST requests to `/notify` and `/client-download`.
    *   Persistence loop: Execution of tasks every 2000ms (2 seconds).
*   **Malicious API/Library Usage (Screen Scraping):**
    *   `BitBlt`
    *   `GetDIBits`
    *   `CreateCompatibleBitmap`
    *   `CreateCompatibleDC`
    *   `GetDC`
    *   `AVICap32` (Library utilized for media/capture capabilities)
*   **Process Manipulation:** 
    *   Use of `CreateProcessA` combined with pipes to execute `cmd.exe` in a "hidden" state.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://api.ipify.org`

---

## Malware Family Classification

1. **Malware family**: custom (RAT-style)
2. **Malware type**: backdoor / RAT
3. **Confidence**: High

**Key evidence**:
* **Persistence & C2 Communication:** The sample implements a standard "heartbeat" and logging mechanism (`/notify?event=heartbeat`) to maintain contact with a remote server, combined with a modular payload retrieval system that fetches custom tools based on unique victim IDs.
* **Spyware Capabilities:** The inclusion of GDI functions (specifically `BitBlt` and `GetDC`) along with the `AVICap32` library confirms active surveillance through screen scraping/capturing.
* **Evasive Execution:** The use of anonymous pipes to wrap `cmd.exe` executions indicates an intentional effort to run system commands in the background without displaying a console or interacting with the user's UI.
