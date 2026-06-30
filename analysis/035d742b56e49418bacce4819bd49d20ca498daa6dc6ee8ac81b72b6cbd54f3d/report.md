# Threat Analysis Report

**Generated:** 2026-06-29 21:48 UTC
**Sample:** `035d742b56e49418bacce4819bd49d20ca498daa6dc6ee8ac81b72b6cbd54f3d_035d742b56e49418bacce4819bd49d20ca498daa6dc6ee8ac81b72b6cbd54f3d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `035d742b56e49418bacce4819bd49d20ca498daa6dc6ee8ac81b72b6cbd54f3d_035d742b56e49418bacce4819bd49d20ca498daa6dc6ee8ac81b72b6cbd54f3d.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 207,664 bytes |
| MD5 | `7ca8c7aab3f69734a2c4b1a67c37e98a` |
| SHA1 | `c59d1cad64980920a738042737c36a64cd9eb711` |
| SHA256 | `035d742b56e49418bacce4819bd49d20ca498daa6dc6ee8ac81b72b6cbd54f3d` |
| Overall entropy | 6.502 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2241433439 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 177,664 | 6.591 | No |
| `.rsrc` | 17,408 | 3.502 | No |

## Extracted Strings

Total strings found: **1464** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
v4.0.30319
#Strings
<.ctor>b__10_0
<>c__DisplayClass51_0
<>9__1_0
<GetWindTuple>b__1_0
<>c__DisplayClass1_0
<>c__DisplayClass14_0
<.ctor>b__4_0
<.ctor>b__55_0
<StrtTskAsnc>b__6_0
<>c__DisplayClass38_0
<>c__DisplayClass39_0
<MainTasksAsync>b__0
<navigate>b__0
<LoadVideo>b__0
<IsSetSuccess>b__0
<IsAlreadySet>b__0
<>o__0
<>p__0
<SendPostRequestAsync>d__11
<.ctor>b__10_1
<LoadVideo>b__1_1
<.ctor>b__4_1
<>8__1
<>p__1
<>u__1
Func`1
IEnumerable`1
Predicate`1
CallSite`1
Task`1
Action`1
AsyncTaskMethodBuilder`1
TaskAwaiter`1
keyCode1
get_Item1
Microsoft.Win32
<i>5__2
<OnLoaded>d__2
<>p__2
Func`2
Tuple`2
Action`2
keyCode2
get_Item2
get_Itr2
set_Itr2
<SendPostRequestAsync>d__13
<>p__3
Func`3
<MainTasksAsync>d__14
StrToB64
ConvertB64
get_b64
set_b64
<>p__4
Func`4
Master.Files.MasterAnimation.mp4
<>o__15
<>p__5
<SendPostRequest>d__16
<StrtTskAsnc>d__6
get_UTF8
<Module>
VK_TAB
get_TsT_MB
set_TsT_MB
get_SourceID
set_SourceID
GetTypeFromProgID
get_ChanID
set_ChanID
VK_ESCAPE
OpenFF
get_MozFF
set_MozFF
VK_CONTROL
get_PRF_URL
set_PRF_URL
OpenURL
AddToL
get_ThirdVM
set_ThirdVM
get_CloseConfirmationVM
set_CloseConfirmationVM
get_FirstVM
set_FirstVM
VK_LWIN
VK_RETURN
VK_DOWN
System.IO
get_TsT_IO
set_TsT_IO
KEYEVENTF_KEYUP
get_RegP
set_RegP
VK_SHIFT
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c._GetWindTuple_b__1_0` | `0x140006206` | 36106 | ✓ |
| `method.Master.MainWindow.get_shutdownService` | `0x140002175` | 650 | ✓ |
| `method.__StrtTskAsnc_b__6_0_d.MoveNext` | `0x14000590c` | 636 | ✓ |
| `method.Master.Models.Network.ReportHashT.AfterVSix` | `0x140003fe8` | 603 | ✓ |
| `method.Master.Views.FirstView.Hyperlink_RequestNavigate` | `0x140002565` | 590 | ✓ |
| `method.Master.Models.AppSettings.Pronto.CreateDesktopShortcut` | `0x140005210` | 580 | ✓ |
| `method.Master.Models.Network.ServerApi.ConvertToSettings` | `0x1400043b0` | 532 | ✓ |
| `method._MainTasksAsync_d__14.MoveNext` | `0x140005bac` | 468 | ✓ |
| `method.Master.ViewModels.MainViewModel.ShowCloseConfirmation` | `0x140002ba5` | 407 | ✓ |
| `method.Master.ViewModels.CloseViewModel.CancelClose` | `0x140002855` | 338 | ✓ |
| `method.Master.ViewModels.MainViewModel.UpdateViewProperties` | `0x140002be8` | 332 | ✓ |
| `method.Master.Models.MainProc.MainProcess.MainWorkFlow` | `0x140002fc4` | 315 | ✓ |
| `method._SendPostRequest_d__16.MoveNext` | `0x140005fd4` | 276 | ✓ |
| `method.Master.Models.Cod.ConvertB64.B64ToStr` | `0x140004f6c` | 274 | ✓ |
| `method.Master.Models.Network.ReportHashT.RepInit` | `0x140003edc` | 268 | ✓ |
| `method.Master.ViewModels.MainViewModel.set_CloseConfirmationVM` | `0x140002a6f` | 266 | ✓ |
| `method.Master.Models.Data.AppilcationData.OpSysData` | `0x140004ab8` | 256 | ✓ |
| `method._StrtTskAsnc_d__6.MoveNext` | `0x140005d90` | 248 | ✓ |
| `method.Master.Models.MainProc.MainProcess.IsAlreadySet` | `0x140003260` | 236 | ✓ |
| `method._SendPostRequestAsync_d__11.MoveNext` | `0x140005ed8` | 236 | ✓ |
| `method._SendPostRequestAsync_d__13.MoveNext` | `0x1400060f8` | 236 | ✓ |
| `method.Master.Models.Cod.ConvertB64.StrToB64` | `0x140004e8c` | 224 | ✓ |
| `method.Master.Models.Data.BrMethods.GetBrVer` | `0x1400047fc` | 216 | ✓ |
| `method.Master.Views.ThirdView.LoadVideo` | `0x140002640` | 212 | ✓ |
| `method.Master.Models.MainProc.MainProcess.TypeText` | `0x1400037bc` | 212 | ✓ |
| `method.Master.Models.Data.BrMethods.GetWindTuple` | `0x140004674` | 212 | ✓ |
| `method.Master.Models.AppSettings.RegSettings.AddAppKey` | `0x1400054d8` | 212 | ✓ |
| `method.Master.Models.MainProc.MainProcess.moveWindowSuccess` | `0x140003520` | 204 | ✓ |
| `method.Master.Models.Network.ReportApi.getBody` | `0x140003ca0` | 200 | ✓ |
| `method.Master.Models.MainProc.MainProcess.SuccessRepUpdate` | `0x140003124` | 196 | ✓ |

