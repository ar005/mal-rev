# Threat Analysis Report

**Generated:** 2026-07-17 23:20 UTC
**Sample:** `07f56ac8b5bd7cdb4c33ea5e9cd42bc7f9d3cd5504aabbb476ef010a142d7e29_07f56ac8b5bd7cdb4c33ea5e9cd42bc7f9d3cd5504aabbb476ef010a142d7e29.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07f56ac8b5bd7cdb4c33ea5e9cd42bc7f9d3cd5504aabbb476ef010a142d7e29_07f56ac8b5bd7cdb4c33ea5e9cd42bc7f9d3cd5504aabbb476ef010a142d7e29.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 3,135,488 bytes |
| MD5 | `c8dbd37cd220b72548a1fdf919b4c71d` |
| SHA1 | `6336ee00c19db6765e07f0b5befc5d089a2e65c0` |
| SHA256 | `07f56ac8b5bd7cdb4c33ea5e9cd42bc7f9d3cd5504aabbb476ef010a142d7e29` |
| Overall entropy | 7.871 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1764970349 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,130,368 | 7.873 | ⚠️ Yes |
| `.rsrc` | 4,096 | 4.906 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **10737** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
%-&s8
&+  N

+
(Y
%-&se
+,8	(4
2#333333
2#ffffff

l[ ,

+_	og
.(+e(z


+ rB
#ffffff
#ffffff
#333333

+2	o

-S+nsH	

%	o0	
jY	n[	nZ*

-	o(
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
fSystem.Drawing.Icon, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3aBj
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Icon
IconData
IconSize
System.Drawing.Size
System.Drawing.Size
height
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
fSystem.Drawing.Icon, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
<?xml version="1.0" encoding="utf-8"?>
<configuration>
<startup><supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.8"/></startup></configuration>@
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Icon
IconData
IconSize
System.Drawing.Size
System.Drawing.Size
height
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
2&6A1A
.d&8@Ab
!Y]aJN
=QpUspys
hOm8C]s
j"$Bg
D"Gw

$Se"A8
U[_hP(f
LT>[*Y
+1.w75
6j)g')`U
;kC]u8
P@$4P=G
)cN(COE
RLC+(Ci
Gy(]br
m{-0_|
J4nSZ`
oH]>#$
O|u{`y
qR8O.v
EYS"a+
=6k	\
\?[B{7
;:(Zmu
aF6'd0o
b\qY/[
<RTE==x:
CHc?-3
~cYEEA
'Yz~["
7Z/\nt+
?9F9I
QKcF}o
>i|z9a
q(5Q[6
J)wDa+G
hL'b:	
-r)(hGh]k
XC)$0;
@RhIJBH
LQ+([7
l&n?w(
v uKG
OWQ-b>
gN<V}
bb86)b
@?r"W
;
gdjbjp
z$v0a3
JC+5qu[S
hV'Iqw
>Z*?W\
7gE^.(S
e+g697
rLDboL
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Orcus.Commands.FileExplorer.ZipUtilities.CreateArchive` | `0x424030` | 2316 | ✓ |
| `method.Orcus.Commands.RegistryExplorer.RegistryCommand.ProcessCommand` | `0x413a98` | 2180 | ✓ |
| `method.Orcus.Commands.Passwords.Utilities.SQLiteHandler.ReadMasterTable` | `0x41f3d4` | 2084 | ✓ |
| `method.Orcus.Commands.Passwords.Utilities.SQLiteHandler.ReadTableFromOffset` | `0x41fd40` | 1722 | ✓ |
| `method.Orcus.Connection.ServerConnection.ProcessResponse` | `0x40a314` | 1708 | ✓ |
| `method.Orcus.Plugins.PluginLoader.LoadPlugins` | `0x404a78` | 1544 | ✓ |
| `method.Orcus.Commands.TaskManager.TaskmanagerCommand.ProcessCommand` | `0x41217c` | 1412 | ✓ |
| `method.Orcus.Commands.WindowsCustomizer.WindowsCustomizerCommand.Initialize` | `0x40efd0` | 1377 | ✓ |
| `method.Orcus.Commands.ComputerInformation.InformationCollector.GetOperatingSystemInformation` | `0x41687c` | 1368 | ✓ |
| `method.Orcus.Commands.DropAndExecute.DropAndExecuteCommand.ProcessCommand` | `0x41c3ac` | 1352 | ✓ |
| `method.Orcus.Commands.FileExplorer.FileExplorerCommand..ctor` | `0x425bf0` | 1344 | ✓ |
| `method.__c._.ctor_b__13_10` | `0x427054` | 1336 | ✓ |
| `entry0` | `0x402068` | 1304 | ✓ |
| `method.Orcus.Connection.ServerConnection.EndRead` | `0x409dfc` | 1304 | ✓ |
| `method.Orcus.Commands.FunActions.FunActionsCommand.ProcessCommand` | `0x41586c` | 1264 | ✓ |
| `method.Orcus.Commands.Webcam.WebcamCommand.ProcessCommand` | `0x410720` | 1212 | ✓ |
| `method.Orcus.Commands.DeviceManager.DeviceManagerCommand.GetAllDevices` | `0x41d574` | 1056 | ✓ |
| `method.Orcus.Commands.ComputerInformation.InformationCollector.GetHardwareInformation` | `0x416ef8` | 1000 | ✓ |
| `method.Orcus.Connection.InformationCollector.SendInformation` | `0x408da4` | 976 | ✓ |
| `method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.ProcessCommand` | `0x41a768` | 964 | ✓ |
| `method.Orcus.StaticCommandManagement.ActiveCommandStopScheduler.ExecuteActiveCommand` | `0x405b98` | 928 | ✓ |
| `method.Orcus.CommandManagement.DatabaseConnection.PushRequests` | `0x42997c` | 900 | ✓ |
| `method.Orcus.Protection.Autostarter.AddToAutostart` | `0x4039fc` | 828 | ✓ |
| `method.Orcus.Commands.FileExplorer.ZipUtilities.ExtractArchive` | `0x423cf4` | 828 | ✓ |
| `method.Costura.AssemblyLoader..cctor` | `0x42a18c` | 813 | ✓ |
| `method.Orcus.Commands.Passwords.Applications.Mozilla.MozillaDecryptor.Initialize` | `0x422448` | 808 | ✓ |
| `method.Orcus.Utilities.WindowsDesktop.DesktopActions.MouseEvent` | `0x40db50` | 783 | ✓ |
| `method.Orcus.CommandManagement.CommandSelector..ctor` | `0x428bec` | 752 | ✓ |
| `method.Orcus.Commands.Passwords.Applications.Mozilla.Thunderbird.GetPasswords` | `0x422fe0` | 728 | ✓ |
| `method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.Streaming` | `0x41ab2c` | 724 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Costura.AssemblyLoader..cctor.c`](code/method.Costura.AssemblyLoader..cctor.c)
- [`code/method.Orcus.CommandManagement.CommandSelector..ctor.c`](code/method.Orcus.CommandManagement.CommandSelector..ctor.c)
- [`code/method.Orcus.CommandManagement.DatabaseConnection.PushRequests.c`](code/method.Orcus.CommandManagement.DatabaseConnection.PushRequests.c)
- [`code/method.Orcus.Commands.ComputerInformation.InformationCollector.GetHardwareInformation.c`](code/method.Orcus.Commands.ComputerInformation.InformationCollector.GetHardwareInformation.c)
- [`code/method.Orcus.Commands.ComputerInformation.InformationCollector.GetOperatingSystemInformation.c`](code/method.Orcus.Commands.ComputerInformation.InformationCollector.GetOperatingSystemInformation.c)
- [`code/method.Orcus.Commands.DeviceManager.DeviceManagerCommand.GetAllDevices.c`](code/method.Orcus.Commands.DeviceManager.DeviceManagerCommand.GetAllDevices.c)
- [`code/method.Orcus.Commands.DropAndExecute.DropAndExecuteCommand.ProcessCommand.c`](code/method.Orcus.Commands.DropAndExecute.DropAndExecuteCommand.ProcessCommand.c)
- [`code/method.Orcus.Commands.FileExplorer.FileExplorerCommand..ctor.c`](code/method.Orcus.Commands.FileExplorer.FileExplorerCommand..ctor.c)
- [`code/method.Orcus.Commands.FileExplorer.ZipUtilities.CreateArchive.c`](code/method.Orcus.Commands.FileExplorer.ZipUtilities.CreateArchive.c)
- [`code/method.Orcus.Commands.FileExplorer.ZipUtilities.ExtractArchive.c`](code/method.Orcus.Commands.FileExplorer.ZipUtilities.ExtractArchive.c)
- [`code/method.Orcus.Commands.FunActions.FunActionsCommand.ProcessCommand.c`](code/method.Orcus.Commands.FunActions.FunActionsCommand.ProcessCommand.c)
- [`code/method.Orcus.Commands.Passwords.Applications.Mozilla.MozillaDecryptor.Initialize.c`](code/method.Orcus.Commands.Passwords.Applications.Mozilla.MozillaDecryptor.Initialize.c)
- [`code/method.Orcus.Commands.Passwords.Applications.Mozilla.Thunderbird.GetPasswords.c`](code/method.Orcus.Commands.Passwords.Applications.Mozilla.Thunderbird.GetPasswords.c)
- [`code/method.Orcus.Commands.Passwords.Utilities.SQLiteHandler.ReadMasterTable.c`](code/method.Orcus.Commands.Passwords.Utilities.SQLiteHandler.ReadMasterTable.c)
- [`code/method.Orcus.Commands.Passwords.Utilities.SQLiteHandler.ReadTableFromOffset.c`](code/method.Orcus.Commands.Passwords.Utilities.SQLiteHandler.ReadTableFromOffset.c)
- [`code/method.Orcus.Commands.RegistryExplorer.RegistryCommand.ProcessCommand.c`](code/method.Orcus.Commands.RegistryExplorer.RegistryCommand.ProcessCommand.c)
- [`code/method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.ProcessCommand.c`](code/method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.ProcessCommand.c)
- [`code/method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.Streaming.c`](code/method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.Streaming.c)
- [`code/method.Orcus.Commands.TaskManager.TaskmanagerCommand.ProcessCommand.c`](code/method.Orcus.Commands.TaskManager.TaskmanagerCommand.ProcessCommand.c)
- [`code/method.Orcus.Commands.Webcam.WebcamCommand.ProcessCommand.c`](code/method.Orcus.Commands.Webcam.WebcamCommand.ProcessCommand.c)
- [`code/method.Orcus.Commands.WindowsCustomizer.WindowsCustomizerCommand.Initialize.c`](code/method.Orcus.Commands.WindowsCustomizer.WindowsCustomizerCommand.Initialize.c)
- [`code/method.Orcus.Connection.InformationCollector.SendInformation.c`](code/method.Orcus.Connection.InformationCollector.SendInformation.c)
- [`code/method.Orcus.Connection.ServerConnection.EndRead.c`](code/method.Orcus.Connection.ServerConnection.EndRead.c)
- [`code/method.Orcus.Connection.ServerConnection.ProcessResponse.c`](code/method.Orcus.Connection.ServerConnection.ProcessResponse.c)
- [`code/method.Orcus.Plugins.PluginLoader.LoadPlugins.c`](code/method.Orcus.Plugins.PluginLoader.LoadPlugins.c)
- [`code/method.Orcus.Protection.Autostarter.AddToAutostart.c`](code/method.Orcus.Protection.Autostarter.AddToAutostart.c)
- [`code/method.Orcus.StaticCommandManagement.ActiveCommandStopScheduler.ExecuteActiveCommand.c`](code/method.Orcus.StaticCommandManagement.ActiveCommandStopScheduler.ExecuteActiveCommand.c)
- [`code/method.Orcus.Utilities.WindowsDesktop.DesktopActions.MouseEvent.c`](code/method.Orcus.Utilities.WindowsDesktop.DesktopActions.MouseEvent.c)
- [`code/method.__c._.ctor_b__13_10.c`](code/method.__c._.ctor_b__13_10.c)

## Behavioral Analysis

Based on the analysis of disassembly chunk 6/6, here is the final comprehensive technical analysis of the "Orcus" malware sample.

### Final Comprehensive Overview
The final disassembly confirms that **Orcus** is a high-tier, professional-grade threat. It is not merely a basic Remote Access Trojan (RAT); it is a multi-functional cyber-espionage tool designed for long-term residency and automated data theft. The inclusion of "Streaming" capabilities and the use of advanced virtualization/obfuscation techniques indicate that the operators of Orcus are well-resourced and intent on maintaining high levels of control over compromised systems while making reverse engineering extremely difficult.

---

### Final Core Functionality and Purpose
*   **Advanced Remote Control & Surveillance:** 
    *   The identification of `method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.Streaming` confirms that the malware can stream real-time visual data (screen scraping/streaming) from the victim's machine to the attacker’s console. This allows the attacker to see exactly what the user is doing in real-time.
*   **Aggressive Credential Harvesting:**
    *   (From previous chunks): The malware contains specific modules for **Mozilla Firefox** and **Thunderbird**. It includes built-in `Decryptor` logic, meaning it doesn't just steal encrypted strings; it solves the encryption locally so the attacker receives plaintext passwords.
*   **Comprehensive Feature Suite:** 
    *   The presence of Webcam access, file system exploration, and automatic "Drop and Execute" capabilities ensures that once a machine is infected, the attacker has nearly all the tools necessary to exploit the target without needing further manual interaction.
*   **Monolithic Architecture (Costura):**
    *   By using `Costura` to bundle multiple functionalities into a single executable, the malware reduces its footprint on the disk while maintaining a complex, multi-functional backend.

---

### Final Suspicious and Malicious Behaviors
*   **High-Value Target Selection:** By specifically targeting Mozilla products (Firefox/Thunderbird), the attackers are targeting high-value credentials: banking logins, personal emails, and encrypted communications.
*   **Live Remote Monitoring:** The "Streaming" functionality indicates that the malware is capable of providing a live visual feed to the attacker, which can be used to guide social engineering attacks or monitor the victim's activity in real-time.
*   **Intentional Tool Sabotage (Anti-Analysis):** 
    *   The disassembly shows "overlapping instructions" and "bad instruction" breaks. This is a deliberate tactic where the malware uses **junk code** to confuse decompilers. When a researcher tries to analyze the code, the tools will fail or produce nonsensical results, forcing the analyst to spend hours/days manually cleaning up the code just to see what it does.

---

### Technical Analysis & Anti-Analysis Techniques
*   **Professional Obfuscation (VMProtect/Themida Class):** 
    *   The heavy use of `CONCAT`, `POPCOUNT`, and complex bitwise operations over simple arithmetic is a hallmark of high-end protectors. These are designed to make the "logical flow" of the program nearly impossible to follow using automated tools like Ghidra or IDA Pro without significant manual intervention.
*   **Instruction Overlapping:** 
    *   The warning regarding `overlapping instructions` (e.g., at `0x41abc2`) is a sophisticated technique where code is "hidden" inside what appears to be the middle of other instructions, effectively breaking the linear flow of disassembly.
*   **Complexity as a Defense:**
    *   The sheer density of junk code in the final chunk shows that the developers prioritized **analysis resistance**. They want to ensure that even if a security researcher finds the file, they cannot easily reverse-engineer it to find "kill switches" or identify the full scope of the network infrastructure.

---

### Final Summary
**Orcus is a sophisticated piece of malware that blends features typical of high-end RATs with specialized credential-stealing modules.** 

**Key Highlights from Full Analysis:**
1.  **Targeted Espionage:** Specifically engineered to extract and decrypt credentials from **Firefox** and **Thunderbird**.
2.  **Live Remote Interaction:** Includes a **Streaming** module for remote desktop capabilities, allowing the attacker to monitor the victim's screen in real-time.
3.  **Professional Packaging:** Uses **Costura** to bundle complex functionality into a single, portable "weaponized" executable.
4.  **Extreme Anti-Analysis:** Employs advanced obfuscation techniques (junk code, overlapping instructions, and bitwise complexity) to defeat automated analysis tools and waste the time of human researchers.

**Conclusion:** 
This is not an amateur creation. The Orcus framework represents a **professional-grade cyber-espionage tool**. It is designed for scenarios where the threat actor intends to maintain long-term access to a target, systematically harvest sensitive credentials, and provide a seamless remote experience for controlling the infected host. Its high level of obfuscation suggests it is used in targeted attacks or by organized criminal groups where "staying hidden" is as important as "obtaining data."

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in the "Orcus" malware analysis to the corresponding MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1134** | Screen Capture | The `Streaming` functionality allows for real-time visual data acquisition, enabling the attacker to monitor user activity via screen scraping. |
| **T1555** | Credentials from Web Browsers | The inclusion of specific modules and decryption logic for Firefox and Thunderbird indicates a targeted effort to harvest plain-text credentials from web browsers. |
| **T1083** | File and Directory Discovery | The "file system exploration" capability allows the threat actor to navigate the local file system to identify and target sensitive data. |
| **T1027** | Obfuscated Files or Information | The use of junk code, overlapping instructions, and VMProtect-style bitwise complexity is designed to hinder analysis by automated tools and human researchers. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavior report. Below are the extracted Indicators of Compromise (IOCs). 

Note: Many of the "Strings" provided were determined to be standard .NET framework references (mscorlib), junk code for anti-analysis, or non-specific memory artifacts. No high-confidence IP addresses or domain names were present in this specific dataset.

### **Indicators of Compromise**

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   *(None identified - only general application targets such as Mozilla Firefox and Thunderbird were mentioned, but no specific file paths were provided.)*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified in the provided strings)*

**Other artifacts**
*   **Command/Functionality Strings:** 
    *   `method.Orcus.Commands.RemoteDesktop.RemoteDesktopCommand.Streaming` (Identifies a specific internal command structure for remote screen scraping).
*   **Malware Frameworks/Techniques:**
    *   **Costura:** Used to bundle multiple functionalities into a single executable to reduce the disk footprint.
    *   **Overlapping Instructions:** Specifically identified at `0x41abc2` (Used as an anti-analysis technique to break disassemblers).
    *   **Junk Code/Bitwise Complexity:** Use of high-complexity bitwise operations and junk code to hinder manual and automated reverse engineering.

---

### **Analyst Notes**
While the report lacks "Network" IOCs (IPs/Domains), the analysis identifies this as a professional-grade piece of malware named **Orcus**. The primary indicators for defensive teams in this instance are behavioral:
1.  **Advanced Obfuscation:** The presence of overlapping instructions and intentional decompiler breaking indicates a high level of sophistication. 
2.  **Targeted Logic:** The malware is specifically designed to hunt for, extract, and decrypt credentials from **Mozilla Firefox** and **Thunderbird**.
3.  **Stealth Packaging:** The use of the **Costura** framework suggests an effort to hide various modules (like the "Streaming" module) within a single binary to evade simple signature-based detection.

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1. **Malware family:** Orcus
2. **Malware type:** RAT (Remote Access Trojan) / Infostealer
3. **Confidence:** High
4. **Key evidence:**
    *   **Advanced Remote Control Features:** The inclusion of `RemoteDesktopCommand.Streaming` and "file system exploration" capabilities are hallmark features of a high-tier RAT designed for long-term surveillance.
    *   **Targeted Credential Theft:** The malware contains specific, integrated modules to locate and decrypt passwords from Mozilla Firefox and Thunderbird, classifying it as an infostealer.
    *   **Sophisticated Anti-Analysis:** The use of "overlapping instructions," junk code, and the Costura framework indicates a professional-grade operation designed to evade automated analysis and hinder manual reverse engineering.
