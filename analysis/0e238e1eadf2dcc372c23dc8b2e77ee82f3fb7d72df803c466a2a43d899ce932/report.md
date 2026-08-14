# Threat Analysis Report

**Generated:** 2026-08-11 18:31 UTC
**Sample:** `0e238e1eadf2dcc372c23dc8b2e77ee82f3fb7d72df803c466a2a43d899ce932_0e238e1eadf2dcc372c23dc8b2e77ee82f3fb7d72df803c466a2a43d899ce932.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e238e1eadf2dcc372c23dc8b2e77ee82f3fb7d72df803c466a2a43d899ce932_0e238e1eadf2dcc372c23dc8b2e77ee82f3fb7d72df803c466a2a43d899ce932.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 19,047,640 bytes |
| MD5 | `87b124f44a077675ad9cbc58e353f543` |
| SHA1 | `2eb6e03a51069f22b56d0c8aadd406c735020c13` |
| SHA256 | `0e238e1eadf2dcc372c23dc8b2e77ee82f3fb7d72df803c466a2a43d899ce932` |
| Overall entropy | 7.99 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4294011290 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 19,014,656 | 7.991 | ⚠️ Yes |
| `.rsrc` | 20,480 | 4.336 | No |

## Extracted Strings

Total strings found: **42551** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

&+N	-B
v4.0.30319
#Strings
	*	]	j	
__StaticArrayInitTypeSize=10
8AE2AA28BDE162C0233C2C2F7BD5EC39EAD36EFAD2C4BA2411C8638DAD7904F0
<>9__10_0
<ParseComplexTypeByType>b__10_0
<>c__DisplayClass10_0
<>c__DisplayClass11_0
<>9__1_0
<TransformComplexType>b__1_0
<>c__DisplayClass1_0
<>9__12_0
<LaunchApplication>b__12_0
<>c__DisplayClass12_0
<>c__DisplayClass13_0
<>c__DisplayClass14_0
<InstallAsync>b__4_0
<.cctor>b__4_0
<>c__DisplayClass4_0
<>9__6_0
<ParseComplexType>b__6_0
<>9__8_0
<CalculateInstallationSize>b__8_0
<>9__0
<OnInstallProgressChanged>b__0
<Obfuscate>b__0
<Deobfuscate>b__0
<ProcessSyncOperation>b__0
<CloseRunningInstances>b__0
<OnStartup>d__0
<StartInstallation>d__11
CD9CB809DF131FE1886468DD6D616F109D4F5D10805E0ECB051051BC33615291
<>9__10_1
<ParseComplexTypeByType>b__10_1
<InstallAsync>b__4_1
<>9__6_1
<ParseComplexType>b__6_1
<TransformComplexType>b__1
<>u__1
<>c__6`1
Func`1
Nullable`1
IEnumerable`1
ConfiguredTaskAwaitable`1
Task`1
ReadOnlyCollection`1
AsyncTaskMethodBuilder`1
EventHandler`1
TaskAwaiter`1
IEnumerator`1
List`1
Lazy`1
get_Item1
<TransmitAsync>d__12
Microsoft.Win32
<>9__10_2
<ParseComplexTypeByType>b__10_2
<InstallAsync>b__4_2
<>9__6_2
<ParseComplexType>b__6_2
<suc>5__2
<passed>5__2
<outcomes>5__2
<syncSettings>5__2
<>u__2
Func`2
Tuple`2
KeyValuePair`2
Dictionary`2
get_Item2
<InstallAsync>b__4_3
<networkTask>5__3
<activeProfileSecondaryDestination>5__3
<>u__3
Func`3
<ProcessSyncOperation>d__14
ToBase64
<activeProfileVerificationToken>5__4
<InstallAsync>b__4
<InstallAsync>d__4
<InitializeAppAsync>d__4
<>u__4
<activeProfileId>5__5
<MainWindow_Closing>d__5
<LogInstallationSuccessAsync>d__6
<ReportTelemetryAsync>d__17
<ReportMetricsAsync>d__18
get_UTF8
<Hyperlink_RequestNavigate>d__8
<EstablishConnection>d__19
<Module>
<PrivateImplementationDetails>
pClassID
GetClassID
STATUS_COMPLETE
get_ASCII
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__ProcessSyncOperation_b__0_d.SetStateMachine` | `0x140007280` | 40466 | ✓ |
| `method._InstallAsync_d__4.MoveNext` | `0x140006500` | 1916 | ✓ |
| `method.__ProcessSyncOperation_b__0_d.MoveNext` | `0x140006c8c` | 1524 | ✓ |
| `method._EstablishConnection_d__19.MoveNext` | `0x1400057d4` | 844 | ✓ |
| `method.AllFiles.utilities.ApiService.LogUserActionSync` | `0x140002f3c` | 840 | ✓ |
| `method._StartInstallation_d__11.MoveNext` | `0x140005484` | 580 | ✓ |
| `method.AllFiles.utilities.ApiService.GetOsTypeName` | `0x14000341c` | 536 | ✓ |
| `method._InitializeAppAsync_d__4.MoveNext` | `0x140005fa4` | 444 | ✓ |
| `method.AllFiles.utilities.DataSerializer.FromJsonString` | `0x140003a08` | 416 | ✓ |
| `method._ReportMetricsAsync_d__18.MoveNext` | `0x140005b30` | 404 | ✓ |
| `method.AllFiles.utilities.DataSerializer.ParseComplexType` | `0x140003ba8` | 372 | ✓ |
| `method.AllFiles.utilities.DataSerializer.ParseComplexTypeByType` | `0x140004018` | 356 | ✓ |
| `method._TransmitAsync_d__12.MoveNext` | `0x140005e14` | 356 | ✓ |
| `method.AllFiles.utilities.DataSerializer.TransformValue` | `0x140003e08` | 324 | ✓ |
| `method.AllFiles.utilities.FileOperationManager.ExtractJsonValue` | `0x14000478c` | 324 | ✓ |
| `method.AllFiles.utilities.FileOperationManager.ParseNestedArray` | `0x1400043b4` | 320 | ✓ |
| `method.AllFiles.utilities.InstallerService.ExtractZipFile` | `0x140004d00` | 312 | ✓ |
| `method._ReportTelemetryAsync_d__17.MoveNext` | `0x140005cd4` | 304 | ✓ |
| `method._OnStartup_d__0.MoveNext` | `0x14000527c` | 288 | ✓ |
| `method.AllFiles.utilities.FileOperationManager.LaunchApplication` | `0x1400044f4` | 280 | ✓ |
| `method._ProcessSyncOperation_d__14.MoveNext` | `0x1400063a8` | 276 | ✓ |
| `method._LogInstallationSuccessAsync_d__6.MoveNext` | `0x140006170` | 272 | ✓ |
| `method.AllFiles.utilities.DataSerializer.ToJsonString` | `0x140003730` | 268 | ✓ |
| `method.AllFiles.utilities.NetworkBridge.CompileStatusReport` | `0x140002ad8` | 252 | ✓ |
| `method.AllFiles.utilities.InstallerService.RegisterUninstaller` | `0x140004ebc` | 248 | ✓ |
| `method.AllFiles.utilities.DataSerializer.ExtractSegments` | `0x140003d1c` | 236 | ✓ |
| `method.AllFiles.utilities.InstallerService.IsChromeInstalled` | `0x1400050dc` | 230 | ✓ |
| `method.AllFiles.utilities.NetworkBridge.EvaluateOutcomes` | `0x140002a00` | 216 | ✓ |
| `method.AllFiles.utilities.DataSerializer.ParseTypedArray` | `0x140003f4c` | 204 | ✓ |
| `method.AllFiles.utilities.NetworkBridge.CompileProfileReport` | `0x140002bd4` | 200 | ✓ |

