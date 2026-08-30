# Threat Analysis Report

**Generated:** 2026-08-16 21:42 UTC
**Sample:** `0fe0289579b5859b4f091a492ba52dd1ac2f53c9a0bf9496339d51fa8a5bfb96_0fe0289579b5859b4f091a492ba52dd1ac2f53c9a0bf9496339d51fa8a5bfb96.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0fe0289579b5859b4f091a492ba52dd1ac2f53c9a0bf9496339d51fa8a5bfb96_0fe0289579b5859b4f091a492ba52dd1ac2f53c9a0bf9496339d51fa8a5bfb96.exe` |
| File type | PE32+ executable for MS Windows 4.00 (DLL), x86-64 Mono/.Net assembly, 4 sections |
| Size | 221,696 bytes |
| MD5 | `4c27694952bf91d0c487aef206a340f9` |
| SHA1 | `1ae1129e75bc23c691c77dcfbc5950539175f763` |
| SHA256 | `0fe0289579b5859b4f091a492ba52dd1ac2f53c9a0bf9496339d51fa8a5bfb96` |
| Overall entropy | 6.605 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773952346 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 78,848 | 6.271 | No |
| `.sdata` | 512 | 1.233 | No |
| `.reloc` | 512 | 0.174 | No |
| `.text` | 140,800 | 6.772 | No |

### Imports

**mscoree.dll**: `_CorDllMain`

### Exports

`DllRegisterServer`, `Entry`

## Extracted Strings

Total strings found: **2484** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.sdata
.reloc
B.text
v4.0.30319
#Strings
%*1@Wel
<Module>
System.Runtime.CompilerServices
CompilationRelaxationsAttribute
RuntimeCompatibilityAttribute
System.Runtime.Versioning
TargetFrameworkAttribute
System
Object
System.Text
Encoding
get_UTF8
GetString
RuntimeHelpers
RuntimeFieldHandle
InitializeArray
String
System.Security.Cryptography
RijndaelManaged
ICryptoTransform
System.Threading
Monitor
SymmetricAlgorithm
set_Key
set_IV
CipherMode
set_Mode
PaddingMode
set_Padding
CreateEncryptor
TransformFinalBlock
IDisposable
Dispose
CreateDecryptor
Convert
FromBase64String
CompilerGeneratedAttribute
UnhandledExceptionEventHandler
ThreadStart
UnhandledExceptionEventArgs
Random
IntPtr
AppDomain
get_CurrentDomain
add_UnhandledException
Thread
set_IsBackground
OpenExisting
WaitHandle
WaitHandleCannotBeOpenedException
Environment
SpecialFolder
GetFolderPath
System.IO
Combine
GetBytes
WriteAllBytes
FileAttributes
SetAttributes
Exists
ReadAllBytes
IsNullOrEmpty
System.Collections.Generic
List`1
System.Collections
IEnumerator
Concat
System.Text.RegularExpressions
MatchCollection
Matches
GetEnumerator
get_Current
GroupCollection
get_Groups
get_Item
Capture
get_Value
Contains
MoveNext
ToArray
System.Net
WebClient
WebHeaderCollection
get_Headers
System.Collections.Specialized
NameValueCollection
DownloadData
System.Net.Sockets
TcpClient
Connect
StringBuilder
DateTime
FileInfo
get_Length
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Shared.S.Get` | `0x180004560` | 68826 | ✓ |
| `method.Watchdog.WatchdogInstallerClass..ctor` | `0x180008197` | 65536 | ✓ |
| `method.Watchdog.WatchdogInstallerClass.Uninstall` | `0x18000818e` | 50130 | ✓ |
| `method.Shared.S..cctor` | `0x1800045d0` | 9440 | ✓ |
| `method.Watchdog.WatchdogDllMain.EnsureTor` | `0x18000731c` | 732 | ✓ |
| `method.Watchdog.WatchdogDllMain.RecoverSkywalker` | `0x180006e7c` | 584 | ✓ |
| `method.Watchdog.WatchdogDllMain.DecryptPayload` | `0x180007918` | 476 | ✓ |
| `method.Watchdog.WatchdogDllMain.ExtractFileFromTarGz` | `0x180007740` | 472 | ✓ |
| `method.Watchdog.WatchdogDllMain.BuildPayloadUrls` | `0x1800070c4` | 364 | ✓ |
| `method.Watchdog.WatchdogDllMain.TryDownloadViaTor` | `0x1800075f8` | 328 | ✓ |
| `method.Watchdog.WatchdogDllMain.LaunchDll` | `0x180007fe0` | 304 | ✓ |
| `method.Watchdog.WatchdogDllMain.BuildLaunchCommand` | `0x180007e1c` | 236 | ✓ |
| `method.Watchdog.WatchdogDllMain.SetRunPersistence` | `0x180007f08` | 216 | ✓ |
| `method.Watchdog.WatchdogDllMain.CleanDeadRunEntries` | `0x180007d50` | 204 | ✓ |
| `method.Watchdog.WatchdogDllMain.SaveStealthDll` | `0x180007c34` | 192 | ✓ |
| `method.Shared.Crypto.AesCrypto.Encrypt` | `0x180006ab0` | 168 | ✓ |
| `method.Shared.Crypto.AesCrypto.Decrypt` | `0x180006b58` | 168 | ✓ |
| `method.Watchdog.WatchdogDllMain.RunWatchdog` | `0x180006cb8` | 164 | ✓ |
| `method.Watchdog.WatchdogDllMain.get_STEALTH_NAMES` | `0x180007af4` | 152 | ✓ |
| `method.Watchdog.WatchdogDllMain.TryDownloadDirect` | `0x180007230` | 144 | ✓ |
| `sym.guardian.dll_Entry` | `0x180015246` | 120 | ✓ |
| `method.Watchdog.WatchdogDllMain.Entry` | `0x180006c44` | 116 | ✓ |
| `method.Watchdog.WatchdogDllMain.IsSkywalkerAlive` | `0x180006d5c` | 92 | ✓ |
| `method.Watchdog.WatchdogDllMain.SaveSkywalkerPath` | `0x180006dd0` | 92 | ✓ |
| `method.Watchdog.WatchdogDllMain.IsTorAlive` | `0x1800072c0` | 92 | ✓ |
| `method.Watchdog.WatchdogDllMain.IsOurRunEntry` | `0x180007cf4` | 92 | ✓ |
| `method.Watchdog.WatchdogDllMain.get_STEALTH_DIRS` | `0x180007b8c` | 84 | ✓ |
| `method.Watchdog.WatchdogDllMain.get_STEALTH_REG_NAMES` | `0x180007be0` | 84 | ✓ |
| `method.Watchdog.WatchdogDllMain.ReadSkywalkerPath` | `0x180006e2c` | 80 | ✓ |
| `method.Shared.Crypto.AesCrypto..cctor` | `0x180006c00` | 42 | ✓ |

