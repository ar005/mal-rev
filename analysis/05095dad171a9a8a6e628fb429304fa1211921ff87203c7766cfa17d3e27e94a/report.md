# Threat Analysis Report

**Generated:** 2026-07-12 10:46 UTC
**Sample:** `05095dad171a9a8a6e628fb429304fa1211921ff87203c7766cfa17d3e27e94a_05095dad171a9a8a6e628fb429304fa1211921ff87203c7766cfa17d3e27e94a.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05095dad171a9a8a6e628fb429304fa1211921ff87203c7766cfa17d3e27e94a_05095dad171a9a8a6e628fb429304fa1211921ff87203c7766cfa17d3e27e94a.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 5 sections |
| Size | 852,992 bytes |
| MD5 | `55ee7cf1d37a864d672147f371003a64` |
| SHA1 | `8d63280f5353f62f7ec1bfd21716545258c98552` |
| SHA256 | `05095dad171a9a8a6e628fb429304fa1211921ff87203c7766cfa17d3e27e94a` |
| Overall entropy | 7.783 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773182801 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,088 | 6.394 | No |
| `.rdata` | 29,184 | 5.546 | No |
| `.data` | 1,536 | 3.581 | No |
| `.rsrc` | 794,112 | 7.818 | ⚠️ Yes |
| `.reloc` | 2,048 | 6.333 | No |

### Imports

**KERNEL32.dll**: `GetTempPathW`, `WaitForSingleObject`, `Sleep`, `GetLastError`, `LockResource`, `CloseHandle`, `LoadResource`, `CreateProcessW`, `GetConsoleWindow`, `IsDebuggerPresent`, `SetUnhandledExceptionFilter`, `InitializeSListHead`, `GetCurrentProcess`, `SizeofResource`, `FindResourceW`
**USER32.dll**: `ShowWindow`
**ADVAPI32.dll**: `RegCreateKeyExW`, `RegSetValueExW`, `RegCloseKey`
**ole32.dll**: `CoTaskMemFree`, `CoUninitialize`, `CoCreateGuid`, `StringFromCLSID`, `CoInitialize`
**MSVCP140.dll**: `??1_Lockit@std@@QAE@XZ`, `??0_Lockit@std@@QAE@H@Z`, `?_Getgloballocale@locale@std@@CAPAV_Locimp@12@XZ`, `?uncaught_exception@std@@YA_NXZ`, `?_Id_cnt@id@locale@std@@0HA`, `?_Xout_of_range@std@@YAXPBD@Z`, `?cerr@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A`, `?id@?$codecvt@DDU_Mbstatet@@@std@@2V0locale@2@A`, `?_Fiopen@std@@YAPAU_iobuf@@PB_WHH@Z`, `?_Xlength_error@std@@YAXPBD@Z`, `??0?$basic_streambuf@DU?$char_traits@D@std@@@std@@IAE@XZ`, `?getloc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QBE?AVlocale@2@XZ`, `?_Init@?$basic_streambuf@DU?$char_traits@D@std@@@std@@IAEXXZ`, `?_Osfx@?$basic_ostream@DU?$char_traits@D@std@@@std@@QAEXXZ`, `??0?$basic_streambuf@_WU?$char_traits@_W@std@@@std@@IAE@XZ`
**ntdll.dll**: `NtQueryInformationProcess`
**WS2_32.dll**: `WSACleanup`, `closesocket`, `getaddrinfo`, `WSAStartup`, `send`, `socket`, `connect`, `setsockopt`, `freeaddrinfo`, `recv`
**VCRUNTIME140.dll**: `memmove`, `_except_handler4_common`, `__std_type_info_destroy_list`, `_CxxThrowException`, `memset`, `memcpy`, `__CxxFrameHandler3`, `__std_exception_destroy`, `__std_exception_copy`, `__std_terminate`
**api-ms-win-crt-runtime-l1-1-0.dll**: `exit`, `_register_onexit_function`, `_cexit`, `_crt_atexit`, `_execute_onexit_table`, `_initialize_onexit_table`, `_initialize_narrow_environment`, `_configure_narrow_argv`, `_invoke_watson`, `_initterm`, `_initterm_e`, `_seh_filter_dll`
**api-ms-win-crt-stdio-l1-1-0.dll**: `fclose`, `_get_stream_buffer_pointers`, `_fseeki64`, `fread`, `fsetpos`, `ungetc`, `setvbuf`, `fgetpos`, `fflush`, `fwrite`, `fputc`, `fgetc`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_lock_file`, `_unlock_file`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `malloc`, `_callnewh`

