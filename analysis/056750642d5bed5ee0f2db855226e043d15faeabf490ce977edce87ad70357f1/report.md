# Threat Analysis Report

**Generated:** 2026-07-13 20:05 UTC
**Sample:** `056750642d5bed5ee0f2db855226e043d15faeabf490ce977edce87ad70357f1_056750642d5bed5ee0f2db855226e043d15faeabf490ce977edce87ad70357f1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `056750642d5bed5ee0f2db855226e043d15faeabf490ce977edce87ad70357f1_056750642d5bed5ee0f2db855226e043d15faeabf490ce977edce87ad70357f1.exe` |
| File type | PE32+ executable for MS Windows 4.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 27,648 bytes |
| MD5 | `ed1bf281ed96dd41a6db2751e5427452` |
| SHA1 | `a7d402dbc3a19b46dbed581ccec19d154b2cb412` |
| SHA256 | `056750642d5bed5ee0f2db855226e043d15faeabf490ce977edce87ad70357f1` |
| Overall entropy | 5.714 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3980465208 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 25,600 | 5.828 | No |
| `.rsrc` | 1,536 | 3.891 | No |

## Extracted Strings

Total strings found: **364** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

X )UU

X )UU

X )UU

,h	of

,a	of
v4.0.30319
#Strings
<i>5__10
<>c__DisplayClass8_0
<>c__DisplayClass9_0
<CheckRunningProcesses>b__0
<CheckRunningAvProcesses>b__0
<>p__0
<FetchConfigAsync>d__11
<>p__1
<>u__1
Nullable`1
IEnumerable`1
CallSite`1
Task`1
ICollection`1
HttpHeaderValueCollection`1
AsyncTaskMethodBuilder`1
IEqualityComparer`1
TaskAwaiter`1
IEnumerator`1
HashSet`1
List`1
ReadOnlyMemory`1
<extractFolder>5__2
<client>5__2
<isBot>5__2
<>p__2
<>u__2
Func`2
ValueTuple`2
AbstractArchive`2
get_CoreWebView2
<SendPostRequest>d__13
<stream>5__3
<exeFiles>5__3
<isAv>5__3
<>p__3
<>u__3
Func`3
<DownloadFileAsync>d__14
<fileStream>5__4
<dllFiles>5__4
<processesAv>5__4
<>p__4
<>u__4
<>f__AnonymousType0`4
Func`4
<UnzipAndInstallAsync>d__15
<archive>5__5
<buffer>5__5
<>p__5
<>u__5
<>7__wrap5
<totalRead>5__6
<bytesRead>5__7
<destinationPath>5__7
<InitializeWebView>d__7
<>o__7
get_UTF8
<entryStream>5__8
<fileStream>5__9
<Module>
System.IO
System.Collections.Generic
EnsureCoreWebView2Async
ReadAsync
DownloadFileAsync
WriteAsync
FetchConfigAsync
ReadAsStringAsync
UnzipAndInstallAsync
ReadAsStreamAsync
CopyToAsync
GetAsync
PostAsync
ParseAdd
set_AreDevToolsEnabled
set_AreDefaultContextMenusEnabled
set_Handled
AwaitUnsafeOnCompleted
get_IsCompleted
CoreWebView2_ContextMenuRequested
AppendFormatted
NewGuid
<method>i__Field
<randomcode>i__Field
<message>i__Field
<type>i__Field
get_method
set_Password
archivePassword
Replace
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.MicrosoftWebViewDriver.MainForm.CoreWebView2_ContextMenuRequested` | `0x140002877` | 38794 | ✓ |
| `method._UnzipAndInstallAsync_d__15.SetStateMachine` | `0x1400040b4` | 32588 | ✓ |
| `method._InitializeWebView_d__7.MoveNext` | `0x140002f10` | 2244 | ✓ |
| `method._UnzipAndInstallAsync_d__15.MoveNext` | `0x140003a14` | 1696 | ✓ |
| `method._DownloadFileAsync_d__14.MoveNext` | `0x1400028b8` | 1108 | ✓ |
| `method._SendPostRequest_d__13.MoveNext` | `0x1400037e4` | 544 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.CheckRunningAvProcesses` | `0x140002378` | 516 | ✓ |
| `method._FetchConfigAsync_d__11.MoveNext` | `0x140002d1c` | 484 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.CheckRunningProcesses` | `0x14000257c` | 360 | ✓ |
| `method.__f__AnonymousType0_4.ToString` | `0x140002180` | 190 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm..ctor` | `0x140002284` | 188 | ✓ |
| `method.__f__AnonymousType0_4.Equals` | `0x140002090` | 128 | ✓ |
| `method.__f__AnonymousType0_4.GetHashCode` | `0x140002110` | 112 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.SendPostRequest` | `0x1400027a4` | 76 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.GenerateActivationCode` | `0x14000275c` | 72 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.DownloadFileAsync` | `0x1400027f0` | 68 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.UnzipAndInstallAsync` | `0x140002834` | 67 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.CheckScreenResolution` | `0x1400026e4` | 60 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.FetchConfigAsync` | `0x140002720` | 60 | ✓ |
| `method.MicrosoftWebViewDriver.MainForm.InitializeWebView` | `0x140002340` | 56 | ✓ |
| `method.WeChat.Properties.Resource.get_ResourceManager` | `0x140002246` | 44 | ✓ |
| `method.__f__AnonymousType0_4..ctor` | `0x140002068` | 40 | ✓ |
| `method._DownloadFileAsync_d__14.SetStateMachine` | `0x140002d0c` | 16 | ✓ |
| `method._FetchConfigAsync_d__11.SetStateMachine` | `0x140002f00` | 16 | ✓ |
| `method._InitializeWebView_d__7.SetStateMachine` | `0x1400037d4` | 16 | ✓ |
| `method._SendPostRequest_d__13.SetStateMachine` | `0x140003a04` | 16 | ✓ |
| `method.__c__DisplayClass8_0._CheckRunningAvProcesses_b__0` | `0x140002894` | 14 | ✓ |
| `method.__c__DisplayClass9_0._CheckRunningProcesses_b__0` | `0x1400028aa` | 14 | ✓ |
| `entry0` | `0x140002880` | 12 | ✓ |
| `method.WeChat.Properties.Resource.set_Culture` | `0x140002279` | 11 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.MicrosoftWebViewDriver.MainForm..ctor.c`](code/method.MicrosoftWebViewDriver.MainForm..ctor.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.CheckRunningAvProcesses.c`](code/method.MicrosoftWebViewDriver.MainForm.CheckRunningAvProcesses.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.CheckRunningProcesses.c`](code/method.MicrosoftWebViewDriver.MainForm.CheckRunningProcesses.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.CheckScreenResolution.c`](code/method.MicrosoftWebViewDriver.MainForm.CheckScreenResolution.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.CoreWebView2_ContextMenuRequested.c`](code/method.MicrosoftWebViewDriver.MainForm.CoreWebView2_ContextMenuRequested.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.DownloadFileAsync.c`](code/method.MicrosoftWebViewDriver.MainForm.DownloadFileAsync.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.FetchConfigAsync.c`](code/method.MicrosoftWebViewDriver.MainForm.FetchConfigAsync.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.GenerateActivationCode.c`](code/method.MicrosoftWebViewDriver.MainForm.GenerateActivationCode.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.InitializeWebView.c`](code/method.MicrosoftWebViewDriver.MainForm.InitializeWebView.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.SendPostRequest.c`](code/method.MicrosoftWebViewDriver.MainForm.SendPostRequest.c)
- [`code/method.MicrosoftWebViewDriver.MainForm.UnzipAndInstallAsync.c`](code/method.MicrosoftWebViewDriver.MainForm.UnzipAndInstallAsync.c)
- [`code/method.WeChat.Properties.Resource.get_ResourceManager.c`](code/method.WeChat.Properties.Resource.get_ResourceManager.c)
- [`code/method.WeChat.Properties.Resource.set_Culture.c`](code/method.WeChat.Properties.Resource.set_Culture.c)
- [`code/method._DownloadFileAsync_d__14.MoveNext.c`](code/method._DownloadFileAsync_d__14.MoveNext.c)
- [`code/method._DownloadFileAsync_d__14.SetStateMachine.c`](code/method._DownloadFileAsync_d__14.SetStateMachine.c)
- [`code/method._FetchConfigAsync_d__11.MoveNext.c`](code/method._FetchConfigAsync_d__11.MoveNext.c)
- [`code/method._FetchConfigAsync_d__11.SetStateMachine.c`](code/method._FetchConfigAsync_d__11.SetStateMachine.c)
- [`code/method._InitializeWebView_d__7.MoveNext.c`](code/method._InitializeWebView_d__7.MoveNext.c)
- [`code/method._InitializeWebView_d__7.SetStateMachine.c`](code/method._InitializeWebView_d__7.SetStateMachine.c)
- [`code/method._SendPostRequest_d__13.MoveNext.c`](code/method._SendPostRequest_d__13.MoveNext.c)
- [`code/method._SendPostRequest_d__13.SetStateMachine.c`](code/method._SendPostRequest_d__13.SetStateMachine.c)
- [`code/method._UnzipAndInstallAsync_d__15.MoveNext.c`](code/method._UnzipAndInstallAsync_d__15.MoveNext.c)
- [`code/method._UnzipAndInstallAsync_d__15.SetStateMachine.c`](code/method._UnzipAndInstallAsync_d__15.SetStateMachine.c)
- [`code/method.__c__DisplayClass8_0._CheckRunningAvProcesses_b__0.c`](code/method.__c__DisplayClass8_0._CheckRunningAvProcesses_b__0.c)
- [`code/method.__c__DisplayClass9_0._CheckRunningProcesses_b__0.c`](code/method.__c__DisplayClass9_0._CheckRunningProcesses_b__0.c)
- [`code/method.__f__AnonymousType0_4..ctor.c`](code/method.__f__AnonymousType0_4..ctor.c)
- [`code/method.__f__AnonymousType0_4.Equals.c`](code/method.__f__AnonymousType0_4.Equals.c)
- [`code/method.__f__AnonymousType0_4.GetHashCode.c`](code/method.__f__AnonymousType0_4.GetHashCode.c)
- [`code/method.__f__AnonymousType0_4.ToString.c`](code/method.__f__AnonymousType0_4.ToString.c)

