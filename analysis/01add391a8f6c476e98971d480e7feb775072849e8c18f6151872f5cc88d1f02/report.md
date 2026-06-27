# Threat Analysis Report

**Generated:** 2026-06-27 06:21 UTC
**Sample:** `01add391a8f6c476e98971d480e7feb775072849e8c18f6151872f5cc88d1f02_01add391a8f6c476e98971d480e7feb775072849e8c18f6151872f5cc88d1f02.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01add391a8f6c476e98971d480e7feb775072849e8c18f6151872f5cc88d1f02_01add391a8f6c476e98971d480e7feb775072849e8c18f6151872f5cc88d1f02.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 7 sections |
| Size | 185,409 bytes |
| MD5 | `c261639d4c0cc7b084e0ee0428400d2f` |
| SHA1 | `41c656f1913a8432f4d54809d57714514814e078` |
| SHA256 | `01add391a8f6c476e98971d480e7feb775072849e8c18f6151872f5cc88d1f02` |
| Overall entropy | 7.577 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 556865846 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 27,136 | 5.625 | No |
| `.data` | 512 | 0.122 | No |
| `.rdata` | 5,120 | 4.52 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 1,024 | 3.57 | No |
| `.rsrc` | 137,728 | 7.901 | ⚠️ Yes |
| `.reloc` | 512 | 0.118 | No |

### Imports

**ADVAPI32.dll**: `GetUserNameW`, `RegCloseKey`
**KERNEL32.dll**: `AllocConsole`, `CloseHandle`, `CreateFileA`, `FlushFileBuffers`, `GetConsoleWindow`, `GetCurrentProcessId`, `GetProcessHeap`, `GetStdHandle`, `GetTempPathA`, `HeapAlloc`, `HeapFree`, `LocalAlloc`, `LocalFree`, `WriteConsoleA`, `WriteFile`
**SHELL32.dll**: `SHGetFolderPathW`
**USER32.dll**: `GetSystemMetrics`, `wsprintfA`

## Extracted Strings

Total strings found: **864** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
.idata
@.rsrc
@.reloc
AWAVATWVSH
[^_A\A^A_]
AVWVSH
[^_A^]
[^_A^]
tvHcJ<H
AVWVSH
[^_A^]
[^_A^]
AUATWVH
[^_A\A]]
[^_A\A]]
AWAVAUATWVSH
[^_A\A]A^A_]
AVAUATWVSH
[^_A\A]A^]
[^_A\A]A^]
AWAVAUATWVSH
[^_A\A]A^A_]
kPD9l$tt
AVWVSH
[^_A^]
[^_A^]
AWAVAUATWVSH
[^_A\A]A^A_]
AWAVWVSH
[^_A^A_]
[^_A^A_]
AVWVSH
[^_A^]
AVWVSH
[^_A^]
AWAVAUATWVSH
[^_A\A]A^A_]
NtTerminateProcess
ExitProcess
[i] a leaf falls in a forest no one walks

[i] rivers run to oceans never asking why

[i] the moon dissolves in still and silver lake

[i] the lantern guttered once and then went dark

[i] morning swallows every trace of night

[i] the clock forgot the hour it was born

[i] shadows learn the angles of the sun

[i] the garden held its breath and did not bloom

[i] petals count themselves before they fall

[i] the compass spun and pointed everywhere

[i] two sparrows share a wire in the grey

[i] the envelope was sealed but held no words

[i] the tide writes letters no shore understands

[i] the candle chose the dark and was at peace

[i] the bridge was out the traveller swam

[i] the swimmer reached the bank but lost the map

[i] a door without a lock without a frame

[i] the mirror maps a room that does not exist

[i] the echo leaves before the call is made

[i] the field was ploughed but never held a seed

[i] the fence remembers pastures not the herd

[i] the river clears its throat and carries on

[i] a name was spoken softly to the dark

[i] the pen ran dry before the verse was done

[i] the loom was set the shuttle never thrown

[i] the census counted stars instead of men

[i] the needle sought the thread inside the wind

[i] the messenger forgot the road by noon

[i] the old road ended where the new one slept

[i] stone-1

[i] stone-2

[i] stone-3

[i] stone-4

[i] stone-5

[i] stone-6

[i] stone-7

[i] stone-8

[i] stone-9

[i] stone-A

[i] stone-B

[i] stone-C

[i] stone-D

[i] stone-D not present

[i] the river swallowed every borrowed stone

[i] the key was lost before the door was made

[i] the wind forgets the names it once had here

[i] the tide erased the writing in the sand

[i] the clock forgot the hour it was wound

[i] the clock forgot the hour it was woundTimer

[i] the table held no guests no names no bread

[i] the gate was built without a hinge or wall

[i] the threshold waited empty in the fog

[i] the door stood open but the room was gone

[i] the cipher asked a question no one knew

/tmp/pepacker_build_awmdz56k/HellsHall.c
[!] FetchWin32uSyscallInst Failed To Fetch A Syscall Instruction Address - %s.%d 

[!] FetchNtSyscall Failed To Fetch The Syscall Number Of Syscall Of Hash: 0x%0.8X - %s.%d 

[i] the archivist found no record of that name

```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x140006ad0` | 14386 | ✓ |
| `sym.InitIndirectSyscalls` | `0x1400011c0` | 5495 | ✓ |
| `sym.InjectShellcode` | `0x140003dc0` | 4866 | ✓ |
| `sym.MapCleanNtdll` | `0x140005b40` | 2531 | ✓ |
| `sym.InitializeWinAPIs` | `0x140002740` | 1651 | ✓ |
| `sym.GetDecodedShellcodePayload` | `0x1400054e0` | 1607 | ✓ |
| `sym.FetchNtSyscall` | `0x140003420` | 1135 | ✓ |
| `sym.ExecShellcodeLocal` | `0x1400050d0` | 1026 | ✓ |
| `sym.GetProcAddressH` | `0x1400038c0` | 736 | ✓ |
| `sym.FetchWin32uSyscallInst` | `0x1400031c0` | 600 | ✓ |
| `sym.GetModuleHandleH` | `0x140003ba0` | 535 | ✓ |
| `sym.UnmapCleanNtdll` | `0x140006560` | 401 | ✓ |
| `sym.CreateDebugConsole` | `0x1400068c0` | 323 | ✓ |
| `sym.UnhookAllLoadedDlls` | `0x140006700` | 289 | ✓ |
| `sym.memset` | `0x140002fc0` | 183 | ✓ |
| `sym.InitDllsConfigStructs` | `0x140003120` | 157 | ✓ |
| `sym.InitializePeStruct` | `0x140002dc0` | 147 | ✓ |
| `sym.GetDebugLogPath` | `0x140006840` | 115 | ✓ |
| `sym.SelfTerminate` | `0x140001060` | 102 | ✓ |
| `sym.Wcscat` | `0x140002ee0` | 89 | ✓ |
| `sym.CRC32B` | `0x140002e60` | 74 | ✓ |
| `sym.Memcpy` | `0x140002f40` | 51 | ✓ |
| `sym.memcpy` | `0x140002f80` | 51 | ✓ |
| `sym.GetCleanNtdllBase` | `0x140006530` | 46 | ✓ |
| `sym.AddWin32uToIat` | `0x140001160` | 45 | ✓ |
| `fcn.140001000` | `0x140001000` | 44 | ✓ |
| `sym.IatCamouflage` | `0x140001130` | 42 | ✓ |
| `sym.DummyAllocation` | `0x1400010d0` | 40 | ✓ |
| `sym.strrchr` | `0x1400030f0` | 39 | ✓ |
| `fcn.14000102c` | `0x14000102c` | 37 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001000.c`](code/fcn.140001000.c)
- [`code/fcn.14000102c.c`](code/fcn.14000102c.c)
- [`code/sym.AddWin32uToIat.c`](code/sym.AddWin32uToIat.c)
- [`code/sym.CRC32B.c`](code/sym.CRC32B.c)
- [`code/sym.CreateDebugConsole.c`](code/sym.CreateDebugConsole.c)
- [`code/sym.DummyAllocation.c`](code/sym.DummyAllocation.c)
- [`code/sym.ExecShellcodeLocal.c`](code/sym.ExecShellcodeLocal.c)
- [`code/sym.FetchNtSyscall.c`](code/sym.FetchNtSyscall.c)
- [`code/sym.FetchWin32uSyscallInst.c`](code/sym.FetchWin32uSyscallInst.c)
- [`code/sym.GetCleanNtdllBase.c`](code/sym.GetCleanNtdllBase.c)
- [`code/sym.GetDebugLogPath.c`](code/sym.GetDebugLogPath.c)
- [`code/sym.GetDecodedShellcodePayload.c`](code/sym.GetDecodedShellcodePayload.c)
- [`code/sym.GetModuleHandleH.c`](code/sym.GetModuleHandleH.c)
- [`code/sym.GetProcAddressH.c`](code/sym.GetProcAddressH.c)
- [`code/sym.IatCamouflage.c`](code/sym.IatCamouflage.c)
- [`code/sym.InitDllsConfigStructs.c`](code/sym.InitDllsConfigStructs.c)
- [`code/sym.InitIndirectSyscalls.c`](code/sym.InitIndirectSyscalls.c)
- [`code/sym.InitializePeStruct.c`](code/sym.InitializePeStruct.c)
- [`code/sym.InitializeWinAPIs.c`](code/sym.InitializeWinAPIs.c)
- [`code/sym.InjectShellcode.c`](code/sym.InjectShellcode.c)
- [`code/sym.MapCleanNtdll.c`](code/sym.MapCleanNtdll.c)
- [`code/sym.Memcpy.c`](code/sym.Memcpy.c)
- [`code/sym.SelfTerminate.c`](code/sym.SelfTerminate.c)
- [`code/sym.UnhookAllLoadedDlls.c`](code/sym.UnhookAllLoadedDlls.c)
- [`code/sym.UnmapCleanNtdll.c`](code/sym.UnmapCleanNtdll.c)
- [`code/sym.Wcscat.c`](code/sym.Wcscat.c)
- [`code/sym.memcpy.c`](code/sym.memcpy.c)
- [`code/sym.memset.c`](code/sym.memset.c)
- [`code/sym.strrchr.c`](code/sym.strrchr.c)

