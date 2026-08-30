# Threat Analysis Report

**Generated:** 2026-08-16 11:56 UTC
**Sample:** `0f69513905b9aeca9ad2659ae16f4363ac03a359abeac9ac05cab70a50f17b65_0f69513905b9aeca9ad2659ae16f4363ac03a359abeac9ac05cab70a50f17b65.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f69513905b9aeca9ad2659ae16f4363ac03a359abeac9ac05cab70a50f17b65_0f69513905b9aeca9ad2659ae16f4363ac03a359abeac9ac05cab70a50f17b65.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 99,634,176 bytes |
| MD5 | `3ef8789b65ac65590fdaa8d06c3cf377` |
| SHA1 | `89f04bbe88c83882827a5164ade78fd4db24b667` |
| SHA256 | `0f69513905b9aeca9ad2659ae16f4363ac03a359abeac9ac05cab70a50f17b65` |
| Overall entropy | 7.935 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770330162 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,444,032 | 6.331 | No |
| `.rdata` | 92,681,216 | 7.964 | ⚠️ Yes |
| `.data` | 16,384 | 0.73 | No |
| `.pdata` | 324,608 | 6.829 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 109,568 | 7.817 | ⚠️ Yes |
| `.reloc` | 56,832 | 5.494 | No |

### Imports

**kernel32.dll**: `LoadLibraryExA`, `GetConsoleWindow`, `GetLastError`, `FreeConsole`, `SetLastError`, `GetSystemInfo`, `GetPhysicallyInstalledSystemMemory`, `GetDiskFreeSpaceExW`, `GetTickCount64`, `SetFileTime`, `GlobalFree`, `GlobalAlloc`, `GlobalSize`, `Sleep`, `PostQueuedCompletionStatus`
**advapi32.dll**: `RegCloseKey`, `ImpersonateAnonymousToken`, `RevertToSelf`, `RegSetValueExW`, `RegQueryValueExW`, `RegCreateKeyExW`, `RegOpenKeyExW`, `RegEnumKeyExW`, `SystemFunction036`, `GetTokenInformation`
**oleaut32.dll**: `SysStringLen`, `GetErrorInfo`, `SysFreeString`
**ntdll.dll**: `NtReadFile`, `RtlNtStatusToDosError`, `NtCancelIoFileEx`, `NtOpenFile`, `NtDeviceIoControlFile`, `NtCreateFile`, `NtCreateNamedPipeFile`, `NtWriteFile`
**ws2_32.dll**: `WSASend`, `WSASocketW`, `ioctlsocket`, `connect`, `getsockopt`, `recv`, `closesocket`, `WSAIoctl`, `bind`, `getsockname`, `send`, `freeaddrinfo`, `getaddrinfo`, `WSAGetLastError`, `WSACleanup`
**bcrypt.dll**: `BCryptGenRandom`
**crypt32.dll**: `CertGetCertificateChain`, `CertFreeCertificateChain`, `CertVerifyCertificateChainPolicy`, `CertEnumCertificatesInStore`, `CertAddCertificateContextToStore`, `CertDuplicateCertificateContext`, `CertFreeCertificateContext`, `CertOpenStore`, `CertDuplicateCertificateChain`, `CertCloseStore`, `CertDuplicateStore`
**secur32.dll**: `DeleteSecurityContext`, `EncryptMessage`, `FreeContextBuffer`, `FreeCredentialsHandle`, `InitializeSecurityContextW`, `AcquireCredentialsHandleA`, `ApplyControlToken`, `QueryContextAttributesW`, `DecryptMessage`, `AcceptSecurityContext`
**bcryptprimitives.dll**: `ProcessPrng`
**api-ms-win-core-synch-l1-2-0.dll**: `WakeByAddressSingle`, `WakeByAddressAll`, `WaitOnAddress`
**KERNEL32.dll**: `UnhandledExceptionFilter`, `IsDebuggerPresent`, `IsProcessorFeaturePresent`, `GetCommandLineA`, `TerminateProcess`, `DeleteCriticalSection`, `InitializeCriticalSectionEx`, `LeaveCriticalSection`, `EnterCriticalSection`, `EncodePointer`, `GetACP`, `FlsSetValue`, `FlsGetValue`, `FlsAlloc`, `RaiseException`
**USER32.dll**: `RegisterWindowMessageA`, `IsProcessDPIAware`, `GetAsyncKeyState`, `RegisterTouchWindow`, `SetWindowDisplayAffinity`, `SetForegroundWindow`, `IsIconic`, `GetKeyboardState`, `ToUnicodeEx`, `GetKeyState`, `MapVirtualKeyExW`, `GetKeyboardLayout`, `ShowCursor`, `ClipCursor`, `GetClipCursor`
**SHELL32.dll**: `DragQueryFileW`, `DragFinish`, `ShellExecuteW`
**GDI32.dll**: `SelectObject`, `DeleteDC`, `CreateCompatibleDC`, `DeleteObject`, `CreateDIBSection`, `GetPixelFormat`, `SetPixelFormat`, `DescribePixelFormat`, `CreateRectRgn`, `GetDeviceCaps`, `ChoosePixelFormat`, `SwapBuffers`, `BitBlt`
**ADVAPI32.dll**: `OpenProcessToken`
**opengl32.dll**: `wglGetCurrentContext`, `wglMakeCurrent`, `wglGetProcAddress`, `wglDeleteContext`, `wglCreateContext`
**d3dcompiler_47.dll**: `D3DCompile`
**ole32.dll**: `CoCreateInstance`, `RevokeDragDrop`, `OleInitialize`, `CoInitializeEx`, `CoUninitialize`, `RegisterDragDrop`
**imm32.dll**: `ImmAssociateContextEx`, `ImmReleaseContext`, `ImmGetContext`, `ImmGetCompositionStringW`
**uxtheme.dll**: `SetWindowTheme`

## Extracted Strings

Total strings found: **273514** (showing first 100)

```
!This program cannot be run in DOS mode.
$
/Rich4
`.rdata
@.data
.pdata
@.fptable
@.reloc
AWAVAUATVWUSH
D$"\u00
([]_^A\A]A^A_
AWAVVWSH
 [_^A^A_
 [_^A^A_
UAWAVAUATVWSH
u#jHYH
[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
BHL;BPs1I
B(L;B0s!I
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
AWAVATVWSH
8[_^A\A^A_
8[_^A\A^A_
AWAVVWUSH
8[]_^A^A_
8[]_^A^A_
8[]_^A^A_
UAVVWSH
[_^A^]
UAVVWSH
0[_^A^]
UAVVWSH
0[_^A^]
UAVVWSH
0[_^A^]
UAVVWSH
0[_^A^]
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14008af2b` | `0x14008af2b` | 16816528 | ✓ |
| `fcn.14001af8b` | `0x14001af8b` | 6013964 | ✓ |
| `fcn.140191660` | `0x140191660` | 5968804 | ✓ |
| `fcn.140068c66` | `0x140068c66` | 5950365 | ✓ |
| `fcn.140097c32` | `0x140097c32` | 5698810 | ✓ |
| `fcn.140097c27` | `0x140097c27` | 5697892 | ✓ |
| `fcn.1400dc83e` | `0x1400dc83e` | 5447585 | ✓ |
| `fcn.14011d8f7` | `0x14011d8f7` | 5186436 | ✓ |
| `fcn.1401214c6` | `0x1401214c6` | 5172539 | ✓ |
| `fcn.14008f5c3` | `0x14008f5c3` | 5001055 | ✓ |
| `fcn.140571d2f` | `0x140571d2f` | 4905919 | ✓ |
| `fcn.1401721d9` | `0x1401721d9` | 4848840 | ✓ |
| `fcn.140172777` | `0x140172777` | 4847840 | ✓ |
| `fcn.140172c50` | `0x140172c50` | 4847098 | ✓ |
| `fcn.140173389` | `0x140173389` | 4845776 | ✓ |
| `fcn.14014f4d1` | `0x14014f4d1` | 4763365 | ✓ |
| `case.0x140232e2f.6108` | `0x14054ca82` | 4753227 | ✓ |
| `fcn.140192bcf` | `0x140192bcf` | 4719620 | ✓ |
| `fcn.140167db9` | `0x140167db9` | 4643861 | ✓ |
| `fcn.1405739c4` | `0x1405739c4` | 4627206 | ✓ |
| `case.0x14016f5f9.1807` | `0x1401b4c95` | 4583699 | ✓ |
| `fcn.1401cabec` | `0x1401cabec` | 4244751 | ✓ |
| `case.0x1400260bd.15` | `0x140030b38` | 4117470 | ✓ |
| `case.0x14020b0cf.171` | `0x140616ce5` | 4099894 | ✓ |
| `case.0x14020b0cf.173` | `0x140616d79` | 4099095 | ✓ |
| `case.0x14020b0cf.169` | `0x140616d56` | 4099047 | ✓ |
| `fcn.140616cc9` | `0x140616cc9` | 4098934 | ✓ |
| `fcn.140232d4e` | `0x140232d4e` | 4098154 | ✓ |
| `fcn.140250f16` | `0x140250f16` | 4010879 | ✓ |
| `fcn.1405815d7` | `0x1405815d7` | 3917017 | ✓ |

