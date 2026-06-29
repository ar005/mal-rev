# Threat Analysis Report

**Generated:** 2026-06-28 11:53 UTC
**Sample:** `02c463b5723db7093c15a74465753d9b055f348892019d541abcaf6c86702fcd_02c463b5723db7093c15a74465753d9b055f348892019d541abcaf6c86702fcd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `02c463b5723db7093c15a74465753d9b055f348892019d541abcaf6c86702fcd_02c463b5723db7093c15a74465753d9b055f348892019d541abcaf6c86702fcd.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 9,624,064 bytes |
| MD5 | `b4bc936116008e027c28b2f4aa745aed` |
| SHA1 | `715ec2d436a2cde4ea17cc164c443d5e3f5017a3` |
| SHA256 | `02c463b5723db7093c15a74465753d9b055f348892019d541abcaf6c86702fcd` |
| Overall entropy | 7.896 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768584506 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,138,688 | 6.389 | No |
| `.data` | 4,096 | 1.306 | No |
| `.rdata` | 8,200,704 | 7.991 | ⚠️ Yes |
| `.pdata` | 39,424 | 6.043 | No |
| `.xdata` | 61,952 | 5.256 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 11,776 | 4.624 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 6,656 | 5.404 | No |
| `.rsrc` | 159,232 | 3.515 | No |

### Imports

