# Threat Analysis Report

**Generated:** 2026-08-18 17:16 UTC
**Sample:** `1039202ca1decbed2f9fddce794a2a29dd1a538f31f0360091f444b132ca19ef_1039202ca1decbed2f9fddce794a2a29dd1a538f31f0360091f444b132ca19ef.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1039202ca1decbed2f9fddce794a2a29dd1a538f31f0360091f444b132ca19ef_1039202ca1decbed2f9fddce794a2a29dd1a538f31f0360091f444b132ca19ef.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 618,888 bytes |
| MD5 | `2a3b6b3395e138593b3c108975867d2f` |
| SHA1 | `b34222023acb51e8d3377f31a8f00a7ace0badf9` |
| SHA256 | `1039202ca1decbed2f9fddce794a2a29dd1a538f31f0360091f444b132ca19ef` |
| Overall entropy | 7.948 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2625594732 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 501,760 | 7.941 | ⚠️ Yes |
| `.rsrc` | 107,008 | 7.975 | ⚠️ Yes |

## Extracted Strings

Total strings found: **1897** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
v4.0.30319
#Strings
<thisLengthKnown>5__10
<>9__2_0
<StartUninstallation>b__2_0
<>c__DisplayClass2_0
<>c__DisplayClass3_0
<>c__DisplayClass4_0
<closeBtn_MouseEnter>b__8_0
<closeBtn_MouseLeave>b__9_0
<StartDownloadsAsync>b__0
<SetProgressSafe>b__0
<MakeDraggable>b__0
<UpdateStatus>b__0
<>p__0
<tempFile>5__11
<>9__2_1
<StartDownloadsAsync>b__2_1
<StartUninstallation>b__2_1
<>8__1
<DownloadForm_Load>d__1
<UninstallForm_Load>d__1
<>p__1
<>u__1
Func`1
Nullable`1
IEnumerable`1
CallSite`1
Task`1
AsyncTaskMethodBuilder`1
TaskAwaiter`1
List`1
label1
dwItem1
progressBar1
<fileStream>5__12
Microsoft.Win32
<>9__2_2
<StartUninstallation>b__2_2
<step>5__2
<req>5__2
<fileUrls>5__2
<StartDownloadsAsync>d__2
<StartUninstallation>d__2
<>p__2
<>u__2
Func`2
ValueTuple`2
Action`2
label2
dwItem2
<contentStream>5__13
<>9__2_3
<StartUninstallation>b__2_3
<totalBytes>5__3
<totalSteps>5__3
<>p__3
<>u__3
<buffer>5__14
<>9__2_4
<StartUninstallation>b__2_4
<totalBytesDownloaded>5__4
<filesToDelete>5__4
<>p__4
<>u__4
Func`4
label4
<bytesRead>5__15
<>9__2_5
<StartUninstallation>b__2_5
<fileIndex>5__5
<>p__5
<>u__5
<>7__wrap5
<bytesDownloadedThisFile>5__16
<>9__2_6
<StartUninstallation>b__2_6
<>o__6
<>p__6
<destination>5__7
<response>5__8
<contentLength>5__9
<Module>
SHCNE_ASSOCCHANGED
GetTypeFromProgID
MainUI
HT_CAPTION
WM_NCLBUTTONDOWN
System.IO
SHCNF_IDLIST
FromArgb
mscorlib
System.Collections.Generic
ReadAsync
SendAsync
WriteAsync
ReadAsStreamAsync
StartDownloadsAsync
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c..cctor` | `0x140004cf7` | 384560 | ✓ |
| `method.__c._StartUninstallation_b__2_6` | `0x140004d45` | 130994 | ✓ |
| `method.__StartDownloadsAsync_b__0_d.SetStateMachine` | `0x140005910` | 26410 | ✓ |
| `method._StartDownloadsAsync_d__2.MoveNext` | `0x14000436c` | 2376 | ✓ |
| `method._StartUninstallation_d__2.MoveNext` | `0x140004d8c` | 2052 | ✓ |
| `method.Installer.MainUI.InitializeComponent` | `0x1400035a0` | 1766 | ✓ |
| `method.Installer.InstallerHelpers.CreateDesktopShortcut` | `0x140002914` | 828 | ✓ |
| `method.Installer.InstallerHelpers.StartService` | `0x1400026ec` | 552 | ✓ |
| `method._DownloadForm_Load_d__1.MoveNext` | `0x140004150` | 524 | ✓ |
| `method.Installer.InstallForm.InitializeComponent` | `0x1400022c4` | 480 | ✓ |
| `method.Installer.UninstallForm.InitializeComponent` | `0x140003e6c` | 458 | ✓ |
| `method.__StartDownloadsAsync_b__0_d.MoveNext` | `0x140005758` | 440 | ✓ |
| `method.Installer.InstallerHelpers.AddToStartupRegistry` | `0x140002c50` | 424 | ✓ |
| `method._UninstallForm_Load_d__1.MoveNext` | `0x1400055a0` | 424 | ✓ |
| `method.Installer.InstallerHelpers.AddContextMenuEntry` | `0x140002df8` | 372 | ✓ |
| `method.Installer.InstallerHelpers.InstallService` | `0x1400025a8` | 324 | ✓ |
| `method.Installer.InstallerHelpers.SelfDestruct` | `0x14000337c` | 312 | ✓ |
| `method.Installer.InstallerHelpers.RemoveFromStartupRegistry` | `0x140003124` | 268 | ✓ |
| `method.Installer.InstallerHelpers.RegisterForUninstall` | `0x140002f6c` | 228 | ✓ |
| `method.Installer.Globals..cctor` | `0x140002050` | 201 | ✓ |
| `method.Installer.InstallerHelpers.RunSc` | `0x1400024e0` | 200 | ✓ |
| `method.Installer.InstallerHelpers.RemoveContextMenuEntry` | `0x140003230` | 176 | ✓ |
| `method.Installer.InstallForm.SetProgressSafe` | `0x1400021a4` | 160 | ✓ |
| `method.Installer.UninstallForm.SetProgressSafe` | `0x140003d4c` | 160 | ✓ |
| `method.Installer.InstallerHelpers.UninstallService` | `0x14000308c` | 152 | ✓ |
| `method.Installer.InstallForm.UpdateStatus` | `0x140002244` | 97 | ✓ |
| `method.Installer.UninstallForm.UpdateStatus` | `0x140003dec` | 97 | ✓ |
| `method.Installer.InstallerHelpers.TerminateProcess` | `0x14000332c` | 80 | ✓ |
| `method.Installer.InstallerHelpers.DeleteDesktopShortcut` | `0x1400032e0` | 76 | ✓ |
| `method.__c__DisplayClass2_0._StartDownloadsAsync_b__0` | `0x1400040c4` | 75 | ✓ |

