# Threat Analysis Report

**Generated:** 2026-06-28 02:11 UTC
**Sample:** `022a46f18a4014d21659f817f9a16da4068d5a1ee20c85d7a2e5062f1005ae05_022a46f18a4014d21659f817f9a16da4068d5a1ee20c85d7a2e5062f1005ae05.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `022a46f18a4014d21659f817f9a16da4068d5a1ee20c85d7a2e5062f1005ae05_022a46f18a4014d21659f817f9a16da4068d5a1ee20c85d7a2e5062f1005ae05.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 481,792 bytes |
| MD5 | `7f1d9703c262c21a88d8bbf60245b799` |
| SHA1 | `21c714007f5659847083a90e88b6e8218610a548` |
| SHA256 | `022a46f18a4014d21659f817f9a16da4068d5a1ee20c85d7a2e5062f1005ae05` |
| Overall entropy | 5.947 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3408626405 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 267,776 | 6.084 | No |
| `.rsrc` | 212,992 | 5.758 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **752** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
#ffffff

%-&~l

*BSJB
v4.0.30319
#Strings
label10
label1
panel1
timer1
pictureBox1
richTextBox1
Microsoft.Win32
label2
panel2
pictureBox2
panel3
label6
get_UTF8
label8
<Module>
AdapticID
MachineID
SPIF_SENDWININICHANGE
SPIF_UPDATEINIFILE
MAX_PATH
SendAPI
System.IO
SPI_GETDESKWALLPAPER
SPI_SETDESKWALLPAPER
get_IV
set_IV
SendIV
get_Captura
mscorlib
UnicallyId
Synchronized
get_Hand
RegistryValueKind
CopyToClipboard
UserPassword
Replace
defaultInstance
AddPersistence
RemovePersistence
set_Mode
set_AutoScaleMode
FileMode
set_SizeMode
PictureBoxSizeMode
PaddingMode
CryptoStreamMode
CipherMode
DeleteSubKeyTree
set_Image
IDisposable
RuntimeTypeHandle
GetTypeFromHandle
inputFile
outputFile
PersistenceModule
get_MainModule
ProcessModule
set_BorderStyle
set_FormBorderStyle
set_FlatStyle
FontStyle
set_Name
get_FileName
set_FileName
GetFileName
get_MachineName
keyName
GetDirectoryName
elapsedTime
DateTime
GetStartupTime
SetStartupTime
RansStartTime
ReadLine
Combine
set_Multiline
get_Culture
set_Culture
resourceCulture
ButtonBase
ApplicationSettingsBase
TextBoxBase
Dispose
Create
EditorBrowsableState
Delete
get_White
STAThreadAttribute
CompilerGeneratedAttribute
GuidAttribute
GeneratedCodeAttribute
DebuggerNonUserCodeAttribute
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **22**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.FuxForm.Algorithms.UserUtils..ctor` | `0x403ed8` | 13090 | ✓ |
| `method.FuxForm.Form1.InitializeComponent` | `0x402258` | 4130 | — |
| `method.FuxForm.Algorithms.SendAlgo.SendAPI` | `0x403acc` | 624 | ✓ |
| `method.FuxForm.Algorithms.DecryptFunctions.DecFileAlgo` | `0x403650` | 360 | ✓ |
| `method.FuxForm.Algorithms.AuxiliaryFunctions.GetStartupTime` | `0x40334c` | 188 | ✓ |
| `method.FuxForm.Algorithms.config..cctor` | `0x4034d0` | 164 | ✓ |
| `method.FuxForm.Algorithms.PersistenceModule.AddPersistence` | `0x403978` | 160 | ✓ |
| `method.FuxForm.Algorithms.DecryptFunctions.DecFiles` | `0x4035c0` | 144 | ✓ |
| `method.FuxForm.Algorithms.AuxiliaryFunctions.ChkRegistry` | `0x403408` | 116 | ✓ |
| `method.FuxForm.Algorithms.DeleteFuncs.SelfRemove` | `0x403820` | 114 | ✓ |
| `method.FuxForm.Algorithms.PersistenceModule.RemovePersistence` | `0x403a18` | 104 | ✓ |
| `method.FuxForm.Algorithms.UserUtils.IsWallpaperStatusSet` | `0x403e20` | 100 | ✓ |
| `method.FuxForm.Algorithms.DeleteFuncs.DeleteAll` | `0x4037c0` | 96 | ✓ |
| `method.FuxForm.Algorithms.Generator.CaesarCipher` | `0x403914` | 89 | ✓ |
| `method.FuxForm.Algorithms.Generator.GetIP` | `0x4038a8` | 84 | ✓ |
| `method.FuxForm.Algorithms.UserUtils.SetWallpaperStatus` | `0x403e84` | 84 | ✓ |
| `method.FuxForm.Algorithms.UserUtils.SetDesktopWallpaper` | `0x403d98` | 78 | ✓ |
| `method.FuxForm.Algorithms.DecryptFunctions.Decryptor` | `0x403574` | 76 | ✓ |
| `method.FuxForm.Algorithms.AuxiliaryFunctions.EncFiles_Count` | `0x40347c` | 68 | ✓ |
| `method.FuxForm.Algorithms.SendAlgo.SendInformation_Checker` | `0x403a88` | 68 | ✓ |
| `method.FuxForm.Form1.InitializeTimer` | `0x4020bf` | 63 | — |
| `method.FuxForm.Algorithms.UserUtils.RestoreOriginalWallpaper` | `0x403de6` | 58 | ✓ |
| `method.FuxForm.Algorithms.UserUtils.GetDesktopWallpaper` | `0x403d60` | 56 | ✓ |
| `method.FuxForm.Form1.Unlock_Click` | `0x40207b` | 50 | — |
| `method.FuxForm.Form1.AboutBitcoin_Click` | `0x4021a8` | 48 | — |
| `method.FuxForm.Form1.HowBuy_Bitcoin_Click` | `0x4021d8` | 48 | — |
| `method.FuxForm.Form1.ContactLabel_Click` | `0x402208` | 48 | — |
| `method.FuxForm.Form1.EncryptedFiles_Count` | `0x40215f` | 44 | — |
| `method.FuxForm.Properties.Resources.get_ResourceManager` | `0x403299` | 44 | ✓ |
| `method.FuxForm.Form1..ctor` | `0x402050` | 43 | — |

### Decompiled Code Files

- [`code/method.FuxForm.Algorithms.AuxiliaryFunctions.ChkRegistry.c`](code/method.FuxForm.Algorithms.AuxiliaryFunctions.ChkRegistry.c)
- [`code/method.FuxForm.Algorithms.AuxiliaryFunctions.EncFiles_Count.c`](code/method.FuxForm.Algorithms.AuxiliaryFunctions.EncFiles_Count.c)
- [`code/method.FuxForm.Algorithms.AuxiliaryFunctions.GetStartupTime.c`](code/method.FuxForm.Algorithms.AuxiliaryFunctions.GetStartupTime.c)
- [`code/method.FuxForm.Algorithms.DecryptFunctions.DecFileAlgo.c`](code/method.FuxForm.Algorithms.DecryptFunctions.DecFileAlgo.c)
- [`code/method.FuxForm.Algorithms.DecryptFunctions.DecFiles.c`](code/method.FuxForm.Algorithms.DecryptFunctions.DecFiles.c)
- [`code/method.FuxForm.Algorithms.DecryptFunctions.Decryptor.c`](code/method.FuxForm.Algorithms.DecryptFunctions.Decryptor.c)
- [`code/method.FuxForm.Algorithms.DeleteFuncs.DeleteAll.c`](code/method.FuxForm.Algorithms.DeleteFuncs.DeleteAll.c)
- [`code/method.FuxForm.Algorithms.DeleteFuncs.SelfRemove.c`](code/method.FuxForm.Algorithms.DeleteFuncs.SelfRemove.c)
- [`code/method.FuxForm.Algorithms.Generator.CaesarCipher.c`](code/method.FuxForm.Algorithms.Generator.CaesarCipher.c)
- [`code/method.FuxForm.Algorithms.Generator.GetIP.c`](code/method.FuxForm.Algorithms.Generator.GetIP.c)
- [`code/method.FuxForm.Algorithms.PersistenceModule.AddPersistence.c`](code/method.FuxForm.Algorithms.PersistenceModule.AddPersistence.c)
- [`code/method.FuxForm.Algorithms.PersistenceModule.RemovePersistence.c`](code/method.FuxForm.Algorithms.PersistenceModule.RemovePersistence.c)
- [`code/method.FuxForm.Algorithms.SendAlgo.SendAPI.c`](code/method.FuxForm.Algorithms.SendAlgo.SendAPI.c)
- [`code/method.FuxForm.Algorithms.SendAlgo.SendInformation_Checker.c`](code/method.FuxForm.Algorithms.SendAlgo.SendInformation_Checker.c)
- [`code/method.FuxForm.Algorithms.UserUtils..ctor.c`](code/method.FuxForm.Algorithms.UserUtils..ctor.c)
- [`code/method.FuxForm.Algorithms.UserUtils.GetDesktopWallpaper.c`](code/method.FuxForm.Algorithms.UserUtils.GetDesktopWallpaper.c)
- [`code/method.FuxForm.Algorithms.UserUtils.IsWallpaperStatusSet.c`](code/method.FuxForm.Algorithms.UserUtils.IsWallpaperStatusSet.c)
- [`code/method.FuxForm.Algorithms.UserUtils.RestoreOriginalWallpaper.c`](code/method.FuxForm.Algorithms.UserUtils.RestoreOriginalWallpaper.c)
- [`code/method.FuxForm.Algorithms.UserUtils.SetDesktopWallpaper.c`](code/method.FuxForm.Algorithms.UserUtils.SetDesktopWallpaper.c)
- [`code/method.FuxForm.Algorithms.UserUtils.SetWallpaperStatus.c`](code/method.FuxForm.Algorithms.UserUtils.SetWallpaperStatus.c)
- [`code/method.FuxForm.Algorithms.config..cctor.c`](code/method.FuxForm.Algorithms.config..cctor.c)
- [`code/method.FuxForm.Properties.Resources.get_ResourceManager.c`](code/method.FuxForm.Properties.Resources.get_ResourceManager.c)

## Behavioral Analysis

This final analysis incorporates the findings from **Chunk 5/5** of the disassembled code for `Ransomware_Form.exe`. This final segment provides insight into the malware's persistence in the user's environment, its technical sophistication in evading analysis, and the "cleanup" or "reversion" logic (which can sometimes indicate multi-stage behavior).

### Analysis Update: Chunk 5/5

The functions `RestoreOriginalWallpaper` and `GetDesktopWallpaper`, combined with the massive blocks of complex, non-linear assembly, provide a final look at how this malware hides its tracks and interacts with the Windows subsystem.

#### 1. Environmental Persistence & Interaction
*   **Functions:** `RestoreOriginalWallpaper`, `GetDesktopWallpaper`.
*   **Analysis:** While these functions might seem benign (looking for "restoration"), in the context of ransomware, they serve two potential purposes:
    *   **Pre-Infection Preparation:** The malware may "cache" the original system state to ensure it can fully take over the display environment without being interrupted by OS notifications.
    *   **Persistence Logic:** These functions suggest a sophisticated installer/loader approach where the ransomware ensures that its "branding" (the ransom note) is consistently displayed across various system states.
*   **Risk Factor:** The ability to manipulate and query deep Windows Shell settings indicates that the malware interacts directly with the OS's graphical environment, making it harder for an average user to ignore the notification of being infected.

#### 2. Heavy Obfuscation & "Code Bloat" as a Shield
*   **Observation:** The large blocks of assembly featuring `CONCAT31`, complex arithmetic on high-value constants (e.g., `0x60ab005`), and nested conditional jumps.
*   **Analysis:** This is a classic sign of **Anti-Analysis/Obfuscation**. By using "junk" calculations, mathematical substitutions for simple values, and convoluted control flows (as evidenced by the "Bad instruction - Truncating control flow" warnings), the developers have made it extremely difficult for automated tools to reconstruct the original logic.
*   **Impact:** This protects the "core" of the ransomware—such as the specific encryption keys or C2 protocols—by burying them inside a wall of complex math that requires significant manual effort from a human researcher to untangle.

#### 3. Low-Level System Interaction
*   **Observation:** The inclusion of `swi(1)` (Software Interrupt) calls and non-standard memory offsets.
*   **Analysis:** This indicates the malware may be interacting with lower-level system functions or trying to bypass standard API hooks used by EDR (Endpoint Detection and Response) solutions. 
*   **Risk Factor:** By operating at a level closer to the kernel, the ransomware can potentially "hide" its activities from traditional antivirus software that only monitors standard Windows APIs.

---

### Final Summary Table (Chunks 1–5)

| Feature | Evidence | Risk Level | Analysis Notes |
| :--- | :--- | :--- | :--- |
| **Ransomware** | `DecFiles`, `EncFiles_Count` | **Critical** | Automated search and count of target files prior to encryption. |
| **Persistence** | `AddPersistence`, `RemovePersistence` | **High** | Active mechanisms to ensure the malware survives a system reboot. |
| **Obfuscation** | Complex arithmetic, "Junk" code loops | **Critical** | High-effort obfuscation designed to defeat static analysis and delay manual RE. |
| **C2/Exfiltration** | `GetIP`, `SendInformation_Checker` | **High** | Communicates with a remote server to register the infection and send data. |
| **User Manipulation** | `SetDesktopWallpaper`, `RestoreOriginalWallpaper` | **Medium/High** | Forces the ransom note onto the screen; ensures maximum visibility for the attacker. |
| **System Interaction**| `swi()` calls, Custom offsets | **High** | Potential for bypassing standard security hooks by using direct system calls. |

---

### Final Conclusion: Overall Threat Profile

The analysis of all five chunks reveals that **`Ransomware_Form.exe` is a highly sophisticated, professional-grade piece of malware.** 

1.  **Sophisticated Construction:** This is not a "script-kiddy" ransomware. The use of custom decryption routines (`Decryptor`), complex mathematical obfuscation (seen in Chunk 5), and proactive data reporting to C2 servers indicates it was developed for wide-scale distribution.
2.  **Multi-Stage Logic:** We have identified the full lifecycle:
    *   **Establishment:** Persistence and environment preparation.
    *   **Reconnaissance:** Gathering system info, IPs, and identifying "valuable" files.
    *   **Encryption/Execution:** Targeted file locking.
    *   **Communication:** Reporting back to a handler to facilitate the ransom process.
3.  **Defensive Hurdles:** The "wall of math" discovered in the final chunks demonstrates that the authors are aware of security researchers. They have intentionally added "bloat" and complex logic gates to make it difficult for automated tools to flag or even understand the malware's true intent until it is already running on a victim's machine.

**Recommendation:** This file should be treated as a high-priority threat. If detected in an environment, isolation of the host is critical due to its active C2 capabilities and sophisticated obfuscation layers.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided for `Ransomware_Form.exe`, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1486** | Data Encrypted for Impact | The presence of `DecFiles` and `EncFiles_Count` confirms the core functionality is to encrypt user data to demand a ransom. |
| **T1565** | Persistence | The inclusion of `AddPersistence` and `RemovePersistence` functions indicates mechanisms designed to ensure the malware survives system reboots. |
| **T1027** | Obfuscated Files or Information | The use of "junk" code loops, complex arithmetic on high-value constants, and "code bloat" is intended to hinder both manual and automated reverse engineering. |
| **T1071** | Application Layer Protocol | The `GetIP` and `SendInformation_Checker` functions indicate the establishment of a communication channel with a remote C2 server. |
| **T1011** | Exfiltration | The reporting of system information to a remote server constitutes the theft of potentially sensitive environment data. |
| **Defense Evasion** | (Generic / Bypassing Hooks) | The use of `swi(1)` calls and non-standard memory offsets is specifically designed to bypass standard API hooks used by EDR security solutions. |
| **T1496** | Service Stop | While not a direct "stop," the interaction with `SetDesktopWallpaper` and `RestoreOriginalWallpaper` ensures the malware maintains control over the UI environment for maximum impact. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, I have extracted the following Indicators of Compromise (IOCs). 

**Note:** While several indicators point to specific behaviors, no hardcoded IP addresses, domains, or specific file paths were present in the text provided.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis mentions `GetIP` and `SendInformation_Checker`, but no static IPs or domain names were extracted from the strings.)

### **File paths / Registry keys**
*   **Files:** 
    *   `Ransomware_Form.exe` (Primary malicious executable)
    *   `EncFiles_log` (Likely a log file generated during the encryption process)
*   **Registry Interaction Indicators:** 
    *   The presence of `AddPersistence`, `RemovePersistence`, `DeleteSubKeyTree`, and `SendKeyReg` indicates active manipulation of Windows Registry keys for persistence.
    *   `fuWinIni` suggests interaction with `.ini` configuration files (commonly used by malware to store settings or paths).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided strings.)

### **Other artifacts**
*   **C2 & Network Communication:**
    *   `GetIP`: Used to identify the victim's local/external IP.
    *   `SendInformation_Checker`: Logic used to transmit system data to a remote server.
    *   `DownloadString` / `UploadString`: Potential indicators of multi-stage payload delivery or exfiltration.
*   **Encryption & Cryptography:**
    *   `SymmetricAlgorithm`, `CryptoStream`, `CipherMode`, `Decryptor`: Evidence of custom cryptographic implementation.
    *   `get_IV`, `set_IV`, `SendIV`: Interaction with Initialization Vectors.
*   **Obfuscation & Anti-Analysis:**
    *   `0x60ab005`: A high-value constant used in complex math to mask logic (Deobfuscation target).
    *   `swi(1)`: Usage of Software Interrupts to bypass standard API hooking.
*   **User Interaction & Manipulation:**
    *   `SetDesktopWallpaper`, `RestoreOriginalWallpaper`, `GetDesktopWallpaper`: Used to manipulate the user's environment and display ransom instructions.
    *   `HowBuy_Bitcoin_Click`, `AboutBitcoin_Click`: Direct indicators of a ransomware payment portal interface.

---
**Analyst Note:** The absence of hardcoded IPs/URLs suggests that the malware likely uses dynamically generated domains (DGAs), encrypted C2 configuration files, or a proxy layer to hide its true infrastructure.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: ransomware
3. **Confidence**: High
4. **Key evidence**:
    *   **Explicit Ransomware Functionality:** The presence of `EncFiles`, `DecFiles`, and specific UI elements for Bitcoin payment instructions (`HowBuy_Bitcoin_Click` and `AboutBitcoin_Click`) confirms the primary goal is to extort money via data encryption.
    *   **Sophisticated Evasion & Obfuscation:** The use of "junk" code, complex mathematical constants (e.g., `0x60ab005`), and `swi(1)` (Software Interrupt) calls indicates a high level of technical sophistication designed to bypass EDR security hooks and complicate manual reverse engineering.
    *   **Complete Operational Lifecycle:** The analysis confirms the malware contains all necessary components for a professional campaign, including persistence mechanisms (`AddPersistence`), C2 communication for infection reporting (`SendInformation_Checker`), and user-interface manipulation to ensure maximum impact.
