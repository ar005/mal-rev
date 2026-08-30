# Threat Analysis Report

**Generated:** 2026-08-20 21:39 UTC
**Sample:** `10c69e7f0d2552ac602c9a9617943ccb862f4afc96fc76e5679b306afc671e38_10c69e7f0d2552ac602c9a9617943ccb862f4afc96fc76e5679b306afc671e38.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10c69e7f0d2552ac602c9a9617943ccb862f4afc96fc76e5679b306afc671e38_10c69e7f0d2552ac602c9a9617943ccb862f4afc96fc76e5679b306afc671e38.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 4 sections |
| Size | 103,936 bytes |
| MD5 | `e0a097af71d016aba19f9076ca1d7b77` |
| SHA1 | `f9d4c2b66b01b3545204c618222a9cff4cb627b8` |
| SHA256 | `10c69e7f0d2552ac602c9a9617943ccb862f4afc96fc76e5679b306afc671e38` |
| Overall entropy | 6.36 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776490225 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 67,072 | 6.577 | No |
| `.rdata` | 28,672 | 4.917 | No |
| `.data` | 2,560 | 2.64 | No |
| `.reloc` | 4,608 | 6.546 | No |

### Imports

**bcrypt.dll**: `BCryptGetProperty`, `BCryptDestroyKey`, `BCryptDecrypt`, `BCryptGenerateSymmetricKey`, `BCryptSetProperty`, `BCryptCloseAlgorithmProvider`, `BCryptOpenAlgorithmProvider`
**KERNEL32.dll**: `GetModuleFileNameW`, `SetFilePointer`, `WaitForSingleObject`, `GetCurrentDirectoryA`, `GetCommandLineA`, `CreateToolhelp32Snapshot`, `MultiByteToWideChar`, `ProcessIdToSessionId`, `Sleep`, `CopyFileA`, `GetLastError`, `GetFileAttributesA`, `Process32NextW`, `CreateFileA`, `DisableThreadLibraryCalls`
**ADVAPI32.dll**: `CreateServiceA`, `CreateProcessAsUserA`, `StartServiceCtrlDispatcherA`, `ConvertSidToStringSidA`, `CloseServiceHandle`, `SetTokenInformation`, `SetServiceStatus`, `RegisterServiceCtrlHandlerA`, `OpenSCManagerA`, `ChangeServiceConfigA`, `StartServiceA`, `OpenProcessToken`, `DuplicateTokenEx`, `ChangeServiceConfig2A`, `OpenServiceA`
**SHELL32.dll**: `SHGetFolderPathA`
**SHLWAPI.dll**: `PathAppendA`
**USERENV.dll**: `DestroyEnvironmentBlock`, `CreateEnvironmentBlock`
**ntdll.dll**: `RtlUnwind`

### Exports

`CreateTipsManager`, `GetUtility`

## Extracted Strings

Total strings found: **443** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.reloc
u&VVVVVVVj
D$hj@j
D$ 9D$(
Yt
jV
M;Jr

QQSVWd
38_^]
E9xt
&9Gv!8E
9Ov:k
URPQQh
kUQPXY]Y[
< t4<	t0
tf;1u
9>tWV
u9~uj
};GvP
u9^uj
};GvP
</t
<\t
u9^u
uSSSSj
};GvP
];3t'
f9:t!V
;ut.;
PPPPPPPP
PPPPPWV
PP9E u
QQSVj8j@

u<jXSf

u	jZf
PVVVVV
t;Et
\9EuY
D$+d$SVW
D$+d$SVW
bad allocation
bad exception
__based(
__cdecl
__pascal
__stdcall
__thiscall
__fastcall
__vectorcall
__clrcall
__eabi
__swift_1
__swift_2
__ptr64
__restrict
__unaligned
restrict(
 delete
operator
`vftable'
`vbtable'
`vcall'
`typeof'
`local static guard'
`string'
`vbase destructor'
`vector deleting destructor'
`default constructor closure'
`scalar deleting destructor'
`vector constructor iterator'
`vector destructor iterator'
`vector vbase constructor iterator'
`virtual displacement map'
`eh vector constructor iterator'
`eh vector destructor iterator'
`eh vector vbase constructor iterator'
`copy constructor closure'
`udt returning'
`local vftable'
`local vftable constructor closure'
 new[]
 delete[]
