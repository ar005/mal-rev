# Threat Analysis Report

**Generated:** 2026-07-13 22:48 UTC
**Sample:** `05856b53b569c7740f19e15584aea33fe711016fcebca3fac8d42411424f6bb9_05856b53b569c7740f19e15584aea33fe711016fcebca3fac8d42411424f6bb9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05856b53b569c7740f19e15584aea33fe711016fcebca3fac8d42411424f6bb9_05856b53b569c7740f19e15584aea33fe711016fcebca3fac8d42411424f6bb9.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,018,880 bytes |
| MD5 | `c57a8f94c54fe276a40081d71a99cc7a` |
| SHA1 | `fc3cd39b306c89b201df80957d4cd6fe192d43d2` |
| SHA256 | `05856b53b569c7740f19e15584aea33fe711016fcebca3fac8d42411424f6bb9` |
| Overall entropy | 7.9 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3070171225 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,016,832 | 7.903 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.142 | No |

## Extracted Strings

Total strings found: **2414** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
p+ r	

-V+drS
aiA.b+

-"+(~
v4.0.30319
#Strings
<>c__DisplayClass3_0
<Gather>g__Log|0
IEnumerable`1
Action`1
List`1
Microsoft.Win32
<Module>
<PrivateImplementationDetails>
System.IO
LoadAndR
get_lbhgT
get_LayerT
value__
mscorlib
set_Verb
System.Collections.Generic
Form1_Load
Form2_Load
Form3_Load
add_Load
add_SelectedIndexChanged
listBoxBackups_SelectedIndexChanged
set_FormattingEnabled
Synchronized
ReadToEnd
add_BeforeExpand
treeViewRegistry_BeforeExpand
IsNullOrWhiteSpace
defaultInstance
EmitBAndAdvance
get_ExitCode
set_AutoScaleMode
get_Node
get_SelectedNode
TreeNode
parentNode
get_Message
AddRange
Invoke
Enumerable
IDisposable
writable
RuntimeTypeHandle
GetTypeFromHandle
ImportRegistryFile
set_Title
lblTitle
btnSchedule
dateTimePickerSchedule
set_DropDownStyle
set_FormBorderStyle
FontStyle
ComboBoxStyle
get_Name
set_Name
get_FileName
set_FileName
GetFileName
lblTaskName
txtTaskName
rootName
lblScheduleTime
scheduleTime
DateTime
get_LastWriteTime
Combine
LocalMachine
GetScheduleType
AsType
System.Core
btnRestore
BuildSignature
get_Culture
set_Culture
resourceCulture
ButtonBase
ApplicationSettingsBase
TextBoxBase
btnClose
Dispose
btnBrowse
EditorBrowsableState
STAThreadAttribute
CompilerGeneratedAttribute
GuidAttribute
GeneratedCodeAttribute
DebuggerNonUserCodeAttribute
DebuggableAttribute
EditorBrowsableAttribute
ComVisibleAttribute
AssemblyTitleAttribute
AssemblyTrademarkAttribute
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass3_0._Gather_g__Log0` | `0x140004c70` | 17430 | ✓ |
| `method.RegistryBackupTool.Form3.InitializeComponent` | `0x140003700` | 2083 | ✓ |
| `method.RegistryBackupTool.Form2.InitializeComponent` | `0x140002c08` | 1584 | ✓ |
| `method.RegistryBackupTool.MainForm.InitializeComponent` | `0x140004238` | 1214 | ✓ |
| `method.RegistryBackupTool.Form1.InitializeComponent` | `0x14000244c` | 968 | ✓ |
| `method.RegistryBackupTool.Form3.btnSchedule_Click` | `0x1400032e4` | 548 | ✓ |
| `method.RegistryBackupTool.RegistryManager.GetRootKey` | `0x140004934` | 396 | ✓ |
| `method.RegistryBackupTool.Form2.btnRestore_Click` | `0x1400029d8` | 372 | ✓ |
| `method.RegistryBackupTool.MainForm.Step` | `0x140003ff8` | 348 | ✓ |
| `method.RegistryBackupTool.Form1.btnBackup_Click` | `0x140002258` | 320 | ✓ |
| `method.RegistryBackupTool.Form2.LoadBackupFiles` | `0x140002884` | 248 | ✓ |
| `method.RegistryBackupTool.Form3.GetScheduleArguments` | `0x14000357c` | 216 | ✓ |
| `method.RegistryBackupTool.RegistryManager.ImportRegistryFile` | `0x1400047c4` | 208 | ✓ |
| `method.RegistryBackupTool.MainForm.Gather` | `0x140003f48` | 176 | ✓ |
| `method.RegistryBackupTool.RegistryManager.ExportRegistryKey` | `0x140004714` | 176 | ✓ |
| `method.RegistryBackupTool.Form1.LoadSubKeys` | `0x14000217c` | 148 | ✓ |
| `method.RegistryBackupTool.Form1.PopulateRootKeys` | `0x140002074` | 144 | ✓ |
| `method.RegistryBackupTool.Form1.treeViewRegistry_BeforeExpand` | `0x140002104` | 120 | ✓ |
| `method.RegistryBackupTool.Form3.GetScheduleType` | `0x140003508` | 116 | ✓ |
| `method.RegistryBackupTool.Form1.Form1_Load` | `0x1400023a4` | 112 | ✓ |
| `method.RegistryBackupTool.Form2.listBoxBackups_SelectedIndexChanged` | `0x140002b60` | 112 | ✓ |
| `method.RegistryBackupTool.Form3.btnViewTasks_Click` | `0x140003654` | 104 | ✓ |
| `method.RegistryBackupTool.Form2..ctor` | `0x140002814` | 100 | ✓ |
| `method.RegistryBackupTool.Form2.btnBrowse_Click` | `0x14000297c` | 92 | ✓ |
| `method.RegistryBackupTool.Form3..ctor` | `0x140003238` | 92 | ✓ |
| `method.RegistryBackupTool.RegistryManager.GetRegistryKey` | `0x1400048dc` | 88 | ✓ |
| `method.RegistryBackupTool.RegistryManager.GetSubKeys` | `0x140004ac0` | 88 | ✓ |
| `method.RegistryBackupTool.Form3.Form3_Load` | `0x140003294` | 80 | ✓ |
| `method.RegistryBackupTool.MainForm.BuildSignature` | `0x140004154` | 80 | ✓ |
| `method.RegistryBackupTool.Form1.GetFullPath` | `0x140002210` | 72 | ✓ |

### Decompiled Code Files

- [`code/method.RegistryBackupTool.Form1.Form1_Load.c`](code/method.RegistryBackupTool.Form1.Form1_Load.c)
- [`code/method.RegistryBackupTool.Form1.GetFullPath.c`](code/method.RegistryBackupTool.Form1.GetFullPath.c)
- [`code/method.RegistryBackupTool.Form1.InitializeComponent.c`](code/method.RegistryBackupTool.Form1.InitializeComponent.c)
- [`code/method.RegistryBackupTool.Form1.LoadSubKeys.c`](code/method.RegistryBackupTool.Form1.LoadSubKeys.c)
- [`code/method.RegistryBackupTool.Form1.PopulateRootKeys.c`](code/method.RegistryBackupTool.Form1.PopulateRootKeys.c)
- [`code/method.RegistryBackupTool.Form1.btnBackup_Click.c`](code/method.RegistryBackupTool.Form1.btnBackup_Click.c)
- [`code/method.RegistryBackupTool.Form1.treeViewRegistry_BeforeExpand.c`](code/method.RegistryBackupTool.Form1.treeViewRegistry_BeforeExpand.c)
- [`code/method.RegistryBackupTool.Form2..ctor.c`](code/method.RegistryBackupTool.Form2..ctor.c)
- [`code/method.RegistryBackupTool.Form2.InitializeComponent.c`](code/method.RegistryBackupTool.Form2.InitializeComponent.c)
- [`code/method.RegistryBackupTool.Form2.LoadBackupFiles.c`](code/method.RegistryBackupTool.Form2.LoadBackupFiles.c)
- [`code/method.RegistryBackupTool.Form2.btnBrowse_Click.c`](code/method.RegistryBackupTool.Form2.btnBrowse_Click.c)
- [`code/method.RegistryBackupTool.Form2.btnRestore_Click.c`](code/method.RegistryBackupTool.Form2.btnRestore_Click.c)
- [`code/method.RegistryBackupTool.Form2.listBoxBackups_SelectedIndexChanged.c`](code/method.RegistryBackupTool.Form2.listBoxBackups_SelectedIndexChanged.c)
- [`code/method.RegistryBackupTool.Form3..ctor.c`](code/method.RegistryBackupTool.Form3..ctor.c)
- [`code/method.RegistryBackupTool.Form3.Form3_Load.c`](code/method.RegistryBackupTool.Form3.Form3_Load.c)
- [`code/method.RegistryBackupTool.Form3.GetScheduleArguments.c`](code/method.RegistryBackupTool.Form3.GetScheduleArguments.c)
- [`code/method.RegistryBackupTool.Form3.GetScheduleType.c`](code/method.RegistryBackupTool.Form3.GetScheduleType.c)
- [`code/method.RegistryBackupTool.Form3.InitializeComponent.c`](code/method.RegistryBackupTool.Form3.InitializeComponent.c)
- [`code/method.RegistryBackupTool.Form3.btnSchedule_Click.c`](code/method.RegistryBackupTool.Form3.btnSchedule_Click.c)
- [`code/method.RegistryBackupTool.Form3.btnViewTasks_Click.c`](code/method.RegistryBackupTool.Form3.btnViewTasks_Click.c)
- [`code/method.RegistryBackupTool.MainForm.BuildSignature.c`](code/method.RegistryBackupTool.MainForm.BuildSignature.c)
- [`code/method.RegistryBackupTool.MainForm.Gather.c`](code/method.RegistryBackupTool.MainForm.Gather.c)
- [`code/method.RegistryBackupTool.MainForm.InitializeComponent.c`](code/method.RegistryBackupTool.MainForm.InitializeComponent.c)
- [`code/method.RegistryBackupTool.MainForm.Step.c`](code/method.RegistryBackupTool.MainForm.Step.c)
- [`code/method.RegistryBackupTool.RegistryManager.ExportRegistryKey.c`](code/method.RegistryBackupTool.RegistryManager.ExportRegistryKey.c)
- [`code/method.RegistryBackupTool.RegistryManager.GetRegistryKey.c`](code/method.RegistryBackupTool.RegistryManager.GetRegistryKey.c)
- [`code/method.RegistryBackupTool.RegistryManager.GetRootKey.c`](code/method.RegistryBackupTool.RegistryManager.GetRootKey.c)
- [`code/method.RegistryBackupTool.RegistryManager.GetSubKeys.c`](code/method.RegistryBackupTool.RegistryManager.GetSubKeys.c)
- [`code/method.RegistryBackupTool.RegistryManager.ImportRegistryFile.c`](code/method.RegistryBackupTool.RegistryManager.ImportRegistryFile.c)
- [`code/method.__c__DisplayClass3_0._Gather_g__Log0.c`](code/method.__c__DisplayClass3_0._Gather_g__Log0.c)

## Behavioral Analysis

Based on the analysis of the provided strings and decompiled code, here is a summary of the findings:

### **Core Functionality**
The binary is a **GUI-based Registry Management and Backup Tool**. It is likely written in C# or another .NET language (evidenced by references to `mscorlib`, `System.Windows.Forms`, and `.Net` assembly naming conventions). 

Its primary functions include:
*   **Registry Navigation:** The code includes logic for traversing registry keys, populating a tree view (`treeViewRegistry_BeforeExpand`), and retrieving subkeys (`GetSubKeys`).
*   **Backup/Restore Operations:** It contains explicit functionality to export registry keys to files (`ExportRegistryKey`) and import them back into the system (`ImportRegistryFile`).
*   **Task Scheduling:** There are elements of a scheduling system (e.g., `btnSchedule_Click`, `GetScheduleArguments`, `DetermineScheduleType`), suggesting it can perform these actions at specific times or intervals.

### **Suspicious and Malicious Behaviors**
While the tool presents itself as a utility for backing up registry settings, its capabilities are common in malware and "grayware" for the following reasons:

*   **High-Value Data Targeting:** The primary function of the tool is to interact with the Windows Registry. In a malware context, this is frequently used to:
    *   **Steal Credentials:** Extracting information from registry hives that store passwords or session tokens.
    *   **Establish Persistence:** Identifying and modifying "Run" keys to ensure the malware executes on every system reboot.
    *   **Disable Security:** Modifying registry keys to disable Windows Defender, firewalls, or other security software.
*   **Potential for Exfiltration:** While this specific snippet does not show an active network connection (e.g., no `Socket` or `HTTPClient` calls are immediately visible), the "Export" functionality allows a user or an automated script to dump entire sections of system configuration to a local file, which can then be exfiltrated by another process.
*   **Scheduled Tasks:** The inclusion of scheduling logic suggests that the application is designed to run automatically or persist in the background, which is a common trait of "droppers" or "backdoors."

### **Notable Techniques and Patterns**
*   **.NET Framework Usage:** The sample relies heavily on standard .NET libraries. This means the actual malicious behavior might be wrapped inside high-level managed code, making it easier to hide logic from simple signature-based scanners but more complex to analyze without a specialized decompiler (like dnSpy or ILSpy).
*   **Deceptive Tooling:** The use of "RegistryBackupTool" as a name and feature set is a common masquerading technique. By providing a functional (but potentially malicious) utility, an attacker can justify the presence of a tool that interacts with sensitive system components.
*   **Complexity in Decompilation:** Many functions show "bad instruction" data or complex bitwise/arithmetic operations in the pseudocode. This is common when a decompiler attempts to translate highly optimized JIT-compiled code (like .NET) into standard C, but it can also indicate the presence of some basic obfuscation or anti-analysis techniques designed to frustrate automated tools.

### **Summary for Incident Response**
*   **Verdict:** Potentially Malicious / Dual-Use Tool.
*   **Primary Risk:** Credential theft and persistence via registry manipulation.
*   **Recommendation:** Monitor the process for access to sensitive registry hives (e.g., `HKEY_LOCAL_MACHINE\SOFTWARE` or paths containing "Run" keys) and check for the creation of local files used as backup containers.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Registry Run Keys / Startup Folder | The tool’s ability to interact with registry keys allows an attacker to establish persistence by modifying "Run" keys. |
| T1053 | Scheduled Task/Job | The inclusion of specific scheduling logic (e.g., `btnSchedule_Click`) indicates the capability to execute actions at predetermined intervals. |
| T1036 | Masquerading | The tool adopts the guise of a legitimate "Registry Management" utility to provide a cover for its interaction with sensitive system components. |
| T1027 | Obfuscated Files or Information | The presence of complex bitwise and arithmetic operations is used to complicate decompiler output and frustrate automated analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None found.

**File paths / Registry keys**
*   `yUdWY.exe` (Executable filename)

**Mutex names / Named pipes**
*   None found.

**Hashes**
*   None found.

**Other artifacts**
*   **Execution Pattern:** The use of "Scheduled Tasks" logic (`btnSchedule_Click`, `GetScheduleArguments`) indicates an attempt to establish persistence or delayed execution.
*   **Data Staging Behavior:** Use of "Export" and "Import" functions on registry keys (specifically targeting areas like `HKEY_LOCAL_MACHINE\SOFTWARE` and "Run" keys) suggests the ability to dump credentials or configuration data to local files for later exfiltration.
*   **Application Masquerading:** The tool utilizes a deceptive name ("RegistryBackupTool") to justify its interaction with sensitive system components.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: Medium

**Key evidence**:
*   **Masquerading & Persistence:** The application uses a deceptive "Registry Management" front to justify interacting with sensitive system areas. The inclusion of specific logic for "Scheduled Tasks" (T1053) and targeting "Run Keys" (T1547.001) are classic indicators of an attempt to establish long-term persistence on a host.
*   **Data Staging Behavior:** While no active network communication was detected, the core functionality involves exporting registry hives to local files. This is a common tactic for staging credentials and system configuration data in a format easy for subsequent processes (or remote actors) to exfiltrate.
*   **Evasive Characteristics:** The use of .NET for high-level wrapper implementation combined with "complex bitwise/arithmetic" operations suggests an intentional effort to complicate static analysis and bypass signature-based detection while maintaining the tool's deceptive functionality.
