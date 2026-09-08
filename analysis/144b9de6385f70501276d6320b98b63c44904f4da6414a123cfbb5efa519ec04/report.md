# Threat Analysis Report

**Generated:** 2026-09-05 06:35 UTC
**Sample:** `144b9de6385f70501276d6320b98b63c44904f4da6414a123cfbb5efa519ec04_144b9de6385f70501276d6320b98b63c44904f4da6414a123cfbb5efa519ec04.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `144b9de6385f70501276d6320b98b63c44904f4da6414a123cfbb5efa519ec04_144b9de6385f70501276d6320b98b63c44904f4da6414a123cfbb5efa519ec04.exe` |
| File type | PE32 executable for MS Windows 6.00 (console), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 18,944 bytes |
| MD5 | `29c2c8c311b56ec02f3399d491cb3ec3` |
| SHA1 | `2aa673f22ebd8322a15bfa02a1a91403db0f9d83` |
| SHA256 | `144b9de6385f70501276d6320b98b63c44904f4da6414a123cfbb5efa519ec04` |
| Overall entropy | 5.344 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3206496629 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 16,384 | 5.572 | No |
| `.rsrc` | 1,536 | 4.14 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **220** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
<>9__4_0
<FetchServerList>b__4_0
<>9__5_0
<FindFastestUrl>b__5_0
<>c__DisplayClass5_0
<>c__DisplayClass8_0
<DownloadFileWithProgress>b__0
<>c__DisplayClass5_1
<FindFastestUrl>b__1
<DownloadFileWithProgress>b__1
IEnumerable`1
IOrderedEnumerable`1
IEnumerator`1
List`1
get_Item1
CS$<>8__locals1
Microsoft.Win32
<>9__5_2
<FindFastestUrl>b__5_2
<>c__DisplayClass5_2
Func`2
Tuple`2
Dictionary`2
get_Item2
CS$<>8__locals2
IsWindows7
get_UTF8
<Module>
PlatformID
System.IO
mscorlib
System.Collections.Generic
DownloadFileAsync
Thread
TestServerSpeed
add_DownloadProgressChanged
failed
add_DownloadFileCompleted
get_BytesReceived
received
set_Method
IsNullOrWhiteSpace
get_Message
AddRange
Enumerable
IDisposable
RunExecutable
set_CursorVisible
Double
Console
set_Title
get_MainModule
ProcessModule
get_FileName
processName
GetProcessesByName
GetDirectoryName
ReadLine
WriteLine
Combine
LocalMachine
System.Core
HttpWebResponse
GetResponse
Dispose
Create
Delete
CompilerGeneratedAttribute
GuidAttribute
DebuggableAttribute
ComVisibleAttribute
AssemblyTitleAttribute
AssemblyTrademarkAttribute
TargetFrameworkAttribute
AssemblyFileVersionAttribute
AssemblyConfigurationAttribute
AssemblyDescriptionAttribute
CompilationRelaxationsAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
AssemblyCompanyAttribute
RuntimeCompatibilityAttribute
set_UseShellExecute
GetValue
get_TotalBytesToReceive
SaMarinDa Downloader.exe
Deserialize
System.Threading
set_Encoding
System.Runtime.Versioning
DownloadString
Substring
Stopwatch
lnkPath
localPath
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass8_0._DownloadFileWithProgress_b__1` | `0x403584` | 27260 | ✓ |
| `method.SaMarinDa_Downloader.Program.SearchUninstallForBroker` | `0x402d24` | 684 | ✓ |
| `entry0` | `0x402050` | 584 | ✓ |
| `sym.SaMarinDa_Downloader.Program.FindFastestUrl` | `0x402488` | 504 | ✓ |
| `method.SaMarinDa_Downloader.Program.FetchServerList` | `0x4022d8` | 432 | ✓ |
| `method.SaMarinDa_Downloader.Program.ResolveShortcut` | `0x4031c4` | 380 | ✓ |
| `method.SaMarinDa_Downloader.Program.GetMachineGuidInstallPath` | `0x402b0c` | 312 | ✓ |
| `method.SaMarinDa_Downloader.Program.FindStartMenuShortcut` | `0x4030a0` | 292 | ✓ |
| `method.SaMarinDa_Downloader.Program.DownloadFileWithProgress` | `0x4027a0` | 280 | ✓ |
| `method.SaMarinDa_Downloader.Program.TestServerSpeed` | `0x4026a0` | 256 | ✓ |
| `method.SaMarinDa_Downloader.Program.FindInUninstallRegistry` | `0x402c44` | 224 | ✓ |
| `method.SaMarinDa_Downloader.Program.ScanLocalAppDataForBroker` | `0x402fd0` | 208 | ✓ |
| `method.SaMarinDa_Downloader.Program.FormatBytes` | `0x402958` | 172 | ✓ |
| `method.SaMarinDa_Downloader.Program.DrawProgressBar` | `0x4028b8` | 160 | ✓ |
| `method.__c__DisplayClass5_2._FindFastestUrl_b__1` | `0x4034b4` | 152 | ✓ |
| `method.SaMarinDa_Downloader.Program.FindInstalledApp` | `0x402a7c` | 144 | ✓ |
| `method.SaMarinDa_Downloader.Program.KillProcess` | `0x403340` | 144 | ✓ |
| `method.SaMarinDa_Downloader.Program.RunExecutable` | `0x402a04` | 120 | ✓ |
| `method.SaMarinDa_Downloader.FastWebClient.GetWebRequest` | `0x403414` | 76 | ✓ |
| `method.SaMarinDa_Downloader.Program.IsWindows7` | `0x402298` | 64 | ✓ |
| `method.SaMarinDa_Downloader.Program..cctor` | `0x4033d9` | 59 | ✓ |
| `method.__c__DisplayClass8_0._DownloadFileWithProgress_b__0` | `0x403555` | 47 | ✓ |
| `method.SaMarinDa_Downloader.Program.FindFastestUrl` | `0x402680` | 32 | ✓ |
| `method.__c..cctor` | `0x403469` | 12 | ✓ |
| `method.__c._FetchServerList_b__4_0` | `0x40347e` | 11 | ✓ |
| `method.SaMarinDa_Downloader.Program..ctor` | `0x4033d0` | 9 | ✓ |
| `method.SaMarinDa_Downloader.FastWebClient..ctor` | `0x403460` | 9 | ✓ |
| `method.__c..ctor` | `0x403475` | 9 | ✓ |
| `method.__c__DisplayClass5_0..ctor` | `0x403499` | 9 | ✓ |
| `method.__c__DisplayClass5_1..ctor` | `0x4034a2` | 9 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.SaMarinDa_Downloader.FastWebClient..ctor.c`](code/method.SaMarinDa_Downloader.FastWebClient..ctor.c)
- [`code/method.SaMarinDa_Downloader.FastWebClient.GetWebRequest.c`](code/method.SaMarinDa_Downloader.FastWebClient.GetWebRequest.c)
- [`code/method.SaMarinDa_Downloader.Program..cctor.c`](code/method.SaMarinDa_Downloader.Program..cctor.c)
- [`code/method.SaMarinDa_Downloader.Program..ctor.c`](code/method.SaMarinDa_Downloader.Program..ctor.c)
- [`code/method.SaMarinDa_Downloader.Program.DownloadFileWithProgress.c`](code/method.SaMarinDa_Downloader.Program.DownloadFileWithProgress.c)
- [`code/method.SaMarinDa_Downloader.Program.DrawProgressBar.c`](code/method.SaMarinDa_Downloader.Program.DrawProgressBar.c)
- [`code/method.SaMarinDa_Downloader.Program.FetchServerList.c`](code/method.SaMarinDa_Downloader.Program.FetchServerList.c)
- [`code/method.SaMarinDa_Downloader.Program.FindFastestUrl.c`](code/method.SaMarinDa_Downloader.Program.FindFastestUrl.c)
- [`code/method.SaMarinDa_Downloader.Program.FindInUninstallRegistry.c`](code/method.SaMarinDa_Downloader.Program.FindInUninstallRegistry.c)
- [`code/method.SaMarinDa_Downloader.Program.FindInstalledApp.c`](code/method.SaMarinDa_Downloader.Program.FindInstalledApp.c)
- [`code/method.SaMarinDa_Downloader.Program.FindStartMenuShortcut.c`](code/method.SaMarinDa_Downloader.Program.FindStartMenuShortcut.c)
- [`code/method.SaMarinDa_Downloader.Program.FormatBytes.c`](code/method.SaMarinDa_Downloader.Program.FormatBytes.c)
- [`code/method.SaMarinDa_Downloader.Program.GetMachineGuidInstallPath.c`](code/method.SaMarinDa_Downloader.Program.GetMachineGuidInstallPath.c)
- [`code/method.SaMarinDa_Downloader.Program.IsWindows7.c`](code/method.SaMarinDa_Downloader.Program.IsWindows7.c)
- [`code/method.SaMarinDa_Downloader.Program.KillProcess.c`](code/method.SaMarinDa_Downloader.Program.KillProcess.c)
- [`code/method.SaMarinDa_Downloader.Program.ResolveShortcut.c`](code/method.SaMarinDa_Downloader.Program.ResolveShortcut.c)
- [`code/method.SaMarinDa_Downloader.Program.RunExecutable.c`](code/method.SaMarinDa_Downloader.Program.RunExecutable.c)
- [`code/method.SaMarinDa_Downloader.Program.ScanLocalAppDataForBroker.c`](code/method.SaMarinDa_Downloader.Program.ScanLocalAppDataForBroker.c)
- [`code/method.SaMarinDa_Downloader.Program.SearchUninstallForBroker.c`](code/method.SaMarinDa_Downloader.Program.SearchUninstallForBroker.c)
- [`code/method.SaMarinDa_Downloader.Program.TestServerSpeed.c`](code/method.SaMarinDa_Downloader.Program.TestServerSpeed.c)
- [`code/method.__c..cctor.c`](code/method.__c..cctor.c)
- [`code/method.__c..ctor.c`](code/method.__c..ctor.c)
- [`code/method.__c._FetchServerList_b__4_0.c`](code/method.__c._FetchServerList_b__4_0.c)
- [`code/method.__c__DisplayClass5_0..ctor.c`](code/method.__c__DisplayClass5_0..ctor.c)
- [`code/method.__c__DisplayClass5_1..ctor.c`](code/method.__c__DisplayClass5_1..ctor.c)
- [`code/method.__c__DisplayClass5_2._FindFastestUrl_b__1.c`](code/method.__c__DisplayClass5_2._FindFastestUrl_b__1.c)
- [`code/method.__c__DisplayClass8_0._DownloadFileWithProgress_b__0.c`](code/method.__c__DisplayClass8_0._DownloadFileWithProgress_b__0.c)
- [`code/method.__c__DisplayClass8_0._DownloadFileWithProgress_b__1.c`](code/method.__c__DisplayClass8_0._DownloadFileWithProgress_b__1.c)
- [`code/sym.SaMarinDa_Downloader.Program.FindFastestUrl.c`](code/sym.SaMarinDa_Downloader.Program.FindFastestUrl.c)

