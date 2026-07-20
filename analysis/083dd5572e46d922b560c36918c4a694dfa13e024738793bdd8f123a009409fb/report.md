# Threat Analysis Report

**Generated:** 2026-07-18 03:18 UTC
**Sample:** `083dd5572e46d922b560c36918c4a694dfa13e024738793bdd8f123a009409fb_083dd5572e46d922b560c36918c4a694dfa13e024738793bdd8f123a009409fb.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `083dd5572e46d922b560c36918c4a694dfa13e024738793bdd8f123a009409fb_083dd5572e46d922b560c36918c4a694dfa13e024738793bdd8f123a009409fb.exe` |
| File type | PE32+ executable for MS Windows 4.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 119,808 bytes |
| MD5 | `61e9c84eca68dfc2e6b66bb5bcd25a1c` |
| SHA1 | `46ce3b738485e5829623a643b5323f93cdb3a383` |
| SHA256 | `083dd5572e46d922b560c36918c4a694dfa13e024738793bdd8f123a009409fb` |
| Overall entropy | 6.121 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1777573826 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 91,648 | 5.988 | No |
| `.rsrc` | 27,648 | 5.737 | No |

## Extracted Strings

Total strings found: **1062** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
Qkkbal
v4.0.30319
#Strings
myprogram.exe
myprogram
<Module>
EmbeddedAttribute
Microsoft.CodeAnalysis
mscorlib
Attribute
System
NullableAttribute
System.Runtime.CompilerServices
NullableContextAttribute
STARTUP_64
ValueType
PROCESS_64
STARTUP_32
PROCESS_32
CreateProc64
MulticastDelegate
VirtualAlloc64
WriteMem64
VirtualProtect64
UnmapView64
GetCtx64
SetCtx64
ResumeThread64
CloseHandle64
CreateProc32
VirtualAlloc32
WriteMem32
ReadMem32
UnmapView32
GetCtx32
GetCtxWow32
SetCtx32
SetCtxWow32
ResumeThread32
MemoryMapper
SystemUtilities
Object
System.Windows.Forms
Homees
Resources
myprogram.Properties
Settings
ApplicationSettingsBase
System.Configuration
AssemblyResolver
SmartAssembly.AssemblyResolver
AssemblyInfo
AssemblyResolverHelper
ObfuscateControlFlowAttribute
SmartAssembly.Attributes
DoNotObfuscateAttribute
DoNotPruneAttribute
DoNotObfuscateTypeAttribute
DoNotPruneTypeAttribute
DoNotMoveAttribute
GetString
SmartAssembly.Delegates
MemberRefsProxy
SmartAssembly.HouseOfCards
Strings
ResourceResolver
SmartAssembly.ResourceResolver
SmartAssembly.StringsEncoding
DoNotEncodeStringsAttribute
SmartAssembly.Zip
Inflater
StreamManipulator
OutputWindow
InflaterHuffmanTree
InflaterDynHeader
Deflater
DeflaterHuffman
DeflaterEngine
DeflaterPending
ZipStream
MemoryStream
System.IO
SimpleZip
__StaticArrayInitTypeSize=16
__StaticArrayInitTypeSize=1024
__StaticArrayInitTypeSize=116
__StaticArrayInitTypeSize=120
__StaticArrayInitTypeSize=12
__StaticArrayInitTypeSize=76
<PrivateImplementationDetails>{EEE1D952-7F5E-4141-84B5-3EF03AF3374F}
Encryption
SmartAssembly.SmartExceptionsCore
AfterLoginClosure
AfterUploadClosure
NotificationEmailSettings
ReportSender
SendingReportFeedbackEventHandler
SendingReportFeedbackEventArgs
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method...cctor` | `0x40a164` | 65524 | ✓ |
| `method.myprogram.Homees.runss` | `0x4031d4` | 1772 | ✓ |
| `method.SystemUtilities.MemoryMapper.Map64` | `0x4020f0` | 1316 | ✓ |
| `method.SystemUtilities.MemoryMapper.Map32` | `0x402614` | 1312 | ✓ |
| `method.SmartAssembly.Zip.SimpleZip.Zip` | `0x404c50` | 1244 | ✓ |
| `method.myprogram.Form1.InitializeComponent` | `0x402d10` | 1064 | ✓ |
| `method.SmartAssembly.SmartUsageCore.UsageReportSender.GenerateReportData` | `0x4097a4` | 948 | ✓ |
| `method.SmartAssembly.SmartExceptionsCore.Encryption.Encrypt` | `0x407d80` | 752 | ✓ |
| `method.SmartAssembly.AssemblyResolver.AssemblyResolverHelper.ResolveAssembly` | `0x403c40` | 720 | ✓ |
| `method.SmartAssembly.Zip.SimpleZip.Unzip` | `0x40498c` | 672 | ✓ |
| `method.DeflaterEngine.DeflateSlow` | `0x4077e0` | 616 | ✓ |
| `method.InflaterDynHeader.Decode` | `0x405f28` | 612 | ✓ |
| `method.DeflaterEngine.FindLongestMatch` | `0x40757c` | 612 | ✓ |
| `method.SmartAssembly.HouseOfCards.MemberRefsProxy.CreateMemberRefsDelegates` | `0x404110` | 604 | ✓ |
| `method.Tree.BuildTree` | `0x406e38` | 600 | ✓ |
| `method.Tree.BuildLength` | `0x406c34` | 516 | ✓ |
| `method.InflaterHuffmanTree.BuildTree` | `0x405c54` | 500 | ✓ |
| `method.Inflater.Decode` | `0x405324` | 468 | ✓ |
| `method.SmartAssembly.SmartUsageCore.PlatformUsageCounter.CountPlatformUsages` | `0x408764` | 464 | ✓ |
| `method.DeflaterHuffman.FlushBlock` | `0x406814` | 456 | ✓ |
| `method.Inflater.DecodeHuffman` | `0x405164` | 448 | ✓ |
| `method.SmartAssembly.SmartUsageCore.UsageCountStore.UnprotectedGetAllUsageCounts` | `0x409190` | 408 | ✓ |
| `method.DeflaterHuffman..cctor` | `0x4063fc` | 320 | ✓ |
| `method.SmartAssembly.HouseOfCards.Strings.CreateGetStringDelegate` | `0x4043b4` | 316 | ✓ |
| `method.SmartAssembly.StringsEncoding.Strings.Get` | `0x40466c` | 308 | ✓ |
| `method.SmartAssembly.SmartUsageCore.UsageCountStore.GetDynamicFeatureUsageFilename` | `0x408ed0` | 300 | ✓ |
| `method.Tree.CalcBLFreq` | `0x4070c8` | 276 | ✓ |
| `method.AssemblyInfo..ctor` | `0x403fd0` | 264 | ✓ |
| `method.AfterLoginClosure.AfterLogin` | `0x408218` | 264 | ✓ |
| `method.Tree.WriteTree` | `0x4071dc` | 252 | ✓ |

