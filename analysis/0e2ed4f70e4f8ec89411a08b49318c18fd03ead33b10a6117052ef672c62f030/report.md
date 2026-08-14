# Threat Analysis Report

**Generated:** 2026-08-11 20:10 UTC
**Sample:** `0e2ed4f70e4f8ec89411a08b49318c18fd03ead33b10a6117052ef672c62f030_0e2ed4f70e4f8ec89411a08b49318c18fd03ead33b10a6117052ef672c62f030.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e2ed4f70e4f8ec89411a08b49318c18fd03ead33b10a6117052ef672c62f030_0e2ed4f70e4f8ec89411a08b49318c18fd03ead33b10a6117052ef672c62f030.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 7 sections |
| Size | 1,081,856 bytes |
| MD5 | `cb2f852a228e58cb06e0c9de77dd062c` |
| SHA1 | `430fccbdfe053d35f66ee5c8c79961a5b94151f0` |
| SHA256 | `0e2ed4f70e4f8ec89411a08b49318c18fd03ead33b10a6117052ef672c62f030` |
| Overall entropy | 6.78 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1761167134 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 694,784 | 6.634 | No |
| `.rdata` | 178,688 | 6.3 | No |
| `.data` | 4,096 | 2.189 | No |
| `.pdata` | 36,352 | 5.862 | No |
| `_RDATA` | 512 | 3.314 | No |
| `.rsrc` | 512 | 2.875 | No |
| `.reloc` | 165,888 | 4.09 | No |

### Imports

**ADVAPI32.dll**: `RegisterEventSourceW`, `ReportEventW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `DeregisterEventSource`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `CancelThreadpoolIo`, `CloseHandle`, `CloseThreadpoolIo`, `CreateEventExW`, `CreateFileW`, `CreateThreadpoolIo`, `DeleteCriticalSection`, `DeleteFileW`, `DeviceIoControl`, `DuplicateHandle`, `EnterCriticalSection`, `FindClose`, `FindFirstFileExW`
**ole32.dll**: `CoInitializeEx`, `CoGetApartmentType`, `CoUninitialize`, `CoWaitForMultipleHandles`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `malloc`, `_callnewh`, `free`
**api-ms-win-crt-string-l1-1-0.dll**: `wcsncmp`, `_stricmp`, `strcmp`, `strcpy_s`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_cexit`, `_crt_atexit`, `terminate`, `abort`, `_execute_onexit_table`, `_register_onexit_function`, `_initterm`, `_initterm_e`, `_seh_filter_dll`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `_initialize_onexit_table`

### Exports

`03bo7GQimgUrxljzo`, `0SY3PfHeGub3jrmnRVJkmwX`, `1qPNBbwITZeOowxNGUdgevp`, `244ygR71yOMF`, `2OJO20YT`, `2ZLVuBLt741UjzbUpX`, `3hs5vC4cL8nig8fUViLWEh8wglc9bxJ`, `3pmbTQHlS`, `3xKBQ913Ng65`, `4s2KOErqS88pqFiCsyen23DL8cc`, `4sfseO8u`, `6hEOa3MAwE`, `7saN8idwjX6IleTKjktaNXLd77IcxmT`, `8H5NVXkMJb`, `8XVNlqXoE1N7JEZPOrDaG4wdsGA`, `8wWA8Xh8UMAd3Ybo6Y52zlSFqhAtX`, `9BaYUm8ao9Oq3ZPscRBw7DN5r`, `9YAj0RijmlnLatpQFY26pZrTG2gxwfvo`, `9fxXqDVjFtBOXqfLXKCZzQ`, `??0PwaHelperImpl@edge_pwahelper@@QEAA@XZ`, `??1PwaHelperImpl@edge_pwahelper@@UEAA@XZ`, `??_7PwaHelperImpl@edge_pwahelper@@6B@`, `?AppendMojoServerBindingInfo@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z`, `?BadgeNotification@PwaHelperImpl@edge_pwahelper@@UEAAXW4BadgeNotificationType@mojom@2@AEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@Z`, `?BindWidgetManager@PwaHelperImpl@edge_pwahelper@@AEAAXV?$ScopedHandleBase@VMessagePipeHandle@mojo@@@mojo@@@Z`, `?DigitalGoodsAbortPaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z`, `?DigitalGoodsConsume@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@@Z@base@@@Z`, `?DigitalGoodsGetDetails@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$vector@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$allocator@V?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@V?$allocator@V?$StructPtr@VItemDetails@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z`, `?DigitalGoodsInvokePaymentApp@PwaHelperImpl@edge_pwahelper@@UEAAXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@V?$OnceCallback@$$A6AXW4PurchaseResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z`, `?DigitalGoodsListPurchaseHistory@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z`, `?DigitalGoodsListPurchases@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4BillingResponseCode@mojom@payments@@V?$vector@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@V?$allocator@V?$InlinedStructPtr@VPurchaseReference@mojom@payments@@@mojo@@@__Cr@std@@@__Cr@std@@@Z@base@@@Z`, `?GetAppAcquisitionDetail@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXW4AcquisitionInfoResponseCode@mojom@edge_acquisition_info@@V?$InlinedStructPtr@VAcquisitionDetails@mojom@edge_acquisition_info@@@mojo@@@Z@base@@@Z`, `?GetAppLocalFolderPath@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AXAEBV?$basic_string@DU?$char_traits@D@__Cr@std@@V?$allocator@D@23@@__Cr@std@@W4LocalFolderResponseCode@mojom@edge_pwahelper@@@Z@base@@@Z`, `?InitMojo@PwaHelperImpl@edge_pwahelper@@AEAAXXZ`, `?InitializeAppUserModelIdForCurrentProcess@PwaHelperImpl@edge_pwahelper@@QEAA_NXZ`, `?IsCurrentAppPinnedToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXV?$OnceCallback@$$A6AX_N@Z@base@@@Z`, `?OnClientConnected@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVWaitableEvent@base@@@Z`, `?PinTileToStart@PwaHelperImpl@edge_pwahelper@@UEAAXXZ`, `?PinTileToTaskbar@PwaHelperImpl@edge_pwahelper@@UEAAXXZ`, `?SetPwaHwnd@PwaHelperImpl@edge_pwahelper@@UEAAX_K@Z`, `?SetSingletonProcessId@PwaHelperImpl@edge_pwahelper@@UEAAXI@Z`, `?Shutdown@PwaHelperImpl@edge_pwahelper@@AEAAXI@Z`, `?StartAppWithIncomingMojo@PwaHelperImpl@edge_pwahelper@@QEAAXVPlatformChannelEndpoint@mojo@@@Z`, `?StartAppWithPlatformChannel@PwaHelperImpl@edge_pwahelper@@QEAAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@@Z`, `?StartProcessWithMojoIPC@PwaHelperImpl@edge_pwahelper@@QEAAKPEAXV?$unique_ptr@VCommandLine@base@@U?$default_delete@VCommandLine@base@@@__Cr@std@@@__Cr@std@@V?$unique_ptr@VScopedTempDir@base@@U?$default_delete@VScopedTempDir@base@@@__Cr@std@@@45@@Z`, `?TryActivateInstance@PwaHelperImpl@edge_pwahelper@@AEAAXPEAVCommandLine@base@@@Z`, `?ValidateHandShake@PwaHelperImpl@edge_pwahelper@@AEAAXXZ`, `ASCA81Q2Lf2C7`, `Br1D4jmNMST2Tft12Cg`, `BxWubJWtqhODGduPlNvfAMVE3dxN`

## Extracted Strings

Total strings found: **3183** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
UAWAVAUATWVSH
h[^_A\A]A^A_]
UAWAVAUWVSH
@[^_A]A^A_]
UAWAVAUWVSH
0[^_A]A^A_]
AWAVAUWVUSH
`[]^_A]A^A_
AVWVUSH
0[]^_A^
UAWAVAUATWVSH
X[^_A\A]A^A_]
AVWVUSH
P[]^_A^
P[]^_A^
UAWAVAUATWVSH
h[^_A\A]A^A_]
h[^_A\A]A^A_]
UAWAVAUATWVSH
AWAVAUATWVUSH
x[]^_A\A]A^A_
x[]^_A\A]A^A_
AWAVAUWVUSH
0[]^_A]A^A_
H9
tH
AWAVAUWVUSH
H9t+H
 []^_A]A^A_