### Decompiled Code Files

- [`code/method.Master.MainWindow.get_shutdownService.c`](code/method.Master.MainWindow.get_shutdownService.c)
- [`code/method.Master.Models.AppSettings.Pronto.CreateDesktopShortcut.c`](code/method.Master.Models.AppSettings.Pronto.CreateDesktopShortcut.c)
- [`code/method.Master.Models.AppSettings.RegSettings.AddAppKey.c`](code/method.Master.Models.AppSettings.RegSettings.AddAppKey.c)
- [`code/method.Master.Models.Cod.ConvertB64.B64ToStr.c`](code/method.Master.Models.Cod.ConvertB64.B64ToStr.c)
- [`code/method.Master.Models.Cod.ConvertB64.StrToB64.c`](code/method.Master.Models.Cod.ConvertB64.StrToB64.c)
- [`code/method.Master.Models.Data.AppilcationData.OpSysData.c`](code/method.Master.Models.Data.AppilcationData.OpSysData.c)
- [`code/method.Master.Models.Data.BrMethods.GetBrVer.c`](code/method.Master.Models.Data.BrMethods.GetBrVer.c)
- [`code/method.Master.Models.Data.BrMethods.GetWindTuple.c`](code/method.Master.Models.Data.BrMethods.GetWindTuple.c)
- [`code/method.Master.Models.MainProc.MainProcess.IsAlreadySet.c`](code/method.Master.Models.MainProc.MainProcess.IsAlreadySet.c)
- [`code/method.Master.Models.MainProc.MainProcess.MainWorkFlow.c`](code/method.Master.Models.MainProc.MainProcess.MainWorkFlow.c)
- [`code/method.Master.Models.MainProc.MainProcess.SuccessRepUpdate.c`](code/method.Master.Models.MainProc.MainProcess.SuccessRepUpdate.c)
- [`code/method.Master.Models.MainProc.MainProcess.TypeText.c`](code/method.Master.Models.MainProc.MainProcess.TypeText.c)
- [`code/method.Master.Models.MainProc.MainProcess.moveWindowSuccess.c`](code/method.Master.Models.MainProc.MainProcess.moveWindowSuccess.c)
- [`code/method.Master.Models.Network.ReportApi.getBody.c`](code/method.Master.Models.Network.ReportApi.getBody.c)
- [`code/method.Master.Models.Network.ReportHashT.AfterVSix.c`](code/method.Master.Models.Network.ReportHashT.AfterVSix.c)
- [`code/method.Master.Models.Network.ReportHashT.RepInit.c`](code/method.Master.Models.Network.ReportHashT.RepInit.c)
- [`code/method.Master.Models.Network.ServerApi.ConvertToSettings.c`](code/method.Master.Models.Network.ServerApi.ConvertToSettings.c)
- [`code/method.Master.ViewModels.CloseViewModel.CancelClose.c`](code/method.Master.ViewModels.CloseViewModel.CancelClose.c)
- [`code/method.Master.ViewModels.MainViewModel.ShowCloseConfirmation.c`](code/method.Master.ViewModels.MainViewModel.ShowCloseConfirmation.c)
- [`code/method.Master.ViewModels.MainViewModel.UpdateViewProperties.c`](code/method.Master.ViewModels.MainViewModel.UpdateViewProperties.c)
- [`code/method.Master.ViewModels.MainViewModel.set_CloseConfirmationVM.c`](code/method.Master.ViewModels.MainViewModel.set_CloseConfirmationVM.c)
- [`code/method.Master.Views.FirstView.Hyperlink_RequestNavigate.c`](code/method.Master.Views.FirstView.Hyperlink_RequestNavigate.c)
- [`code/method.Master.Views.ThirdView.LoadVideo.c`](code/method.Master.Views.ThirdView.LoadVideo.c)
- [`code/method._MainTasksAsync_d__14.MoveNext.c`](code/method._MainTasksAsync_d__14.MoveNext.c)
- [`code/method._SendPostRequestAsync_d__11.MoveNext.c`](code/method._SendPostRequestAsync_d__11.MoveNext.c)
- [`code/method._SendPostRequestAsync_d__13.MoveNext.c`](code/method._SendPostRequestAsync_d__13.MoveNext.c)
- [`code/method._SendPostRequest_d__16.MoveNext.c`](code/method._SendPostRequest_d__16.MoveNext.c)
- [`code/method._StrtTskAsnc_d__6.MoveNext.c`](code/method._StrtTskAsnc_d__6.MoveNext.c)
- [`code/method.__StrtTskAsnc_b__6_0_d.MoveNext.c`](code/method.__StrtTskAsnc_b__6_0_d.MoveNext.c)
- [`code/method.__c._GetWindTuple_b__1_0.c`](code/method.__c._GetWindTuple_b__1_0.c)