### Decompiled Code Files

- [`code/method.Shared.Crypto.AesCrypto..cctor.c`](code/method.Shared.Crypto.AesCrypto..cctor.c)
- [`code/method.Shared.Crypto.AesCrypto.Decrypt.c`](code/method.Shared.Crypto.AesCrypto.Decrypt.c)
- [`code/method.Shared.Crypto.AesCrypto.Encrypt.c`](code/method.Shared.Crypto.AesCrypto.Encrypt.c)
- [`code/method.Shared.S..cctor.c`](code/method.Shared.S..cctor.c)
- [`code/method.Shared.S.Get.c`](code/method.Shared.S.Get.c)
- [`code/method.Watchdog.WatchdogDllMain.BuildLaunchCommand.c`](code/method.Watchdog.WatchdogDllMain.BuildLaunchCommand.c)
- [`code/method.Watchdog.WatchdogDllMain.BuildPayloadUrls.c`](code/method.Watchdog.WatchdogDllMain.BuildPayloadUrls.c)
- [`code/method.Watchdog.WatchdogDllMain.CleanDeadRunEntries.c`](code/method.Watchdog.WatchdogDllMain.CleanDeadRunEntries.c)
- [`code/method.Watchdog.WatchdogDllMain.DecryptPayload.c`](code/method.Watchdog.WatchdogDllMain.DecryptPayload.c)
- [`code/method.Watchdog.WatchdogDllMain.EnsureTor.c`](code/method.Watchdog.WatchdogDllMain.EnsureTor.c)
- [`code/method.Watchdog.WatchdogDllMain.Entry.c`](code/method.Watchdog.WatchdogDllMain.Entry.c)
- [`code/method.Watchdog.WatchdogDllMain.ExtractFileFromTarGz.c`](code/method.Watchdog.WatchdogDllMain.ExtractFileFromTarGz.c)
- [`code/method.Watchdog.WatchdogDllMain.IsOurRunEntry.c`](code/method.Watchdog.WatchdogDllMain.IsOurRunEntry.c)
- [`code/method.Watchdog.WatchdogDllMain.IsSkywalkerAlive.c`](code/method.Watchdog.WatchdogDllMain.IsSkywalkerAlive.c)
- [`code/method.Watchdog.WatchdogDllMain.IsTorAlive.c`](code/method.Watchdog.WatchdogDllMain.IsTorAlive.c)
- [`code/method.Watchdog.WatchdogDllMain.LaunchDll.c`](code/method.Watchdog.WatchdogDllMain.LaunchDll.c)
- [`code/method.Watchdog.WatchdogDllMain.ReadSkywalkerPath.c`](code/method.Watchdog.WatchdogDllMain.ReadSkywalkerPath.c)
- [`code/method.Watchdog.WatchdogDllMain.RecoverSkywalker.c`](code/method.Watchdog.WatchdogDllMain.RecoverSkywalker.c)
- [`code/method.Watchdog.WatchdogDllMain.RunWatchdog.c`](code/method.Watchdog.WatchdogDllMain.RunWatchdog.c)
- [`code/method.Watchdog.WatchdogDllMain.SaveSkywalkerPath.c`](code/method.Watchdog.WatchdogDllMain.SaveSkywalkerPath.c)
- [`code/method.Watchdog.WatchdogDllMain.SaveStealthDll.c`](code/method.Watchdog.WatchdogDllMain.SaveStealthDll.c)
- [`code/method.Watchdog.WatchdogDllMain.SetRunPersistence.c`](code/method.Watchdog.WatchdogDllMain.SetRunPersistence.c)
- [`code/method.Watchdog.WatchdogDllMain.TryDownloadDirect.c`](code/method.Watchdog.WatchdogDllMain.TryDownloadDirect.c)
- [`code/method.Watchdog.WatchdogDllMain.TryDownloadViaTor.c`](code/method.Watchdog.WatchdogDllMain.TryDownloadViaTor.c)
- [`code/method.Watchdog.WatchdogDllMain.get_STEALTH_DIRS.c`](code/method.Watchdog.WatchdogDllMain.get_STEALTH_DIRS.c)
- [`code/method.Watchdog.WatchdogDllMain.get_STEALTH_NAMES.c`](code/method.Watchdog.WatchdogDllMain.get_STEALTH_NAMES.c)
- [`code/method.Watchdog.WatchdogDllMain.get_STEALTH_REG_NAMES.c`](code/method.Watchdog.WatchdogDllMain.get_STEALTH_REG_NAMES.c)
- [`code/method.Watchdog.WatchdogInstallerClass..ctor.c`](code/method.Watchdog.WatchdogInstallerClass..ctor.c)
- [`code/method.Watchdog.WatchdogInstallerClass.Uninstall.c`](code/method.Watchdog.WatchdogInstallerClass.Uninstall.c)
- [`code/sym.guardian.dll_Entry.c`](code/sym.guardian.dll_Entry.c)