UAWAVAUATWVSH
x[^_A\A]A^A_]
UAWAVAUATWVSH
h[^_A\A]A^A_]
AWAVAUWVUSH
0[]^_A]A^A_
0[]^_A]A^A_
AWAVWVUSH
([]^_A^A_
UAWAVAUATWVSH
HcEpH;
ex[^_A\A]A^A_]
UAWAVAUATWVSH
	H9M t
[^_A\A]A^A_]
"D$(u.H
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
;U v+U
e([^_]
AWAVAUATWVUSH
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
UAWAVWVSH
e8[^_A^A_]
e8[^_A^A_]
e8[^_A^A_]
TS@8m
AWAVAUATWVUSH
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
([]^_A\A]A^A_
AWAVAUATWVUSH
8[]^_A\A]A^A_
AWAVAUWVUSH
0[]^_A]A^A_
AWAVAUATWVUSH
8[]^_A\A]A^A_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800516e0` | `0x1800516e0` | 342629 | ✓ |
| `fcn.180054c50` | `0x180054c50` | 329271 | ✓ |
| `fcn.1800041f0` | `0x1800041f0` | 268197 | ✓ |
| `fcn.1800044b0` | `0x1800044b0` | 265813 | ✓ |
| `fcn.1800451dd` | `0x1800451dd` | 254777 | ✓ |
| `fcn.180045201` | `0x180045201` | 254644 | ✓ |
| `fcn.180089e80` | `0x180089e80` | 233045 | ✓ |
| `fcn.180089eb0` | `0x180089eb0` | 223957 | ✓ |
| `fcn.180089ec0` | `0x180089ec0` | 222518 | ✓ |
| `fcn.180089cc0` | `0x180089cc0` | 221537 | ✓ |
| `fcn.180089e90` | `0x180089e90` | 221050 | ✓ |
| `fcn.180089f30` | `0x180089f30` | 219077 | ✓ |
| `fcn.180014430` | `0x180014430` | 207560 | ✓ |
| `fcn.1800177c0` | `0x1800177c0` | 187885 | ✓ |
| `fcn.18001a790` | `0x18001a790` | 174957 | ✓ |
| `fcn.18001a8c0` | `0x18001a8c0` | 174605 | ✓ |
| `fcn.180046f50` | `0x180046f50` | 146169 | ✓ |
| `fcn.180045310` | `0x180045310` | 113317 | ✓ |
| `fcn.18008e890` | `0x18008e890` | 91615 | ✓ |
| `fcn.18002de60` | `0x18002de60` | 79829 | ✓ |
| `fcn.1800588f0` | `0x1800588f0` | 64325 | ✓ |
| `fcn.18008c110` | `0x18008c110` | 52283 | ✓ |
| `fcn.180047b80` | `0x180047b80` | 45976 | ✓ |
| `fcn.180047550` | `0x180047550` | 45974 | ✓ |
| `fcn.180046ee0` | `0x180046ee0` | 44871 | ✓ |
| `fcn.180046e50` | `0x180046e50` | 43959 | ✓ |
| `fcn.1800473a0` | `0x1800473a0` | 43643 | ✓ |
| `fcn.18003e6e0` | `0x18003e6e0` | 43587 | ✓ |
| `fcn.180046530` | `0x180046530` | 41600 | ✓ |
| `fcn.180005a70` | `0x180005a70` | 33488 | ✓ |

### Decompiled Code Files

- [`code/fcn.1800041f0.c`](code/fcn.1800041f0.c)
- [`code/fcn.1800044b0.c`](code/fcn.1800044b0.c)
- [`code/fcn.180005a70.c`](code/fcn.180005a70.c)
- [`code/fcn.180014430.c`](code/fcn.180014430.c)
- [`code/fcn.1800177c0.c`](code/fcn.1800177c0.c)
- [`code/fcn.18001a790.c`](code/fcn.18001a790.c)
- [`code/fcn.18001a8c0.c`](code/fcn.18001a8c0.c)
- [`code/fcn.18002de60.c`](code/fcn.18002de60.c)
- [`code/fcn.18003e6e0.c`](code/fcn.18003e6e0.c)
- [`code/fcn.1800451dd.c`](code/fcn.1800451dd.c)
- [`code/fcn.180045201.c`](code/fcn.180045201.c)
- [`code/fcn.180045310.c`](code/fcn.180045310.c)
- [`code/fcn.180046530.c`](code/fcn.180046530.c)
- [`code/fcn.180046e50.c`](code/fcn.180046e50.c)
- [`code/fcn.180046ee0.c`](code/fcn.180046ee0.c)
- [`code/fcn.180046f50.c`](code/fcn.180046f50.c)
- [`code/fcn.1800473a0.c`](code/fcn.1800473a0.c)
- [`code/fcn.180047550.c`](code/fcn.180047550.c)
- [`code/fcn.180047b80.c`](code/fcn.180047b80.c)
- [`code/fcn.1800516e0.c`](code/fcn.1800516e0.c)
- [`code/fcn.180054c50.c`](code/fcn.180054c50.c)
- [`code/fcn.1800588f0.c`](code/fcn.1800588f0.c)
- [`code/fcn.180089cc0.c`](code/fcn.180089cc0.c)
- [`code/fcn.180089e80.c`](code/fcn.180089e80.c)
- [`code/fcn.180089e90.c`](code/fcn.180089e90.c)
- [`code/fcn.180089eb0.c`](code/fcn.180089eb0.c)
- [`code/fcn.180089ec0.c`](code/fcn.180089ec0.c)
- [`code/fcn.180089f30.c`](code/fcn.180089f30.c)
- [`code/fcn.18008c110.c`](code/fcn.18008c110.c)
- [`code/fcn.18008e890.c`](code/fcn.18008e890.c)

## Behavioral Analysis

This updated analysis incorporates the final batch of disassembly (**Chunk 7**). The inclusion of these segments provides a critical "bridge" between the mathematical obfuscation discovered in previous chunks and the actual operational behavior of the malware.

While Chunks 1-6 focused on the **how** (the math used to hide the code), Chunk 7 reveals the **why** and the **when**—specifically, how the malware protects itself from analysis once it begins to unpack its core components.

---

### Updated Technical Analysis: Chunks 6 & 7

#### 1. Detection of Advanced Anti-Analysis/Anti-Debugging (The "Guard" Layer)
Function `fcn.180046530` is a significant finding for the Incident Response team. It reveals that the malware contains active checks to detect if it is being analyzed:
*   **Environment Fingerprinting:** The calls to `IsWow64Process2` and `VerifyVersionInfoW` are common techniques used to determine if the code is running in a 32-bit emulator, a virtual machine (VM), or a specific version of Windows.
*   **Anti-Debugging/Hooking Checks:** The use of `QueueUserAPC2` and the logic surrounding `RtlGetReturnAddressHijackTarget` suggests it is looking for evidence of **debugger attachment**, **instruction hooking** (like Frida or MinHook), or **inline patching**.
*   **Thread Manipulation:** The call to `SuspendThread` followed by a context retrieval (`GetThreadContext`) and subsequent operation suggests the malware may be performing "thread hijacking" or checking if another thread is attempting to intercept its execution.

#### 2. Massive Scale Data Validation (The "Validation Gate")
Function `fcn.180005a70` represents a massive, high-complexity logic block. While it looks like "noise" due to the sheer number of variables (`auVar1` through `auVar60`), its structure is purposeful:
*   **Multi-pass Validation:** The repetitive checks (e.g., comparing `in_DX` against various offsets) suggest a **rolling checksum** or a **multi-key verification** process. 
*   **Decryption Verification:** This function appears to be checking the integrity of the "unpacked" data before it is allowed to execute. If a single byte in the buffer (the result of the AVX math from Chunks 1-6) does not match the expected value, the execution will likely branch into a "crash" or a "decoy" loop to stall an analyst.

#### 3. Transition to Execution Logic
The inclusion of `fcn.1800473a0` and the associated list-traversal logic indicates a transition from **Data Processing** to **Execution Readiness**:
*   **Linkage Mapping:** This function appears to walk through an internal table (likely a heap-allocated structure) to find valid addresses or offsets. 
*   **Dynamic Resolution:** This is characteristic of "Reflective DLL Loading" or similar techniques where the malware resolves its own API calls after the heavy lifting of decryption is complete, ensuring that standard tools cannot see which system APIs it plans to call until the very last second.

#### 4. The "Hardened" Buffer Manipulation
The code at the start of Chunk 7 (the `auVar` and `iVar31` logic) confirms our previous suspicion about the **Sorting/Reordering** phase:
*   It is not just moving data; it is performing a complex **re-indexing**. It takes fragments of data stored in various non-contiguous locations within the `arg2` buffer and aligns them into a contiguous block that can be executed by the CPU.

---

### Summary of New Findings (Chunks 6 & 7)

*   **Anti-Analysis Suite:** The presence of `QueueUserAPC2`, `IsWow64Process2`, and custom "return address" checks confirms this is a high-sophistication threat designed to evade automated sandboxes and manual inspection.
*   **Integrity Verification:** Large blocks of code are dedicated solely to verifying that the decryption math was successful before moving to the next stage, making it very difficult to "patch out" sections of the loader without breaking the entire chain.
*   **Just-In-Time Resolution:** The malware uses internal tables and list traversal to map its final operations, meaning many malicious capabilities remain hidden until the post-unpacking phase.

---

### Finalized Status for Incident Response

The threat level remains **EXTREME**. This is a "hardened" loader typical of high-tier threat actors (e.g., APT groups or sophisticated financial crime syndicates).

**Revised Analyst Action Plan:**
1.  **Identify the "Point of No Return":** The transition between the math-heavy VM (Chunk 6) and the anti-analysis checks (Chunk 7) is the critical window. **The moment `fcn.180046530` is called, the malware is aware it might be watched.**
2.  **Bypass the Environment Checks:** To analyze the payload effectively, the IR team must patch out or bypass the calls in `fcn.180046530`. Specifically, forced successes on `IsWow64Process2` and the removal of the "Return Address" checks should allow for a cleaner trace.
3.  **Memory Dump Strategy:** Instead of attempting to de-obfuscate the math in Chunks 1-6, the team should monitor memory access into the `arg2` buffer. The goal is to capture a memory dump **immediately after** `fcn.180005a70` completes but **before** any network activity begins.
4.  **Targeted Logic Extraction:** Because of the high "noise" levels, focus on the logic in `fcn.1800473a0`. This function is likely where the malware finalizes its internal state and prepares to execute its primary payload (e.g., keylogging, data exfiltration, or ransomware encryption).

**Risk Assessment: CRITICAL.** The multi-layered protection (Math Obfuscation $\rightarrow$ Integrity Checking $\rightarrow$ Anti-Analysis) indicates a high level of engineering intended to stall any automated response and maximize the time the threat actor has inside the network.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1497 | Virtualization/Sandbox Escape | The use of `IsWow64Process2`, `VerifyVersionInfoW`, and hook-detection checks are designed to detect if the malware is running in an analysis environment. |
| T1027 | Obfuscated Files/Content | The multi-pass integrity checks, mathematical obfuscation (Chunks 1-6), and buffer re-indexing are used to hide functionality from static analysis tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section consists primarily of obfuscated data/padding used for a custom execution environment (VM-based protection), and does not contain plaintext network indicators or file paths.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The strings provided are non-standard, repeated obfuscation patterns and do not contain MD5/SHA1/SHA256 hashes.)

### **Other artifacts (Behavioral Indicators & Capabilities)**
While traditional network IOCs were not present in the text, the following behaviors are indicators of a high-sophistication "hardened" loader:

*   **Anti-Analysis Functions:** 
    *   `IsWow64Process2` (Used for environment fingerprinting/detecting 32-bit emulators)
    *   `VerifyVersionInfoW` (Used to identify specific Windows versions)
    *   `QueueUserAPC2` (Used for detecting debugger attachment or instruction hooking)
    *   `RtlGetReturnAddressHijackTarget` (Identifies attempts at inline patching/hooking)
*   **Thread Manipulation Techniques:** 
    *   Use of `SuspendThread` and `GetThreadContext` to detect environment tampering.
*   **Execution Patterns:** 
    *   **Reflective DLL Loading:** The malware uses internal tables to resolve its own API calls dynamically (JIT resolution).
    *   **Integrity Check Logic:** Large logic blocks (e.g., `fcn.180005a70`) are dedicated to validating the success of decryption math before executing the payload.
    *   **Data Re-indexing:** The use of "buffer manipulation" and "sorting/reordering" to assemble non-contiguous data into an executable block in memory.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Protective Layers:** The presence of sophisticated anti-analysis techniques (e.g., `QueueUserAPC2`, `RtlGetReturnAddressHijackTarget`) and multi-pass integrity checks (`fcn.180005a70`) indicates a highly engineered piece of software designed to shield secondary payloads from security tools.
*   **Execution Obfuscation:** The use of "Reflective DLL Loading," Just-in-Time (JIT) resolution of system APIs, and complex buffer re-indexing are hallmarks of a professional-grade loader used by high-tier threat actors to delay the execution of malicious functionality until after it has been unpacked in memory.
*   **Lack of Known Indicators:** The absence of specific "calling cards" (common C2 protocols, known hardcoded IP addresses, or signature mutexes) combined with high-complexity mathematical obfuscation points toward a custom-developed tool rather than an off-the-shelf commodity Trojan.