### Decompiled Code Files

- [`code/method...cctor.c`](code/method...cctor.c)
- [`code/method.AfterLoginClosure.AfterLogin.c`](code/method.AfterLoginClosure.AfterLogin.c)
- [`code/method.AssemblyInfo..ctor.c`](code/method.AssemblyInfo..ctor.c)
- [`code/method.DeflaterEngine.DeflateSlow.c`](code/method.DeflaterEngine.DeflateSlow.c)
- [`code/method.DeflaterEngine.FindLongestMatch.c`](code/method.DeflaterEngine.FindLongestMatch.c)
- [`code/method.DeflaterHuffman..cctor.c`](code/method.DeflaterHuffman..cctor.c)
- [`code/method.DeflaterHuffman.FlushBlock.c`](code/method.DeflaterHuffman.FlushBlock.c)
- [`code/method.Inflater.Decode.c`](code/method.Inflater.Decode.c)
- [`code/method.Inflater.DecodeHuffman.c`](code/method.Inflater.DecodeHuffman.c)
- [`code/method.InflaterDynHeader.Decode.c`](code/method.InflaterDynHeader.Decode.c)
- [`code/method.InflaterHuffmanTree.BuildTree.c`](code/method.InflaterHuffmanTree.BuildTree.c)
- [`code/method.SmartAssembly.AssemblyResolver.AssemblyResolverHelper.ResolveAssembly.c`](code/method.SmartAssembly.AssemblyResolver.AssemblyResolverHelper.ResolveAssembly.c)
- [`code/method.SmartAssembly.HouseOfCards.MemberRefsProxy.CreateMemberRefsDelegates.c`](code/method.SmartAssembly.HouseOfCards.MemberRefsProxy.CreateMemberRefsDelegates.c)
- [`code/method.SmartAssembly.HouseOfCards.Strings.CreateGetStringDelegate.c`](code/method.SmartAssembly.HouseOfCards.Strings.CreateGetStringDelegate.c)
- [`code/method.SmartAssembly.SmartExceptionsCore.Encryption.Encrypt.c`](code/method.SmartAssembly.SmartExceptionsCore.Encryption.Encrypt.c)
- [`code/method.SmartAssembly.SmartUsageCore.PlatformUsageCounter.CountPlatformUsages.c`](code/method.SmartAssembly.SmartUsageCore.PlatformUsageCounter.CountPlatformUsages.c)
- [`code/method.SmartAssembly.SmartUsageCore.UsageCountStore.GetDynamicFeatureUsageFilename.c`](code/method.SmartAssembly.SmartUsageCore.UsageCountStore.GetDynamicFeatureUsageFilename.c)
- [`code/method.SmartAssembly.SmartUsageCore.UsageCountStore.UnprotectedGetAllUsageCounts.c`](code/method.SmartAssembly.SmartUsageCore.UsageCountStore.UnprotectedGetAllUsageCounts.c)
- [`code/method.SmartAssembly.SmartUsageCore.UsageReportSender.GenerateReportData.c`](code/method.SmartAssembly.SmartUsageCore.UsageReportSender.GenerateReportData.c)
- [`code/method.SmartAssembly.StringsEncoding.Strings.Get.c`](code/method.SmartAssembly.StringsEncoding.Strings.Get.c)
- [`code/method.SmartAssembly.Zip.SimpleZip.Unzip.c`](code/method.SmartAssembly.Zip.SimpleZip.Unzip.c)
- [`code/method.SmartAssembly.Zip.SimpleZip.Zip.c`](code/method.SmartAssembly.Zip.SimpleZip.Zip.c)
- [`code/method.SystemUtilities.MemoryMapper.Map32.c`](code/method.SystemUtilities.MemoryMapper.Map32.c)
- [`code/method.SystemUtilities.MemoryMapper.Map64.c`](code/method.SystemUtilities.MemoryMapper.Map64.c)
- [`code/method.Tree.BuildLength.c`](code/method.Tree.BuildLength.c)
- [`code/method.Tree.BuildTree.c`](code/method.Tree.BuildTree.c)
- [`code/method.Tree.CalcBLFreq.c`](code/method.Tree.CalcBLFreq.c)
- [`code/method.Tree.WriteTree.c`](code/method.Tree.WriteTree.c)
- [`code/method.myprogram.Form1.InitializeComponent.c`](code/method.myprogram.Form1.InitializeComponent.c)
- [`code/method.myprogram.Homees.runss.c`](code/method.myprogram.Homees.runss.c)

