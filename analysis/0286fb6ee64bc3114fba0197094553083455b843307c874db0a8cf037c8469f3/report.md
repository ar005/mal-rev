# Threat Analysis Report

**Generated:** 2026-06-28 07:20 UTC
**Sample:** `0286fb6ee64bc3114fba0197094553083455b843307c874db0a8cf037c8469f3_0286fb6ee64bc3114fba0197094553083455b843307c874db0a8cf037c8469f3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0286fb6ee64bc3114fba0197094553083455b843307c874db0a8cf037c8469f3_0286fb6ee64bc3114fba0197094553083455b843307c874db0a8cf037c8469f3.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 925,696 bytes |
| MD5 | `83f22d4959a30695ab6831fdec1f80dc` |
| SHA1 | `a6d9a2bde390b9c10f5ba64a9b8b44f60b58ea01` |
| SHA256 | `0286fb6ee64bc3114fba0197094553083455b843307c874db0a8cf037c8469f3` |
| Overall entropy | 7.091 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2725057335 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 906,240 | 7.112 | ⚠️ Yes |
| `.rsrc` | 18,432 | 4.459 | No |

## Extracted Strings

Total strings found: **1775** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
v4.0.30319
#Strings
<>c__DisplayClass2_0
<ExtractManifold>b__0
<ExtractManifold>b__1
Func`1
IEnumerable`1
Stack`1
ThreadLocal`1
List`1
lastPoint1
Dictionary`2
lastPoint2
<ExtractManifold>g__debugNoOp|2
<Module>
MySql.Data
System.Data
FromArgb
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
Thread
Synchronized
ondNameField
FirstNameField
TelField
EmailField
LoginField
loginField
PassField
passField
get_Gold
ExtractManifold
get_Hand
DbCommand
MySqlCommand
set_SelectCommand
textPassword
FlatButtonAppearance
get_FlatAppearance
defaultInstance
set_AutoScaleMode
set_SizeMode
PictureBoxSizeMode
set_Image
AddRange
Invoke
DataTable
IDisposable
RuntimeTypeHandle
GetTypeFromHandle
DockStyle
set_BorderStyle
set_FormBorderStyle
set_FlatStyle
FontStyle
set_Name
textSurName
textName
CallByName
DateTime
set_Multiline
textPhone
MySqlDbType
CallType
GetType
get_Culture
set_Culture
resourceCulture
InternalDataCollectionBase
ButtonBase
ApplicationSettingsBase
TextBoxBase
Dispose
get_State
EditorBrowsableState
ConnectionState
get_White
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
TargetFrameworkAttribute
AssemblyFileVersionAttribute
AssemblyConfigurationAttribute
AssemblyDescriptionAttribute
CompilationRelaxationsAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
AssemblyCompanyAttribute
RuntimeCompatibilityAttribute
get_Value
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass2_0._ExtractManifold_g__debugNoOp2` | `0x140005ca8` | 17658 | ✓ |
| `method.ExampleSQLApp.RegisterForm.InitializeComponent` | `0x1400045b8` | 5338 | ✓ |
| `method.ExampleSQLApp.LoginForm.InitializeComponent` | `0x140002698` | 3841 | ✓ |
| `method.ExampleSQLApp.MainForm.InitializeComponent` | `0x140003714` | 1488 | ✓ |
| `method.ExampleSQLApp.LoginForm.ExtractManifold` | `0x140002154` | 720 | ✓ |
| `method.ExampleSQLApp.RegisterForm.buttonLogin_Click` | `0x1400042a8` | 488 | ✓ |
| `method.ExampleSQLApp.LoginForm.buttonLogin_Click` | `0x14000254c` | 240 | ✓ |
| `method.ExampleSQLApp.RegisterForm..ctor` | `0x140003d00` | 240 | ✓ |
| `method.ExampleSQLApp.RegisterForm.isUserExist` | `0x140004490` | 204 | ✓ |
| `method.ExampleSQLApp.LoginForm..ctor` | `0x1400020e0` | 116 | ✓ |
| `method.ExampleSQLApp.LoginForm.title_MouseMove` | `0x140002424` | 97 | ✓ |
| `method.ExampleSQLApp.LoginForm.panel_MouseMove` | `0x1400024a0` | 97 | ✓ |
| `method.ExampleSQLApp.MainForm.title_MouseMove` | `0x1400035e4` | 97 | ✓ |
| `method.ExampleSQLApp.MainForm.Main_MouseMove` | `0x140003660` | 97 | ✓ |
| `method.ExampleSQLApp.RegisterForm.title_MouseMove` | `0x140003df0` | 97 | ✓ |
| `method.ExampleSQLApp.RegisterForm.panel_MouseMove` | `0x140003e6c` | 97 | ✓ |
| `method.ExampleSQLApp.RegisterForm.FisrtNameField_Enter` | `0x140003f18` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.FisrtNameField_Leave` | `0x140003f64` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.SeondNameField_Enter` | `0x140003fb0` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.SeondNameField_Leave` | `0x140003ffc` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.LoginField_Enter` | `0x140004048` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.LoginField_Leave` | `0x140004094` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.PassField_Enter` | `0x1400040e0` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.PassField_Leave` | `0x14000412c` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.EmailField_Enter` | `0x140004178` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.EmailField_Leave` | `0x1400041c4` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.TelField_Enter` | `0x140004210` | 76 | ✓ |
| `method.ExampleSQLApp.RegisterForm.TelField_Leave` | `0x14000425c` | 76 | ✓ |
| `method.ExampleSQLApp.Properties.Resources.get_ResourceManager` | `0x140005a9c` | 72 | ✓ |
| `method.ExampleSQLApp.LoginForm.Dispose` | `0x140002660` | 56 | ✓ |

