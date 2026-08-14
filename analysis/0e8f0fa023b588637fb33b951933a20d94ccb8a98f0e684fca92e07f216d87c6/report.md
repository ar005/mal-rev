# Threat Analysis Report

**Generated:** 2026-08-12 20:24 UTC
**Sample:** `0e8f0fa023b588637fb33b951933a20d94ccb8a98f0e684fca92e07f216d87c6_0e8f0fa023b588637fb33b951933a20d94ccb8a98f0e684fca92e07f216d87c6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e8f0fa023b588637fb33b951933a20d94ccb8a98f0e684fca92e07f216d87c6_0e8f0fa023b588637fb33b951933a20d94ccb8a98f0e684fca92e07f216d87c6.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 14,336 bytes |
| MD5 | `b1a031ea42ce7c7d3afc496f862cd155` |
| SHA1 | `92bd064212033d96c4453857e5dc78d5974850c6` |
| SHA256 | `0e8f0fa023b588637fb33b951933a20d94ccb8a98f0e684fca92e07f216d87c6` |
| Overall entropy | 5.461 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2425790517 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 11,264 | 5.816 | No |
| `.rsrc` | 2,048 | 4.276 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **183** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
__StaticArrayInitTypeSize=10
63279522FEBCF5538B72996C16A8660FF177CD5536E86FB9C2A577BF32A65430
__StaticArrayInitTypeSize=60
<>c__DisplayClass24_0
CE8DABF843E3E5CC62AD186CF6D52365052622309C78C4E00FD9C5C706D9CA61
IEnumerable`1
List`1
__StaticArrayInitTypeSize=32
D686451E3D030110D8729E559FD15D8FAF7F51E4F162B55E53EA6DCDBF3CF2F2
Func`2
__StaticArrayInitTypeSize=13
__StaticArrayInitTypeSize=33
__StaticArrayInitTypeSize=14
BF6AD492C1A76E8BD936D8954F1F2654F69E708D3BADF8E32F1438E7E4674755
__StaticArrayInitTypeSize=5
__StaticArrayInitTypeSize=36
__StaticArrayInitTypeSize=7
__StaticArrayInitTypeSize=38
DC9EC376254415374B6819A2BD9A1437B337809EF0535D6D068A547E5B304788
E42F3EA0E570C80C26413369327AFA51EC71BF3AC2729AD61E87370BAF3714E8
get_UTF8
F31229C050C1CAE1936F0C1CB767AC915AA0F3ED1CFF2111C08B9BCBDB255009
<Module>
<PrivateImplementationDetails>
7371F071A9A4E653A5AFD134BCE9C735EF74B0421D6988958E5C6D8A34FEAA3B
0B83573B66D3FFE50F83E2DA5C72AFB7370A29E08C8DAF14368E5F54BB0B67CB
B54A61E1DDA9F15D433B32A498BE6D26E10488A213CF1123C8BF82E605A9AF6E
B8BCD45AC095259959025C186A28D04182CABEF776212B1170EFA9452DD1BC7E
A840405EC063A57CFAD884363A05ACABB35AF9DE0F5F2BE0589502338F084F7E
C33C0DF50DC77BDDF6D36930013CBE28C5093CF54F582F6BCD2C5D455CA8863F
F307E73A3447B10444E67233700C1AA5CA8E3673DD2F292084BF485583CAAD6F
System.IO
mscorlib
System.Collections.Generic
get_Id
Thread
get_HasExited
System.Collections.Specialized
GetField
get_Millisecond
GetMethod
GetHashCode
GCCollectionMode
get_Unicode
Invoke
Enumerable
IDisposable
RuntimeFieldHandle
RuntimeTypeHandle
GetTypeFromHandle
processHandle
DownloadFile
ProcessWindowStyle
GetDirectoryName
DateTime
Combine
ValueType
SecurityProtocolType
System.Core
MethodBase
Dispose
EmbeddedAttribute
CompilerGeneratedAttribute
AttributeUsageAttribute
DebuggableAttribute
TargetFrameworkAttribute
RefSafetyRulesAttribute
CompilationRelaxationsAttribute
RuntimeCompatibilityAttribute
SetValue
Megoossggooj.exe
dwSize
System.Threading
Encoding
System.Runtime.Versioning
ToBase64String
ToString
GetString
GetFolderPath
get_Length
processInformationLength
returnLength
Megoossggooj
kernel32.dll
ntdll.dll
set_SecurityProtocol
get_Item
System
Random
Boolean
GetExtension
GetFileNameWithoutExtension
Version
processInformation
System.Reflection
```

## Disassembly Overview

Functions analyzed: **19** | Decompiled to C: **19**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass24_0.__b__0` | `0x402c32` | 29646 | ✓ |
| `sym...__3` | `0x4021c4` | 756 | ✓ |
| `sym...__7` | `0x4026c8` | 428 | ✓ |
| `sym...__5` | `0x402508` | 380 | ✓ |
| `method....cctor` | `0x402ac0` | 362 | ✓ |
| `sym...__8` | `0x402874` | 324 | ✓ |
| `sym...__9` | `0x4029b8` | 176 | ✓ |
| `sym...__1` | `0x4020ec` | 126 | ✓ |
| `sym...` | `0x402098` | 84 | ✓ |
| `sym...__4` | `0x4024b8` | 80 | ✓ |
| `method...` | `0x402a68` | 80 | ✓ |
| `sym...__2` | `0x402178` | 76 | ✓ |
| `sym...__6` | `0x402684` | 68 | ✓ |
| `method...GetAllUrls` | `0x402067` | 49 | ✓ |
| `method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor` | `0x402058` | 15 | ✓ |
| `entry0` | `0x40216a` | 14 | ✓ |
| `method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor` | `0x402050` | 8 | ✓ |
| `method....ctor` | `0x402ab8` | 8 | ✓ |
| `method.__c__DisplayClass24_0..ctor` | `0x402c2a` | 8 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method....c`](code/method....c)
- [`code/method....cctor.c`](code/method....cctor.c)
- [`code/method....ctor.c`](code/method....ctor.c)
- [`code/method...GetAllUrls.c`](code/method...GetAllUrls.c)
- [`code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c`](code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c)
- [`code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c`](code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c)
- [`code/method.__c__DisplayClass24_0..ctor.c`](code/method.__c__DisplayClass24_0..ctor.c)
- [`code/method.__c__DisplayClass24_0.__b__0.c`](code/method.__c__DisplayClass24_0.__b__0.c)
- [`code/sym....c`](code/sym....c)
- [`code/sym...__1.c`](code/sym...__1.c)
- [`code/sym...__2.c`](code/sym...__2.c)
- [`code/sym...__3.c`](code/sym...__3.c)
- [`code/sym...__4.c`](code/sym...__4.c)
- [`code/sym...__5.c`](code/sym...__5.c)
- [`code/sym...__6.c`](code/sym...__6.c)
- [`code/sym...__7.c`](code/sym...__7.c)
- [`code/sym...__8.c`](code/sym...__8.c)
- [`code/sym...__9.c`](code/sym...__9.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis. The latest data confirms high-level sophistication in the sample's construction, specifically regarding **anti-analysis techniques** and **packer behavior**.

### Updated Analysis: Comprehensive Report

#### Summary of Findings
The binary is a highly sophisticated **multi-stage loader/downloader**. While the first chunk established its intent (C2 communication, PowerShell abuse, and evasion), the second chunk reveals the "armor" it wears to protect itself from researchers. It utilizes advanced obfuscation techniques typical of commercial packers or professional-grade malware protectors.

---

### Expanded Core Functionality & Tactics

**1. Advanced Obfuscation & Anti-Analysis (New Findings)**
*   **Junk Code/Opaque Predicates:** The functions `sym...`, `sym...__4`, and `sym...__6` contain massive blocks of mathematical operations, bitwise shifts (`>> 8`), and complex logic flows that appear to perform no meaningful task. This is a classic **"junk code"** technique designed to:
    *   Exhaust the analyst's time during manual review.
    *   Confuse automated decompiler engines (as seen by the "bad instruction" warnings).
    *   Hide the actual logic of the program behind "mathematical noise."
*   **Instruction Overlapping:** The disassembly reports multiple instances where instructions overlap (`overlapping instruction at (ram,0x0040216d)`). This is a deliberate technique to thwart linear disassemblers. By overlapping bytes, the malware ensures that only a specific jump or offset leads to the "real" code path, while anything else results in junk data being executed.
*   **Control Flow Flattening:** The complexity of these routines suggests the use of **control-flow flattening**, where all logical paths are flattened into a single large switch/loop structure, making it nearly impossible to follow the logic without high-level symbolic execution.

**2. Memory Manipulation & Packing (Expanded)**
*   **VirtualProtect Utilization:** The disassembly confirms the presence of `VirtualProtect`. In this context, it is almost certainly used to change memory segments from **Read/Write (RW)** to **Execute/Read (RX)** or **Read/Write/Execute (RWX)**. This is a prerequisite for:
    *   Decrypting and "mapping" shellcode into memory.
    *   Executing the secondary payloads (`randll32`, `RSASAR`) that were identified in the string analysis.

**3. Persistence of Malicious Behaviors (From Previous Analysis)**
*   **Command & Control (C2):** The core purpose remains the retrieval of malicious modules from `.cfd` domains.
*   **Defense Evasion:** The use of `Add-MpPreference` and hidden PowerShell windows continues to be a primary method for ensuring the "first stage" remains active on the system without alerting the user or local security software.

---

### Updated Indicators & Risk Assessment

| Category | Observation | Severity | Analysis Note |
| :--- | :--- | :--- | :--- |
| **Network** | Hardcoded C2 links (.cfd) | High | Used for multi-stage payload retrieval. |
| **Evasion** | `Add-MpPreference` & Hidden PWSH | High | Direct attempt to disable local Windows Defender alerts. |
| **Obfuscation** | Instruction Overlapping/Junk Code | High | High complexity indicates a professional packer or custom protection layer. |
| **Memory** | `VirtualProtect` calls | High | Classic indicator of shellcode injection or unpacking "stage 2." |
| **Tooling** | .NET Framework usage | Medium | Indicates the core logic is likely wrapped in a .NET environment to simplify networking/execution. |

---

### Conclusion and Recommendation
The analysis confirms that this is not a simple script, but a **sophisticatedly engineered loader**. The presence of instruction overlapping and extensive mathematical junk code indicates that the developers intended to thwart automated sandboxes and professional reverse engineers.

**Recommended Response Actions:**
1.  **Network Blocking:** Block all traffic associated with the `.cfd` domains identified in the initial string analysis.
2.  **Endpoint Monitoring:** Monitor for `powershell.exe -EncodedCommand` or any process attempting to call `VirtualProtect` on its own memory space, as these are "high-confidence" indicators of malicious loader behavior.
3.  **Indicator Update:** Feed the specific hash of this binary into EDR systems; however, be aware that due to the heavy obfuscation/packing, similar variants may have different hashes despite having identical functionality.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of "junk code," opaque predicates, and instruction overlapping is specifically designed to complicate manual analysis and evade detection by automated disassembly tools. |
| T1055 | Process Injection | The utilization of `VirtualProtect` to change memory permissions (e.g., from RW to RX/RWX) indicates the preparation for mapping and executing shellcode or secondary payloads. |
| T1105 | Ingress Tool Transfer | The loader's core functionality is to retrieve and stage additional malicious modules (like `randll32` and `RSASAR`) from hardcoded `.cfd` domains. |
| T1562.001 | Disable or Remove Security Software | The use of the `Add-MpPreference` command is a direct attempt to disable local Windows Defender security settings to ensure the malware's persistence. |
| T1059.001 | Command and Scripting Interpreter: PowerShell | The execution of scripts via PowerShell, particularly with hidden windows, allows for fileless execution and masks malicious activity from the end-user. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have extracted the following Indicators of Compromise (IOCs) from the provided strings and behavioral analysis.

### **IP addresses / URLs / Domains**
*   **Domain:** `goooooogk.cfd`
*   **URL:** `https://goooooogk.cfd/noo/randll32.exe`
*   **URL:** `https://goooooogk.cfd/noo/RSASAR.exe`

