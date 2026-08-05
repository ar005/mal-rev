# Threat Analysis Report

**Generated:** 2026-08-04 22:04 UTC
**Sample:** `0d2d887adcdf6309c4532e75ddb508db33402c7a488c3e2b8943c6721dab6708_0d2d887adcdf6309c4532e75ddb508db33402c7a488c3e2b8943c6721dab6708.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d2d887adcdf6309c4532e75ddb508db33402c7a488c3e2b8943c6721dab6708_0d2d887adcdf6309c4532e75ddb508db33402c7a488c3e2b8943c6721dab6708.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 1,410,560 bytes |
| MD5 | `82f08a330f0ed7e3178fbf81eeaa18b5` |
| SHA1 | `abb66ca320e068183f80e19a3f814330441e5fa9` |
| SHA256 | `0d2d887adcdf6309c4532e75ddb508db33402c7a488c3e2b8943c6721dab6708` |
| Overall entropy | 7.021 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1761490030 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 695,808 | 6.513 | No |
| `.rdata` | 592,384 | 7.433 | ⚠️ Yes |
| `.data` | 71,168 | 3.242 | No |
| `.pdata` | 39,936 | 5.927 | No |
| `.rsrc` | 2,560 | 3.848 | No |
| `.reloc` | 7,680 | 5.425 | No |

### Imports

**ADVAPI32.dll**: `DeregisterEventSource`, `RegCloseKey`, `RegCreateKeyExW`, `RegSetValueExW`, `RegisterEventSourceW`, `ReportEventW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptGenRandom`
**CRYPT32.dll**: `CryptUnprotectData`, `CryptProtectData`
**KERNEL32.dll**: `EncodePointer`, `InitializeCriticalSectionEx`, `CloseHandle`, `CompareStringEx`, `CompareStringOrdinal`, `CopyFileW`, `CreateDirectoryW`, `CreateEventExW`, `DuplicateHandle`, `FileTimeToSystemTime`, `FindClose`, `FindFirstFileW`, `FindNLSStringEx`, `FindNextFileW`, `FindStringOrdinal`
**ole32.dll**: `CoInitializeEx`, `CoUninitialize`, `CoGetApartmentType`, `CoCreateGuid`, `CoWaitForMultipleHandles`
**api-ms-win-crt-heap-l1-1-0.dll**: `_callnewh`, `malloc`, `free`, `calloc`
**api-ms-win-crt-math-l1-1-0.dll**: `log`
**api-ms-win-crt-string-l1-1-0.dll**: `strcpy`, `strcmp`, `_stricmp`, `strlen`, `strcpy_s`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__stdio_common_vsnprintf_s`, `__acrt_iob_func`, `__stdio_common_vsscanf`, `__stdio_common_vsprintf_s`, `__stdio_common_vfprintf`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_initterm_e`, `_seh_filter_dll`, `abort`, `_initterm`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `_cexit`, `_execute_onexit_table`, `_initialize_onexit_table`, `_register_onexit_function`, `terminate`, `_crt_atexit`

### Exports

`1UgrYjaXSTp22`, `4QL7jjUXQ8taeJBm4Uz1BsUgkB`, `4ygiyMJs`, `5YHrLB9ELQMpZ9qKfzPAffk`, `5nwiuZxGrOjzOOFfF2`, `6CsP79PdbRqT`, `6LuhC4tMPI3BLO`, `6ce4yW3gtynv5iCZ`, `7p9AXT6gmeTRpmhSs5u7OL0y`, `8DhHMFAUFUeVzA7iEKyU`, `8lvTHjdjyJCjdM4M`, `??0PwaHelperImpl@edge_pwahelper@@QEAA@XZ`, `??1PwaHelperImpl@edge_pwahelper@@UEAA@XZ`, `??_7PwaHelperImpl@edge_pwahelper@@6B@`, `?AppendMojoServerBindingInfo@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z`, `?BadgeNotification@PwaHelperImpl@edge_pwahelper@@UEAAXW4BadgeNotificationType@mojom@2@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z`, `?BindWidgetManager@PwaHelperImpl@edge_pwahelper@@AEAAXV?$ScopedHandleBase@VMessagePipeHandle@mojo@@@mojo@@@Z`, `?DigitalGoodsAbortPaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z`, `?DigitalGoodsConsume@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@@Z@base@@@Z`, `?DigitalGoodsGetDetails@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$vector@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@V?$allocator@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z`, `?DigitalGoodsInvokePaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4PurchaseResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z`, `?DigitalGoodsListPurchaseHistory@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z`, `?DigitalGoodsListPurchases@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z`, `?GetAppAcquisitionDetail@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4AcquisitionInfoResponseCode@mojom@edge_acquisition_info@@V?$InlinedStructPtr@VAcquisitionDetails@mojom@edge_acquisition_info@@@mojo@@@Z@base@@@Z`, `?GetAppLocalFolderPath@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4LocalFolderResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z`, `?InitMojo@PwaHelperImpl@edge_pwahelper@@AEAAXXZ`, `?InitializeAppUserModelIdForCurrentProcess@PwaHelperImpl@edge_pwahelper@@QEAA_NXZ`, `?IsCurrentAppPinnedToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z`, `?OnClientConnected@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVWaitableEvent@base@@@Z`, `?PinTileToStart@PwaHelperImpl@edge_pwahelper@@UEAAXXZ`, `?PinTileToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXXZ`, `?SetPwaHwnd@PwaHelperImpl@edge_pwahelper@@UEAAX_K@Z`, `?SetSingletonProcessId@PwaHelperImpl@edge_pwahelper@@UEAAXI@Z`, `?Shutdown@PwaHelperImpl@edge_pwahelper@@AEAAXI@Z`, `?StartAppWithIncomingMojo@PwaHelperImpl@edge_pwahelper@@QEAAXVPlatformChannelEndpoint@mojo@@@Z`, `?StartAppWithPlatformChannel@PwaHelperImpl@edge_pwahelper@@QEAAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@@Z`, `?StartProcessWithMojoIPC@PwaHelperImpl@edge_pwahelper@@QEAAKPEAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@V?$unique_ptr@VScopedTempDir@base@@U?$default_delete@VScopedTempDir@base@@@__Cr@std@@@45@@Z`, `?TryActivateInstance@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z`, `?ValidateHandShake@PwaHelperImpl@edge_pwahelper@@AEAAXXZ`, `BAq7j3tTmRlg8f7Nf0oDXs0u`, `BJ2sD1vx1kw85z1mJZ9upjyXxr`, `CboESWXcruqRu2fP7jGBlhhRtr`, `ClearReportsBetween_ExportThunk`, `CrashForException_ExportThunk`, `DR5P7qAm4thFgIdEkBjcEYE2M`, `DYUyk4hqiw5`, `DisableHook`, `DrainLog`, `DumpHungProcessWithPtype_ExportThunk`, `DumpProcessWithoutCrash`

## Extracted Strings

Total strings found: **5081** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
h[^_A\A]A^A_]
AWAVAUATWVUSH
x[]^_A\A]A^A_
x[]^_A\A]A^A_
AWAVAUWVUSH
0[]^_A]A^A_
H9
tH
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUATWVSH
v+U`H
ex[^_A\A]A^A_]
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUATWVSH
e([^_A\A]A^A_]
Ff;Ct
3
UAWAVAUATWVSH
[^_A\A]A^A_]
AVWVUSH
0[]^_A^
0[]^_A^
AWAVWVUSH
([]^_A^A_
([]^_A^A_
([]^_A^A_
([]^_A^A_
AWAVAUATWVUSH
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
AWAVAUATWVUSH
([]^_A\A]A^A_
([]^_A\A]A^A_
AWAVAUATWVUSH
8[]^_A\A]A^A_
8[]^_A\A]A^A_
AWAVAUATWVUSH
H[]^_A\A]A^A_
H[]^_A\A]A^A_
;U v+U
e([^_]
TS@8m
AVWVUSH
0[]^_A^
AVWVUSH
0[]^_A^
0[]^_A^
AWAVWVUSH
8[]^_A^A_
8[]^_A^A_
AWAVAUATWVUSH
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
AWAVAUATWVUSH
([]^_A\A]A^A_
AWAVAUATWVUSH
([]^_A\A]A^A_
AWAVWVUSH
([]^_A^A_
AWAVAUATWVUSH
8[]^_A\A]A^A_
AWAVWVUSH
8[]^_A^A_
UAWAVAUATWVSH
[^_A\A]A^A_]
UAWAVAUWVSH
0[^_A]A^A_]
AWAVWVUSH
8[]^_A^A_
UAWAVWVSH
X[^_A^A_]
UAWAVAUATWVSH
H[^_A\A]A^A_]
x0t^H
UAWAVWVSH
H[^_A^A_]
AVWVUSH
 []^_A^
