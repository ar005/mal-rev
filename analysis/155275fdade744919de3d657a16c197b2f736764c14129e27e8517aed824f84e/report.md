# Threat Analysis Report

**Generated:** 2026-09-07 18:05 UTC
**Sample:** `155275fdade744919de3d657a16c197b2f736764c14129e27e8517aed824f84e_155275fdade744919de3d657a16c197b2f736764c14129e27e8517aed824f84e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `155275fdade744919de3d657a16c197b2f736764c14129e27e8517aed824f84e_155275fdade744919de3d657a16c197b2f736764c14129e27e8517aed824f84e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 448,000 bytes |
| MD5 | `37118d432b7fa6f74e877563b361ec7f` |
| SHA1 | `5fc4b4eb87039d3e4bdc1f9dab1ff8cfc9e0c77a` |
| SHA256 | `155275fdade744919de3d657a16c197b2f736764c14129e27e8517aed824f84e` |
| Overall entropy | 5.857 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1763097219 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 382,976 | 5.717 | No |
| `.rdata` | 6,656 | 5.716 | No |
| `.data` | 22,016 | 3.663 | No |
| `.pdata` | 27,136 | 4.945 | No |
| `.rsrc` | 2,560 | 4.175 | No |
| `.reloc` | 5,632 | 5.425 | No |

### Imports

**USER32.dll**: `GetSystemMetrics`, `ReleaseDC`, `RegisterClassExW`, `UpdateWindow`, `GetDC`, `ShowWindow`, `CreateWindowExW`, `DestroyWindow`
**GDI32.dll**: `CreateCompatibleBitmap`, `CreateCompatibleDC`, `SelectObject`, `DeleteDC`, `DeleteObject`
**SHELL32.dll**: `SHGetKnownFolderPath`, `SHGetFolderPathW`
**ADVAPI32.dll**: `RegQueryValueExW`, `RegOpenKeyExW`, `RegCloseKey`
**ole32.dll**: `CoCreateInstance`, `CoUninitialize`, `CoInitializeEx`

### Exports

`DllRegisterServer`, `Start`

## Extracted Strings

Total strings found: **1465** (showing first 100)

```
!This program requires Microsoft Window.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
UWATAVAWH
A_A^A\_]
H3D$XH
D$$9D$ sD
H3D$`H
WAVAWH
 A_A^_
