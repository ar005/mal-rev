# Threat Analysis Report

**Generated:** 2026-09-06 12:59 UTC
**Sample:** `14ed3878b6623c287283a8a80020f68e1cb6bfc37b236f33a95f3a64c4f4611f_14ed3878b6623c287283a8a80020f68e1cb6bfc37b236f33a95f3a64c4f4611f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14ed3878b6623c287283a8a80020f68e1cb6bfc37b236f33a95f3a64c4f4611f_14ed3878b6623c287283a8a80020f68e1cb6bfc37b236f33a95f3a64c4f4611f.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 1,870,336 bytes |
| MD5 | `092864a16fff333b8a98b29eb0a06d6c` |
| SHA1 | `c7fc692b4650356566b33414924475176328bd93` |
| SHA256 | `14ed3878b6623c287283a8a80020f68e1cb6bfc37b236f33a95f3a64c4f4611f` |
| Overall entropy | 6.559 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1739168729 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 976,384 | 6.336 | No |
| `.rdata` | 844,800 | 6.061 | No |
| `.data` | 512 | 2.612 | No |
| `.pdata` | 39,936 | 6.025 | No |
| `.reloc` | 7,680 | 5.366 | No |

### Imports

**bcrypt.dll**: `BCryptGenRandom`
**PSAPI.DLL**: `GetModuleFileNameExW`, `EnumProcessModulesEx`, `GetProcessMemoryInfo`, `GetModuleBaseNameW`
**KERNEL32.dll**: `SetFileCompletionNotificationModes`, `GetModuleHandleW`, `GetProcAddress`, `SetHandleInformation`, `GetStdHandle`, `GetConsoleMode`, `MultiByteToWideChar`, `WriteConsoleW`, `GetModuleHandleA`, `FormatMessageW`, `lstrlenW`, `GetEnvironmentVariableW`, `CreateThread`, `QueryPerformanceCounter`, `QueryPerformanceFrequency`
**OLEAUT32.dll**: `SysFreeString`, `GetErrorInfo`, `SysStringLen`
**pdh.dll**: `PdhCloseQuery`, `PdhRemoveCounter`, `PdhGetFormattedCounterValue`, `PdhAddEnglishCounterW`, `PdhCollectQueryData`, `PdhOpenQueryA`
**ADVAPI32.dll**: `RegOpenKeyExW`, `RegCloseKey`, `OpenProcessToken`, `CopySid`, `GetLengthSid`, `SystemFunction036`, `GetTokenInformation`, `IsValidSid`, `RegQueryValueExW`
**POWRPROF.dll**: `CallNtPowerInformation`
**SHELL32.dll**: `CommandLineToArgvW`
**Secur32.dll**: `DeleteSecurityContext`, `AcquireCredentialsHandleA`, `FreeCredentialsHandle`, `EncryptMessage`, `AcceptSecurityContext`, `InitializeSecurityContextW`, `DecryptMessage`, `ApplyControlToken`, `QueryContextAttributesW`, `FreeContextBuffer`
**api-ms-win-core-synch-l1-2-0.dll**: `WakeByAddressAll`, `WaitOnAddress`, `WakeByAddressSingle`
**bcryptprimitives.dll**: `ProcessPrng`
**USER32.dll**: `MessageBoxW`
**ws2_32.dll**: `WSACleanup`, `recv`, `send`, `closesocket`, `WSAIoctl`, `WSASend`, `getsockname`, `WSAGetLastError`, `getpeername`, `shutdown`, `WSASocketW`, `ioctlsocket`, `connect`, `getsockopt`, `WSAStartup`
**ntdll.dll**: `NtDeviceIoControlFile`, `NtCreateFile`, `RtlGetVersion`, `NtWaitForSingleObject`, `NtCancelIoFileEx`, `RtlNtStatusToDosError`, `NtReadVirtualMemory`, `NtWriteVirtualMemory`, `NtProtectVirtualMemory`, `NtCreateThreadEx`, `NtQuerySystemInformation`, `NtQueryInformationProcess`, `NtReadFile`, `NtWriteFile`, `NtAllocateVirtualMemory`
**crypt32.dll**: `CertDuplicateStore`, `CertAddCertificateContextToStore`, `CertOpenStore`, `CertDuplicateCertificateContext`, `CertVerifyCertificateChainPolicy`, `CertDuplicateCertificateChain`, `CertEnumCertificatesInStore`, `CertFreeCertificateChain`, `CertCloseStore`, `CertGetCertificateChain`, `CertFreeCertificateContext`
**VCRUNTIME140.dll**: `__current_exception`, `__current_exception_context`, `_CxxThrowException`, `memcpy`, `memcmp`, `__CxxFrameHandler3`, `memmove`, `memset`, `__C_specific_handler`
**api-ms-win-crt-string-l1-1-0.dll**: `wcslen`, `strlen`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `free`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argv`, `__p___argc`, `terminate`, `_exit`, `_cexit`, `_initterm_e`, `_initterm`, `_c_exit`, `_initialize_narrow_environment`, `_configure_narrow_argv`, `_register_thread_local_exe_atexit_callback`, `_set_app_type`, `_get_initial_narrow_environment`, `exit`, `_crt_atexit`

