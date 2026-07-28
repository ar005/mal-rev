# Threat Analysis Report

**Generated:** 2026-07-27 16:10 UTC
**Sample:** `0bc1875fd1b702e00722e2881a529ad770056b907a2fbcb1fecaf883ddd6d050_0bc1875fd1b702e00722e2881a529ad770056b907a2fbcb1fecaf883ddd6d050.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0bc1875fd1b702e00722e2881a529ad770056b907a2fbcb1fecaf883ddd6d050_0bc1875fd1b702e00722e2881a529ad770056b907a2fbcb1fecaf883ddd6d050.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 3,726,848 bytes |
| MD5 | `a7f5813610510c8a4aeef8f4fb0d984e` |
| SHA1 | `6a05f6f09171bd36870c8315e1efa256cbe548d8` |
| SHA256 | `0bc1875fd1b702e00722e2881a529ad770056b907a2fbcb1fecaf883ddd6d050` |
| Overall entropy | 6.593 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,697,792 | 6.459 | No |
| `.rdata` | 1,789,952 | 6.291 | No |
| `.data` | 115,200 | 3.948 | No |
| `.pdata` | 68,608 | 6.176 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 46,080 | 7.654 | ⚠️ Yes |
| `.reloc` | 7,680 | 5.344 | No |

### Imports

**ADVAPI32.dll**: `SystemFunction036`, `GetSidSubAuthority`, `RegSetValueExW`, `RegQueryInfoKeyW`, `RegFlushKey`, `RegEnumValueW`, `RegEnumKeyExW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegCreateKeyExW`, `BuildTrusteeWithSidW`, `GetNamedSecurityInfoW`, `GetEffectiveRightsFromAclW`, `LookupAccountSidW`, `MapGenericMask`
**KERNEL32.dll**: `GetConsoleMode`, `GetConsoleOutputCP`, `WaitForSingleObject`, `MultiByteToWideChar`, `WriteConsoleW`, `HeapAlloc`, `GetEnvironmentVariableW`, `GetModuleHandleW`, `FormatMessageW`, `GetModuleHandleA`, `CreateThread`, `CreateWaitableTimerExW`, `SetWaitableTimer`, `Sleep`, `ExitProcess`
**ntdll.dll**: `RtlNtStatusToDosError`, `NtWriteFile`
**bcrypt.dll**: `BCryptGenRandom`
**USERENV.dll**: `GetUserProfileDirectoryW`
**VERSION.dll**: `GetFileVersionInfoSizeW`, `GetFileVersionInfoW`, `VerQueryValueW`
**NETAPI32.dll**: `NetApiBufferFree`, `NetShareEnum`
**WS2_32.dll**: `WSAAsyncSelect`
**ole32.dll**: `CoTaskMemFree`, `CoUninitialize`, `CoInitialize`, `CoCreateInstance`
**USER32.dll**: `MsgWaitForMultipleObjectsEx`, `GetQueueStatus`, `DestroyWindow`, `CreateWindowExW`, `UnregisterClassW`, `RegisterClassW`, `KillTimer`, `GetWindowLongPtrW`, `SetWindowLongPtrW`, `CharNextExA`, `SetTimer`, `PostMessageW`, `PostThreadMessageW`, `EnumWindows`, `GetWindowThreadProcessId`
**WINMM.dll**: `timeKillEvent`, `timeSetEvent`

## Extracted Strings

Total strings found: **21160** (showing first 100)

```
`.rdata
@.data
.pdata
@.fptable
@.reloc
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
H+|$(H
H[]_^A\A]A^A_
AWAVAUATVWUSH
L;d$(u$H
[]_^A\A]A^A_
AWAVAUATVWUSH
L;l$ u$L
[]_^A\A]A^A_
AWAVAUATVWUSH
L;l$ u$L
[]_^A\A]A^A_
AWAVAUATVWUSH
X[]_^A\A]A^A_
AWAVAUATVWUSH
H[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
t'L;d$Pt
[]_^A\A]A^A_
AWAVAUATVWUSH
L9L$@s
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
IoCompleH
UAVVWSH
`[_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
P[_^A^]
UAVVWSH
0[_^A^]
UAVVWSH
 [_^A^]
UAVVWSH
 [_^A^]
UAWAVAUATVWSH
fffff.
ffffff.
[_^A\A]A^A_]
fffff.
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
X[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAVVWSH
0[_^A^]
UAWAVAUATVWSH
ffffff.
H[_^A\A]A^A_]H
H[_^A\A]A^A_]
UAWAVAUATVWSH
X[_^A\A]A^A_]H
X[_^A\A]A^A_]
AWAVAUATVWSL
Affffff.
[_^A\A]A^A_
UAVVWSH
 [_^A^]H
 [_^A^]