## Behavioral Analysis

Based on the provided strings and decompiled code, here is an analysis of the binary sample.

### Core Functionality and Purpose
The application appears to be a **malicious downloader/dropper** disguised with a user interface (likely a WebView2-based front end). Its primary purpose is to evade security software while reaching out to a remote server to fetch configuration data and download additional, potentially malicious, payloads onto the victim's system.

### Suspoded or Malicious Behaviors
*   **Anti-Analysis & Evasion:** 
    *   The binary explicitly includes functions like `CheckRunningAvProcesses` and `CheckRunningProcesses`.
    *   Internal logic (seen in strings) checks for "AV" (Antivirus), a "Bot," and various process names. This is intended to determine if the code is running in a sandbox or on a machine protected by security software before executing malicious actions.
*   **Command & Control (C2) Communication:** 
    *   The presence of `FetchConfigAsync`, `SendPostRequest`, and `GetAsync` suggests that the program communicates with an external server to receive instructions or configuration data.
*   **Payload Delivery & Execution:** 
    *   The code contains several functions for handling remote files: `DownloadFileAsync`, `WriteAsync`, and `UnzipAndInstallAsync`.
    *   This indicates a multi-stage infection process where the initial binary is just a "loader" that pulls down and extracts (unpacks) the actual payload.
