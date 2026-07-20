# Threat Analysis Report

**Generated:** 2026-07-18 18:07 UTC
**Sample:** `08afb4d1eea5ca092fc3243049e1d737d5239db7d9aa69467f8fd6c742fe3797_08afb4d1eea5ca092fc3243049e1d737d5239db7d9aa69467f8fd6c742fe3797.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08afb4d1eea5ca092fc3243049e1d737d5239db7d9aa69467f8fd6c742fe3797_08afb4d1eea5ca092fc3243049e1d737d5239db7d9aa69467f8fd6c742fe3797.exe` |
| File type | PE32+ executable for MS Windows 4.00 (DLL), x86-64 Mono/.Net assembly, 4 sections |
| Size | 780,288 bytes |
| MD5 | `ad6ccf408c0eda72995826836b1fd360` |
| SHA1 | `b688463a650e498b45e0322980f7029afea673b5` |
| SHA256 | `08afb4d1eea5ca092fc3243049e1d737d5239db7d9aa69467f8fd6c742fe3797` |
| Overall entropy | 6.124 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774216632 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 360,448 | 6.064 | No |
| `.sdata` | 512 | 1.324 | No |
| `.reloc` | 512 | 0.159 | No |
| `.text` | 417,792 | 6.179 | No |

### Imports

**mscoree.dll**: `_CorDllMain`

### Exports

`DllRegisterServer`, `Entry`

## Extracted Strings

Total strings found: **7897** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.sdata
.reloc
B.text
p+tra
p+lru