`omni callsig'
`placement delete closure'
`placement delete[] closure'
`managed vector constructor iterator'
`managed vector destructor iterator'
`eh vector copy constructor iterator'
`eh vector vbase copy constructor iterator'
`dynamic initializer for '
`dynamic atexit destructor for '
`vector copy constructor iterator'
`vector vbase copy constructor iterator'
`managed vector copy constructor iterator'
`local static thread guard'
operator "" 
operator co_await
operator<=>
 Type Descriptor'
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.100053ed` | `0x100053ed` | 14840 | ✓ |
| `fcn.10005f50` | `0x10005f50` | 6139 | ✓ |
| `fcn.10005410` | `0x10005410` | 4529 | ✓ |
| `fcn.1000ef38` | `0x1000ef38` | 4301 | ✓ |
| `fcn.100013c0` | `0x100013c0` | 2352 | ✓ |
| `fcn.10001cf0` | `0x10001cf0` | 1982 | ✓ |
| `fcn.10007b90` | `0x10007b90` | 1396 | ✓ |
| `fcn.1000d110` | `0x1000d110` | 1262 | ✓ |
| `fcn.10003d20` | `0x10003d20` | 1108 | ✓ |
| `fcn.100024b0` | `0x100024b0` | 970 | ✓ |
| `fcn.1000deb1` | `0x1000deb1` | 962 | ✓ |
| `fcn.10003830` | `0x10003830` | 944 | ✓ |
| `fcn.10006ac1` | `0x10006ac1` | 938 | ✓ |
| `fcn.10002880` | `0x10002880` | 896 | ✓ |
| `fcn.10002d00` | `0x10002d00` | 870 | ✓ |
| `fcn.1000a6a3` | `0x1000a6a3` | 645 | ✓ |
| `fcn.10010822` | `0x10010822` | 640 | ✓ |
| `fcn.1000f84e` | `0x1000f84e` | 614 | ✓ |
| `fcn.1000fc1d` | `0x1000fc1d` | 576 | ✓ |
| `fcn.10010ac5` | `0x10010ac5` | 563 | ✓ |
| `fcn.1000e764` | `0x1000e764` | 540 | ✓ |
| `fcn.10003430` | `0x10003430` | 539 | ✓ |
| `fcn.10004870` | `0x10004870` | 518 | ✓ |
| `fcn.1000b26b` | `0x1000b26b` | 517 | ✓ |
| `fcn.100092ff` | `0x100092ff` | 503 | ✓ |
| `fcn.10010113` | `0x10010113` | 500 | ✓ |
| `fcn.1000c050` | `0x1000c050` | 498 | ✓ |
| `fcn.1000d7a4` | `0x1000d7a4` | 495 | ✓ |
| `fcn.10003650` | `0x10003650` | 470 | ✓ |
| `fcn.10005788` | `0x10005788` | 465 | ✓ |

### Decompiled Code Files

- [`code/fcn.100013c0.c`](code/fcn.100013c0.c)
- [`code/fcn.10001cf0.c`](code/fcn.10001cf0.c)
- [`code/fcn.100024b0.c`](code/fcn.100024b0.c)
- [`code/fcn.10002880.c`](code/fcn.10002880.c)
- [`code/fcn.10002d00.c`](code/fcn.10002d00.c)
- [`code/fcn.10003430.c`](code/fcn.10003430.c)
- [`code/fcn.10003650.c`](code/fcn.10003650.c)
- [`code/fcn.10003830.c`](code/fcn.10003830.c)
- [`code/fcn.10003d20.c`](code/fcn.10003d20.c)
- [`code/fcn.10004870.c`](code/fcn.10004870.c)
- [`code/fcn.100053ed.c`](code/fcn.100053ed.c)
- [`code/fcn.10005410.c`](code/fcn.10005410.c)
- [`code/fcn.10005788.c`](code/fcn.10005788.c)
- [`code/fcn.10005f50.c`](code/fcn.10005f50.c)
- [`code/fcn.10006ac1.c`](code/fcn.10006ac1.c)
- [`code/fcn.10007b90.c`](code/fcn.10007b90.c)
- [`code/fcn.100092ff.c`](code/fcn.100092ff.c)
- [`code/fcn.1000a6a3.c`](code/fcn.1000a6a3.c)
- [`code/fcn.1000b26b.c`](code/fcn.1000b26b.c)
- [`code/fcn.1000c050.c`](code/fcn.1000c050.c)
- [`code/fcn.1000d110.c`](code/fcn.1000d110.c)
- [`code/fcn.1000d7a4.c`](code/fcn.1000d7a4.c)
- [`code/fcn.1000deb1.c`](code/fcn.1000deb1.c)
- [`code/fcn.1000e764.c`](code/fcn.1000e764.c)
- [`code/fcn.1000ef38.c`](code/fcn.1000ef38.c)
- [`code/fcn.1000f84e.c`](code/fcn.1000f84e.c)
- [`code/fcn.1000fc1d.c`](code/fcn.1000fc1d.c)
- [`code/fcn.10010113.c`](code/fcn.10010113.c)
- [`code/fcn.10010822.c`](code/fcn.10010822.c)
- [`code/fcn.10010ac5.c`](code/fcn.10010ac5.c)

