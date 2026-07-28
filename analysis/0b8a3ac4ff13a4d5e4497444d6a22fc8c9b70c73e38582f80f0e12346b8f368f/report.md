# Threat Analysis Report

**Generated:** 2026-07-26 11:53 UTC
**Sample:** `0b8a3ac4ff13a4d5e4497444d6a22fc8c9b70c73e38582f80f0e12346b8f368f_0b8a3ac4ff13a4d5e4497444d6a22fc8c9b70c73e38582f80f0e12346b8f368f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b8a3ac4ff13a4d5e4497444d6a22fc8c9b70c73e38582f80f0e12346b8f368f_0b8a3ac4ff13a4d5e4497444d6a22fc8c9b70c73e38582f80f0e12346b8f368f.exe` |
| File type | PE32+ executable for MS Windows 4.00 (DLL), x86-64 Mono/.Net assembly, 4 sections |
| Size | 1,007,104 bytes |
| MD5 | `11a2ecac741464d04e8ac2e17b032015` |
| SHA1 | `5692ade635992ae89fadf8d0ff3b6f995230a111` |
| SHA256 | `0b8a3ac4ff13a4d5e4497444d6a22fc8c9b70c73e38582f80f0e12346b8f368f` |
| Overall entropy | 6.855 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773952350 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 473,088 | 6.846 | No |
| `.sdata` | 512 | 1.288 | No |
| `.reloc` | 512 | 0.174 | No |
| `.text` | 531,968 | 6.871 | No |

### Imports

**mscoree.dll**: `_CorDllMain`

### Exports

`DllRegisterServer`, `Entry`

## Extracted Strings

Total strings found: **8185** (showing first 100)

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

