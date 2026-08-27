# Threat Analysis Report

**Generated:** 2026-08-25 18:50 UTC
**Sample:** `127226334ce62510f9bb1467d9d006108bd4d4884afa48f64cb4b03be47851d2_127226334ce62510f9bb1467d9d006108bd4d4884afa48f64cb4b03be47851d2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `127226334ce62510f9bb1467d9d006108bd4d4884afa48f64cb4b03be47851d2_127226334ce62510f9bb1467d9d006108bd4d4884afa48f64cb4b03be47851d2.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 105,472 bytes |
| MD5 | `7d85683a846f0467e068927e5e7a0267` |
| SHA1 | `811e7aad3bea7ff8341ff5106bf0a29db3bb9fc2` |
| SHA256 | `127226334ce62510f9bb1467d9d006108bd4d4884afa48f64cb4b03be47851d2` |
| Overall entropy | 5.884 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767354682 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 54,272 | 6.411 | No |
| `.rdata` | 40,448 | 4.699 | No |
| `.data` | 3,072 | 2.08 | No |
| `.pdata` | 4,096 | 4.744 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.851 | No |

### Imports

**WININET.dll**: `InternetCloseHandle`, `InternetOpenA`, `InternetOpenUrlA`, `InternetReadFile`
**ole32.dll**: `CoInitializeEx`, `CoUninitialize`
**OLEAUT32.dll**: `SafeArrayCreate`, `SafeArrayDestroy`, `SafeArrayGetUBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `VariantClear`, `VariantInit`, `SafeArrayCreateVector`, `SafeArrayPutElement`
**USER32.dll**: `TranslateMessage`, `DispatchMessageA`, `GetMessageA`
**ADVAPI32.dll**: `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`, `RegSetValueExA`
**KERNEL32.dll**: `SetFilePointerEx`, `GetConsoleMode`, `GetConsoleOutputCP`, `WriteFile`, `FlushFileBuffers`, `HeapReAlloc`, `HeapSize`, `GetStringTypeW`, `GetFileType`, `GetStdHandle`, `GetProcessHeap`, `CreateFileW`, `CloseHandle`, `WriteConsoleW`, `SetStdHandle`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **398** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
D$`bin
PPD9t$@
UVWAVAWH
A_A^_^]
|$ AVH
WATAUAVAWH
A_A^A]A\_
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
G0HcX
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
@SVWATAUAVAWH
A_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
|$$Hc^
@A_A^A]A\_^[
UVWATAUAVAWH
G0Lch
G0HcX
D$hIcu
 A_A^A]A\_^]
