# Threat Analysis Report

**Generated:** 2026-07-15 11:45 UTC
**Sample:** `06ca7ba51ae9961b1f4fe512f1e83f487f4c3ba8eda46a98ad0dd46c1f8f0399_06ca7ba51ae9961b1f4fe512f1e83f487f4c3ba8eda46a98ad0dd46c1f8f0399.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `06ca7ba51ae9961b1f4fe512f1e83f487f4c3ba8eda46a98ad0dd46c1f8f0399_06ca7ba51ae9961b1f4fe512f1e83f487f4c3ba8eda46a98ad0dd46c1f8f0399.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 209,976 bytes |
| MD5 | `025ac7621be8ba585b195906537b0c29` |
| SHA1 | `e6b5a1fecfcfea793ff2302ef605a82b180625f4` |
| SHA256 | `06ca7ba51ae9961b1f4fe512f1e83f487f4c3ba8eda46a98ad0dd46c1f8f0399` |
| Overall entropy | 6.621 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769374733 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 109,056 | 6.479 | No |
| `.rdata` | 50,176 | 5.03 | No |
| `.data` | 3,072 | 2.278 | No |
| `.pdata` | 6,144 | 5.188 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 512 | 4.718 | No |
| `.reloc` | 2,048 | 5.045 | No |

### Imports

**KERNEL32.dll**: `GetModuleHandleA`, `GetCurrentThread`, `LoadLibraryA`, `AddVectoredExceptionHandler`, `GetThreadContext`, `GetModuleHandleW`, `WriteFile`, `GetTickCount64`, `GetLastError`, `CreateFileA`, `WriteConsoleW`, `GetCurrentProcessId`, `ReadProcessMemory`, `GetProcAddress`, `GetWindowsDirectoryW`
**ADVAPI32.dll**: `CryptAcquireContextW`, `CryptCreateHash`, `CryptHashData`, `CryptDestroyHash`, `CryptGetHashParam`, `CryptReleaseContext`, `AllocateAndInitializeSid`, `FreeSid`, `CheckTokenMembership`, `RegCloseKey`, `RegQueryValueExA`, `RegCreateKeyExA`, `RegSetValueExA`, `RegOpenKeyExA`
**SHELL32.dll**: `SHGetFolderPathA`
**ole32.dll**: `CoInitializeEx`, `CoGetObject`, `CoCreateInstance`, `CoUninitialize`
**OLEAUT32.dll**: `VariantClear`, `SysAllocString`, `SysFreeString`, `VariantInit`
**WS2_32.dll**: `connect`, `htons`, `WSACleanup`, `closesocket`, `inet_pton`, `socket`, `recv`, `WSAStartup`, `setsockopt`, `send`

## Extracted Strings

Total strings found: **721** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
L$ SUVWH
t$ UWATAVAWH
A_A^A\_]
L$@u@f
L$ SWH
@USVWAVH
D9t$4v/
A^_^[]
@UVAVAWH
A_A^^]
@USVATH
UAVAWH
L$ SVWH
@UVWAWH
8A__^]
@SVATAUAVH
@A^A]A\^[
u0HcH<
8T$(ua
L$0tA
t$ WATAUAVAWH
~ND;t;
 A_A^A]A\_
WATAUAVAWH
A_A^A]A\_
x ATAVAWH
A_A^A\
H;XXs
H;xXu5
WATAUAVAWH
A_A^A]A\_
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
AUAVAWH
9{u	9{
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
L$pHcX
A_A^A]A\_^[]
@USVWATAUAVAWH
G0HcX
D$h;D$x
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
@USVWATAUAVAWH
A_A^A]A\_^[]
WAVAWH
 A_A^_
x ATAVAWH
 A_A^A\
WAVAWH
x ATAVAWH
9h@u(D93t#D9
D9uhL
9l$Pu	
A_A^A\
IH9BtEHcRI
@SVWATAUAVAWH
D$0HcH
pA_A^A]A\_^[
@SVWATAUAVAWH
A_A^A]A\_^[
A9	upA
B(I9A(u
A9	u;A
SVWATAUAVAWH
|$ Hc^
0A_A^A]A\_^[
SVWATAUAVAWH
A_A^A]A\_^[
UVWATAUAVAWH
F0Hcx
|$hHcX
 A_A^A]A\_^]
UVWATAUAVAWH
 A_A^A]A\_^]