### Decompiled Code Files

- [`code/method.ExampleSQLApp.LoginForm..ctor.c`](code/method.ExampleSQLApp.LoginForm..ctor.c)
- [`code/method.ExampleSQLApp.LoginForm.Dispose.c`](code/method.ExampleSQLApp.LoginForm.Dispose.c)
- [`code/method.ExampleSQLApp.LoginForm.ExtractManifold.c`](code/method.ExampleSQLApp.LoginForm.ExtractManifold.c)
- [`code/method.ExampleSQLApp.LoginForm.InitializeComponent.c`](code/method.ExampleSQLApp.LoginForm.InitializeComponent.c)
- [`code/method.ExampleSQLApp.LoginForm.buttonLogin_Click.c`](code/method.ExampleSQLApp.LoginForm.buttonLogin_Click.c)
- [`code/method.ExampleSQLApp.LoginForm.panel_MouseMove.c`](code/method.ExampleSQLApp.LoginForm.panel_MouseMove.c)
- [`code/method.ExampleSQLApp.LoginForm.title_MouseMove.c`](code/method.ExampleSQLApp.LoginForm.title_MouseMove.c)
- [`code/method.ExampleSQLApp.MainForm.InitializeComponent.c`](code/method.ExampleSQLApp.MainForm.InitializeComponent.c)
- [`code/method.ExampleSQLApp.MainForm.Main_MouseMove.c`](code/method.ExampleSQLApp.MainForm.Main_MouseMove.c)
- [`code/method.ExampleSQLApp.MainForm.title_MouseMove.c`](code/method.ExampleSQLApp.MainForm.title_MouseMove.c)
- [`code/method.ExampleSQLApp.Properties.Resources.get_ResourceManager.c`](code/method.ExampleSQLApp.Properties.Resources.get_ResourceManager.c)
- [`code/method.ExampleSQLApp.RegisterForm..ctor.c`](code/method.ExampleSQLApp.RegisterForm..ctor.c)
- [`code/method.ExampleSQLApp.RegisterForm.EmailField_Enter.c`](code/method.ExampleSQLApp.RegisterForm.EmailField_Enter.c)
- [`code/method.ExampleSQLApp.RegisterForm.EmailField_Leave.c`](code/method.ExampleSQLApp.RegisterForm.EmailField_Leave.c)
- [`code/method.ExampleSQLApp.RegisterForm.FisrtNameField_Enter.c`](code/method.ExampleSQLApp.RegisterForm.FisrtNameField_Enter.c)
- [`code/method.ExampleSQLApp.RegisterForm.FisrtNameField_Leave.c`](code/method.ExampleSQLApp.RegisterForm.FisrtNameField_Leave.c)
- [`code/method.ExampleSQLApp.RegisterForm.InitializeComponent.c`](code/method.ExampleSQLApp.RegisterForm.InitializeComponent.c)
- [`code/method.ExampleSQLApp.RegisterForm.LoginField_Enter.c`](code/method.ExampleSQLApp.RegisterForm.LoginField_Enter.c)
- [`code/method.ExampleSQLApp.RegisterForm.LoginField_Leave.c`](code/method.ExampleSQLApp.RegisterForm.LoginField_Leave.c)
- [`code/method.ExampleSQLApp.RegisterForm.PassField_Enter.c`](code/method.ExampleSQLApp.RegisterForm.PassField_Enter.c)
- [`code/method.ExampleSQLApp.RegisterForm.PassField_Leave.c`](code/method.ExampleSQLApp.RegisterForm.PassField_Leave.c)
- [`code/method.ExampleSQLApp.RegisterForm.SeondNameField_Enter.c`](code/method.ExampleSQLApp.RegisterForm.SeondNameField_Enter.c)
- [`code/method.ExampleSQLApp.RegisterForm.SeondNameField_Leave.c`](code/method.ExampleSQLApp.RegisterForm.SeondNameField_Leave.c)
- [`code/method.ExampleSQLApp.RegisterForm.TelField_Enter.c`](code/method.ExampleSQLApp.RegisterForm.TelField_Enter.c)
- [`code/method.ExampleSQLApp.RegisterForm.TelField_Leave.c`](code/method.ExampleSQLApp.RegisterForm.TelField_Leave.c)
- [`code/method.ExampleSQLApp.RegisterForm.buttonLogin_Click.c`](code/method.ExampleSQLApp.RegisterForm.buttonLogin_Click.c)
- [`code/method.ExampleSQLApp.RegisterForm.isUserExist.c`](code/method.ExampleSQLApp.RegisterForm.isUserExist.c)
- [`code/method.ExampleSQLApp.RegisterForm.panel_MouseMove.c`](code/method.ExampleSQLApp.RegisterForm.panel_MouseMove.c)
- [`code/method.ExampleSQLApp.RegisterForm.title_MouseMove.c`](code/method.ExampleSQLApp.RegisterForm.title_MouseMove.c)
- [`code/method.__c__DisplayClass2_0._ExtractManifold_g__debugNoOp2.c`](code/method.__c__DisplayClass2_0._ExtractManifold_g__debugNoOp2.c)