### Decompiled Code Files

- [`code/case.0x1400260bd.15.c`](code/case.0x1400260bd.15.c)
- [`code/case.0x14016f5f9.1807.c`](code/case.0x14016f5f9.1807.c)
- [`code/case.0x14020b0cf.169.c`](code/case.0x14020b0cf.169.c)
- [`code/case.0x14020b0cf.171.c`](code/case.0x14020b0cf.171.c)
- [`code/case.0x14020b0cf.173.c`](code/case.0x14020b0cf.173.c)
- [`code/case.0x140232e2f.6108.c`](code/case.0x140232e2f.6108.c)
- [`code/fcn.14001af8b.c`](code/fcn.14001af8b.c)
- [`code/fcn.140068c66.c`](code/fcn.140068c66.c)
- [`code/fcn.14008af2b.c`](code/fcn.14008af2b.c)
- [`code/fcn.14008f5c3.c`](code/fcn.14008f5c3.c)
- [`code/fcn.140097c27.c`](code/fcn.140097c27.c)
- [`code/fcn.140097c32.c`](code/fcn.140097c32.c)
- [`code/fcn.1400dc83e.c`](code/fcn.1400dc83e.c)
- [`code/fcn.14011d8f7.c`](code/fcn.14011d8f7.c)
- [`code/fcn.1401214c6.c`](code/fcn.1401214c6.c)
- [`code/fcn.14014f4d1.c`](code/fcn.14014f4d1.c)
- [`code/fcn.140167db9.c`](code/fcn.140167db9.c)
- [`code/fcn.1401721d9.c`](code/fcn.1401721d9.c)
- [`code/fcn.140172777.c`](code/fcn.140172777.c)
- [`code/fcn.140172c50.c`](code/fcn.140172c50.c)
- [`code/fcn.140173389.c`](code/fcn.140173389.c)
- [`code/fcn.140191660.c`](code/fcn.140191660.c)
- [`code/fcn.140192bcf.c`](code/fcn.140192bcf.c)
- [`code/fcn.1401cabec.c`](code/fcn.1401cabec.c)
- [`code/fcn.140232d4e.c`](code/fcn.140232d4e.c)
- [`code/fcn.140250f16.c`](code/fcn.140250f16.c)
- [`code/fcn.140571d2f.c`](code/fcn.140571d2f.c)
- [`code/fcn.1405739c4.c`](code/fcn.1405739c4.c)
- [`code/fcn.1405815d7.c`](code/fcn.1405815d7.c)
- [`code/fcn.140616cc9.c`](code/fcn.140616cc9.c)

