# Threat Analysis Report

**Generated:** 2026-09-07 20:29 UTC
**Sample:** `1570f05cfa7581ca2f1123f09b15ffea002ec9749a30bfc961e78bff21a7b4cc_1570f05cfa7581ca2f1123f09b15ffea002ec9749a30bfc961e78bff21a7b4cc.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1570f05cfa7581ca2f1123f09b15ffea002ec9749a30bfc961e78bff21a7b4cc_1570f05cfa7581ca2f1123f09b15ffea002ec9749a30bfc961e78bff21a7b4cc.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,019,600 bytes |
| MD5 | `02ba30736de6a2749db1d6ce79c93365` |
| SHA1 | `0b4608431fd8020df12e19a1ce21267412c49f3c` |
| SHA256 | `1570f05cfa7581ca2f1123f09b15ffea002ec9749a30bfc961e78bff21a7b4cc` |
| Overall entropy | 5.627 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3794216892 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 897,536 | 5.757 | No |
| `.rsrc` | 109,568 | 3.641 | No |

## Extracted Strings

Total strings found: **5968** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

X )UU

X )UU

X )UU

,p	o#
v4.0.30319
#Strings

-BT
	C
V
l
s

__StaticArrayInitTypeSize=20
__StaticArrayInitTypeSize=40
<>9__20_0
<InstallWorker_DoWork>b__20_0
<TerStractureProcess>b__20_0
<>c__DisplayClass21_0
<>c__DisplayClass12_0
<>9__22_0
<InstallWorker_ProgressChanged>b__22_0
<>c__DisplayClass13_0
<HideQuitDialog>b__33_0
<>c__DisplayClass24_0
<ShowEncouragementMessage>b__25_0
<ProceedButton_Click>b__35_0
<InstallWorker_RunWorkerCompleted>b__26_0
<>9__36_0
<AnimateAndClose>b__36_0
<TransitionToInstalling>b__18_0
<>9__28_0
<BS>b__28_0
<>9__19_0
<BP>b__19_0
<>c__DisplayClass19_0
<ExecuteDocumentMerge>b__0
<DecryptValue>b__0
<EncryptValue>b__0
<StartInstallation>b__0
<ExtractEmbeddedExecutables>b__0
<>p__0
<ExecuteTTransmission>d__31
C894F66F62774945D1DBE6C7C9ED1A4EF34DF9AC949BA819BEC5895A808195D1
get_SD1
<ProceedButton_Click>b__35_1
<InstallWorker_RunWorkerCompleted>b__26_1
<>p__1
<>u__1
<>f__AnonymousType0`1
Func`1
Nullable`1
IEnumerable`1
ConfiguredTaskAwaitable`1
CallSite`1
Task`1
Action`1
AsyncTaskMethodBuilder`1
EqualityComparer`1
TaskAwaiter`1
IEnumerator`1
get_Item1
<>7__wrap1
__StaticArrayInitTypeSize=12
<CheckInternetConnectivityOnStartup>d__12
<SendJsonPostRequest>d__22
<SendCompletionNotification>d__32
Microsoft.Win32
7BE2E64563997DD0E9A07AF3766F7272259B253411C22E66D5E68096E147ED62
get_SD2
<mergeConfiguration>5__2
<httpClient>5__2
<CheckInternetConnectivityAsync>d__2
<>p__2
<>u__2
Func`2
Tuple`2
Action`2
KeyValuePair`2
Dictionary`2
get_Item2
<>7__wrap2
<InitializeAndMerge>d__23
<startTime>5__3
<>o__3
<>p__3
Func`3
__StaticArrayInitTypeSize=24
<ExecuteDocumentMerge>d__24
ConvertToBase64
<endTime>5__4
<httpClient>5__4
<CheckInternetConnectivityThoroughAsync>d__4
<>p__4
<>f__AnonymousType1`4
Func`4
<CheckConnectionSpeedAsync>d__5
<>p__5
<>p__6
02CA228A31114E5A8B745B009B4A1421BD98E6444F1B40B3B69B076FA64FBBD7
get_UTF8
<InitializeBackendCommunication>d__29
<Module>
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__InstallWorker_DoWork_b__20_0_d.SetStateMachine` | `0x14000612c` | 33454 | ✓ |
| `method.SupremePDFInstaller.MainWindow.TitleBar_MouseLeftButtonDown` | `0x140003aab` | 2258 | ✓ |
| `method.SupremePDFInstaller.MainWindow.ReturnButton_Click` | `0x140004503` | 892 | ✓ |
| `method.__c__DisplayClass24_0._ExecuteDocumentMerge_b__0` | `0x1400050a8` | 876 | ✓ |
| `method.SupremeDOC.SystemUtilities.CreateDesktopShortcut` | `0x1400030a4` | 864 | ✓ |
| `method._ExecuteTTransmission_d__31.MoveNext` | `0x140004900` | 740 | ✓ |
| `method.SupremePDFInstaller.MainWindow.InstallWorker_DoWork` | `0x140003ca8` | 728 | ✓ |
| `entry0` | `0x140003779` | 586 | ✓ |
| `method._InitializeBackendCommunication_d__29.MoveNext` | `0x140004bf4` | 576 | ✓ |
| `method._CheckConnectionSpeedAsync_d__5.MoveNext` | `0x14000587c` | 576 | ✓ |
| `method.SupremeDOC.TManager.IsChreInstalled` | `0x1400026a4` | 536 | ✓ |
| `method._SendCompletionNotification_d__32.MoveNext` | `0x140004e44` | 468 | ✓ |
| `method._CheckInternetConnectivityThoroughAsync_d__4.MoveNext` | `0x140005c1c` | 448 | ✓ |
| `method._InitializeAndMerge_d__23.MoveNext` | `0x140005504` | 440 | ✓ |
| `method._SendJsonPostRequest_d__22.MoveNext` | `0x1400056cc` | 416 | ✓ |
| `method.SupremePDFInstaller.MainWindow.StartInstallation` | `0x140003b38` | 368 | ✓ |
| `method.SupremeDOC.SystemUtilities.IsSupportedUser` | `0x140003530` | 356 | ✓ |
| `method.SupremePDFInstaller.MainWindow.System.Windows.Markup.IComponentConnector.Connect` | `0x14000463c` | 352 | ✓ |
| `method._CheckInternetConnectivityAsync_d__2.MoveNext` | `0x140005acc` | 320 | ✓ |
| `method.SupremePDFInstaller.MainWindow.ExtractEmbeddedExecutables` | `0x140003f80` | 316 | ✓ |
| `method.SupremePDFInstaller.MainWindow.PrivacyPolicy_Click` | `0x1400043d5` | 302 | ✓ |
| `method.SupremeDOC.SystemUtilities.RegisterApplicationInUninstallRegistry` | `0x140003404` | 268 | ✓ |
| `method.SupremePDFInstaller.MainWindow.InstallWorker_RunWorkerCompleted` | `0x140004278` | 264 | ✓ |
| `method.__ProceedButton_Click_b__35_0_d.MoveNext` | `0x140005dec` | 252 | ✓ |
| `method.SupremeDOC.DocumentMergeService.RestartStractureProcess` | `0x140002bf8` | 248 | ✓ |
| `method.SupremeDOC.SystemUtilities.CollectOperatingSystemInformation` | `0x140002ee4` | 248 | ✓ |
| `method.SupremePDFInstaller.MainWindow.MainWindow_Closing` | `0x1400039c3` | 232 | ✓ |
| `method.SupremePDFInstaller.MainWindow.InitializeInstaller` | `0x1400039d4` | 232 | ✓ |
| `method._ExecuteDocumentMerge_d__24.MoveNext` | `0x140005414` | 224 | ✓ |
| `method.SupremePDFInstaller.MainWindow..ctor` | `0x1400038c8` | 204 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.SupremeDOC.DocumentMergeService.RestartStractureProcess.c`](code/method.SupremeDOC.DocumentMergeService.RestartStractureProcess.c)
- [`code/method.SupremeDOC.SystemUtilities.CollectOperatingSystemInformation.c`](code/method.SupremeDOC.SystemUtilities.CollectOperatingSystemInformation.c)
- [`code/method.SupremeDOC.SystemUtilities.CreateDesktopShortcut.c`](code/method.SupremeDOC.SystemUtilities.CreateDesktopShortcut.c)
- [`code/method.SupremeDOC.SystemUtilities.IsSupportedUser.c`](code/method.SupremeDOC.SystemUtilities.IsSupportedUser.c)
- [`code/method.SupremeDOC.SystemUtilities.RegisterApplicationInUninstallRegistry.c`](code/method.SupremeDOC.SystemUtilities.RegisterApplicationInUninstallRegistry.c)
- [`code/method.SupremeDOC.TManager.IsChreInstalled.c`](code/method.SupremeDOC.TManager.IsChreInstalled.c)
- [`code/method.SupremePDFInstaller.MainWindow..ctor.c`](code/method.SupremePDFInstaller.MainWindow..ctor.c)
- [`code/method.SupremePDFInstaller.MainWindow.ExtractEmbeddedExecutables.c`](code/method.SupremePDFInstaller.MainWindow.ExtractEmbeddedExecutables.c)
- [`code/method.SupremePDFInstaller.MainWindow.InitializeInstaller.c`](code/method.SupremePDFInstaller.MainWindow.InitializeInstaller.c)
- [`code/method.SupremePDFInstaller.MainWindow.InstallWorker_DoWork.c`](code/method.SupremePDFInstaller.MainWindow.InstallWorker_DoWork.c)
- [`code/method.SupremePDFInstaller.MainWindow.InstallWorker_RunWorkerCompleted.c`](code/method.SupremePDFInstaller.MainWindow.InstallWorker_RunWorkerCompleted.c)
- [`code/method.SupremePDFInstaller.MainWindow.MainWindow_Closing.c`](code/method.SupremePDFInstaller.MainWindow.MainWindow_Closing.c)
- [`code/method.SupremePDFInstaller.MainWindow.PrivacyPolicy_Click.c`](code/method.SupremePDFInstaller.MainWindow.PrivacyPolicy_Click.c)
- [`code/method.SupremePDFInstaller.MainWindow.ReturnButton_Click.c`](code/method.SupremePDFInstaller.MainWindow.ReturnButton_Click.c)
- [`code/method.SupremePDFInstaller.MainWindow.StartInstallation.c`](code/method.SupremePDFInstaller.MainWindow.StartInstallation.c)
- [`code/method.SupremePDFInstaller.MainWindow.System.Windows.Markup.IComponentConnector.Connect.c`](code/method.SupremePDFInstaller.MainWindow.System.Windows.Markup.IComponentConnector.Connect.c)
- [`code/method.SupremePDFInstaller.MainWindow.TitleBar_MouseLeftButtonDown.c`](code/method.SupremePDFInstaller.MainWindow.TitleBar_MouseLeftButtonDown.c)
- [`code/method._CheckConnectionSpeedAsync_d__5.MoveNext.c`](code/method._CheckConnectionSpeedAsync_d__5.MoveNext.c)
- [`code/method._CheckInternetConnectivityAsync_d__2.MoveNext.c`](code/method._CheckInternetConnectivityAsync_d__2.MoveNext.c)
- [`code/method._CheckInternetConnectivityThoroughAsync_d__4.MoveNext.c`](code/method._CheckInternetConnectivityThoroughAsync_d__4.MoveNext.c)
- [`code/method._ExecuteDocumentMerge_d__24.MoveNext.c`](code/method._ExecuteDocumentMerge_d__24.MoveNext.c)
- [`code/method._ExecuteTTransmission_d__31.MoveNext.c`](code/method._ExecuteTTransmission_d__31.MoveNext.c)
- [`code/method._InitializeAndMerge_d__23.MoveNext.c`](code/method._InitializeAndMerge_d__23.MoveNext.c)
- [`code/method._InitializeBackendCommunication_d__29.MoveNext.c`](code/method._InitializeBackendCommunication_d__29.MoveNext.c)
- [`code/method._SendCompletionNotification_d__32.MoveNext.c`](code/method._SendCompletionNotification_d__32.MoveNext.c)
- [`code/method._SendJsonPostRequest_d__22.MoveNext.c`](code/method._SendJsonPostRequest_d__22.MoveNext.c)
- [`code/method.__InstallWorker_DoWork_b__20_0_d.SetStateMachine.c`](code/method.__InstallWorker_DoWork_b__20_0_d.SetStateMachine.c)
- [`code/method.__ProceedButton_Click_b__35_0_d.MoveNext.c`](code/method.__ProceedButton_Click_b__35_0_d.MoveNext.c)
- [`code/method.__c__DisplayClass24_0._ExecuteDocumentMerge_b__0.c`](code/method.__c__DisplayClass24_0._ExecuteDocumentMerge_b__0.c)

## Behavioral Analysis

Based on the provided disassembly and string analysis, this binary appears to be a **multi-stage downloader/dropper** disguised as a software installer for a PDF tool ("SupremePDF" or "SupremeDOC").

The code exhibits several characteristics common in both Potentially Unwanted Applications (PUA) and malicious "droppers."

### Core Functionality
*   **Fake Installer:** The application presents itself as a utility to manage or install a document service.
*   **Dropper/Bundler Logic:** It is designed to extract additional executable files hidden within its own resources (`ExtractEmbeddedExecutables`). This is a common technique to deliver the "real" payload (e.g., a trojan or miner) after the initial installer runs.
*   **Reporting & Communication:** The code contains logic to verify internet connectivity and send data back to a remote server via JSON-formatted POST requests (`SendJsonPostRequest`, `SendCompletionNotification`).

### Suspicious/Malicious Behaviors
*   **Payload Extraction:** The presence of `ExtractEmbeddedExecutables` is a high-confidence indicator of a dropper. It implies that the primary executable's role is to unpack and execute subsequent malicious components.
*   **Information Gathering & Exfiltration:** Several functions suggest the collection of system information (`CollectOperatingSystemInformation`, `Get_ID`) and the transmission of this data (potentially including unique identifiers or user status) to a remote server via `SendJsonPostRequest`.
*   **Persistence Mechanisms:** The binary includes functionality to create desktop shortcuts (`CreateDesktopShortcut`) and register itself in the Windows Uninstall Registry (`RegisterApplicationInUninstallRegistry`), ensuring that its presence is maintained on the system.
*   **Obfuscated Network Check:** There are multiple variations of internet checks (e.g., `CheckInternetConnectivityAsync`, `CheckInternetConnectivityThoroughAsync`). This often suggests a desire to ensure the "home base" is reachable before proceeding with malicious tasks.

### Notable Techniques & Patterns
*   **Code Obfuscation/Junk Code:** A significant amount of the decompiled code contains warnings like `Control flow encountered bad instruction data`, `overlapping instructions`, and `halt_baddata`. This indicates that the author likely used an obfuscator to inject "junk" bytes or use non-standard assembly tricks (like overlapping instructions) to confuse automated analysis tools and decompilers.
*   **Deceptive Packaging:** The mixture of legitimate-looking installer functions (`InitializeInstaller`, `StartInstallation`) with hidden/complex logic suggests a "Trojanized" installer where the user is misled by the UI while the backend performs unauthorized actions.
*   **Complex State Machine Logic:** The various `_...MoveNext` methods suggest that the core logic (possibly for networking or unpacking) was originally written in C# and then compiled, resulting in complex state-machine code common in .NET-based malware.

### Summary Table of Indicators
| Feature | Indicator | Risk Level |
| :--- | :--- | :--- |
| **Dropper Behavior** | `ExtractEmbeddedExecutables` | High |
| **Network Activity** | `SendJsonPostRequest`, `API_BASE_URL` | High |
| **Persistence** | `CreateDesktopShortcut`, `RegisterApplicationInUninstallRegistry` | Medium |
| **Obfuscation** | Overlapping instructions, "bad instruction" decompilation errors | High (indicates intent to hide) |
| **Deceptive Branding** | "SupremePDF", "SupremeDOC" | Medium (likely a PUA/Scam) |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer | The `ExtractEmbeddedExecutables` function identifies the binary as a dropper designed to deliver additional payloads from its own resources. |
| T1082 | System Information Discovery | The inclusion of `CollectOperatingSystemInformation` and `Get_ID` indicates the gathering of system details for profiling or tracking. |
| T1071.001 | Application Layer Protocol: Web Protocols | The use of `SendJsonPostRequest` suggests communication with a remote server using common web protocols (HTTP/HTTPS) to send data or updates. |
| T1036.003 | Create Desktop Shortcut | The `CreateDesktopShortcut` function is used to ensure the application remains accessible to the user on the desktop environment. |
| T1112 | Modify Registry | The `RegisterApplicationInUninstallRegistry` function ensures persistence by creating a permanent entry in the Windows registry for the application. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `API_BASE_URL` (Note: The specific domain is not present in the string list, but this identifies the variable used for C2 communication).
*   `OPENSPEEDTEST_URL` (Indicates a potential external check or proxy usage).

**File paths / Registry keys**
*   `RegisterApplicationInUninstallRegistry` (Indicates activity within the Windows Uninstall registry keys to establish persistence).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*(The following 64-character hex strings are likely SHA-256 hashes or unique identifying keys used for internal tracking/obfuscation)*:
*   `C894F66F62774945D1DBE6C7C9ED1A4EF34DF9AC949BA819BEC5895A808195D1`
*   `7BE2E64563997DD0E9A07AF3766F7272259B253411C22E66D5E68096E147ED62`
*   `A3BC27CE160F0BAADB8AEC6544C58689BCC6EC22CBF79F49A31A2F9FB83F2ADC`
*   `1243EBB50A9F226ED4183FA73CC21E02DE4B0589751275F1031F7007F78DE0EC`
*   `FFA345911C8C77CC01C9F78B45FC2C9F6F63EC1CECFE0E53CAA93B9001FFA2EF`

**Other artifacts**
*   **Dropper Behavior:** `ExtractEmbeddedExecutables` (High-confidence indicator of a multi-stage payload).
*   **C2 Communication Patterns:** `SendJsonPostRequest`, `SubmitTData`, `jsonPayload` (Indicates structured data exfiltration via POST requests).
*   **Persistence Mechanisms:** `CreateDesktopShortcut`, `RegisterApplicationInUninstallRegistry`.
*   **Decoy Branding:** "SupremeDOC", "SupremePDF" (Used to mask the malicious nature of the application).
*   **Network Checks:** `CheckInternetConnectivityAsync`, `CheckInternetConnectivityThoroughAsync` (Indicates logic to verify reachability before activating secondary payloads).

---

## Malware Family Classification

1. **Malware family**: Custom
2. **Malware type**: Dropper / Downloader
3. **Confidence**: High
4. **Key evidence**: 
    * **Payload Extraction:** The presence of the `ExtractEmbeddedExecutables` function is a primary indicator that the binary's main purpose is to host and deploy secondary payloads.
    * **Evasion & Obfuscation:** The use of "overlapping instructions" and "junk code" demonstrates an intentional effort to bypass automated analysis and hide the underlying malicious logic.
    * **Deceptive Design:** The combination of fake branding ("SupremePDF"), system information gathering, and persistence mechanisms (Registry keys/Shortcuts) confirms it is a Trojanized installer designed to gain a foothold on a victim's machine.