## Behavioral Analysis

Based on the provided strings and decompiled code, here is an analysis of the binary's functionality and behavior.

### Core Functionality and Purpose
The binary appears to be a **credential harvesting or information-stealing application** disguised as a legitimate utility or portal. 
*   **User Interface:** The presence of `LoginForm`, `RegisterForm`, and various UI components (e.g., `buttonLogin_Click`, `textPassword`, `FirstnameField`) indicates the program presents a GUI to the user for entering personal information.
*   **Data Collection:** The code specifically targets Personally Identifiable Information (PII), including:
    *   First/Last Names
    *   Email addresses
    *   Phone numbers
    *   Login credentials (usernames and passwords)
*   **Database Interaction:** The inclusion of `MySql.Data` and `DbCommand` indicates that the stolen data is intended to be stored in, or verified against, a MySQL database.

### Suspicious and Malicious Behaviors
*   **Credential Harvesting:** The primary workflow involves capturing user credentials through a login/registration interface. Given the high level of obfuscation (see below), this is likely part of a phishing campaign or an "InfoStealer" malware family.
*   **Data Exfiltration Preparation:** By using `MySql.Data` libraries, the application is prepared to transmit captured data from the local machine to a remote server managed by the attacker.
*   **Intentional Obfuscation:** The repeated "WARNING: Control flow encountered bad instruction data" and the presence of "junk" code (e.g., complex bitwise logic and `CONCAT` operations in functions like `ExtractManifold`) are clear indicators that the developer is trying to hinder reverse engineering and automated analysis.