## Behavioral Analysis

This analysis has been updated to incorporate the technical details from the final chunk of disassembly. The addition of this data confirms that the packer employs a **multi-layered, polymorphic execution environment** where even the "handler" functions are heavily obfuscated through recursive complexity and intentional decompiler sabotage.

### Updated Analysis: [Project Name/Samuel ID] - Technical Analysis (Chunk 5)

#### Core Functionality and Purpose
The final chunk provides a granular look at the **Micro-Execution Layer**. It reveals that the VM is not just a single dispatcher but a nested system where complex operations are subdivided into numerous internal "micro-instructions."

*   **Recursive Complexity & Nested Dispatch:** The transitions between cases (e.g., `0xde` through `0xff`) reveal logic that handles complex data processing—such as sorting algorithms, bitwise transformations, and range checks—within the VM's scope. This suggests that what might be a single x86 instruction is "expanded" into a series of sophisticated VM operations to hide its true intent (e.g., string manipulation or memory copying).
*   **Sophisticated Data-Type Handling:** The repetitive use of constants like `0x110000` and various bitmasks indicates that the VM is performing **internal type checking**. It determines the "type" of an operand at runtime before deciding which sub-routine to invoke, effectively creating a private, typed environment for the payload.
*   **Internal State Mutation:** The interaction between `puVar29`, `puVar31`, and the various stack offsets suggests that the VM maintains a massive internal state structure. Every "instruction" execution modifies not just a register-equivalent value, but potentially multiple fields in a complex data structure used to track the payload's progress.

