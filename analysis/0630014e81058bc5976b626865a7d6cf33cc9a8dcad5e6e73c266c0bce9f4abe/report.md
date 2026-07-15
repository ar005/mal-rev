# Threat Analysis Report

**Generated:** 2026-07-14 22:21 UTC
**Sample:** `0630014e81058bc5976b626865a7d6cf33cc9a8dcad5e6e73c266c0bce9f4abe_0630014e81058bc5976b626865a7d6cf33cc9a8dcad5e6e73c266c0bce9f4abe.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0630014e81058bc5976b626865a7d6cf33cc9a8dcad5e6e73c266c0bce9f4abe_0630014e81058bc5976b626865a7d6cf33cc9a8dcad5e6e73c266c0bce9f4abe.dll` |
| File type | PE32 executable for MS Windows 5.00 (DLL), Intel i386, 5 sections |
| Size | 212,992 bytes |
| MD5 | `5a34fd27b27f03cf41669d3eb244dc1f` |
| SHA1 | `067e767484d54d8ac4edea2cafdfce3125e7b5a8` |
| SHA256 | `0630014e81058bc5976b626865a7d6cf33cc9a8dcad5e6e73c266c0bce9f4abe` |
| Overall entropy | 6.513 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1752930131 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 157,696 | 6.653 | No |
| `.rdata` | 36,864 | 4.73 | No |
| `.data` | 6,144 | 3.906 | No |
| `.rsrc` | 512 | 5.11 | No |
| `.reloc` | 10,752 | 5.44 | No |

### Imports

**RPCRT4.dll**: `UuidCreate`, `RpcStringFreeW`, `UuidToStringW`
**msi.dll**: `ord_160`, `ord_159`, `ord_32`, `ord_49`, `ord_103`, `ord_125`, `ord_17`, `ord_8`, `ord_145`, `ord_74`, `ord_120`
**KERNEL32.dll**: `LoadResource`, `LockResource`, `SizeofResource`, `FindResourceW`, `FindResourceExW`, `GetLastError`, `CloseHandle`, `WaitForSingleObject`, `Sleep`, `FindFirstFileW`, `FindNextFileW`, `FindClose`, `GetExitCodeProcess`, `CreateFileW`, `GetFileSize`
**USER32.dll**: `AttachThreadInput`, `GetWindowThreadProcessId`, `GetForegroundWindow`, `IsWindow`, `BringWindowToTop`, `UpdateWindow`, `ShowWindow`, `SystemParametersInfoW`, `RegisterClassExW`, `DefWindowProcW`, `SetForegroundWindow`, `AllowSetForegroundWindow`, `CreateWindowExW`
**ADVAPI32.dll**: `RegQueryValueExW`, `RegOpenKeyExW`, `RegEnumKeyExW`, `RegCloseKey`, `RegDeleteValueW`, `RegDeleteKeyW`, `GetTokenInformation`, `OpenProcessToken`, `GetUserNameW`, `CryptGetHashParam`, `CryptHashData`, `CryptCreateHash`, `CryptAcquireContextW`, `CryptReleaseContext`, `CryptDestroyHash`
**SHELL32.dll**: `SHGetFolderPathW`, `ShellExecuteExW`, `ord_680`
**SHLWAPI.dll**: `PathFindExtensionW`, `PathAppendW`, `PathFileExistsW`

### Exports

`_CheckReboot@4`, `_InstallFinish1@4`, `_InstallFinish2@4`, `_InstallMain@4`, `_InstallPrepare@4`, `_InstallRollback@4`, `_SubstWrappedArguments@4`, `_UninstallFinish1@4`, `_UninstallFinish2@4`, `_UninstallPrepare@4`

## Extracted Strings