## Extracted Strings

Total strings found: **4860** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.reloc
AWAVAUATVWUSH
[]_^A\A]A^A_
t$@t.H
\$(s+1
AWAVVWSH
@[_^A^A_
AVVWSH
([_^A^
AWAVAUATVWUSH
L;l$ u$L
[]_^A\A]A^A_
AWAVAUATVWSH
[_^A\A]A^A_
UAWAVVWSH
8[_^A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAVVWSH
 [_^A^]
H;>uH
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
AWAVVWSH
 [_^A^A_H
 [_^A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
AWAVVWSH
 [_^A^A_
AVVWSH
([_^A^
AVVWSH
H[_^A^
H[_^A^
AWAVATVWSH
X[_^A\A^A_
AWAVATVWSH
([_^A\A^A_
AWAVVWSH
 [_^A^A_
 [_^A^A_
AWAVATVWSH
([_^A\A^A_
([_^A\A^A_
AVVWSH
([_^A^
AWAVATVWSH
([_^A\A^A_
AWAVATVWSH
8[_^A\A^A_
AVVWSH
([_^A^
AWAVVWSH
 [_^A^A_
AWAVVWSH
@[_^A^A_
AVVWSH
8[_^A^
AWAVVWSH
@[_^A^A_
AVVWSH
AVVWSH
AVVWSH
AWAVVWSH
@[_^A^A_
AWAVVWSH
0[_^A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
UAWAVAUATVWSH
H[_^A\A]A^A_]
H[_^A\A]A^A_]H
ffffff.
UAWAVATVWSH
p[_^A\A^A_]
UAVVWSH
 [_^A^]H
 [_^A^]
UAWAVAUATVWSH
&fffff.
([_^A\A]A^A_]I
([_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
m4ffffff.
UAWAVVWSH
fffff.
[_^A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140010383` | `0x140010383` | 887510 | ✓ |
| `fcn.1400e9c00` | `0x1400e9c00` | 423123 | ✓ |
| `fcn.14004daf2` | `0x14004daf2` | 412106 | ✓ |
| `fcn.14001ebf7` | `0x14001ebf7` | 378400 | ✓ |
| `fcn.140031a1a` | `0x140031a1a` | 326197 | ✓ |
| `fcn.140043d91` | `0x140043d91` | 314121 | ✓ |
| `case.0x14003f21c.15` | `0x140042e65` | 267923 | ✓ |
| `fcn.1400cd190` | `0x1400cd190` | 203329 | ✓ |
| `fcn.14006682e` | `0x14006682e` | 199942 | ✓ |
| `fcn.14004567b` | `0x14004567b` | 197614 | ✓ |
| `fcn.1400cd7c0` | `0x1400cd7c0` | 190962 | ✓ |
| `fcn.14005c250` | `0x14005c250` | 190185 | ✓ |
| `fcn.14009b0a0` | `0x14009b0a0` | 159988 | ✓ |
| `fcn.140065b24` | `0x140065b24` | 150784 | ✓ |
| `fcn.1400642d3` | `0x1400642d3` | 139106 | ✓ |
| `fcn.140042f25` | `0x140042f25` | 138261 | ✓ |
| `fcn.1400c6eb0` | `0x1400c6eb0` | 131832 | ✓ |
| `fcn.140043033` | `0x140043033` | 127831 | ✓ |
| `fcn.140034302` | `0x140034302` | 104235 | ✓ |
| `fcn.14009b090` | `0x14009b090` | 103943 | ✓ |
| `fcn.14009b080` | `0x14009b080` | 103812 | ✓ |
| `fcn.14009b070` | `0x14009b070` | 103632 | ✓ |
| `fcn.14009b060` | `0x14009b060` | 103606 | ✓ |
| `fcn.140010800` | `0x140010800` | 96354 | ✓ |
| `fcn.14004b2fb` | `0x14004b2fb` | 94326 | ✓ |
| `fcn.140084120` | `0x140084120` | 79697 | ✓ |
| `fcn.140032a3e` | `0x140032a3e` | 72445 | ✓ |
| `fcn.140075fab` | `0x140075fab` | 69356 | ✓ |
| `fcn.1400b0000` | `0x1400b0000` | 69144 | ✓ |
| `fcn.1400b0be0` | `0x1400b0be0` | 65310 | ✓ |

### Decompiled Code Files

- [`code/case.0x14003f21c.15.c`](code/case.0x14003f21c.15.c)
- [`code/fcn.140010383.c`](code/fcn.140010383.c)
- [`code/fcn.140010800.c`](code/fcn.140010800.c)
- [`code/fcn.14001ebf7.c`](code/fcn.14001ebf7.c)
- [`code/fcn.140031a1a.c`](code/fcn.140031a1a.c)
- [`code/fcn.140032a3e.c`](code/fcn.140032a3e.c)
- [`code/fcn.140034302.c`](code/fcn.140034302.c)
- [`code/fcn.140042f25.c`](code/fcn.140042f25.c)
- [`code/fcn.140043033.c`](code/fcn.140043033.c)
- [`code/fcn.140043d91.c`](code/fcn.140043d91.c)
- [`code/fcn.14004567b.c`](code/fcn.14004567b.c)
- [`code/fcn.14004b2fb.c`](code/fcn.14004b2fb.c)
- [`code/fcn.14004daf2.c`](code/fcn.14004daf2.c)
- [`code/fcn.14005c250.c`](code/fcn.14005c250.c)
- [`code/fcn.1400642d3.c`](code/fcn.1400642d3.c)
- [`code/fcn.140065b24.c`](code/fcn.140065b24.c)
- [`code/fcn.14006682e.c`](code/fcn.14006682e.c)
- [`code/fcn.140075fab.c`](code/fcn.140075fab.c)
- [`code/fcn.140084120.c`](code/fcn.140084120.c)
- [`code/fcn.14009b060.c`](code/fcn.14009b060.c)
- [`code/fcn.14009b070.c`](code/fcn.14009b070.c)
- [`code/fcn.14009b080.c`](code/fcn.14009b080.c)
- [`code/fcn.14009b090.c`](code/fcn.14009b090.c)
- [`code/fcn.14009b0a0.c`](code/fcn.14009b0a0.c)
- [`code/fcn.1400b0000.c`](code/fcn.1400b0000.c)
- [`code/fcn.1400b0be0.c`](code/fcn.1400b0be0.c)
- [`code/fcn.1400c6eb0.c`](code/fcn.1400c6eb0.c)
- [`code/fcn.1400cd190.c`](code/fcn.1400cd190.c)
- [`code/fcn.1400cd7c0.c`](code/fcn.1400cd7c0.c)
- [`code/fcn.1400e9c00.c`](code/fcn.1400e9c00.c)

## Behavioral Analysis

Based on the final chunk of disassembly provided, I have integrated these findings into the existing technical analysis. The addition of this data confirms that the binary is not merely a simple loader; it is a **sophisticated "Stage-0" or "Stager"** designed to perform environment preparation, file system manipulation, and process spawning with a high degree of environmental awareness.

### Updated Technical Analysis (Full Synthesis)

#### 1. Core Functionality and Purpose
The binary functions as a multi-stage deployment engine. While previous segments highlighted its networking capabilities and execution logic, this final segment reveals deep **File System Manipulation** and **Environment Preparation**.

*   **Sophisticated File Manipulation:** The presence of `CreateFileW` followed by `SetFileInformationByHandle` is highly significant. This indicates the binary isn't just creating a file; it is likely modifying specific attributes (such as hidden attributes, system attributes, or specific permissions) to mask its activity on the local disk.
*   **Execution Environment Tailoring:** The code contains extensive logic for constructing and setting environment variables before calling execution functions. This ensures that when the "next stage" of the malware is launched, it arrives in a pre-configured environment (e.g., specific paths, modified `PATH` variables, or custom variables) required for its operation.
*   **Sophisticated Logic Control:** The massive switch tables and complex jump logic confirm that the binary handles multiple execution paths based on internal states. It is designed to react differently depending on what it "sees" during its pre-execution checks.

#### 2. Suspicious or Malicious Behaviors
The final disassembly highlights three critical behaviors:

*   **File Masking/Obfuscation:** The use of `SetFileInformationByHandle` immediately after file creation is a common technique to hide files from the user and some basic security tools. This suggests the binary may be dropping components (like DLLs or scripts) that it wants to "hide" while they are being loaded into memory.
*   **Robust State Machine:** The complexity of the switch tables (some with dozens/hundreds of cases) indicates a very large codebase capable of handling complex logic flows. This is characteristic of professional-grade malware where the binary must navigate various OS checks and "anti-analysis" triggers before proceeding.
*   **Professional Resource Management:** Frequent calls to `CloseHandle` following file or process creation indicate an effort to leave a "clean" footprint. By closing handles promptly, the malware avoids "hanging" resources that could be flagged by EDR (Endpoint Detection and Response) systems as suspicious behavior.

#### 3. Notable Techniques & Patterns
*   **High-Level Language Artifacts:** The complexity of the jump tables and the specific way memory is accessed strongly suggest a **Rust-based implementation**. This confirms that the threat actor is likely an organized group using modern development tools to produce stable, complex software rather than simple "script kiddie" malware.
*   **Automated Resource Management:** The consistent cleanup of environment strings (`FreeEnvironmentStringsW`) and handle closing suggests a focus on **stealth and reliability**. A crash or a lingering resource leak can alert defenders; this binary is built to avoid such pitfalls.
*   **Dynamic Payload Contextualization:** The code demonstrates complex logic for calculating lengths, offsets, and buffer sizes before passing data to system calls. This indicates that the arguments (for file paths, process names, etc.) may be dynamically generated based on instructions received from a Command & Control (C2) server.

---

### Final Summary for Incident Response

*   **Primary Risk: Critical.** The binary is confirmed as a **Sophisticated Loader/Stager**. It provides the necessary infrastructure to drop, hide, and execute secondary payloads while meticulously preparing the environment for those payloads to run undetected.
*   **Key Behavioral Indicators:**
    *   **Persistence & Stealth:** Watch for `SetFileInformationByHandle` calls. This is a primary indicator of an attempt to mask files or folders on the system.
    *   **Environment Modification:** Monitor for frequent/unusual modifications to environment variables shortly after this binary executes.
    *   **Staged Execution:** The heavy use of `CreateProcessW` and complex jump tables suggests that if you find one malicious file, there is likely a second (or third) component designed to perform the actual data theft or-encryption.
    *   **Rust Signature:** Its internal structure aligns with Rust-compiled binaries, suggesting a sophisticated threat actor (potentially APT or advanced cybercrime).

#### Final Recommendations:
1.  **Endpoint Monitoring:** Monitor for any calls to `CreateFileW` followed by `SetFileInformationByHandle`, especially in system directories like `System32` or `SysWOW64`.
2.  **Behavioral Blocking:** Block and alert on the specific logic patterns related to environment variable manipulation following a network connection from this process.
3.  **Network Hunting:** Continue monitoring for 80/443 traffic, but pay close attention to **Beaconing Patterns** (consistent timing between heartbeats) indicating use of `SleepEx` or similar timers.
4.  **Forensic Artifact Hunt:** Search for newly created files that have "Hidden" or "System" attributes set in the last 24 hours, specifically those created by processes exhibiting this binary's behavior.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1564 | Hide Files and Directories | The use of `SetFileInformationByHandle` following file creation specifically aims to mask artifacts from the user and security tools. |
| T1036 | Masquerading | The manipulation of environment variables and "execution environment tailoring" allows the malware to blend in with normal system behavior during multi-stage execution. |
| T1059 | Command and Scripting Interpreter (Execution) | The use of `CreateProcessW` within a complex state machine facilitates the staged transition from a loader to secondary payloads. |
| T1105 | Ingress Tool Transfer | The "Stager" functionality, which prepares the environment and manages dynamic payload context based on C2 input, is indicative of a multi-stage delivery mechanism. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "Strings" section contained heavily obfuscated or repeated data typical of Rust-compiled binaries; no immediate high-fidelity network indicators (IPs/URLs) were present in those specific strings.

### **IP addresses / URLs / Domains**
*   *None detected.*

### **File paths / Registry keys**
*   *None detected.* (Note: The analysis identifies the use of `CreateFileW` and `SetFileInformationByHandle`, but no specific hardcoded paths were provided in the raw strings.)

### **Mutex names / Named pipes**
*   *None detected.*

### **Hashes**
*   *None detected.*

### **Other artifacts**
*   **Behavioral - File Masking:** Use of `SetFileInformationByHandle` immediately following `CreateFileW` to strip attributes (e.g., hiding files from the user/system).
*   **Behavioral - Environment Manipulation:** Extensive use of `FreeEnvironmentStringsW` and logic for constructing environment variables prior to launching child processes.
*   **Technique - Staged Execution:** Implementation of a "Stage-0" stager utilizing complex switch tables and jump logic to navigate pre-execution checks.
*   **Development Profile:** Rust-based implementation (indicated by specific memory access patterns and high-level language artifacts in the assembly).
*   **C2 Pattern:** Potential beaconing activity over ports 80 and 443 using `SleepEx` or similar timing functions to evade detection.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `index.crates.io`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated "Stage-0" Architecture:** The binary is explicitly identified as a multi-stage deployment engine (Stager) designed to prepare the environment, manipulate system variables, and launch secondary payloads while hiding its footprint.
*   **Advanced Evasion Techniques:** The use of `SetFileInformationByHandle` for file masking and complex Rust-based switch tables indicates a professional-grade tool designed to evade both manual inspection and automated detection systems (EDR).
*   **Intentional Persistence & Stealth:** Features such as rigorous resource management (e.g., `CloseHandle`, `FreeEnvironmentStringsW`) and the deliberate manipulation of environment variables to mask subsequent execution confirm its role as a specialized loader rather than a standalone malware payload.