## Behavioral Analysis

Based on the provided strings and decompiled code, this binary is a **multi-stage malware loader/dropper** designed for persistence, evasion, and delivery of secondary payloads.

The presence of various "Watchdog" and "Stealth" related functions suggests it is part of a sophisticated threat actor's toolkit (likely a botnet or ransomware loader).

### Core Functionality
The program acts as a "loader." Its primary role is to download an encrypted/compressed payload from a remote server, decrypt it, extract the files, and ensure the malicious components remain active on the system.

### Suspicious & Malicious Behaviors
*   **Anonymized Networking (Tor):** 
    *   The function `TryDownloadViaTor` indicates the malware is designed to communicate over the Tor network to hide the location of its Command and Control (C2) servers or to bypass geographic IP blocking.
    *   `TryDownloadDirect` serves as a fallback mechanism if the Tor connection fails.
*   **Persistence Mechanisms:** 
    *   The function `SetRunPersistence` explicitly aims to ensure that the malware remains active after system reboots. This typically involves modifying Registry "Run" keys or creating Scheduled Tasks.
*   **Payload Decryption & Extraction:**
    *   The code includes logic for `DecryptPayload` (using AES/Rijndael) and `ExtractFileFromTarGz`. This indicates that the primary malicious payload is "packed" inside this loader to evade static detection by antivirus scanners.
