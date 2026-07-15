# Threat Analysis Report

**Generated:** 2026-07-14 23:20 UTC
**Sample:** `0642f3d9f5ebb1fa0f2fa08c151797176fd7c81cfb9aaa650801ed6e77eaad18_0642f3d9f5ebb1fa0f2fa08c151797176fd7c81cfb9aaa650801ed6e77eaad18.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0642f3d9f5ebb1fa0f2fa08c151797176fd7c81cfb9aaa650801ed6e77eaad18_0642f3d9f5ebb1fa0f2fa08c151797176fd7c81cfb9aaa650801ed6e77eaad18.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 8 sections |
| Size | 2,859,680 bytes |
| MD5 | `394af1b15cfad030113ed68d8b750ac7` |
| SHA1 | `585b6064f6d6e29dcbcbcbfdec3a4d4525474252` |
| SHA256 | `0642f3d9f5ebb1fa0f2fa08c151797176fd7c81cfb9aaa650801ed6e77eaad18` |
| Overall entropy | 5.914 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1675386875 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,839,616 | 5.655 | No |
| `.rdata` | 845,312 | 5.216 | No |
| `.data` | 10,752 | 2.754 | No |
| `.pdata` | 111,616 | 5.864 | No |
| `.idata` | 9,216 | 3.04 | No |
| `.00cfg` | 512 | 0.155 | No |
| `.rsrc` | 2,048 | 1.827 | No |
| `.reloc` | 29,184 | 4.51 | No |

### Imports

**WS2_32.dll**: `closesocket`, `bind`, `accept`, `listen`, `WSACleanup`, `WSAStartup`, `gethostbyname`, `getsockopt`, `getsockname`, `ioctlsocket`, `getnameinfo`, `ntohs`, `freeaddrinfo`, `getaddrinfo`, `setsockopt`
**ADVAPI32.dll**: `RegisterEventSourceW`, `DeregisterEventSource`, `ReportEventW`
**USER32.dll**: `GetUserObjectInformationW`, `MessageBoxW`, `GetProcessWindowStation`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `SetUnhandledExceptionFilter`, `UnhandledExceptionFilter`, `RtlVirtualUnwind`, `RtlLookupFunctionEntry`, `RtlCaptureContext`, `TerminateProcess`, `GetCurrentProcess`, `ReadConsoleW`, `ReadConsoleA`, `SetConsoleMode`, `IsProcessorFeaturePresent`, `TlsFree`, `TlsSetValue`, `TlsGetValue`, `TlsAlloc`
**VCRUNTIME140.dll**: `__std_type_info_destroy_list`, `strstr`, `wcsstr`, `memmove`, `strchr`, `strrchr`, `memcmp`, `memset`, `memcpy`, `__C_specific_handler`, `memchr`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vswprintf`, `_setmode`, `ftell`, `__stdio_common_vfprintf`, `fwrite`, `fseek`, `fread`, `fopen`, `_fileno`, `fgets`, `fflush`, `ferror`, `clearerr`, `setbuf`, `feof`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoul`, `atoi`, `strtol`
**api-ms-win-crt-string-l1-1-0.dll**: `_strnicmp`, `strcspn`, `strncmp`, `strncpy`, `strcmp`, `isspace`, `_strdup`, `_stricmp`, `strspn`
**api-ms-win-crt-time-l1-1-0.dll**: `_gmtime64_s`, `_time64`
**api-ms-win-crt-utility-l1-1-0.dll**: `qsort`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_initialize_narrow_environment`, `_initialize_onexit_table`, `signal`, `strerror_s`, `_execute_onexit_table`, `_seh_filter_dll`, `_crt_atexit`, `_errno`, `_crt_at_quick_exit`, `terminate`, `perror`, `_register_onexit_function`, `_exit`, `_initterm_e`, `_initterm`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_fstat64i32`, `_stat64i32`, `_chmod`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `realloc`, `malloc`
**api-ms-win-crt-environment-l1-1-0.dll**: `getenv`

### Exports

`ACCESS_DESCRIPTION_free`, `ACCESS_DESCRIPTION_it`, `ACCESS_DESCRIPTION_new`, `ADMISSIONS_free`, `ADMISSIONS_get0_admissionAuthority`, `ADMISSIONS_get0_namingAuthority`, `ADMISSIONS_get0_professionInfos`, `ADMISSIONS_it`, `ADMISSIONS_new`, `ADMISSIONS_set0_admissionAuthority`, `ADMISSIONS_set0_namingAuthority`, `ADMISSIONS_set0_professionInfos`, `ADMISSION_SYNTAX_free`, `ADMISSION_SYNTAX_get0_admissionAuthority`, `ADMISSION_SYNTAX_get0_contentsOfAdmissions`, `ADMISSION_SYNTAX_it`, `ADMISSION_SYNTAX_new`, `ADMISSION_SYNTAX_set0_admissionAuthority`, `ADMISSION_SYNTAX_set0_contentsOfAdmissions`, `AES_bi_ige_encrypt`, `AES_cbc_encrypt`, `AES_cfb128_encrypt`, `AES_cfb1_encrypt`, `AES_cfb8_encrypt`, `AES_decrypt`, `AES_ecb_encrypt`, `AES_encrypt`, `AES_ige_encrypt`, `AES_ofb128_encrypt`, `AES_options`, `AES_set_decrypt_key`, `AES_set_encrypt_key`, `AES_unwrap_key`, `AES_wrap_key`, `ASIdOrRange_free`, `ASIdOrRange_it`, `ASIdOrRange_new`, `ASIdentifierChoice_free`, `ASIdentifierChoice_it`, `ASIdentifierChoice_new`, `ASIdentifiers_free`, `ASIdentifiers_it`, `ASIdentifiers_new`, `ASN1_ANY_it`, `ASN1_BIT_STRING_check`, `ASN1_BIT_STRING_free`, `ASN1_BIT_STRING_get_bit`, `ASN1_BIT_STRING_it`, `ASN1_BIT_STRING_name_print`, `ASN1_BIT_STRING_new`

## Extracted Strings

Total strings found: **13328** (showing first 100)

```
!This program cannot be run in DOS mode.
$
OKkQ.%8Q.%8Q.%8XV
F$9S.%8
F 9Z.%8
F!9Y.%8
F&9R.%8EE$9Z.%8Q.$8
G&9P.%8
G!9.,%8
G%9P.%8
G'9P.%8RichQ.%8
`.rdata
@.data
.pdata
@.idata
@.00cfg
@.rsrc
@.reloc
|$ ATAUAVAW
D$A_A^A]A\
|$ ATAUAVAW
D$A_A^A]A\
B0E3B$E
B8A3B,
BPE3BDE
BpE3BdE
J4A3J A
J@A3J,
B`E3BLE
BdE3BPE
JlA3JXA
BxE3BdE
B|E3BhE
H<D3H D
H@D3H$A3
HLD3H0D
HPD3H4D
HDD3H<A3
@USVWATAUAVH
A^A]A\_^[]
SUVWAV
pA^_^][
D3]A3
t$4D3H,D
\$ ATAVAW
0A_A^A\
0A_A^A\
t$ WATAUAVAW
HcT$pA
0A_A^A]A\_
UWATAUAW
PA_A]A\_]
PA_A]A\_]
l$ VAVAW
0A_A^^
0A_A^^
UWATAVAW
0A_A^A\_]
0A_A^A\_]
@SUATAW
8A_A\][
8A_A\][
@SUVWAV
@A^_^][
HcD$`H
@USATAVAWH
A_A^A\[]
@UATAW
;|$8~GH
ta;D$<
@SVWAUAV
`A^A]_^[
`A^A]_^[
WATAUAVAW
A_A^A]A\_
VATAUAVAW
A_A^A]A\^
@UWATAUAVAW
t$8H;|$Hu	f
~7ft$4
t$8H;|$Ht?
xA_A^A]A\_]
t$ WAVAW
 A_A^_
\$ UVWATAUAVAW
L$0;D$P
A_A^A]A\_^]
VWATAVAW
A_A^A\_^
0A_A^_
HcD$pH
HcD$pH
tKLcD$ H
UVWATAUAVAWH
',+</w
< .ubE
A_A^A]A\_^]
WATAUAVAW
@A_A^A]A\_
VWATAVAW
@A_A^A\_^
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180001ff0` | `0x180001ff0` | 1804535 | ✓ |
| `fcn.180001fd2` | `0x180001fd2` | 1804196 | ✓ |
| `fcn.18000287e` | `0x18000287e` | 1802276 | ✓ |
| `fcn.180001055` | `0x180001055` | 1801772 | ✓ |
| `fcn.180001258` | `0x180001258` | 1800877 | ✓ |
| `fcn.180002d24` | `0x180002d24` | 1800372 | ✓ |
| `fcn.180003161` | `0x180003161` | 1800090 | ✓ |
| `fcn.180001ee2` | `0x180001ee2` | 1799915 | ✓ |
| `fcn.1800022ed` | `0x1800022ed` | 1799167 | ✓ |
| `fcn.1800034e5` | `0x1800034e5` | 1799131 | ✓ |
| `fcn.180002ff9` | `0x180002ff9` | 1798331 | ✓ |
| `fcn.1800039fe` | `0x1800039fe` | 1797873 | ✓ |
| `fcn.1800027b6` | `0x1800027b6` | 1797618 | ✓ |
| `fcn.180002266` | `0x180002266` | 1797454 | ✓ |
| `fcn.1800028c4` | `0x1800028c4` | 1796049 | ✓ |
| `fcn.180002eb4` | `0x180002eb4` | 1795945 | ✓ |
| `fcn.180003ec7` | `0x180003ec7` | 1795717 | ✓ |
| `fcn.18000419c` | `0x18000419c` | 1794975 | ✓ |
| `fcn.1800035a8` | `0x1800035a8` | 1794688 | ✓ |
| `fcn.180002e23` | `0x180002e23` | 1794296 | ✓ |
| `fcn.180004bb5` | `0x180004bb5` | 1793334 | ✓ |
| `fcn.180003364` | `0x180003364` | 1792208 | ✓ |
| `fcn.180003fa8` | `0x180003fa8` | 1791572 | ✓ |
| `fcn.180004eb2` | `0x180004eb2` | 1790800 | ✓ |
| `fcn.180004fc5` | `0x180004fc5` | 1790165 | ✓ |
| `fcn.18000405c` | `0x18000405c` | 1790083 | ✓ |
| `fcn.1800058ee` | `0x1800058ee` | 1789957 | ✓ |
| `sym.libcrypto_1_1_x64.dll_i2s_ASN1_INTEGER` | `0x1800029c8` | 1789860 | ✓ |
| `fcn.180005114` | `0x180005114` | 1789844 | ✓ |
| `fcn.180004615` | `0x180004615` | 1789776 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001055.c`](code/fcn.180001055.c)
- [`code/fcn.180001258.c`](code/fcn.180001258.c)
- [`code/fcn.180001ee2.c`](code/fcn.180001ee2.c)
- [`code/fcn.180001fd2.c`](code/fcn.180001fd2.c)
- [`code/fcn.180001ff0.c`](code/fcn.180001ff0.c)
- [`code/fcn.180002266.c`](code/fcn.180002266.c)
- [`code/fcn.1800022ed.c`](code/fcn.1800022ed.c)
- [`code/fcn.1800027b6.c`](code/fcn.1800027b6.c)
- [`code/fcn.18000287e.c`](code/fcn.18000287e.c)
- [`code/fcn.1800028c4.c`](code/fcn.1800028c4.c)
- [`code/fcn.180002d24.c`](code/fcn.180002d24.c)
- [`code/fcn.180002e23.c`](code/fcn.180002e23.c)
- [`code/fcn.180002eb4.c`](code/fcn.180002eb4.c)
- [`code/fcn.180002ff9.c`](code/fcn.180002ff9.c)
- [`code/fcn.180003161.c`](code/fcn.180003161.c)
- [`code/fcn.180003364.c`](code/fcn.180003364.c)
- [`code/fcn.1800034e5.c`](code/fcn.1800034e5.c)
- [`code/fcn.1800035a8.c`](code/fcn.1800035a8.c)
- [`code/fcn.1800039fe.c`](code/fcn.1800039fe.c)
- [`code/fcn.180003ec7.c`](code/fcn.180003ec7.c)
- [`code/fcn.180003fa8.c`](code/fcn.180003fa8.c)
- [`code/fcn.18000405c.c`](code/fcn.18000405c.c)
- [`code/fcn.18000419c.c`](code/fcn.18000419c.c)
- [`code/fcn.180004615.c`](code/fcn.180004615.c)
- [`code/fcn.180004bb5.c`](code/fcn.180004bb5.c)
- [`code/fcn.180004eb2.c`](code/fcn.180004eb2.c)
- [`code/fcn.180004fc5.c`](code/fcn.180004fc5.c)
- [`code/fcn.180005114.c`](code/fcn.180005114.c)
- [`code/fcn.1800058ee.c`](code/fcn.1800058ee.c)
- [`code/sym.libcrypto_1_1_x64.dll_i2s_ASN1_INTEGER.c`](code/sym.libcrypto_1_1_x64.dll_i2s_ASN1_INTEGER.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The binary appears to be a piece of software that utilizes **OpenSSL** for network communication (indicated by the `OPENSSL_Applink` references and standard crypto library symbols). However, the included functions suggest it is heavily hardened against analysis. The presence of complex wrapper logic suggests this might be a "packer" or a "stub" designed to protect a primary payload that handles encrypted communications.

### Suspicious or Malicious Behaviors
*   **Anti-Debugging / Anti-Analysis:** 
    *   The function `fcn.180004eb2` explicitly calls **`IsDebuggerPresent()`**. This is a standard technique used by malware to determine if it is being analyzed in a debugger (like x64dbg or OllyDbg).
    *   The code contains several "check-and-terminate" patterns. If certain conditions are not met (likely related to memory integrity or the presence of analysis tools), the program calls `fcn.180002266`.
*   **Evasive Termination:** 
    *   Function `fcn.180002266` retrieves the current process handle and terminates it with the status code **`0xc0000409`** (STATUS_STACK_BUFFER_OVERRUN). This specific error code is often used to mask a deliberate exit as a crash, making it harder for an analyst to determine why the program stopped.
*   **Integrity Checking:** 
    *   Functions like `fcn.180002c4` and `fcn.180002e23` perform calculations on memory addresses/offsets and compare them against hardcoded constants. If these checks fail (which happens if the code is patched or modified by an analyst), the program triggers the aforementioned termination logic.

### Notable Techniques and Patterns
*   **Control Flow Guard (CFG) / Integrity Checks:** The repetitive pattern of calculating offsets based on memory addresses before proceeding indicates a form of **self-integrity checking**. This ensures that the binary hasn't been modified or hooked by security software/analysis tools.
*   **Exception Handling Manipulation:** Use of `SetUnhandledExceptionFilter` and `RtlCaptureContext` (in `fcn.180004eb2`) indicates an attempt to handle system exceptions gracefully while also checking the environment for debuggers.
*   **Obfuscated Strings/Data:** The string dump contains a large amount of non-human-readable data, which is typical in binaries that use encrypted strings or have undergone packing.

### Summary
This binary exhibits characteristics common in **malware (such as a Trojan or Downloader)** designed to protect its primary functionality from security researchers. It uses standard anti-debugging techniques and integrity checks to ensure it is running in an "original" state; if any tampering or analysis tools are detected, it intentionally crashes the process to prevent further inspection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Debugger Detected | The explicit call to `IsDebuggerPresent()` is a primary method used to identify if the code is being run within an analysis environment. |
| T1497 | Defensive Sandbox Detection | Integrity checks on memory addresses and offsets are performed to detect modifications or hooks from security tools or analysts. |
| T1036 | Debugger Detected | The use of `SetUnhandledExceptionFilter` and `RtlCaptureContext` is a common method for detecting the presence of debuggers via exception handling manipulation. |
| T1497 | Defensive Sandbox Detection | Terminating with error code `0xc0000409` (STATUS_STACK_BUFFER_OVERRUN) masks an intentional exit as a crash to mislead analysts. |
| T1027 | Obfuscated Files or Information | The presence of non-human-readable data and evidence of packing suggests an effort to hide the binary's strings and logic from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: The string dump contains a high volume of obfuscated data/junk characters typical of a packed binary. No network infrastructure or filesystem-specific IOCs were identified in the raw text.*

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (The symbols like `.rdata`, `.data`, and `.idata` are standard PE section headers and are not specific to a single malware sample).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Evasion Exit Code:** `0xc0000409` (STATUS_STACK_BUFFER_OVERRUN) — Used as a tactic to mask intentional crashes during anti-analysis checks.
*   **Anti-Debugging Functions:** `IsDebuggerPresent`, `SetUnhandledExceptionFilter`, and `RtlCaptureContext`.
*   **Packer/Loader Behavior:** The presence of high volumes of non-human-readable data and self-integrity checking logic (comparing memory offsets against constants) indicates the binary is likely a protected loader or packer.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High (for Type) / Low (for Family)
4. **Key evidence**:
    *   **Sophisticated Anti-Analysis Tactics:** The binary employs multiple layers of defense, including `IsDebuggerPresent`, exception handling manipulation (`SetUnhandledExceptionFilter`), and complex integrity checks to detect if the code has been tampered with or hooked by security tools.
    *   **Evasive Execution Strategy:** The use of a specific exit code (`0xc0000409`) specifically designed to mask an intentional crash as a stack buffer overflow indicates an active effort to deceive analysts during automated and manual analysis.
    *   **Protective Wrapper Characteristics:** The combination of OpenSSL integration, high volumes of non-human-readable data, and "check-and-terminate" logic suggests the binary functions as a hardened stub/packer designed to protect and deliver a secondary payload.