## Behavioral Analysis

Based on the provided strings and disassembled code, this binary is highly characteristic of a **malware loader/dropper** designed to inject a secondary payload into memory while using various obfuscation and evasion techniques.

### Core Functionality and Purpose
The primary purpose of this program appears to be an "initial stage" loader. It is designed to:
1.  Decompress and decrypt an embedded malicious payload (likely a .NET assembly or a native PE file).
2.  Manually map that payload into memory.
3.  Execute the hidden functionality in a separate process or within its own space to evade detection.

### Suspicious/Malicious Behaviors
*   **Process Injection & Manual Mapping:** 
    *   The presence of `MemoryMapper` (containing `Map64` and `Map32` methods) is a strong indicator of **manual mapping**. Instead of letting the OS loader handle an executable, the malware manually maps sections into memory.
    *   The inclusion of `VirtualAlloc`, `WriteMem`, `VirtualProtect`, and `CreateProc` (for both 32-bit and 64-bit architectures) suggests it is preparing to inject code into a target process or allocate space for a hidden payload.
*   **Evasive Decompression & Encryption:**
    *   The "Strings" section contains several terms related to the **Zlib/Deflate** algorithm (e.g., `DECODE_BLOCKS`, `Inflater`, `Deflater`, `HuffmanTree`). This indicates the actual malicious payload is compressed inside this binary to evade signature-based detection.
    *   The presence of an `Encryption` class suggests that, in addition to being packed/compressed, the payload may be encrypted and only decrypted in memory at runtime.
