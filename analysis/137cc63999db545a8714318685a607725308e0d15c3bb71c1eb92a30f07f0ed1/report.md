# Threat Analysis Report

**Generated:** 2026-09-02 16:43 UTC
**Sample:** `137cc63999db545a8714318685a607725308e0d15c3bb71c1eb92a30f07f0ed1_137cc63999db545a8714318685a607725308e0d15c3bb71c1eb92a30f07f0ed1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `137cc63999db545a8714318685a607725308e0d15c3bb71c1eb92a30f07f0ed1_137cc63999db545a8714318685a607725308e0d15c3bb71c1eb92a30f07f0ed1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 758,464 bytes |
| MD5 | `3acb776fdb1759259e51101712023f56` |
| SHA1 | `50346d0def41d34c84685be2f479dfff38305abd` |
| SHA256 | `137cc63999db545a8714318685a607725308e0d15c3bb71c1eb92a30f07f0ed1` |
| Overall entropy | 6.883 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766752383 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 528,384 | 6.696 | No |
| `.rdata` | 114,176 | 5.732 | No |
| `.data` | 72,192 | 7.584 | ⚠️ Yes |
| `.pdata` | 20,992 | 5.895 | No |
| `_RDATA` | 512 | 2.472 | No |
| `.reloc` | 18,944 | 5.433 | No |

### Imports

**WS2_32.dll**: `WSAStartup`, `getaddrinfo`, `ntohs`, `socket`, `closesocket`, `inet_ntop`, `connect`, `freeaddrinfo`, `shutdown`, `recv`, `send`
**USER32.dll**: `ExitWindowsEx`, `OpenClipboard`, `GetClipboardData`, `CloseClipboard`, `EnumDisplayDevicesA`
**SHELL32.dll**: `SHGetKnownFolderPath`, `ShellExecuteExA`, `ShellExecuteA`, `ShellExecuteW`
**ole32.dll**: `CreateStreamOnHGlobal`, `CoInitializeSecurity`, `CoCreateInstance`, `CoUninitialize`, `CoTaskMemFree`, `GetHGlobalFromStream`, `CoInitializeEx`
**OLEAUT32.dll**: `SysAllocString`, `SysFreeString`, `VariantClear`, `VariantInit`
**ADVAPI32.dll**: `RegCloseKey`, `OpenProcessToken`, `GetTokenInformation`, `RegOpenKeyExA`, `RegDeleteTreeA`, `GetUserNameA`, `RegSetValueExA`, `RegCreateKeyA`
**d3d11.dll**: `D3D11CreateDevice`
**dxgi.dll**: `CreateDXGIFactory1`
**WININET.dll**: `InternetOpenA`, `InternetReadFile`, `InternetOpenUrlA`, `InternetCloseHandle`
**IPHLPAPI.DLL**: `GetExtendedUdpTable`, `GetExtendedTcpTable`
**bcrypt.dll**: `BCryptOpenAlgorithmProvider`, `BCryptGetProperty`, `BCryptCloseAlgorithmProvider`, `BCryptCreateHash`, `BCryptHashData`, `BCryptFinishHash`, `BCryptDestroyHash`, `BCryptSetProperty`, `BCryptGenerateSymmetricKey`, `BCryptDecrypt`, `BCryptDestroyKey`
**KERNEL32.dll**: `FreeEnvironmentStringsW`, `GetEnvironmentStringsW`, `GetCPInfo`, `GetOEMCP`, `GetACP`, `IsValidCodePage`, `FindFirstFileExW`, `GetFileType`, `LCMapStringW`, `CompareStringW`, `SetEnvironmentVariableW`, `GetCommandLineW`, `GetCommandLineA`, `GetStdHandle`, `GetModuleHandleExW`

## Extracted Strings

