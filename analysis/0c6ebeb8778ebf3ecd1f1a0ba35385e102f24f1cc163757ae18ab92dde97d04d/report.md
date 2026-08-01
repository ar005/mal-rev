# Threat Analysis Report

**Generated:** 2026-07-30 09:12 UTC
**Sample:** `0c6ebeb8778ebf3ecd1f1a0ba35385e102f24f1cc163757ae18ab92dde97d04d_0c6ebeb8778ebf3ecd1f1a0ba35385e102f24f1cc163757ae18ab92dde97d04d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c6ebeb8778ebf3ecd1f1a0ba35385e102f24f1cc163757ae18ab92dde97d04d_0c6ebeb8778ebf3ecd1f1a0ba35385e102f24f1cc163757ae18ab92dde97d04d.exe` |
| File type | PE32+ executable for MS Windows 5.02 (DLL), x86-64 (stripped to external PDB), 11 sections |
| Size | 3,803,648 bytes |
| MD5 | `57949a35fe645d14f03d8e1e6e7c9423` |
| SHA1 | `d5ffd41d5258039715a8575088a961a580da3100` |
| SHA256 | `0c6ebeb8778ebf3ecd1f1a0ba35385e102f24f1cc163757ae18ab92dde97d04d` |
| Overall entropy | 4.111 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1731853135 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 28,160 | 5.914 | No |
| `.data` | 512 | 0.624 | No |
| `.rdata` | 7,680 | 4.367 | No |
| `.pdata` | 3,584 | 4.169 | No |
| `.xdata` | 2,048 | 2.914 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 6,144 | 5.251 | No |
| `.idata` | 1,536 | 3.914 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 3,751,936 | 4.006 | No |
| `.reloc` | 512 | 0.958 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `CreateFileW`, `CreateToolhelp32Snapshot`, `DeleteCriticalSection`, `EnterCriticalSection`, `GetLastError`, `GetTickCount`, `InitializeCriticalSection`, `LeaveCriticalSection`, `MultiByteToWideChar`, `Process32First`, `Process32Next`, `Sleep`, `TlsGetValue`, `VirtualProtect`
**msvcrt.dll**: `__iob_func`, `_amsg_exit`, `_initterm`, `_lock`, `_strdup`, `_time64`, `_unlock`, `abort`, `calloc`, `fprintf`, `free`, `malloc`, `memcpy`, `rand`, `realloc`
**USER32.dll**: `CharLowerA`

### Exports

`AcquireIcon32_B183`, `AddChannelInfo_B183`, `AddEntryEx_B183`, `AddMedia32_B183`, `AllocBounds64_B183`, `AllocResource32_B183`, `AppendStatusInfo_B183`, `AsyncValueInternal_B183`, `BeginCountExtended_B183`, `BeginDeviceExtended_B183`, `BeginEntryInternal_B183`, `BeginHook64_B183`, `CallConfig_B183`, `CallCountEx_B183`, `CallDataA_B183`, `CallNameInternal_B183`, `CallNodeW_B183`, `CanSanitizerData_B183`, `CheckChannelImpl_B183`, `CheckEventImpl_B183`, `ClearNodeInternal_B183`, `ClearPathA_B183`, `ClearReportsBetween_ExportThunk`, `ClearStyle_B183`, `ClearTreeInfo_B183`, `CloseDataInternal_B183`, `ClosePropertiesW_B183`, `CommitFactory32_B183`, `CommitNormalizerW_B183`, `CommitProcess32_B183`, `CommitRegion_B183`, `CommitRevisionData_B183`, `CommitZoneExtended_B183`, `CrashForException_ExportThunk`, `CreateModuleW_B183`, `CreateVersion32_B183`, `DeleteDriverInternal_B183`, `DisableHook`, `DisableMapInfo_B183`, `DisableProviderImpl_B183`, `DispatchAssetA_B183`, `DispatchConfigInternal_B183`, `DispatchContext2_B183`, `DispatchPropertiesEx_B183`, `DispatchSegmentExtended_B183`, `DrainLog`, `DumpHungProcessWithPtype_ExportThunk`, `DumpProcessWithoutCrash`, `EnableConfigData_B183`, `EnableLimitData_B183`

## Extracted Strings