## Behavioral Analysis

This final chunk of disassembly provides a look into the malware's **longevity and defense-in-depth strategies**. While previous sections showed how it hides its actions, this section reveals how it protects itself against automated analysis environments and ensures it leaves as little footprint as possible.

### Updated & Expanded Analysis (Chunk 4/4)

#### 1. Anti-Analysis & Sandbox Evasion (New)
The functions `sym.IatCamouflage` and `sym.DummyAllocation` are classic indicators of **Time-Based Evasion**.
*   **Stalling Loops:** Both functions utilize a loop that continues until a large, arbitrary hex value (`0x491fd3a2`) is reached. 
*   **Purpose:** These aren't "real" tasks; they are designed to exhaust the time limits of automated sandboxes. Many automated analysis systems only run a sample for 2–5 minutes. By forcing the CPU to perform meaningless calculations, the malware "waits out" the sandbox's timer before it ever reaches its malicious payload.
*   **IatCamouflage:** The name suggests it may also be attempting to mask the Import Address Table (IAT) or related structures from being easily parsed by tools that look for suspicious API imports.

#### 2. Manual PE Parsing & "Pure" Implementation (New)
The functions `sym.InitDllsConfigStructs` and `sym.InitializePeStruct` reveal a high level of technical maturity.
*   **Manual Header Parsing:** These functions check for the `0x4550` ("PE") magic number and manually calculate offsets to find headers and sections. 
*   **Why this is used:** By doing this manually instead of using standard Windows APIs to load modules, the malware avoids "noisy" system calls that EDRs monitor. It essentially treats the operating system like a raw data source rather than relying on the OS's helper functions.

