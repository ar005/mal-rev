# Threat Analysis Report

**Generated:** 2026-07-17 18:43 UTC
**Sample:** `07c0609ee3b96b3ea827ec0d7b2d38124614566fd9b0eb51920aa6d07c7cd519_07c0609ee3b96b3ea827ec0d7b2d38124614566fd9b0eb51920aa6d07c7cd519.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07c0609ee3b96b3ea827ec0d7b2d38124614566fd9b0eb51920aa6d07c7cd519_07c0609ee3b96b3ea827ec0d7b2d38124614566fd9b0eb51920aa6d07c7cd519.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64 Mono/.Net assembly, 2 sections |
| Size | 755,200 bytes |
| MD5 | `208f11c756159725c8308a0cdfeb1209` |
| SHA1 | `18ff01f9e5f72434aae0c4b7d6a054ba3531fed6` |
| SHA256 | `07c0609ee3b96b3ea827ec0d7b2d38124614566fd9b0eb51920aa6d07c7cd519` |
| Overall entropy | 6.824 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3600851286 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 753,152 | 6.821 | No |
| `.rsrc` | 1,536 | 3.98 | No |

## Extracted Strings

Total strings found: **11254** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
v4.0.30319
#Strings
ToUInt32
ReadInt32
ToInt32
cbReserved2
lpReserved2
CONTEXT64
ToInt64
ToInt16
get_UTF8
<Module>
PROCESS_INFORMATION
STARTUPINFO
System.IO
mscorlib
dwThreadId
dwProcessId
GetProcessById
ResumeThread
hThread
payload
lpReserved
FixedElementField
DecryptSafe
get_Message
IDisposable
RuntimeTypeHandle
GetTypeFromHandle
Console
lpTitle
lpApplicationName
P1Home
P2Home
P3Home
P4Home
P5Home
P6Home
lpCommandLine
WriteLine
Combine
ValueType
flAllocationType
PtrToStructure
Dispose
EmbeddedAttribute
CompilerGeneratedAttribute
UnverifiableCodeAttribute
AttributeUsageAttribute
DebuggableAttribute
AssemblyTitleAttribute
UnsafeValueTypeAttribute
TargetFrameworkAttribute
dwFillAttribute
AssemblyFileVersionAttribute
AssemblyInformationalVersionAttribute
SecurityPermissionAttribute
AssemblyConfigurationAttribute
FixedBufferAttribute
RefSafetyRulesAttribute
CompilationRelaxationsAttribute
AssemblyProductAttribute
AssemblyCompanyAttribute
RuntimeCompatibilityAttribute
ReadByte
XOR_Loader.exe
dwXSize
dwYSize
dwSize
SizeOf
Encoding
System.Runtime.Versioning
ToString
GetFolderPath
get_Length
AllocHGlobal
FreeHGlobal
Marshal
kernel32.dll
ntdll.dll
GetManifestResourceStream
Program
System
lpNumberOfBytesWritten
SeekOrigin
Version
lpProcessInformation
SecurityAction
NtUnmapViewOfSection
System.Reflection
get_Position
Exception
lpStartupInfo
XOR_Loader.build.bmp
lpDesktop
Header
BinaryReader
XOR_Loader
```

## Disassembly Overview

Functions analyzed: **6** | Decompiled to C: **6**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor` | `0x140002051` | 761776 | ✓ |
| `entry0` | `0x140002064` | 761756 | ✓ |
| `method.XOR_Loader.Program..ctor` | `0x1400026ac` | 63928 | ✓ |
| `method.XOR_Loader.Program.RunHollow` | `0x1400022f0` | 956 | ✓ |
| `method.XOR_Loader.Program.DecryptSafe` | `0x140002138` | 440 | ✓ |
| `method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor` | `0x140002048` | 9 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c`](code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c)
- [`code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c`](code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c)
- [`code/method.XOR_Loader.Program..ctor.c`](code/method.XOR_Loader.Program..ctor.c)
- [`code/method.XOR_Loader.Program.DecryptSafe.c`](code/method.XOR_Loader.Program.DecryptSafe.c)
- [`code/method.XOR_Loader.Program.RunHollow.c`](code/method.XOR_Loader.Program.RunHollow.c)

## Behavioral Analysis