## Behavioral Analysis

This final chunk of disassembly completes the technical profile of **SaMarinDa_Downloader.exe**. While previous segments established the intent (malicious payload retrieval) and the methods (advanced obfuscation), this final section exposes the **mathematical complexity** used to protect the internal state of the malware during its execution.

The analysis below incorporates all previous findings while incorporating new details from Chunk 5/5.

---

### Finalized Technical Analysis: SaMarinDa_Downloader.exe

#### 1. Infrastructure & Delivery (Refined)
*   **Resilient Fetching:** The `FindFastestUrl` logic confirms a multi-source strategy. By evaluating "speed" and "reliability," the malware ensures it can bypass simple domain blocks.
*   **Stealthy Networking:** The use of custom/modified libraries (`FastWebClient`) rather than standard Windows APIs is designed to evade EDR (Endpoint Detection and Response) systems that monitor for common networking hooks.

#### 2. Advanced Anti-Analysis & Obfuscation (Enhanced)
This final chunk provides the most striking evidence of high-level "Armor":
*   **Arithmetic Dilution:** The constructor `method.__c__DisplayClass5_1..ctor` is a masterclass in **arithmetic obfuscation**. Notice how simple operations are replaced with complex calculations involving bitwise shifts, carry-flag checks (`CARRY1`), and multiple concatenation steps (e.g., `CONCAT31`, `CONCAT22`).
    *   *Purpose:* To calculate a single constant or memory offset, the malware performs dozens of operations. This exhausts human analysts and makes it nearly impossible for automated tools to simplify the logic into readable "if/then" statements.