*   **Evidence of Information Gathering:** 
    *   The presence of `GenerateActivationCode` and potentially credential-related logic suggests it may also be designed to engage in some form of social engineering or theft.

### Notable Techniques & Patterns
*   **Heavy Obfuscation (Anti-Analysis):** The disassembly shows a high amount of "bad instruction data," overlapping instructions, and junk code calculations (e.g., repetitive additions/subtractions). This is a deliberate technique used to break decompilers and disassemblers like Ghidra or IDA Pro, making it harder for researchers to trace the actual logic.
*   **WebViewer Wrapper:** The use of `Microsoft_WebView2` suggests the malware may present a legitimate-looking web interface to the user. This is often used to mask malicious activity (like fake "update" screens or credential harvesting pages) under the guise of a standard browser window.
*   **Staged Loading:** By using an unzip/install routine, the malware avoids having its primary payload on disk in its initial form, which helps evade simple signature-based detection from antivirus software.

### Summary Table of Indicators
| Feature | Detected Evidence | Significance |
| :--- | :--- | :--- |
| **Evasion** | `CheckRunningAvProcesses`, `isAv`, `isBot` | Active effort to hide from security analysts. |
| **Networking** | `FetchConfigAsync`, `SendPostRequest` | Communication with a remote Command & Control server. |
| **File Dropping** | `DownloadFileAsync`, `UnzipAndInstallAsync` | Capability to download and install secondary payloads. |
| **Obfuscation** | Overlapping instructions, "bad" data blocks | Deliberate attempt to hinder reverse engineering. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1562.001 | Impair Defenses: Disable or Notify Security Software | The binary explicitly checks for antivirus software processes (`CheckRunningAvProcesses`) to decide whether to execute its payload. |
| T1497 | Virtualized Environment/Sandbox Detection | The inclusion of `isBot` and `CheckRunning_Processes` logic suggests an attempt to detect and evade automated analysis environments. |
| T1027 | Obfuscated Files or Information | The use of junk code, overlapping instructions, and "bad" data blocks is a deliberate attempt to hinder reverse engineering by analysts. |
| T1105 | Ingress Tool Transfer | The `DownloadFileAsync` and `UnzipAndInstallAsync` functions indicate the binary acts as a dropper to pull down additional malicious components. |
| T1071.001 | Application Layer Protocol: Web Protocols | The use of `FetchConfigAsync` and `SendPostRequest` indicates communication with a remote server using standard web protocols for configuration. |
| T1036 | Masquerading | Utilizing the `Microsoft_WebView2` component allows the malware to wrap malicious activity within a legitimate-looking user interface. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** Because the input consists of raw internal code strings and high-level behavioral descriptions rather than a full packet capture or memory dump, several atomic indicators (like specific IP addresses) are not present. However, the following behaviors and artifacts were identified:

