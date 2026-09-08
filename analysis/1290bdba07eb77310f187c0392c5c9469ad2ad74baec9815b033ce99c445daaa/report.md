# Threat Analysis Report

**Generated:** 2026-08-31 17:16 UTC
**Sample:** `1290bdba07eb77310f187c0392c5c9469ad2ad74baec9815b033ce99c445daaa_1290bdba07eb77310f187c0392c5c9469ad2ad74baec9815b033ce99c445daaa.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1290bdba07eb77310f187c0392c5c9469ad2ad74baec9815b033ce99c445daaa_1290bdba07eb77310f187c0392c5c9469ad2ad74baec9815b033ce99c445daaa.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 8 sections |
| Size | 633,344 bytes |
| MD5 | `4afb25f1c6d862466a1c44709b4fc6cd` |
| SHA1 | `702fe397e23d41fd4cd5a3f3f76acedb39ee90e0` |
| SHA256 | `1290bdba07eb77310f187c0392c5c9469ad2ad74baec9815b033ce99c445daaa` |
| Overall entropy | 5.856 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1779628442 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 171,520 | 6.521 | No |
| `.rdata` | 445,952 | 4.871 | No |
| `.data` | 3,072 | 2.249 | No |
| `.pdata` | 8,192 | 5.371 | No |
| `_RDATA` | 512 | 2.437 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 512 | 4.768 | No |
| `.reloc` | 2,048 | 5.038 | No |

### Imports

**KERNEL32.dll**: `FreeConsole`, `LocalFree`, `GetTickCount64`, `SetLastError`, `TerminateProcess`, `WriteConsoleW`, `SetFileAttributesW`, `GetFileAttributesW`, `CreateFileW`, `DeviceIoControl`, `WriteFile`, `GetFullPathNameW`, `GetExitCodeProcess`, `CreateProcessW`, `CloseHandle`
**ADVAPI32.dll**: `RegDeleteTreeW`, `LookupPrivilegeValueW`, `AdjustTokenPrivileges`, `RevertToSelf`, `RegCloseKey`, `CloseServiceHandle`, `OpenSCManagerW`, `ChangeServiceConfig2W`, `RegCreateKeyExW`, `ControlService`, `RegSaveKeyExW`, `ImpersonateLoggedOnUser`, `RegSetValueExW`, `OpenProcessToken`, `RegUnLoadKeyW`
**SHELL32.dll**: `SHGetFolderPathW`, `SHGetKnownFolderPath`, `SHCreateDirectoryExW`, `ShellExecuteExW`
**ole32.dll**: `CoTaskMemFree`

## Extracted Strings

Total strings found: **10632** (showing first 100)

```
!This program cannot be run in DOS mode.
$
~Rich$z
`.rdata
@.data
.pdata
@_RDATA
@.fptable
@.reloc
L$ SVWH
@UATAUAVAWH
fD93tyL
fD93tyL
fD93tyL
A_A^A]A\]
\$ UVAVH
UVWAVH
@SVAVH
L$ SWH
L$ SVWH
L$ SWH
f3LT fA3
UATAUAVAWH
A_A^A]A\]
UWATAVAWH
A_A^A\_]
UWATAVAWH
A_A^A\_]
|$ fff
fB3BfA3
L$ SVWH
L$ SVWH
@UWATAVH
(A^A\_]
@SVAVAWH
8A_A^^[
@VWAUAVH
8A^A]_^
CT$HE3
UWATAVAWH
A_A^A\_]
fA3PfA3
fA3PfA3
l$ VWAVH
d$ UAVAWH
D$L}v?
f3LT0fA3
|$ UATAUAVAWH
A_A^A]A\]
UATAUAVAWH
A_A^A]A\]
fB3BfA3
fB3BfA3
fB3BfA3
@SUATAVAWH
@A_A^A\][
fB3BfA3
@UWATAVH
(A^A\_]
UVWATAUAVAWH
 A_A^A]A\_^]
@SVAVH
fA94Qu
H9t$`t
fA3PfA3
D$<jvP
f3LT fA3
fB3BfA3
fB3BfA3
fB3Bf3
UATAUAVAWH
f3TD f3
D$HQ7#
f3LT8f3
f3LTXf3
fA3Pf3
fA3Pf3
fA3Pf3
fA3Pf3
f3LT f3
f3LT f3
D$HQ7#
f3LT8f3
D$HQ7#
f3LT8f3
f3LT f3
fB3LD f3
fB3LDXf3
f3LTxf3
D$HQ7#
A_A^A]A\]
fB3BfA3
fB3BfA3
fB3BfA3
fB3BfA3
fB3BfA3
fB3BfA3
fB3BfA3
fB3Bf3
fB3Bf3
@UWATAVH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14001bd50` | `0x14001bd50` | 23971 | ✓ |
| `fcn.14001bd3c` | `0x14001bd3c` | 23930 | ✓ |
| `fcn.14001a9d4` | `0x14001a9d4` | 20166 | ✓ |
| `fcn.140025300` | `0x140025300` | 12425 | ✓ |
| `fcn.1400095d0` | `0x1400095d0` | 8612 | ✓ |
| `fcn.140027d00` | `0x140027d00` | 5831 | ✓ |
| `fcn.140023fec` | `0x140023fec` | 4735 | ✓ |
| `fcn.14000b7c0` | `0x14000b7c0` | 4415 | ✓ |
| `fcn.14000e8a0` | `0x14000e8a0` | 2450 | ✓ |
| `fcn.14000eb64` | `0x14000eb64` | 2445 | ✓ |
| `fcn.140002b30` | `0x140002b30` | 2377 | ✓ |
| `fcn.140006270` | `0x140006270` | 2025 | ✓ |
| `main` | `0x1400073a0` | 1976 | ✓ |
| `fcn.140015180` | `0x140015180` | 1898 | ✓ |
| `fcn.14000d3c0` | `0x14000d3c0` | 1876 | ✓ |
| `fcn.140020438` | `0x140020438` | 1829 | ✓ |
| `fcn.1400142e0` | `0x1400142e0` | 1685 | ✓ |
| `fcn.140018388` | `0x140018388` | 1532 | ✓ |
| `fcn.140027dd0` | `0x140027dd0` | 1451 | ✓ |
| `fcn.140018984` | `0x140018984` | 1397 | ✓ |
| `fcn.140017e50` | `0x140017e50` | 1336 | ✓ |
| `fcn.140011b3c` | `0x140011b3c` | 1275 | ✓ |
| `fcn.140005090` | `0x140005090` | 1274 | ✓ |
| `fcn.140006eb0` | `0x140006eb0` | 1250 | ✓ |
| `fcn.140011664` | `0x140011664` | 1237 | ✓ |
| `fcn.14000db20` | `0x14000db20` | 1193 | ✓ |
| `fcn.140022cf8` | `0x140022cf8` | 1171 | ✓ |
| `fcn.140023b60` | `0x140023b60` | 1164 | ✓ |
| `fcn.1400015e0` | `0x1400015e0` | 1161 | ✓ |
| `fcn.140025f1c` | `0x140025f1c` | 1119 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400015e0.c`](code/fcn.1400015e0.c)
- [`code/fcn.140002b30.c`](code/fcn.140002b30.c)
- [`code/fcn.140005090.c`](code/fcn.140005090.c)
- [`code/fcn.140006270.c`](code/fcn.140006270.c)
- [`code/fcn.140006eb0.c`](code/fcn.140006eb0.c)
- [`code/fcn.1400095d0.c`](code/fcn.1400095d0.c)
- [`code/fcn.14000b7c0.c`](code/fcn.14000b7c0.c)
- [`code/fcn.14000d3c0.c`](code/fcn.14000d3c0.c)
- [`code/fcn.14000db20.c`](code/fcn.14000db20.c)
- [`code/fcn.14000e8a0.c`](code/fcn.14000e8a0.c)
- [`code/fcn.14000eb64.c`](code/fcn.14000eb64.c)
- [`code/fcn.140011664.c`](code/fcn.140011664.c)
- [`code/fcn.140011b3c.c`](code/fcn.140011b3c.c)
- [`code/fcn.1400142e0.c`](code/fcn.1400142e0.c)
- [`code/fcn.140015180.c`](code/fcn.140015180.c)
- [`code/fcn.140017e50.c`](code/fcn.140017e50.c)
- [`code/fcn.140018388.c`](code/fcn.140018388.c)
- [`code/fcn.140018984.c`](code/fcn.140018984.c)
- [`code/fcn.14001a9d4.c`](code/fcn.14001a9d4.c)
- [`code/fcn.14001bd3c.c`](code/fcn.14001bd3c.c)
- [`code/fcn.14001bd50.c`](code/fcn.14001bd50.c)
- [`code/fcn.140020438.c`](code/fcn.140020438.c)
- [`code/fcn.140022cf8.c`](code/fcn.140022cf8.c)
- [`code/fcn.140023b60.c`](code/fcn.140023b60.c)
- [`code/fcn.140023fec.c`](code/fcn.140023fec.c)
- [`code/fcn.140025300.c`](code/fcn.140025300.c)
- [`code/fcn.140025f1c.c`](code/fcn.140025f1c.c)
- [`code/fcn.140027d00.c`](code/fcn.140027d00.c)
- [`code/fcn.140027dd0.c`](code/fcn.140027dd0.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

This updated analysis incorporates findings from the third and final portion of the disassembled code.

### Updated Summary: Analysis of Malware Loader/Rootkit Component

The binary is a highly sophisticated **malware loader and staging engine** for a kernel-mode rootkit. The latest disassembly reveals the specific mechanisms used to decrypt the payload, drop it onto the file system, and implement "waiting" periods to ensure security software has been successfully disabled before the final infection stage occurs.

---

### Core Functionality and Purpose
The code functions as a multi-stage execution pipeline:
*   **Payload Decryption & File I/O:** The function `fcn.140005090` contains the logic for processing an in-memory buffer. Crucially, it includes the string **"Driver image decrypted,"** confirming that the primary payload (the driver) is decrypted within memory before being written to disk via `CreateFileW` and `WriteFile`.
*   **Staged Execution & Wait Logic:** The function `fcn.140006eb0` implements a timed loop (approximately 60,000 milliseconds or 1 minute). This is used as a "waiting period" to allow system changes—such as the shutdown of antivirus services—to complete before the loader proceeds to its next phase.
*   **Environmental Fingerprinting:** The functions `fcn.1400015e0` and `fcn.140025f1c` interact with `GetEnvironmentVariableW`, `GetUserNameW`, and `GetComputerNameExW`. This is used to gather system information, likely to detect virtual machine environments or specific target profiles.
*   **Complex Data Parsing:** The functions `fcn.140011664` and `fcn.140023b60` act as the "brain" of the loader. They use nested loops, complex bitwise shifts, and multi-pass processing to interpret encrypted configuration tables or state machines that guide the malware’s execution flow.

---

### Suspicious and Malicious Behaviors (Expanded)

*   **In-Memory Payload Decryption:**
    *   The transition from "encrypted data" in a buffer to the string **"Driver image decrypted"** followed by `WriteFile` operations indicates a multi-stage loading process. This ensures that the raw, malicious driver file only exists on disk for a very short window after being decrypted in memory, making it harder for scanners to detect.
*   **Persistence & Timing Evasion:**
    *   The 60-second loop (using `GetTickCount64`) and the logic checking for **"Some targets still running after 1 minute"** is a sophisticated evasion tactic. It ensures that if an antivirus service takes time to shut down, the malware stays "silent" until the security software is fully offline before it attempts to inject or load the rootkit.
*   **Dropper Behavior:**
    *   The use of hardcoded logic for `CreateFileW(drop)` and `WriteFile(drop)` confirms that this binary's primary role is as a **dropper**. It takes an encrypted blob, decrypts it, and writes it to the filesystem with a name (or temporary location) intended for subsequent loading via `NtLoadDriver`.
*   **Heavy Obfuscation & State-Machine Dispatching:**
    *   The logic in `fcn.140011664` uses complex nested loops to parse data tables. This isn't just "messy code"; it is a deliberate attempt to hide the execution path from automated analysis tools (like IDA or Ghidra's standard decompiler), as the actual "next step" in the code depends on values hidden inside decrypted memory buffers.