### Decompiled Code Files

- [`code/method.Installer.Globals..cctor.c`](code/method.Installer.Globals..cctor.c)
- [`code/method.Installer.InstallForm.InitializeComponent.c`](code/method.Installer.InstallForm.InitializeComponent.c)
- [`code/method.Installer.InstallForm.SetProgressSafe.c`](code/method.Installer.InstallForm.SetProgressSafe.c)
- [`code/method.Installer.InstallForm.UpdateStatus.c`](code/method.Installer.InstallForm.UpdateStatus.c)
- [`code/method.Installer.InstallerHelpers.AddContextMenuEntry.c`](code/method.Installer.InstallerHelpers.AddContextMenuEntry.c)
- [`code/method.Installer.InstallerHelpers.AddToStartupRegistry.c`](code/method.Installer.InstallerHelpers.AddToStartupRegistry.c)
- [`code/method.Installer.InstallerHelpers.CreateDesktopShortcut.c`](code/method.Installer.InstallerHelpers.CreateDesktopShortcut.c)
- [`code/method.Installer.InstallerHelpers.DeleteDesktopShortcut.c`](code/method.Installer.InstallerHelpers.DeleteDesktopShortcut.c)
- [`code/method.Installer.InstallerHelpers.InstallService.c`](code/method.Installer.InstallerHelpers.InstallService.c)
- [`code/method.Installer.InstallerHelpers.RegisterForUninstall.c`](code/method.Installer.InstallerHelpers.RegisterForUninstall.c)
- [`code/method.Installer.InstallerHelpers.RemoveContextMenuEntry.c`](code/method.Installer.InstallerHelpers.RemoveContextMenuEntry.c)
- [`code/method.Installer.InstallerHelpers.RemoveFromStartupRegistry.c`](code/method.Installer.InstallerHelpers.RemoveFromStartupRegistry.c)
- [`code/method.Installer.InstallerHelpers.RunSc.c`](code/method.Installer.InstallerHelpers.RunSc.c)
- [`code/method.Installer.InstallerHelpers.SelfDestruct.c`](code/method.Installer.InstallerHelpers.SelfDestruct.c)
- [`code/method.Installer.InstallerHelpers.StartService.c`](code/method.Installer.InstallerHelpers.StartService.c)
- [`code/method.Installer.InstallerHelpers.TerminateProcess.c`](code/method.Installer.InstallerHelpers.TerminateProcess.c)
- [`code/method.Installer.InstallerHelpers.UninstallService.c`](code/method.Installer.InstallerHelpers.UninstallService.c)
- [`code/method.Installer.MainUI.InitializeComponent.c`](code/method.Installer.MainUI.InitializeComponent.c)
- [`code/method.Installer.UninstallForm.InitializeComponent.c`](code/method.Installer.UninstallForm.InitializeComponent.c)
- [`code/method.Installer.UninstallForm.SetProgressSafe.c`](code/method.Installer.UninstallForm.SetProgressSafe.c)
- [`code/method.Installer.UninstallForm.UpdateStatus.c`](code/method.Installer.UninstallForm.UpdateStatus.c)
- [`code/method._DownloadForm_Load_d__1.MoveNext.c`](code/method._DownloadForm_Load_d__1.MoveNext.c)
- [`code/method._StartDownloadsAsync_d__2.MoveNext.c`](code/method._StartDownloadsAsync_d__2.MoveNext.c)
- [`code/method._StartUninstallation_d__2.MoveNext.c`](code/method._StartUninstallation_d__2.MoveNext.c)
- [`code/method._UninstallForm_Load_d__1.MoveNext.c`](code/method._UninstallForm_Load_d__1.MoveNext.c)
- [`code/method.__StartDownloadsAsync_b__0_d.MoveNext.c`](code/method.__StartDownloadsAsync_b__0_d.MoveNext.c)
- [`code/method.__StartDownloadsAsync_b__0_d.SetStateMachine.c`](code/method.__StartDownloadsAsync_b__0_d.SetStateMachine.c)
- [`code/method.__c..cctor.c`](code/method.__c..cctor.c)
- [`code/method.__c._StartUninstallation_b__2_6.c`](code/method.__c._StartUninstallation_b__2_6.c)
- [`code/method.__c__DisplayClass2_0._StartDownloadsAsync_b__0.c`](code/method.__c__DisplayClass2_0._StartDownloadsAsync_b__0.c)

