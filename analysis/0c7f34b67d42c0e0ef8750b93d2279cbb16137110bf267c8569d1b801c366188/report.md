# Threat Analysis Report

**Generated:** 2026-07-31 15:09 UTC
**Sample:** `0c7f34b67d42c0e0ef8750b93d2279cbb16137110bf267c8569d1b801c366188_0c7f34b67d42c0e0ef8750b93d2279cbb16137110bf267c8569d1b801c366188.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c7f34b67d42c0e0ef8750b93d2279cbb16137110bf267c8569d1b801c366188_0c7f34b67d42c0e0ef8750b93d2279cbb16137110bf267c8569d1b801c366188.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,063,120 bytes |
| MD5 | `b6c5b9ea469cb955f37ab9bc5699b84c` |
| SHA1 | `75245900bfdf89bd4603643dfac360a8175ded85` |
| SHA256 | `0c7f34b67d42c0e0ef8750b93d2279cbb16137110bf267c8569d1b801c366188` |
| Overall entropy | 5.663 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4092151228 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 941,056 | 5.787 | No |
| `.rsrc` | 109,568 | 3.641 | No |

## Extracted Strings

Total strings found: **6247** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

X )UU

X )UU

X )UU

,p	oF
v4.0.30319
#Strings
<>o__10
<>p__10
__StaticArrayInitTypeSize=20
<>p__20
<InitializeAndMerge>d__30
<>p__30
__StaticArrayInitTypeSize=40
<ExecuteTTransmission>d__40
<>p__40
<>9__20_0
<BP>b__20_0
<InstallWorker_RunWorkerCompleted>b__40_0
<HideQuitDialog>b__50_0
<>9__21_0
<TerStractureProcess>b__21_0
<TransitionToInstalling>b__31_0
<HideAndRunBackgroundTasks>b__41_0
<>9__32_0
<BS>b__32_0
<>c__DisplayClass32_0
<ProceedButton_Click>b__52_0
<>c__DisplayClass13_0
<AnimateAndClose>b__43_0
<>c__DisplayClass14_0
<InstallWorker_DoWork>b__34_0
<>c__DisplayClass35_0
<>9__36_0
<InstallWorker_ProgressChanged>b__36_0
<>9__6_0
<RunScheduledTask>b__6_0
<ShowEncouragementMessage>b__39_0
<ExecuteDocumentMerge>b__0
<DecryptValue>b__0
<EncryptValue>b__0
<StartInstallation>b__0
<ExtractEmbeddedExecutables>b__0
<>p__0
<>o__11
<>p__11
<>p__21
<>p__31
<SendCompletionNotification>d__41
<>p__41
C894F66F62774945D1DBE6C7C9ED1A4EF34DF9AC949BA819BEC5895A808195D1
get_SD1
<InstallWorker_RunWorkerCompleted>b__40_1
<>9__41_1
<HideAndRunBackgroundTasks>b__41_1
<ProceedButton_Click>b__52_1
<AnimateAndClose>b__43_1
<InstallWorker_DoWork>b__34_1
<>9__1
<ExecuteDocumentMerge>b__1
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
<>p__12
<>p__22
<>p__32
Microsoft.Win32
<>p__42
7BE2E64563997DD0E9A07AF3766F7272259B253411C22E66D5E68096E147ED62
get_SD2
<>9__43_2
<AnimateAndClose>b__43_2
<InstallWorker_DoWork>b__34_2
<sessionConfiguration>5__2
<progress>5__2
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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__RunScheduledTask_b__6_0_d.SetStateMachine` | `0x140008e20` | 43470 | ✓ |
| `method.SupremePDFInstaller.TaskSchedulerService.CreateDailyTask` | `0x140003bd8` | 3924 | ✓ |
| `method.__c__DisplayClass35_0._ExecuteDocumentMerge_b__0` | `0x140007334` | 1176 | ✓ |
| `method._InitializeAndMerge_d__30.MoveNext` | `0x140007900` | 1064 | ✓ |
| `method.SupremePDFInstaller.TaskSchedulerService.TaskExists` | `0x140004d64` | 888 | ✓ |
| `method.SupremeDOC.SystemUtilities.CreateDesktopShortcut` | `0x140003504` | 864 | ✓ |
| `method.SupremePDFInstaller.MainWindow.InstallWorker_DoWork` | `0x1400057e4` | 812 | ✓ |
| `method._ExecuteTTransmission_d__40.MoveNext` | `0x140006774` | 756 | ✓ |
| `method.SupremeDOC.TManager.IsChreInstalled` | `0x140002958` | 592 | ✓ |
| `method._InitializeBackendCommunication_d__38.MoveNext` | `0x140006a78` | 576 | ✓ |
| `method._CheckConnectionSpeedAsync_d__5.MoveNext` | `0x140008048` | 576 | ✓ |
| `method.SupremePDFInstaller.TaskSchedulerService.RemoveTask` | `0x140004b2c` | 568 | ✓ |
| `method._SendCompletionNotification_d__41.MoveNext` | `0x140006f38` | 468 | ✓ |
| `method.__ExecuteDocumentMerge_b__1_d.MoveNext` | `0x140008b74` | 464 | ✓ |
| `method.SupremePDFInstaller.MainWindow.ExtractEmbeddedExecutables` | `0x140005b10` | 460 | ✓ |
| `method._CheckInternetConnectivityThoroughAsync_d__4.MoveNext` | `0x1400083e8` | 448 | ✓ |
| `method._SendJsonPostRequest_d__23.MoveNext` | `0x140007d38` | 416 | ✓ |
| `method.SupremePDFInstaller.MainWindow.StartInstallation` | `0x140005600` | 408 | ✓ |
| `method._SubmitJsonPayloadAsync_d__33.MoveNext` | `0x14000711c` | 392 | ✓ |
| `method.SupremeDOC.SystemUtilities.IsSupportedUser` | `0x140003990` | 368 | ✓ |
| `method.SupremePDFInstaller.MainWindow.System.Windows.Markup.IComponentConnector.Connect` | `0x14000635c` | 352 | ✓ |
| `method.SupremePDFInstaller.MainWindow.InstallWorker_RunWorkerCompleted` | `0x140005f2c` | 332 | ✓ |
| `method._CheckInternetConnectivityAsync_d__2.MoveNext` | `0x140008298` | 320 | ✓ |
| `method._ReportOperationTelemetryAsync_d__37.MoveNext` | `0x140006dec` | 316 | ✓ |
| `method.__InstallWorker_DoWork_b__34_0_d.MoveNext` | `0x1400085b8` | 312 | ✓ |
| `method.__InstallWorker_DoWork_b__34_2_d.MoveNext` | `0x1400087f4` | 284 | ✓ |
| `method._ReportAuthStatusAsync_d__36.MoveNext` | `0x140006cc8` | 276 | ✓ |
| `method.SupremePDFInstaller.MainWindow.ProgressTimer_Tick` | `0x140005d2c` | 272 | ✓ |
| `method.SupremeDOC.SystemUtilities.RegisterApplicationInUninstallRegistry` | `0x140003864` | 268 | ✓ |
| `method._RunScheduledTask_d__6.MoveNext` | `0x140007f38` | 256 | ✓ |