*   **Advanced Decoding Logic:**
    *   The function `fcn.140023b60` uses complex bitwise arithmetic (e.g., `uVar16 = uVar8 | uVar16 << (iVar11 & 0x1f)`). This is indicative of a **custom decompression or de-obfuscation algorithm** used to unpack internal commands or configurations from the remote server (C2) or an embedded file.

---

### Notable Techniques and Patterns

*   **Delayed Execution:** Using `GetTickCount64` to wait out security sweeps is a hallmark of professional malware intended to bypass automated "sandbox" analysis, where the sandbox might give up before the 60-second timer expires.
*   **Just-In-Time (JIT) Decryption:** By only decrypting components at the moment they are needed for use (e.g., just before a `WriteFile` or a jump), the malware minimizes its "memory footprint" of plain-text strings and malicious code.
*   **Complex Table Processing:** The repeated logic of checking indices, offsets, and then jumping to different blocks of code suggests the use of an **encrypted dispatch table**. This allows the developer to update the malware's functionality by simply changing a data table without changing the underlying execution engine.

---

### Summary Table of Indicators

| Feature | Technical Evidence | Significance |
| :--- | :--- | :--- |
| **Rootkit Target** | `NtLoadDriver`, `NtUnloadDriver` | Confirmed intent to move into Kernel Mode for maximum persistence. |
| **Payload Dropping** | "Driver image decrypted", `WriteFile` | Validates the binary as a primary loader/dropper for malicious drivers. |
| **Anti-Analysis Gap** | 60,000ms loop; "targets still running" check | Uses time delays to outwait security software processes. |
| **Sophisticated Obfuscation** | Nested loops in `fcn.140011664` & `fcn.140023b60` | Hides the logic flow from human and automated analysis tools. |
| **Environment Probing** | `GetUserNameW`, `GetComputerNameExW` | Identifies if the target is a specific machine or a sandbox environment. |
| **Custom Crypto/Math** | Bit-shift/Masking loops in `fcn.140023b60` | Indicates advanced methods for unpacking internal configurations. |