## Behavioral Analysis

Based on the provided strings and disassembled code, here is a technical analysis of the binary's functionality.

### **Core Functionality**
The binary functions as a **downloader and installer**. It is designed to fetch remote content (likely a secondary payload or application components), install them onto the local system, configure persistence mechanisms, and provide a user interface for these actions. 

Based on the function names and internal logic, it handles:
*   **Remote Fetching:** The `StartDownloadsAsync` functions indicate the program reaches out to a remote server to retrieve files.
*   **Installation Management:** It includes routines to install/uninstall software, manage installation progress (`SetProgressSafe`, `UpdateStatus`), and handle "Setup" and "Uninstall" UI forms.
*   **System Integration:** It modifies the OS environment by creating desktop shortcuts and interacting with Windows Services.

### **Suspicious or Malicious Behaviors**
The following behaviors are highly characteristic of a "Loader" or a "Dropper" used in malware campaigns:

*   **Network Communication (Downloader):** The presence of `StartDownloadsAsync` and the inclusion of `System.Net`, `HttpClient`, and `Request` suggests that the primary purpose of this binary is to download additional files from a remote server into the local system.
*   **Persistence Mechanisms:**
    *   **Service Creation/Manipulation:** The functions `InstallService`, `UninstallService`, and `StartService` indicate the program can install a persistent background service. This is a common technique for malware to maintain a presence on a machine after a reboot or to run with elevated privileges.
    *   **Registry Persistence:** `AddToStartupRegistry` and `RemoveFromStartupRegistry` suggest it modifies Windows Registry keys to ensure its components start automatically when the system boots.
*   **System Manipulation & File Interaction:**
    *   The binary interacts with the file system (via `System.IO`) and manages "hidden" or specific directories (`programFilesShield`, `publicDocumentsShield`).
    *   **Desktop Persistence:** `CreateDesktopShortcut` and `DeleteDesktopShortcut` ensure that the user sees a shortcut for the installed application, making it appear as legitimate software to the end-user.
*   **Process Manipulation:** The function `TerminateProcess` is often used by malware to shut down competing applications or antivirus/security software to prevent interference during the installation phase.

