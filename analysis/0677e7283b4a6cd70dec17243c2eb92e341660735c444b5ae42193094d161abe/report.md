# Threat Analysis Report

**Generated:** 2026-07-15 03:52 UTC
**Sample:** `0677e7283b4a6cd70dec17243c2eb92e341660735c444b5ae42193094d161abe_0677e7283b4a6cd70dec17243c2eb92e341660735c444b5ae42193094d161abe.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0677e7283b4a6cd70dec17243c2eb92e341660735c444b5ae42193094d161abe_0677e7283b4a6cd70dec17243c2eb92e341660735c444b5ae42193094d161abe.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64, 19 sections |
| Size | 238,535 bytes |
| MD5 | `9c7dfb001d92c18ab850f454310d4f1d` |
| SHA1 | `1ba3f939e8e76f597ccbfc97175003ccce95ec7a` |
| SHA256 | `0677e7283b4a6cd70dec17243c2eb92e341660735c444b5ae42193094d161abe` |
| Overall entropy | 5.749 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774221791 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 8,192 | 6.117 | No |
| `.data` | 512 | 1.601 | No |
| `.rdata` | 1,536 | 3.936 | No |
| `.pdata` | 1,024 | 2.823 | No |
| `.xdata` | 512 | 3.587 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 1,024 | 3.199 | No |
| `.idata` | 2,048 | 3.91 | No |
| `.CRT` | 512 | 0.202 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 512 | 1.031 | No |
| `/4` | 1,024 | 1.221 | No |
| `/19` | 160,768 | 5.987 | No |
| `/31` | 7,168 | 4.521 | No |
| `/45` | 9,216 | 5.318 | No |
| `/57` | 2,048 | 4.194 | No |
| `/70` | 1,024 | 4.013 | No |
| `/81` | 10,752 | 1.998 | No |
| `/92` | 1,536 | 1.382 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegOpenKeyExA`, `RegQueryValueExA`, `RegSetValueExA`
**KERNEL32.dll**: `CheckRemoteDebuggerPresent`, `CloseHandle`, `CreateThread`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `EnterCriticalSection`, `FlushInstructionCache`, `GetCurrentProcess`, `GetLastError`, `GetModuleFileNameA`, `GetProcAddress`, `GetTickCount`, `InitializeCriticalSection`, `IsDebuggerPresent`, `LeaveCriticalSection`
**msvcrt.dll**: `__iob_func`, `_amsg_exit`, `_initterm`, `_lock`, `_unlock`, `abort`, `calloc`, `free`, `fwrite`, `realloc`, `strlen`, `strncmp`, `vfprintf`
**USER32.dll**: `DispatchMessageA`, `GetMessageA`, `TranslateMessage`
**WININET.dll**: `InternetCloseHandle`, `InternetOpenA`, `InternetOpenUrlA`, `InternetReadFile`

### Exports

`GetFileVersionInfoA`, `GetFileVersionInfoByHandle`, `GetFileVersionInfoExA`, `GetFileVersionInfoExW`, `GetFileVersionInfoSizeA`, `GetFileVersionInfoSizeExA`, `GetFileVersionInfoSizeExW`, `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerFindFileA`, `VerFindFileW`, `VerInstallFileA`, `VerInstallFileW`, `VerLanguageNameA`, `VerLanguageNameW`, `VerQueryValueA`, `VerQueryValueW`

## Extracted Strings

Total strings found: **6059** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.edata
@.idata
.reloc
AUATUWVSH
([^_]A\A]
([^_]A\A]
([^_]A\A]
AVAUATVSH
 [^A\A]A^