UAWAVAUATWVSH
h[^_A\A]A^A_]
AWAVAUWVUSH
SiGw
 []^_A]A^A_
AWAVWVUSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180003310` | `0x180003310` | 345879 | ✓ |
| `fcn.180056ddc` | `0x180056ddc` | 330728 | ✓ |
| `fcn.180064bf0` | `0x180064bf0` | 282566 | ✓ |
| `fcn.180064c40` | `0x180064c40` | 282486 | ✓ |
| `fcn.18001a1c0` | `0x18001a1c0` | 250008 | ✓ |
| `fcn.18001df20` | `0x18001df20` | 233357 | ✓ |
| `fcn.18001e050` | `0x18001e050` | 233013 | ✓ |
| `fcn.18009ba40` | `0x18009ba40` | 229909 | ✓ |
| `fcn.180063f20` | `0x180063f20` | 229189 | ✓ |
| `fcn.18009ba50` | `0x18009ba50` | 223285 | ✓ |
| `fcn.18009ba60` | `0x18009ba60` | 221830 | ✓ |
| `fcn.18009b880` | `0x18009b880` | 220881 | ✓ |
| `fcn.18009bad0` | `0x18009bad0` | 218709 | ✓ |
| `fcn.1800670d0` | `0x1800670d0` | 217415 | ✓ |
| `fcn.1800572b0` | `0x1800572b0` | 206617 | ✓ |
| `fcn.180056dc6` | `0x180056dc6` | 198012 | ✓ |
| `fcn.180056a78` | `0x180056a78` | 197128 | ✓ |
| `fcn.180056eb0` | `0x180056eb0` | 165493 | ✓ |
| `fcn.180030d10` | `0x180030d10` | 77725 | ✓ |
| `fcn.18004f930` | `0x18004f930` | 65875 | ✓ |
| `fcn.18005a710` | `0x18005a710` | 50859 | ✓ |
| `fcn.18005a540` | `0x18005a540` | 50185 | ✓ |
| `fcn.180057190` | `0x180057190` | 48631 | ✓ |
| `fcn.180057220` | `0x180057220` | 45623 | ✓ |
| `fcn.180058460` | `0x180058460` | 39449 | ✓ |
| `fcn.1800593f0` | `0x1800593f0` | 36955 | ✓ |
| `fcn.1800595e0` | `0x1800595e0` | 36806 | ✓ |
| `fcn.18000d3a0` | `0x18000d3a0` | 34437 | ✓ |
| `fcn.180062c10` | `0x180062c10` | 33943 | ✓ |
| `fcn.18005a8d0` | `0x18005a8d0` | 33589 | ✓ |

### Decompiled Code Files

- [`code/fcn.180003310.c`](code/fcn.180003310.c)
- [`code/fcn.18000d3a0.c`](code/fcn.18000d3a0.c)
- [`code/fcn.18001a1c0.c`](code/fcn.18001a1c0.c)
- [`code/fcn.18001df20.c`](code/fcn.18001df20.c)
- [`code/fcn.18001e050.c`](code/fcn.18001e050.c)
- [`code/fcn.180030d10.c`](code/fcn.180030d10.c)
- [`code/fcn.18004f930.c`](code/fcn.18004f930.c)
- [`code/fcn.180056a78.c`](code/fcn.180056a78.c)
- [`code/fcn.180056dc6.c`](code/fcn.180056dc6.c)
- [`code/fcn.180056ddc.c`](code/fcn.180056ddc.c)
- [`code/fcn.180056eb0.c`](code/fcn.180056eb0.c)
- [`code/fcn.180057190.c`](code/fcn.180057190.c)
- [`code/fcn.180057220.c`](code/fcn.180057220.c)
- [`code/fcn.1800572b0.c`](code/fcn.1800572b0.c)
- [`code/fcn.180058460.c`](code/fcn.180058460.c)
- [`code/fcn.1800593f0.c`](code/fcn.1800593f0.c)
- [`code/fcn.1800595e0.c`](code/fcn.1800595e0.c)
- [`code/fcn.18005a540.c`](code/fcn.18005a540.c)
- [`code/fcn.18005a710.c`](code/fcn.18005a710.c)
- [`code/fcn.18005a8d0.c`](code/fcn.18005a8d0.c)
- [`code/fcn.180062c10.c`](code/fcn.180062c10.c)
- [`code/fcn.180063f20.c`](code/fcn.180063f20.c)
- [`code/fcn.180064bf0.c`](code/fcn.180064bf0.c)
- [`code/fcn.180064c40.c`](code/fcn.180064c40.c)
- [`code/fcn.1800670d0.c`](code/fcn.1800670d0.c)
- [`code/fcn.18009b880.c`](code/fcn.18009b880.c)
- [`code/fcn.18009ba40.c`](code/fcn.18009ba40.c)
- [`code/fcn.18009ba50.c`](code/fcn.18009ba50.c)
- [`code/fcn.18009ba60.c`](code/fcn.18009ba60.c)
- [`code/fcn.18009bad0.c`](code/fcn.18009bad0.c)

## Behavioral Analysis

Based on the disassembly provided, here is an analysis of the binary's functionality:

### Core Functionality and Purpose
The code describes a **sophisticated malware loader or packer**. Rather than performing standard application tasks, the code is designed to unpack, manage, and execute a secondary payload. It exhibits characteristics of a "loader" that prepares the system environment for malicious code to run while evading security software.

### Suspicious and Malicious Behaviors
*   **Anti-Analysis/Anti-Debugging:** 
    *   The binary attempts to resolve `RtlGetReturnAddressHijackTarget` from `ntdll.dll`. This is a known technique used to detect if the code is being debugged or instrumented by analysis tools.
    *   It uses `VerifyVersionInfoW` and checks for specific flags (e.g., `IsWow64Process2`). These are common "environment checks" to determine if the code is running in a sandbox or a virtual machine.
*   **Thread Context Manipulation:** 
    *   In `fcn.180058460`, the code calls `SuspendThread` followed by `GetThreadContext`. This specific sequence—suspending a thread, grabbing its register context, and then calling `ResumeThread`—is a classic technique for **process injection** or modifying the execution path of a target thread to jump to malicious code.
*   **Shellcode/Payload Execution:** 
    *   The presence of complex loops in `fcn.18009ba40` and various memory management routines suggests the program is iterating through an internal structure (likely a list of shellcode instructions or unpacked modules) and executing them piece-by-piece.
*   **Manual Memory Management:** 
    *   Functions like `fcn.18005a540` appear to be custom memory allocators. Malware often uses custom allocators to bypass standard Windows heap protections and hide "hidden" memory allocations from security scanners.

### Notable Techniques and Patterns
*   **Obfuscated Strings:** The extracted strings are highly repetitive and non-human-readable (e.g., `UAWAVAUATWVSH`). This indicates that the code uses **string encryption or encoding**, common in high-end malware to hide IP addresses, file paths, and registry keys from static analysis.
*   **Indirect Jumps and Jump Tables:** The frequent warnings about "Could not recover jumptable" and the use of `(**0x1800ab538)` indicate a heavily **obfuscated control flow**. This makes it difficult for automated tools to map out what the code will do next.
*   **Software Interrupts (`swi(3)`):** The frequent usage of `swi(3)` (a "Breakpoint" exception) in the disassembly suggests the code may be using a custom exception handler to redirect execution flow, another common method for bypassing security checks and making static analysis difficult.
*   **Execution Guards:** Functions like `fcn.18001df20` and `fcn.18001e050` appear to perform internal integrity checks or state validations before allowing the execution of subsequent stages.

### Summary Conclusion
This is a **malware loader**. It is designed to hide its true intent behind layers of obfuscation, check for the presence of security analysts/debuggers, and then inject/execute an encrypted payload into memory using advanced thread manipulation techniques.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Detection | The use of `RtlGetReturnAddressHijackTarget` and `VerifyVersionInfoW` are classic methods for identifying if the code is running in a virtualized or analyzed environment. |
| T1055 | Process Injection | The sequence of `SuspendThread`, `GetThreadContext`, and `ResumeThread` indicates an attempt to hijack execution flow or inject code into a target process. |
| T1027 | Software Obfuscation | The use of non-human-readable, repeated strings is a primary indicator of encoding/encryption used to hide strings from static analysis. |
| T1036 | Execution Guard | The heavy use of indirect jumps, jump tables, and `swi(3)` interrupts functions as a mechanism to complicate control flow and bypass security checks. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted intelligence. 

**Note:** Due to the heavy use of packing/encryption techniques identified in the report, many standard indicators (such as IP addresses and file paths) remain obfuscated and were not present in plaintext within the provided data.

### **IP addresses / URLs / Domains**
*   None identified (Strings are currently encrypted/obfuscated).

### **File paths / Registry keys**
*   None identified (The analysis notes that the malware uses a custom loader to hide these values from static analysis).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Anti-Analysis Indicators:** 
    *   `RtlGetReturnAddressHijackTarget` (ntdll.dll): Used to detect debugger/instrumentation.
    *   `VerifyVersionInfoW`: Used for environment checking.
    *   `IsWow64Process2`: Used to identify execution context (x86 vs x64).
*   **Injection Techniques:** 
    *   Thread Context Manipulation: Utilization of `SuspendThread`, `GetThreadContext`, and `ResumeThread`.
*   **Execution Patterns:**
    *   `swi(3)`: Frequent use of software interrupts to redirect execution flow and bypass static analysis.
    *   Indirect Jumps/Jump Tables: Use of specific offsets (e.g., `0x1800ab538`) for obfuscated control flow.
    *   Custom Memory Management: Usage of non-standard memory allocation routines to hide malicious heap allocations.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Anti-Analysis & Evasion:** The sample employs sophisticated techniques such as `RtlGetReturnAddressHijackTarget` and `VerifyVersionInfoW` to detect if it is running in a debugger or sandbox environment.
*   **Injection Techniques:** The use of `SuspendThread`, `GetThreadContext`, and `ResumeThread` are definitive indicators of process injection, used to execute malicious code within the context of another process.
*   **Heavy Obfuscation:** The presence of encrypted strings, complex jump tables, and software interrupts (`swi(3)`) suggests a design intended to bypass static analysis and hide the secondary payload's true functionality.