## Behavioral Analysis

This updated analysis incorporates the additional disassembly from chunk 2, which provides deeper insight into the malware's deployment tactics, environmental fingerprints, and infrastructure for handling its internal components.

### Updated Analysis Summary
The binary remains a sophisticated **malware dropper/loader**. The new code confirms that it doesn't just drop a payload; it actively manages a local environment by creating hidden directories, manipulating file attributes to hide from the user, and performing deep hardware-level checks (CPUID) to detect high-end virtualization or emulation environments.

---

### New Findings & Detailed Analysis

#### 1. File System Manipulation & "Stealth" Deployment
The functions `fcn.10003430` and `fcn.10003650` reveal how the malware prepares its environment:
*   **Hidden Directory Creation:** The code specifically constructs paths for a directory named **"client"**. It uses `CreateDirectoryA` to build this structure.
*   **Attribute Manipulation (Stealth):** After copying files into these directories, it calls `SetFileAttributesA` with flags like `0x80`. In the Windows API, `0x10` is the "Hidden" attribute; the use of various bitmasks suggests it is marking its components as **System**, **Hidden**, or both.
*   **Evasive File Operations:** In `fcn.10003650`, the code uses a loop to perform several operations between file moves, followed by `Sleep(100)`. This "sleep" behavior is a common technique to evade heuristic scanners that look for rapid-fire file system changes (which usually indicate unpacking or dropping).
*   **File Movement:** It utilizes `CopyFileA` and `DeleteFileA` to move the payload from its initial location to a more permanent, hidden path.

#### 2. Advanced Anti-Analysis & Hardware Fingerprinting
The function `fcn.10005788` provides evidence of sophisticated evasion techniques:
*   **CPUID Instruction Analysis:** The code interacts with low-level CPU features using `IsProcessorFeaturePresent` and multiple custom functions (`cpuid_basic_info`, `cpuid_Version_info`, and `cpuid_Extended_Feature_Enumeration_info`).
*   **Virtualization Detection:** It checks for specific hardware signatures (e.g., bitmasks like `0x756e6547` which can be related to identifying specific processor families). This is a high-level check designed to determine if the code is running on a **physical machine** or inside an **emulator/hypervisor** (like QEMU, KVM, or advanced Sandbox environments).
*   **Feature Flag Checking:** It checks for various hardware features. If the environment doesn't "look" like a standard physical PC, the malware may terminate or change its behavior to avoid analysis.

#### 3. Complex Payload Capabilities
The presence of `fcn.10010113` is highly significant:
*   **Mathematical Library Integration:** This function contains a large internal dispatch table for mathematical operations such as **"sqrt"**, **"acos"**, **"asin"**, and **"log10"**.
*   **Implication:** The fact that the loader includes (or prepares for) a heavy math library suggests that the final payload is not a simple "script." It likely performs complex calculations, which are common in **cryptominers**, **sophisticated ransomware encryption engines**, or **complex communication protocols** used by advanced RATs.

#### 4. Robust Internal Handling
*   **Exception/Signal Handling:** `fcn.1000c050` appears to be a custom exception handling routine. It uses the `swi(3)` instruction (Software Interrupt) which, on Windows, is often used by malware to transition into an error-handling state or bypass standard debugger breakpoints during "noisy" operations like memory allocation.
*   **Data Processing:** The code includes robust routines for Unicode conversion (`fcn.1000b26b`) and buffer management (`fcn.10004870`), ensuring that the malware can handle complex string manipulations or data conversions during its extraction phase without crashing or alerting the OS.

