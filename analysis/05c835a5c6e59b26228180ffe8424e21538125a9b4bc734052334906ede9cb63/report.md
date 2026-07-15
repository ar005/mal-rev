# Threat Analysis Report

**Generated:** 2026-07-14 17:18 UTC
**Sample:** `05c835a5c6e59b26228180ffe8424e21538125a9b4bc734052334906ede9cb63_05c835a5c6e59b26228180ffe8424e21538125a9b4bc734052334906ede9cb63.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05c835a5c6e59b26228180ffe8424e21538125a9b4bc734052334906ede9cb63_05c835a5c6e59b26228180ffe8424e21538125a9b4bc734052334906ede9cb63.exe` |
| File type | PE32+ executable for MS Windows 4.00 (DLL), x86-64 Mono/.Net assembly, 4 sections |
| Size | 868,352 bytes |
| MD5 | `18c565dd69cb1057159403f13beb75f0` |
| SHA1 | `ab66f28925a01148e29db858c4bd6fd58276e08e` |
| SHA256 | `05c835a5c6e59b26228180ffe8424e21538125a9b4bc734052334906ede9cb63` |
| Overall entropy | 6.198 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774492686 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 361,472 | 6.069 | No |
| `.sdata` | 512 | 1.292 | No |
| `.reloc` | 512 | 0.179 | No |
| `.text` | 504,832 | 6.276 | No |

### Imports

**mscoree.dll**: `_CorDllMain`

### Exports

`DllRegisterServer`, `Entry`

## Extracted Strings

Total strings found: **7990** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.sdata
.reloc
B.text
p+trc
p+lrw