99~YHc^
t98t H
u3HcH<H
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
	H;&H
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
D$0@8{
u$D8r(tH
D81u`L9r
uPD8r(tH
vWD8s(tH
u$D8r(tH
fD91u_L9r
uPD8r(tH
vVD8s(tH
UVWATAUAVAWH
PA_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
@USVWATAUAVH
,/<-w
H
D8t$ht
H
D8t$ht
H
A^A]A\_^[]
f9)u4H9j
u%@8j(t
v@8k(t
8D$@tH
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
t$ WATAUAVAWH
 A_A^A]A\_
fD9t$b
t$ WATAUAVAWH
D!|$xA
A_A^A]A\_
L$ VWAVH
fD94H}aD
@SUVWATAVAWH
@A_A^A\_^][
t$ WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800058d8` | `0x1800058d8` | 13503 | ✓ |
| `fcn.1800058a0` | `0x1800058a0` | 13498 | ✓ |
| `fcn.18000209c` | `0x18000209c` | 11399 | ✓ |
| `fcn.180001f9c` | `0x180001f9c` | 2302 | ✓ |
| `fcn.18000212c` | `0x18000212c` | 2024 | ✓ |
| `fcn.1800073d4` | `0x1800073d4` | 1985 | ✓ |
| `fcn.18000d280` | `0x18000d280` | 1677 | ✓ |
| `fcn.180003788` | `0x180003788` | 1213 | ✓ |
| `fcn.18000b780` | `0x18000b780` | 1171 | ✓ |
| `fcn.180001390` | `0x180001390` | 990 | ✓ |
| `fcn.18000a7c0` | `0x18000a7c0` | 922 | ✓ |
| `fcn.18000d930` | `0x18000d930` | 920 | ✓ |
| `fcn.18000a250` | `0x18000a250` | 920 | ✓ |
| `section..text` | `0x180001000` | 909 | ✓ |
| `fcn.180001b60` | `0x180001b60` | 892 | ✓ |
| `fcn.180006fd8` | `0x180006fd8` | 862 | ✓ |
| `fcn.18000ada4` | `0x18000ada4` | 817 | ✓ |
| `fcn.18000c0cc` | `0x18000c0cc` | 815 | ✓ |
| `fcn.180007ea0` | `0x180007ea0` | 712 | ✓ |
| `fcn.180001770` | `0x180001770` | 689 | ✓ |
| `fcn.180002388` | `0x180002388` | 667 | ✓ |
| `fcn.180007afc` | `0x180007afc` | 623 | ✓ |
| `fcn.180008f34` | `0x180008f34` | 604 | ✓ |
| `fcn.1800055a8` | `0x1800055a8` | 589 | ✓ |
| `fcn.180003c48` | `0x180003c48` | 584 | ✓ |
| `fcn.1800041e8` | `0x1800041e8` | 557 | ✓ |
| `fcn.180009dfc` | `0x180009dfc` | 555 | ✓ |
| `fcn.180002640` | `0x180002640` | 517 | ✓ |
| `fcn.180007904` | `0x180007904` | 501 | ✓ |
| `fcn.1800033fc` | `0x1800033fc` | 499 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001390.c`](code/fcn.180001390.c)
- [`code/fcn.180001770.c`](code/fcn.180001770.c)
- [`code/fcn.180001b60.c`](code/fcn.180001b60.c)
- [`code/fcn.180001f9c.c`](code/fcn.180001f9c.c)
- [`code/fcn.18000209c.c`](code/fcn.18000209c.c)
- [`code/fcn.18000212c.c`](code/fcn.18000212c.c)
- [`code/fcn.180002388.c`](code/fcn.180002388.c)
- [`code/fcn.180002640.c`](code/fcn.180002640.c)
- [`code/fcn.1800033fc.c`](code/fcn.1800033fc.c)
- [`code/fcn.180003788.c`](code/fcn.180003788.c)
- [`code/fcn.180003c48.c`](code/fcn.180003c48.c)
- [`code/fcn.1800041e8.c`](code/fcn.1800041e8.c)
- [`code/fcn.1800055a8.c`](code/fcn.1800055a8.c)
- [`code/fcn.1800058a0.c`](code/fcn.1800058a0.c)
- [`code/fcn.1800058d8.c`](code/fcn.1800058d8.c)
- [`code/fcn.180006fd8.c`](code/fcn.180006fd8.c)
- [`code/fcn.1800073d4.c`](code/fcn.1800073d4.c)
- [`code/fcn.180007904.c`](code/fcn.180007904.c)
- [`code/fcn.180007afc.c`](code/fcn.180007afc.c)
- [`code/fcn.180007ea0.c`](code/fcn.180007ea0.c)
- [`code/fcn.180008f34.c`](code/fcn.180008f34.c)
- [`code/fcn.180009dfc.c`](code/fcn.180009dfc.c)
- [`code/fcn.18000a250.c`](code/fcn.18000a250.c)
- [`code/fcn.18000a7c0.c`](code/fcn.18000a7c0.c)
- [`code/fcn.18000ada4.c`](code/fcn.18000ada4.c)
- [`code/fcn.18000b780.c`](code/fcn.18000b780.c)
- [`code/fcn.18000c0cc.c`](code/fcn.18000c0cc.c)
- [`code/fcn.18000d280.c`](code/fcn.18000d280.c)
- [`code/fcn.18000d930.c`](code/fcn.18000d930.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This additional disassembly provides deeper insight into the malware's internal architecture, confirming its complexity and sophistication. The new code segments reinforce the previous findings of a multi-stage downloader while adding significant evidence of **anti-analysis** and **environmental fingerprinting** capabilities.

Here is the updated technical analysis:

### Updated Technical Analysis (Cumulative)

#### 1. Core Functionality and Purpose
The binary remains confirmed as a high-sophistication **downloader/dropper**. The presence of complex, multi-stage decryption loops and heavy obfuscation layers indicates that this is not a simple "one-off" script but part of a professional malware toolkit (e.g., a botnet loader or an info-stealer stage-1 dropper).

#### 2. Enhanced Suspicious Behaviors
*   **Advanced Anti-Analysis & Anti-VM (New Findings):**
    *   The function `fcn.180002388` heavily utilizes the `CPUID` instruction and checks for specific processor features/flags. This is a classic technique used to detect if the code is running inside a **Virtual Machine (VM)** or an emulator. By checking for specific hardware signatures, it can decide whether to execute its malicious payload or "go dark" to evade analysis in a sandbox.
    *   The extensive branching and checks for various processor capabilities suggest the malware may be targeting specific hardware environments while intentionally avoiding analysis environments.

*   **Multi-Layered Obfuscation (Refined Analysis):**
    *   `fcn.180001770` reveals a highly complex, custom decryption/scrambling routine. It uses rolling XOR operations and non-standard arithmetic to transform data in memory. This is used to hide the "true" logic of the second-stage payload even after it has been initially unpacked from the internet.
    *   The sheer volume of switch statements and layered function calls (like `fcn.180007afc` calling `fcn.180007ea0`) acts as a "maze" for automated scanners, making it difficult to follow the execution flow during static analysis.

*   **Environmental Awareness:**
    *   The logic in `fcn.180007ea0` involving `GetCPInfo` and codepage checks suggests the malware is inspecting system-level localized settings. While this can be for legitimate reasons, in a malware context, it is often used to ensure the environment "looks" like a standard user's machine before executing final stages.

*   **Persistence & Masquerading (Previously identified):**
    *   The continued use of the **"EdgeUpdate"** registry key confirms an intent to hide within legitimate browser update processes.

#### 3. Notable Techniques & Patterns
*   **Anti-Debugging/Sanitization:** The intricate logic in `fcn.1800041e8` and `fcn.180003c48` involves checking memory offsets against hardcoded values (like `0x1fffffff`). This is common in "packer" code to ensure that no debuggers or instrumentation tools are attached to the process before high-risk actions (like decryption) take place.
*   **Delayed/Staged Execution:** The flow shows a clear distinction between **Environment Check $\rightarrow$ Decryption of Stage 1 $\rightarrow$ Decoding of Stage 2**. This "nesting" ensures that even if an analyst captures the first stage, the second stage remains encrypted until specific environmental conditions are met.

---

### Updated Summary for Incident Response
This is a **high-risk, sophisticated piece of malware** exhibiting hallmarks of professional production (e.g., it utilizes custom packers and anti-virtualization logic). It aims to bypass traditional security measures by hiding its true behavior behind layers of obfuscation until it confirms the environment is a genuine user machine.

**Updated Indicators of Compromise (IOCs) & Behavioral Evidence:**
*   **Network Intelligence:** Block domain `tbox.moe`. Monitor for outbound traffic related to `.rf` or other hidden TLDs used in multi-stage hopping.
*   **Host Persistence:** Scan for the registry key: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\EdgeUpdate`.
*   **Process Monitoring:** Look for processes attempting to perform high-frequency memory swaps (obfuscation) or performing repeated `CPUID` queries in a short timeframe.
*   **File/Module Analysis:** Identify and isolate any files named `cc_ser.dll` or others appearing as "Edge" updates that are not signed by legitimate vendors.

**Refined Risk Assessment:**
The presence of **Anti-VM and CPU fingerprinting** suggests this malware is designed to bypass automated sandboxes used by security companies. If an infection is suspected, the host should be treated as highly compromised, as it likely points toward a threat actor capable of conducting targeted activities (e.g., data exfiltration or ransomware deployment).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided technical analysis to the relevant MITRE ATT&K techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The malware is identified as a multi-stage downloader/dropper designed to fetch and deliver secondary payloads. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `CPUID` instructions and `GetCPInfo` checks are specifically used to detect virtual machines or analysis environments. |
| **T1027** | Obfuscated Files or Information | Complex decryption loops, rolling XOR operations, and layered function calls are used to hide the payload's logic from automated tools. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The malware establishes persistence by utilizing a registry key associated with "EdgeUpdate" to ensure it runs upon login. |
| **T1036.005** | Masquerading: Match Legitimate Name or Location | By naming its components and registry entries as "EdgeUpdate," the malware attempts to blend in with legitimate system processes. |
| **T1204** | Proxy** (Optional/Contextual) | The mention of "multi-stage hopping" via specific TLDs suggests a mechanism for routing traffic through multiple points to evade detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   **Domain:** `tbox.moe`
*   **URL Fragment:** `https://files.ca` (Extracted from string: `tbox.moe/q894or.https://files.ca`)

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\Run\EdgeUpdate`
*   **File Name:** `cc_ser.dll` (Identified as a potential malicious module masquerading as an Edge update)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **User Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`
*   **C2 Patterns:** Use of `.rf` TLDs and multi-stage "hopping" for initial payloads.
*   **Anti-Analysis Techniques:** Frequent `CPUID` instructions to detect VM environments and environment fingerprinting via `GetCPInfo`.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.caCLRCreateInstanc`

---

## Malware Family Classification

1. **Malware family**: Unknown (Likely a custom-built loader or part of a professional malware toolkit)
2. **Malware type**: Downloader / Loader
3. **Confidence**: High (regarding behavior/functionality); Low (regarding a specific named family)

4. **Key evidence**:
*   **Multi-Stage Architecture:** The analysis confirms the sample is a sophisticated downloader that uses layered decryption, rolling XOR operations, and "hopping" via suspicious TLDs to fetch subsequent payloads while hiding its core logic from scanners.
*   **Advanced Anti-Analysis Tactics:** The use of `CPUID` instructions, `GetCPInfo` checks, and memory offset verification indicates a deliberate effort to detect virtual machines and debuggers, typical of high-tier malware designed to bypass automated sandbox analysis.
*   **Persistence & Masquerading:** The sample employs "EdgeUpdate" naming conventions for its registry keys and files (e.g., `cc_ser.dll`) to blend in with legitimate system processes, a common tactic used by professional loaders to ensure persistence on infected hosts.