**Final Conclusion:** This is a highly professional, multi-stage malware loader designed to deploy a kernel-mode rootkit. It incorporates several layers of protection: **encryption** (to hide the payload), **obfuscation** (to hide the logic from analysts), and **timing/environmental checks** (to evade automated security systems). The presence of "wait" loops and specific checks for "still running" targets confirms it is designed to navigate complex, modern security environments.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The malware utilizes in-memory decryption, complex state-machine dispatching (fcn.140011664), and custom bitwise arithmetic to hide its logic flow and payload from automated analysis tools. |
| T1497 | Virtualization/Sandbox Evasion | The 60-second "waiting" loop (fcn.140006eb0) and environment fingerprinting (GetComputerNameExW, GetUserNameW) are specifically designed to bypass sandboxes and wait for security software to shut down. |
| T1068 | Exploitation for Privilege Escalation | The transition from a user-mode loader to a kernel-mode rootkit via `NtLoadDriver` indicates an intent to gain higher-level privileges and system-wide persistence. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*None identified.* (While "WriteFile" operations were noted in the behavior report, no specific hardcoded file paths or registry keys were present in the provided string dump.)

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts**
**Strings / Internal Status Messages:**
*   `Driver image decrypted` (Used as a status marker during payload processing)
*   `Some targets still running after 1 minute` (Used in the timing/evasion logic)