### **Notable Techniques & Patterns**
*   **Obfuscation and Anti-Analysis:** A significant portion of the disassembly shows "bad instruction" errors, "halt_baddata," and complex assembly structures that failed to decompile into clean C code. This is a strong indicator that the binary is protected by an **obfuscator or packer**. These tools are designed to hinder manual analysis and automated sandboxing.
*   **Modular Framework:** The naming conventions (e.g., `InstallerHelpers`) suggest this may be part of a larger "builder" framework, where different payloads can be "wrapped" into the same installer template.
*   **Sophisticated Networking Logic:** The inclusion of `HttpClient`, `EnsureSuccessStatusCode`, and `Task` objects indicates that it is designed for modern asynchronous communication with web servers.

### **Summary Conclusion**
This binary is likely a **malicious downloader/loader**. While it contains the components to appear as a legitimate installer (UI forms, progress bars, shortcut creation), its underlying capabilities—**remote downloads, service installation, and startup persistence**—are hallmarks of malware designed to deliver a persistent backdoor or other malicious payloads.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The use of `StartDownloadsAsync` and `HttpClient` components indicates the binary is designed to fetch remote payloads or modules onto the local system. |
| **T1543.003** | Create or Run Service | The functions `InstallService`, `UninstallService`, and `StartService` indicate a mechanism for establishing persistent background execution with elevated privileges. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The `AddToStartupRegistry` and `RemoveFromStartupRegistry` functions are used to ensure the malware persists across system reboots via the Windows Registry. |
| **T1546.003** | Event Triggered Execution: Shortcut File | The use of `CreateDesktopShortcut` provides a means for the user to interact with the application while maintaining a persistent presence on the desktop. |
| **T1083** | File and Directory Hide | The management of "hidden" or specific directory paths (`programFilesShield`) indicates an attempt to conceal malicious files from the user and basic system tools. |
| **T1027** | Obfuscated Files or Information | The presence of "bad instructions" and complex assembly structures signifies the use of packers or obfuscators to hinder reverse engineering and automated analysis. |
| **T1496** | Disable or Modify System Attributes | The `TerminateProcess` function, specifically when used to shut down security software, is a common method for evading system defenses during installation. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The provided text contains many functional indicators (behaviors) but lacks specific infrastructure IOCs (such as hardcoded IP addresses or unique file hashes).

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis mentions `StartDownloadsAsync` and `HttpClient`, indicating network activity, but no specific C2 domains or IP addresses were present in the provided strings.)

### **File paths / Registry keys**
*   **programFilesShield** (Potential internal variable/path used for staging files)
*   **publicDocumentsShield** (Potential internal variable/path used for staging files)
*   **StartupRegistryValueName** (Indicator of registry modification for persistence; specific key path not provided in strings)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **C2/Download Patterns:** 
    *   Use of `HttpClient` and `GetAsync` for remote content retrieval.
    *   Presence of `EnsureSuccessStatusCode` and `Request` logic to handle automated payload downloads.
*   **Persistence Mechanisms:**
    *   **Service Manipulation:** References to `InstallService`, `UninstallService`, and `StartService`.
    *   **Registry Persistence:** Reference to `StartupRegistryValueName` for automatic execution.
    *   **Shortcut Creation:** Presence of `CreateDesktopShortcut` and `DeleteDesktopShortcut` to provide a visual presence on the desktop.
*   **Obfuscation/Packing Indicators:** 
    *   The behavioral analysis notes "bad instruction" errors and "halt_baddata," indicating the use of an **obfuscator or packer** to hinder analysis.
*   **Internal Component Names (Potential identifying markers for a specific builder):**
    *   `InstallerHelpers`
    *   `DownloadForm_Load`
    *   `UninstallForm_Load`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Remote Fetching & Delivery:** The inclusion of `StartDownloadsAsync`, `HttpClient`, and `System.Net` libraries confirms its primary role as a downloader designed to fetch and install secondary payloads from a remote server.
*   **Persistence Mechanisms:** The binary explicitly contains logic for installing/starting Windows Services (`InstallService`) and modifying Registry keys (`AddToStartupRegistry`), both of which are classic techniques used by loaders to ensure the malware (or subsequent payloads) remains active after reboots.
*   **Evasion & Obfuscation:** The report notes "bad instruction" errors and "halt_baddata," indicating heavy use of packers/obfuscators, combined with a decoy "installer" UI (progress bars and desktop shortcuts) to hide its malicious intent from the end-user.