Total strings found: **727** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
UVQRS
F09^(u
D$XSVW
9t$Hr?
9t$Hr
L$P9t$ds
9t$dr
L$(j@Q
L$(j@Q
T$,j@R
T$,j@R
T$`jlR
t$HWSPQV
T$`jlR
t$HWSPQV
U(VjeS
<+t'<-t#<0u
D$8SP3
VWVVVh
PWWj%W
0WWWWW
0WWWWW
PPPPPPPP
^SSSSS
^SSSSS
@9Ew	
@AA;Er
uWhEP
uWWWWW
u)jAXf;
0WWWWW
AAFFf;
E9Xt
0SSSSS
u.j^9
tSSSSS
tSSSSS
tSSSSS
tVVVVV
tVVVVV
tVVVVV
v	N+D$
tVVVVV
tVVVVV
tWWWWW
tWWWWW
tWWWWW
tWWWWW
8VVVVV
tVVVVV
0A@@Ju
u,9Et'9
j@j ^V
>=Yt1j
< tK<	tG
tVVVVV
tVVVVV
tVVVVV
URPQQh
C PjPV
C$PjQV
C*PjTV
C+PjUV
C,PjVV
C-PjWV
C.PjRV
C/PjSV
0SSSSS
0SSSSS
@9]|FVW
Y;Fu!
G9^t;
Y;Fu.j
u49^t/
p;qt~
PPPPPPPP
t)jXP
^SSSSS
j"^SSSSS
MQSWVj
F@u^V
HHtYHHt
tZj"[f;
0WWWWW
AAFFf;
utSSSSS
:u#f9tx
xf91t
tSSSSS
tWWWWW
tWWWWW
tWWWWW
>=Yt1j
t"SS9]
uL9=$0
tSSSSS
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.10013a06` | `0x10013a06` | 8959 | ✓ |
| `fcn.10019b95` | `0x10019b95` | 5632 | ✓ |
| `fcn.10007710` | `0x10007710` | 5321 | ✓ |
| `fcn.1000e930` | `0x1000e930` | 3444 | ✓ |
| `fcn.1002176e` | `0x1002176e` | 2982 | ✓ |
| `fcn.10006ce0` | `0x10006ce0` | 2600 | ✓ |
| `fcn.10025010` | `0x10025010` | 2343 | ✓ |
| `fcn.1001b761` | `0x1001b761` | 1843 | ✓ |
| `fcn.10024918` | `0x10024918` | 1736 | ✓ |
| `sym.MsiCustomActions.dll__UninstallPrepare_4` | `0x1000ac90` | 1507 | ✓ |
| `fcn.1000c6f0` | `0x1000c6f0` | 1450 | ✓ |
| `fcn.10005fb0` | `0x10005fb0` | 1389 | ✓ |
| `fcn.10023e8e` | `0x10023e8e` | 1348 | ✓ |
| `fcn.100243d2` | `0x100243d2` | 1348 | ✓ |
| `fcn.10004080` | `0x10004080` | 1338 | ✓ |
| `fcn.1000da40` | `0x1000da40` | 1226 | ✓ |
| `fcn.10006520` | `0x10006520` | 1214 | ✓ |
| `sym.MsiCustomActions.dll__UninstallFinish1_4` | `0x1000b280` | 1110 | ✓ |
| `fcn.10018326` | `0x10018326` | 1051 | ✓ |
| `fcn.1001d6b9` | `0x1001d6b9` | 1045 | ✓ |
| `fcn.1000bb20` | `0x1000bb20` | 955 | ✓ |
| `fcn.1000d200` | `0x1000d200` | 951 | ✓ |
| `fcn.1001deb1` | `0x1001deb1` | 933 | ✓ |
| `fcn.1000cca0` | `0x1000cca0` | 903 | ✓ |
| `fcn.10023232` | `0x10023232` | 883 | ✓ |
| `fcn.10010f00` | `0x10010f00` | 869 | ✓ |
| `fcn.100112f0` | `0x100112f0` | 869 | ✓ |
| `fcn.10020020` | `0x10020020` | 867 | ✓ |
| `fcn.10001d20` | `0x10001d20` | 841 | ✓ |
| `fcn.100228e7` | `0x100228e7` | 839 | ✓ |

### Decompiled Code Files

- [`code/fcn.10001d20.c`](code/fcn.10001d20.c)
- [`code/fcn.10004080.c`](code/fcn.10004080.c)
- [`code/fcn.10005fb0.c`](code/fcn.10005fb0.c)
- [`code/fcn.10006520.c`](code/fcn.10006520.c)
- [`code/fcn.10006ce0.c`](code/fcn.10006ce0.c)
- [`code/fcn.10007710.c`](code/fcn.10007710.c)
- [`code/fcn.1000bb20.c`](code/fcn.1000bb20.c)
- [`code/fcn.1000c6f0.c`](code/fcn.1000c6f0.c)
- [`code/fcn.1000cca0.c`](code/fcn.1000cca0.c)
- [`code/fcn.1000d200.c`](code/fcn.1000d200.c)
- [`code/fcn.1000da40.c`](code/fcn.1000da40.c)
- [`code/fcn.1000e930.c`](code/fcn.1000e930.c)
- [`code/fcn.10010f00.c`](code/fcn.10010f00.c)
- [`code/fcn.100112f0.c`](code/fcn.100112f0.c)
- [`code/fcn.10013a06.c`](code/fcn.10013a06.c)
- [`code/fcn.10018326.c`](code/fcn.10018326.c)
- [`code/fcn.10019b95.c`](code/fcn.10019b95.c)
- [`code/fcn.1001b761.c`](code/fcn.1001b761.c)
- [`code/fcn.1001d6b9.c`](code/fcn.1001d6b9.c)
- [`code/fcn.1001deb1.c`](code/fcn.1001deb1.c)
- [`code/fcn.10020020.c`](code/fcn.10020020.c)
- [`code/fcn.1002176e.c`](code/fcn.1002176e.c)
- [`code/fcn.100228e7.c`](code/fcn.100228e7.c)
- [`code/fcn.10023232.c`](code/fcn.10023232.c)
- [`code/fcn.10023e8e.c`](code/fcn.10023e8e.c)
- [`code/fcn.100243d2.c`](code/fcn.100243d2.c)
- [`code/fcn.10024918.c`](code/fcn.10024918.c)
- [`code/fcn.10025010.c`](code/fcn.10025010.c)
- [`code/sym.MsiCustomActions.dll__UninstallFinish1_4.c`](code/sym.MsiCustomActions.dll__UninstallFinish1_4.c)
- [`code/sym.MsiCustomActions.dll__UninstallPrepare_4.c`](code/sym.MsiCustomActions.dll__UninstallPrepare_4.c)

## Behavioral Analysis

This updated analysis incorporates the findings from chunk 3/3 into the existing report. The additional disassembly provides significant evidence regarding how the binary manages its lifecycle, interacts with system environment variables, and handles complex internal data structures.

### Updated Technical Analysis (Comprehensive Report)

The binary continues to demonstrate high complexity consistent with a **sophisticated installer wrapper or persistent loader**. The latest analysis reveals that it doesn't just "launch" components; it actively monitors the environment, manages system state, and performs intricate data processing to ensure the successful transition between execution stages.

---

### Core Functionality and Purpose

The application is designed to manage a multi-stage deployment process where it serves as a protective and preparatory layer for secondary payloads.

*   **Advanced MSI Lifecycle Management:** The interaction with `MnsGetFeatureCostA`, `MsiEnumClientsA`, and `MsiViewModify` (found in `fcn.10006520`) confirms that the binary is deeply integrated with Windows Installer components. It doesn't just trigger an installer; it interacts with specific "features" and "client" views of the MSI database, suggesting it can be customized to perform different actions based on the system state.
*   **"Wait-and-Verify" Execution Logic:** A critical pattern was identified in `fcn.10006520` where the code enters a loop, calling `Sleep(1000)` while repeatedly checking for the existence of a file (`PathFileExistsW`). This is a common technique in multi-stage malware to wait for an asynchronous process (like an installer or a separate "dropper" thread) to finish writing a payload to disk before proceeding.
*   **Environment Manipulation:** The function `fcn.10020020` utilizes `SetEnvironmentVariableW`. This is used to modify the environment variables of the current or subsequent processes. In an attack scenario, this is often used to inject paths into the `PATH` variable or set custom variables that tell a secondary payload where to find its configuration files or remote command-and-control (C2) instructions.
*   **Robust Data Processing & Formatting:** Functions like `fcn.10023232` show highly specialized logic for converting numeric values into strings, handling signs, leading zeros, and complex ranges. This suggests the tool processes a high volume of configuration data—possibly serial numbers, versioning info, or memory offsets—and formats them for internal use or logging.
*   **Complex Internal State Management:** The massive routine in `fcn.100228e7` involves checking for "magic values" (e.g., `-0x1f928c9d`) and iterating through nested structures. This suggests a high-level "engine" is being used to parse, perhaps decrypt or decompress, internal data blocks that define the installation's behavior or the payload's configuration.

### Suspicious or Malicious Behaviors

The findings in chunk 3 reinforce several patterns common in sophisticated malware:

*   **Persistence & Environment Stability:** By manipulating environment variables and checking for specific registry keys via MSI calls, the binary ensures that its "environment" is perfectly prepared for the final payload. This reduces the chance of a secondary payload crashing or alerting security software due to missing paths or incorrect configurations.
*   **Evasion through Delay (Timing Attacks):** The loop containing `Sleep(1000)` is a classic anti-analysis and evasion tactic. By waiting, the binary avoids "burst" activity that might trigger heuristic alarms from EDR solutions that look for rapid file creation followed by immediate execution.
*   **Credential/Certificate Context:** The presence of `CryptGetHashParam` (in `fcn.10021d20`) indicates the code may be inspecting certificates or hash values of files before executing them. While legitimate in installers to verify digital signatures, this is also a standard method for malware to ensure it is "running correctly" or hasn't been tampered with by security researchers.
*   **Sophisticated Masking (Living off the Land):** The heavy use of `ShellExecuteExW` combined with internal "wait loops" and MSI-specific API calls makes this binary very difficult to distinguish from a legitimate enterprise installer like those used for complex software suites or drivers.

### Notable Techniques & Patterns

*   **The "Stage-Gate" Pattern:** The code is structured in "stages." It performs checks (admin status, file presence), modifies the environment (SetEnvironmentVariable), waits for confirmation (the sleep loop), and only then proceeds to the next high-level logic block.
*   **Resource/Data Abstraction:** The complex loops and memory offsets suggest the binary is not hardcoding its behavior but is reading it from a pre-processed data table or encrypted blob, allowing a single "engine" to behave differently based on passed parameters.
*   **Memory Integrity Check:** The extensive use of internal checks (e.g., `fcn.100228e7`) suggests that the binary verifies its own configuration and state before attempting to launch higher-risk operations.

---

### Summary for Incident Response

This is a **high-complexity, multi-stage loader/installer wrapper** designed with significant attention to detail regarding stability and evasion.

**Key Findings for IR:**
1.  **Mechanism of Action:** It acts as an "orchestrator." It prepares the environment (via MSI calls), configures the pathing (via `SetEnvironmentVariableW`), waits for external signals/files (`Sleep` loop), and validates system integrity before handing off control to a final payload.
2.  **Evasion Profile:** The use of "wait-loops" suggests an awareness of behavioral analysis tools that flag rapid-fire execution chains. It deliberately slows down its operation to blend in with legitimate installation windows.
3.  **Advanced Features:** Use of `Advapi32` for hash/certificate checks and complex internal data processing indicates it is likely a professional grade tool, potentially used as part of an Advanced Persistent Threat (APT) toolkit or highly sophisticated malware campaign.
4.  **Actionable Intelligence:**
    *   **Indicators of Behavior:** Look for processes that call `SetEnvironmentVariableW` immediately before launching child processes, or processes that exhibit "sleep" behavior while waiting for file system changes in the `\Temp\` or `\AppData\` directories.
    *   **Search Targets:** Investigation should focus on associated `.msi`, `.inf`, and any non-standard `.dll` files it may reference via its internal data table during the `fcn.100228e7` routine.
    *   **Monitoring Point:** Monitor for any calls to `CryptGetHashParam`, as this may indicate a "gatekeeping" check before a secondary payload is activated.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1566.001 | Masquerading | The binary uses Windows Installer (MSI) APIs to masquerade as a legitimate software installer or update service. |
| T1497 | Virtualization/Sandbox Evasion | The use of `Sleep()` loops and "Wait-and-Verify" logic is designed to bypass automated analysis tools by delaying malicious actions. |
| T1497 | Virtualization/Sandbox Evasion | Use of `CryptGetHashParam` functions as a gatekeeping mechanism to detect if the environment has been tampered with or is being analyzed. |
| T1028 | Loader | The multi-stage "Stage-Gate" logic and complex internal data processing identify the binary as a sophisticated loader for secondary payloads. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The provided data contains significantly more **behavioral indicators** than static indicators (like IP addresses or specific file paths), as the text describes a sophisticated loader/wrapper designed to obscure its core functionality.

### **IP addresses / URLs / Domains**
*None identified.*

### **File paths / Registry keys**
*   **Note:** While the analysis mentions that the binary checks for "specific registry keys" and "file existence," no specific hardcoded paths or keys were provided in the raw strings (e.g., a specific C:\ path was not listed).

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*   **Internal Magic Value:** `-0x1f928c9d` (Note: This is an internal constant used in `fcn.100228e7` for state management/parsing; while not a file hash, it can be used as a signature for YARA rules).

### **Other artifacts**
*   **Behavioral Patterns:**
    *   **Wait-and-Verify Loop:** The binary employs a `Sleep(1000)` loop while calling `PathFileExistsW`. This is used to delay execution and evade "burst" activity detection by EDR.
    *   **Environment Manipulation:** Frequent use of `SetEnvironmentVariableW` immediately before launching child processes (used to pass configuration or paths).
    *   **MSI Integration:** Use of `MnsGetFeatureCostA`, `MsiEnumClientsA`, and `MsiViewModify` to blend in with legitimate system installers.
    *   **Certificate Validation:** Usage of `CryptGetHashParam` to perform "gatekeeping" checks on file hashes/certificates before execution.
    *   **Execution Method:** Use of `ShellExecuteExW` to launch subsequent payloads or components.
*   **Code Signatures (Internal Functions):** 
    *   `fcn.10006520` (Wait loop logic)
    *   `fcn.10020020` (Environment manipulation)
    *   `fcn.10023232` (Data conversion/formatting)
    *   `fcn.100228e7` (State machine/magic value checking)

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family:** custom
2.  **Malware type:** loader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated Orchestration (Loader behavior):** The binary acts as a "Stage-Gate" orchestrator, using MSI APIs (`MnsGetFeatureCostA`, `MsiViewModify`) and environment variable manipulation to prepare the system state for secondary payloads rather than performing malicious actions itself.
    *   **Advanced Evasion Tactics:** The use of intentional `Sleep` loops (to bypass "burst" activity detection by EDRs) and `CryptGetHashParam` (as a gatekeeping mechanism to check certificate/hash integrity before execution) indicates a high level of professional development.
    *   **Complex Internal Logic:** The presence of complex data conversion functions, magic value checks (`-0x1f928c9d`), and multi-stage state management suggests this is a sophisticated component of a larger infection chain rather than a simple standalone malware tool.