#### Suspicious or Malicious Behaviors
The final chunk reinforces the presence of highly advanced anti-analysis techniques:

*   **Advanced Control Flow Flattening (CFF) & Jump Table Mangling:** The "UNRECOVERED_JUMPTABLE" warnings are pervasive. By forcing the decompiler to treat these as indirect calls, the author ensures that no automated tool can generate a clean functional graph. This is a deliberate tactic to hide the "logic flow" of the packer from static analysis tools.
*   **Execution Path Obfuscation:** Cases like `0xde` and `0xf4` include loops and conditional logic that appear highly complex but may boil down to simple operations at runtime. This **Instruction Bloat** is designed to exhaust an analyst's time, forcing them to manually trace hundreds of instructions just to understand a single branch.
*   **Deterministic "Landmines":** The continued appearance of `halt_baddata()` in cases like `0xdb`, `0xdc`, and `0xfd` confirms the existence of "dead-end" paths. These are designed to be hit only by automated tracers or imperfect decompilers, causing the analysis tool to crash or produce a "broken" result while the real path remains hidden.
*   **Dynamic Handler Resolution:** The code shows calls to various `fcn` handles (e.g., `fcn.14023dd79`, `fcn.14023a3cd`). These are not standard API calls but internal "micro-handlers." This means the packer's core logic is segmented into a library of functions, making it difficult to identify the "main" malicious routine even after jumping through the VM.

#### Notable Techniques & Patterns
*   **Complex Comparison Logic:** The usage of `SORT` or `SEARCH` patterns (seen in the loops following `0xde`) suggests the packer may be performing **Dynamic API Resolution**. Instead of calling a known DLL function, it likely searches for an address at runtime and resolves it through its own internal "lookup" logic.
*   **Memory Overlay Logic:** The frequent calculation of stack offsets and local variable addresses (e.g., `0x145d6ecf8`) suggests that the packer is building a complex "shadow memory" space for the payload to execute in, isolated from standard system calls.

### Summary for Incident Report (Final Update)
The sample is a **highly advanced, multi-tiered Virtual Machine (VM)-based packer** capable of high-level obfuscation and anti-analysis evasion.