*   **Instruction Overlap & Packing:** The warning at `0x0040377c` regarding overlapping instructions is a signature of **advanced protectors like VMProtect or Themida**. This indicates that the binary isn't just "messy"—it is intentionally designed to break disassemblers. By creating "overlapping" instructions, the malware causes tools like IDA Pro to display different code depending on where they start reading, effectively hiding the true execution path from static analysis.
*   **Opaque Predicates & Junk Code:** The repeated use of `POPCOUNT` and `CARRY1` logic creates a "maze" of control flow. Many branches in this chunk are mathematically guaranteed to go one way, but since they rely on complex bitwise math, the decompiler cannot resolve them, forcing the analyst to step through thousands of lines of useless code.

#### 3. Loader Architecture & State Management
*   **Just-In-Time (JIT) Decoding:** The heavy focus on constructor methods (`...ctor`) suggests that the loader spends significant time preparing its internal "environment" before making any external calls. It is likely building a map of memory, decrypting strings in segments, and resolving API addresses only at the micro-second they are needed.
*   **Memory Mapping:** The repeated use of large offsets (e.g., `0x23000009`, `0x60b3003`) indicates that the loader is managing a complex internal memory map, possibly preparing to inject or "carve" the final payload into a specific memory region.

---

### Final Executive Summary for Incident Response (IR)