D$ I;R
D$ I9P
WATAUAVAWH
 A_A^A]A\_
@USVWATAVAWH
A_A^A\_^[]
WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14000eb78` | `0x14000eb78` | 22635 | ✓ |
| `fcn.14000eb64` | `0x14000eb64` | 22594 | ✓ |
| `fcn.140010bd4` | `0x140010bd4` | 22443 | ✓ |
| `fcn.140016060` | `0x140016060` | 10985 | ✓ |
| `fcn.1400184c0` | `0x1400184c0` | 5271 | ✓ |
| `fcn.140014d4c` | `0x140014d4c` | 4735 | ✓ |
| `fcn.1400011a0` | `0x1400011a0` | 2416 | ✓ |
| `fcn.1400031c0` | `0x1400031c0` | 1971 | ✓ |
| `fcn.140012558` | `0x140012558` | 1829 | ✓ |
| `fcn.14001a820` | `0x14001a820` | 1661 | ✓ |
| `fcn.140018590` | `0x140018590` | 1451 | ✓ |
| `fcn.14000b624` | `0x14000b624` | 1336 | ✓ |
| `fcn.140007240` | `0x140007240` | 1335 | ✓ |
| `fcn.140006d50` | `0x140006d50` | 1263 | ✓ |
| `fcn.14000841c` | `0x14000841c` | 1245 | ✓ |
| `fcn.1400167ec` | `0x1400167ec` | 1171 | ✓ |
| `fcn.1400148c0` | `0x1400148c0` | 1164 | ✓ |
| `fcn.14000bb5c` | `0x14000bb5c` | 1133 | ✓ |
| `fcn.140002ab0` | `0x140002ab0` | 1067 | ✓ |
| `fcn.1400179e0` | `0x1400179e0` | 922 | ✓ |
| `fcn.14001a460` | `0x14001a460` | 920 | ✓ |
| `fcn.140017470` | `0x140017470` | 920 | ✓ |
| `fcn.14000f5d8` | `0x14000f5d8` | 915 | ✓ |
| `fcn.14000ac28` | `0x14000ac28` | 897 | ✓ |
| `fcn.14000afac` | `0x14000afac` | 871 | ✓ |
| `fcn.1400121f8` | `0x1400121f8` | 862 | ✓ |
| `fcn.140001db0` | `0x140001db0` | 835 | ✓ |
| `fcn.140017e34` | `0x140017e34` | 817 | ✓ |
| `fcn.140002780` | `0x140002780` | 816 | ✓ |
| `fcn.140017138` | `0x140017138` | 815 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400011a0.c`](code/fcn.1400011a0.c)
- [`code/fcn.140001db0.c`](code/fcn.140001db0.c)
- [`code/fcn.140002780.c`](code/fcn.140002780.c)
- [`code/fcn.140002ab0.c`](code/fcn.140002ab0.c)
- [`code/fcn.1400031c0.c`](code/fcn.1400031c0.c)
- [`code/fcn.140006d50.c`](code/fcn.140006d50.c)
- [`code/fcn.140007240.c`](code/fcn.140007240.c)
- [`code/fcn.14000841c.c`](code/fcn.14000841c.c)
- [`code/fcn.14000ac28.c`](code/fcn.14000ac28.c)
- [`code/fcn.14000afac.c`](code/fcn.14000afac.c)
- [`code/fcn.14000b624.c`](code/fcn.14000b624.c)
- [`code/fcn.14000bb5c.c`](code/fcn.14000bb5c.c)
- [`code/fcn.14000eb64.c`](code/fcn.14000eb64.c)
- [`code/fcn.14000eb78.c`](code/fcn.14000eb78.c)
- [`code/fcn.14000f5d8.c`](code/fcn.14000f5d8.c)
- [`code/fcn.140010bd4.c`](code/fcn.140010bd4.c)
- [`code/fcn.1400121f8.c`](code/fcn.1400121f8.c)
- [`code/fcn.140012558.c`](code/fcn.140012558.c)
- [`code/fcn.1400148c0.c`](code/fcn.1400148c0.c)
- [`code/fcn.140014d4c.c`](code/fcn.140014d4c.c)
- [`code/fcn.140016060.c`](code/fcn.140016060.c)
- [`code/fcn.1400167ec.c`](code/fcn.1400167ec.c)
- [`code/fcn.140017138.c`](code/fcn.140017138.c)
- [`code/fcn.140017470.c`](code/fcn.140017470.c)
- [`code/fcn.1400179e0.c`](code/fcn.1400179e0.c)
- [`code/fcn.140017e34.c`](code/fcn.140017e34.c)
- [`code/fcn.1400184c0.c`](code/fcn.1400184c0.c)
- [`code/fcn.140018590.c`](code/fcn.140018590.c)
- [`code/fcn.14001a460.c`](code/fcn.14001a460.c)
- [`code/fcn.14001a820.c`](code/fcn.14001a820.c)