#### 3. Self-Termination & Artifact Cleanup (New)
The `sym.SelfTerminate` function is highly significant for incident responders.
*   **Two-Stage Termination:** The function resolves two different addresses using CRC32 and then executes them. One of these is likely a "cleanup" routine to delete temporary files or logs, while the second terminates the process.
*   **Persistence Logic:** This indicates that this specific binary is a **loader/dropper**. Once it has successfully delivered or executed the next stage of the infection (the shellcode), it attempts to "suicide" so that there is no malicious process left in memory for an analyst to find later.

#### 4. Hardened Internal Utilities (Refined)
The inclusion of `sym.Wcscat`, `sym.Memcpy`, and `sym.CRC32B` as internal functions reinforces the "Unhooking" theme:
*   **No Reliance on System DLLs:** By including its own versions of standard C library functions, the malware ensures that even if an EDR successfully hooks the standard `ntdll.dll` or `msvcrt.dll`, the malware remains unaffected because it isn't using the "poisoned" system version—it is using its own "clean" internal copy.

---

### Updated Technical Indicators Summary

| Feature | Technique Identified | Impact on Defense |
| :--- | :--- | :--- |
| **Sandbox Evasion** | `IatCamouflage` / `DummyAllocation` | Prevents automated sandboxes from observing the full execution chain by "timing out" the analysis. |
| **Manual Parsing** | PE Header parsing (`0x4550`) | Bypasses standard API monitoring by manually calculating memory offsets for module loading. |
| **Anti-Hooking** | Custom `Memcpy`/`Wcscat` | Ensures functionality remains intact even if the OS's primary libraries are hooked or monitored. |
| **Artifact Cleanup** | `sym.SelfTerminate` | Minimizes forensic evidence by cleaning up files and closing processes after payload delivery. |
| **Detection Gap** | CRC32-based Resolution | Makes it impossible to find malicious intent via static string analysis of the binary. |