Total strings found: **3694** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@_RDATA
@.reloc
AVVWSH
8[_^A^
AVVWSH
([_^A^
AVVWSH
([_^A^H
AWAVATVWSH
8[_^A\A^A_
<8
|,H
AVVWSH
8[_^A^
AWAVAUATVWUSH
[]_^A\A]A^A_
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVAUATVWSH
H[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
AWAVAUATVWSH
@[_^A\A]A^A_
AWAVATVWSH
<1
|EH
([_^A\A^A_
AWAVATVWUSH
 []_^A\A^A_
UAWAVAUATVWSH
<(
|^H
<!
|2H
<!
|2H
<!
|/H
<!
|2H
<0
|OH
[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
AWAVVWSH
<9
|.H
 [_^A^A_
AWAVAUATVWUSH
<(
|TH
H[]_^A\A]A^A_
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
UAWAVAUATVWSH
h[_^A\A]A^A_]
AWAVVWSH
0[_^A^A_
<

|!H
AVVWSH
([_^A^
AWAVAUATVWUSH
[]_^A\A]A^A_
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14007fdc8` | `0x14007fdc8` | 39490 | ✓ |
| `fcn.140075d88` | `0x140075d88` | 21916 | ✓ |
| `fcn.140075d74` | `0x140075d74` | 21876 | ✓ |
| `fcn.140071718` | `0x140071718` | 19803 | ✓ |
| `fcn.14007da48` | `0x14007da48` | 10749 | ✓ |
| `fcn.14007e80c` | `0x14007e80c` | 8369 | ✓ |
| `fcn.14007c77c` | `0x14007c77c` | 4676 | ✓ |
| `fcn.1400030fe` | `0x1400030fe` | 2075 | ✓ |
| `fcn.14006a240` | `0x14006a240` | 2046 | ✓ |
| `fcn.1400792ac` | `0x1400792ac` | 1705 | ✓ |
| `fcn.14006d180` | `0x14006d180` | 1685 | ✓ |
| `fcn.14007fe90` | `0x14007fe90` | 1451 | ✓ |
| `fcn.14006efb0` | `0x14006efb0` | 1275 | ✓ |
| `fcn.14007ec94` | `0x14007ec94` | 1260 | ✓ |
| `fcn.14006ead8` | `0x14006ead8` | 1237 | ✓ |
| `fcn.14007c350` | `0x14007c350` | 1065 | ✓ |
| `fcn.14007a5ec` | `0x14007a5ec` | 1037 | ✓ |
| `fcn.14007dfe0` | `0x14007dfe0` | 949 | ✓ |
| `fcn.140057a90` | `0x140057a90` | 936 | ✓ |
| `fcn.14007dac0` | `0x14007dac0` | 925 | ✓ |
| `fcn.1400778f4` | `0x1400778f4` | 896 | ✓ |
| `fcn.1400808c0` | `0x1400808c0` | 861 | ✓ |
| `fcn.140078300` | `0x140078300` | 823 | ✓ |
| `fcn.14007e444` | `0x14007e444` | 789 | ✓ |
| `fcn.140078f9c` | `0x140078f9c` | 782 | ✓ |
| `fcn.140072230` | `0x140072230` | 770 | ✓ |
| `fcn.140070acc` | `0x140070acc` | 762 | ✓ |
| `fcn.14006f6c8` | `0x14006f6c8` | 751 | ✓ |
| `fcn.140072534` | `0x140072534` | 749 | ✓ |
| `fcn.14007f5fc` | `0x14007f5fc` | 739 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400030fe.c`](code/fcn.1400030fe.c)
- [`code/fcn.140057a90.c`](code/fcn.140057a90.c)
- [`code/fcn.14006a240.c`](code/fcn.14006a240.c)
- [`code/fcn.14006d180.c`](code/fcn.14006d180.c)
- [`code/fcn.14006ead8.c`](code/fcn.14006ead8.c)
- [`code/fcn.14006efb0.c`](code/fcn.14006efb0.c)
- [`code/fcn.14006f6c8.c`](code/fcn.14006f6c8.c)
- [`code/fcn.140070acc.c`](code/fcn.140070acc.c)
- [`code/fcn.140071718.c`](code/fcn.140071718.c)
- [`code/fcn.140072230.c`](code/fcn.140072230.c)
- [`code/fcn.140072534.c`](code/fcn.140072534.c)
- [`code/fcn.140075d74.c`](code/fcn.140075d74.c)
- [`code/fcn.140075d88.c`](code/fcn.140075d88.c)
- [`code/fcn.1400778f4.c`](code/fcn.1400778f4.c)
- [`code/fcn.140078300.c`](code/fcn.140078300.c)
- [`code/fcn.140078f9c.c`](code/fcn.140078f9c.c)
- [`code/fcn.1400792ac.c`](code/fcn.1400792ac.c)
- [`code/fcn.14007a5ec.c`](code/fcn.14007a5ec.c)
- [`code/fcn.14007c350.c`](code/fcn.14007c350.c)
- [`code/fcn.14007c77c.c`](code/fcn.14007c77c.c)
- [`code/fcn.14007da48.c`](code/fcn.14007da48.c)
- [`code/fcn.14007dac0.c`](code/fcn.14007dac0.c)
- [`code/fcn.14007dfe0.c`](code/fcn.14007dfe0.c)
- [`code/fcn.14007e444.c`](code/fcn.14007e444.c)
- [`code/fcn.14007e80c.c`](code/fcn.14007e80c.c)
- [`code/fcn.14007ec94.c`](code/fcn.14007ec94.c)
- [`code/fcn.14007f5fc.c`](code/fcn.14007f5fc.c)
- [`code/fcn.14007fdc8.c`](code/fcn.14007fdc8.c)
- [`code/fcn.14007fe90.c`](code/fcn.14007fe90.c)
- [`code/fcn.1400808c0.c`](code/fcn.1400808c0.c)

## Behavioral Analysis

Based on the second chunk of disassembly, I have updated and expanded the analysis. The additional code provides significant evidence that this binary is not just a simple dropper, but a sophisticated **virtualized packer/loader** that likely employs a custom VM architecture to execute its internal logic.

### Updated Analysis Summary
The presence of large switch tables, complex bit-shifting for "reconstructing" variables, and multi-layered indirect calls confirms that the malware uses a **custom virtual machine (VM) or interpreter**. This is a high-tier obfuscation technique used to hide the execution flow from automated sandboxes and static disassemblers.

---

### 1. Advanced Architectural Features
*   **Virtual Machine (VM) Implementation:**
    *   **Switch Tables & Handlers:** Functions like `fcn.14007dfe0` contain massive switch tables with very tight offsets (e.g., `0x14007e328`). This is a classic signature of a VM where the "bytecode" of the original malware is translated into these jump points to hide the actual logic.
    *   **Instruction Decoding:** Functions like `fcn.14006f6c8` and `fcn.140072230` perform extensive bit-shifting and masking (e.g., `uVar_1 & 0x3f`, `uVar_1 >> 6`) to interpret "instructions" from a data buffer. This allows the author to write "custom" CPU instructions that are very hard for analysts to reverse-engineer.
*   **Multi-Layered API Obfuscation:**
    *   Several functions (e.g., `fcn.140057a90`, `fcn.14007e444`) use nested, complex pointer arithmetic and indirect offsets to call system APIs. Instead of calling a standard Windows API directly, it calculates an offset into a table or another table, making it very difficult for automated tools to generate a clean "Import Address Table" (IAT).

### 2. Core Functionality & Behavior
*   **Dynamic File System Exploration:**
    *   **`fcn.140078f9c`**: This function explicitly calls `FindFirstFileExW`, `FindNextFileW`, and `FindClose`. This confirms the binary is actively searching the filesystem, likely looking for specific system files, other executable programs to infect, or checking for the existence of "key" files required for the next stage.
*   **Advanced Buffer/Memory Management:**
    *   **`fcn.14007dac0`**: This appears to be a custom memory management routine. It handles complex shifting and "compacting" of data in a buffer. This is often used when decrypting a payload where the resulting size isn't known upfront or where multiple objects are packed into one continuous blob.
*   **Robust File I/O & Handling:**
    *   **`fcn.14007f5fc`**: This function wraps several standard Windows operations, including `WriteFile`. Notably, it also includes logic related to `GetConsoleMode`. In a malware context, checking the console mode can be used to detect if the sample is being run in a "clean" terminal or by an automated analysis script.

### 3. Evasive & Malicious Behaviors
*   **Payload Reconstruction:** The heavy use of bit-shifting in `fcn.14007c350` and `fcn.140072230` suggests the payload is stored in a non-standard format (e.g., "shuffled" or "split"). The code reconstructs these variables at runtime before use, ensuring that standard string/file scanners cannot find the raw payloads on disk.
*   **Anti-Analysis (Expanded):**
    *   In addition to the `IsProcessorFeaturePresent` check mentioned previously, the usage of **custom interpreter loops** acts as a massive time-sink for manual analysis. By forcing an analyst to deconstruct their "virtual instruction set" before they can even see what the malware *actually* does, it delays discovery significantly.
*   **Hidden Intent:** The complexity of `fcn.14007e80c` (from your first chunk) combined with the complex loop structures in `fcn.14007a5ec` suggests a **multi-stage decryption routine**. The code doesn't decrypt everything at once; it likely decodes "chunks" or "modules" only as they are needed for execution.

### Summary of Identified Techniques
| Feature | Location(s) | Risk Level | Description |
| :--- | :--- | :--- | :--- |
| **VM / Interpreter** | `fcn.14007dfe0`, `fcn.14006f6c8` | **High** | Custom instruction set used to hide primary logic. |
| **API Obfuscation** | `fcn.140057a90`, `fcn.14007e444` | **High** | Indirect calls via calculated offsets to bypass static analysis. |
| **File System Crawling** | `fcn.140078f9c` | **Medium** | Searching the system for targets or local environment info. |
| **Buffer Manipulation** | `fcn.14007dac0` | **Medium** | Complex logic to manage and move decrypted payload chunks. |
| **Data "Re-assembly"** | `fcn.14007c350`, `fcn.140072230` | **High** | Using bitwise shifts to reconstruct variables from "scrambled" data. |

### Conclusion for Incident Response
This is a high-sophistication piece of malware, likely a **loader or protector (packer)** for an advanced threat actor. It uses a customized execution environment (Virtual Machine) to hide its true intentions. The presence of file system crawling and robust writing routines suggests it is designed to drop and execute additional malicious modules once the initial "guards" are bypassed. 

**Recommendation:** Treat this as a high-priority sample. Dynamic analysis should be performed in a hardened environment, but note that static analysis will remain difficult due to the VM layer. Focus on capturing memory dumps during execution to bypass the VM's decryption layers and see the de-obfuscated "payload" code.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a custom virtual machine, instruction decoding (bit-shifting/masking), and multi-layer API obfuscation hides the execution flow from static analysis. |
| T1083 | File and Directory Discovery | The binary uses `FindFirstFileExW` and `FindNextFileW` to crawl the filesystem for system files or target programs. |
| T1497 | Virtualization/Sandbox Detection | The use of `GetConsoleMode` and `IsProcessorFeaturePresent` indicates checks designed to detect if the sample is running in a virtualized or analysis environment. |
| T1027 | Obfuscated Files or Information (Payload Reconstruction) | The use of bitwise shifts and "shuffling" to reconstruct variables ensures that raw payloads remain hidden from signature-based scanners on disk. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Because this sample utilizes heavy virtualization (VM-based packing), many static Indicators of Compromise (IOCs) like hardcoded IPs or file paths are obfuscated and were not present in the provided text.

Below are the identified indicators based on the available data:

**IP addresses / URLs / Domains**
*   *None* (The analysis indicates these are likely hidden within the virtual machine layer).

**File paths / Registry keys**
*   *None* (While the malware performs "FileSystem Crawling," no specific hardcoded paths were identified in the strings provided).

**Mutex names / Named pipes**
*   *None*

**Hashes**
*   *None*

**Other artifacts**
*   **Internal Function Offsets (Behavioral Markers):** The following addresses represent core logic for VM-based execution, API obfuscation, and payload reconstruction. These can be used to identify the specific behavior of the loader in memory:
    *   `fcn.14007dfe0` (VM Switch Table)
    *   `fcn.14006f6c8` & `fcn.140072230` (Instruction Decoding/Bit-shifting)
    *   `fcn.140057a90` & `fcn.14007e444` (API Obfuscation via indirect offsets)
    *   `fcn.140078f9c` (Filesystem Crawling logic)
    *   `fcn.14007dac0` (Custom Buffer/Memory management)
    *   `fcn.14007f5fc` (File I/O and `GetConsoleMode` anti-analysis checks)
    *   `fcn.14007e80c` & `fcn.14007a5ec` (Multi-stage decryption routines)
*   **API Interaction Patterns:**
    *   Use of `FindFirstFileExW`, `FindNextFileW`, and `FindClose` for environment discovery.
    *   Usage of `GetConsoleMode` to detect automated analysis environments.
*   **De-obfuscation Techniques:**
    *   Extensive use of bitwise shifts (`>>`) and masking (`& 0x3f`) to reconstruct payloads at runtime.
    *   Hidden payload "re-assembly" from non-standard data blocks.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (for type) / Low (for specific family)
4. **Key evidence**:
    *   **VM-Based Execution:** The use of large switch tables, instruction decoding via bit-shifting/masking, and a custom interpreter loop indicates a sophisticated virtualized packer used to hide primary logic from static analysis.
    *   **Multi-Stage Payload Handling:** The presence of "shuffled" data reconstruction (bit-shifting) and multi-stage decryption routines suggests the binary’s primary purpose is to de-obfuscate and launch a second-stage payload.
    *   **Advanced Evasion:** The combination of indirect API calls, anti-analysis checks (`GetConsoleMode`), and environmental discovery indicates this is a professional-grade loader designed to protect and deliver downstream malware components.