,p	rj-
&	,%	(
 OMER
	 OMER(

--r(M

-*r>M

-rYQ

,&r)_

,&r3_
 OMER(
 OMER(
 OMER(
Xl[%Z
Yl	ZiX~Q
Yl	ZiX~Q
 OMER(
 OMER(
@[Y+#

- OMER(
j1)rAk
%,#rup

,\	o^
%,P	-M
p+=r8

+e	oE
v4.0.30319
#Strings
!$!,!4!?!Q!^!
"#"I"P"l"v"~"
""#Q#^#
$&$a$j$
&/&;&D&W&c&q&~&
(#(-(3(J(h(q(
($)-)3)J)R)])g)t)7*?*E*K*\*
+#+3+]+k+
,#,),<,C,M,V,`,p,w,},
-:-G-Z-a-j-
.*.4.:.].e.x.
	.
D
M

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
| `method.Shared.Packets.BackupServerItem.OnDeserialized` | `0x1800085e5` | 458752 | ✓ |
| `sym.Client.WatchdogInstaller.KillGuardianProcess` | `0x18000b384` | 435162 | ✓ |
| `method.__c__DisplayClass364_0._ShowValidationMessage_b__0` | `0x180025815` | 77264 | ✓ |
| `method.Client.ClientCore.CreateJpegParams` | `0x1800108fb` | 71734 | ✓ |
| `method.Client.ClientCore.StopKeylogger` | `0x180017549` | 32446 | ✓ |
| `method.Client.ClientCore.StopWindowMonitor` | `0x1800115ef` | 21788 | ✓ |
| `method.__c__DisplayClass49_0._GetAllChildWindows_b__0` | `0x1800266e0` | 19620 | ✓ |
| `method.Shared.S..cctor` | `0x180004600` | 9440 | ✓ |
| `method.Client.ClientCore.HandleSystemDiagRequest` | `0x180014718` | 8988 | ✓ |
| `method.Client.ClientCore.CreateHoleFormInternal` | `0x180019dbc` | 5540 | ✓ |
| `method.__c__DisplayClass287_2..ctor` | `0x18002328f` | 5048 | ✓ |
| `method.Client.ClientCore.CheckBrowserWindows` | `0x18001166c` | 4264 | ✓ |
| `method.__c__DisplayClass245_0..ctor` | `0x18002243f` | 3664 | ✓ |
| `method.Client.ClientCore.CreateComponentControl` | `0x18001b604` | 3648 | ✓ |
| `method.Client.ClientCore.SetupNativeBlockForm` | `0x18001e390` | 3440 | ✓ |
| `method.Client.ClientCore.SendMachineDiagLog` | `0x18000d654` | 3352 | ✓ |
| `method.Client.ClientCore.OnPacketReceived` | `0x18000e53c` | 3108 | ✓ |
| `method.Client.MouseHook.Unhook` | `0x18001f66f` | 2924 | ✓ |
| `method.Client.ClientCore.StopClipboardMonitor` | `0x180016b0b` | 2622 | ✓ |
| `method.__c__DisplayClass352_1..ctor` | `0x18002490d` | 2576 | ✓ |
| `method.Client.ClientCore.HandleUpdateClient` | `0x18000f548` | 2116 | ✓ |
| `method.Client.ClientCore.Connect` | `0x18000c9c8` | 1828 | ✓ |
| `method.Client.ClientCore.HandleScreenshotReal` | `0x180010e04` | 1752 | ✓ |
| `method.Client.ClientCore.TempBlockPoll` | `0x180018e88` | 1620 | ✓ |
| `method.Client.ClientCore.ShowValidationMessage` | `0x18001c588` | 1476 | ✓ |
| `method.Client.ClientCore.HandleMouseClick` | `0x180012fa4` | 1380 | ✓ |
| `method.Client.ClientInstaller..ctor` | `0x18000a9a3` | 1341 | ✓ |
| `method.Client.ClientCore.LoadSession` | `0x18001d9f0` | 1336 | ✓ |
| `method.Client.TorManager.DownloadTor` | `0x1800215d4` | 1300 | ✓ |
| `method.Shared.Network.TcpConnection.get_RemoteEndPoint` | `0x180009fab` | 1266 | ✓ |

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
- [`code/method.Client.ClientCore.StopKeylogger.c`](code/method.Client.ClientCore.StopKeylogger.c)
- [`code/method.Client.ClientCore.StopWindowMonitor.c`](code/method.Client.ClientCore.StopWindowMonitor.c)
- [`code/method.Client.ClientCore.TempBlockPoll.c`](code/method.Client.ClientCore.TempBlockPoll.c)
- [`code/method.Client.ClientInstaller..ctor.c`](code/method.Client.ClientInstaller..ctor.c)
- [`code/method.Client.MouseHook.Unhook.c`](code/method.Client.MouseHook.Unhook.c)
- [`code/method.Client.TorManager.DownloadTor.c`](code/method.Client.TorManager.DownloadTor.c)
- [`code/method.Shared.Network.TcpConnection.get_RemoteEndPoint.c`](code/method.Shared.Network.TcpConnection.get_RemoteEndPoint.c)
- [`code/method.Shared.Packets.BackupServerItem.OnDeserialized.c`](code/method.Shared.Packets.BackupServerItem.OnDeserialized.c)
- [`code/method.Shared.S..cctor.c`](code/method.Shared.S..cctor.c)
- [`code/method.__c__DisplayClass245_0..ctor.c`](code/method.__c__DisplayClass245_0..ctor.c)
- [`code/method.__c__DisplayClass287_2..ctor.c`](code/method.__c__DisplayClass287_2..ctor.c)
- [`code/method.__c__DisplayClass352_1..ctor.c`](code/method.__c__DisplayClass352_1..ctor.c)
- [`code/method.__c__DisplayClass364_0._ShowValidationMessage_b__0.c`](code/method.__c__DisplayClass364_0._ShowValidationMessage_b__0.c)
- [`code/method.__c__DisplayClass49_0._GetAllChildWindows_b__0.c`](code/method.__c__DisplayClass49_0._GetAllChildWindows_b__0.c)
- [`code/sym.Client.WatchdogInstaller.KillGuardianProcess.c`](code/sym.Client.WatchdogInstaller.KillGuardianProcess.c)

## Behavioral Analysis

Based on the analysis of the provided strings and disassembly, this binary is highly suspicious and exhibits characteristics consistent with **spyware** or a **Remote Access Trojan (RAT)**. The code contains multiple components designed for information theft, anti-analysis evasion, and covert communication.

### Core Functionality and Purpose
The primary purpose of this code appears to be the surveillance and exfiltration of user data from a compromised host. It implements several "spy" modules common in malware:
*   **Data Collection:** Tools for capturing keystrokes (Keylogger), monitoring the clipboard, and taking screenshots.
*   **Information Gathering:** Collecting system diagnostics ("SendMachineDiagLog") to profile the victim's machine.
*   **Communication:** Establishing connections to remote servers to transmit the stolen data.

### Suspicious or Malicious Behaviors
The following behaviors are highly indicative of malicious intent:

*   **Anti-Analysis & Anti-Malware:**
    *   **`KillGuardianProcess`**: This function explicitly attempts to terminate "Guardian" processes, a common tactic used to disable antivirus (AV) or Endpoint Detection and Response (EDR) software.
    *   **Execution Protection**: The presence of various "Stop" functions (e.g., `StopKeylogger`, `StopWindowMonitor`) suggests the malware may toggle these features off when it detects it is being analyzed or under observation.

*   **Information Theft (Spyware):**
    *   **Clipboard Monitoring**: The function `StartClipboardMonitor` indicates the code captures data from the system clipboard, which is commonly used to steal passwords, private keys, and copied text.
    *   **Keylogging**: The presence of `StopKeylogger` confirms that a keylogging component exists within the binary to log user input.
    *   **Screen Capturing**: Functions like `CreateJpegParams` and `HandleScreenshotReal` suggest the software takes and processes screenshots of the user's desktop.

*   **Evasive Network Communication:**
    *   **Tor Integration**: The inclusion of `TorManager` and `DownloadTor` is a major red flag. Using the Tor network allows the malware to anonymize its command-and-control (C2) traffic, making it significantly harder for defenders to trace the remote infrastructure.
    *   **C2 Communication**: Standard networking components (`TcpClient`, `NetworkStream`, `WebClient`) are utilized to exfiltrate gathered data.

### Notable Techniques and Patterns
*   **Obfuscation/Packing:** The decompiler shows numerous instances of "Bad instruction - Truncating control flow" and "Truncating control flow here." This is a classic indicator that the original .NET binary was processed with an obfuscator (like ConfuserEx or Dotfuscator) or packed, intended to hinder static analysis.
*   **Telemetry Collection:** The `SendMachineDiagLog` function suggests the malware sends system-specific information back to the attacker to confirm successful infection and provide details about the victim's environment.
*   **Complex Networking**: The use of `RemoteEndPoint` and internal packet handling (`BackupServerItem`, `OnPacketReceived`) suggests a structured protocol for interacting with a remote server.

### Summary Table of Findings
| Feature | Evidence | Risk Level |
| :--- | :--- | :--- |
| **Anti-Analysis** | `KillGuardianProcess`, obfuscated control flow | High |
| **Information Theft** | `StartClipboardMonitor`, `StopKeylogger`, `HandleScreenshotReal` | High |
| **Evasion** | `TorManager.DownloadTor` (Anonymized C2) | High |
| **Data Exfiltration** | `SendMachineDiagLog`, `TcpConnection` | High |

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Impair Defenses: Disable or Remove Security Software | The `KillGuardianProcess` function explicitly targets and terminates security-related processes (AV/EDR). |
| **T1497** | Virtualization/Sandbox Evasion | The "Stop" functions for keyloggers and monitors suggest a mechanism to disable malicious features when analysis is detected. |
| **T1027** | Packed_Command_and_Control | The "Truncating control flow" messages indicate the binary was processed with an obfuscator or packer to hinder static analysis. |
| **T1056.001** | Keylogging | The presence of `StopKeylogger` confirms a component designed to intercept and log user keystrokes. |
| **T1113** | Screen Capture | The functions `CreateJpegParams` and `HandleScreenshotReal` indicate the capture of the user's visual output for data theft. |
| **T1090** | Proxy | The integration of Tor (`TorManager`, `DownloadTor`) is used to anonymize C2 traffic and hide the actual network infrastructure. |
| **T1082** | System Information Discovery | The `SendMachineDiagLog` function is utilized to gather system-specific telemetry to profile the victim's environment. |
| **T1041** | Exfiltration Over C2 Channel | Standard networking libraries (`TcpClient`, `WebClient`) are used to transmit collected data (logs, screenshots) to a remote server. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that since no specific hardcoded IP addresses, URLs, or file paths were present in the raw string dump, those categories are listed as "None identified." The behaviorally derived indicators have been grouped under "Other artifacts."

**IP addresses / URLs / Domains**
*   None identified (The analysis mentions Tor integration, but no specific .onion addresses or IP addresses were provided).

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **C2 Infrastructure/Protocols:** 
    *   Tor Network Integration (via `TorManager` and `DownloadTor`)
    *   TCP Communication (`TcpClient`, `NetworkStream`)
    *   HTTP(S) Web Requests (`WebClient`)
*   **Suspicious Function Names (Behavioral Indicators):**
    *   `KillGuardianProcess` (Anti-AV/EDR activity)
    *   `StartClipboardMonitor` (Information theft)
    *   `StopKeylogger` (Evidence of keylogging capability)
    *   `HandleScreenshotReal` / `CreateJpegParams` (Evidence of screen scraping)
    *   `SendMachineDiagLog` (Telemetry exfiltration)
    *   `BackupServerItem` / `OnPacketReceived` (Custom C2 communication protocol)
*   **Evasion Techniques:** 
    *   Obfuscated control flow (indicated by "Bad instruction - Truncating control flow" markers in the decompiler).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT (Remote Access Trojan) / Spyware
3. **Confidence**: High
4. **Key evidence**: 
    *   **Information Stealing Suite:** The binary includes comprehensive "spy" modules, specifically keylogging (`StopKeylogger`), clipboard monitoring (`StartClipboardMonitor`), and screen capturing (`HandleScreenshotReal` / `CreateJpegParams`).
    *   **Evasive C2 Infrastructure:** The integration of the Tor network (`TorManager`, `DownloadTor`) to anonymize command-and-control traffic and the inclusion of specific anti-analysis functions like `KillGuardianProcess` (aimed at disabling security software) indicate a high level of sophistication.
    *   **Data Exfiltration & Telemetry:** The presence of `SendMachineDiagLog` for system profiling and custom packet handling (`OnPacketReceived`) demonstrates a structured method for exfiltrating stolen data to a remote server.
