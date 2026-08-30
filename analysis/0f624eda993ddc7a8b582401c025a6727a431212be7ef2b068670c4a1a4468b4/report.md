# Threat Analysis Report

**Generated:** 2026-08-16 06:46 UTC
**Sample:** `0f624eda993ddc7a8b582401c025a6727a431212be7ef2b068670c4a1a4468b4_0f624eda993ddc7a8b582401c025a6727a431212be7ef2b068670c4a1a4468b4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f624eda993ddc7a8b582401c025a6727a431212be7ef2b068670c4a1a4468b4_0f624eda993ddc7a8b582401c025a6727a431212be7ef2b068670c4a1a4468b4.exe` |
| File type | PE32+ executable for MS Windows 4.00 (DLL), x86-64 Mono/.Net assembly, 4 sections |
| Size | 961,536 bytes |
| MD5 | `0d4d655fd0cc6f15b69ad3698ffe3319` |
| SHA1 | `6e78b809e73ead296dd29fc8f4662a1d6b99501e` |
| SHA256 | `0f624eda993ddc7a8b582401c025a6727a431212be7ef2b068670c4a1a4468b4` |
| Overall entropy | 6.838 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773592622 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 440,320 | 6.795 | No |
| `.sdata` | 512 | 1.267 | No |
| `.reloc` | 512 | 0.17 | No |
| `.text` | 519,168 | 6.882 | No |

### Imports

**mscoree.dll**: `_CorDllMain`

### Exports

`DllRegisterServer`, `Entry`

## Extracted Strings

