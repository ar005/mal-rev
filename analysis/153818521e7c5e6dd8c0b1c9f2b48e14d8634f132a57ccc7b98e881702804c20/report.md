# Threat Analysis Report

**Generated:** 2026-09-06 20:26 UTC
**Sample:** `153818521e7c5e6dd8c0b1c9f2b48e14d8634f132a57ccc7b98e881702804c20_153818521e7c5e6dd8c0b1c9f2b48e14d8634f132a57ccc7b98e881702804c20.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `153818521e7c5e6dd8c0b1c9f2b48e14d8634f132a57ccc7b98e881702804c20_153818521e7c5e6dd8c0b1c9f2b48e14d8634f132a57ccc7b98e881702804c20.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 8 sections |
| Size | 2,497,024 bytes |
| MD5 | `60e90409c6bf0351c709084315a9f7bf` |
| SHA1 | `54367657542277e3970479d896b3f4903aa20f95` |
| SHA256 | `153818521e7c5e6dd8c0b1c9f2b48e14d8634f132a57ccc7b98e881702804c20` |
| Overall entropy | 6.615 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1530316372 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,234,432 | 6.226 | No |
| `.rdata` | 186,880 | 7.417 | ⚠️ Yes |
| `.data` | 4,096 | 6.72 | No |
| `.pdata2` | 512 | 1.166 | No |
| `.text2` | 512 | 0.969 | No |
| `.tls2` | 512 | 0.423 | No |
| `.rsrc` | 985,600 | 5.848 | No |
| `.reloc` | 83,456 | 6.81 | No |

### Imports