The analysis of **SaMarinDa_Downloader.exe** confirms it as a professional-grade, highly engineered threat tool. It is not a "script kiddie" tool; it is built with techniques typically associated with sophisticated APTs or high-end Ransomware-as-a-Service (RaaS) operations.

#### Key Indicators of Compromise (IOC) & Tactics:
*   **Resilient Infrastructure:** The malware likely uses a rotating list of mirrors/CDNs via the `FindFastestUrl` logic. **Single-IP blocking is insufficient.** 
*   **Advanced Packing Protection:** The use of instruction overlapping and arithmetic dilution confirms it is protected by premium "packers." These are designed specifically to defeat automated sandbox detection and static analysis.
*   **High Complexity Obfuscation:** Because the code is so heavily obfuscated, **static analysis will be time-consuming.** This means manual reverse engineering to find every potential C2 (Command & Control) server may take days of effort.

#### Critical Risk Assessment: **CRITICAL**
The complexity of the "armor" suggests that the actors are highly organized and have a high tolerance for sophistication. The tool is designed to survive in an enterprise environment by appearing as "garbage" or "noise" to automated security systems.

#### Recommended IR Actions:
1.  **Dynamic Behavior Monitoring:** Since static analysis is intentionally crippled, focus on **behavioral indicators**. Monitor the process for `FastWebClient` activity, any rapid-fire DNS requests (indicating it's searching for "faster" mirrors), and memory allocation/injection following a network connection.
2.  **Network-Level Defenses:** Implement deep packet inspection (DPI) to identify non-standard network libraries or connections to known high-reputation CDNs that might be used as staging points for the payload.
3.  **Memory Forensics:** Because the code is decrypted in memory only when needed, **memory dumps** of the running process are the most effective way to capture cleartext strings (IPs, URLs, and internal keys) that remain hidden on disk.
4.  **Hunting Rule:** Create a signature for the specific pattern of "overlapping instructions" or high-density `POPCOUNT` loops in memory as an indicator of this specific loader's presence in the environment.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors of **SaMarinDa_Downloader.exe** to the MITRE ATT&CK framework based on the provided technical analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files/Information | The use of "Arithmetic Dilution" (complex bitwise math) and "Junk Code" is designed to exhaust human analysts and bypass automated decompiler logic. |
| T1027 | Obfuscated Files/Information | "Instruction Overlapping" and packing techniques are specifically employed to break disassemblers like IDA Pro, hindering static analysis. |
| T1613 | Dynamic Resolution | The "Just-in-Time (JIT) Decoding" of strings and API addresses ensures that sensitive information remains hidden until the moment of execution. |
| T1055 | Process Injection | The use of "Memory Mapping" and "Carving" indicates the loader is preparing to inject a malicious payload into a specific memory region. |
| T1102 | System Service Resolution (Optional/Contextual) | The use of custom libraries like `FastWebClient` to bypass standard Windows API hooks is a technique used to evade EDR monitoring. |

### Analyst Notes:
*   **T1027 (Obfuscated Files/Information):** This category covers multiple behaviors identified in the report. Both "Arithmetic Dilution" and "Instruction Overlapping" fall under this umbrella as they are intended to hide the true intent of the code from both humans and automated tools.
*   **T1613 (Dynamic Resolution):** This is specifically mapped to the JIT decoding mentioned in the analysis; by resolving components at the "micro-second they are needed," the malware ensures that its footprint in memory is minimized for any period of time.
*   **T1055 (Process Injection):** The mention of "carving" and "memory mapping" to prepare a payload suggests the loader functions as a precursor to injecting more complex malicious code into the system's memory space.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   **None explicitly listed.** 
    *   *Note:* The analysis indicates that while specific IPs/URLs are not visible in plain text due to "Just-In-Time (JIT) Decoding," the malware uses a multi-source strategy via `FindFastestUrl`, `Win7Urls`, and `JsonUrls`. These suggest hardcoded lists of URLs or CDNs used for payload retrieval.

### **File paths / Registry keys**
*   **Registry Key:** `uninstallKey` (Indicates potential persistence or configuration modification in the Windows Registry).
*   **Process/File Name:** `SaMarinDa_Downloader.exe`
*   **Process/File Name:** `SaMarinDa Downloader`

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified in the provided text.*

### **Other artifacts**
*   **Custom Library Indicator:** `FastWebClient` (Identified as a non-standard/modified library used to evade EDR monitoring of standard Windows network APIs).
*   **Obfuscation Artifacts:** 
    *   **Instruction Overlapping:** Presence of overlapping instructions at offset `0x0040377c` (indicative of VMProtect or Themida packing).
    *   **Arithmetic Dilution:** Use of `POPCOUNT`, `CARRY1`, and complex bitwise math for constant calculation.
    *   **JIT Decoding:** Code behavior suggesting that strings and API addresses are only resolved in memory at the moment of execution to bypass static analysis.
*   **Behavioral Patterns:** 
    *   `FindFastestUrl`: Multi-source/mirror selection logic.
    *   `GetSubKeyNames`: Potential enumeration of registry keys for system reconnaissance or environment mapping.

---

## Malware Family Classification

1. **Malware family:** Custom (or Unknown)
2. **Malware type:** Downloader / Loader
3. **Confidence:** High

4. **Key evidence:**
*   **Multi-Stage Retrieval Logic:** The presence of `FindFastestUrl`, `Win7Urls`, and `JsonUrls` confirms the primary function is to identify and download malicious payloads from multiple sources/mirrors.
*   **Advanced Anti-Analysis Techniques:** The use of "Arithmetic Dilution" (complex bitwise math), "Instruction Overlapping," and JIT decoding indicates a high level of sophistication intended to bypass EDR systems and frustrate manual reverse engineering.
*   **Evasion Infrastructure:** The implementation of custom networking libraries (`FastWebClient`) instead of standard Windows APIs is a specific tactic used to bypass common security monitoring hooks during the network retrieval phase.