### Exports

`RunDLL`, `_vkEnumerateInstanceVersion`, `sqlite3_aggregate_context`, `sqlite3_aggregate_count`, `sqlite3_auto_extension`, `sqlite3_backup_finish`, `sqlite3_backup_init`, `sqlite3_backup_pagecount`, `sqlite3_backup_remaining`, `sqlite3_backup_step`, `sqlite3_bind_blob`, `sqlite3_bind_blob64`, `sqlite3_bind_double`, `sqlite3_bind_int`, `sqlite3_bind_int64`, `sqlite3_bind_null`, `sqlite3_bind_parameter_count`, `sqlite3_bind_parameter_index`, `sqlite3_bind_parameter_name`, `sqlite3_bind_text`, `sqlite3_bind_text16`, `sqlite3_bind_text64`, `sqlite3_bind_value`, `sqlite3_bind_zeroblob`, `sqlite3_bind_zeroblob64`, `sqlite3_blob_bytes`, `sqlite3_blob_close`, `sqlite3_blob_open`, `sqlite3_blob_read`, `sqlite3_blob_reopen`, `sqlite3_blob_write`, `sqlite3_busy_handler`, `sqlite3_busy_timeout`, `sqlite3_cancel_auto_extension`, `sqlite3_changes`, `sqlite3_clear_bindings`, `sqlite3_close`, `sqlite3_close_v2`, `sqlite3_collation_needed`, `sqlite3_collation_needed16`, `sqlite3_column_blob`, `sqlite3_column_bytes`, `sqlite3_column_bytes16`, `sqlite3_column_count`, `sqlite3_column_database_name`, `sqlite3_column_database_name16`, `sqlite3_column_decltype`, `sqlite3_column_decltype16`, `sqlite3_column_double`, `sqlite3_column_int`

## Extracted Strings

Total strings found: **2666** (showing first 100)