UAVVWSH
 [_^A^]
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
$ffffff.
8[_^A\A]A^A_]I
8[_^A\A]A^A_]
AWAVVWSE1
[_^A^A_
fffff.
UAVVWSH
P[_^A^]
UAWAVAUATVWSH
ffffff.
X[_^A\A]A^A_]
UAVVWSH
 [_^A^]
 [_^A^]H
UAWAVAUATVWSH
X[_^A\A]A^A_]
UAVVWSH
`[_^A^]
UAWAVAUATVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140016346` | `0x140016346` | 1619174 | ✓ |
| `fcn.14000a120` | `0x14000a120` | 1618580 | ✓ |
| `fcn.14001ccd0` | `0x14001ccd0` | 1542341 | ✓ |
| `fcn.140164030` | `0x140164030` | 1395008 | ✓ |
| `fcn.14018a880` | `0x14018a880` | 1391187 | ✓ |
| `fcn.14018df10` | `0x14018df10` | 1342942 | ✓ |
| `fcn.1401066f0` | `0x1401066f0` | 735240 | ✓ |
| `method.QBig5Codec.virtual_16` | `0x14008df40` | 468198 | ✓ |
| `method.QBig5hkscsCodec.virtual_16` | `0x14008df50` | 468198 | ✓ |
| `method.QCP949Codec.virtual_16` | `0x14008df60` | 465270 | ✓ |
| `method.QEucKrCodec.virtual_16` | `0x14008df70` | 465270 | ✓ |
| `fcn.1400ccc10` | `0x1400ccc10` | 464505 | ✓ |
| `fcn.140070720` | `0x140070720` | 442988 | ✓ |
| `fcn.1400a9540` | `0x1400a9540` | 431475 | ✓ |
| `fcn.140062410` | `0x140062410` | 401469 | ✓ |
| `fcn.1400c4590` | `0x1400c4590` | 326348 | ✓ |
| `fcn.1400c46a0` | `0x1400c46a0` | 324010 | ✓ |
| `fcn.1400cbf10` | `0x1400cbf10` | 302521 | ✓ |
| `method.QTemporaryFileEngine.virtual_280` | `0x140103e50` | 299094 | ✓ |
| `method.QTemporaryFileEngine.virtual_40` | `0x140103c90` | 298841 | ✓ |
| `method.QTemporaryFileEngine.virtual_32` | `0x140103cf0` | 298738 | ✓ |
| `method.QTemporaryFileEngine.virtual_56` | `0x140103a20` | 298409 | ✓ |
| `method.QTemporaryFileEngine.virtual_272` | `0x140103550` | 297574 | ✓ |
| `method.QTemporaryFileEngine.virtual_264` | `0x140103320` | 297167 | ✓ |
| `method.QTemporaryFileEngine.virtual_48` | `0x1401031c0` | 296953 | ✓ |
| `method.QTemporaryFileEngine.virtual_24` | `0x140102e60` | 296907 | ✓ |
| `method.QTemporaryFileEngine.virtual_232` | `0x140102f50` | 296905 | ✓ |
| `fcn.140102aa0` | `0x140102aa0` | 296397 | ✓ |
| `fcn.1400a4340` | `0x1400a4340` | 285717 | ✓ |
| `fcn.1400a4850` | `0x1400a4850` | 234289 | ✓ |