### **File paths / Registry keys**
*   **Malicious Executables:**
    *   `Megoossggooj.exe` (Primary loader)
    *   `randll32.exe` (Note: This is a masqueraded filename likely mimicking `rundll32.exe`)
    *   `RSASAR.exe`

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No clear file hashes (MD5/SHA1/SHA256) were identified in the provided text. The long hex strings present appear to be internal obfuscation keys or junk code rather than standard file signatures.*

### **Other artifacts**
*   **User-Agent String:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36` (Used by the loader to blend in with legitimate browser traffic during C2 communication).
*   **Command Line Arguments:** `-EncodedCommand` (Flag used for executing Base64 encoded PowerShell scripts).
*   **Evasion Commands:** `Add-MpPreference -ExclusionPath` (Specific command used to disable Windows Defender protections for the malware's directory).
*   **Behavioral Indicators:** 
    *   Usage of `VirtualProtect` to transition memory pages to executable states.
    *   Use of "Instruction Overlapping" and "Control Flow Flattening" to hinder static analysis.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://schemas.microsoft.com/SMI/2016/WindowsSettings`
- `https://goooooogk.cfd/noo/RSASAR.exe`
- `https://goooooogk.cfd/noo/randll32.exe`

---

## Malware Family Classification

1. **Malware family**: custom (Sophisticated Loader)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Downloader Behavior:** The sample is designed to fetch and execute secondary payloads (`randll32`, `RSASAR`) from hardcoded `.cfd` domains, a hallmark of high-end loader operations.
*   **Advanced Anti-Analysis Techniques:** The presence of instruction overlapping, control flow flattening, and "junk code" indicates the use of professional-grade packers or custom protection layers specifically designed to thwart automated sandboxes and manual reverse engineering.
*   **Aggressive Defense Evasion:** The sample actively attempts to disable Windows Defender via `Add-MpPreference` and utilizes hidden PowerShell windows to mask its execution and ensure persistence while preparing memory for shellcode injection (via `VirtualProtect`).