## Behavioral Analysis

Based on the provided disassembly and string list, here is an analysis of the binary's functionality.

### Core Functionality
The sample appears to be a **malicious loader or bot agent** (likely written in .NET) designed to collect system information, report it to a remote server, maintain persistence on the host machine, and potentially interact with other applications or windows automatically.

### Suspicious and Malicious Behaviors

*   **Data Exfiltration & Reporting:**
    *   The code contains multiple instances of `SendPostRequestAsync` and `ReportHashT`. This suggests a consistent pattern of gathering data from the local system and "reporting" it to a Command & Control (C2) server.
    *   The presence of specific identifiers in the strings (e.g., `sorcid`, `chnid`, `visid`) suggests tracking unique identities for infected machines within a botnet or malicious infrastructure.
    *   `ReportApi.getBody` and `reportHashT` indicate that various system attributes are being gathered, potentially hashed to create a "fingerprint" of the victim's hardware/software environment.

*   **Persistence Mechanism:**
    *   The function `method.Master.Models.AppSettings.Pronto.CreateDesktopShortcut` is a clear indicator of persistence. The malware intends to create a shortcut on the desktop to ensure it can be easily reopened or continue running after the initial infection.

*   **Data Obfuscation:**
    *   The inclusion of `ConvertB64`, `StrToB64`, and internal "Cod" (Coding) modules indicates that the malware uses Base64 encoding to obfuscate outgoing network traffic, file paths, or received commands from the C2 server.

*   **Automated Interaction & UI Manipulation:**
    *   **`TypeText`**: The presence of a text-typing function suggests the malware may simulate human input. This is often used to auto-fill login credentials into other windows or interact with terminal prompts.
    *   **`GetWindTuple` and `moveWindowSuccess`**: These suggest interaction with the Windows API to manipulate, move, or identify windows. In a malicious context, this could be used to overlay a fake UI over another application or ensure its own window remains visible/hidden.

### Notable Techniques & Patterns