1.  **Architecture:** The core logic resides within a custom VM with an "executive" layer that handles complex state transitions via a massive instruction map. It employs nested handlers to break down actions into small, discrete units, making it extremely difficult to reconstruct the original code's intent through static analysis.
2.  **Advanced Obfuscation:** The packer utilizes **Control Flow Flattening (CFF)**, **Instruction Virtualization**, and **Deep Instruction Bloat**. It purposefully breaks decompiler logic by utilizing indirect jumps and complex bitwise math to hide logical branches.
3.  **Anti-Analysis Infrastructure:** The presence of "landmines" (`halt_baddata`) and the deliberate destruction of jump tables indicates a professional-grade tool designed to foil both automated scanners and manual human analysis.
4.  **Threat Assessment:** This is a high-sophistication, likely **custom-built packer or a highly customized commercial protector (e.g., modified VMProtect/Themida)**. Its complexity suggests use in advanced persistent threat (APT) scenarios where the goal is to delay discovery and complicate reverse engineering of the underlying malware payload.

**Recommendation:**
Static analysis has reached its point of diminishing returns due to the sophisticated VM architecture and intentional decompiler sabotage. **Dynamic Analysis with memory dumping at the "tail" of the execution is required.** The analyst should monitor for a significant change in memory entropy or the creation of new executable memory segments, which would indicate the moment the VM extracts/decodes the primary payload into its final, runnable form.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1026.003 | Packer | The analysis confirms a multi-layered, polymorphic packer used to hide the primary payload and obfuscate handler functions. |
| T1497 | Virtualization | The use of a custom "Micro-Execution Layer" and nested dispatch logic transforms x86 instructions into a private, complex instruction set to hide intent. |
| T1026 | Packaged/Obfuscated Code | Techniques such as Control Flow Flattening (CFF), Instruction Bloat, and Jump Table Mangling are used to exhaust analyst time and break decompiler tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The input data describes a **highly sophisticated VM-based packer**. Most of the raw strings provided are obfuscated code fragments or "junk" data used by the packer to frustrate static analysis; therefore, they do not constitute actionable network or file system IOCs.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: `.rdata`, `.data`, and `.pdata` were excluded as standard PE section headers).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Function Handles (Memory Offsets):** 
    *   `fcn.14023dd79`
    *   `fcn.14023a3cd`
    *(Note: These represent specific internal micro-handler offsets within the packer's memory space.)*
*   **Anti-Analysis Signatures:** 
    *   `halt_baddata()` 
    *(Note: Identified as a "landmine" function used to crash debuggers or decompilers during analysis.)*
*   **Behavioral Patterns:**
    *   **Technique:** Control Flow Flattening (CFF)
    *   **Technique:** Instruction Virtualization / VM-based packing
    *   **Technique:** Dynamic API Resolution (via internal `SORT`/`SEARCH` logic)
    *   **Mechanism:** Use of "Instruction Bloat" and "Data-Type Handling" to hide payload intent.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium

**Key evidence**:
*   **Advanced VM-based Packing:** The analysis confirms the sample utilizes a "Micro-Execution Layer," where standard x86 instructions are translated into a private, complex instruction set. This is a hallmark of high-end custom packers or heavily modified commercial protectors (like VMProtect/Themida).
*   **Intentional Decompiler Sabotage:** The use of Control Flow Flattening (CFF), "Instruction Bloat," and Jump Table Mangling are specific techniques designed to exhaust human analysts and break automated static analysis tools. 
*   **Anti-Analysis "Landmines":** The presence of `halt_baddata()` functions specifically designed to crash debuggers or decompilers indicates a high level of sophistication, typically associated with advanced persistent threats (APTs) or professional-grade malware distributors.

**Note:** Because the primary payload is still encapsulated within the virtual machine's "shadow memory," its final role (e.g., RAT, Ransomware, etc.) cannot be determined until the packer is fully stripped and the underlying code is dumped from memory.