## Behavioral Analysis

This updated analysis incorporates the final segment of the disassembly (chunk 3/3). The addition of these functions confirms that this malware is not only complex but also incorporates several advanced evasion, identification, and interactive features typical of high-end **Remote Access Trojans (RATs)** or **Spyware**.

---

### Updated Analysis of Functionality and Behavior

#### 1. Anti-Analysis & Stealth Techniques
The code block preceding `fcn.140017e34` reveals a sophisticated approach to system interrogation:
*   **Direct System Calls (via Dynamic Loading):** The malware uses `GetProcAddress` to resolve "Nt" prefixed functions like `NtQueryInformationProcess`. This is a classic evasion technique designed to bypass security software that hooks standard Win32 API calls. By calling the underlying Native API directly, the malware attempts to hide its activities from most Endpoint Detection and Response (EDR) systems.
*   **Process Environment Scrutiny:** The sequence of `NtQueryInformationProcess` followed by multiple `ReadProcessMemory` calls indicates that the malware is scanning for other processes, potentially looking for debuggers, sandboxes, or monitoring tools. It specifically targets memory regions to identify if it is being analyzed in a controlled environment.

#### 2. Unique Identifier (ID) Generation
In `fcn.14002780`, we see the implementation of:
*   **SHA-1 Hashing:** The use of `CryptAcquireContextW` and `CryptCreateHash(..., 0x80c)` (which specifies the SHA-1 algorithm) confirms that the malware is generating a unique hash. 
*   **Machine Fingerprinting:** This is likely used to generate a "Unique Machine ID." By hashing local system information or hardware IDs, the malware ensures that when it beacons back to the C2 server (`144.31.169.98`), the attacker knows exactly which machine they are interacting with, even if different machines are infected by the same sample.

#### 3. Execution Engine / VM State Management
The function `fcn.140017e34` is highly complex and serves as a core part of the internal logic:
*   **Complex Dispatching:** The sheer size of this function, combined with its use of internal pointers (like `uVar1 * 2 + 0x10`) and nested conditional checks, confirms it is a major component of the **VM Interpreter** identified in previous chunks. It manages how "instructions" are translated into actions.
*   **Memory Management:** The logic suggests it handles dynamic memory allocation for data received from the C2, ensuring that commands are correctly unpacked before being executed by the VM's dispatcher.

#### 4. Remote Terminal / Interaction Handling
The function `fcn.140017138` provides evidence of interactive features:
*   **Console Manipulation:** The calls to `GetConsoleMode` and the manual conversion of newline characters (LF to CRLF) strongly suggest a **Remote Shell** or **Command Prompt** feature.
*   **Input Processing:** This logic is used when an attacker wants to send commands to the victim's machine via the C2. The complexity indicates it handles various input types, potentially ensuring that commands are formatted correctly before being executed by the system shell.

---

### Updated Summary Table