*   **Stealth Operations:**
    *   Several functions (`get_STEALTH_NAMES`, `get_STEALTH_DIRS`, `get_STEALTH_REG_NAMES`) suggest a mechanism for hiding its footprint. The malware likely checks for or modifies file attributes and registry keys to hide from the user or automated system scans.
*   **Process/DLL Execution:**
    *   The `LaunchDll` and `BuildLaunchCommand` functions indicate that after extracting the payload, the loader will execute it (possibly via process injection or by launching a separate command line).

### Notable Techniques & Patterns
*   **Multi-Stage Loading:** By using an initial "loader" to fetch a secondary DLL/executable, the malware reduces the amount of "malicious" code in the first file that touches the network.
*   **Obfuscation via Decompilation Hurdles:** The frequent `halt_baddata` and `bad instruction` warnings in the decompiled output are often symptoms of **anti-analysis techniques**. These occur when a developer uses "junk code" or non-standard instructions to confuse disassemblers like Hex-Rays/Ghidra.
*   **Complexity in Communication:** The use of both Tor and direct downloads suggests a sophisticated infrastructure designed to maintain connectivity even if one method is blocked by security software.
*   **Codename Usage:** The presence of "Skywalker" (e.g., `IsSkywalkerAlive`, `SaveSkywalkerPath`) is likely an internal codename used by the developers for specific modules or high-value functionality within the malware's ecosystem.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1090** | Proxy | The use of Tor (`TryDownloadViaTor`) to mask C2 infrastructure and bypass geographic IP filtering. |
| **T1105** | Ingress Tool Transfer Protocol | Utilizing both Tor and direct connections to download additional payloads from remote servers. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys/Startup Folder | The `SetRunPersistence` function explicitly targets registry "Run" keys to ensure the malware remains active after reboots. |
| **T1027** | Obfuscated Files or Information | The use of AES encryption, TarGz compression, and "junk code" (bad instructions) to hide payload functionality from scanners/analysts. |
| **T1036** | Masquerading | The `STEALTH` functions suggest the malware hides its file names, directory paths, and registry keys to evade detection. |
| **T1059** | Command and Scripting Interpreter | The `BuildLaunchCommand` function indicates the creation of command-line strings to execute the extracted payload components. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *None identified.* (The report notes the use of the **Tor network** and a "Direct" download fallback, but no specific C2 domains or IP addresses were listed in the provided text.)

**File paths / Registry keys**
*   `guardian.dll` (Identified as a specific component/file name)
*   `Run` keys (Mentioned in behavioral analysis as the target for persistence; specifically **Registry Run Keys**)
*   `STEALTH_DIRS` (References internal logic to identify hidden file paths)
*   `STEALTH_REG_NAMES` (References internal logic for identifying/manipulating registry keys)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Codename:** `Skywalker` (Internal identifier used in several functions: `IsSkywalkerAlive`, `SaveSkywalkerPath`)
*   **Encryption Method:** `RijndaelManaged` / AES (Used for payload decryption)
*   **Compression Format:** `.tar.gz` (Used for payload extraction)
*   **Communication Tactics:** 
    *   `TryDownloadViaTor` (Function used to bypass geo-blocking/anonymize traffic)
    *   `TryDownloadDirect` (Fallback mechanism for direct connections)
*   **Suspicious Function Names:** `LaunchDll`, `BuildLaunchCommand`, `DecryptPayload`, `ExtractFileFromTarGz`

---

## Malware Family Classification

1. **Malware family**: Unknown (likely a custom-built tool)
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Delivery Architecture:** The binary is designed to fetch, decrypt (AES/Rijndael), and extract secondary payloads from compressed archives (.tar.gz). This "wrapper" behavior is a hallmark of a sophisticated loader intended to shield the primary malicious payload from initial detection.
*   **Advanced Persistence & Evasion:** The inclusion of explicit "Stealth" functions for hiding file paths/registry keys, combined with `SetRunPersistence` (Registry Run Keys), indicates an intent to maintain a long-term presence on the host while evading manual or automated discovery.
*   **Sophisticated Networking:** The use of Tor (`TryDownloadViaTor`) as a primary communication method suggests a high level of operational security (OpSec) designed to mask C2 infrastructure and bypass geographic filtering, typical of professional threat actors or complex botnet infrastructures.