*   **Asynchronous Network Operations:** The heavy use of `Task` and `Async` (e.g., `MainTasksAsync`, `SendPostRequestAsync`) suggests the malware is designed to perform network operations in the background without "freezing" the UI, allowing it to stay active while exfiltrating data.
*   **Modular Architecture:** The naming convention (`Master.Models.Network`, `Master.Views`, `Master.Models.Data`) indicates a structured development approach typical of sophisticated malware samples that may be part of a larger framework or botnet toolkit.
*   **Information Gathering (Profiling):** The strings `Get_OS_OU`, `get_DpiX`, and `get_WorkingArea` indicate the program is profiling the user's display environment—information often used by malware to determine if it is running in a virtual machine or a sandbox.

### Summary of Risk
This binary shows high indicators of **malicious intent**. It is equipped with the necessary components for:
1.  **Information Stealing:** Collecting and "reporting" system data via HTTP POST.
2.  **Persistence:** Ensuring it stays on the system via desktop shortcuts.
3.  **Evasion/Obfuscation:** Using Base64 to hide its communication.
4.  **User Interaction Simulation:** Potentially automating input or manipulating windows to deceive the user.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1041** | Exfiltration Over C2 Channel | The use of `SendPostRequestAsync` and "Report" functions indicates that gathered system data is being transmitted back to the attacker's infrastructure. |
| **T1071.001** | Web Protocols (HTTP) | The consistent use of `SendPostRequestAsync` implies the malware uses standard web protocols for communication with its C2 server. |
| **T1547.001** | Add Startup Entry (Shortcut) | The creation of a desktop shortcut is a direct method used to ensure the application remains accessible and persistent on the host. |
| **T1132** | Data Encoding | The use of Base64 encoding functions (`ConvertB64`, `StrToB64`) is employed to obfuscate network traffic, file paths, and received commands. |
| **T1018** | System Information Discovery | The collection of specific attributes like `Get_OS_OU` and `get_DpiX` allows the malware to profile the host system's hardware and software environment. |
| **T1497** | Virtualization/Sandbox Evasion | Profiling display metrics such as `get_WorkingArea` is a common tactic used to determine if the malware is running in a sandbox or virtual machine. |
| **T0835** | Interaction with Windows API (UI Manipulation) | The use of `GetWindTuple` and `moveWindowSuccess` suggests manipulation of window properties, potentially to hide its presence or overlay fake content. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** No explicit IP addresses, URLs, or file hashes were found in the raw string list; however, several significant behavioral artifacts and identifiers were identified.

### **IP addresses / URLs / Domains**
*None identified.* (The analysis notes `SendPostRequestAsync`, but no specific destination URLs or IPs are present in the provided text.)

### **File paths / Registry keys**
*   **Master.Files.MasterAnimation.mp4** (Specific file resource/filename)
*   **Get_RegP** (Indicates an internal routine for registry key interaction, though no specific keys were listed in the string dump).

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts**
*   **C2 Communication Patterns:** 
    *   `SendPostRequestAsync`, `ReportHashT`: Indicates automated data exfiltration to a remote server.
    *   `PostAsync`: Further evidence of HTTP-based reporting.
*   **Obfuscation Techniques:**
    *   `StrToB64`, `ConvertB64`: Usage of Base64 encoding to mask network traffic or internal strings.
*   **Persistence Mechanisms:**
    *   `CreateDesktopShortcut`: Specific method used to maintain presence on the host system via a desktop icon.
*   **Tracking & Profiling Identifiers:**
    *   `sorcid`, `chnid`, `visid`: Unique identifiers used for tracking infected machines within a botnet infrastructure.
    *   `get_ThirdVM`, `get_WorkingArea`, `get_DpiX`: Specific variables used to profile the environment and potentially detect virtual machine (VM) usage or sandbox analysis.
*   **User Interaction Simulation:**
    *   `TypeText`: Indicates capability to simulate keyboard input to automate data entry or bypass prompts.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Unknown
2. **Malware type**: Loader / Bot Agent
3. **Confidence**: High (on behavior type) / Medium (on specific naming)
4. **Key evidence**:
    *   **C2 Communication & Reporting:** The presence of `SendPostRequestAsync`, `ReportHashT`, and unique identifiers (`sorcid`, `chnid`, `visid`) indicates the sample is part of a structured botnet or a multi-stage loader designed to "phone home" with victim machine fingerprints.
    *   **Persistence & Evasion:** The use of `CreateDesktopShortcut` for persistence, combined with Base64 obfuscation and environment checks (`get_ThirdVM`, `get_WorkingArea`), is characteristic of malware designed to maintain a long-term presence while evading automated sandbox detection.
    *   **Automation & Interaction:** The inclusion of `TypeText` and UI manipulation functions suggests the malware is capable of automating user interactions, likely to facilitate credential theft or bypass security prompts during the initial infection phase.