@UVATAUAWH
A_A]A\^]
UWATAVAWH
E3:iY
f
A_A^A\_]
UVWATAUAVAWH
`A_A^A]A\_^]
UATAVAWH
XA_A^A\]
|$ ATAVAWH
 A_A^A\
t$ WATAUAVAWL
t$HA_A^A]A\_
)|$pfA
L$0fff
l$ VWAVH
|$ ATAVAW
|$8A_A^A\
|$ AVH
\$ UVWAVAWH
fD9=bX
D$@{tD
D$A"id"
fE9<Du
D$A"hos
D$Etnam
D$Ie":"
A_A^_^]
|$ AVH
fD956U
fF94Cu
|$ AVH
\$ UVWAVAWH
fD9&t
A
fF9<fu
pA_A^_^]
VWATAVAWH
A_A^A\_^
@UWATH
fD9d$ptA
fF9d|pu
fD9dt u
USVATAUAVAWH
|$xfA9G
A_A^A]A\^[]
UAVAWH
D0fD9<Wu
L$ SUVWATH
PA\_^][
PA\_^][
t$ WATAWH
UWATAVH
A^A\_]
fA9>t

A^A\_]
D$(9D$
D$ 5QsF8
D$(9D$
D$(9D$
HcD$H
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$H9D$
D$(9D$
D$89D$
D$(9D$
D$(9D$
D$H9D$
D$(9D$
D$H9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
D$(9D$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.18000ab20` | `0x18000ab20` | 2477 | ✓ |
| `sym.loader.dll_DllRegisterServer` | `0x180001020` | 1918 | ✓ |
| `fcn.180009e40` | `0x180009e40` | 1661 | ✓ |
| `fcn.18000a4c0` | `0x18000a4c0` | 1629 | ✓ |
| `fcn.180003d90` | `0x180003d90` | 1624 | ✓ |
| `fcn.1800045c0` | `0x1800045c0` | 1460 | ✓ |
| `fcn.180009070` | `0x180009070` | 1282 | ✓ |
| `fcn.180003270` | `0x180003270` | 1180 | ✓ |
| `fcn.180002500` | `0x180002500` | 1101 | ✓ |
| `fcn.180001d30` | `0x180001d30` | 1055 | ✓ |
| `fcn.180003710` | `0x180003710` | 1040 | ✓ |
| `fcn.180006860` | `0x180006860` | 932 | ✓ |
| `fcn.180006cc0` | `0x180006cc0` | 884 | ✓ |
| `fcn.180009880` | `0x180009880` | 793 | ✓ |
| `fcn.180001830` | `0x180001830` | 712 | ✓ |
| `fcn.180004b80` | `0x180004b80` | 669 | ✓ |
| `fcn.180009bd0` | `0x180009bd0` | 622 | ✓ |
| `fcn.180003b20` | `0x180003b20` | 616 | ✓ |
| `fcn.180009580` | `0x180009580` | 535 | ✓ |
| `fcn.180005020` | `0x180005020` | 479 | ✓ |
| `fcn.180002320` | `0x180002320` | 471 | ✓ |
| `fcn.180002150` | `0x180002150` | 461 | ✓ |
| `fcn.1800043f0` | `0x1800043f0` | 458 | ✓ |
| `fcn.18000b670` | `0x18000b670` | 412 | ✓ |
| `fcn.180007120` | `0x180007120` | 399 | ✓ |
| `fcn.180004ee0` | `0x180004ee0` | 250 | ✓ |
| `fcn.180002950` | `0x180002950` | 247 | ✓ |
| `fcn.180001c40` | `0x180001c40` | 239 | ✓ |
| `fcn.1800097a0` | `0x1800097a0` | 224 | ✓ |
| `fcn.18000b810` | `0x18000b810` | 222 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001830.c`](code/fcn.180001830.c)
- [`code/fcn.180001c40.c`](code/fcn.180001c40.c)
- [`code/fcn.180001d30.c`](code/fcn.180001d30.c)
- [`code/fcn.180002150.c`](code/fcn.180002150.c)
- [`code/fcn.180002320.c`](code/fcn.180002320.c)
- [`code/fcn.180002500.c`](code/fcn.180002500.c)
- [`code/fcn.180002950.c`](code/fcn.180002950.c)
- [`code/fcn.180003270.c`](code/fcn.180003270.c)
- [`code/fcn.180003710.c`](code/fcn.180003710.c)
- [`code/fcn.180003b20.c`](code/fcn.180003b20.c)
- [`code/fcn.180003d90.c`](code/fcn.180003d90.c)
- [`code/fcn.1800043f0.c`](code/fcn.1800043f0.c)
- [`code/fcn.1800045c0.c`](code/fcn.1800045c0.c)
- [`code/fcn.180004b80.c`](code/fcn.180004b80.c)
- [`code/fcn.180004ee0.c`](code/fcn.180004ee0.c)
- [`code/fcn.180005020.c`](code/fcn.180005020.c)
- [`code/fcn.180006860.c`](code/fcn.180006860.c)
- [`code/fcn.180006cc0.c`](code/fcn.180006cc0.c)
- [`code/fcn.180007120.c`](code/fcn.180007120.c)
- [`code/fcn.180009070.c`](code/fcn.180009070.c)
- [`code/fcn.180009580.c`](code/fcn.180009580.c)
- [`code/fcn.1800097a0.c`](code/fcn.1800097a0.c)
- [`code/fcn.180009880.c`](code/fcn.180009880.c)
- [`code/fcn.180009bd0.c`](code/fcn.180009bd0.c)
- [`code/fcn.180009e40.c`](code/fcn.180009e40.c)
- [`code/fcn.18000a4c0.c`](code/fcn.18000a4c0.c)
- [`code/fcn.18000ab20.c`](code/fcn.18000ab20.c)
- [`code/fcn.18000b670.c`](code/fcn.18000b670.c)
- [`code/fcn.18000b810.c`](code/fcn.18000b810.c)
- [`code/sym.loader.dll_DllRegisterServer.c`](code/sym.loader.dll_DllRegisterServer.c)

## Behavioral Analysis

Based on the second portion of disassembly, your analysis of this binary as a sophisticated multi-state loader is confirmed and significantly deepened. This new data reveals specific implementation techniques for **API Hashing**, **Dispatch Tables**, and **Environment Discovery**.

The updated analysis integrates your previous findings with the new evidence:

### Updated Core Functionality & Purpose
The binary is confirmed to be a **sophisticated, multi-stage loader/dropper**. 
*   **Dispatcher Architecture:** The snippet at the beginning of chunk 2 shows a "Dispatch Table" pattern. Instead of calling functions directly, it iterates through an array of function pointers (`uVar3 < *0x180066980`). This allows the malware to hide its true capabilities by wrapping them in a generic execution loop.
*   **Environment Awareness:** The inclusion of `fcn.18000b810` shows the binary actively probes the system for information (e.g., `ProgramFilesDir`). This suggests it is preparing to drop additional payloads into specific system directories or determining where to place its components to ensure persistence.

### Updated Suspicious & Malicious Behaviors
*   **Advanced API Hashing (New):** The function `fcn.180001c40` contains a classic "Rolling Hash" algorithm (`((uVar4 >> 3 | uVar4 << 0x1d) ^ uVar1) * 0xbeef3`). This is used to resolve Windows API addresses at runtime by hashing the names of the functions. By doing this, the malware ensures that standard analysis tools cannot see which APIs (like `CreateProcess`, `WriteProcessMemory`, etc.) it uses until it is actually running.
*   **System Path Enumeration:** The code specifically looks for `ProgramFilesDir` using `RegOpenKeyExW`. While this can be done by legitimate programs, in a loader with heavy obfuscation and SIMD-based string decryption, it is a major red flag for identifying paths to inject files or establish persistence.
*   **Large Buffer Management:** Function `fcn.1800097a0` manages large memory blocks (e.g., `0x40000`). This suggests the loader handles substantial amounts of decrypted data, likely the "payload" that follows the initial decryption stages.

### Updated Techniques & Patterns
*   **SIMD-Accelerated Decryption (Existing):** Retained from previous analysis; confirms high-level evasion techniques to hide strings/IPs.
*   **Dispatch Table Obfuscation (Enhanced):** The loop `uVar4 = (*pcVar1)(arg2,arg3,arg4,in_stack_00000028)` demonstrates that the loader uses an internal jump table. This makes it difficult for analysts to follow the "control flow" of the program because the next step in the execution is determined at runtime.
*   **Hash-Based Resolver (New):** The constant `0xbeef3` used in a bitwise rotation/shift loop is a hallmark of malware designed to evade static analysis by hiding its Import Address Table (IAT). 
*   **Fallback Logic:** The logic in `fcn.18000b810` that checks for `SHGetFolderPathW` and falls back to registry keys if it fails shows a high level of "robustness," ensuring the malware can find its necessary paths regardless of the OS configuration.

### Summary for Incident Response
This binary is a **high-threat, advanced packer/loader.** It utilizes several "pro" techniques intended to bypass automated sandboxes and manual analysis:

1.  **Anti-Analysis:** It hides its API calls using custom hashing algorithms (mitigating static detection of malicious imports).
2.  **Control Flow Flattening:** It uses a dispatcher loop to hide the true progression of its internal tasks.
3.  **Persistence/Delivery Preparation:** It actively queries the system for common installation paths, indicating it is likely a precursor to a dropper or an injector.

**Revised Recommendations:**
*   **Dynamic Analysis Required:** Since much of the "malicious" behavior (like specific URLs or file paths) is hidden behind SIMD de-obfuscation and API hashing, static analysis will only show the *loader*. You must run this in a sandbox to capture it at the moment it resolves its hashes and decodes its final strings.
*   **Monitor for Registry/File Changes:** Specifically monitor for interactions with `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion` as the binary is specifically looking for system directories.
*   **Memory Forensics:** Perform a memory dump once the "Dispatch Loop" has finished running to see the final, de-obfuscated code in memory.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of API Hashing, SIMD-accelerated decryption, and Dispatch Tables (Control Flow Flattening) are employed to hide the malware's true functionality and intent from static analysis. |
| **T1083** | File and Directory Discovery | The binary actively probes the system for `ProgramFilesDir` via registry keys and fallback logic to identify valid locations for staging or installing payloads. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Because the malware uses **SIMD-based string decryption** and **API hashing**, much of the primary malicious infrastructure (IPs, URLs) remains encrypted in the static strings. However, several high-fidelity indicators and behavioral artifacts were identified.

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.* (Note: Analysis indicates these are currently hidden behind SIMD decryption and will only be visible during dynamic analysis/memory forensics).

**File paths / Registry keys**
*   `ProgramFilesDir` (Targeted via `RegOpenKeyExW`)
*   `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion` (Specifically targeted for persistence/path discovery)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `0xbeef3` (Note: This is not a file hash, but the specific **constant used in the Rolling Hash algorithm** to resolve APIs at runtime).

**Other artifacts**
*   **API Hashing Constant:** `0xbeef3` (Used in a bitwise rotation/shift loop: `((uVar4 >> 3 | uVar4 << 0x1d) ^ uVar1) * 0xbeef3`)
*   **Memory Allocation Buffer:** `0x40000` (Size of the buffer used to hold decrypted payload data).
*   **Internal Function Offsets (Potential entry points/jump targets):**
    *   `0x180066980` (Dispatch Table)
    *   `0x18000b810` (Environment Discovery / `SHGetFolderPathW` check)
    *   `0x180001c40` (Rolling Hash Resolver)
    *   `0x1800097a0` (Buffer Management)
*   **Tactic/Technique Identifiers:** 
    *   "Dispatch Table" execution flow.
    *   "SIMD-Accelerated Decryption".
    *   "Control Flow Flattening".

---

### **Analyst Notes for Incident Response**
The presence of the `0xbeef3` hash constant and the "Dispatch Table" architecture confirms this is a sophisticated loader designed to evade static detection. Since the strings provided in the raw dump are heavily obfuscated (e.g., `D$(9D$`, `UWATAVAWH`), **no network infrastructure can be blocked based on this data alone.** 

**Recommended Actions:**
1.  **Memory Forensics:** Execute the sample in a controlled environment and perform a memory dump after the "Dispatch Loop" has completed to capture decrypted strings (IPs, URLs, and file paths).
2.  **SIEM Alerting:** Create alerts for any unauthorized processes attempting to access `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion` or unusually large memory allocations (`0x40000`) followed by network activity.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Anti-Analysis Techniques:** The sample utilizes complex "Rolling Hash" algorithms (constant `0xbeef3`) to resolve APIs at runtime and a "Dispatch Table" architecture to flatten control flow, specifically designed to evade static analysis.
*   **Multi-Stage Delivery Design:** Large memory buffer management (`0x40000`) combined with environment discovery (searching for `ProgramFilesDir` via registry keys) confirms its role as a precursor intended to host and decrypt subsequent payloads.
*   **Sophisticated Obfuscation:** The use of SIMD-accelerated decryption and hidden Import Address Tables (IAT) indicates a high level of development aimed at hiding infrastructure (IPs/URLs) until execution.