Total strings found: **7951** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.sdata
.reloc
B.text
XZ!R5G&
;Q}ATG|
+D'DAA$
eUnL.qk
oWnFK(
JB>V=a*
yW+K6K?
rz+DV#g
Gg
`'p
|t<Jr$
|A+WOk%
rB:JAA$
] (L=
eV!O
hS+KL.
2N%a"K
[!K1M'
eV"@AK8
F!KOk%
bS"V=v$
d\=JGv
XZ!R5G&
y]"fK.
ys>LAD$
p+tre
p+lry

%-&(M
p+*r[

,p	r-'
&	,%	(
p+r11
 OMER
	 OMER(

, rPJ
 OMER(
 OMER(
 OMER(
Xl[%Z
Yl	ZiX~8
Yl	ZiX~8
 OMER(
 OMER(
@[Y+#

- OMER(

,r``

,6r}i

	rR^

,\	o^
%,P	-M
p+=r:

+e	o@
v4.0.30319
#Strings
 & . 6 A S ` 
!&!L!S!o!y!
!%"T"\"k"
#&#=#F#]#
$3$E$Q$Z$m$y$
&#&)&@&^&g&
'#')'@'H'S']'j'-(5(;(A(R(
)')M)R)`)
*0*7*A*J*T*d*k*q*v*}*
+)+6+I+P+Y+o+y+
,#,),L,T,g,o,u,~,
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Shared.Packets.BackupServerItem.OnDeserialized` | `0x180008575` | 957068 | ✓ |
| `sym.Client.WatchdogInstaller.KillGuardianProcess` | `0x18000b10c` | 402690 | ✓ |
| `method.__c__DisplayClass351_0._ShowValidationMessage_b__0` | `0x18002353d` | 86072 | ✓ |
| `method.Client.ClientCore.StopKeylogger` | `0x1800154a9` | 32202 | ✓ |
| `method.__c__DisplayClass49_0._GetAllChildWindows_b__0` | `0x180024408` | 27908 | ✓ |
| `method.Client.ClientCore.StopWindowMonitor` | `0x18000febb` | 19376 | ✓ |
| `method.Shared.S..cctor` | `0x1800045dc` | 9392 | ✓ |
| `method.Client.ClientCore.HandleSystemDiagRequest` | `0x180012b64` | 7728 | ✓ |
| `method.__c__DisplayClass168_1..ctor` | `0x18001e679` | 6400 | ✓ |
| `method.Client.ClientCore.CreateHoleFormInternal` | `0x180017d10` | 5540 | ✓ |
| `method.__c__DisplayClass274_2..ctor` | `0x180020fb7` | 5048 | ✓ |
| `method.__c__DisplayClass232_0..ctor` | `0x180020167` | 3664 | ✓ |
| `method.Client.ClientCore.CreateComponentControl` | `0x180019558` | 3648 | ✓ |
| `method.Client.ClientCore.SetupNativeBlockForm` | `0x18001c204` | 3440 | ✓ |
| `method.Client.ClientCore.CreateJpegParams` | `0x18000f1c7` | 3268 | ✓ |
| `method.Client.ClientCore.CheckBrowserWindows` | `0x18000ff38` | 3112 | ✓ |
| `method.Client.ClientCore.OnPacketReceived` | `0x18000d534` | 2972 | ✓ |
| `method.Client.MouseHook.Unhook` | `0x18001d4db` | 2924 | ✓ |
| `method.Client.ClientCore.StopClipboardMonitor` | `0x180014a6b` | 2622 | ✓ |
| `method.__c__DisplayClass339_1..ctor` | `0x180022635` | 2576 | ✓ |
| `method.Client.ClientCore.HandleUpdateClient` | `0x18000e484` | 2116 | ✓ |
| `method.Shared.Network.TcpConnection.get_RemoteEndPoint` | `0x180009e6b` | 1917 | ✓ |
| `method.Client.ClientCore.Connect` | `0x18000c73c` | 1780 | ✓ |
| `method.Client.ClientCore.HandleScreenshotReal` | `0x18000f6d0` | 1752 | ✓ |
| `method.Client.ClientCore.TempBlockPoll` | `0x180016ddc` | 1620 | ✓ |
| `method.Client.ClientCore.ShowValidationMessage` | `0x18001a4dc` | 1476 | ✓ |
| `method.Client.ClientCore.HandleMouseClick` | `0x1800113f0` | 1380 | ✓ |
| `method.Client.ClientInstaller..ctor` | `0x18000a72b` | 1341 | ✓ |
| `method.Client.TorManager.DownloadTor` | `0x18001f37c` | 1300 | ✓ |
| `method.__c__DisplayClass274_2._ShowBlockScreenWithHtml_b__3` | `0x180020fc0` | 1236 | ✓ |

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
- [`code/method.Client.ClientCore.OnPacketReceived.c`](code/method.Client.ClientCore.OnPacketReceived.c)
- [`code/method.Client.ClientCore.SetupNativeBlockForm.c`](code/method.Client.ClientCore.SetupNativeBlockForm.c)
- [`code/method.Client.ClientCore.ShowValidationMessage.c`](code/method.Client.ClientCore.ShowValidationMessage.c)
- [`code/method.Client.ClientCore.StopClipboardMonitor.c`](code/method.Client.ClientCore.StopClipboardMonitor.c)
- [`code/method.Client.ClientCore.StopKeylogger.c`](code/method.Client.ClientCore.StopKeylogger.c)
- [`code/method.Client.ClientCore.StopWindowMonitor.c`](code/method.Client.ClientCore.StopWindowMonitor.c)
- [`code/method.Client.ClientCore.TempBlockPoll.c`](code/method.Client.ClientCore.TempBlockPoll.c)
- [`code/method.Client.ClientInstaller..ctor.c`](code/method.Client.ClientInstaller..ctor.c)
- [`code/method.Client.MouseHook.Unhook.c`](code/method.Client.MouseHook.Unhook.c)
- [`code/method.Client.TorManager.DownloadTor.c`](code/method.Client.TorManager.DownloadTor.c)
- [`code/method.Shared.Network.TcpConnection.get_RemoteEndPoint.c`](code/method.Shared.Network.TcpConnection.get_RemoteEndPoint.c)
- [`code/method.Shared.Packets.BackupServerItem.OnDeserialized.c`](code/method.Shared.Packets.BackupServerItem.OnDeserialized.c)
- [`code/method.Shared.S..cctor.c`](code/method.Shared.S..cctor.c)
- [`code/method.__c__DisplayClass168_1..ctor.c`](code/method.__c__DisplayClass168_1..ctor.c)
- [`code/method.__c__DisplayClass232_0..ctor.c`](code/method.__c__DisplayClass232_0..ctor.c)
- [`code/method.__c__DisplayClass274_2..ctor.c`](code/method.__c__DisplayClass274_2..ctor.c)
- [`code/method.__c__DisplayClass274_2._ShowBlockScreenWithHtml_b__3.c`](code/method.__c__DisplayClass274_2._ShowBlockScreenWithHtml_b__3.c)
- [`code/method.__c__DisplayClass339_1..ctor.c`](code/method.__c__DisplayClass339_1..ctor.c)
- [`code/method.__c__DisplayClass351_0._ShowValidationMessage_b__0.c`](code/method.__c__DisplayClass351_0._ShowValidationMessage_b__0.c)
- [`code/method.__c__DisplayClass49_0._GetAllChildWindows_b__0.c`](code/method.__c__DisplayClass49_0._GetAllChildWindows_b__0.c)
- [`code/sym.Client.WatchdogInstaller.KillGuardianProcess.c`](code/sym.Client.WatchdogInstaller.KillGuardianProcess.c)

## Behavioral Analysis

Based on the analysis of the provided strings and decompiled code, this binary is highly indicative of a **malware sample**, likely a Trojan or an Information Stealer with significant anti-analysis features.

### Core Functionality
The program appears to be a sophisticated piece of malware designed for remote access (RAT), information theft, and evasion. The presence of .NET libraries (`System.*`) suggests it is a managed binary that has been heavily obfuscated/packed to hide its true behavior from security researchers.

### Suspicious or Malicious Behaviors
The following behaviors were identified in the code:

*   **Anti-Malware & Defense Evasion:**
    *   **`KillGuardianProcess`**: The inclusion of a "Watchdog" that specifically targets and attempts to terminate processes labeled as "Guardian" strongly suggests an attempt to disable antivirus or other security software.
    *   **Obfuscation/Packing**: A significant amount of the decompiled code resulted in `halt_baddata()` and "bad instruction data." This indicates the binary uses advanced obfuscation techniques (such as junk code, metamorphic code, or a custom packer) to hinder manual analysis.

*   **Spyware & Information Stealing:**
    *   **Keylogging**: The function `StopKeylogger` explicitly confirms that a keylogging component is present within the codebase. 
    *   **Clipboard Monitoring**: The `StartClipboardMonitor` routine suggests it monitors the user's clipboard, likely to steal passwords or copied sensitive data.
    *   **Screen Scraping/Capture**: Functions such as `HandleScreenshotReal` and `CreateJpegParams` indicate that the malware captures images of the screen (potentially used to bypass security by "reading" text from a screenshot).
    *   **Window Monitoring**: The presence of `StopWindowMonitor` and `_FindWindowBehindBlock` suggests it monitors user interaction with windows, possibly to detect if a user is trying to access security settings or a specific application.

*   **Anonymized Network Communication:**
    *   **Tor Integration**: The presence of `TorManager.DownloadTor` indicates the malware can utilize the Tor network for its Command and Control (C2) communication, allowing it to route traffic through multiple nodes to hide the location of its home server.
    *   **Direct Sockets**: Use of `TcpClient` and `NetworkStream` suggests standard backdoor capabilities to receive commands from a remote operator.

### Notable Techniques & Patterns
*   **Malware Components:** The code is structured into "Modules" (e.g., `ClientCore`, `TorManager`, `MouseHook`), which is typical of modular malware where different features (logging, networking, evasion) are bundled together.
*   **Information Gathering:** Inclusion of `Get-SystemInfo` style behaviors (via the strings for `get_MachineName`, `get_UserName`, and `get_OSVersion`) indicates it gathers environmental data about the victim's machine upon infection.
*   **Data Serialization:** The use of `BinaryFormatter` is a common technique in older .NET malware to deserialize complex objects received from a remote server (e.g., executing instructions sent by an attacker).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in the provided analysis to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Disable or Remove Security Software | The `KillGuardianProcess` function specifically targets "Guardian" processes to disable local security defenses. |
| **T1027** | Obfuscated Files or Information | The presence of "bad instruction data" and evidence of packing indicate the use of obfuscation to hinder manual analysis. |
| **T1056.001** | Keylogging | The `StopKeylogger` function confirms a module specifically designed to capture user keystrokes. |
| **T1113** | Screen Capture | The `HandleScreenshotReal` and `CreateJpegParams` functions indicate the ability to capture images of the user's screen. |
| **T1572** | Protocol Tunneling | The integration of Tor suggests that the malware wraps its traffic in a tunnel to anonymize communication with C2 servers. |
| **T1071** | Application Layer Protocol | The use of `TcpClient` and `NetworkStream` indicates the use of standard network protocols for remote command execution. |
| **T1082** | System Compromise Information | Functions such as `get_MachineName`, `get_UserName`, and `get_OSVersion` are used to gather system environment details. |
| **T1570** | Data Encoding | The use of `BinaryFormatter` is a common technique for serializing/deserializing complex objects (instructions) from a remote source. |
| **T1113** | Screen Capture | While often used for images, this category covers the monitoring of screen content, which includes capturing clipboard data via visual observation. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because the provided data consists primarily of raw string dumps from an obfuscated .NET binary and a high-level behavioral summary, many technical indicators (like specific IP addresses or hardcoded file paths) are not present in this specific sample. However, several **behavioral IOCs** and **technical artifacts** were identified.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes the use of the Tor network for C2, but no specific onion addresses or IP addresses were provided).

### **File paths / Registry keys**
*   *None identified.* (No hardcoded file system paths or registry hive locations were found in the provided string dump).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **C2 Patterns:** 
    *   Utilization of `TorManager` to route traffic through the Tor network for anonymized C2 communication.
    *   Use of `TcpClient` and `NetworkStream` for direct socket communication with remote servers.
*   **Evasion & Defense Evasion:**
    *   Targeted termination of security software (Function: `KillGuardianProcess`).
    *   Heavy use of .NET obfuscation/packing techniques (indicated by "bad instruction data" in deconstruction).
*   **Spyware/Information Stealing Capabilities:**
    *   Keylogging functionality (`StopKeylogger`).
    *   Clipboard monitoring (`StartClipboardMonitor`) to harvest credentials.
    *   Screen scraping capabilities (`HandleScreenshotReal`, `CreateJpegParams`).
    *   Window tracking/monitoring (`_FindWindowBehindBlock`).
*   **Technical Frameworks:** 
    *   Target Environment: .NET Framework (version `4.0.30319` identified).
    *   Data Serialization: Use of `BinaryFormatter` (a common vector for deserialization attacks in malicious .NET applications).
    *   Information Gathering: Enumeration of machine name, username, and OS version.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT (Remote Access Trojan) / Infostealer
3. **Confidence**: High

4. **Key evidence**:
*   **Comprehensive Spyware Capabilities:** The inclusion of specific modules for keylogging (`StopKeylogger`), clipboard monitoring (`StartClipboardMonitor`), and screen scraping (`HandleScreenshotReal`) are primary indicators of a tool designed to exfiltrate sensitive user data and credentials.
*   **Sophisticated Evasion & C2 Tactics:** The binary utilizes dedicated functions to terminate security software (`KillGuardianProcess`), employs heavy obfuscation/packing, and integrates the Tor network (`TorManager`) to anonymize its communication with Command and Control (C2) servers.
*   **Modular Remote Management:** The use of `BinaryFormatter` for deserializing instructions from a remote server and the presence of various "Modules" suggest a multi-functional backend capable of receiving commands and executing unauthorized actions on the host machine.