Total strings found: **365** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.edata
@.idata
@.reloc
AVWVSH
ARASA[AZ
ARASA[AZ
U]ATA\
$$VV^^
	ARASA[AZM
6A^PSQY[X
ARASA[AZ
W_RZW_M
ARASA[AZM
6AVA^M
PQYXWH
AWAVAUATUWVSH
AYARASA[AZH
ZPQYXM
_ARASA[AZH
6ARAZH
8[^_]A\A]A^A_
ATA\AVM
SRZ[VV^^H
AVUWVSH
6V^AWA_
	ARAZM
[^_]A^
(ASA[M
D$PS[X
?APAXH
D$AQM
ARASA[AZ
?QRZYH
D$VV^^H
6V^PS[XM
D$AQM
ARASA[AZ
APAQAYAXH
(AUA]M
(VW_^M
(AWA_M
APAQAYAX
QRZYRZRH
(ARASA[AZASA[
ARASA[AZAVA^1
D$,ATM
?AQAY1
D$AQM
	ARASA[AZH
AWA_RZH
APAQAYAXH
6V^APAQAYAXM
ASA[PS[XH
?AUA]ARAZH
6VW_^H
PSQY[XH
ARASA[AZM
T\AQAYM
PSQY[XASM
AWAVAUATUWVSH
8[^_]A\A]A^A_
$ZARASA[AZ
APAQAYAXH
APAXSRZ[M
AVWVSH
([^_A^
6V^ASM
([^_A^
AWAVATUWVSH
APAQAYAX
C AWA_
x-ASA[APAXASM
p[^_]A\A^A_
p[^_]A\A^A_
PS[XSH
AVA^ATM
?VW_^M
ARASA[AZH
ARAZARASA[AZM
AWAVAUATUWVSH
APAQAYAXM
[^_]A\A]A^A_
ARASA[AZH
ARASA[AZH
AVAUATUWVSH
ARASA[AZH
[^_]A\A]A^
A\AVA^T\1
UAWAVAUATWVSH
[^_A\A]A^A_]
([^_]H
@' t	H
5f5252f936a032ea454e437345b1394b416a39bc3835535a
72067344654175906f6f73f26489525165c473b365b6632e4ce2630a727a41ee63f4
4c176ea1724173cc65a564f464db46986fe763ef69365574729c5ffe52f2751a65fd
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.216f06d10` | `0x216f06d10` | 23122 | ✓ |
| `fcn.216f04970` | `0x216f04970` | 1971 | ✓ |
| `fcn.216f05130` | `0x216f05130` | 1674 | ✓ |
| `fcn.216f06360` | `0x216f06360` | 1449 | ✓ |
| `fcn.216f01ca0` | `0x216f01ca0` | 1195 | ✓ |
| `fcn.216f07030` | `0x216f07030` | 912 | ✓ |
| `fcn.216f05b90` | `0x216f05b90` | 834 | ✓ |
| `fcn.216f06910` | `0x216f06910` | 816 | ✓ |
| `sym.chrome_elf.dll_GetInstallDetailsPayload` | `0x216f01450` | 777 | ✓ |
| `fcn.216f02b50` | `0x216f02b50` | 773 | ✓ |
| `section..text` | `0x216f01000` | 496 | ✓ |
| `fcn.216f05950` | `0x216f05950` | 421 | ✓ |
| `fcn.216f057c0` | `0x216f057c0` | 386 | ✓ |
| `fcn.216f06ec0` | `0x216f06ec0` | 368 | ✓ |
| `entry0` | `0x216f011f0` | 305 | ✓ |
| `fcn.216f07550` | `0x216f07550` | 258 | ✓ |
| `fcn.216f06260` | `0x216f06260` | 241 | ✓ |
| `fcn.216f05ee0` | `0x216f05ee0` | 222 | ✓ |
| `fcn.216f07b20` | `0x216f07b20` | 199 | ✓ |
| `fcn.216f023c0` | `0x216f023c0` | 176 | ✓ |
| `fcn.216f02700` | `0x216f02700` | 175 | ✓ |
| `fcn.216f025c0` | `0x216f025c0` | 173 | ✓ |
| `fcn.216f02510` | `0x216f02510` | 170 | ✓ |
| `fcn.216f02850` | `0x216f02850` | 166 | ✓ |
| `fcn.216f02470` | `0x216f02470` | 160 | ✓ |
| `fcn.216f02150` | `0x216f02150` | 158 | ✓ |
| `fcn.216f02320` | `0x216f02320` | 156 | ✓ |
| `fcn.216f02280` | `0x216f02280` | 156 | ✓ |
| `fcn.216f02ab0` | `0x216f02ab0` | 153 | ✓ |
| `fcn.216f02e70` | `0x216f02e70` | 151 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.216f01ca0.c`](code/fcn.216f01ca0.c)
- [`code/fcn.216f02150.c`](code/fcn.216f02150.c)
- [`code/fcn.216f02280.c`](code/fcn.216f02280.c)
- [`code/fcn.216f02320.c`](code/fcn.216f02320.c)
- [`code/fcn.216f023c0.c`](code/fcn.216f023c0.c)
- [`code/fcn.216f02470.c`](code/fcn.216f02470.c)
- [`code/fcn.216f02510.c`](code/fcn.216f02510.c)
- [`code/fcn.216f025c0.c`](code/fcn.216f025c0.c)
- [`code/fcn.216f02700.c`](code/fcn.216f02700.c)
- [`code/fcn.216f02850.c`](code/fcn.216f02850.c)
- [`code/fcn.216f02ab0.c`](code/fcn.216f02ab0.c)
- [`code/fcn.216f02b50.c`](code/fcn.216f02b50.c)
- [`code/fcn.216f02e70.c`](code/fcn.216f02e70.c)
- [`code/fcn.216f04970.c`](code/fcn.216f04970.c)
- [`code/fcn.216f05130.c`](code/fcn.216f05130.c)
- [`code/fcn.216f057c0.c`](code/fcn.216f057c0.c)
- [`code/fcn.216f05950.c`](code/fcn.216f05950.c)
- [`code/fcn.216f05b90.c`](code/fcn.216f05b90.c)
- [`code/fcn.216f05ee0.c`](code/fcn.216f05ee0.c)
- [`code/fcn.216f06260.c`](code/fcn.216f06260.c)
- [`code/fcn.216f06360.c`](code/fcn.216f06360.c)
- [`code/fcn.216f06910.c`](code/fcn.216f06910.c)
- [`code/fcn.216f06d10.c`](code/fcn.216f06d10.c)
- [`code/fcn.216f06ec0.c`](code/fcn.216f06ec0.c)
- [`code/fcn.216f07030.c`](code/fcn.216f07030.c)
- [`code/fcn.216f07550.c`](code/fcn.216f07550.c)
- [`code/fcn.216f07b20.c`](code/fcn.216f07b20.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sym.chrome_elf.dll_GetInstallDetailsPayload.c`](code/sym.chrome_elf.dll_GetInstallDetailsPayload.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and strings, here is a breakdown of the functionality and behavior of this binary sample:

### Core Functionality and Purpose
The binary appears to be a **sophisticated downloader or a modular loader** (possibly part of a Trojan/Backdoor). It uses heavy obfuscation techniques to hide its true logic until it is executed in memory. 

Instead of containing a clear, linear path of malicious actions, the code acts as a "packer" or "stub." It de-obfuscates and builds execution stubs dynamically to perform its actual tasks (like network communication or payload execution) only in RAM, making it harder for static analysis tools to flag.

### Suspicious and Malicious Behaviors
*   **Dynamic Code Generation & Execution:** 
    *   Functions like `fcn.216f04970` and `fcn.216f05130` contain large switch-case blocks that populate memory with specific byte sequences (e.g., `0x48`, `0x8d`). This is a technique used to build machine code in the heap/stack at runtime.
    *   The use of `VirtualProtect` (found in `fcn.216f07030` and others) indicates that the sample changes memory permissions—likely marking "data" sections as executable—to run the dynamically generated code mentioned above.
*   **Process Enumeration:** 
    *   The function `fcn.216f06910` calls `CreateToolhelp32Snapshot`, `Process32First`, and `Process32Next`. It then iterates through all running processes on the system. This is a classic technique used to find target processes for **process injection** or to detect security software/sandboxes.
*   **Complex String Logic & Command Parsing:** 
    *   Function `fcn.216f06360` uses `strtok`, `strstr`, and loops through long internal arrays. It seems to be parsing a "configuration" block or a list of commands. It compares system strings against its internal, obfuscated strings to decide which functionality (e.g., stealth, communication, persistence) to enable.
*   **Masquerading:** 
    *   The inclusion of the string `chrome_elf.dll` suggests the malware may attempt to hide in plain sight by mimicking components used by Google Chrome or other Chromium-based browsers, which are frequently targeted for "browser hijacker" type infections.

### Notable Techniques and Patterns
*   **Heavy Obfuscation (Junk Code/Opaque Predicates):** The high number of `fcn.` prefixes and the complex arithmetic performed just to decide if a block should be executed suggest the use of an automated obfuscator or a custom virtual machine (VM) layer. 
*   **Anti-Analysis through Timing:** The heavy reliance on `GetTickCount` (via `sub.msvcrt.dll_time64`) in multiple functions suggests it uses timing-based logic to choose different execution paths, which can hinder automated sandboxes or static tracers.
*   **Layered Loading:** The "Switch Table" approach seen in `fcn.216f04970` indicates a technique where the actual malicious functionality is hidden behind a layer of dynamically generated jump tables, making it difficult to follow the logic flow statically.
*   **Data-Driven Logic:** Rather than having a hardcoded routine for its actions, the malware seems to have a "logic engine" that reads a large blob of data (the long hex strings in the header) and executes different routines based on what is found in those records.

### Summary Table
| Feature | Evidence/Technique | Potential Risk |
| :--- | :--- | :--- |
| **Dynamic Execution** | `VirtualProtect`, dynamic byte construction. | Hides malicious payload from signature scanners. |
| **System Recon** | `CreateToolhelp32Snapshot` + `Process32Next`. | Used for finding targets for injection or searching for AV tools. |
| **Obfuscation** | Multi-layered switch tables, junk code. | Hinders manual analysis and automated de-obfuscation. |
| **Masquerading** | `chrome_elf.dll` string reference. | Evades suspicion by mimicking legitimate software components. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | **Packer** | The use of `VirtualProtect` to change memory permissions and the construction of machine code in heap/stack space indicate a packer or "stub" used for dynamic execution. |
| **T1027** | **Obfuscated Files or Programs** | The presence of junk code, opaque predicates, switch-case tables, and complex string logic are designed to hide functionality from static analysis. |
| **T1497** | **Evasion via Sandbox Detection** | The frequent use of `GetTickCount` to determine execution paths suggests timing-based checks intended to detect and bypass automated sandboxes or security environments. |
| **T1036** | **Dynamic Resolution** | While "Masquerading" is a broad term, the deliberate use of common names like `chrome_elf.dll` and complex string logic fits the broader pattern of hiding malicious intent from detection systems. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The long hexadecimal strings appear to be encrypted/obfuscated data blocks or shellcode rather than plaintext network indicators.)

### **File paths / Registry keys**
*   **chrome_elf.dll** (Note: Used for masquerading; while a legitimate system file, its inclusion in the binary's logic indicates an attempt to blend with Chromium-based browser components.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The large hexadecimal strings provided are not structured as standard MD5/SHA1/SHA256 file hashes; they appear to be internal data blobs or encrypted configuration blocks.)

### **Other artifacts**
*   **Masquerading String:** `chrome_elf.dll`
*   **Dynamic Execution Behavior:** Use of `VirtualProtect` to change memory permissions (likely for executing dynamically generated code).
*   **Process Enumeration Activity:** Usage of `CreateToolhelp32Snapshot`, `Process32First`, and `Process32Next`.
*   **Anti-Analysis/Evasion:** 
    *   Time-based logic using `GetTickCount` (via `sub.mscrt.dll_time64`) to detect sandboxes or automated analysis.
    *   Heavy obfuscation including "Switch Table" logic and junk code to hide malicious functionality.
*   **Data-Driven Logic:** The presence of large, multi-line hex blocks used as an internal "logic engine" for command parsing and execution paths.

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Dynamic Execution & Evasion:** The use of `VirtualProtect` to change memory permissions and the construction of machine code in heap/stack space indicate a sophisticated loader designed to execute malicious payloads only in-memory to bypass traditional signature-based detection.
*   **Advanced Obfuscation:** The presence of "Switch Table" logic, junk code, and time-based anti-analysis checks (via `GetTickCount`) demonstrates a high level of engineering intended to thwart automated sandboxes and manual reverse engineering.
*   **Stealth & Persistence Mechanics:** The inclusion of the `chrome_elf.dll` string for masquerading and the use of process enumeration (`CreateToolhelp32Snapshot`) suggest it is designed to blend into common system environments while searching for targets or security software.