%-&(M
p+*rY

p+*ri'
%- &rk5
&	,%	(%
+3 OMER
 OMER
	 OMER(

,&r5e

,&rMe

,&r}e

	rev

-4	rsv

-'	r}v
 OMER(
 OMER(
 OMER(
Xl[%Z
Yl	ZiX~}
Yl	ZiX~}
 OMER(
 OMER(
@[Y+#

- OMER(

,\	oc
%,P	-M
p+=r8

+e	oG
v4.0.30319
#Strings
!(!3!H!g!y!
")"/"@"F"K"O"U"d"k"q"
#"$+$B$`$n$u$z$
&*&8&G&O&X&|&
(*(4(:(Q(o(x(
)+)4):)Q)Y)d)n){)>*F*L*R*c*
*+*+:+d+r+
,+,O,V,`,d,i,x,
-(-Q-|-
.-.9.S.\.j.v.
/ /*/0/d
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Shared.Packets.BackupServerItem.OnDeserialized` | `0x180008649` | 866744 | ✓ |
| `sym.__c..ctor` | `0x18000b2c0` | 323554 | ✓ |
| `method.Client.ClientCore.CreateJpegParams` | `0x18000fe1b` | 165934 | ✓ |
| `method.__c__DisplayClass369_0._ShowValidationMessage_b__0` | `0x180026685` | 38806 | ✓ |
| `method.Client.ClientCore.StopKeylogger` | `0x180017701` | 31696 | ✓ |
| `method.Client.ClientCore.StopWindowMonitor` | `0x180010b0f` | 25012 | ✓ |
| `method.__c__DisplayClass49_0._GetAllChildWindows_b__0` | `0x1800275dc` | 15588 | ✓ |
| `method.Client.ClientCore.HandleSystemDiagRequest` | `0x180013e08` | 11748 | ✓ |
| `method.Shared.S..cctor` | `0x180004618` | 9516 | ✓ |
| `method.__c__DisplayClass180_1..ctor` | `0x180021681` | 6240 | ✓ |
| `method.Client.ClientCore.CreateHoleFormInternal` | `0x180019f74` | 4940 | ✓ |
| `method.Client.ClientCore.CheckBrowserWindows` | `0x180010b8c` | 4264 | ✓ |
| `method.Client.ClientCore.OnPacketReceived` | `0x18000d538` | 3804 | ✓ |
| `method.__c__DisplayClass250_0..ctor` | `0x1800231ef` | 3664 | ✓ |
| `method.Client.ClientCore.CreateComponentControl` | `0x18001b7bc` | 3648 | ✓ |
| `method.Client.ClientCore.SetupNativeBlockForm` | `0x18001e4fc` | 3440 | ✓ |
| `method.Client.ClientCore.SendMachineDiagLog` | `0x18000c650` | 3352 | ✓ |
| `method.__c__DisplayClass292_3..ctor` | `0x180024833` | 3204 | ✓ |
| `method.Client.MouseHook.Unhook` | `0x18002041f` | 2924 | ✓ |
| `method.Client.ClientCore.HandleUpdateClient` | `0x18000e7fc` | 2736 | ✓ |
| `method.Client.ClientCore.StopClipboardMonitor` | `0x180016cc3` | 2622 | ✓ |
| `method.__c__DisplayClass357_1..ctor` | `0x18002577d` | 2576 | ✓ |
| `method.Client.ClientCore.StopDetectDevTools` | `0x18001f53d` | 2270 | ✓ |
| `method.__c__DisplayClass292_2..ctor` | `0x18002403f` | 2036 | ✓ |
| `method.Client.ClientCore.Connect` | `0x18000b9c4` | 1828 | ✓ |
| `method.Client.ClientCore.HandleScreenshotReal` | `0x180010324` | 1752 | ✓ |
| `method.Client.ClientCore.TempBlockPoll` | `0x180019040` | 1620 | ✓ |
| `method.Client.ClientCore.ShowValidationMessage` | `0x18001c740` | 1476 | ✓ |
| `method.Client.ClientCore.HandleMouseClick` | `0x1800124c4` | 1380 | ✓ |
| `method.Client.ClientCore.LoadSession` | `0x18001dba8` | 1336 | ✓ |

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

Based on the provided strings and disassembled code, here is an analysis of the binary sample.

### Core Functionality and Purpose
The sample appears to be a **spyware or information-stealer** component, likely part of a larger Trojan. While the decompilation results are heavily mangled by anti-analysis techniques, the naming conventions in the decompiler output and the included .NET libraries strongly suggest the following functions:

*   **Information Gathering:** The code contains logic for capturing user input (keylogging) and gathering system information ("MachineDiagLog").
*   **Surveillance:** It includes capabilities to capture screenshots (referenced by `CreateJpegParams` and `HandleScreenshotReal`).
*   **Command and Control (C2):** Based on the `System.Net` and `TcpClient` strings, the malware is designed to communicate over a network to exfiltrate stolen data or receive instructions.

### Suspicious or Malicious Behaviors
The following behaviors are highly indicative of malicious intent:

*   **Keylogging:** The functions `StartKeylogger` and `StopKeylogger` indicate the malware actively monitors and records user keystrokes, which is a primary method for stealing credentials (passwords, credit card numbers).
*   **Screen Capturing:** The references to "JpegParams" and "ScreenshotReal" suggest the ability to take images of the victim's desktop.
*   **Anti-Analysis/Evasion:**
    *   **DevTools Detection:** The function `StartDetectDevTools` suggests the malware checks for environments typical of security researchers or automated analysis sandboxes.
    *   **Window Monitoring:** Functions like `StopWindowMonitor` and `FindWindowBehindBlock` suggest it monitors active windows to determine what the user is doing or to identify specific targets (like banking websites).
*   **Data Exfiltration:** The inclusion of `SHA256Managed` suggests that captured data might be hashed or encrypted before being sent over the network to hide its content from network security monitors.

### Notable Techniques and Patterns
*   **Heavy Obfuscation/Packing:** The decompiler (r2ghidra) repeatedly flags "bad instruction" errors and "truncated control flow." This indicates the author has used **code packing or "junk code" insertion**. This is a common technique to break decompilers and disassemblers, making it difficult for analysts to see the true logic of the program.
*   **NET Framework Implementation:** The presence of `System.Reflection` and `System.Runtime.Serialization.Formatters.Binary` suggests the malware is written in .NET. These libraries are often used by malware to dynamically load code at runtime or unpack payloads into memory.
*   **Persistence/Configuration:** The `Microsoft.Win32.Registry` string indicates that the malware likely interacts with the Windows Registry to ensure it starts automatically upon system reboot or to store configuration data (like C2 server addresses).

### Summary of Findings
The sample is a sophisticated piece of spyware designed to **monitor user activity (keylogging and screen capturing), evade detection (anti-analysis/DevTools checks), and exfiltrate gathered information via network protocols.** The high level of obfuscation indicates an intent to remain hidden on the victim's machine for as long as possible.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1056.001** | Keylogging | The presence of `StartKeylogger` and `StopKeylogger` functions indicates the malware is designed to record user keystrokes for credential theft. |
| **T1113** | Screen Capture | References to "CreateJpegParams" and "HandleScreenshotReal" indicate capabilities to capture images of the victim's screen for surveillance. |
| **T1497** | Virtualization/Sandbox Detection | The `StartDetectDevTools` function is a common indicator used to detect if the malware is running in a researcher-controlled environment. |
| **T1027** | Obfuscated Files or Information | The use of "junk code," "bad instructions," and potential hashing via `SHA256Managed` are employed to hide malicious logic and exfiltrated data from analysis. |
| **T1112** | Modify Registry | Interaction with the `Microsoft.Win32.Registry` library is used to establish persistence or store configuration data such as C2 server addresses. |
| **T1071** | Application Layer Protocol | The utilization of `System.Net` and `TcpClient` indicates that the malware communicates over common network protocols for command and control (C2) activities. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted Indicators of Compromise (IOCs). 

*Note: The provided text contains many standard .NET library strings and internal function names rather than hardcoded infrastructure like IP addresses or URLs.*

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   **MachineDiagLog** (Identified as a component/file related to gathering system information).
*   *Note: While `Microsoft.Win32` was mentioned, no specific registry keys or file paths were extracted from the string dump.*

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified (The algorithm `SHA256Managed` was noted in the behavior analysis, but no specific file hashes were present in the strings).

### **Other artifacts**
*   **Malicious Function Names/Internal Logic:**
    *   `StartKeylogger` / `StopKeylogger` (Indicates keylogging capabilities)
    *   `CreateJpegParams` / `HandleScreenshotReal` (Indicates screen scraping/capture functionality)
    *   `StartDetectDevTools` (Anti-analysis/Evasion technique)
    *   `StopWindowMonitor` / `FindWindowBehindBlock` (Refers to window monitoring and target identification)
*   **C2 / Network Indicators:** 
    *   The use of `System.Net.Sockets.TcpClient` and `System.Net.WebClient` indicates the sample communicates over standard TCP/HTTP ports for data exfiltration or command reception.
*   **Technical Signatures:** 
    *   Reference to `.NET Framework v4.0.30319` (Identifying the execution environment).
    *   Presence of `System.Runtime.Serialization.Formatters.Binary` and `System.Reflection` (Commonly used for payload unpacking or dynamic code execution).

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1.  **Malware family**: custom
2.  **Malware type**: infostealer
3.  **Confidence**: High
4.  **Key evidence**:
    *   **Credential and Data Theft:** The presence of explicit functions for keylogging (`StartKeylogger`) and screen scraping (`HandleScreenshotReal`, `CreateJpegParams`) directly indicates its purpose is to capture sensitive user information.
    *   **Evasion and Stealth:** The use of "DevTools" detection, intentional "junk code" to break decompilers, and the use of `SHA256Managed` suggests a sophisticated intent to evade security researchers and hide exfiltrated data.
    *   **Command and Control (C2) Infrastructure:** The integration of `.NET` networking libraries (`TcpClient`, `WebClient`) and registry manipulation indicates a persistent capability to communicate with a remote server to transmit stolen data or receive commands.