### Decompiled Code Files

- [`code/method.SupremeDOC.SystemUtilities.CreateDesktopShortcut.c`](code/method.SupremeDOC.SystemUtilities.CreateDesktopShortcut.c)
- [`code/method.SupremeDOC.SystemUtilities.IsSupportedUser.c`](code/method.SupremeDOC.SystemUtilities.IsSupportedUser.c)
- [`code/method.SupremeDOC.SystemUtilities.RegisterApplicationInUninstallRegistry.c`](code/method.SupremeDOC.SystemUtilities.RegisterApplicationInUninstallRegistry.c)
- [`code/method.SupremeDOC.TManager.IsChreInstalled.c`](code/method.SupremeDOC.TManager.IsChreInstalled.c)
- [`code/method.SupremePDFInstaller.MainWindow.ExtractEmbeddedExecutables.c`](code/method.SupremePDFInstaller.MainWindow.ExtractEmbeddedExecutables.c)
- [`code/method.SupremePDFInstaller.MainWindow.InstallWorker_DoWork.c`](code/method.SupremePDFInstaller.MainWindow.InstallWorker_DoWork.c)
- [`code/method.SupremePDFInstaller.MainWindow.InstallWorker_RunWorkerCompleted.c`](code/method.SupremePDFInstaller.MainWindow.InstallWorker_RunWorkerCompleted.c)
- [`code/method.SupremePDFInstaller.MainWindow.ProgressTimer_Tick.c`](code/method.SupremePDFInstaller.MainWindow.ProgressTimer_Tick.c)
- [`code/method.SupremePDFInstaller.MainWindow.StartInstallation.c`](code/method.SupremePDFInstaller.MainWindow.StartInstallation.c)
- [`code/method.SupremePDFInstaller.MainWindow.System.Windows.Markup.IComponentConnector.Connect.c`](code/method.SupremePDFInstaller.MainWindow.System.Windows.Markup.IComponentConnector.Connect.c)
- [`code/method.SupremePDFInstaller.TaskSchedulerService.CreateDailyTask.c`](code/method.SupremePDFInstaller.TaskSchedulerService.CreateDailyTask.c)
- [`code/method.SupremePDFInstaller.TaskSchedulerService.RemoveTask.c`](code/method.SupremePDFInstaller.TaskSchedulerService.RemoveTask.c)
- [`code/method.SupremePDFInstaller.TaskSchedulerService.TaskExists.c`](code/method.SupremePDFInstaller.TaskSchedulerService.TaskExists.c)
- [`code/method._CheckConnectionSpeedAsync_d__5.MoveNext.c`](code/method._CheckConnectionSpeedAsync_d__5.MoveNext.c)
- [`code/method._CheckInternetConnectivityAsync_d__2.MoveNext.c`](code/method._CheckInternetConnectivityAsync_d__2.MoveNext.c)
- [`code/method._CheckInternetConnectivityThoroughAsync_d__4.MoveNext.c`](code/method._CheckInternetConnectivityThoroughAsync_d__4.MoveNext.c)
- [`code/method._ExecuteTTransmission_d__40.MoveNext.c`](code/method._ExecuteTTransmission_d__40.MoveNext.c)
- [`code/method._InitializeAndMerge_d__30.MoveNext.c`](code/method._InitializeAndMerge_d__30.MoveNext.c)
- [`code/method._InitializeBackendCommunication_d__38.MoveNext.c`](code/method._InitializeBackendCommunication_d__38.MoveNext.c)
- [`code/method._ReportAuthStatusAsync_d__36.MoveNext.c`](code/method._ReportAuthStatusAsync_d__36.MoveNext.c)
- [`code/method._ReportOperationTelemetryAsync_d__37.MoveNext.c`](code/method._ReportOperationTelemetryAsync_d__37.MoveNext.c)
- [`code/method._RunScheduledTask_d__6.MoveNext.c`](code/method._RunScheduledTask_d__6.MoveNext.c)
- [`code/method._SendCompletionNotification_d__41.MoveNext.c`](code/method._SendCompletionNotification_d__41.MoveNext.c)
- [`code/method._SendJsonPostRequest_d__23.MoveNext.c`](code/method._SendJsonPostRequest_d__23.MoveNext.c)
- [`code/method._SubmitJsonPayloadAsync_d__33.MoveNext.c`](code/method._SubmitJsonPayloadAsync_d__33.MoveNext.c)
- [`code/method.__ExecuteDocumentMerge_b__1_d.MoveNext.c`](code/method.__ExecuteDocumentMerge_b__1_d.MoveNext.c)
- [`code/method.__InstallWorker_DoWork_b__34_0_d.MoveNext.c`](code/method.__InstallWorker_DoWork_b__34_0_d.MoveNext.c)
- [`code/method.__InstallWorker_DoWork_b__34_2_d.MoveNext.c`](code/method.__InstallWorker_DoWork_b__34_2_d.MoveNext.c)
- [`code/method.__RunScheduledTask_b__6_0_d.SetStateMachine.c`](code/method.__RunScheduledTask_b__6_0_d.SetStateMachine.c)
- [`code/method.__c__DisplayClass35_0._ExecuteDocumentMerge_b__0.c`](code/method.__c__DisplayClass35_0._ExecuteDocumentMerge_b__0.c)

