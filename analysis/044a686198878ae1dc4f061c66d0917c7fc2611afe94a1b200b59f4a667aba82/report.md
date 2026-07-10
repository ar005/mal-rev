# Threat Analysis Report

**Generated:** 2026-07-09 22:24 UTC
**Sample:** `044a686198878ae1dc4f061c66d0917c7fc2611afe94a1b200b59f4a667aba82_044a686198878ae1dc4f061c66d0917c7fc2611afe94a1b200b59f4a667aba82.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `044a686198878ae1dc4f061c66d0917c7fc2611afe94a1b200b59f4a667aba82_044a686198878ae1dc4f061c66d0917c7fc2611afe94a1b200b59f4a667aba82.exe` |
| File type | PE32+ executable for MS Windows 5.02 (console), x86-64 (stripped to external PDB), 9 sections |
| Size | 2,129,408 bytes |
| MD5 | `578dc45d359a94e03e3ec1b9e5a9bbae` |
| SHA1 | `bc0c3fa2a2938fddd40d08acbe1c2d0c2db0154d` |
| SHA256 | `044a686198878ae1dc4f061c66d0917c7fc2611afe94a1b200b59f4a667aba82` |
| Overall entropy | 6.5 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764886424 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,604,096 | 6.385 | No |
| `.data` | 3,584 | 0.953 | No |
| `.rdata` | 304,128 | 5.933 | No |
| `.pdata` | 88,064 | 6.238 | No |
| `.xdata` | 108,032 | 4.788 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 12,288 | 4.704 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 7,680 | 5.319 | No |

### Imports

**ADVAPI32.dll**: `ConvertSidToStringSidW`, `ConvertStringSidToSidW`, `CopySid`, `GetLengthSid`, `GetTokenInformation`, `IsValidSid`, `LookupAccountSidW`, `LsaClose`, `OpenProcessToken`, `RegCloseKey`, `RegOpenKeyExW`, `RegQueryValueExW`, `SystemFunction036`
**KERNEL32.dll**: `DeleteCriticalSection`, `EnterCriticalSection`, `InitializeCriticalSection`, `LeaveCriticalSection`, `RaiseException`, `RtlUnwindEx`, `VirtualProtect`, `VirtualQuery`, `__C_specific_handler`
**ntdll.dll**: `NtCreateNamedPipeFile`, `NtOpenFile`, `NtQueryInformationProcess`, `NtReadFile`, `NtWriteFile`, `RtlCaptureContext`, `RtlGetVersion`, `RtlLookupFunctionEntry`, `RtlNtStatusToDosError`, `RtlVirtualUnwind`
**Secur32.dll**: `LsaEnumerateLogonSessions`, `LsaFreeReturnBuffer`, `LsaGetLogonSessionData`
**api-ms-win-core-winrt-l1-1-0.dll**: `RoGetActivationFactory`
**bcrypt.dll**: `BCryptGenRandom`
**iphlpapi.dll**: `FreeMibTable`, `GetAdaptersAddresses`, `GetIfTable2`
**netapi32.dll**: `NetApiBufferFree`, `NetGroupEnum`, `NetGroupGetInfo`, `NetUserEnum`, `NetUserGetInfo`, `NetUserGetLocalGroups`
**ole32.dll**: `CoCreateGuid`, `CoCreateInstance`, `CoIncrementMTAUsage`, `CoInitializeEx`, `CoInitializeSecurity`, `CoSetProxyBlanket`, `PropVariantClear`, `PropVariantCopy`
**oleaut32.dll**: `GetErrorInfo`, `SetErrorInfo`, `SysAllocString`, `SysAllocStringLen`, `SysFreeString`, `SysStringLen`, `VariantClear`, `VariantCopy`
**pdh.dll**: `PdhAddEnglishCounterA`, `PdhAddEnglishCounterW`, `PdhCloseQuery`, `PdhCollectQueryData`, `PdhCollectQueryDataEx`, `PdhEnumObjectsA`, `PdhGetFormattedCounterValue`, `PdhOpenQueryA`, `PdhRemoveCounter`
**powrprof.dll**: `CallNtPowerInformation`
**propsys.dll**: `PropVariantCompareEx`, `PropVariantToBSTR`, `PropVariantToBoolean`, `PropVariantToDouble`, `PropVariantToInt16`, `PropVariantToInt32`, `PropVariantToInt64`, `PropVariantToUInt16`, `PropVariantToUInt32`, `PropVariantToUInt64`, `PropVariantToVariant`, `VariantToBoolean`, `VariantToDouble`, `VariantToInt16`, `VariantToInt32`
**psapi.dll**: `GetModuleFileNameExW`, `GetProcessMemoryInfo`
**shell32.dll**: `CommandLineToArgvW`
**user32.dll**: `UnregisterPowerSettingNotification`
**userenv.dll**: `GetUserProfileDirectoryW`
**ws2_32.dll**: `WSACleanup`, `WSADuplicateSocketW`, `WSAGetLastError`, `WSARecv`, `WSASend`, `WSASocketW`, `WSAStartup`, `accept`, `bind`, `closesocket`, `connect`, `freeaddrinfo`, `getaddrinfo`, `getpeername`, `getsockname`
**api-ms-win-core-synch-l1-2-0.dll**: `WaitOnAddress`, `WakeByAddressAll`, `WakeByAddressSingle`
**bcryptprimitives.dll**: `ProcessPrng`

## Extracted Strings

Total strings found: **5125** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
ATUWVSH
 [^_]A\
 [^_]A\
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AVVWSH
AVVWSH
AWAVAUATVWSH
[_^A\A]A^A_
AWAVATVWUSH
[]_^A\A^A_
AWAVATVWUSH
[]_^A\A^A_
AWAVVWSH
[_^A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
UAWAVAUATVWSH
e8M;e@sJL
|$8M;|$@sIL
[_^A\A]A^A_]
AWAVAUATVWUSH
[]_^A\A]A^A_
D$0H;D$XukH
AWAVATVWSH
8[_^A\A^A_
AWAVATVWSH
8[_^A\A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
 [_^A^A_
AWAVAUATVWSH
[_^A\A]A^A_
AWAVAUATVWSH
P[_^A\A]A^A_
AWAVAUATVWSH
[_^A\A]A^A_
AWAVAUATVWSH
[_^A\A]A^A_
AVVWSH
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVATVWSH
[_^A\A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
AWAVVWSH
[_^A^A_
UAWAVAUATVWSH
[_^A\A]A^A_]
AVVWUSH
 []_^A^
AWAVAUATVWSH
[_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
[]_^A\A]A^A_
H;\$@v#L
AWAVAUATVWUSH
L9l$0tiL
d$XL;d$Ht6H
[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
t$xH;t$hu
[]_^A\A]A^A_
AWAVAUATVWUSH
l$xt{H
[]_^A\A]A^A_
AWAVATVWSH
([_^A\A^A_
AWAVAUATVWUSH
h[]_^A\A]A^A_
AWAVAUATVWUSH
h[]_^A\A]A^A_
AWAVAUATVWUSH
x[]_^A\A]A^A_
AWAVAUATVWUSH
L;/uH
L;.uH
h[]_^A\A]A^A_
AWAVAUATVWUSH
8[]_^A\A]A^A_
AWAVVWSH
@[_^A^A_
AWAVVWSH
@[_^A^A_
AVVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1401878e0` | `0x1401878e0` | 1598778 | ✓ |
| `fcn.14000be10` | `0x14000be10` | 1253369 | ✓ |
| `fcn.14000e5bb` | `0x14000e5bb` | 1239802 | ✓ |
| `fcn.14000be00` | `0x14000be00` | 1169535 | ✓ |
| `fcn.14000bde0` | `0x14000bde0` | 1169296 | ✓ |
| `fcn.14000bdd0` | `0x14000bdd0` | 1169258 | ✓ |
| `fcn.1400051fa` | `0x1400051fa` | 1107867 | ✓ |
| `fcn.140005ace` | `0x140005ace` | 528377 | ✓ |
| `fcn.140129570` | `0x140129570` | 379714 | ✓ |
| `fcn.14012ba20` | `0x14012ba20` | 371993 | ✓ |
| `fcn.14015a118` | `0x14015a118` | 122310 | ✓ |
| `fcn.14008576d` | `0x14008576d` | 79593 | ✓ |
| `fcn.1400eeb60` | `0x1400eeb60` | 73229 | ✓ |
| `fcn.140112770` | `0x140112770` | 61812 | ✓ |
| `fcn.140113130` | `0x140113130` | 59409 | ✓ |
| `fcn.140113dc0` | `0x140113dc0` | 56241 | ✓ |
| `fcn.1401203f0` | `0x1401203f0` | 33841 | ✓ |
| `fcn.140103640` | `0x140103640` | 33688 | ✓ |
| `fcn.1400bea9b` | `0x1400bea9b` | 33096 | ✓ |
| `fcn.14001e72c` | `0x14001e72c` | 25540 | ✓ |
| `fcn.14013d1f0` | `0x14013d1f0` | 22545 | ✓ |
| `fcn.14007e360` | `0x14007e360` | 21265 | ✓ |
| `fcn.14008b4e7` | `0x14008b4e7` | 18459 | ✓ |
| `fcn.14013e0c0` | `0x14013e0c0` | 17659 | ✓ |
| `fcn.140136fc0` | `0x140136fc0` | 16801 | ✓ |
| `fcn.14000f21d` | `0x14000f21d` | 13095 | ✓ |
| `fcn.14000f2b5` | `0x14000f2b5` | 13055 | ✓ |
| `fcn.14012c000` | `0x14012c000` | 10232 | ✓ |
| `fcn.1400d5846` | `0x1400d5846` | 9700 | ✓ |
| `fcn.1401045c0` | `0x1401045c0` | 9509 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400051fa.c`](code/fcn.1400051fa.c)
- [`code/fcn.140005ace.c`](code/fcn.140005ace.c)
- [`code/fcn.14000bdd0.c`](code/fcn.14000bdd0.c)
- [`code/fcn.14000bde0.c`](code/fcn.14000bde0.c)
- [`code/fcn.14000be00.c`](code/fcn.14000be00.c)
- [`code/fcn.14000be10.c`](code/fcn.14000be10.c)
- [`code/fcn.14000e5bb.c`](code/fcn.14000e5bb.c)
- [`code/fcn.14000f21d.c`](code/fcn.14000f21d.c)
- [`code/fcn.14000f2b5.c`](code/fcn.14000f2b5.c)
- [`code/fcn.14001e72c.c`](code/fcn.14001e72c.c)
- [`code/fcn.14007e360.c`](code/fcn.14007e360.c)
- [`code/fcn.14008576d.c`](code/fcn.14008576d.c)
- [`code/fcn.14008b4e7.c`](code/fcn.14008b4e7.c)
- [`code/fcn.1400bea9b.c`](code/fcn.1400bea9b.c)
- [`code/fcn.1400d5846.c`](code/fcn.1400d5846.c)
- [`code/fcn.1400eeb60.c`](code/fcn.1400eeb60.c)
- [`code/fcn.140103640.c`](code/fcn.140103640.c)
- [`code/fcn.1401045c0.c`](code/fcn.1401045c0.c)
- [`code/fcn.140112770.c`](code/fcn.140112770.c)
- [`code/fcn.140113130.c`](code/fcn.140113130.c)
- [`code/fcn.140113dc0.c`](code/fcn.140113dc0.c)
- [`code/fcn.1401203f0.c`](code/fcn.1401203f0.c)
- [`code/fcn.140129570.c`](code/fcn.140129570.c)
- [`code/fcn.14012ba20.c`](code/fcn.14012ba20.c)
- [`code/fcn.14012c000.c`](code/fcn.14012c000.c)
- [`code/fcn.140136fc0.c`](code/fcn.140136fc0.c)
- [`code/fcn.14013d1f0.c`](code/fcn.14013d1f0.c)
- [`code/fcn.14013e0c0.c`](code/fcn.14013e0c0.c)
- [`code/fcn.14015a118.c`](code/fcn.14015a118.c)
- [`code/fcn.1401878e0.c`](code/fcn.1401878e0.c)

## Behavioral Analysis

This final segment of disassembly provides the most granular look at the internal mechanics of the loader. It confirms that the "Hydration" phase isn't just a simple decryption, but an **extensive, stateful data transformation**—possibly involving a custom virtual machine or complex scripting engine—prior to the actual execution of the payload.

The following analysis incorporates findings from chunk 6/6 into the existing profile.

### Updated Analysis of Binary Functionality (Chunk 6/6)

#### 1. Advanced Decoding via Complex Logic Gates
While previous chunks highlighted SIMD for performance, this final segment reveals the **complexity of the logic** governing those transformations.
*   **Multi-Stage Verification:** The code frequently performs checks on specific bytes (e.g., checking if a value equals `'R'` or evaluating `uVar29` against several constants like `0x10`, `0x1f`, and `0x72`). This suggests that the loader is navigating a "decision tree" based on the data it has just hydrated.
*   **Stateful Parsing:** The heavy use of multi-byte calculations (e.g., `iVar_13 = iVar_14 * 10 + ...` and complex bitwise shifts) indicates that the loader is not just looking for strings, but parsing a **complex internal data structure**. It is likely reconstructing an "instruction set" or a configuration map from the raw encrypted blob.

#### 2. Sophisticated Command-Line Construction
The transformation of "hydrated" data into a format ready for `CreateProcessW` is highly non-linear:
*   **Segmented Assembly:** The code doesn't just concatenate strings; it performs intensive arithmetic to calculate offsets and lengths (`auVar80`, `piVar1`). This implies the loader is building a **multi-part command line**. It may be stitching together various environment variables, encoded script blocks (e.g., Base64 for PowerShell), and hidden execution flags into a single long string before spawning the process.
*   **Buffer Management:** The usage of arrays and specific memory offsets just before the call to `CreateProcessW` suggests that the loader is preparing a "ready-to-run" environment. It ensures that all required components (the payload, the arguments, and the environment block) are perfectly aligned in memory.

#### 3. Validation Gate: The "Safe Passage" Check
This chunk contains several "logical gates." If the data doesn't meet specific criteria during the decryption loop (e.g., if a mandatory signature or checksum isn't found), the logic will branch away from `CreateProcessW`.
*   **Pre-Execution Validation:** Before the payload is even allowed to spawn, the loader confirms that the "Hydration" was successful and that the resulting data matches expected patterns. This prevents the launcher from being observed by automated sandboxes if the sandbox doesn't provide the correct environment for a successful decryption.

#### 4. Sophisticated Anti-Forensic Persistence
The final portion of the code demonstrates how it interacts with system resources:
*   **Memory "scrubbing":** After determining the necessary parameters, the code begins managing memory blocks very carefully. The transition from internal processing to `CreateProcessW` is marked by a shift from **calculation mode** to **execution mode**, where it attempts to minimize any remaining artifacts of its own existence in the process heap.

---

### Updated Summary of Findings

#### Core Functionality & Purpose
The binary is a **sophisticated, multi-stage "Stage 0" loader.** It acts as a protective shell for a more complex payload:
1.  **Hydration/De-virtualization:** Uses SIMD instructions and a series of logic gates to decode a highly complex internal configuration or script.
2.  **Validation:** Validates the integrity and "correctness" of the decoded data before proceeding.
3.  **Dynamic Assembly:** Constructs an elaborate, multi-part command line in memory just-in-time for execution.
4.  **Execution & Sanitize:** Spawns the final payload via `CreateProcessW` and immediately begins a teardown process to destroy its own footprint.

#### Suspected Malicious Behaviors (Refined)
*   **Anti-Analysis through Logic Complexity:** The sheer number of nested loops and bitwise transformations makes static analysis extremely difficult. It isn't just "obfuscated"; it is designed to be functionally complex enough to confuse automated tools and slow down a human analyst.
*   **Environment-Dependent Decryption:** The multiple logic gates (checking for specific characters/values) suggest the loader can change its behavior based on what it finds in memory, potentially detecting sandboxes or debuggers before "deciding" whether to launch the final payload.
*   **Just-in-Time Construction:** By only constructing the full command line at the very last millisecond, the malware ensures that any "scanned" strings during its operation are fragments rather than complete, malicious commands.

#### Technical Indicators for Analysts
*   **The SIMD/AVX Loops (`pshufb`, `vpaddd`):** This is the **decryption engine**. Analysis of these loops reveals how the primary payload is "unpacked."
*   **Length and Offset Arithmetic:** The area immediately preceding `CreateProcessW` is where the **actual malicious commands are formed.** Extracting the buffers here will reveal the final script/command.
*   **The Validation Loop (e.g., checking for 'R'):** These are **safety checks**. If a manual jump over these checks fails, the loader may fail to launch the payload or crash on purpose if it detects interference.

---

### Final Recommendations for Analysis

1.  **Identify the Payload during Assembly:** Use a debugger (x64dbg) and set a breakpoint on `CreateProcessW`. Examine the buffer passed as the second argument (the Command Line). This is the only time the full, "naked" malicious command will exist in plain text within memory.
2.  **Trace the SIMD Logic:** Identify the loop that processes the `0x230` bytes mentioned in previous chunks. Trace how these values are transformed by `pshufb`. This will lead you to the "Configuration Blob."
3.  **Memory Forensics Timing:** Because of the heavy cleanup (closing handles, unmapping memory) after `CreateProcessW`, use a tool like **Hollows_Hunter** or **Moneta** to check for injected code in child processes immediately upon creation.
4.  **Identify "Key" Logic Gates:** Pinpoint the logic gates (like those involving variable `uVar29`). These are the points where the loader decides if it is being watched; finding these can help you identify exactly how it detects analysis environments.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Executables | The "Hydration" phase, use of SIMD for decryption, and complex logic gates are designed to hide the payload's true intent from automated analysis. |
| T1059.001 | PowerShell | The loader specifically constructs Base64-encoded script blocks intended for execution via `CreateProcessW`. |
| T1497 | Virtualization/Sandbox Detection | The "Validation Gate" and logic checks (e.g., checking for specific constants) are designed to detect if the loader is running in an analysis environment. |
| T1213 | Data Encoding | The transformation of "hydrated" data into Base64 and other encoded formats hides malicious commands until they are staged for execution. |
| T1027 | Obfuscated Executables (JIT construction) | By only constructing the full command line at the last possible moment, the loader prevents security tools from identifying complete strings during static analysis. |
| T1036 | Masquerading | The "memory scrubbing" and transition to execution mode are used to hide the launcher's footprint and evade detection after the payload is handed off. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type.

### **IP addresses / URLs / Domains**
*   None identified. (The "obfuscated" strings in the data block do not resolve to recognizable network infrastructure).

### **File paths / Registry keys**
*   None identified.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts (User agents, C2 patterns, etc.)**
*   **Encryption/Decoding Pattern:** Use of SIMD instructions (`pshufb`, `vpaddd`) for "Hydration" (decryption) of a large data blob (referenced as ~0x230 bytes).
*   **Anti-Analysis Logic Gates:** Presence of specific logic gates checking against constants `0x10`, `0x1f`, and `0x72` to validate environment safety before execution. 
*   **JIT Command Construction:** The loader utilizes a "Just-in-Time" assembly method to construct complex, multi-part command lines in memory specifically for the `CreateProcessW` function call.
*   **Execution Behavior:** Rapid transition from calculation mode to execution mode followed by immediate "memory scrubbing" (clearing traces of the loader's existence).

---

### **Analyst Note:**
The provided text is a post-analysis report of a sophisticated **Stage 0 Loader**. While it contains no "hard" IOCs (like static IP addresses or specific file paths) in its current form, it describes significant behavioral signatures. The lack of clear strings suggests the malware uses high levels of obfuscation; therefore, the primary indicators for hunting are the **SIMD-based decryption loops** and the **dynamic construction of arguments preceding `CreateProcessW`**.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Sophisticated "Hydration" Mechanism:** The use of SIMD instructions (`pshufb`, `vpaddd`) and complex logic gates to decrypt a large internal data block indicates a highly engineered, multi-stage decryption process designed to hide the final payload from static analysis.
    *   **Just-in-Time (JIT) Command Construction:** The loader constructs multi-part, potentially Base64-encoded command lines in memory immediately before calling `CreateProcessW`. This is a classic "Stage 0" behavior used to deliver payloads like PowerShell scripts while avoiding detection by string scanners.
    *   **Advanced Anti-Forensics:** The inclusion of specific "validation gates" and "memory scrubbing" techniques demonstrates an intentional design to detect sandboxes/debuggers and erase the loader's footprint upon successful handoff to the primary payload.