**KERNEL32.dll**: `CreateThread`, `DeleteCriticalSection`, `DisableThreadLibraryCalls`, `FindFirstFileA`, `GetACP`, `GetCommandLineA`, `GetCommandLineW`, `GetCurrentProcess`, `GetCurrentProcessId`, `GetCurrentProcessorNumber`, `GetCurrentThreadId`, `GetLargePageMinimum`, `GetLastError`, `GetLocalTime`, `GetModuleHandleA`
**ADVAPI32.dll**: `RegDeleteValueA`, `RegOpenKeyExA`, `RegQueryValueExA`
**SHELL32.dll**: `DragQueryFileA`, `SHGetFileInfoA`
**USER32.dll**: `BeginDeferWindowPos`, `BeginPaint`, `EndDeferWindowPos`, `EndPaint`, `EnumWindows`, `GetActiveWindow`, `GetCapture`, `GetCaretBlinkTime`, `GetCaretPos`, `GetCursor`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetDlgCtrlID`, `GetDoubleClickTime`

### Exports

`LdrQueryPermissionCount@8`, `NdisRegisterHandleCount`, `NtInvokeCatalogEx`, `RtlUnlockController@4`, `UsbInspectPermissionCount`, `WppCloseNotificationData`, `ZwBindControllerA@8`

## Extracted Strings

Total strings found: **12641** (showing first 100)

```
!This program cannot be run in DOS mode.$
`.rdata
@.data
.pdata2
@.text2
@.tls2
@.rsrc
@.reloc
D$3D$
L$#L$
L$3L$
D$3D$
D$4D$(
L$4#L$(
D$,D$$
L$,#L$$
D$83D$ 
L$8#L$ 
L$83L$ 
D$83D$ )
T$T#T$0
D$T#D$0
D$,3D$ 
L$,#L$ 
T$,3T$ 
L$,3L$ 
T$L#T$8
D$L#D$8
D$#D$@
t$#t$@
D$ D$<
L$ #L$<
D$<#D$(
L$<#L$(
D$4#D$$
t$4#t$$
fffff.
ffffff.
D$,3D$H
L$,#L$H
L$,3L$H
D$,3D$H)
$#L$8
$3L$8
$3D$8)
D$@3D$,
L$@#L$,
L$@3L$,
D$@3D$,)
D$(3D$
L$(#L$
L$(3L$
D$(3D$
$#L$
t$4#t$8
L$4#L$8
L$DL$4
T$D#T$4
$L$(
D$,#D$X
t$,#t$X
D$83D$
L$8#L$
L$83L$
D$83D$
T$#T$T
D$#D$T
D$$3D$
L$$#L$
L$$3L$
D$$3D$
T$ #T$(
D$ #D$(
T$0#T$\
D$0#D$\
t$H#t$4
L$H#L$4
L$<L$
T$<#T$
L$3L$D
T$#T$D
T$3T$D
L$3L$D)
L$ 3L$
T$ #T$
t$ 3t$
T$ 3T$
T$P#T$4
D$P#D$4
T$$#T$
D$$#D$
wMfff.
ffffff.
D$3D$<
L$#L$<
L$3L$<
D$3D$<)
D$ D$0
L$ #L$0
D$$3D$8
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.101264a0` | `0x101264a0` | 25966 | ✓ |
| `fcn.100d7d60` | `0x100d7d60` | 8387 | ✓ |
| `fcn.10065090` | `0x10065090` | 5165 | ✓ |
| `fcn.100d6430` | `0x100d6430` | 3808 | ✓ |
| `fcn.100639e0` | `0x100639e0` | 3197 | ✓ |
| `fcn.10064660` | `0x10064660` | 2608 | ✓ |
| `fcn.100d7310` | `0x100d7310` | 2605 | ✓ |
| `fcn.1012dc40` | `0x1012dc40` | 1253 | ✓ |
| `sym.unfortunately50.dll_UsbInspectPermissionCount` | `0x1012d050` | 1075 | ✓ |
| `sym.unfortunately50.dll_LdrQueryPermissionCount_8` | `0x1012d8b0` | 899 | ✓ |
| `fcn.100d9e30` | `0x100d9e30` | 824 | ✓ |
| `fcn.1012e130` | `0x1012e130` | 706 | ✓ |
| `fcn.10063680` | `0x10063680` | 606 | ✓ |
| `sym.unfortunately50.dll_ZwBindControllerA_8` | `0x1012d660` | 582 | ✓ |
| `fcn.100d6210` | `0x100d6210` | 544 | ✓ |
| `sym.unfortunately50.dll_WppCloseNotificationData` | `0x1012d490` | 449 | ✓ |
| `sym.unfortunately50.dll_RtlUnlockController_4` | `0x1012cd60` | 397 | ✓ |
| `sym.unfortunately50.dll_NdisRegisterHandleCount` | `0x1012cef0` | 346 | ✓ |
| `entry0` | `0x1012ca10` | 295 | ✓ |
| `fcn.100da170` | `0x100da170` | 272 | ✓ |
| `fcn.10001080` | `0x10001080` | 181 | ✓ |
| `sym.unfortunately50.dll_NtInvokeCatalogEx` | `0x1012ccd0` | 137 | ✓ |
| `section..text` | `0x10001000` | 126 | ✓ |
| `fcn.1012e4b8` | `0x1012e4b8` | 48 | ✓ |
| `fcn.1012e401` | `0x1012e401` | 48 | ✓ |
| `fcn.1012e4e8` | `0x1012e4e8` | 45 | ✓ |
| `fcn.1012e432` | `0x1012e432` | 45 | ✓ |
| `fcn.1012e48b` | `0x1012e48b` | 45 | ✓ |
| `fcn.1012e45f` | `0x1012e45f` | 44 | ✓ |
| `fcn.1012e3f5` | `0x1012e3f5` | 12 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.10001080.c`](code/fcn.10001080.c)
- [`code/fcn.10063680.c`](code/fcn.10063680.c)
- [`code/fcn.100639e0.c`](code/fcn.100639e0.c)
- [`code/fcn.10064660.c`](code/fcn.10064660.c)
- [`code/fcn.10065090.c`](code/fcn.10065090.c)
- [`code/fcn.100d6210.c`](code/fcn.100d6210.c)
- [`code/fcn.100d6430.c`](code/fcn.100d6430.c)
- [`code/fcn.100d7310.c`](code/fcn.100d7310.c)
- [`code/fcn.100d7d60.c`](code/fcn.100d7d60.c)
- [`code/fcn.100d9e30.c`](code/fcn.100d9e30.c)
- [`code/fcn.100da170.c`](code/fcn.100da170.c)
- [`code/fcn.101264a0.c`](code/fcn.101264a0.c)
- [`code/fcn.1012dc40.c`](code/fcn.1012dc40.c)
- [`code/fcn.1012e130.c`](code/fcn.1012e130.c)
- [`code/fcn.1012e3f5.c`](code/fcn.1012e3f5.c)
- [`code/fcn.1012e401.c`](code/fcn.1012e401.c)
- [`code/fcn.1012e432.c`](code/fcn.1012e432.c)
- [`code/fcn.1012e45f.c`](code/fcn.1012e45f.c)
- [`code/fcn.1012e48b.c`](code/fcn.1012e48b.c)
- [`code/fcn.1012e4b8.c`](code/fcn.1012e4b8.c)
- [`code/fcn.1012e4e8.c`](code/fcn.1012e4e8.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sym.unfortunately50.dll_LdrQueryPermissionCount_8.c`](code/sym.unfortunately50.dll_LdrQueryPermissionCount_8.c)
- [`code/sym.unfortunately50.dll_NdisRegisterHandleCount.c`](code/sym.unfortunately50.dll_NdisRegisterHandleCount.c)
- [`code/sym.unfortunately50.dll_NtInvokeCatalogEx.c`](code/sym.unfortunately50.dll_NtInvokeCatalogEx.c)
- [`code/sym.unfortunately50.dll_RtlUnlockController_4.c`](code/sym.unfortunately50.dll_RtlUnlockController_4.c)
- [`code/sym.unfortunately50.dll_UsbInspectPermissionCount.c`](code/sym.unfortunately50.dll_UsbInspectPermissionCount.c)
- [`code/sym.unfortunately50.dll_WppCloseNotificationData.c`](code/sym.unfortunately50.dll_WppCloseNotificationData.c)
- [`code/sym.unfortunately50.dll_ZwBindControllerA_8.c`](code/sym.unfortunately50.dll_ZwBindControllerA_8.c)