## Behavioral Analysis

Based on my analysis of the provided strings and decompiled code, this binary is a **sophisticated multi-stage downloader/dropper** disguised as legitimate software (likely related to document or PDF processing).

The presence of heavy obfuscation in the disassembly suggests an intentional attempt to hinder analysis by security tools and researchers.

### Core Functionality
The program acts as an "installer" for a product named **SupremeDOC** or **SupremePDF**. Its primary role is to prepare the environment, verify connectivity, extract hidden components, and establish persistence on the host system.

### Suspicious & Malicious Behaviors
*   **Payload Dropping:** The function `ExtractEmbeddedExecutables` indicates that the binary contains other executables within its own resources. This is a classic technique for "droppers" to deliver secondary malware (e.g., info-stealers, miners, or ransomware) after the initial execution.
*   **Persistence Mechanisms:** 
    *   The code includes `RunScheduledTask` and `CreateDailyTask`. These are used to ensure that the malicious components execute automatically on a recurring basis.
    *   It also attempts to interact with the Windows Registry via `RegisterApplicationInUninstallRegistry`, which makes the "installation" appear legitimate to the user while ensuring it remains accessible in the system.
*   **Network Communication (C2/Telemetry):**
    *   The program performs several pre-flight checks before communicating, including `CheckInternetConnectivityAsync` and `CheckConnectionSpeedAsync`.
    *   Functions like `SubmitJsonPayloadAsync`, `SendJsonPostRequest`, and `ReportOperationTelemetryAsync` indicate that the malware "phones home" to a Command & Control (C2) server. It likely sends system information or stolen data as JSON-formatted packets.
    *   The function `ReportAuthStatusAsync` may be checking for administrative privileges or other environment details before proceeding with its routine.