```
!This program cannot be run in DOS mode.
$
=:pa>;
=:pa9;
=:pa8;
=:pa<;
=:xa<;
=:aa4;
=:aa=;
=:aa?;
=:Rich
`.rdata
@.data
@.reloc
vVVVVV
vVVVVV
vVVVVV
u0PPPPP
B;0v>f
N<9
t2W
u%PPPPP
t9 9\9$|
u(PPPPP
u,PPPPP
uBA;S
J9Mr

5ntel
5Genu
	

	

	


	

	


	


	

	


	


	
















	

	

	

	



	


	


	


	

























bad allocation
Unknown exception
bad array new length
string too long
bad cast
WSAStartup failed
Socket creation failed
getaddrinfo failed
Connection failed
 HTTP/1.1

Host: 
Connection: close


ip-api.com
/json/
invalid string position
C:\Users\Administrator\Desktop\
)\Release\DLL.pdb
.text$di
.text$mn
.text$x
.text$yd
.idata$5
.00cfg
.CRT$XCA
.CRT$XCL
.CRT$XCZ
.CRT$XIA
.CRT$XIZ
.CRT$XPA
.CRT$XPZ
.CRT$XTA
.CRT$XTZ
.rdata
.rdata$r
.rdata$sxdata
.rdata$voltmd
.rdata$zzzdbg
.rtc$IAA
.rtc$IZZ
.rtc$TAA
.rtc$TZZ
.xdata$x
.edata
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.100062c7` | `0x100062c7` | 2245 | ✓ |
| `fcn.10001230` | `0x10001230` | 2183 | ✓ |
| `fcn.10001b60` | `0x10001b60` | 1791 | ✓ |
| `fcn.10002360` | `0x10002360` | 1506 | ✓ |
| `fcn.100064d6` | `0x100064d6` | 794 | ✓ |
| `fcn.1000682b` | `0x1000682b` | 793 | ✓ |
| `method.std::basic_filebuf_char__struct_std::char_traits_char__.virtual_28` | `0x10004290` | 636 | ✓ |
| `fcn.10005b90` | `0x10005b90` | 569 | ✓ |
| `fcn.10002e50` | `0x10002e50` | 560 | ✓ |
| `fcn.10002ad0` | `0x10002ad0` | 544 | ✓ |
| `fcn.10004a90` | `0x10004a90` | 495 | ✓ |
| `method.std::basic_stringbuf_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_12` | `0x10003860` | 492 | ✓ |
| `fcn.10003b10` | `0x10003b10` | 484 | ✓ |
| `method.std::basic_stringbuf_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_40` | `0x100035a0` | 474 | ✓ |
| `fcn.10005600` | `0x10005600` | 383 | ✓ |
| `fcn.10005320` | `0x10005320` | 355 | ✓ |
| `method.std::basic_stringbuf_wchar_t__struct_std::char_traits_wchar_t___class_std::allocator_wchar_t__.virtual_44` | `0x10003440` | 349 | ✓ |
| `method.std::basic_filebuf_char__struct_std::char_traits_char__.virtual_12` | `0x10004600` | 345 | ✓ |
| `fcn.10002950` | `0x10002950` | 320 | ✓ |
| `fcn.10004d80` | `0x10004d80` | 318 | ✓ |
| `fcn.10004960` | `0x10004960` | 296 | ✓ |
| `fcn.10002d20` | `0x10002d20` | 291 | ✓ |
| `fcn.10004fb0` | `0x10004fb0` | 286 | ✓ |
| `method.std::basic_filebuf_char__struct_std::char_traits_char__.virtual_40` | `0x10003f50` | 285 | ✓ |
| `fcn.100054e0` | `0x100054e0` | 283 | ✓ |
| `method.std::basic_filebuf_char__struct_std::char_traits_char__.virtual_32` | `0x10004170` | 282 | ✓ |
| `fcn.10006909` | `0x10006909` | 277 | ✓ |
| `fcn.1000605e` | `0x1000605e` | 270 | ✓ |
| `fcn.10005e9d` | `0x10005e9d` | 266 | ✓ |
| `fcn.10005850` | `0x10005850` | 264 | ✓ |

### Decompiled Code Files

- [`code/fcn.10001230.c`](code/fcn.10001230.c)
- [`code/fcn.10001b60.c`](code/fcn.10001b60.c)
- [`code/fcn.10002360.c`](code/fcn.10002360.c)
- [`code/fcn.10002950.c`](code/fcn.10002950.c)
- [`code/fcn.10002ad0.c`](code/fcn.10002ad0.c)
- [`code/fcn.10002d20.c`](code/fcn.10002d20.c)
- [`code/fcn.10002e50.c`](code/fcn.10002e50.c)
- [`code/fcn.10003b10.c`](code/fcn.10003b10.c)
- [`code/fcn.10004960.c`](code/fcn.10004960.c)
- [`code/fcn.10004a90.c`](code/fcn.10004a90.c)
- [`code/fcn.10004d80.c`](code/fcn.10004d80.c)
- [`code/fcn.10004fb0.c`](code/fcn.10004fb0.c)
- [`code/fcn.10005320.c`](code/fcn.10005320.c)
- [`code/fcn.100054e0.c`](code/fcn.100054e0.c)
- [`code/fcn.10005600.c`](code/fcn.10005600.c)
- [`code/fcn.10005850.c`](code/fcn.10005850.c)
- [`code/fcn.10005b90.c`](code/fcn.10005b90.c)
- [`code/fcn.10005e9d.c`](code/fcn.10005e9d.c)
- [`code/fcn.1000605e.c`](code/fcn.1000605e.c)
- [`code/fcn.100062c7.c`](code/fcn.100062c7.c)
- [`code/fcn.100064d6.c`](code/fcn.100064d6.c)
- [`code/fcn.1000682b.c`](code/fcn.1000682b.c)
- [`code/fcn.10006909.c`](code/fcn.10006909.c)
- [`code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_12.c`](code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_12.c)
- [`code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_28.c`](code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_28.c)
- [`code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_32.c`](code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_32.c)
- [`code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_40.c`](code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_40.c)
- [`code/method.std__basic_stringbuf_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_12.c`](code/method.std__basic_stringbuf_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_12.c)
- [`code/method.std__basic_stringbuf_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_40.c`](code/method.std__basic_stringbuf_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_40.c)
- [`code/method.std__basic_stringbuf_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_44.c`](code/method.std__basic_stringbuf_wchar_t__struct_std__char_traits_wchar_t___class_std__allocator_wchar_t__.virtual_44.c)

## Behavioral Analysis

### Overview
The analyzed binary functions as a **downloader/dropper** with integrated anti-analysis capabilities. Its primary role is to establish a network connection to a remote server, perform an HTTP request, and potentially download or prepare a secondary executable (`setup.exe`) while attempting to evade detection from sandbox environments or analysis tools.

### Key Behaviors
*   **Network Communication (C2/Data Retrieval):**
    *   The binary initializes networking via `WSAStartup`.
    *   It creates a socket and performs a DNS lookup (`getaddrinfo`) followed by a connection to a remote host.
    *   It constructs an **HTTP request** manually, including headers like `"HTTP/1.1"`, a target path (implied by logic), and `"Connection: close"`.
    *   It receives data from the server via `recv()` in a loop, suggesting it is downloading content or receiving commands.

*   **Persistence & System Manipulation:**
    *   The code utilizes `RegCreateKeyExW` and `RegSetValueExW` to create/modify Registry keys. This is a common technique for establishing **persistence** (ensuring the malware runs on startup) or storing configuration data for subsequent stages of an infection.

*   **Process Execution:**
    *   The binary uses `CreateProcessW` to execute a secondary file, specifically identified in strings and logic as **"setup.exe"**. This indicates it acts as a "dropper"—launching the actual payload or installer after certain conditions (like successful network communication) are met.

*   **Anti-Analysis & Evasion:**
    *   The function `fcn.100064d6` performs extensive **CPU fingerprinting**. It uses `IsProcessorFeaturePresent` and various `cpuid` checks to identify the specific features of the processor.
    *   These checks are typically used to detect if the code is running inside a **virtual machine (VM)**, an emulator, or a sandbox environment by looking for specific hardware signatures.

### Notable Techniques & Patterns
*   **Resource Loading:** The use of `FindResourceW` and `LoadResource` suggests that some components (such as the URL or strings used in the HTTP request) are embedded within the binary's resource section to hide them from simple string analysis.
*   **HTTP Hand-Crafting:** Rather than using a high-level library, the code manually constructs the HTTP request buffer and manages the raw socket. This is common in malware to minimize dependencies and bypass standard API monitoring of higher-level web libraries.
*   **Hardcoded Indicators:** The presence of `ip-api.com` in the string list suggests it may attempt to resolve its own geographical location or IP information, a common precursor to determining if the victim's environment is "worthy" (e.g., not a researcher's IP).
*   **Wait/Sleep Cycles:** The use of `Sleep()` and subsequent logic after networking suggest a "staged" execution where the malware waits for data to arrive or delays its primary payload to evade behavior-based detection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1071.001 | Application Layer Protocol: Web Protocols | The binary manually constructs HTTP requests and utilizes standard web ports to communicate with a remote server for data retrieval. |
| T1547.001 | Boot or Log-on Autostart Execution: Registry Run Keys | The use of `RegCreateKeyExW` and `RegSetValueExW` indicates an attempt to establish persistence by modifying registry keys. |
| T1204 | User Execution | The binary acts as a dropper by using `CreateProcessW` to launch a secondary executable (`setup.exe`) as the final payload. |
| T1497 | Virtualization/Sandbox Detection | The use of `cpuid` and `IsProcessorFeaturePresent` are signature techniques for detecting if the malware is running in a virtualized or analysis environment. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `ip-api.com` (Used for geolocation/environment checking)
*   `/json/` (Path associated with the `ip-api.com` service)

**File paths / Registry keys**
*   `C:\Users\Administrator\Desktop\` (Potential hardcoded staging path)
*   `setup.exe` (Identified as the secondary payload/dropper executable)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **C2 Communication Pattern:** Manual construction of HTTP headers (`HTTP/1.1` and `Connection: close`).
*   **Anti-Analysis Techniques:** 
    *   CPU fingerprinting via `IsProcessorFeaturePresent`.
    *   Detection of virtual machines/emulators using `cpuid` checks.
*   **Persistence Mechanism:** Use of `RegCreateKeyExW` and `RegSetValueExW` (Note: specific registry keys were not provided in the strings).
*   **Behavioral Indicator:** Utilization of `sqlite3` library functions, suggesting a local database for configuration or log storage.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High

**Key evidence**:
*   **Dropper Functionality:** The binary explicitly functions as a "staged" downloader, utilizing manual HTTP request construction (avoiding standard libraries) to fetch and execute a secondary payload (`setup.exe`) via `CreateProcessW`.
*   **Sophisticated Anti-Analysis:** The inclusion of specific CPU fingerprinting techniques (using `cpuid` and `IsProcessorFeaturePresent`) strongly indicates an intentional effort to detect virtualized or sandbox environments before executing the primary payload.
*   **Persistence & Environment Checking:** The combination of Registry modification for persistence, use of `ip-api.com` for potential geofencing/environment validation, and internal SQLite library usage suggests a structured infection chain typical of professional malware delivery components.