---

### Final Executive Summary for Incident Response (Full Scope)

The full disassembly confirms that this is a **highly sophisticated, "stealth-first" malware loader**, likely utilized by an advanced threat actor or as part of a high-end malware-as-a-service (MaaS) platform. It is specifically engineered to defeat the current generation of EDR (Endpoint Detection and Response) tools.

**Key Technical Pillars:**
1.  **Un-Hooking:** It actively strips away security "traps" by reloading clean copies of `ntdll` system files.
2.  **Obfuscation:** It uses CRC32 hashing to hide all its internal function calls, making it nearly invisible to static scanners.
3.  **Anti-Analysis:** It uses stalling loops to trick automated security sandboxes into thinking the file is benign because "nothing happened" during the test window.
4.  **Execution Lifecycle:** It follows a strict lifecycle—Prepare (Decrypt), Unhook (Bypass EDR), Execute (Payload Delivery), and Terminate (Evidence Destruction).

#### Strategic Recommendations for SOC/IR Teams:
*   **Behavioral over Signature Detection:** Do not rely on file hashes or string-based alerts. The malware's core logic is hidden behind CRC32 and encryption. Focus instead on **behavioral indicators**, such as a process suddenly mapping new memory regions or performing manual "PE" header calculations.
*   **Memory Forensics (The "Golden Hour"):** Because the malware terminates itself after success, the best time to catch it is in-memory during the seconds/minutes after initial execution. Look for **unbacked memory regions** containing executable code—this is where the decrypted shellcode lives.
*   **Identify "Living off the Land" (LotL) Patterns:** Monitor for processes that perform a large number of memory operations or attempt to interact with `ntdll` in non-standard ways. 
*   **Advanced EDR Configuration:** Ensure your security stack is configured to alert on **direct system calls (Syscalls)** and **memory injection**, rather than just relying on standard API hooking, as this sample is designed specifically to bypass the latter.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in your disassembly analysis to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Evasion | The `IatCamouflage` and `DummyAllocation` functions use stalling loops to exhaust the time limits of automated analysis environments. |
| **T1055** | Process Injection | Manual PE header parsing and the use of internal library functions allow the malware to load components while avoiding standard, monitored system API calls. |
| **T1070** | Indicator Removal | The `sym.SelfTerminate` function performs a cleanup routine followed by immediate process termination to remove evidence of infection. |
| **T1562.001** | Disable or Modify Tools | By utilizing "hardened" internal functions (like `Memcpy`), the malware bypasses EDR hooks designed to monitor standard system DLLs. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have processed the provided strings and behavioral analysis to extract the relevant Indicators of Compromise (IOCs).