### Decompiled Code Files

- [`code/method.AllFiles.utilities.ApiService.GetOsTypeName.c`](code/method.AllFiles.utilities.ApiService.GetOsTypeName.c)
- [`code/method.AllFiles.utilities.ApiService.LogUserActionSync.c`](code/method.AllFiles.utilities.ApiService.LogUserActionSync.c)
- [`code/method.AllFiles.utilities.DataSerializer.ExtractSegments.c`](code/method.AllFiles.utilities.DataSerializer.ExtractSegments.c)
- [`code/method.AllFiles.utilities.DataSerializer.FromJsonString.c`](code/method.AllFiles.utilities.DataSerializer.FromJsonString.c)
- [`code/method.AllFiles.utilities.DataSerializer.ParseComplexType.c`](code/method.AllFiles.utilities.DataSerializer.ParseComplexType.c)
- [`code/method.AllFiles.utilities.DataSerializer.ParseComplexTypeByType.c`](code/method.AllFiles.utilities.DataSerializer.ParseComplexTypeByType.c)
- [`code/method.AllFiles.utilities.DataSerializer.ParseTypedArray.c`](code/method.AllFiles.utilities.DataSerializer.ParseTypedArray.c)
- [`code/method.AllFiles.utilities.DataSerializer.ToJsonString.c`](code/method.AllFiles.utilities.DataSerializer.ToJsonString.c)
- [`code/method.AllFiles.utilities.DataSerializer.TransformValue.c`](code/method.AllFiles.utilities.DataSerializer.TransformValue.c)
- [`code/method.AllFiles.utilities.FileOperationManager.ExtractJsonValue.c`](code/method.AllFiles.utilities.FileOperationManager.ExtractJsonValue.c)
- [`code/method.AllFiles.utilities.FileOperationManager.LaunchApplication.c`](code/method.AllFiles.utilities.FileOperationManager.LaunchApplication.c)
- [`code/method.AllFiles.utilities.FileOperationManager.ParseNestedArray.c`](code/method.AllFiles.utilities.FileOperationManager.ParseNestedArray.c)
- [`code/method.AllFiles.utilities.InstallerService.ExtractZipFile.c`](code/method.AllFiles.utilities.InstallerService.ExtractZipFile.c)
- [`code/method.AllFiles.utilities.InstallerService.IsChromeInstalled.c`](code/method.AllFiles.utilities.InstallerService.IsChromeInstalled.c)
- [`code/method.AllFiles.utilities.InstallerService.RegisterUninstaller.c`](code/method.AllFiles.utilities.InstallerService.RegisterUninstaller.c)
- [`code/method.AllFiles.utilities.NetworkBridge.CompileProfileReport.c`](code/method.AllFiles.utilities.NetworkBridge.CompileProfileReport.c)
- [`code/method.AllFiles.utilities.NetworkBridge.CompileStatusReport.c`](code/method.AllFiles.utilities.NetworkBridge.CompileStatusReport.c)
- [`code/method.AllFiles.utilities.NetworkBridge.EvaluateOutcomes.c`](code/method.AllFiles.utilities.NetworkBridge.EvaluateOutcomes.c)
- [`code/method._EstablishConnection_d__19.MoveNext.c`](code/method._EstablishConnection_d__19.MoveNext.c)
- [`code/method._InitializeAppAsync_d__4.MoveNext.c`](code/method._InitializeAppAsync_d__4.MoveNext.c)
- [`code/method._InstallAsync_d__4.MoveNext.c`](code/method._InstallAsync_d__4.MoveNext.c)
- [`code/method._LogInstallationSuccessAsync_d__6.MoveNext.c`](code/method._LogInstallationSuccessAsync_d__6.MoveNext.c)
- [`code/method._OnStartup_d__0.MoveNext.c`](code/method._OnStartup_d__0.MoveNext.c)
- [`code/method._ProcessSyncOperation_d__14.MoveNext.c`](code/method._ProcessSyncOperation_d__14.MoveNext.c)
- [`code/method._ReportMetricsAsync_d__18.MoveNext.c`](code/method._ReportMetricsAsync_d__18.MoveNext.c)
- [`code/method._ReportTelemetryAsync_d__17.MoveNext.c`](code/method._ReportTelemetryAsync_d__17.MoveNext.c)
- [`code/method._StartInstallation_d__11.MoveNext.c`](code/method._StartInstallation_d__11.MoveNext.c)
- [`code/method._TransmitAsync_d__12.MoveNext.c`](code/method._TransmitAsync_d__12.MoveNext.c)
- [`code/method.__ProcessSyncOperation_b__0_d.MoveNext.c`](code/method.__ProcessSyncOperation_b__0_d.MoveNext.c)
- [`code/method.__ProcessSyncOperation_b__0_d.SetStateMachine.c`](code/method.__ProcessSyncOperation_b__0_d.SetStateMachine.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's functionality:

### Core Functionality
The binary appears to be a **downloader/installer** designed to deploy a software component or service onto a host system. It utilizes several distinct phases typical of modern malware delivery:
*   **Installation Logic:** The presence of `InstallAsync`, `RegisterUninstaller`, and `StartInstallation` suggests the primary purpose is to install a "suite" or "application."
*   **Data Serialization/Extraction:** It uses JSON parsing (`FromJsonString`) and ZIP extraction (`ExtractZipFile`), implying that it receives instructions or additional modules in compressed/encoded formats from a remote server.
*   **System Profiling:** The code includes methods like `CompileProfileReport` and `GetMachineGuid`, which are used to gather information about the host machine (fingerprinting).

### Suspicious & Malicious Behaviors
The following behaviors are highly indicative of malicious intent:

*   **Information Gathering & Exfiltration:**
    *   The inclusion of `ReportTelemetryAsync`, `ReportMetricsAsync`, and `LogUserActionSync` suggests the program tracks user activity and sends system statistics back to a remote server.
    *   `CompileProfileReport` likely bundles system metadata (OS type, hardware IDs, etc.) to be sent to a Command & Control (C2) infrastructure.
*   **Dropper/Loader Behavior:**
    *   The `ExtractZipFile` function is a common indicator of a "dropper." It suggests the initial binary is just a wrapper used to unpack and execute further malicious components or persistence modules.
*   **Command & Control (C2) Communication:**
    *   Explicitly named endpoints such as `BOOTSTRAP_ENDPOINT`, `METRICS_ENDPOINT`, `TELEMETRY_ENDPOINT`, and `SUCCESS_API_URL` indicate a structured communication protocol with a remote server to report success, receive updates, or download further tasks.
*   **Environment Checking:**
    *   The function `IsChromeInstalled` is often used by "browser hijackers" or malware that targets specific web-based features/extensions.

### Notable Techniques & Patterns
*   **Obfuscation & Anti-Analysis:** 
    *   The disassembled code contains numerous "warning" flags (e.g., *control flow encountered bad instruction data*, *overlapping instructions*). This is a strong indicator that the binary has been **intentionally obfuscated** to break decompilers and frustrate manual analysis.
    *   The presence of `Obfuscate` and `Deobfuscate` functions in the string list confirms that the code handles internal encryption/encoding for its communication or payload strings.
*   **Evidence of Managed Origin:** 
    *   The presence of `.NET` artifacts (e.g., `mscorlib`, `System.Runtime`, `AsyncTaskMethodBuilder`) suggests the original source was a .NET application. It may have been converted to native code via a tool like IL2CPP or was heavily packed/protected before being compiled into its current state.
*   **Network Bridge Pattern:** 
    *   The "NetworkBridge" class name and methods like `EstablishConnection` and `TransmitAsync` indicate a modular architecture where network operations are abstracted, common in both legitimate software installers and sophisticated malware for managing C2 traffic.

### Summary
This is likely a **malware dropper or an installer for a potentially unwanted program (PUP)**. It performs system fingerprinting, extracts additional components from compressed archives, and communicates with remote servers to report success and gather telemetry. The heavy use of anti-decompilation techniques suggests it is designed to evade automated analysis tools.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information or Network Traffic | The use of "bad instruction" data, overlapping instructions, and explicit `Obfuscate` functions indicates an attempt to hinder manual analysis and bypass security tools. |
| **T1082** | System Information Discovery | Functions like `CompileProfileReport` and `GetMachineGuid` are used to gather hardware/software identifiers for fingerprinting the host. |
| **T1102** | Web Service | The use of specific, named endpoints (e.g., `BOOTSTRAP_ENDPOINT`, `METRICS_ENDPOINT`) indicates a structured communication protocol with a web service for C2 or data reporting. |
| **T1041** | Exfiltrate Data over C2 Channel | The collection and transmission of telemetry, system metrics, and profile reports to remote servers suggests the exfiltration of gathered information. |
| **T1105** | Ingress Tool Transfer | The `ExtractZipFile` functionality used in conjunction with receiving instructions from a remote server identifies it as a mechanism for deploying additional payloads/modules. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*Note: Specific IPs or fully qualified domain names (FQDNs) were not present in the raw strings; however, the following constants define the C2 communication infrastructure:*
* `LOG_API_URL`
* `SUCCESS_API_URL`
* `BOOTSTRAP_ENDPOINT`
* `METRICS_ENDPOINT`
* `TELEMETRY_ENDPOINT`

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   `8AE2AA28BDE162C0233C2C2F7BD5EC39EAD36EFAD2C4BA2411C8638DAD7904F0` (Potential file/payload hash)
*   `CD9CB809DF131FE1886468DD6D616F109D4F5D10805E0ECB051051BC33615291` (Potential file/payload hash)

**Other artifacts**
*   **C2 Communication Patterns:** Evidence of structured reporting via `ReportTelemetryAsync`, `ReportMetricsAsync`, and `LogUserActionSync`.
*   **De-obfuscation Logic:** Presence of `Obfuscate` and `Deobfuscate` functions indicating wrapped communication strings or payloads.
*   **Dropper Behavior:** Use of `ExtractZipFile` and `JoinPayload` suggesting a multi-stage delivery mechanism.
*   **System Fingerprinting:** Use of `GetMachineGuid`, `CompileProfileReport`, and `IsChromeInstalled` to profile the victim machine before or during exfiltration.

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification for the sample:

1. **Malware family**: Unknown (The behavior suggests it could be part of a larger campaign, but no specific known brand identifiers like Emotet or Cobalt Strike were detected in the report.)
2. **Malware type**: Dropper / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Multi-Stage Delivery:** The use of `ExtractZipFile` and `JoinPayload` combined with remote "Bootstrap" and "Success" endpoints confirms its role as a primary vehicle to deliver and install further malicious components.
    *   **System Profiling & Exfiltration:** The inclusion of functions like `CompileProfileReport`, `GetMachineGuid`, and `ReportTelemetryAsync` indicates the sample is designed to fingerprint the victim's environment before reporting back to a C2 infrastructure.
    *   **Anti-Analysis Techniques:** The presence of intentional obfuscation (overlapping instructions, "bad instruction" data) and explicit `Deobfuscate` routines are hallmark indicators of malware designed to evade security software and manual analysis during the initial infection phase.
