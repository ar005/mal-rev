# Threat Analysis Report

**Generated:** 2026-07-13 14:04 UTC
**Sample:** `054ad4bf54b21866acc10d47c7fff6cdff699d4093f6fe1d759e8124e6faa8c0_054ad4bf54b21866acc10d47c7fff6cdff699d4093f6fe1d759e8124e6faa8c0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `054ad4bf54b21866acc10d47c7fff6cdff699d4093f6fe1d759e8124e6faa8c0_054ad4bf54b21866acc10d47c7fff6cdff699d4093f6fe1d759e8124e6faa8c0.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 2 sections |
| Size | 328,704 bytes |
| MD5 | `3536df7f6e240942b7e84508d1a03afd` |
| SHA1 | `c09c76403429e0ee67a1816d012a9a836d0f6384` |
| SHA256 | `054ad4bf54b21866acc10d47c7fff6cdff699d4093f6fe1d759e8124e6faa8c0` |
| Overall entropy | 6.755 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2441795967 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 327,680 | 6.766 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1936** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.reloc
v4.0.30319
#Strings
<Module>
System.IO
<0>__R
TripleDES
set_IV
mscorlib
set_Mode
PaddingMode
CompressionMode
CipherMode
Invoke
IDisposable
RuntimeTypeHandle
GetTypeFromHandle
get_Name
get_ReturnType
SetProcessDPIAware
MethodBase
Dispose
Create
EmbeddedAttribute
CompilerGeneratedAttribute
AttributeUsageAttribute
DebuggableAttribute
RefSafetyRulesAttribute
CompilationRelaxationsAttribute
RuntimeCompatibilityAttribute
add_AssemblyResolve
Loader.exe
set_Padding
FromBase64String
get_Length
TransformFinalBlock
user32.dll
protobuf-net.dll
GetManifestResourceStream
GZipStream
MemoryStream
System
SymmetricAlgorithm
ICryptoTransform
AppDomain
get_CurrentDomain
Version
System.IO.Compression
System.Reflection
MethodInfo
ParameterInfo
PayloadSource.zip
PCLoader
ResolveEventHandler
CreateDecryptor
System.Diagnostics
GetMethods
System.Runtime.CompilerServices
DebuggingModes
GetTypes
BindingFlags
ResolveEventArgs
Microsoft.CodeAnalysis
Contains
GetParameters
AttributeTargets
Object
Convert
ToArray
set_Key
System.Security.Cryptography
get_Assembly
op_Equality
WrapNonExceptionThrows
AllowMultiple
	Inherited
Do54Eu.
@?>]d"n
U2F?q<
Ll"jb/E
/wi?$}
6&&@bJd
L	uM^f
!M$%|K
%^(*fb,
=3D'
$nq'g?
Zje}fL
Wf51.b
	RI