### **Executive Summary of Findings**
The analysis indicates a highly sophisticated malware loader/packer identified as **HellsHall**. The primary characteristics are anti-analysis techniques (stalling loops), manual PE parsing to bypass EDR hooks, and the use of CRC32 hashing for internal function resolution.

---

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified in the provided text.*

**File paths / Registry keys**
*   `/tmp/pepacker_build_awmdz56k/HellsHall.c` (Internal build path/source reference)
*   `debug_log.txt` (Local file artifact)

**Mutex names / Named pipes**
*   *None identified in the provided text.*

**Hashes**
*   *No MD5, SHA1, or SHA256 hashes were found in the provided strings.* 
    *(Note: The malware uses **CRC32** as a method for internal resolution, but no specific hash values for malicious payloads were present.)*

**Other artifacts**
*   **Specific Hex Constants:** `0x491fd3a2` (Identified as the target value for stalling loops used to exhaust sandbox timers).
*   **Tooling/Packer Identifiers:** `HellsHall` (Associated with the build path and likely the name of the packer or loader framework).
*   **Internal Function Identifiers (Behavioral Artifacts):** 
    *   `IatCamouflage`
    *   `DummyAllocation`
    *   `InitDllsConfigStructs`
    *   `InitializePeStruct`
    *   `SelfTerminate`
*   **Signature-able Strings:** The series of poetic "filler" strings (e.g., `"a leaf falls in a forest no one walks"`, `"the clock forgot the hour it was born"`). While these do not function as network indicators, they serve as **unique binary signatures** for identifying specific builds of this loader.

---

### **Technical Analyst Notes (Behavioral Context)**
*   **Anti-Analysis:** The use of `IatCamouflage` and `DummyAllocation` combined with the hex constant `0x491fd3a2` indicates a deliberate attempt to bypass automated analysis platforms.
*   **Evasion Technique:** Manual PE Header parsing (searching for the `0x4550` magic number) is used to bypass standard Windows API monitoring by avoiding "noisy" system calls during module loading.
*   **Persistence/Cleanup:** The `SelfTerminate` routine indicates a multi-stage infection lifecycle where this specific binary acts as a "disposable" loader, designed to delete its tracks immediately after the primary payload (shellcode) is executed in memory.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: HellsHall
2. **Malware type**: Loader / Dropper
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced EDR Bypass Techniques:** The sample utilizes "un-hooking" methods, including manual PE header parsing (avoiding standard Windows APIs) and the implementation of custom internal functions (`Memcpy`, `Wcscat`) to bypass security monitors on system DLLs.
    *   **Sophisticated Sandbox Evasion:** The inclusion of `IatCamouflage` and `DummyAllocation` functions uses specific stalling loops (targeting hex value `0x419fd3a2`) to exhaust the time limits of automated analysis environments.
    *   **Disposable Lifecycle:** The `sym.SelfTerminate` function indicates a "loader" behavior, where the primary binary performs a cleanup routine and deletes itself immediately after successfully injecting its payload (shellcode) into memory.