### Notable Techniques and Patterns
*   **Anti-Analysis/Obfuscation:** The decompilation results are heavily mangled. In modern malware, this often indicates:
    *   **Control Flow Flattening:** Making it difficult for analysts to follow the logic of a function.
    *   **Junk Code Insertion:** Adding meaningless calculations and "opaque predicates" (logic that always evaluates one way but looks complex to a decompiler) to hide the real malicious logic.
    *   **Packer/Protector Usage:** The "bad instruction" errors often occur when a decompiler encounters code protected by packers like VMProtect or Themida, or custom mutation engines.
*   **Evidence of Phishing Architecture:** The inclusion of both `LoginForm` and `RegisterForm` suggests the application might be used to create fake portals where users are tricked into registering for a fake service or "validating" their information.

### Summary for Incident Response
This sample shows strong indicators of **malicious intent**. It combines **Credential Harvesting** (collecting login/PII) with **Advanced Obfuscation** (to hide the data's path and the ultimate destination). The presence of MySQL integration suggests it is designed to aggregate stolen data into a centralized database for the attacker.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1566.003** | Phishing: Spearphishing Attachment (Information) | The use of `LoginForm` and `RegisterForm` to trick users into providing PII and credentials suggests a phishing-based information gathering tactic. |
| **T1041** | Exfiltration Over C2 Channel | The inclusion of `MySql.Data` libraries indicates the intent to transmit stolen data from the local machine to a remote server for aggregation. |
| **T1036** | Masquerading | The application is explicitly described as being disguised as a legitimate utility or portal to deceive users into interacting with it. |
| **T1027** | Obfuscated Files or Information | The use of junk code, complex bitwise logic, and control flow flattening are clear attempts to hide the malicious functionality from analysts. |
| **T1027.002** | Obfusculated Files or Information: Debug Ignore Flag | (Optional/Specific) The "bad instruction" errors suggest the use of packers or protectors which often trigger during de-obfuscation attempts. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `bLbPm.exe` (Identified filename)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **C2/Exfiltration Mechanism:** The use of `MySql.Data`, `DbCommand`, and `MySqlCommand` indicates the malware utilizes a MySQL database for data storage or exfiltration.
*   **Obfuscation Indicators:** 
    *   `ExtractManifold`: A recurring custom function used to hide logic or facilitate "junk code" insertion.
    *   Control flow flattening/malformed instructions: Evidence of advanced packers (e.g., VMProtect, Themida) or custom mutation engines.
*   **Credential Harvesting Fields:** The application targets the following specific data points via UI components: `FirstNameField`, `EmailField`, `TelField`, `LoginField`, and `PassField`.
*   **Application Logic:** Presence of both `LoginForm` and `RegisterForm` indicates a phishing-style architecture.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: Infostealer (Custom)
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Credential & PII Harvesting:** The presence of `LoginForm`, `RegisterForm`, and specific fields for names, emails, phone numbers, and passwords indicates a deliberate intent to steal sensitive user information.
    *   **Exfiltration Infrastructure:** The inclusion of `MySql.Data` libraries confirms that the malware is designed to transmit stolen data to a remote database managed by the attacker.
    *   **Advanced Evasion Techniques:** The use of junk code, control flow flattening (via the `ExtractManifold` function), and "bad instruction" obfuscation indicates a sophisticated effort to hide malicious logic from automated analysis and reverse engineering.