---

### Updated Summary of Key Indicators (IOCs) & Behaviors

*   **Persistence:** Creates/modifies a service named *"Web Service (Auto Run)"*.
*   **Evasion (Environmental):** 
    *   Standard checks: `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`.
    *   Advanced checks: **CPUID-based hardware fingerprinting** to detect virtualization and specific processor features.
*   **Evasion (File System):** Creates a hidden directory named **"client"** and applies system/hidden attributes to the dropped files.
*   **Privilege Escalation:** Manually manipulates Windows Tokens to gain **SYSTEM** authority.
*   **Payload Extraction:** Extracts `user.dat` into memory, moves components to hidden folders, and utilizes a math-capable runtime for execution.

### Conclusion
This is a high-tier piece of malware. The combination of **manual token manipulation**, **hardened anti-virtualization checks (CPUID)**, and **sophisticated file system hiding** indicates that this is likely a primary infection vector for a sophisticated Trojan or Ransomware family. It is designed to be "invisible" to both the average user and automated security scanners.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualized Environment Detection | The use of `CPUID` instructions and hardware fingerprinting is specifically designed to detect if the malware is running in a virtual machine or emulator. |
| **T1457** | Debugger Detection | The inclusion of standard checks like `IsDebuggerPresent` and `CheckRemoteDebuggerPresent` are primary methods for detecting analysis tools. |
| **T1036** | Hide Files or Directories | The malware creates a "client" directory and uses `SetFileAttributesA` to apply hidden/system flags to its components to evade user and scanner detection. |
| **T1543.003** | Create or Modify System Services | The creation of the "Web Service (Auto Run)" service is a direct method for establishing persistence on the host system. |
| **T1134** | Masquerade | The manual manipulation of Windows Tokens to gain SYSTEM authority allows the malware to masquerade as a higher-privileged user. |
| **T1630** | Subvert Detection | The use of `Sleep()` between file operations and advanced hardware checks are tactics used to evade heuristic analysis and automated security scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `DuiLib_u.dll` (Likely component/payload)
*   `GameBox.exe` (Likely payload executable)
*   `user.dat` (Configuration or data file)
*   `Utility.dll` (Library component)
*   `"client"` (Specific directory name used for staging and hiding components)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Persistence Mechanism:** `Web Service (Auto Run)` (Service name/description used for persistence).
*   **Evasion - Hardware Fingerprinting:** 
    *   Utilization of `CPUID` instructions.
    *   Detection of specific hardware bitmasks (e.g., `0x756e6547`) to identify virtualized environments.
*   **Evasion - File System Manipulation:** Use of `SetFileAttributesA` with the `0x80` mask (indicating "System" and/or "Hidden" attributes) for file obfuscation.
*   **Potential Masquerading Names:** The following strings appear to be used either as decoy filenames or to check for the presence of security software: 
    *   `360tray.exe`
    *   `360safe.exe`
    *   `QMUI.exe`
    *   `QQPCTray.exe`
    *   `QQPCRtpService.exe`
    *   `HipsTray.exe`
    *   `HipsDaemon.exe`
*   **Execution Technique:** The inclusion of a large mathematical library (functions such as `sqrt`, `acos`, `asin`, and `log10`) suggests the payload may involve encryption or complex communication protocols.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper, loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Evasion & Anti-Analysis:** The sample employs sophisticated hardware fingerprinting (via `CPUID` instructions) to detect virtualized environments and uses manual Windows Token manipulation to escalate privileges to SYSTEM, indicating a high-tier threat actor.
*   **Stealthy Payload Deployment:** The loader actively conceals its footprint by creating hidden "client" directories, applying system/hidden attributes (`0x80`) to files, and using `Sleep` timers to evade heuristic detection during the extraction of components like `GameBox.exe`.
*   **Sophisticated Infrastructure for Complex Payloads:** The inclusion of a heavy mathematical library (calculating `sqrt`, `acos`, etc.) indicates that the loader is preparing an environment for high-complexity payloads, such as ransomware encryption engines or complex RAT communication protocols.