**Behavioral Patterns & Metadata:**
*   **Timing Evasion:** A hardcoded **60,000ms (1-minute)** sleep/wait loop used to bypass automated sandboxes and wait for antivirus services to shut down.
*   **Kernel Interaction:** Utilization of `NtLoadDriver` and `NtUnloadDriver` for rootkit functionality.
*   **Decryption Routine:** Use of complex bitwise shifts (`uVar16 = uVar8 | uVar16 << (iVar11 & 0x1f)`) in function `fcn.140023b60` indicating custom obfuscation for configuration or command decoding.
*   **Environmental Profiling:** Use of `GetEnvironmentVariableW`, `GetUserNameW`, and `GetComputerNameExW` to detect sandbox environments.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Multi-Stage Loading & Decryption:** The sample explicitly decrypts a "Driver image" in memory before writing it to disk, specifically intended for subsequent loading via `NtLoadDriver` to achieve kernel-mode persistence.
    *   **Advanced Evasion Tactics:** Use of significant time delays (60,000ms) and environmental fingerprinting (`GetUserNameW`, `GetComputerNameExW`) indicates a sophisticated attempt to outwait security software and bypass sandbox environments.
    *   **Complex Obfuscation:** The use of custom bitwise arithmetic and nested loops for state-machine dispatching highlights a deliberate effort to hide the execution path from automated analysis tools.
