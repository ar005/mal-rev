# Threat Analysis Report

**Generated:** 2026-08-16 06:53 UTC
**Sample:** `0f6491a71f06d4468f37e04ca5a09df3487fc03c4a04cc73263720c144cde600_0f6491a71f06d4468f37e04ca5a09df3487fc03c4a04cc73263720c144cde600.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f6491a71f06d4468f37e04ca5a09df3487fc03c4a04cc73263720c144cde600_0f6491a71f06d4468f37e04ca5a09df3487fc03c4a04cc73263720c144cde600.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 7 sections |
| Size | 1,162,240 bytes |
| MD5 | `4cfc3c122758c31df123a1c3b3032ac1` |
| SHA1 | `5f9f7aac1b6a13efb8bd70df70050d422f7d4646` |
| SHA256 | `0f6491a71f06d4468f37e04ca5a09df3487fc03c4a04cc73263720c144cde600` |
| Overall entropy | 6.578 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1698148974 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 389,120 | 6.488 | No |
| `.rdata` | 542,720 | 5.852 | No |
| `.data` | 512 | 1.075 | No |
| `.data2` | 512 | 0.508 | No |
| `.rdata2` | 512 | 1.001 | No |
| `.rsrc` | 199,680 | 4.843 | No |
| `.reloc` | 28,160 | 6.767 | No |

### Imports

**KERNEL32.dll**: `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `FindClose`, `GetACP`, `GetCommandLineA`, `GetCommandLineW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentProcessorNumber`, `GetCurrentThreadId`, `GetLargePageMinimum`, `GetLastError`, `GetLocalTime`, `GetModuleHandleA`, `GetOEMCP`
**ADVAPI32.dll**: `RegDeleteKeyA`, `RegEnumKeyExA`
**GDI32.dll**: `CreateFontIndirectA`, `MoveToEx`, `SetBkMode`
**USER32.dll**: `BeginDeferWindowPos`, `BeginPaint`, `EndDeferWindowPos`, `EndPaint`, `GetActiveWindow`, `GetCapture`, `GetCaretBlinkTime`, `GetCaretPos`, `GetClassNameA`, `GetCursor`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgCtrlID`, `GetDoubleClickTime`

### Exports

`CfgStopRuntimeStatus@12`, `CsrNotifyObjectStatus@12`, `CsrQueryPartitionEx`, `DbgAcquireHandleData@12`, `DbgEnumeratePipelineData@4`, `DllInitialize@8`, `DllUninitialize@12`, `DllUpdate`, `GetDllVersion@12`, `KsecConfigureServiceData@12`, `KsecObservePartition`, `NtDeleteEndpointW@8`, `NtObservePropertiesAsync`, `PfxAttachControllerCount@4`, `RtlGetStatisticsA`, `RtlInspectSchema`, `SvcHostPushServiceGlobals`, `UnregisterDll@4`, `UsbUnlockPartitionEx`, `WppResumePartitionEx`

## Extracted Strings

Total strings found: **3208** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.data2
@.rdata2
@.rsrc
@.reloc
ffffff.
4$#5`P
ffffff.
ffffff.
ffffff.
ffffff.
ffffff.
ffffff.
4$#5TP
ffffff.
ffffff.
ffffff.
4$#5TP
ffffff.
ffffff.
T$#T$
D$#D$
ffffff.
L$#$
T$(#T$,
D$(#D$,
ffffff.
ffffff.
D$@j//\
T$(T$
t$(#t$
|$(3|$
T$(3T$
T$T$8
t$#t$8
|$3|$8
T$3T$8
|$$#|$H
T$$#T$H
T$(T$$
t$(#t$$
|$(3|$$
T$(3T$$
|$4#|$$
T$4#T$$
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
4$35XP
D$<#D$
t$<#t$
ffffff.
ffffff.
T$<T$
t$<#t$
|$<3|$
T$<3T$
T$T$,
t$#t$,
|$3|$,
T$3T$,
T$#T$
D$#D$
L$ L$
D$ #D$
D$D$
L$#L$
T$3T$
D$3D$
T$0#T$
D$0#D$
D$8D$@
L$8#L$@
T$83T$@
D$83D$@
L$$L$ 
D$$#D$ 
D$4D$0
L$4#L$0
T$43T$0
D$43D$0
ffffff.
ffffff.
ffffff.
4$#5`P
D$(&@A|
D$4#D$
t$4#t$
D$ D$
L$ #L$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.10055b80` | `0x10055b80` | 23220 | ✓ |
| `fcn.1003b860` | `0x1003b860` | 7928 | ✓ |
| `fcn.1001cf90` | `0x1001cf90` | 4909 | ✓ |
| `fcn.1003a930` | `0x1003a930` | 2662 | ✓ |
| `fcn.1001e2c0` | `0x1001e2c0` | 2354 | ✓ |
| `fcn.1005f120` | `0x1005f120` | 1219 | ✓ |
| `fcn.1003b3a0` | `0x1003b3a0` | 1176 | ✓ |
| `fcn.1005f5f0` | `0x1005f5f0` | 889 | ✓ |
| `fcn.1003d760` | `0x1003d760` | 834 | ✓ |
| `fcn.1001cb90` | `0x1001cb90` | 775 | ✓ |
| `fcn.1003a6b0` | `0x1003a6b0` | 625 | ✓ |
| `sym.ZCF617.dll_RtlInspectSchema` | `0x1005dba0` | 316 | ✓ |
| `sym.ZCF617.dll_UnregisterDll_4` | `0x1005bd10` | 311 | ✓ |
| `sym.ZCF617.dll_SvcHostPushServiceGlobals` | `0x1005e340` | 282 | ✓ |
| `fcn.1003dab0` | `0x1003dab0` | 278 | ✓ |
| `sym.ZCF617.dll_KsecConfigureServiceData_12` | `0x1005d920` | 277 | ✓ |
| `sym.ZCF617.dll_CsrQueryPartitionEx` | `0x1005c620` | 268 | ✓ |
| `sym.ZCF617.dll_NtObservePropertiesAsync` | `0x1005d250` | 238 | ✓ |
| `sym.ZCF617.dll_RtlGetStatisticsA` | `0x1005c8b0` | 232 | ✓ |
| `sym.ZCF617.dll_CsrNotifyObjectStatus_12` | `0x1005e900` | 228 | ✓ |
| `sym.ZCF617.dll_WppResumePartitionEx` | `0x1005ddd0` | 226 | ✓ |
| `sym.ZCF617.dll_PfxAttachControllerCount_4` | `0x1005cbb0` | 202 | ✓ |
| `sym.ZCF617.dll_DllUninitialize_12` | `0x1005cff0` | 200 | ✓ |
| `sym.ZCF617.dll_DllInitialize_8` | `0x1005b8c0` | 194 | ✓ |
| `sym.ZCF617.dll_DbgEnumeratePipelineData_4` | `0x1005def0` | 191 | ✓ |
| `sym.ZCF617.dll_DbgAcquireHandleData_12` | `0x1005e100` | 172 | ✓ |
| `sym.ZCF617.dll_UsbUnlockPartitionEx` | `0x1005c250` | 168 | ✓ |
| `sym.ZCF617.dll_KsecObservePartition` | `0x1005bc00` | 153 | ✓ |
| `sym.ZCF617.dll_GetDllVersion_12` | `0x1005e6a0` | 98 | ✓ |
| `sym.ZCF617.dll_NtDeleteEndpointW_8` | `0x1005bfc0` | 93 | ✓ |

### Decompiled Code Files

- [`code/fcn.1001cb90.c`](code/fcn.1001cb90.c)
- [`code/fcn.1001cf90.c`](code/fcn.1001cf90.c)
- [`code/fcn.1001e2c0.c`](code/fcn.1001e2c0.c)
- [`code/fcn.1003a6b0.c`](code/fcn.1003a6b0.c)
- [`code/fcn.1003a930.c`](code/fcn.1003a930.c)
- [`code/fcn.1003b3a0.c`](code/fcn.1003b3a0.c)
- [`code/fcn.1003b860.c`](code/fcn.1003b860.c)
- [`code/fcn.1003d760.c`](code/fcn.1003d760.c)
- [`code/fcn.1003dab0.c`](code/fcn.1003dab0.c)
- [`code/fcn.10055b80.c`](code/fcn.10055b80.c)
- [`code/fcn.1005f120.c`](code/fcn.1005f120.c)
- [`code/fcn.1005f5f0.c`](code/fcn.1005f5f0.c)
- [`code/sym.ZCF617.dll_CsrNotifyObjectStatus_12.c`](code/sym.ZCF617.dll_CsrNotifyObjectStatus_12.c)
- [`code/sym.ZCF617.dll_CsrQueryPartitionEx.c`](code/sym.ZCF617.dll_CsrQueryPartitionEx.c)
- [`code/sym.ZCF617.dll_DbgAcquireHandleData_12.c`](code/sym.ZCF617.dll_DbgAcquireHandleData_12.c)
- [`code/sym.ZCF617.dll_DbgEnumeratePipelineData_4.c`](code/sym.ZCF617.dll_DbgEnumeratePipelineData_4.c)
- [`code/sym.ZCF617.dll_DllInitialize_8.c`](code/sym.ZCF617.dll_DllInitialize_8.c)
- [`code/sym.ZCF617.dll_DllUninitialize_12.c`](code/sym.ZCF617.dll_DllUninitialize_12.c)
- [`code/sym.ZCF617.dll_GetDllVersion_12.c`](code/sym.ZCF617.dll_GetDllVersion_12.c)
- [`code/sym.ZCF617.dll_KsecConfigureServiceData_12.c`](code/sym.ZCF617.dll_KsecConfigureServiceData_12.c)
- [`code/sym.ZCF617.dll_KsecObservePartition.c`](code/sym.ZCF617.dll_KsecObservePartition.c)
- [`code/sym.ZCF617.dll_NtDeleteEndpointW_8.c`](code/sym.ZCF617.dll_NtDeleteEndpointW_8.c)
- [`code/sym.ZCF617.dll_NtObservePropertiesAsync.c`](code/sym.ZCF617.dll_NtObservePropertiesAsync.c)
- [`code/sym.ZCF617.dll_PfxAttachControllerCount_4.c`](code/sym.ZCF617.dll_PfxAttachControllerCount_4.c)
- [`code/sym.ZCF617.dll_RtlGetStatisticsA.c`](code/sym.ZCF617.dll_RtlGetStatisticsA.c)
- [`code/sym.ZCF617.dll_RtlInspectSchema.c`](code/sym.ZCF617.dll_RtlInspectSchema.c)
- [`code/sym.ZCF617.dll_SvcHostPushServiceGlobals.c`](code/sym.ZCF617.dll_SvcHostPushServiceGlobals.c)
- [`code/sym.ZCF617.dll_UnregisterDll_4.c`](code/sym.ZCF617.dll_UnregisterDll_4.c)
- [`code/sym.ZCF617.dll_UsbUnlockPartitionEx.c`](code/sym.ZCF617.dll_UsbUnlockPartitionEx.c)
- [`code/sym.ZCF617.dll_WppResumePartitionEx.c`](code/sym.ZCF617.dll_WppResumePartitionEx.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2, I have updated the analysis of the binary. The evidence confirms that this is a highly sophisticated piece of malware with advanced protective layers.

### Updated Analysis

#### 1. Advanced Obfuscation: Virtualization & State Machine Logic
The most striking feature in this second chunk is the extreme level of **Control Flow Flattening (CFF)** and what appears to be a **Custom Virtual Machine (VM) architecture** or a "Dispatcher" pattern.
*   **Dispatcher Loops:** Functions like `fcn.10055b80` and `fcn.1001cf90` are not standard functions; they are large state machines. The variable `uStack_178` (and similar variables) acts as a "virtual" program counter. Instead of logical flow, the code evaluates this value against various constants to decide which block of code to execute next.
*   **Complex Arithmetic for Branching:** Many blocks involve complex mathematical calculations (e.g., `uVar5 = ((~uVar1 | uVar2) ...` ) before setting the state variable. This is designed to break static analysis tools; it's difficult to tell which path the "real" code takes without running it in a debugger.
*   **Indirect Jumps:** The use of `0x1005dcdc`, `0x1005e462`, and other memory-based jumps indicates that the binary uses an internal jump table. This allows the malware to "jump" into different pieces of code that aren't explicitly linked in a standard way, making it hard for a researcher to follow the logical flow.

#### 2. Enhanced Anti-Analysis & Environment Fingerprinting
The second chunk provides more concrete evidence of how the binary detects and evades analysis:
*   **System Information Harvesting:** The use of `GetSystemMetrics` (found in `fcn.1001cb90`), `GetProcessId`, and `GetVersion`. These are classic indicators used to detect if the application is running on a standard workstation or within a virtualized sandbox environment (where metrics like screen resolution or system versions might differ).
*   **Active Window & Focus Checks:** The calls to `GetForegroundWindow` and `IsWindowVisible` suggest the malware checks for user interaction. If no window is "in focus," it may assume it is being monitored by an automated sandboxed tool.
*   **Resource Management:** Use of `GetProcessHeap`, `HeapFree`, and standard memory management functions are often used in loaders to allocate space for decrypted payloads or to manage the "garbage" data generated during the unpacking process.

#### 3. Just-In-Time (JIT) Decryption & Dynamic Resolution
*   **Dynamic Memory Manipulation:** There is frequent access to specific hardcoded memory addresses (e.g., `0x100e505c`, `0x100e5054`). The code frequently performs XOR and ADD operations on these locations based on values it "scrapes" from the environment or other functions. This is a hallmark of **Just-In-Time (JIT) decryption**, where parts of the malicious payload are only decrypted in memory for the millisecond they are needed, then re-encrypted or overwritten.
*   **Implicit API Mapping:** The series of `sym.` prefixed functions (e.g., `sym.ZCF617.dll_RtlInspectSchema`, `sym.ZCF617.dll_SvcHostPushServiceGlobals`) indicates a **System Call/API mapping table**. This suggests the binary has its own internal "dictionary" of Windows functions, allowing it to call system functionalities without directly referencing names in the Import Address Table (IAT), thereby hiding its capabilities from static scanners.

#### 4. Potential Payload Logic Indicators
While this code is primarily a loader, some hints about the payload's nature appear:
*   **String Processing:** `fcn.1005f5f0` and `fcn.1003a6b0` contain logic that seems to handle specific character patterns (like `%`, or checks for 'N' and 't'). This is often used in the parsing of configuration files, C2 instructions, or internal "handshake" protocols between a bot and its server.
*   **Data Parsing:** The loops involving `uStack_8c` being decremented while checking against a limit (like 8) suggest the processing of structured data packets.

---

### Summary for Incident Response

**Risk Level: High / Sophisticated.**

1.  **Classification:** This binary is a **highly professional malware loader/protector**. It likely utilizes techniques similar to those found in Cobalt Strike, Emotet, or other high-tier Trojan families.
2.  **Evasion Tactics:** 
    *   **Anti-Sandbox:** It actively checks system metrics and user interaction to "sleep" or change behavior if it detects a researcher's environment.
    *   **Anti-Analysis:** The control flow is so heavily flattened that manual deconstruction via static analysis (like IDA Pro) will be extremely time-consuming and may not fully reveal the payload until the moment of execution.
3.  **Payload Presence:** This specific module is a "wrapper." It is designed to:
    *   Verify the environment is safe for infection.
    *   Decrypt and inject an additional, potentially more malicious stage (the "payload").
4.  **Recommendation:** 
    *   **Isolate Host:** Any machine where this binary is found should be isolated from the network immediately.
    *   **Dynamic Analysis:** Because of the high level of obfuscation, static analysis alone is insufficient. Memory forensics and behavior monitoring in a *hardened* (non-standard) sandbox are required to capture the payload as it "unpacks" itself in memory.
    *   **Look for Indicators of Compromise (IOCs):** Look for suspicious network connections (specifically over non-standard ports), calls to `GetSystemMetrics` or `GetProcessId`, and any new entries in persistence locations (Registry, Scheduled Tasks) following the execution of this loader.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Programs | The use of control flow flattening, a custom VM architecture, and JIT decryption are designed to hide the program's logic from static analysis. |
| **T1036** | System Information Discovery | Functions such as `GetSystemMetrics` and `GetVersion` are used to fingerprint the environment and detect if it is being monitored or sandboxed. |
| **T1027.001** | Obfuscated Files or Programs: Packing | The use of an internal mapping table (dynamic resolution) and JIT decryption indicates a "wrapper" approach to hide the final payload until execution. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contains significant amounts of obfuscated data and internal memory offsets/garbage characters that do not constitute actionable network or file system IOCs.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified (Note: Hexadecimal values like `0x1005b80` are internal memory offsets, not file hashes).*

### **Other artifacts**
*   **Anti-Analysis API Calls:** The binary utilizes the following Windows APIs to fingerprint the environment and detect sandboxes/debuggers:
    *   `GetSystemMetrics` (Used for detecting non-standard screen resolutions)
    *   `GetProcessId` (Used to identify specific system processes)
    *   `GetVersion` (Used to determine OS version compatibility)
    *   `GetForegroundWindow` & `IsWindowVisible` (Used to detect active user interaction/manual operation)
*   **Evasion Techniques:** 
    *   **Control Flow Flattening (CFF):** Use of a "Dispatcher" pattern to obscure logic.
    *   **Custom VM Architecture:** Implementation of a custom instruction set/dispatcher for malicious code execution.
    *   **JIT Decryption:** Frequent memory manipulation (`XOR`, `ADD` operations) on specific memory addresses to decrypt payloads in-memory only when needed.
*   **Instructional Mapping:** The use of an internal API mapping table (e.g., `sym.ZCF617.dll_...`) suggests a technique to bypass Import Address Table (IAT) scanning.

---
**Analyst Note:** While there are no "hard" IOCs (like IPs or file hashes) present in this specific sample, the **behavioral indicators** suggest a high-sophistication loader. Detection should focus on heuristic triggers: execution of processes calling `GetSystemMetrics` followed by rapid memory allocation and `XOR` operations, or calls to `GetForegroundWindow` used as an anti-analysis gate.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Obfuscation & Anti-Analysis:** The sample employs highly sophisticated techniques including Control Flow Flattening (CFF), a Custom Virtual Machine architecture, and extensive environment fingerprinting (e.g., `GetSystemMetrics`, `GetForegroundWindow`) to evade automated sandboxes and manual analysis.
*   **Loader Functionality:** The presence of Just-In-Time (JIT) decryption (using XOR/ADD operations on memory segments) and a custom internal API mapping table indicates its primary role is as a "wrapper" or loader designed to decrypt and inject a secondary, potentially more malicious payload into memory.
*   **Evasion Indicators:** The use of hidden import tables and complex state machine logic suggests it belongs to the category of professional-grade tools (similar in sophistication to Cobalt Strike components) rather than common commodity malware.