%-&(M
p+*rW

p+*rg'
%- &rw4
&	,%	(#
p+r$<
+3 OMER
 OMER
	 OMER(

-.	{	

,&rAd

,&rYd

	rqu
 OMER(
 OMER(
 OMER(
Xl[%Z
Yl	ZiX~x
Yl	ZiX~x
 OMER(
 OMER(
@[Y+#

- OMER(

,\	oc
%,P	-M
p+=r6

+e	oJ
v4.0.30319
#Strings
!$!9!X!j!v!~!
" "1"7"<"@"I"X"_"e"s"
$)$G$U$\$a$l$
&.&6&?&c&j&p&v&
(!(8(V(_(
)!)8)@)K)U)b)%*-*3*9*J*
+!+K+Y+
,6,=,G,K,P,_,g,m,
-8-c-~-
. .:.C.Q.].f.r.|.
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
Environment
get_MachineName
get_UserName
DateTime
get_UtcNow
get_TickCount
Version
OperatingSystem
get_OSVersion
get_Version
get_Major
get_Build
get_Minor
ToString
Concat
IntPtr
get_Size
System.Security.Principal
WindowsIdentity
GetCurrent
WindowsPrincipal
WindowsBuiltInRole
IsInRole
System.Security.Cryptography
SHA256Managed
StringBuilder
get_ProcessorCount
GetBytes
HashAlgorithm
ComputeHash
Append
IDisposable
Dispose
Microsoft.Win32
RegistryKey
Registry
LocalMachine
OpenSubKey
GetValue
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Shared.Packets.BackupServerItem.OnDeserialized` | `0x180008601` | 768512 | ✓ |
| `sym.__c..ctor` | `0x18000b2a8` | 322262 | ✓ |
| `method.__c__DisplayClass369_0._ShowValidationMessage_b__0` | `0x180026401` | 74240 | ✓ |
| `method.Client.ClientCore.StopKeylogger` | `0x18001747d` | 31696 | ✓ |
| `method.Client.ClientCore.StopWindowMonitor` | `0x18001088b` | 25012 | ✓ |
| `method.__c__DisplayClass49_0._GetAllChildWindows_b__0` | `0x180027358` | 16208 | ✓ |
| `method.Client.ClientCore.HandleSystemDiagRequest` | `0x180013b84` | 11748 | ✓ |
| `method.Shared.S..cctor` | `0x180004600` | 9468 | ✓ |
| `method.__c__DisplayClass180_1..ctor` | `0x1800213fd` | 6240 | ✓ |
| `method.Client.ClientCore.CreateHoleFormInternal` | `0x180019cf0` | 5540 | ✓ |
| `method.Client.ClientCore.CheckBrowserWindows` | `0x180010908` | 4264 | ✓ |
| `method.Client.ClientCore.OnPacketReceived` | `0x18000d520` | 3804 | ✓ |
| `method.__c__DisplayClass250_0..ctor` | `0x180022f6b` | 3664 | ✓ |
| `method.Client.ClientCore.CreateComponentControl` | `0x18001b538` | 3648 | ✓ |
| `method.Client.ClientCore.SetupNativeBlockForm` | `0x18001e278` | 3440 | ✓ |
| `method.Client.ClientCore.SendMachineDiagLog` | `0x18000c638` | 3352 | ✓ |
| `method.Client.ClientCore.CreateJpegParams` | `0x18000fb97` | 3268 | ✓ |
| `method.__c__DisplayClass292_3..ctor` | `0x1800245af` | 3204 | ✓ |
| `method.Client.ClientCore.StopDetectDevTools` | `0x18001f2b9` | 3194 | ✓ |
| `method.Client.MouseHook.Unhook` | `0x18002019b` | 2924 | ✓ |
| `method.Client.ClientCore.StopClipboardMonitor` | `0x180016a3f` | 2622 | ✓ |
| `method.__c__DisplayClass357_1..ctor` | `0x1800254f9` | 2576 | ✓ |
| `method.Client.ClientCore.HandleUpdateClient` | `0x18000e7e4` | 2116 | ✓ |
| `method.__c__DisplayClass292_2..ctor` | `0x180023dbb` | 2036 | ✓ |
| `method.Client.ClientCore.Connect` | `0x18000b9ac` | 1828 | ✓ |
| `method.Client.ClientCore.HandleScreenshotReal` | `0x1800100a0` | 1752 | ✓ |
| `method.Client.ClientCore.TempBlockPoll` | `0x180018dbc` | 1620 | ✓ |
| `method.Client.ClientCore.ShowValidationMessage` | `0x18001c4bc` | 1476 | ✓ |
| `method.Client.ClientCore.HandleMouseClick` | `0x180012240` | 1380 | ✓ |
| `method.Client.ClientCore.LoadSession` | `0x18001d924` | 1336 | ✓ |

### Decompiled Code Files

- [`code/method.Client.ClientCore.CheckBrowserWindows.c`](code/method.Client.ClientCore.CheckBrowserWindows.c)
- [`code/method.Client.ClientCore.Connect.c`](code/method.Client.ClientCore.Connect.c)
- [`code/method.Client.ClientCore.CreateComponentControl.c`](code/method.Client.ClientCore.CreateComponentControl.c)
- [`code/method.Client.ClientCore.CreateHoleFormInternal.c`](code/method.Client.ClientCore.CreateHoleFormInternal.c)
- [`code/method.Client.ClientCore.CreateJpegParams.c`](code/method.Client.ClientCore.CreateJpegParams.c)
- [`code/method.Client.ClientCore.HandleMouseClick.c`](code/method.Client.ClientCore.HandleMouseClick.c)
- [`code/method.Client.ClientCore.HandleScreenshotReal.c`](code/method.Client.ClientCore.HandleScreenshotReal.c)
- [`code/method.Client.ClientCore.HandleSystemDiagRequest.c`](code/method.Client.ClientCore.HandleSystemDiagRequest.c)
- [`code/method.Client.ClientCore.HandleUpdateClient.c`](code/method.Client.ClientCore.HandleUpdateClient.c)
- [`code/method.Client.ClientCore.LoadSession.c`](code/method.Client.ClientCore.LoadSession.c)
- [`code/method.Client.ClientCore.OnPacketReceived.c`](code/method.Client.ClientCore.OnPacketReceived.c)
- [`code/method.Client.ClientCore.SendMachineDiagLog.c`](code/method.Client.ClientCore.SendMachineDiagLog.c)
- [`code/method.Client.ClientCore.SetupNativeBlockForm.c`](code/method.Client.ClientCore.SetupNativeBlockForm.c)
- [`code/method.Client.ClientCore.ShowValidationMessage.c`](code/method.Client.ClientCore.ShowValidationMessage.c)
- [`code/method.Client.ClientCore.StopClipboardMonitor.c`](code/method.Client.ClientCore.StopClipboardMonitor.c)
- [`code/method.Client.ClientCore.StopDetectDevTools.c`](code/method.Client.ClientCore.StopDetectDevTools.c)
- [`code/method.Client.ClientCore.StopKeylogger.c`](code/method.Client.ClientCore.StopKeylogger.c)
- [`code/method.Client.ClientCore.StopWindowMonitor.c`](code/method.Client.ClientCore.StopWindowMonitor.c)
- [`code/method.Client.ClientCore.TempBlockPoll.c`](code/method.Client.ClientCore.TempBlockPoll.c)
- [`code/method.Client.MouseHook.Unhook.c`](code/method.Client.MouseHook.Unhook.c)
- [`code/method.Shared.Packets.BackupServerItem.OnDeserialized.c`](code/method.Shared.Packets.BackupServerItem.OnDeserialized.c)
- [`code/method.Shared.S..cctor.c`](code/method.Shared.S..cctor.c)
- [`code/method.__c__DisplayClass180_1..ctor.c`](code/method.__c__DisplayClass180_1..ctor.c)
- [`code/method.__c__DisplayClass250_0..ctor.c`](code/method.__c__DisplayClass250_0..ctor.c)
- [`code/method.__c__DisplayClass292_2..ctor.c`](code/method.__c__DisplayClass292_2..ctor.c)
- [`code/method.__c__DisplayClass292_3..ctor.c`](code/method.__c__DisplayClass292_3..ctor.c)
- [`code/method.__c__DisplayClass357_1..ctor.c`](code/method.__c__DisplayClass357_1..ctor.c)
- [`code/method.__c__DisplayClass369_0._ShowValidationMessage_b__0.c`](code/method.__c__DisplayClass369_0._ShowValidationMessage_b__0.c)
- [`code/method.__c__DisplayClass49_0._GetAllChildWindows_b__0.c`](code/method.__c__DisplayClass49_0._GetAllChildWindows_b__0.c)
- [`code/sym.__c..ctor.c`](code/sym.__c..ctor.c)

## Behavioral Analysis

Based on the provided disassembly and string definitions, here is an analysis of the binary sample:

### Core Functionality and Purpose
The binary appears to be a **spyware/trojan** designed for information theft and surveillance. It targets user interactions by monitoring inputs (keyboard and mouse) and system environment details, likely transmitting this data to a remote server. The presence of heavy obfuscation suggests it is intended to evade both automated security scanners and manual analysis.

### Suspicious or Malicious Behaviors
*   **Keylogging:** The code contains explicit references to `StartKeylogger` and `StopKeylogger`. This confirms the malware's intent to capture every keystroke made by the user (passwords, messages, etc.).
*   **Input Hooking:** The function `method.Client.MouseHook.Hook` indicates the use of Windows hooks to intercept mouse movements or clicks. This is a common technique in spyware to track user activity even when standard input methods are bypassed.
*   **Clipboard Monitoring:** The inclusion of `StopClipboardMonitor` suggests that the malware monitors the system clipboard, likely to steal passwords or sensitive text copied by the user (e.g., from a password manager).
*   **Information Exfiltration:** 
    *   The function `SendMachineDiagLog` indicates it collects and sends "diagnostic" logs—typically containing OS version, hardware specs, and IP addresses—to an external server.
    *   The string `System.Net.WebClient` suggests the use of this class for direct communication with a remote URL to upload stolen data or download additional components.
*   **Environment Reconnaissance:** The functions `CheckBrowserWindows` and `StopWindowMonitor` suggest the malware monitors which applications are in focus, potentially to identify when a user is on a sensitive website (like a bank) to trigger specific actions.

### Notable Techniques and Patterns
*   **Heavy Obfuscation/Anti-Analysis:** 
    *   The decompiler produced numerous "Control flow encountered bad instruction data" warnings and `halt_baddata()` calls. This is a classic sign of **Control Flow Flattening** or the use of junk code/opaque predicates designed to break decompilers like Hex-Rays or Ghidra. 
    *   This makes it significantly harder for an analyst to follow the logical "if/then" flow of the malware's logic during manual review.
*   **Reflection and Dynamic Loading:** The inclusion of `System.Reflection`, `Assembly`, and `GetExecutingAssembly` suggests the code may dynamically load additional modules or decrypt its own functionality in memory to hide its full capabilities from static analysis.
*   **Standard Library Abuse (Packing):** The presence of `System.Runtime.Serialization.Formatters.Binary` and `BinaryFormatter` is a red flag. While common in .NET, these are frequently used by malware to deserialize complex objects or "unpack" hidden payloads into memory.
*   **.NET Framework Wrapper:** The string list confirms this is a .NET-based application (likely wrapped in a native stub). This allows the author to use high-level libraries for easy networking and system manipulation while using standard encryption (like `SHA256Managed`) to secure their communications with an attacker's C&C server.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1056.001 | Keylogging | The presence of `StartKeylogger` and `StopKeylogger` functions confirms the intent to capture user keystrokes for information theft. |
| T1056 | Input Capture | Mouse hooking and clipboard monitoring are utilized to intercept user interactions and steal sensitive data like passwords or copied text. |
| T1615 | System Environment Information | The collection of "diagnostic logs" (OS version, hardware specs) is used to gather reconnaissance on the target system's environment. |
| T1110 | Exfiltration Over Web Service | The use of `System.Net.WebClient` indicates that stolen data and telemetry are being exfiltrated via web protocols. |
| T1027 | Obfuscated Files or Information | The use of control flow flattening, junk code, and opaque predicates is intended to hinder both automated and manual analysis. |
| T1106 | Dynamic Resolution | The use of `System.Reflection` allows the malware to resolve and load components at runtime to hide its full functionality from static analysis. |
| T1029 | Packing | The presence of `BinaryFormatter` and specific serialization libraries suggests the malware is packed or uses a layered execution model to hide payloads. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The provided text contains a descriptive analysis of malware capabilities but does not include specific hardcoded infrastructure (like actual IP addresses or URLs) or unique file system paths.

### **IP addresses / URLs / Domains**
*   *None detected.* (The text mentions the use of `System.Net.WebClient` to communicate with remote servers, but no specific domains or IP addresses are listed.)

### **File paths / Registry keys**
*   *None detected.* (While `Microsoft.Win32` and `RegistryKey` were identified in the strings, these refer to standard .NET library components; no specific malicious registry keys were identified.)

### **Mutex names / Named pipes**
*   *None detected.*

### **Hashes**
*   *None detected.* (The string `SHA256Managed` refers to a cryptographic algorithm class in the .NET library, not a specific file hash.)

### **Other artifacts**
*   **Framework/Environment:** .NET Framework 4.0 (identified by version string `v4.0.30319`).
*   **Communication Patterns:** Usage of `System.Net.WebClient` for exfiltrating "MachineDiagLog" and potential secondary payload downloading.
*   **Serialization/Packing Indicator:** Use of `System.Runtime.Serialization.Formatters.Binary` and `BinaryFormatter`, often used in .NET malware to de-serialize data or unpack payloads into memory.
*   **Behavioral Identifiers (TTPs):** 
    *   Keylogging functionality (`StartKeylogger`, `StopKeylogger`).
    *   Input hooking for mouse tracking (`MouseHook.Hook`).
    *   Clipboard monitoring (`StopClipboardMonitor`).
    *   Context-aware surveillance (`CheckBrowserWindows`) to identify sensitive activities (e.g., banking).

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: RAT (Remote Access Trojan) / Infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Spyware/Surveillance Capabilities:** The presence of `StartKeylogger`, `MouseHook.Hook`, and `StopClipboardMonitor` confirms the sample is designed to intercept sensitive user input (passwords, personal messages, and copied data).
    *   **Data Exfiltration & Reconnaissance:** The use of `SendMachineDiagLog` and `System.Net.WebClient` indicates a structured method for gathering system information and exfiltrating stolen data to a remote server via web protocols.
    *   **Advanced Evasion Techniques:** The sample utilizes common .NET-based evasion tactics, including **Control Flow Flattening**, the use of `Reflection` for dynamic loading, and `BinaryFormatter` for potentially unpacking secondary payloads in memory.
