# Threat Analysis Report

**Generated:** 2026-07-11 20:02 UTC
**Sample:** `049388e86f349f34e39d4e7d908b9447e3705dcc8d983aaa5e3c886e4151f448_049388e86f349f34e39d4e7d908b9447e3705dcc8d983aaa5e3c886e4151f448.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `049388e86f349f34e39d4e7d908b9447e3705dcc8d983aaa5e3c886e4151f448_049388e86f349f34e39d4e7d908b9447e3705dcc8d983aaa5e3c886e4151f448.exe` |
| File type | PE32+ executable for MS Windows 4.00 (DLL), x86-64 Mono/.Net assembly, 4 sections |
| Size | 17,228,800 bytes |
| MD5 | `47b8a17940f4615f8673d47a10a79a3e` |
| SHA1 | `c9a600fb869f949250b68dc9f73ef44ffb4257b3` |
| SHA256 | `049388e86f349f34e39d4e7d908b9447e3705dcc8d983aaa5e3c886e4151f448` |
| Overall entropy | 6.857 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769164492 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 17,225,728 | 6.858 | No |
| `.sdata` | 512 | 0.832 | No |
| `.rsrc` | 1,024 | 2.953 | No |
| `.reloc` | 512 | 0.159 | No |

### Imports

**mscoree.dll**: `_CorDllMain`

### Exports

`ApiNet`

## Extracted Strings

Total strings found: **117903** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.sdata
@.reloc
C:\Users\
\AppData\Local\Temp\DllExporter\MpAsDesc.pdb
v4.0.30319
#Strings
<Module>
System.Runtime.CompilerServices
CompilationRelaxationsAttribute
RuntimeCompatibilityAttribute
System.Reflection
AssemblyTitleAttribute
AssemblyDescriptionAttribute
AssemblyConfigurationAttribute
AssemblyCompanyAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
AssemblyTrademarkAttribute
System.Runtime.InteropServices
ComVisibleAttribute
GuidAttribute
AssemblyFileVersionAttribute
System.Runtime.Versioning
TargetFrameworkAttribute
System
Object
System.CodeDom.Compiler
GeneratedCodeAttribute
System.Diagnostics
DebuggerNonUserCodeAttribute
CompilerGeneratedAttribute
System.Resources
ResourceManager
System.Globalization
CultureInfo
RuntimeTypeHandle
GetTypeFromHandle
Assembly
get_Assembly
GetObject
System.ComponentModel
EditorBrowsableAttribute
EditorBrowsableState
Action
Random
System.Threading
Thread
Invoke
RuntimeHelpers
RuntimeFieldHandle
InitializeArray
Buffer
BlockCopy
System.IO
Exists
FileNotFoundException
ReadAllBytes
InvalidDataException
BitConverter
ToInt32
MethodInfo
op_Equality
get_EntryPoint
ParameterInfo
MethodBase
GetParameters
String
Concat
Monitor
BindingFlags
GetMethod
MpAsDesc.dll
mscorlib
Resources
MpAsDesc.Properties
IProcessor
XorExtract
IExecutor
IPathResolver
IDelayExecutor
DelayExecutor
DataProcessor
<PrivateImplementationDetails>
AssemblyExecutor
PathResolver
Orchestrator
Extractor
resourceMan
resourceCulture
get_ResourceManager
get_Culture
set_Culture
get_dag1
Process
offset
Execute
Resolve
action
_random
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MpAsDesc.Properties.Resources..ctor` | `0x180002064` | 663730 | ✓ |
| `method.MpAsDesc.Properties.Resources.set_Culture` | `0x18000209f` | 663672 | ✓ |
| `method.XorExtract.Extractor.ApiNet` | `0x180002534` | 129840 | ✓ |
| `method.XorExtract.Orchestrator..ctor` | `0x18000242b` | 64628 | ✓ |
| `method.XorExtract.DataProcessor..ctor` | `0x180002127` | 364 | ✓ |
| `method.XorExtract.DataProcessor.ValidateLength` | `0x180002293` | 272 | ✓ |
| `method.XorExtract.DelayExecutor.Execute` | `0x1800020c4` | 156 | ✓ |
| `sym.MpAsDesc.dll_ApiNet` | `0x18106f65a` | 116 | ✓ |
| `method.XorExtract.Extractor..cctor` | `0x1800024b8` | 112 | ✓ |
| `method.XorExtract.AssemblyExecutor.Execute` | `0x18000236c` | 110 | ✓ |
| `method.MpAsDesc.Properties.Resources.get_dag1` | `0x1800020a7` | 108 | ✓ |
| `method.XorExtract.DataProcessor.DecryptData` | `0x180002300` | 108 | ✓ |
| `method.XorExtract.AssemblyExecutor.InvokeEntry` | `0x1800023cf` | 92 | ✓ |
| `method.XorExtract.DataProcessor.Process` | `0x180002214` | 80 | ✓ |
| `method.XorExtract.DataProcessor.GetKey` | `0x1800021b4` | 78 | ✓ |
| `method.XorExtract.Orchestrator._Run_b__5_0` | `0x18000246c` | 76 | ✓ |
| `method.XorExtract.DataProcessor.VerifyMarker` | `0x1800022cc` | 52 | ✓ |
| `method.XorExtract.PathResolver..ctor` | `0x1800023e2` | 52 | ✓ |
| `method.XorExtract.PathResolver.BuildPath` | `0x18000241e` | 50 | ✓ |
| `method.MpAsDesc.Properties.Resources.get_ResourceManager` | `0x18000206c` | 44 | ✓ |
| `method.XorExtract.DataProcessor.GenerateKeyPart2` | `0x180002188` | 44 | ✓ |
| `method.XorExtract.DataProcessor.GenerateKeyPart1` | `0x180002160` | 40 | ✓ |
| `method.XorExtract.DataProcessor.ExtractLength` | `0x18000228a` | 34 | ✓ |
| `method.XorExtract.DataProcessor.ExtractCipher` | `0x1800022ac` | 32 | ✓ |
| `method.XorExtract.AssemblyExecutor.PrepareArguments` | `0x1800023b3` | 28 | ✓ |
| `method.XorExtract.Orchestrator.Run` | `0x180002450` | 28 | ✓ |
| `method.XorExtract.DataProcessor.ReadData` | `0x180002264` | 22 | ✓ |
| `method.XorExtract.DataProcessor.GetMarker` | `0x180002202` | 18 | ✓ |
| `method.XorExtract.DataProcessor.ValidateOffset` | `0x18000227a` | 16 | ✓ |
| `entry0` | `0x18106f6ce` | 12 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.MpAsDesc.Properties.Resources..ctor.c`](code/method.MpAsDesc.Properties.Resources..ctor.c)
- [`code/method.MpAsDesc.Properties.Resources.get_ResourceManager.c`](code/method.MpAsDesc.Properties.Resources.get_ResourceManager.c)
- [`code/method.MpAsDesc.Properties.Resources.get_dag1.c`](code/method.MpAsDesc.Properties.Resources.get_dag1.c)
- [`code/method.MpAsDesc.Properties.Resources.set_Culture.c`](code/method.MpAsDesc.Properties.Resources.set_Culture.c)
- [`code/method.XorExtract.AssemblyExecutor.Execute.c`](code/method.XorExtract.AssemblyExecutor.Execute.c)
- [`code/method.XorExtract.AssemblyExecutor.InvokeEntry.c`](code/method.XorExtract.AssemblyExecutor.InvokeEntry.c)
- [`code/method.XorExtract.AssemblyExecutor.PrepareArguments.c`](code/method.XorExtract.AssemblyExecutor.PrepareArguments.c)
- [`code/method.XorExtract.DataProcessor..ctor.c`](code/method.XorExtract.DataProcessor..ctor.c)
- [`code/method.XorExtract.DataProcessor.DecryptData.c`](code/method.XorExtract.DataProcessor.DecryptData.c)
- [`code/method.XorExtract.DataProcessor.ExtractCipher.c`](code/method.XorExtract.DataProcessor.ExtractCipher.c)
- [`code/method.XorExtract.DataProcessor.ExtractLength.c`](code/method.XorExtract.DataProcessor.ExtractLength.c)
- [`code/method.XorExtract.DataProcessor.GenerateKeyPart1.c`](code/method.XorExtract.DataProcessor.GenerateKeyPart1.c)
- [`code/method.XorExtract.DataProcessor.GenerateKeyPart2.c`](code/method.XorExtract.DataProcessor.GenerateKeyPart2.c)
- [`code/method.XorExtract.DataProcessor.GetKey.c`](code/method.XorExtract.DataProcessor.GetKey.c)
- [`code/method.XorExtract.DataProcessor.GetMarker.c`](code/method.XorExtract.DataProcessor.GetMarker.c)
- [`code/method.XorExtract.DataProcessor.Process.c`](code/method.XorExtract.DataProcessor.Process.c)
- [`code/method.XorExtract.DataProcessor.ReadData.c`](code/method.XorExtract.DataProcessor.ReadData.c)
- [`code/method.XorExtract.DataProcessor.ValidateLength.c`](code/method.XorExtract.DataProcessor.ValidateLength.c)
- [`code/method.XorExtract.DataProcessor.ValidateOffset.c`](code/method.XorExtract.DataProcessor.ValidateOffset.c)
- [`code/method.XorExtract.DataProcessor.VerifyMarker.c`](code/method.XorExtract.DataProcessor.VerifyMarker.c)
- [`code/method.XorExtract.DelayExecutor.Execute.c`](code/method.XorExtract.DelayExecutor.Execute.c)
- [`code/method.XorExtract.Extractor..cctor.c`](code/method.XorExtract.Extractor..cctor.c)
- [`code/method.XorExtract.Extractor.ApiNet.c`](code/method.XorExtract.Extractor.ApiNet.c)
- [`code/method.XorExtract.Orchestrator..ctor.c`](code/method.XorExtract.Orchestrator..ctor.c)
- [`code/method.XorExtract.Orchestrator.Run.c`](code/method.XorExtract.Orchestrator.Run.c)
- [`code/method.XorExtract.Orchestrator._Run_b__5_0.c`](code/method.XorExtract.Orchestrator._Run_b__5_0.c)
- [`code/method.XorExtract.PathResolver..ctor.c`](code/method.XorExtract.PathResolver..ctor.c)
- [`code/method.XorExtract.PathResolver.BuildPath.c`](code/method.XorExtract.PathResolver.BuildPath.c)
- [`code/sym.MpAsDesc.dll_ApiNet.c`](code/sym.MpAsDesc.dll_ApiNet.c)

## Behavioral Analysis

Based on the provided strings and decompiled code, here is an analysis of the binary:

### Core Functionality and Purpose
This binary functions as a **packer or loader** (often called a "stub"). Its primary purpose is not to perform its own functional actions but to decrypt and execute a hidden secondary payload. 

The namespace `XorExtract` and internal classes like `Orchestrator`, `PathResolver`, and `AssemblyExecutor` indicate a multi-stage loading process:
1.  **Extraction:** It locates an encrypted/obfuscated data blob embedded within the file.
2.  **Decryption:** It uses the `DataProcessor` class to decrypt this data (likely using XOR operations, given the naming convention).
3.  **Resolution & Execution:** The `PathResolver` and `AssemblyExecutor` components are used to resolve the entry point of the decrypted code and execute it in memory.

### Suspicious or Malicious Behaviors
*   **Payload Decryption:** The presence of functions like `DecryptData`, `VerifyMarker`, and `GenerateKeyPart1/2` strongly suggests that the actual malicious payload is encrypted within this file to evade signature-based detection.
*   **Hidden Execution (Reflective Loading):** The `AssemblyExecutor` class, specifically methods like `PrepareArguments` and `InvokeEntry`, suggest the binary might be performing reflective loading or dynamic assembly execution—loading a .NET DLL/EXE into memory without saving it to disk to evade forensic analysis.
*   **Anti-Analysis Obfuscation:** The disassembly is riddled with "bad instruction" errors, overlapping instructions, and forced jumps. This is a deliberate technique used to break the logic of disassemblers (like Ghidra or IDA) and make manual analysis much more difficult for a human researcher.
*   **Data Obfuscation:** The long hex string in the `Strings` section is likely an encrypted key or a hardcoded seed used by the `DataProcessor` to decrypt the main payload.

### Notable Techniques and Patterns
*   **Anti-Disassembly:** The decompiler's failure to resolve control flow (e.g., `halt_baddata()`, "overlap instruction") indicates the use of **junk code insertion** or **opaque predicates**. These are standard techniques used in malware to hide the true execution path from automated tools.
*   **Modular Design:** The code is structured into distinct components (`Orchestrator`, `DataProcessor`, `PathResolver`). This modularity allows the author to swap out encryption algorithms or delivery methods while keeping the core "loader" logic intact.
*   **Custom Decryption Loop:** The complexity and mathematical operations seen in `DataProcessor` (using things like `POPCOUNT` and complex bitwise manipulations) suggest a custom-built decryption routine rather than a standard library, which is common in high-quality malware to bypass simple scanners.

### Summary for Incident Response
This is a **highly suspicious loader stub**. It contains significant layers of obfuscation intended to hide its true functionality. The presence of `XorExtract` and `AssemblyExecutor` confirms that it is designed to "unpack" or "de-obfuscate" secondary components into memory. **Any system where this binary is found should be treated as compromised, as the primary payload is likely hidden behind these layers.**

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The binary uses XOR decryption, junk code insertion, and overlapping instructions to hide its true functionality from both automated tools and manual analysis. |
| T1630 | Reflective Loader | The `AssemblyExecutor` component facilitates the loading of a .NET assembly into memory for execution without saving it to disk to evade forensic detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `C:\Users\...\AppData\Local\Temp\DllExporter\MpAsDesc.pdb` (Note: This indicates a non-standard build artifact or temporary drop location).

**Mutex names / Named pipes**
*   *None explicitly identified in the strings.*

**Hashes**
*   `1217B945CC894D7DF646635E4DDF0F22F7C9DE11EF5BC47E75D0062D439DBA7B` (Identified as a hardcoded encryption key or seed).

**Other artifacts**
*   **GUID:** `$ed738e15-545b-482e-8496-93bbff144d72`
*   **Internal Module/Class Names (Telltale signs of specific packer logic):** 
    *   `XorExtract`
    *   `Orchestrator`
    *   `PathResolver`
    *   `AssemblyExecutor`
    *   `DataProcessor`
    *   `VerifyMarker`
*   **Notable Behavior Indicators:** Reflective loading of .NET assemblies, custom XOR-based decryption loops, and the presence of "junk code" to impede disassembly.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High (for Type) / Low (for Family)
4. **Key evidence**:
    *   **Reflective Loading:** The presence of the `AssemblyExecutor` class and the use of techniques like T1630 indicate it is designed to execute .NET assemblies directly in memory to evade disk-based detection.
    *   **Multi-Stage Decryption:** The specialized modules (`XorExtract`, `DataProcessor`, and `VerifyMarker`) confirm its primary role is as a "stub" or "wrapper" intended to decrypt and unpack a hidden secondary payload.
    *   **Anti-Analysis Techniques:** The use of junk code, overlapping instructions, and complex bitwise operations (e.g., `POPCOUNT`) are classic indicators of a loader designed to frustrate automated sandboxes and manual reverse engineering.