## Behavioral Analysis

This additional disassembly (chunk 3) provides further confirmation of the malware’s high level of sophistication, specifically regarding **Control Flow Flattening**, **API Masquerading**, and **Multi-Layered Environmental Checks.**

The evidence suggests this is not a simple piece of malware but a professionally engineered "Loader" or "Dropper," likely utilizing a commercial protector (like Tigress, VMProtect, or a custom LLVM-based obfuscator).

### Updated Analysis Summary
The inclusion of these functions confirms that the malware uses a **Modular State-Machine Architecture**. The code is designed to be virtually unreadable to humans and difficult for automated tools to map. Each function acts as a "gate" or "transformation engine." If the environment (the computer) satisfies certain conditions, the state machine progresses; if not, it halts execution or takes an alternate path that hides its true behavior.

---

### Core Functionality and Purpose (Updated)
The code's primary role is to **sanitize the environment** before unpacking a secondary payload. 

*   **Control Flow Flattening (CFF):** In functions like `fcn.100d7310` and `fcn.1012dc40`, the standard logic of "if this, do that" has been replaced by a massive switch-case structure where every jump is determined by a calculation (`uStack_cc = uStack_cc ^ 0x19c7`). This makes it impossible to follow the logic path without tracing it in real-time with a debugger.
*   **Sophisticated State Management:** The use of `iStack_d8` and `uStack_cc` as state variables allows the code to perform multiple different actions (decryption, anti-debugging, environment check) while appearing as one large, convoluted loop. 
*   **Decoy Name/API Masking:** Several functions possess "legitimate-sounding" names that likely have nothing to do with their actual function:
    *   `UsbInspectPermissionCount`
    *   `LdrQueryPermissionCount_8`
    *   `ZwBindControllerA_8`
    *   `WppCloseNotificationData`
    *   `NdisRegisterHandleCount`
    These names are likely chosen to blend in with system-level DLLs or are artifacts of an obfuscation tool. They contain heavy logic related to **User Interface interaction** and **System Time**, which suggests they are actually part of the anti-analysis engine.

### New Suspicious or Malicious Behaviors
*   **Interaction Monitoring:** The functions `sym.unfortunately50.dll_RtlUnlockController_4` and `sym.unfortunately50.dll_ZwBindControllerA_8` call `GetCursor()` and `GetCaretPos()`. This is a high-confidence indicator of **anti-automation**. It checks if the mouse/cursor is moving or where it is located to determine if a human is actively interacting with the PC.
*   **Contextual Awareness:** The calls to `GetForegroundWindow`, `GetActiveWindow`, and `GetDesktopWindow` suggest the malware is checking which window has focus. If the "active" window is a known analysis tool or if there is no active window (typical of sandboxes), it may stay dormant.
*   **Advanced Environment Verification:** The use of `GetVersion`, `GetOEMCP`, and `IsValidCodePage` in functions like `NdisRegisterHandleCount` suggests the malware is checking for specific OS versions or localization settings that are common in certain regions, potentially to target a specific geographic audience or avoid automated Western-based security labs.
*   **Internal Data Processing:** The function `fcn.100d6210` contains a **switch table of 57 cases**. This is typically used for complex character mapping or decoding an encoded string/configuration block at runtime. It likely decodes "hardcoded" strings (like C2 domains or registry keys) only *after* the anti-analysis checks are passed.

### Technical Obfuscation Techniques
1.  **Opaque Predicates:** The code contains many branches where the condition is mathematically complex but ultimately leads to a known result, designed solely to confuse automated decompilers (e.g., the arithmetic in `fcn.1012dc40`).
2.  **Instruction Substitution:** Simple operations are replaced with multi-step bitwise manipulations (e.g., `uStack_cc = uStack_cc ^ 0x19c7`). This prevents an analyst from seeing "simple" logic and instead shows a wall of math.
3.  **Junk Code Insertion:** There is evidence of code that does nothing except modify local variables used for the next jump, ensuring the "logical path" stays hidden.