### **IP addresses / URLs / Domains**
*   *None identified in provided text.*

### **File paths / Registry keys**
*   `WeChat.dll` (Note: This is a highly suspicious filename often associated with fake application wrappers or credential harvesters mimicking popular messaging platforms.)

### **Mutex names / Named pipes**
*   *None identified in system strings.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **C2 Patterns:** 
    *   `FetchConfigAsync` (Indicates routine call to fetch remote configuration)
    *   `SendPostRequest` (Mechanism for exfiltrating data or sending heartbeats)
    *   `GetAsync` / `PostAsync` (Standard HTTP methods used for C2 communication)
*   **Evasion Techniques:**
    *   `CheckRunningAvProcesses` (Specific logic to detect and bypass Antivirus software)
    *   `isAv`, `isBot` (Internal flags used to determine if the environment is a sandbox or protected machine)
    *   `CheckRunningProcesses` (Used for environment fingerprinting)
*   **Malware Behavior Indicators:**
    *   `UnzipAndInstallAsync` (Identifies the binary as a "dropper" or "downloader")
    *   `DownloadFileAsync` / `WriteAsync` (Indicates secondary payload retrieval and local storage)
    *   `GetRandomFileName` (Often used to hide malicious files in paths with non-descript names)

---
**Analyst Note:** The presence of `WeChat.dll` combined with `WebView2` integration suggests this is a "Fake App" trojan. It likely mimics a legitimate login screen for WeChat or a similar service to steal credentials, while the internal calls to `FetchConfigAsync` and `UnzipAndInstallAsync` confirm its role as a multi-stage downloader.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-stage Delivery:** The presence of `DownloadFileAsync`, `WriteAsync`, and `UnzipAndInstallAsync` confirms the primary role is a "loader" designed to fetch, stage, and execute secondary payloads.
*   **Aggressive Evasion Tactics:** The binary implements significant anti-analysis measures, including specific checks for antivirus processes (`CheckRunningAvProcesses`), sandbox detection (`isBot`), and heavy code obfuscation (overlapping instructions) to hinder manual analysis.
*   **Masquerading & Social Engineering:** The integration of `Microsoft_WebView2` combined with the suspicious file name `WeChat.dll` suggests a "Fake App" strategy used to deceive users into interacting with the UI while the loader operates in the background.