| Feature | Observation | Risk Level | Analysis / Significance |
| :--- | :--- | :--- | :--- |
| **C2 Infrastructure** | Hardcoded IP `144.31.169.98` Port `1190`. | **Critical** | Direct communication with a known malicious host. |
| **VM Interpreter** | Complex dispatching and heavy use of internal offsets in `fcn.140017e34`. | **High** | Obscures the "real" payload; makes automated analysis nearly impossible. |
| **Anti-Analysis/Evasion** | Use of `NtQueryInformationProcess` via `GetProcAddress`. | **High** | Attempts to bypass EDR systems and identify debuggers or sandboxes. |
| **Machine Fingerprinting**| SHA-1 hashing (`CryptCreateHash`) for machine identification. | **Medium** | Used by the attacker to uniquely track each infected victim. |
| **Registry Persistence** | Interaction with `Software\SysMon`. | **High** | Likely used to maintain a presence on the system across reboots. |
| **File Discovery** | `FindFirstFileExW` and `FindNextFileW` loops. | **High** | Automated searching for sensitive documents or configuration files. |
| **Remote Interaction** | `GetConsoleMode` and manual CRLF processing in `fcn.140017138`. | **High** | Indicates a Remote Shell/Terminal capability for the attacker to issue commands. |

---

### Final Conclusion (Updated)

The addition of these final functions confirms that this is an extremely sophisticated, multi-functional malware agent. 

The binary's architecture follows a "Modular Loader" or **Remote Access Trojan (RAT)** design pattern:
1.  **Stealth Layer:** It uses Native API calls (`Nt...`) to evade detection and monitors the environment for security tools.
2.  **Identification Layer:** It generates unique fingerprints of the victim machine using SHA-1 hashing.
3.  **Obfuscation Layer (The VM):** The core functionality is "hidden" inside a custom Virtual Machine interpreter. This allows the attacker to change the malware's behavior by simply sending new bytecode from the server, rather than pushing out new binary files.
4.  **Interaction Layer:** It contains enough logic to provide an interactive shell for the attacker, allowing them to execute commands remotely on the infected host.

**Verdict:** The presence of a **VM-based interpreter**, **Anti-debugging techniques**, and **Remote Shell capabilities** classifies this as a high-tier threat (likely a professional RAT). It is designed for long-term persistence and complex remote manipulation of the victim's system.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The use of `GetProcAddress` to resolve "Nt" functions is intended to masquerade as standard system calls to bypass EDR hooks. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `NtQueryInformationProcess` specifically targets the identification of debuggers, sandboxes, and monitoring tools. |
| **T1082** | System Information Discovery | The implementation of SHA-1 hashing on system components to create a unique "Machine Fingerprint" identifies specific hardware/software details. |
| **T1027** | Obfuscated Files or Information | The use of a custom VM Interpreter hides the true logic of the malware and complicates static/dynamic analysis. |
| **T1547.001** | Registry Run Keys / Startup Folder | Interaction with `Software\SysMon` indicates an attempt to establish persistence via registry modifications. |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileExW` and `FindNextFileW` in loops indicates automated searching for sensitive data or configurations. |
| **T1059** | Command and Scripting Interpreter | The implementation of `GetConsoleMode` and CRLF processing provides the attacker with a functional remote shell/interactive command prompt. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `144.31.169.98` (Associated with Port `1190`)

**File paths / Registry keys**
*   `Software\SysMon` (Registry key associated with persistence)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified in the provided strings.

**Other artifacts**
*   **C2 Port:** `1190`
*   **Evasion Techniques:** Use of `NtQueryInformationProcess` via `GetProcAddress` to bypass EDR.
*   **Persistence/Detection:** Interaction with the `SysMon` registry key (often used to manipulate or hide from system monitoring).
*   **Behavioral Artifacts:** 
    *   Presence of a custom **VM Interpreter** for obfuscating payload execution.
    *   **Remote Shell capabilities** (identified via `GetConsoleMode` and CRLF processing).
    *   **Machine Fingerprinting** using SHA-1 hashing (`CryptCreateHash`).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**IP addresses:**
- `144.31.169.98`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT (Remote Access Trojan)
3. **Confidence**: High

**Key evidence**:
*   **VM-based Obfuscation:** The analysis identifies a complex "VM Interpreter" used to execute core logic as bytecode, which is a hallmark of sophisticated, high-end RATs designed to hide functionality from automated scanners.
*   **Interactive Remote Shell:** Evidence of `GetConsoleMode` and CRLF processing confirms the ability for an attacker to interact with the system via a command prompt/terminal.
*   **Advanced Evasion & Persistence:** The use of direct `Nt` system calls (via `GetProcAddress`) to bypass EDR hooks, combined with machine fingerprinting (SHA-1) and registry persistence, indicates a high-tier tool designed for long-term unauthorized access.