AWAVAUATUWVSH
https://E1
files.ca
tbox.moeH
/rzaifg.H
Mozilla/H
5.0 (WinH
dows NT H
10.0; WiH
n64; x64H
) AppleWH
ebKit/53H
[^_]A\A]A^A_
L+^0t~
ATUWVSH
PHc=#O
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
[^_A\A]A^A_]
ATWVSH
([^_A\H
tNHcA<H
tTIcB<L
t	HcA<
tCHcA<H
@' t	M
tKIcA<L
tSIcK<L
l:qi+[/
Software\Microsoft\Windows\CurrentVersion\Run
EdgeUpdate
Mingw-w64 runtime failure:

Address %p has no image-section
  VirtualQuery failed for %d bytes at address %p
  VirtualProtect failed with code 0x%x
  Unknown pseudo relocation protocol version %d.

  Unknown pseudo relocation bit size %d.

GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 10-win32 20220113
GCC: (GNU) 10-win32 20220113
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 10-win32 20220113
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 9.3-win32 20200320
GCC: (GNU) 10-win32 20220113
0`
p	P
b0`
p	
VERSION.dll
GetFileVersionInfoA
GetFileVersionInfoByHandle
GetFileVersionInfoExA
GetFileVersionInfoExW
GetFileVersionInfoSizeA
GetFileVersionInfoSizeExA
GetFileVersionInfoSizeExW
GetFileVersionInfoSizeW
GetFileVersionInfoW
VerFindFileA
VerFindFileW
VerInstallFileA
VerInstallFileW
VerLanguageNameA
VerLanguageNameW
VerQueryValueA
VerQueryValueW
RegCloseKey
RegOpenKeyExA
RegQueryValueExA
RegSetValueExA
CheckRemoteDebuggerPresent
CloseHandle
CreateThread
DeleteCriticalSection
DisableThreadLibraryCalls
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **6**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.VhDfCSCZjM_DoWork__` | `0x3740013a0` | 1850 | ✓ |
| `dbg._pei386_runtime_relocator` | `0x374002350` | 752 | ✓ |
| `sym.__write_memory.part.0` | `0x374002130` | 544 | ✓ |
| `sym._CRT_INIT` | `0x374001010` | 495 | ✓ |
| `dbg.__DllMainCRTStartup` | `0x374001200` | 324 | ✓ |
| `dbg.__mingw_TLScallback` | `0x3740027c0` | 224 | ✓ |
| `dbg._register_onexit_function` | `0x374002d60` | 212 | — |
| `dbg.__mingw_enum_import_library_names` | `0x374002bc0` | 178 | — |
| `dbg._FindPESectionByName` | `0x374002930` | 159 | — |
| `dbg.___w64_mingwthr_remove_key_dtor` | `0x374002730` | 137 | — |
| `dbg._IsNonwritableInCurrentImage` | `0x374002b30` | 133 | — |
| `entry1` | `0x374002020` | 129 | — |
| `dbg.__mingw_GetSectionForAddress` | `0x3740029d0` | 129 | — |
| `dbg.___w64_mingwthr_add_key_dtor` | `0x3740026b0` | 120 | — |
| `dbg._execute_onexit_table` | `0x374002e40` | 113 | — |
| `dbg.__report_error` | `0x3740020c0` | 112 | — |
| `dbg._FindPESectionExec` | `0x374002a90` | 108 | — |
| `sym.__mingwthr_run_key_dtors.part.0` | `0x374002640` | 107 | — |
| `dbg.__do_global_ctors` | `0x374001f60` | 106 | — |
| `sym.DllMain` | `0x374001e50` | 98 | — |
| `sym._FindPESection` | `0x3740028e0` | 72 | — |
| `dbg.__do_global_dtors` | `0x374001f20` | 58 | — |
| `sym.GetFileVersionInfoSizeA` | `0x374001ba0` | 57 | — |
| `sym.GetFileVersionInfoSizeExA` | `0x374001be0` | 57 | — |
| `sym.GetFileVersionInfoSizeExW` | `0x374001c20` | 57 | — |
| `sym.GetFileVersionInfoSizeW` | `0x374001c60` | 57 | — |
| `fcn.374002c90` | `0x374002c90` | 50 | — |
| `dbg.__dyn_tls_dtor` | `0x374001ff0` | 47 | — |
| `sym.GetFileVersionInfoA` | `0x374001ae0` | 46 | — |
| `sym.GetFileVersionInfoByHandle` | `0x374001b10` | 46 | — |

### Decompiled Code Files

- [`code/dbg.__DllMainCRTStartup.c`](code/dbg.__DllMainCRTStartup.c)
- [`code/dbg.__mingw_TLScallback.c`](code/dbg.__mingw_TLScallback.c)
- [`code/dbg._pei386_runtime_relocator.c`](code/dbg._pei386_runtime_relocator.c)
- [`code/sym.VhDfCSCZjM_DoWork__.c`](code/sym.VhDfCSCZjM_DoWork__.c)
- [`code/sym._CRT_INIT.c`](code/sym._CRT_INIT.c)
- [`code/sym.__write_memory.part.0.c`](code/sym.__write_memory.part.0.c)

## Behavioral Analysis

### Analysis Summary
This binary functions as a **downloader and loader (dropper)**. Its primary purpose is to evade detection, establish persistence on the infected machine, download a malicious payload from a remote server, decrypt that payload in memory, and execute it.

### Core Functionality
*   **Anti-Analysis/Evasion:** The code begins by checking for debuggers using `IsDebuggerPresent` and `CheckRemoteDebuggerPresent`. If a debugger is detected, the program performs a dummy calculation and exits to prevent analysis.
*   **Execution Delay:** It uses a calculated `Sleep` timer immediately after the anti-debugging check to stall execution, a common technique used to bypass automated sandbox analysis.
*   **Persistence:** The malware attempts to ensure it runs automatically upon system reboot by modifying the Windows Registry. Specifically, it targets the `Software\Microsoft\Windows\CurrentVersion\Run` key and creates or modifies a value named `"EdgeUpdate"`, masquerading as a legitimate browser update component.
*   **Payload Fetching:** It uses the WinINet API (`InternetOpenA`, `InternetOpenUrlA`) to connect to a remote server and download a chunk of data into a buffer allocated in memory via `VirtualAlloc`.
*   **Decryption/De-obfuscation:** Once the data is downloaded, the code performs two distinct loops of transformation (likely XORing and arithmetic shifts) on the buffer. This is done to "unpack" or decrypt the malicious payload before it is executed.
*   **Reflective Loading / Manual Mapping:** The code checks if the decrypted buffer contains a valid `MZ` header and `PE` signature. If confirmed, it performs manual mapping:
    *   It iterates through the headers of the *hidden* executable.
    *   It maps the sections into memory using `VirtualAlloc`.
    *   It resolves the required imports (DLLs and functions) for the hidden payload using `LoadLibraryA` and `GetProcAddress`.
    *   Finally, it uses `CreateThread` to execute the decrypted code in a new thread.

### Suspicious/Malicious Behaviors
*   **Anti-Debugging & Anti-Analysis:** Active checks for debuggers and the use of timed delays are clear indicators of malicious intent.
*   **Persistence Mechanism:** The creation of a "Run" key in the registry is a standard persistence technique used by malware to remain on a system across reboots.
*   **Masquerading:** Using the name `"EdgeUpdate"` for a registry key is a common tactic to blend in with legitimate Windows/Microsoft software.
*   **In-Memory Execution (Fileless Payload):** The manual mapping of a secondary executable into memory without saving it as a file on disk is a high-confidence indicator of malicious "loader" behavior, designed to evade traditional antivirus scanners that monitor the filesystem.

### Notable Techniques & Patterns
*   **WinINet for C2/Downloader:** The use of `InternetOpenA` and `InternetReadFile` suggests the malware can communicate with external Command and Control (C2) servers.
*   **Manual PE Loading:** The implementation of a full PE loader (handling relocations, imports, and section mapping) indicates this is a sophisticated "packer" or "loader" designed to execute a second-stage payload.
*   **Staged Decryption:** The presence of multiple loops to decode the downloaded buffer suggests that the primary payload is heavily obfuscated to evade network-based security appliances.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Evasion | The use of `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, and a `Sleep` timer are designed to detect analysis environments and stall execution to bypass automated sandboxes. |
| T1547.001 | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The malware modifies the `Run` registry key (specifically using the name "EdgeUpdate") to ensure it persists and executes automatically upon system reboot. |
| T1105 | Ingress Tool Transfer | The use of WinINet APIs (`InternetOpenA`, `InternetOpenUrlA`) indicates the remote fetching of a payload/tool from a server into memory. |
| T1435 | Decrypt Data | The execution of multiple loops involving XORing and arithmetic shifts is performed to de-obfuscate or decrypt the fetched buffer before it can be executed. |
| T1027 | Obfuscated Files/Information | The use of "Manual Mapping" (reflective loading) to execute a hidden payload in memory avoids writing the file to disk, thereby evading signature-based detection on the filesystem. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   **https://E1** (Potentialer fragmented or obfuscated C2/Download URL)
*   **files.ca** (Potential suspicious domain)
*   **tbox.moe** (Potential suspicious domain; note: "H" characters in string suggests obfuscation)

### **File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\Run`
*   **Registry Value Name:** `EdgeUpdate` (Used as a persistence mechanism to masquerade as a system update)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No hashes were present in the provided strings or behavioral analysis.*

### **Other artifacts**
*   **User-Agent String:** `Mozilla/H 5.0 (WinH dows NT H 10.0; WiH n64; x64H ) AppleWH ebKit/53H` (Note: The inclusion of "H" suggests a specific obfuscation pattern or custom naming convention).
*   **C2/Downloader Behavior:** Use of `InternetOpenA`, `InternetOpenUrlA`, and `InternetReadFile` to fetch payloads.
*   **Loader Techniques:** 
    *   Manual mapping of PE files into memory.
    *   Reflective loading (resolving imports via `GetProcAddress` and `LoadLibraryA`).
    *   In-memory execution of decrypted buffers to bypass disk-based scanning.
*   **Anti-Analysis Methods:** 
    *   Debugger checks (`IsDebuggerPresent`, `CheckRemoteDebuggerPresent`).
    *   Execution stalling/delaying via calculated sleep timers to evade sandbox analysis.

---

## Malware Family Classification

1. **Malware family**: Generic Loader / Dropper
2. **Malware type**: Downloader / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Reflective Loading & In-Memory Execution:** The sample utilizes manual mapping (resolving imports via `GetProcAddress` and `LoadLibraryA`) to execute a decrypted payload in memory without saving it to disk, a hallmark of sophisticated loaders designed to bypass signature-based antivirus.
*   **Multi-Stage Fetch & Decryption:** The use of WinINet APIs followed by multiple rounds of XOR/arithmetic decoding indicates a modular design where the initial binary acts as a "bridge" to deliver more complex malicious functionality (such as a RAT or InfoStealer).
*   **Evasion & Persistence Tactics:** The inclusion of anti-debugging checks (`IsDebuggerPresent`), execution delays to bypass sandboxes, and masqueraded registry keys ("EdgeUpdate") are standard techniques used by organized malware groups to maintain presence while avoiding detection.