[Y
PpBl@
BZ3 /"n[
j:S*H"
3#X(e)
uIm*13
01(}|K
GKl="(
K+d ]*
yJ]8.^
```

## Disassembly Overview

Functions analyzed: **4** | Decompiled to C: **4**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x4020f8` | 39826 | ✓ |
| `method.PCLoader.R` | `0x402068` | 144 | ✓ |
| `method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor` | `0x402058` | 16 | ✓ |
| `method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor` | `0x402050` | 8 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c`](code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c)
- [`code/method.PCLoader.R.c`](code/method.PCLoader.R.c)
- [`code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c`](code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary sample:

### Core Functionality and Purpose
The binary functions as a **multi-stage loader (or "packer")**. Its primary purpose is to decrypt and decompress an embedded payload—likely a malicious DLL or EXE—and execute it in memory. 

Key indicators include:
*   **Payload Extraction:** The presence of `GetManifestResourceStream`, `GZipStream`, and `MemoryStream` suggests that the actual "payload" is bundled inside the binary as a compressed resource.
*   **Decryption Routine:** The inclusion of `TripleDES`, `SymmetricAlgorithm`, and `CreateDecryptor` indicates that the internal payload is encrypted using Triple DES (3DES) before being extracted.
*   **Reflection-based Execution:** The use of `System.Reflection` (`GetMethods`, `GetTypes`, `MethodInfo`) suggests that once the payload is decrypted in memory, the loader uses reflection to find and call the main entry point of the hidden functionality without ever saving the decrypted code to the disk (in-memory execution).

### Suspicious or Malicious Behaviors
*   **Payload Encapsulation:** The string `PayloadSource.zip` confirms the presence of a bundled, potentially malicious, secondary payload.
*   **Anti-Analysis/Obfuscation:** 
    *   The decompiled code is heavily obfuscated with "junk" instructions and complex arithmetic to calculate memory offsets (e.g., calculations involving `0x1ebd9ed` or `0xf86541`). This is designed to break the logic of automated decompilers and slow down manual analysis.
    *   The presence of many overlapping blocks and "bad instruction" warnings in the disassembly suggests **Control Flow Flattening** or **Instruction Substitution**, common techniques used by protectors like ConfuserEx or VMProtect.
*   **Reflective Loading:** By using `System.Reflection` to resolve methods at runtime, the malware avoids creating a traditional Import Address Table (IAT) for its malicious components, making it harder for security software to detect what functions are being called.

### Notable Techniques and Patterns
*   **Standard Encryption/Compression Stack:** The use of `TripleDES` combined with `GZipStream` is a classic "packer" pattern used to hide malicious payloads from static signature-based detection.
*   **Resource Embedding:** Instead of downloading the payload over the network immediately, it stores it as an internal resource (likely under the name `PayloadSource`), which allows for "offline" infection.
*   **Heavy De-compilation Resistance:** The use of complex, nested calculations for what are essentially simple memory offsets is a high-effort obfuscation technique used to hide the program's logic from human analysts.

### Summary for Incident Response
This sample is highly likely a **Downloader or Dropper**. It contains an encrypted and compressed "Stage 2" payload. The primary indicators of compromise (IoCs) would be:
1.  **Persistence/Execution:** Once executed, it will decompress the internal payload into memory.
2.  **Technique:** Reflective Loading and highly obfuscated control flow to evade heuristic detection.
3.  **Detection Point:** The most effective point for interception is at the `CreateDecryptor` or `GZipStream` calls, where the payload must be "plain" in a buffer before execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of TripleDES, GZipStream, Junk Instructions, and Control Flow Flattening are used to hide the payload's logic and evade signature-based detection. |
| T1633 | Reflective Code Loading | The application uses `System.Reflection` to resolve and execute methods in memory, allowing it to bypass traditional disk-based security controls. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that many items in the raw data were identified as standard .NET framework libraries (e.g., `System.IO`, `mscorlib`, `user32.dll`) and have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **PayloadSource.zip** (Identified as the internal resource name for the embedded payload.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (Note: Hexadecimal values like `0x1ebd9ed` in the analysis refer to memory offsets/instructions, not file hashes.)

### **Other artifacts**
*   **Internal Component Name:** `PCLoader`
*   **Encryption Algorithm:** `TripleDES` (3DES) / `SymmetricAlgorithm`
*   **Compression Method:** `GZipStream`
*   **Technical Indicators:** 
    *   Reflective Loading via `System.Reflection`
    *   Use of `GetManifestResourceStream` for internal payload extraction.
    *   Detection of "Control Flow Flattening" and "Instruction Substitution" (indicative of a packer like ConfuserEx or VMProtect).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Multi-stage Execution:** The binary acts as a wrapper/loader that extracts an embedded resource (`PayloadSource.zip`), decrypts it using `TripleDES`, and decompresses it using `GZipStream`.
*   **Reflective Loading:** It utilizes `System.Reflection` to execute the decrypted payload directly in memory, a common technique used to bypass disk-based antivirus signatures.
*   **Advanced Obfuscation:** The presence of "Control Flow Flattening" and "Instruction Substitution" (typical of tools like ConfuserEx) indicates high-effort efforts to hinder automated analysis and hide its true functionality.