### Decompiled Code Files

- [`code/fcn.14000a120.c`](code/fcn.14000a120.c)
- [`code/fcn.140016346.c`](code/fcn.140016346.c)
- [`code/fcn.14001ccd0.c`](code/fcn.14001ccd0.c)
- [`code/fcn.140062410.c`](code/fcn.140062410.c)
- [`code/fcn.140070720.c`](code/fcn.140070720.c)
- [`code/fcn.1400a4340.c`](code/fcn.1400a4340.c)
- [`code/fcn.1400a4850.c`](code/fcn.1400a4850.c)
- [`code/fcn.1400a9540.c`](code/fcn.1400a9540.c)
- [`code/fcn.1400c4590.c`](code/fcn.1400c4590.c)
- [`code/fcn.1400c46a0.c`](code/fcn.1400c46a0.c)
- [`code/fcn.1400cbf10.c`](code/fcn.1400cbf10.c)
- [`code/fcn.1400ccc10.c`](code/fcn.1400ccc10.c)
- [`code/fcn.140102aa0.c`](code/fcn.140102aa0.c)
- [`code/fcn.1401066f0.c`](code/fcn.1401066f0.c)
- [`code/fcn.140164030.c`](code/fcn.140164030.c)
- [`code/fcn.14018a880.c`](code/fcn.14018a880.c)
- [`code/fcn.14018df10.c`](code/fcn.14018df10.c)
- [`code/method.QBig5Codec.virtual_16.c`](code/method.QBig5Codec.virtual_16.c)
- [`code/method.QBig5hkscsCodec.virtual_16.c`](code/method.QBig5hkscsCodec.virtual_16.c)
- [`code/method.QCP949Codec.virtual_16.c`](code/method.QCP949Codec.virtual_16.c)
- [`code/method.QEucKrCodec.virtual_16.c`](code/method.QEucKrCodec.virtual_16.c)
- [`code/method.QTemporaryFileEngine.virtual_232.c`](code/method.QTemporaryFileEngine.virtual_232.c)
- [`code/method.QTemporaryFileEngine.virtual_24.c`](code/method.QTemporaryFileEngine.virtual_24.c)
- [`code/method.QTemporaryFileEngine.virtual_264.c`](code/method.QTemporaryFileEngine.virtual_264.c)
- [`code/method.QTemporaryFileEngine.virtual_272.c`](code/method.QTemporaryFileEngine.virtual_272.c)
- [`code/method.QTemporaryFileEngine.virtual_280.c`](code/method.QTemporaryFileEngine.virtual_280.c)
- [`code/method.QTemporaryFileEngine.virtual_32.c`](code/method.QTemporaryFileEngine.virtual_32.c)
- [`code/method.QTemporaryFileEngine.virtual_40.c`](code/method.QTemporaryFileEngine.virtual_40.c)
- [`code/method.QTemporaryFileEngine.virtual_48.c`](code/method.QTemporaryFileEngine.virtual_48.c)
- [`code/method.QTemporaryFileEngine.virtual_56.c`](code/method.QTemporaryFileEngine.virtual_56.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The code appears to be part of a large, complex application or framework (likely utilizing libraries like **Qt**, given the `method.QTemporaryFileEngine` naming convention). The primary purpose of these specific functions is high-level resource management, file system interaction, and internal object dispatching.

The presence of massive switch tables (e.g., in `fcn.1400ccc10` with 122 cases) indicates a "dispatcher" pattern common in frameworks where one function handles many different types of operations or objects by checking an ID at the start.

### Suspicious or Malicious Behaviors
While much of the code resembles standard library behavior for a large application, there are specific areas of interest:

*   **Dynamic API Resolution:** Function `fcn.140070720` utilizes `GetProcAddress`. This allows the binary to resolve function addresses at runtime rather than having them listed in the Import Address Table (IAT). While common in large software to manage complex dependencies, it is also a standard technique used by malware to hide its true capabilities from static analysis.
*   **Inter-Process Communication (IPC):** Function `fcn.1400c46a0` explicitly references and manages **Named Pipes** (`hNamedPipe`). Named pipes are often used for communication between different components of an application, but they can also be used by malware to facilitate communication between a malicious payload and a "loader" or across different processes on the same machine.
*   **Complex File Manipulation:** The functions under `method.QTemporaryFileEngine` (e.g., `virtual_280`, `virtual_56`, `virtual_264`) perform low-level file operations including `WriteFile`, `ReadFile`, `FlushFileBuffers`, and `SetFilePointerEx`. This suggests the application is designed to handle significant amounts of data, potentially involving temporary files as a buffer.

### Notable Techniques or Patterns
*   **Framework Integration:** The code exhibits a highly structured, modular design typical of large frameworks. If this were part of a "dropper" or "loader," it would indicate that the malware is disguised as, or integrated into, a legitimate-looking application.
*   **Robust Error Handling/Resource Management:** Several functions (e.g., `fcn.140062410`) are dedicated strictly to closing handles and freeing memory. This level of meticulous resource management is typical of professional software but can also be used in sophisticated malware to ensure the process remains stable while performing malicious actions.
*   **Abstraction Layers:** The heavy use of switch tables for method dispatching (as seen in `fcn.140016346` and `fcn.1400ccc10`) makes it difficult for an analyst to follow the execution flow without identifying the underlying "class" or "object" being passed through the system.

### Summary for Threat Intelligence
The binary exhibits characteristics of a **large, complex application**. While there is no "smoking gun" (like an immediate call to `ShellExecute` or a known C2 IP) in this specific snippet, the use of **dynamic API resolution** and **Named Pipes** are areas that warrant further investigation. The code's complexity suggests it may be part of a larger system where malicious functionality is hidden behind layers of legitimate-looking framework logic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of `GetProcAddress` for dynamic API resolution is a common method to hide functionality from static analysis by avoiding the Import Address Table (IAT). |
| T1036 | Proxy Execution | The use of Named Pipes for communication between different components (e.g., a loader and a payload) can be used to mask the origin or purpose of malicious actions. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Many of the provided strings appear to be obfuscated, junk data, or fragments of standard library functions; these were excluded as per your instructions.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **360Tray.H**: (Potential reference to 360 Total Security software components).

### **Mutex names / Named pipes**
*   **Named Pipes:** The behavioral analysis confirms the usage of **Named Pipes** (`hNamedPipe`) for inter-process communication (IPC). *Note: Specific pipe names were not provided in the raw string dump.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Dynamic API Resolution:** The binary utilizes `GetProcAddress` to resolve function addresses at runtime. This is a common technique used to hide functionality from static analysis and bypass security products.
*   **Framework Integration:** References to `QTemporaryFileEngine` indicate the use of the Qt framework, which may be used by the malware to blend in with legitimate software behavior.
*   **Signature Fragments:** The strings `AuthentiH1`, `HygonGenH1`, and `GenuineIH1` suggest potential logic for hardware checks or license validation (e.g., "Authentication," "Hygon," or "Genuine").

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: Medium

**Key evidence**:
*   **Evasion Techniques:** The use of `GetProcAddress` (T1027) for dynamic API resolution indicates a deliberate attempt to hide the application's true capabilities from static analysis by keeping the Import Address Table (IAT) clean.
*   **Multi-Stage Infrastructure:** The inclusion of Named Pipes (`hNamedPipe`, T1036) strongly suggests an inter-process communication (IPC) architecture, commonly used by loaders to facilitate communication between a primary stager and secondary payloads or for reflective loading.
*   **Obfuscated Complexity:** The high level of abstraction (large switch tables and complex resource management) is characteristic of sophisticated loaders designed to blend in with legitimate, large-scale frameworks (like Qt) to evade automated detection while hosting malicious components.