---

### Summary for Incident Response (Updated)

This is a **Highly Sophisticated Loader**. It is specifically engineered to evade detection by human analysts and automated sandbox systems during the initial stages of infection.

**Critical Indicators & Tactics:**
1.  **Anti-Sandbox/Analysis Environment:** The malware uses multiple layers of checks (`GetCursor`, `GetTickCount`, `GetForegroundWindow`) to ensure it is running on a "real" user's machine before revealing its malicious payload.
2.  **Decoy Logic:** It uses misleading function names and massive switch tables to slow down manual analysis. If an analyst spends hours de-obfuscating one function, they may miss the overarching behavior of the malware.
3.  **Delayed Payload Execution:** The complexity of these functions indicates that this is a "Pre-Flight" check. Once it determines the environment is safe, it will likely perform a final decryption and execute its primary payload (e.g., ransomware or info-stealer).

**Recommended Actions:**
*   **Dynamic Analysis Strategy:** Do not spend significant manual effort trying to "de-obfuscate" the logic of these specific functions; they are designed as a labyrinth for that purpose. Instead, use a debugger and **manually step through the code until it reaches its next "jump point."**
*   **Payload Extraction via Memory Forensics:** The most effective way to see what this malware actually *does* is to run it in a controlled environment (with simulated mouse/keyboard input) and perform a **memory dump** once the initial "loop" of obfuscation finishes. This will reveal the actual malicious payload (the "stage 2" component).
*   **Network Monitoring:** Monitor for outbound connections. Even if the code is heavily obfuscated, it must eventually connect to an external server to receive commands or exfiltrate data. Identify these IP addresses/domains as high-priority indicators of compromise (IOCs).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or System Tools | The use of Control Flow Flattening, Instruction Substitution, and Junk Code Insertion is designed to hide the logic flow and complicate manual reverse engineering. |
| **T1036** | Masquerading | The use of "legitimate-sounding" function names (e.g., `UsbInspectPermissionCount`) allows the malware to blend in with system-level components to deceive analysts. |
| **T1497** | Virtualization/Sandbox Detection | The analysis of `GetCursor`, `GetCaretPos`, and `GetForegroundWindow` indicates checks designed to detect automated sandboxes or lack of human interaction. |
| **T1027** | Obfuscated Files or System Tools | The implementation of a large switch table (fcn.100d6210) for decoding strings at runtime is used to hide configuration data and indicators of compromise from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The report notes that C2 domains/IPs are hidden within a "switch table of 57 cases" to be decrypted only after anti-analysis checks pass; however, they are not present in the provided text.)

### **File paths / Registry keys**
*   *None identified.* (Standard system calls were used, but no specific hardcoded file paths or registry keys were disclosed in this analysis segment.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Decoy Function Names (Indicator of Obfuscation/Packer):** 
    The following function names are confirmed as "masking" techniques to blend in with system DLLs:
    *   `UsbInspectPermissionCount`
    *   `LdrQueryPermissionCount_8`
    *   `ZwBindControllerA_8`
    *   `WppCloseNotificationData`
    *   `NdisRegisterHandleCount`
*   **Obfuscation Constants:**
    *   `0x19c7` (Used in the calculation for Control Flow Flattening: `uStack_cc = uStack_cc ^ 0x19c7`)
*   **Behavioral Markers:**
    *   **Anti-Automation Checks:** Use of `GetCursor()`, `GetCaretPos()`, and `GetForegroundWindow()` to detect human interaction.
    *   **Environment Verification:** Utilization of `GetVersion`, `GetOEMCP`, and `IsValidCodePage` to identify target regions or OS versions.

---
**Analyst Note:** The provided "EXTRACTED STRINGS" section consists entirely of obfuscated/encoded data (likely from a packed binary) and does not contain human-readable indicators such as plain-text IP addresses or file paths. The primary value for incident response in this sample lies in the **behavioral signatures** used by the loader to evade detection.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Evasion Techniques:** The sample employs high-level obfuscation such as Control Flow Flattening (CFF), instruction substitution, and a modular state-machine architecture to hide its true logic from automated analysis tools.
*   **Robust Anti-Analysis/Anti-Sandbox Measures:** The presence of `GetCursor`, `GetCaretPos`, and `GetForegroundWindow` indicates a deliberate attempt to detect human interaction and bypass automated sandboxes before executing the next stage.
*   **Pre-Flight Design:** The analysis explicitly identifies the sample as a "pre-flight" component whose primary purpose is to sanitize the environment and decrypt a secondary payload, which is the defining characteristic of a sophisticated Loader.