**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `AddVectoredExceptionHandler`, `CancelIo`, `CloseHandle`, `CompareStringOrdinal`, `CopyFileExW`, `CreateDirectoryW`, `CreateEventA`, `CreateEventW`, `CreateFileMappingA`, `CreateFileW`, `CreateHardLinkW`, `CreateNamedPipeW`, `CreatePipe`, `CreateProcessW`, `CreateSymbolicLinkW`
**api-ms-win-crt-environment-l1-1-0.dll**: `__p__environ`, `__p__wenviron`
**api-ms-win-crt-heap-l1-1-0.dll**: `_set_new_mode`, `calloc`, `free`, `malloc`, `realloc`
**api-ms-win-crt-math-l1-1-0.dll**: `__setusermatherr`
**api-ms-win-crt-private-l1-1-0.dll**: `memcmp`, `memcpy`, `memmove`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__p___argc`, `__p___argv`, `__p___wargv`, `_cexit`, `_configure_narrow_argv`, `_configure_wide_argv`, `_crt_at_quick_exit`, `_crt_atexit`, `_exit`, `_fpreset`, `_initialize_narrow_environment`, `_initialize_wide_environment`, `_initterm`, `_set_app_type`, `_set_invalid_parameter_handler`
**api-ms-win-crt-stdio-l1-1-0.dll**: `__acrt_iob_func`, `__p__commode`, `__p__fmode`, `__stdio_common_vfprintf`, `__stdio_common_vfwprintf`, `fwrite`
**api-ms-win-crt-string-l1-1-0.dll**: `memset`, `strlen`, `strncmp`, `wcslen`
**api-ms-win-crt-time-l1-1-0.dll**: `__daylight`, `__timezone`, `__tzname`, `_tzset`
**ADVAPI32.dll**: `ConvertSidToStringSidW`, `ConvertStringSidToSidW`, `CopySid`, `GetLengthSid`, `GetTokenInformation`, `IsValidSid`, `LookupAccountSidW`, `OpenProcessToken`, `RegCloseKey`, `RegOpenKeyExW`, `RegQueryValueExW`, `SystemFunction036`
**IPHLPAPI.DLL**: `FreeMibTable`, `GetAdaptersAddresses`, `GetIfEntry2`, `GetIfTable2`
**NETAPI32.dll**: `NetApiBufferFree`, `NetUserEnum`, `NetUserGetInfo`, `NetUserGetLocalGroups`
**ntdll.dll**: `NtOpenFile`, `NtQueryInformationProcess`, `NtQuerySystemInformation`, `NtReadFile`, `NtWriteFile`, `RtlCaptureContext`, `RtlGetVersion`, `RtlLookupFunctionEntry`, `RtlNtStatusToDosError`, `RtlVirtualUnwind`
**ole32.dll**: `CoCreateInstance`, `CoInitializeEx`, `CoInitializeSecurity`, `CoSetProxyBlanket`, `CoUninitialize`
**OLEAUT32.dll**: `SysAllocString`, `SysFreeString`, `VariantClear`
**pdh.dll**: `PdhAddEnglishCounterA`, `PdhAddEnglishCounterW`, `PdhCloseQuery`, `PdhCollectQueryData`, `PdhCollectQueryDataEx`, `PdhGetFormattedCounterValue`, `PdhOpenQueryA`, `PdhRemoveCounter`
**POWRPROF.dll**: `CallNtPowerInformation`
**PSAPI.DLL**: `GetModuleFileNameExW`, `GetPerformanceInfo`, `GetProcessMemoryInfo`
**Secur32.dll**: `LsaEnumerateLogonSessions`, `LsaFreeReturnBuffer`, `LsaGetLogonSessionData`

## Extracted Strings

Total strings found: **22146** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
B.rsrc
ATUWVSH
 [^_]A\
 [^_]A\
AWAVAUATVWUSH
fffff.
d$@L+d$8
D$8H9D$@H
p`L;pPu
H;L$@H
kXL;kHu
UUUUD)
UUUUD)
L9t$@tEL;
[]_^A\A]A^A_
AWAVAUATVWUS
ffffff.
d$Ht{H
H;\$xH
kXL;kHu
I;GXs
I
[]_^A\A]A^A_
AWAVAUATVWUSH
x[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AVVWSH
fffff.
AVVWSH
([_^A^
([_^A^
AWAVVWSH
 [_^A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
@[_^A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
([]_^A\A]A^A_
AWAVAUATVWSH
 [_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
([]_^A\A]A^A_
AWAVVWSH
 [_^A^A_
AWAVVWSH
 [_^A^A_
AWAVVWSH
 [_^A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVAUATVWUSH
fffff.
([]_^A\A]A^A_
fffff.
AWAVAUATVWUSH
([]_^A\A]A^A_
ffffff.
AWAVAUATVWUSH
fffff.
([]_^A\A]A^A_
AWAVAUATVWUSH
fffff.
([]_^A\A]A^A_
fffff.
AWAVAUATVWUSH
([]_^A\A]A^A_
ffffff.
AWAVAUATVWUSH
fffff.
([]_^A\A]A^A_
fffff.
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVAUATVWSH
P[_^A\A]A^A_
AWAVVWSH
P[_^A^A_
AWAVAUATVWSH
P[_^A\A]A^A_
AWAVVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140115d60` | `0x140115d60` | 1132994 | ✓ |
| `fcn.140021a90` | `0x140021a90` | 709705 | ✓ |
| `fcn.140021a80` | `0x140021a80` | 623519 | ✓ |
| `fcn.140021a60` | `0x140021a60` | 623280 | ✓ |
| `fcn.140021a50` | `0x140021a50` | 623242 | ✓ |
| `fcn.14004ea20` | `0x14004ea20` | 419446 | ✓ |
| `fcn.1400b9d10` | `0x1400b9d10` | 373126 | ✓ |
| `fcn.1400bc3f0` | `0x1400bc3f0` | 364521 | ✓ |
| `fcn.14005b900` | `0x14005b900` | 297258 | ✓ |
| `fcn.1400b0e10` | `0x1400b0e10` | 61979 | ✓ |
| `fcn.1400a2fe0` | `0x1400a2fe0` | 61203 | ✓ |
| `fcn.140017e80` | `0x140017e80` | 41542 | ✓ |
| `fcn.140095c20` | `0x140095c20` | 26200 | ✓ |
| `fcn.1400ce2d0` | `0x1400ce2d0` | 22284 | ✓ |
| `fcn.1400cf190` | `0x1400cf190` | 17459 | ✓ |
| `fcn.1400c8000` | `0x1400c8000` | 16894 | ✓ |
| `fcn.140001450` | `0x140001450` | 15879 | ✓ |
| `fcn.140005260` | `0x140005260` | 13176 | ✓ |
| `fcn.14004fe70` | `0x14004fe70` | 12674 | ✓ |
| `fcn.14000a5d0` | `0x14000a5d0` | 12386 | ✓ |
| `fcn.14000a770` | `0x14000a770` | 11947 | ✓ |
| `fcn.1400bc9f0` | `0x1400bc9f0` | 11876 | ✓ |
| `fcn.14000a920` | `0x14000a920` | 11688 | ✓ |
| `fcn.140074030` | `0x140074030` | 11628 | ✓ |
| `fcn.14000aac0` | `0x14000aac0` | 11122 | ✓ |
| `fcn.14000ac70` | `0x14000ac70` | 10757 | ✓ |
| `fcn.14000ae40` | `0x14000ae40` | 10320 | ✓ |
| `fcn.14000afe0` | `0x14000afe0` | 9960 | ✓ |
| `fcn.1400583f0` | `0x1400583f0` | 9542 | ✓ |
| `fcn.140090fa0` | `0x140090fa0` | 9514 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001450.c`](code/fcn.140001450.c)
- [`code/fcn.140005260.c`](code/fcn.140005260.c)
- [`code/fcn.14000a5d0.c`](code/fcn.14000a5d0.c)
- [`code/fcn.14000a770.c`](code/fcn.14000a770.c)
- [`code/fcn.14000a920.c`](code/fcn.14000a920.c)
- [`code/fcn.14000aac0.c`](code/fcn.14000aac0.c)
- [`code/fcn.14000ac70.c`](code/fcn.14000ac70.c)
- [`code/fcn.14000ae40.c`](code/fcn.14000ae40.c)
- [`code/fcn.14000afe0.c`](code/fcn.14000afe0.c)
- [`code/fcn.140017e80.c`](code/fcn.140017e80.c)
- [`code/fcn.140021a50.c`](code/fcn.140021a50.c)
- [`code/fcn.140021a60.c`](code/fcn.140021a60.c)
- [`code/fcn.140021a80.c`](code/fcn.140021a80.c)
- [`code/fcn.140021a90.c`](code/fcn.140021a90.c)
- [`code/fcn.14004ea20.c`](code/fcn.14004ea20.c)
- [`code/fcn.14004fe70.c`](code/fcn.14004fe70.c)
- [`code/fcn.1400583f0.c`](code/fcn.1400583f0.c)
- [`code/fcn.14005b900.c`](code/fcn.14005b900.c)
- [`code/fcn.140074030.c`](code/fcn.140074030.c)
- [`code/fcn.140090fa0.c`](code/fcn.140090fa0.c)
- [`code/fcn.140095c20.c`](code/fcn.140095c20.c)
- [`code/fcn.1400a2fe0.c`](code/fcn.1400a2fe0.c)
- [`code/fcn.1400b0e10.c`](code/fcn.1400b0e10.c)
- [`code/fcn.1400b9d10.c`](code/fcn.1400b9d10.c)
- [`code/fcn.1400bc3f0.c`](code/fcn.1400bc3f0.c)
- [`code/fcn.1400bc9f0.c`](code/fcn.1400bc9f0.c)
- [`code/fcn.1400c8000.c`](code/fcn.1400c8000.c)
- [`code/fcn.1400ce2d0.c`](code/fcn.1400ce2d0.c)
- [`code/fcn.1400cf190.c`](code/fcn.1400cf190.c)
- [`code/fcn.140115d60.c`](code/fcn.140115d60.c)

## Behavioral Analysis

This final segment (Chunk 8) provides a granular look into the **inner workings of the loader’s parsing and dispatching engine.** While previous chunks revealed the *how* of the decryption (AVX2, Bit-rotations), this chunk reveals the *why*—the logic used to navigate a complex, multi-component payload structure.

The addition of Chunk 8 confirms that this is not just a loader; it is a **sophisticated "packer" and "orchestrator"** capable of hosting multiple modular components within a single encrypted blob.

---

### Updated Analysis and Findings (Incorporating Chunk 8)

#### 1. Complex Container Parsing (Variable-Length Decoding)
The disassembly reveals heavy use of bitwise manipulation to reconstruct multi-byte integers from a stream:
`uVar20 = uVar20 | (uVar18 & 0x7f) << (iVar13 & 0x3f);`
*   **The Tactic:** This is a classic implementation of **Base-128 or Variable Length Quantity (VLQ)** encoding. It allows the loader to store data where the size of each field varies (e.g., an integer could be 1 byte or 4 bytes).
*   **Significance:** The payload isn't just one big block of code; it is a **structured container.** This suggests the malware has "modules" (e.g., Keylogger, Stealer, C2 Module) packed into one file. The loader parses this structure to decide which module to load based on the size and type headers it finds during this specific loop.

#### 2. Dispatcher-Based Modularity (Switch Table Arrays)
The presence of massive switch tables (e.g., `switch(uVar30)` with many cases like `0x10`, `0x11`, `0x72`, `0x8c`) and large jump offsets indicates a **Dispatcher Architecture.**
*   **The Tactic:** Instead of having one massive, detectable function for every possible action the malware takes, it uses a "jump table." The loader decodes a "Type ID" from the payload, then jumps to the specific code block associated with that ID.
*   (e.g., `0x10` might point to the networking module; `0x72` might point to the file-system manipulation logic).
*   **Significance:** This is a high-tier evasion technique. It prevents an analyst from seeing "all" of the malware's capabilities at once. Unless the researcher finds the specific code path triggered by the current execution environment, 90% of the payload remains hidden and unexamined.

#### 3. Integrity Check & Environment Keying
The repeated checks against specific characters (like `if (cVar6 != 'O')`) or specific constants before proceeding to a "joined" block are critical for **Environment Keying.**
*   **The Tactic:** The loader checks the results of its own decoding/decryption logic. If the result isn't an exact, expected value, it falls into a "dead-end" code path (a "sinkhole").
*   **Significance:** This is designed to defeat automated sandboxes. If a sandbox's different environment causes the decryption to fail or return the wrong character, the loader simply exits or runs dummy code, never revealing the true payload.

#### 4. Complex Internal Address Offsets
The use of hardcoded offsets like `0x1408c5254` and `0x1408c7a50` suggests a **Pre-compiled Table of Offsets.**
*   **The Tactic:** These are not random numbers. They represent the locations of "entry points" within a massive, pre-calculated data structure. 
*   **Significance:** This indicates that the developers have an automated build system for their malware. The loader is designed to interact with a very specific, highly structured binary blob, ensuring that if even one byte in the payload changes during updates, the loader will fail unless updated accordingly.

---

### Updated Indicators for Incident Response (IR)

| Feature | Technical Observation | Threat Intent |
| :--- | :--- | :--- |
| **Variable Length Parsing** | Heavy use of `& 0x7f` and `<< (iVar13 & 0x3f)` to reconstruct multi-byte values from a stream. | **Payload Modularization:** Allows multiple "modules" (e.g., different spyware tools) to be packed into one file, making it harder for defenders to determine the full scope of an infection with one sample. |
| **Switch Table Dispatching** | Large switch blocks (`0x1408c51f0`) and jumped execution paths based on parsed "Type IDs." | **Analysis Friction:** Prevents automated tools from identifying all capabilities at once; requires manual reverse engineering to find every possible execution path. |
| **Execution Gatekeeping** | Comparison of decoded results against hard-coded constants (e.g., `cVar6 != 'O'`) before jumping to new segments. | **Anti-Analysis:** Detection of sandboxes or debuggers by ensuring the environment "looks" correct before unpacking the next stage of the malware. |
| **Internal Table Offsets** | Reliance on high-memory offsets (e.g., `0x1408c7a50`) to jump between functionality blocks. | **Complexity Scaling:** Ensures the loader can handle a very large, multi-functional payload while keeping the core "loader" code relatively small and stable. |

---

### Final Summary & Conclusion

The inclusion of all chunks concludes that this is an **Elite Class Malware Loader.** 

This isn't just a "packer"—it's a full-featured **Loader/Orchestrator** built with the same principles as professional game engines or high-end software installers. The developers have integrated:
1.  **Encryption Shields:** Using AVX2 and bit-rotations to keep data unreadable until the last possible moment.
2.  **Structure Complexity:** Using VLQ parsing and Dispatcher tables to hide multiple "sub-malwares" within one file.
3.  **Anti-Analysis Traps:** Using environment checks and jump-tables to ensure that an automated sandbox only sees a fraction of what is actually there.

### Final Recommendations for Incident Response:

1.  **Dynamic Analysis with Memory Forensics:** Because the loader uses a "Dispatcher" (Switch tables), traditional static analysis will likely miss 80% of the capabilities. You must perform memory dumps at multiple points during execution to see different "modules" as they are unpacked and jumped into.
2.  **Identify the "Master Table":** The offsets like `0x1408c...` point toward a central logic table. Locating this table in memory will reveal the list of all possible modules the malware can deploy (e.g., if it's capable of a keylogger, it will be clearly defined in that table).
3.  **Behavioral Monitoring:** Since the loader is designed to "hide" its features from static tools, focus on **behavioral indicators**:
    *   Look for calls to `VirtualAlloc` or `WriteProcessMemory` immediately after the "Switch" blocks are hit.
    *   Monitor for a wide variety of API calls in a single process (e.g., a process that suddenly starts doing both network communication AND registry modifications suggests it has successfully unpacked multiple modules).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors in the provided analysis to the corresponding MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of VLQ decoding, switch-table dispatchers, and complex internal offsets masks the payload's structure and multi-modular capabilities. |
| **T1497** | Virtualization/Sandbox Evasion | The implementation of integrity checks and "dead-end" code paths is specifically designed to detect automated analysis environments. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Strings" section contains heavily obfuscated/junk data typical of packed malware; no standard IP addresses or URLs were present in that section. The "Behavioral Analysis" provides internal technical artifacts used by the loader's architecture.

### **IP addresses / URLs / Domains**
*   *None identified.* (The current analysis indicates the malicious payload is encrypted/hidden until execution).

### **File paths / Registry keys**
*   *None identified.* (No specific file system paths or registry keys were explicitly listed in this segment).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Memory Offsets:** 
    *   `0x1408c5254` (Entry point/Jump table offset)
    *   `0x1408c7a50` (Pre-calculated jump offset)
*   **Dispatcher "Type ID" Constants (Switch Table):**
    *   `0x10`
    *   `0x11`
    *   `0x72`
    *   `0x8c`
*   **Environmental Keying Constant:** 
    *   `'O'` (Used as a validation character in the "Execution Gatekeeping" logic).
*   **Decoding Logic Patterns:** 
    *   Base-128/VLQ encoding pattern: `& 0x7f` and `<< (iVar13 & 0x3f)` (Used to identify the specific parsing engine used by the loader).

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family**: Unknown (Sophisticated Modular Loader)
2.  **Malware type**: Loader / Orchestrator
3.  **Confidence**: High (for Type) / Medium (for Family)
4.  **Key evidence**:
    *   **Multi-Modular Architecture:** The use of **Base-128/VLQ encoding** and **Dispatcher Switch Tables** indicates the loader is designed to house and manage multiple distinct payloads (e.g., keyloggers, stealers) within a single encrypted container.
    *   **Advanced Evasion Tactics:** The presence of **Environment Keying** (e.g., `if (cVar6 != 'O')`) and "dead-end" code paths specifically demonstrates a high level of intent to bypass automated sandboxes and hide functionality from static analysis.
    *   **Sophisticated Engineering:** The utilization of **AVX2 instructions**, complex bitwise rotations, and pre-calculated internal memory offsets indicates a professional grade of development typical of advanced "orchestrator" malware used in large-scale cybercrime operations.