*   **Credential/Data Obfuscation:** The presence of `DecryptValue` and `EncryptValue` suggests that sensitive strings (such as C2 URLs, IP addresses, or hardcoded keys) are encrypted within the binary to evade simple static analysis.

### Notable Techniques & Patterns
*   **Control-Flow Obfuscation:** The disassembly is riddled with "bad instruction" warnings and complex mathematical operations on memory offsets (e.g., `POPCOUNT`, `CONCAT` macros). This indicates the use of a **packer or obfuscator** (such as OLLVM) designed to break the logic flow of the decompiler, making it difficult to follow the execution path without manual effort.
*   **Deceptive Naming:** The code uses "professional" naming conventions like `SystemUtilities`, `ReportOperationTelemetry`, and `IdentifySoftware` to mimic legitimate software behavior, a common tactic used by threat actors to blend in with valid processes during forensic investigation.
*   **Multi-Stage Execution:** The naming of the various "Workers" (e.g., `InstallWorker_DoWork`) and "Phases" suggests a state-machine architecture where the program performs different actions sequentially, moving from preparation to extraction to persistence.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of `DecryptValue`/`EncryptValue` functions and OLLVM-style control-flow obfuscation indicates an intent to hide strings and execution logic from analysis. |
| **T1053.005** | Scheduled Task | The presence of `RunScheduledTask` and `CreateDailyTask` functions confirms the use of scheduled tasks to maintain persistence on the host. |
| **T1112** | Modify Registry | The binary interacts with the Windows Registry via `RegisterApplicationInUninstallRegistry` to establish persistence and mimic a legitimate installation. |
| **T1036** | Masquerading | The use of "professional" naming conventions (e.g., `SystemUtilities`) and a fake product name (`SupremeDOC`) is intended to blend in with legitimate software. |
| **T1071** | Application Layer Protocol | The use of `SendJsonPostRequest` and `ReportOperationTelemetryAsync` indicates the malware communicates with C2 servers using standard application-layer protocols (likely HTTP/S). |
| **T1547.001** | JavaScript/VBScript (or similar) / Dropper behavior* | While not a single ID, the extraction of embedded executables via `ExtractEmbeddedExecutables` identifies the binary as a classic dropper/downloader for multi-stage execution. |