Based on the provided disassembly and string extractions, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
The binary is a **malware loader** (specifically titled "XOR_Loader"). Its primary purpose is to decrypt an embedded payload and inject it into a separate process to execute. The presence of `.NET` artifacts suggests this is a managed-code loader designed to hide the final malicious payload from simple signature-based detection.

### Suspicious or Malicious Behaviors
*   **Process Hollowing:** This is the most prominent malicious behavior identified. The inclusion of the following specific functions is a classic indicator:
    *   `RunHollow`: A direct reference to the "hollowing" technique.
    *   `NtUnmapViewOfSection`: Used to unmap the memory of a legitimate process to make room for the injected payload.
    *   `WriteProcessMemory` & `VirtualAllocEx`: Used to allocate memory in a remote/target process and copy the decrypted payload into it.
    *   `GetThreadContext` & `SetThreadContext`: Typically used during hollowing to redirect the execution flow of the hijacked thread to the new malicious entry point.
    *   `ResumeThread`: Used to start execution once the memory has been swapped.
*   **Payload Decryption:** The function `DecryptSafe` suggests that the main payload is not stored in plaintext. It likely uses an XOR-based algorithm (as hinted by the name "XOR_Loader") or another simple cipher to hide its presence on disk.
*   **Evasive Execution:** By using a loader, the malware ensures that the actual malicious functionality is only present in memory after being decrypted and injected into a different process, making it harder for antivirus scanners to detect the primary payload file.

### Notable Techniques or Patterns
*   **Process Injection Chain:** The binary follows a standard "Loader" pattern: 
    1.  Read/Decrypt embedded data (via `DecryptSafe`).
    2.  Spawn a target process in a suspended state.
    3.  Unmap the original code (`NtUnmapViewOfSection`).
    4.  Write the new payload to that memory space.
    5.  Adjust execution context and resume.
*   **Use of .NET Framework:** The sample utilizes common .NET libraries (like `System.Reflection` and `System.Runtime.InteropServices`) to interact directly with low-level Windows APIs (`kernel32.dll`, `ntdll.dll`). 
*   **Resource Loading:** The presence of "XOR_Loader.build.bmp" and various system strings suggests it may use standard resources for metadata or basic GUI elements before the main loader logic takes over.

### Summary
This is a **highly suspicious loader**. It utilizes **Process Hollowing** to execute an encrypted payload within the memory space of a separate process, which is a hallmark of modern malware designed to bypass security software and evade detection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055.001 | Process Hollow | The binary explicitly utilizes `NtUnmapViewOfSection`, `WriteProcessMemory`, and `SetThreadContext` to replace the memory of a legitimate process with a malicious payload. |
| T1027 | Obfuscated Files or Information | The use of the `DecryptSafe` function and XOR-based encryption is intended to hide the primary payload from signature-based detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `XOR_Loader.exe` (Primary executable filename)
*   `XOR_Loader.build.bmp` (Embedded resource/artifact)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified in the provided text.*

**Other artifacts**
*   **Malicious Techniques:** Process Hollowing (identified via the specific sequence of `NtUnmapViewOfSection`, `WriteProcessMemory`, `VirtualAllocEx`, `GetThreadContext`, and `SetThreadContext`).
*   **Internal Labels/Identifiers:** `XOR_Loader` (Used as an internal naming convention for the malware's core logic).
*   **Library Usage:** Reliance on `.NET Framework 4.8` and `mscorlib` to facilitate malicious execution in a managed environment.

---

## Malware Family Classification

1. **Malware family**: custom (loader)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
* **Process Hollowing Implementation:** The binary utilizes a complete sequence of API calls (`NtUnmapViewOfSection`, `VirtualAllocEx`, `WriteProcessMemory`, `GetThreadContext`, and `SetThreadContext`) to replace the code of a legitimate process with a malicious one.
* **Obfuscation & Payload Delivery:** The presence of the `DecryptSafe` function indicates the use of XOR-based encryption to hide an embedded payload, which is then decrypted in memory to bypass disk-based antivirus scans.
* **Detection Evasion Architecture:** The combination of .NET infrastructure and known "loader" patterns (hollowing + decryption) confirms its primary purpose is as a vehicle for delivering subsequent malicious payloads rather than performing final actions itself.