*   **Command & Control (C2) / Exfiltration:**
    *   Several very suspicious strings point toward back-end communication: `AfterLoginClosure`, `UploadReportLoginService`, `SendingReportFeedbackEventHandler`, and `ReportSender`.
    *   These indicate that the final payload likely performs **credential harvesting** or data exfiltration, reporting the results back to an attacker's server.
*   **Multi-Architecture Support:** 
    *   The code specifically handles both `x64` and `x86` (32-bit) logic (`Map64`, `Map32`, `CreateProc64`, etc.). This is a common tactic to ensure the malware remains functional regardless of whether the target system is running a 32-bit or 64-bit OS.

### Notable Techniques and Patterns
*   **Obfuscation:** The decompiler output shows significant "noise" (e.g., `unaff_` variables, `CONCAT` macros, and "bad instruction" warnings). This is typical of **code obfuscation**, where the author intentionally complicates the control flow to hinder reverse engineering.
*   **Resource Utilization:** The presence of `System.Windows.Forms` and `Form1.InitializeComponent` suggests that the malware might have a GUI (perhaps a fake "Update" window or a decoy application) to mask its activity from the user while it performs its background tasks.
*   **Dynamic Assembly Loading:** The use of `AssemblyResolver` and `HouseOfCards` suggests advanced .NET techniques for resolving dependencies dynamically, which is often used to hide the true scope of what modules are being loaded during execution.

### Summary Conclusion
This binary is a **sophisticated multi-stage loader**. It uses common malware techniques such as **manual mapping**, **compressed/encrypted payloads**, and **obfuscated control flow** to host a malicious payload that likely performs credential theft or other malicious actions via a remote C2 server.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055.016** | Process Injection: Reflective Loader | The use of `MemoryMapper` (with `Map32`/`Map64`) and functions like `VirtualAlloc` to manually map a payload into memory is a signature of reflective loading to bypass the OS loader. |
| **T1027** | Obfuscated Files or Information | The inclusion of Zlib/Deflate components, an encryption class, and "noise" in the control flow are used to hide the malicious payload and logic from static analysis. |
| **T1041** | Exfiltration | The presence of strings such as `UploadReportLoginService` and `SendingReportFeedback` indicates that the malware is designed to transmit stolen data (like credentials) to a remote server. |
| **T1568** | Dynamic Resolution | The use of `AssemblyResolver` suggests the dynamic resolution of components at runtime to hide the true scope of functionality from security scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `myprogram.exe` (Potential internal filename/executable name)

**Mutex names / Named pipes**
*   None identified. (Note: While `DisposableMutex` appears in the strings, it is a generic class name rather than a specific unique mutex string).

**Hashes**
*   None identified.

**Other artifacts**
*   **C2/Exfiltration Indicators:** The following strings indicate functionality related to remote reporting and credential harvesting: 
    *   `AfterLoginClosure`
    *   `UploadReportLoginService`
    *   `SendingReportFeedbackEventHandler`
    *   `ReportSender`
    *   `ReportingService`
*   **Manual Mapping/Injection Indicators:** The presence of `MemoryMapper`, `Map64`, `Map32`, `VirtualAlloc`, `WriteMem`, and `VirtualProtect` indicates a manual mapping technique to inject payloads.
*   **Decompression Logic (Zlib/Deflate):** 
    *   `Inflater`
    *   `Deflater`
    *   `HuffmanTree`
    *   `DECODE_BLOCKS`, `DECODE_HUFFMAN`, `DECODE_CHKSUM` (indicates a hidden, compressed payload).
*   **Dynamic Loading/Evasion:** 
    *   `SmartAssembly.HouseOfCards` (Used for advanced .NET assembly resolution)
    *   `ObfuscateControlFlowAttribute`

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Manual Mapping & Injection:** The presence of `MemoryMapper` (with `Map32`/`Map64`), `VirtualAlloc`, and `WriteMem` indicates a classic "reflective loader" behavior designed to inject a payload into memory while bypassing standard OS loading procedures.
*   **Obfuscation/Decompression Logic:** The inclusion of Zlib/Deflate libraries (`Inflater`, `Deflater`) and an encryption class suggests the sample is a wrapper for a hidden, compressed primary payload, common in multi-stage malware.
*   **Exfiltration Indicators:** String constants such as `UploadReportLoginService` and `ReportSender` confirm that the final stage of the execution chain involves collecting data (likely credentials) and transmitting it to a remote server.