*\*Note: While "Dropper" is an adversary tactic, the specific action of extracting and executing hidden components from internal resources is often categorized under broader execution or delivery techniques depending on the final payload's nature.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

### **IP addresses / URLs / Domains**
*   **Note:** No literal IP addresses or domains were found in the raw strings. However, the following internal variables indicate where these values are stored/used within the binary:
    *   `PRE_BASE_URL`
    *   `API_BASE_URL`
    *   `PER_BASE_URL`
    *   `OPENSPEEDTEST_URL`

### **File paths / Registry keys**
*   **Registry Interaction:** The binary interacts with the Windows Registry specifically for uninstallation management (`RegisterApplicationInUninstallRegistry`).
*   **Note:** No specific, hardcoded file paths (e.g., `C:\Windows\...`) were identified in the provided strings.

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
The following high-entropy hex strings appear in the sample. While they may function as internal encryption keys or seeds for the `DecryptValue` and `EncryptValue` functions, they are unique identifiers within the binary:
*   `C894F66F62774945D1DBE6C7C9ED1A4EF34DF9AC949BA819BEC5895A808195D1`
*   `7BE2E64563997DD0E9A07AF3766F7272259B253411C22E66D5E68096E147ED62`
*   `A3BC27CE160F0BAADB8AEC6544C58689BCC6EC22CBF79F49A31A2F9FB83F2ADC`
*   `1243EBB50A9F226ED4183FA73CC21E02DE4B0589751275F1031F7007F78DE0EC`
*   `FFA345911C8C77CC01C9F78B45FC2C9F6F63EC1CECFE0E53CAA93B9001FFA2EF`

### **Other artifacts**
*   **Malware Branding:** `SupremeDOC`, `SupremePDF` (Used to mask the application's true purpose).
*   **C2 Communication Patterns:** 
    *   `SubmitJsonPayloadAsync` (Indicates JSON-formatted exfiltration/heartbeats)
    *   `SendJsonPostRequest` (HTTP POST method for C2 communication)
    *   `ReportOperationTelemetryAsync` (Potential data exfiltration routine)
    *   `ReportAuthStatusAsync` (Environment/Privilege checking)
*   **Persistence Mechanisms:** 
    *   `RunScheduledTask`
    *   `CreateDailyTask`
*   **Dropper Functionality:** 
    *   `ExtractEmbeddedExecutables` (Indicates the presence of hidden payloads).
*   **Pre-flight Network Checks:** 
    *   `CheckInternetConnectivityAsync`
    *   `CheckConnectionSpeedAsync`
    *   `CheckInternetConnectivityOnStartup`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High

4. **Key evidence**:
*   **Explicit Dropper Behavior:** The inclusion of the `ExtractEmbeddedExecutables` function and a multi-stage "Worker/Phase" architecture confirms its primary role is to unpack and execute secondary malicious payloads hidden within its own resources.
*   **Sophisticated Evasion & Persistence:** The use of OLLVM-style control-flow obfuscation, encrypted internal strings (C2 URLs), and the creation of Scheduled Tasks/Registry keys indicate a professional design intended to evade detection while maintaining a long-term presence on the host.
*   **Masquerading Tactics:** The use of "professional" naming conventions (`SystemUtilities`, `ReportOperationTelemetry`) and fake product branding (`SupremeDOC`/`SupremePDF`) are classic indicators of malware designed to blend in with legitimate software during initial infection.
