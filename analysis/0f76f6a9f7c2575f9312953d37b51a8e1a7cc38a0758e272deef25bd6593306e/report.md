# Threat Analysis Report

**Generated:** 2026-08-16 14:40 UTC
**Sample:** `0f76f6a9f7c2575f9312953d37b51a8e1a7cc38a0758e272deef25bd6593306e_0f76f6a9f7c2575f9312953d37b51a8e1a7cc38a0758e272deef25bd6593306e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f76f6a9f7c2575f9312953d37b51a8e1a7cc38a0758e272deef25bd6593306e_0f76f6a9f7c2575f9312953d37b51a8e1a7cc38a0758e272deef25bd6593306e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 133,408 bytes |
| MD5 | `13a6edd9c1ab6cb2961a4b3bdda4a655` |
| SHA1 | `5160b586b1a9a75ed881001b3ef776ddd60ab4f3` |
| SHA256 | `0f76f6a9f7c2575f9312953d37b51a8e1a7cc38a0758e272deef25bd6593306e` |
| Overall entropy | 7.239 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3026318791 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 103,424 | 7.487 | ⚠️ Yes |
| `.rsrc` | 17,408 | 3.966 | No |

## Extracted Strings

Total strings found: **604** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

&*fsK
v4.0.30319
#Strings
<>9__8_0
<UploadPanel_MouseDown>b__8_0
<>9__8_1
<UploadPanel_MouseDown>b__8_1
<>u__1
Nullable`1
IEnumerable`1
ConfiguredTaskAwaitable`1
Task`1
AsyncTaskMethodBuilder`1
IEnumerator`1
Microsoft.Win32
<getStream>d__2
<>u__2
Func`2
<Module>
Crystal PDF
get_ASCII
Native.UI
System.IO
mscorlib
System.Collections.Generic
ReadAsStreamAsync
GetAsync
PostAsync
ReadAsByteArrayAsync
connectionId
_contentLoaded
AwaitUnsafeOnCompleted
get_IsCompleted
Synchronized
<file>k__BackingField
<filename>k__BackingField
<size>k__BackingField
<convertBaseUrl>k__BackingField
<url>k__BackingField
<error>k__BackingField
<success>k__BackingField
<waitWindow>k__BackingField
UriKind
defaultInstance
get_IsSuccessStatusCode
FileMode
HttpResponseMessage
message
Enumerable
IDisposable
RuntimeTypeHandle
GetTypeFromHandle
UploadFile
saveFile
RspFile
get_file
set_file
get_FileName
GetFileName
get_filename
set_filename
Combine
IAsyncStateMachine
SetStateMachine
stateMachine
ValueType
set_ContentType
System.Core
PresentationCore
get_Culture
set_Culture
resourceCulture
ConverterBase
ApplicationSettingsBase
Dispose
Create
EditorBrowsableState
<>1__state
STAThreadAttribute
CompilerGeneratedAttribute
GeneratedCodeAttribute
DebuggerNonUserCodeAttribute
DebuggableAttribute
EditorBrowsableAttribute
ComVisibleAttribute
AssemblyTitleAttribute
AsyncStateMachineAttribute
AssemblyTrademarkAttribute
TargetFrameworkAttribute
DebuggerHiddenAttribute
AssemblyFileVersionAttribute
AssemblyConfigurationAttribute
AssemblyDescriptionAttribute
ThemeInfoAttribute
CompilationRelaxationsAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
AssemblyCompanyAttribute
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym._getStream_d__2.SetStateMachine_1` | `0x140002cd4` | 127788 | ✓ |
| `method._getStream_d__2.SetStateMachine` | `0x140002e34` | 65184 | ✓ |
| `method.Native.MainWindow..ctor` | `0x140002087` | 1122 | ✓ |
| `method.Native.Actions.ConverterBase..ctor` | `0x140002803` | 384 | ✓ |
| `sym._getStream_d__2.MoveNext` | `0x140002a24` | 336 | ✓ |
| `sym._getStream_d__2.MoveNext_1` | `0x140002b84` | 336 | ✓ |
| `method._getStream_d__2.MoveNext` | `0x140002ce4` | 336 | ✓ |
| `method.Native.MainWindow.UploadPanel_MouseDown` | `0x1400021f0` | 320 | ✓ |
| `method.Native.MainWindow.System.Windows.Markup.IComponentConnector.Connect` | `0x140002428` | 252 | ✓ |
| `method.Native.Actions.Merger.getRespObj` | `0x140002850` | 240 | ✓ |
| `method.Native.Entities.RspInfo..ctor` | `0x1400025bf` | 228 | ✓ |
| `method.Native.Actions.Compressor..ctor` | `0x1400026a3` | 228 | ✓ |
| `method.Native.UI.WaitWindow..ctor` | `0x14000298b` | 153 | ✓ |
| `method.Native.Actions.ConverterBase.saveFile` | `0x140002798` | 128 | ✓ |
| `method.Native.MainWindow.MergeButton_MouseDown` | `0x140002178` | 120 | ✓ |
| `method.Native.MainWindow.ConvertButton_MouseDown` | `0x140002098` | 112 | ✓ |
| `method.Native.MainWindow.CompressButton_MouseDown` | `0x140002108` | 112 | ✓ |
| `method.Native.Actions.Merger.getStream` | `0x140002940` | 92 | ✓ |
| `method.Native.Actions.ConverterBase.get_convertBaseUrl` | `0x14000278f` | 90 | ✓ |
| `method.Native.Actions.Compressor.Compress` | `0x1400025c8` | 88 | ✓ |
| `method.Native.Actions.Converter.Convert` | `0x1400026ac` | 88 | ✓ |
| `method.Native.Actions.Converter.getStream` | `0x140002744` | 84 | ✓ |
| `method.Native.Actions.Compressor.getStream` | `0x140002660` | 76 | ✓ |
| `method.Native.Actions.Compressor.getRespObj` | `0x140002620` | 64 | ✓ |
| `method.Native.Actions.Converter.getRespObj` | `0x140002704` | 64 | ✓ |
| `method.Native.Actions.Merger.Merge` | `0x140002818` | 56 | ✓ |
| `method.Native.MainWindow.compress` | `0x140002330` | 54 | ✓ |
| `method.Native.MainWindow.convert` | `0x14000238c` | 54 | ✓ |
| `method.Native.Properties.Settings.get_Default` | `0x14000252c` | 54 | ✓ |
| `method.Native.MainWindow.InitializeComponent` | `0x1400023f8` | 48 | ✓ |

### Decompiled Code Files

- [`code/method.Native.Actions.Compressor..ctor.c`](code/method.Native.Actions.Compressor..ctor.c)
- [`code/method.Native.Actions.Compressor.Compress.c`](code/method.Native.Actions.Compressor.Compress.c)
- [`code/method.Native.Actions.Compressor.getRespObj.c`](code/method.Native.Actions.Compressor.getRespObj.c)
- [`code/method.Native.Actions.Compressor.getStream.c`](code/method.Native.Actions.Compressor.getStream.c)
- [`code/method.Native.Actions.Converter.Convert.c`](code/method.Native.Actions.Converter.Convert.c)
- [`code/method.Native.Actions.Converter.getRespObj.c`](code/method.Native.Actions.Converter.getRespObj.c)
- [`code/method.Native.Actions.Converter.getStream.c`](code/method.Native.Actions.Converter.getStream.c)
- [`code/method.Native.Actions.ConverterBase..ctor.c`](code/method.Native.Actions.ConverterBase..ctor.c)
- [`code/method.Native.Actions.ConverterBase.get_convertBaseUrl.c`](code/method.Native.Actions.ConverterBase.get_convertBaseUrl.c)
- [`code/method.Native.Actions.ConverterBase.saveFile.c`](code/method.Native.Actions.ConverterBase.saveFile.c)
- [`code/method.Native.Actions.Merger.Merge.c`](code/method.Native.Actions.Merger.Merge.c)
- [`code/method.Native.Actions.Merger.getRespObj.c`](code/method.Native.Actions.Merger.getRespObj.c)
- [`code/method.Native.Actions.Merger.getStream.c`](code/method.Native.Actions.Merger.getStream.c)
- [`code/method.Native.Entities.RspInfo..ctor.c`](code/method.Native.Entities.RspInfo..ctor.c)
- [`code/method.Native.MainWindow..ctor.c`](code/method.Native.MainWindow..ctor.c)
- [`code/method.Native.MainWindow.CompressButton_MouseDown.c`](code/method.Native.MainWindow.CompressButton_MouseDown.c)
- [`code/method.Native.MainWindow.ConvertButton_MouseDown.c`](code/method.Native.MainWindow.ConvertButton_MouseDown.c)
- [`code/method.Native.MainWindow.InitializeComponent.c`](code/method.Native.MainWindow.InitializeComponent.c)
- [`code/method.Native.MainWindow.MergeButton_MouseDown.c`](code/method.Native.MainWindow.MergeButton_MouseDown.c)
- [`code/method.Native.MainWindow.System.Windows.Markup.IComponentConnector.Connect.c`](code/method.Native.MainWindow.System.Windows.Markup.IComponentConnector.Connect.c)
- [`code/method.Native.MainWindow.UploadPanel_MouseDown.c`](code/method.Native.MainWindow.UploadPanel_MouseDown.c)
- [`code/method.Native.MainWindow.compress.c`](code/method.Native.MainWindow.compress.c)
- [`code/method.Native.MainWindow.convert.c`](code/method.Native.MainWindow.convert.c)
- [`code/method.Native.Properties.Settings.get_Default.c`](code/method.Native.Properties.Settings.get_Default.c)
- [`code/method.Native.UI.WaitWindow..ctor.c`](code/method.Native.UI.WaitWindow..ctor.c)
- [`code/method._getStream_d__2.MoveNext.c`](code/method._getStream_d__2.MoveNext.c)
- [`code/method._getStream_d__2.SetStateMachine.c`](code/method._getStream_d__2.SetStateMachine.c)
- [`code/sym._getStream_d__2.MoveNext.c`](code/sym._getStream_d__2.MoveNext.c)
- [`code/sym._getStream_d__2.MoveNext_1.c`](code/sym._getStream_d__2.MoveNext_1.c)
- [`code/sym._getStream_d__2.SetStateMachine_1.c`](code/sym._getStream_d__2.SetStateMachine_1.c)

## Behavioral Analysis

### Analysis Summary

**Core Functionality**
Based on the strings and method names, this binary is a **PDF manipulation utility** named "Crystal PDF." Its primary purpose appears to be processing PDF documents through several features:
*   **Merging:** Combining multiple files into one (`Merger.Merge`).
*   **Compressing:** Reducing file size (`Compressor.Compress`, `CompressButton_MouseDown`).
*   **Converting:** Changing the format of a document or converting it via a remote service (`Converter.Convert`, `get_convertBaseUrl`).
*   **File Management:** Interacting with the local filesystem to read and save files (`saveFile`, `OpenFileDialog`).

**Suspicious or Malicious Behavs**
While the application presents as a legitimate utility, several indicators suggest potential malicious intent or a "trojanized" functionality:

*   **Obfuscation/Packing:** The most significant finding is the extensive presence of `halt_baddata()` and "bad instruction data" across nearly every function. This indicates that the binary has been heavily **obfuscated or packed**. Obfuscation is a primary technique used by malware to hinder manual analysis and hide malicious logic (such as backdoors or information stealers).
*   **Network Communication for Data Exfiltration:** The presence of `System.Net.Http` components (`PostAsync`, `GetAsync`, `upload_file`) combined with "Convert" features suggests the application communicates with a remote server. In a malicious context, these features can be used to exfiltrate sensitive documents under the guise of an "online conversion service."
*   **Potential Information Stealing:** The inclusion of `JavaScriptSerializer` and various networking libraries suggest that data (possibly metadata or full file content) is serialized and sent over the internet.

**Notable Techniques & Patterns**
*   **Obfuscated Control Flow:** The decompiler's inability to resolve jump logic (`Control flow encountered bad instruction data`) points to the use of obfuscation tools like ConfuserEx or similar packers. This is intended to confuse analysts by injecting junk code and "spaghetti" jumps.
*   **WinForms Framework Usage:** The sample uses standard Windows Forms elements (e.g., `UploadPanel`, `_MouseDown` events). Malware often uses these familiar GUI components to appear as a legitimate "tool" while performing malicious background tasks.
*   **API Wrapping:** Many functions are named in the format `method.Native...`. This suggests the code is interacting with lower-level system APIs or standard .NET libraries, which may be wrapping more complex logic that remains obscured by the obfuscation layer.

### Conclusion
The sample appears to be a **Potentially Unwanted Application (PUA) or Trojan**. While it possesses features of a PDF utility, the high level of **obfuscation** and the presence of **remote upload capabilities** are major red flags. It may be designed to lure users into "converting" documents, which then transmits those files to an attacker-controlled server.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The extensive presence of `halt_baddata` and "bad instruction data" indicates heavy obfuscation designed to hinder manual analysis and hide malicious code. |
| T1567 | Exfiltration Over Web Service | The use of `PostAsync`, `GetAsync`, and `upload_file` functions suggests the utility exfiltrates documents to a remote server under the guise of an "online conversion" service. |
| T1036 | Masquerading | Use of standard WinForms components and common functionality (PDF merging/compressing) allows the malware to blend in as a legitimate tool to deceive the user. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Many strings in the source text are standard .NET framework libraries or internal method names; these have been excluded as false positives.*

**IP addresses / URLs / Domains**
*   *None identified.* (The report mentions "remote servers" and `get_convertBaseUrl`, but no specific hardcoded IPs or domains were provided in the source text.)

**File paths / Registry keys**
*   `Crystal PDF.exe` (Identified as the primary filename for the utility)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Application Name:** Crystal PDF (Potential identity used for social engineering or as a front for malicious activity).
*   **C2/Exfiltration Pattern:** Usage of `System.Net.Http` classes (`GetAsync`, `PostAsync`) in conjunction with `upload_file` and `convert` functions, suggesting an infrastructure for remote file transmission.
*   **Obfuscation Technique:** Evidence of "bad instruction data" and "halt_baddata()" indicates the use of a packer/obfuscator (e.g., ConfuserEx) to hide malicious logic or exfiltration routines.
*   **Suspicious Functionality:** The integration of `JavaScriptSerializer` with networking libraries suggests structured data packaging before transmission to an external endpoint.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://ns.adobe.com/xap/1.0/`
- `http://ns.adobe.com/xap/1.0/mm/`
- `http://ns.adobe.com/xap/1.0/sType/ResourceRef#`
- `http://schemas.microsoft.com/expression/blend/2008`
- `http://schemas.microsoft.com/winfx/2006/xaml`
- `http://schemas.microsoft.com/winfx/2006/xaml/presentation`
- `http://schemas.openxmlformats.org/markup-compatibility/2006`
- `http://www.w3.org/1999/02/22-rdf-syntax-ns#`

**IP addresses:**
- `3.0.10.100`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High

4. **Key evidence**:
*   **Deceptive Functionality (Masquerading):** The malware presents as a legitimate utility ("Crystal PDF") to convince users to interact with it, while the underlying logic uses "conversion" and "upload" features as a pretext for exfiltrating documents to remote servers via `System.Net.Http`.
*   **Heavy Obfuscation:** The extensive use of "bad instruction data" and `halt_baddata()` indicates a deliberate attempt to hide malicious code and thwart automated analysis, typical of malware designed to conceal stolen-data routines.
*   **Data Packaging for Exfiltration:** The integration of `JavaScriptSerializer` with networking libraries suggests that the software is structured to package and serialize sensitive data (files or metadata) before transmission over the internet.
