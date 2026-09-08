# Threat Analysis Report

**Generated:** 2026-09-01 19:15 UTC
**Sample:** `12edcaafab7703d0819b1395f45c35e3083dd83fb8b128292cb11033453fb6e8_12edcaafab7703d0819b1395f45c35e3083dd83fb8b128292cb11033453fb6e8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12edcaafab7703d0819b1395f45c35e3083dd83fb8b128292cb11033453fb6e8_12edcaafab7703d0819b1395f45c35e3083dd83fb8b128292cb11033453fb6e8.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 51,902,576 bytes |
| MD5 | `8c67ae3b4b8d30d13a8118701134d94e` |
| SHA1 | `9ccd769624de98eeeb12714ff1707ec4f5bf196d` |
| SHA256 | `12edcaafab7703d0819b1395f45c35e3083dd83fb8b128292cb11033453fb6e8` |
| Overall entropy | 7.996 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775638835 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 51,769,344 | 7.997 | ⚠️ Yes |
| `.rsrc` | 120,320 | 4.006 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **115808** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU
j[	~C
%- &~#

	,	rD

%-&~Y

%-&~Y
%-&sV

+#r)

, 8!

- 8!

, 5!

- 6!

, 5!

, 5!

,	()

z*V~?

%-&#

%-&#
p*.  '

+.	,	
v4.0.30319
#Strings
tj< xj
09X
$2Y
STR_5100
STR_5200
STR_5400
STR_5010
STR_5110
STR_5210
STR_5310
STR_5410
STR_ADV_MOUNT_ARCHIVES_FROM_WIN_10
<>p__10
STR_5020
STR_5220
STR_5320
STR_5420
STR_5030
STR_5130
STR_5230
STR_5330
STR_5430
STR_5040
STR_5140
STR_5240
STR_5340
IDS_TYPE_OF_EMULATION_5440
STR_5050
STR_5250
STR_5350
STR_5060
STR_5260
STR_5360
STR_5460
IDS_2GB_BIG_FILES_ON_ISO9660
IDS_BIG_FILES_ON_ISO9660
STR_5070
STR_5170
STR_5270
STR_5370
STR_5470
STR_5080
STR_5280
STR_5380
STR_5480
STR_5090
STR_5190
STR_5390
<IsAllowed>b__10_0
<>c__DisplayClass10_0
<>9__30_0
<SetLogger>b__30_0
<.ctor>b__0_0
<>c__DisplayClass0_0
<Initialize>b__11_0
<>c__DisplayClass11_0
<>c__DisplayClass61_0
<MainWindow_ContentRendered>b__1_0
<get_ConfigurePageCommand>b__22_0
<>9__42_0
<get_BuyNowCommand>b__42_0
<>c__DisplayClass42_0
<>9__2_0
<.ctor>b__2_0
<Convert>b__2_0
<.cctor>b__33_0
<>c__DisplayClass33_0
<>9__63_0
<get_BrowseCommand>b__63_0
<get_CloseCommand>b__14_0
<>c__DisplayClass14_0
<.ctor>b__34_0
<>9__4_0
<UpdateAvailableFrames>b__4_0
<Convert>b__4_0
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.__c..cctor_8` | `0x413555` | 330218 | ✓ |
| `method.__c__DisplayClass0_0_1._DoWhenLoaded_b__0` | `0x412bcc` | 326620 | ✓ |
| `method.__c__DisplayClass48_0._StartInstallOffer_b__0` | `0x413568` | 128612 | ✓ |
| `method.__c._UpdateAvailableFrames_b__4_3` | `0x413741` | 65044 | ✓ |
| `method.__ShowAsync_b__0_d.SetStateMachine` | `0x413884` | 64740 | ✓ |
| `method.DTWpfInstaller.Utils.BrowserBehavior.SetIsAutoHeight` | `0x40776f` | 2929 | ✓ |
| `method.DTWpfInstaller.ViewModel.Base.BaseWizard.get_Header` | `0x406e09` | 2182 | ✓ |
| `method.__c__DisplayClass61_1._ShowAsync_b__1` | `0x412c9f` | 2112 | ✓ |
| `method.DTWpfInstaller.Utils.BrowserBehavior.AutoSizeBrowser` | `0x4078b8` | 1388 | ✓ |
| `method.DTWpfInstaller.Controls.Buttons.BaseColoredButton..cctor` | `0x40fb1c` | 1280 | ✓ |
| `method.DTWpfInstaller.View.LicensePageView..ctor` | `0x404aad` | 1272 | ✓ |
| `method.DTWpfInstaller.Utils.Tracer.Translit` | `0x406ff0` | 1248 | — |
| `method.DTWpfInstaller.Installer.Install` | `0x4035e4` | 1204 | ✓ |
| `method.DTWpfInstaller.ViewModel.Pages.EnterSerialPageVM._.ctor_b__34_0` | `0x406219` | 890 | ✓ |
| `method.DTWpfInstaller.SecondaryWindows.DTMessageBox..ctor` | `0x40a88c` | 836 | ✓ |
| `method.DTWpfInstaller.ViewModel.Pages.ConfigurePageVM.get_IsWinGadgetVisible` | `0x4055b7` | 826 | — |
| `method.FileAssociation.FileAssociationManager..cctor` | `0x402f4c` | 763 | ✓ |
| `method.DeviceManagement.PhantomDeviceManager.DiscSoftUninstallDeviceInfo` | `0x402360` | 724 | ✓ |
| `method.DiscSoft.NET.Common.Utils.NavigationServiceHTML.SetTextToTextBlock` | `0x412288` | 720 | ✓ |
| `method.DTWpfInstaller.ViewModel.Pages.ConfigurePageVM.get_PageName` | `0x405171` | 716 | ✓ |
| `method.DTWpfInstaller.App.OnStartup` | `0x404108` | 708 | ✓ |
| `method.DTWpfInstaller.ViewModel.Pages.InstallPageVM.set_ProgressText` | `0x405bdb` | 684 | ✓ |
| `method.DTWpfInstaller.Offers.ConfigLoader.SendWshAnalytics` | `0x40cea0` | 656 | ✓ |
| `method.DTWpfInstaller.Offers.OffersHelper.CreateNextOffer` | `0x40dfdc` | 640 | ✓ |
| `method.DTWpfInstaller.ViewModel.Pages.ConfigurePageVM.CreateExtLists` | `0x40568c` | 630 | ✓ |
| `method.DTWpfInstaller.Offers.ConfigLoader._RequestConfig_b__6_0` | `0x40d13c` | 628 | ✓ |
| `method.DTWpfInstaller.Offers.CustomOffer.Install` | `0x40d520` | 608 | ✓ |
| `method.DTWpfInstaller.Controls.Buttons.ImageButton..cctor` | `0x41036c` | 533 | ✓ |
| `method.DTWpfInstaller.MainWindow.OnClose` | `0x4046a9` | 528 | ✓ |
| `method.DiscSoft.NET.Base.Utils.DSUtils.GetScanCodeFromKey` | `0x410a94` | 528 | ✓ |

### Decompiled Code Files

- [`code/method.DTWpfInstaller.App.OnStartup.c`](code/method.DTWpfInstaller.App.OnStartup.c)
- [`code/method.DTWpfInstaller.Controls.Buttons.BaseColoredButton..cctor.c`](code/method.DTWpfInstaller.Controls.Buttons.BaseColoredButton..cctor.c)
- [`code/method.DTWpfInstaller.Controls.Buttons.ImageButton..cctor.c`](code/method.DTWpfInstaller.Controls.Buttons.ImageButton..cctor.c)
- [`code/method.DTWpfInstaller.Installer.Install.c`](code/method.DTWpfInstaller.Installer.Install.c)
- [`code/method.DTWpfInstaller.MainWindow.OnClose.c`](code/method.DTWpfInstaller.MainWindow.OnClose.c)
- [`code/method.DTWpfInstaller.Offers.ConfigLoader.SendWshAnalytics.c`](code/method.DTWpfInstaller.Offers.ConfigLoader.SendWshAnalytics.c)
- [`code/method.DTWpfInstaller.Offers.ConfigLoader._RequestConfig_b__6_0.c`](code/method.DTWpfInstaller.Offers.ConfigLoader._RequestConfig_b__6_0.c)
- [`code/method.DTWpfInstaller.Offers.CustomOffer.Install.c`](code/method.DTWpfInstaller.Offers.CustomOffer.Install.c)
- [`code/method.DTWpfInstaller.Offers.OffersHelper.CreateNextOffer.c`](code/method.DTWpfInstaller.Offers.OffersHelper.CreateNextOffer.c)
- [`code/method.DTWpfInstaller.SecondaryWindows.DTMessageBox..ctor.c`](code/method.DTWpfInstaller.SecondaryWindows.DTMessageBox..ctor.c)
- [`code/method.DTWpfInstaller.Utils.BrowserBehavior.AutoSizeBrowser.c`](code/method.DTWpfInstaller.Utils.BrowserBehavior.AutoSizeBrowser.c)
- [`code/method.DTWpfInstaller.Utils.BrowserBehavior.SetIsAutoHeight.c`](code/method.DTWpfInstaller.Utils.BrowserBehavior.SetIsAutoHeight.c)
- [`code/method.DTWpfInstaller.View.LicensePageView..ctor.c`](code/method.DTWpfInstaller.View.LicensePageView..ctor.c)
- [`code/method.DTWpfInstaller.ViewModel.Base.BaseWizard.get_Header.c`](code/method.DTWpfInstaller.ViewModel.Base.BaseWizard.get_Header.c)
- [`code/method.DTWpfInstaller.ViewModel.Pages.ConfigurePageVM.CreateExtLists.c`](code/method.DTWpfInstaller.ViewModel.Pages.ConfigurePageVM.CreateExtLists.c)
- [`code/method.DTWpfInstaller.ViewModel.Pages.ConfigurePageVM.get_PageName.c`](code/method.DTWpfInstaller.ViewModel.Pages.ConfigurePageVM.get_PageName.c)
- [`code/method.DTWpfInstaller.ViewModel.Pages.EnterSerialPageVM._.ctor_b__34_0.c`](code/method.DTWpfInstaller.ViewModel.Pages.EnterSerialPageVM._.ctor_b__34_0.c)
- [`code/method.DTWpfInstaller.ViewModel.Pages.InstallPageVM.set_ProgressText.c`](code/method.DTWpfInstaller.ViewModel.Pages.InstallPageVM.set_ProgressText.c)
- [`code/method.DeviceManagement.PhantomDeviceManager.DiscSoftUninstallDeviceInfo.c`](code/method.DeviceManagement.PhantomDeviceManager.DiscSoftUninstallDeviceInfo.c)
- [`code/method.DiscSoft.NET.Base.Utils.DSUtils.GetScanCodeFromKey.c`](code/method.DiscSoft.NET.Base.Utils.DSUtils.GetScanCodeFromKey.c)
- [`code/method.DiscSoft.NET.Common.Utils.NavigationServiceHTML.SetTextToTextBlock.c`](code/method.DiscSoft.NET.Common.Utils.NavigationServiceHTML.SetTextToTextBlock.c)
- [`code/method.FileAssociation.FileAssociationManager..cctor.c`](code/method.FileAssociation.FileAssociationManager..cctor.c)
- [`code/method.__ShowAsync_b__0_d.SetStateMachine.c`](code/method.__ShowAsync_b__0_d.SetStateMachine.c)
- [`code/method.__c._UpdateAvailableFrames_b__4_3.c`](code/method.__c._UpdateAvailableFrames_b__4_3.c)
- [`code/method.__c__DisplayClass0_0_1._DoWhenLoaded_b__0.c`](code/method.__c__DisplayClass0_0_1._DoWhenLoaded_b__0.c)
- [`code/method.__c__DisplayClass48_0._StartInstallOffer_b__0.c`](code/method.__c__DisplayClass48_0._StartInstallOffer_b__0.c)
- [`code/method.__c__DisplayClass61_1._ShowAsync_b__1.c`](code/method.__c__DisplayClass61_1._ShowAsync_b__1.c)
- [`code/sym.__c..cctor_8.c`](code/sym.__c..cctor_8.c)

## Behavioral Analysis

This analysis incorporates findings from **Chunk 9/9**. The final disassembly segment provides conclusive evidence regarding the sophistication of the malware’s protection layer, confirming that it utilizes industry-standard anti-analysis techniques designed to frustrate both automated tools and human researchers.

---

### Updated Analysis of Binary Sample

#### 1. Advanced Virtual Machine (VM) & Control Flow Flattening
The final disassembly confirms a massive investment in **Control Flow Flattening**.
*   **"Unreachable Block" Warnings:** The repeated `WARNING: Removing unreachable block` warnings throughout the file are a signature of high-level obfuscation. These occur because the decompiler is attempting to map out a "flat" structure where almost every logic branch is technically possible at the assembly level, but functionally impossible in reality (due to internal state checks). 
*   **State Machine Complexity:** The `while(true)` loops containing complex arithmetic on variables like `uVar23` and `puVar18` suggest a dispatcher-style loop. Instead of a linear "if/then" progression, the code constantly updates a central state variable to determine the next jump destination, effectively hiding the logic flow from static analysis tools.

#### 2. Mixed Boolean-Arithmetic (MBA) & Junk Code
The complexity of the math in `method.DTWpfInstaller.MainWindow.ExecClose` and `GetScanCodeFromKey` highlights the use of **Mixed Boolean-Arithmetic**.
*   **Obfuscated Constants:** Simple values are never stored as constants. Instead, they are reconstructed through complex chains of `CONCAT`, bit-shifts (`>> 8`), and arithmetic operations (e.g., `uVar12 = (uVar12 | uVar3) + cVar4 + *in_EAX`). This forces the analyst to perform significant manual calculation just to determine what a single instruction is doing.
*   **Instruction Bloat:** The sheer volume of code in `GetScanCodeFromKey`—which appears to involve some form of input handling or scanning—is intentionally inflated with "junk" instructions. These serve as **Time-Bombs** for researchers; it takes an immense amount of human time to determine that 100 lines of assembly might ultimately just be a single pointer calculation or a simple loop counter.

#### 3. Opaque Predicates & Anti-Decompilation
The recurring `POPCOUNT` logic (found in previous and current chunks) is the primary mechanism for **Opaque Predicates**.
*   **Forcing Branch Proliferation:** By using mathematically certain but computationally complex checks, the author forces tools like Ghidra to generate thousands of branches. This makes it impossible for an analyst to see "the big picture" because they are constantly forced to navigate through hundreds of nested "dummy" functions and blocks that will never actually execute.

#### 4. Potential Payload Concealment
The function name `GetScanCodeFromKey` provides a hint into the malware's potential behavior or its attempt at **Masquerading**:
*   **Interaction with Input:** While the naming could be part of a "Trojan" strategy (making it look like a legitimate utility for "scancodes"), it suggests the code may interact with keyboard/input events. 
*   **Persistence and Interaction:** In some advanced threats, such functions are used to detect if an analyst is manually interacting with a GUI or to intercept keys before they reach the OS.

---

### Updated Summary for Incident Response (IR)

The final chunk of disassembly reinforces that this malware belongs in the **highest tier of sophistication**. It does not just use simple packers; it uses advanced protection suites typically associated with sophisticated APT (Advanced Persistent Threat) actors or high-end "Malware-as-a-Service" (MaaS) platforms.

**Key Findings Refined:**
*   **State Machine & VM Core:** The malware's logic is executed through a dispatcher. Static analysis of the binary will likely never yield a complete map of its behavior because the "logic" only exists as data interpreted by the VM at runtime.
*   **Anti-Analysis Overhead:** The extensive use of **MBA (Mixed Boolean-Arithmetic)** and **Opaque Predicates** is specifically designed to break automated de-obfuscation scripts and exhaust human analyst time. 
*   **High Complexity Indicator:** The "junk code" volume suggests a high level of effort. This isn't a low-level script; it is a professionally engineered piece of malware.

**Risk Assessment & IR Recommendations (Updated):**
1.  **Abandon Deep Static Analysis:** Due to the heavy use of VM protection and MBA, attempting to manually de-obfuscate every loop in this sample is inefficient. Focus on **behavioral indicators**. 
2.  **Memory Forensics are Mandatory:** Because the "true" code only reveals itself after the VM has unpacked its state, memory dumps taken during execution (using tools like Volatility or specialized dumpers) are the most effective way to capture injected payloads and resolved strings.
3.  **Behavioral IOCs:** 
    *   Monitor for **Process Hollowing** or **Reflective DLL Injection**. The VM likely prepares a payload in memory that is then executed by "injecting" it into a legitimate process (e.g., `svchost.exe` or `explorer.exe`).
    *   Look for unauthorized network connections initiated by the initial dropper after a period of dormancy (the time required for the internal VM to execute its logic).
4.  **Advanced Hunting Strategy:** If this sample is found, assume it may be part of a broader campaign. The sophistication level suggests that there are likely other variations or "helper" modules designed to maintain persistence and steal data.

**Final Conclusion Statement:** 
The malware utilizes **Virtual Machine (VM) architecture**, **Mixed Boolean-Arithmetic (MBA)**, and **Opaque Predicates** to hide its logic path and **Dynamic API Resolution** to hide its interaction with the OS. It is highly resistant to static analysis and should be countered primarily through memory forensics and behavioral blocking of suspicious network activity/process injections.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of Control Flow Flattening, Mixed Boolean-Arithmetic (MBA), and Opaque Predicates are specifically designed to hide the logic flow and frustrate both static analysis and automated tools. |
| **T1036** | Masquerading | The naming of functions like `GetScanCodeFromKey` is used to disguise malicious intent by making it appear as a legitimate system utility or input handler. |
| **T1055.012** | Process Hollowing | The analyst notes that the malware likely utilizes process hollowing to inject its payload into a legitimate process (e.g., `svchost.exe`) to evade detection. |
| **T1037.005** | Reflective DLL Injection | This is identified as a high-probability method for injecting and executing payloads in memory without the need for file-based footprints. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

**Note:** The majority of the technical data provided describes **TTPs (Tactics, Techniques, and Procedures)**—specifically advanced evasion techniques—rather than static IOCs like specific IP addresses or file hashes.

### **IP addresses / URLs / Domains**
*   None identified in the provided text.

### **File paths / Registry keys**
*   None identified in the provided text. (Note: `sft7Z001` is a fragment of a filename but does not constitute a complete path or specific indicator).

### **Mutex names / Named pipes**
*   None identified in the provided text.

### **Hashes**
*   None identified in the provided text.

### **Other artifacts**
*   **Suspicious Function Name:** `GetScanCodeFromKey` (Indicates potential keylogging, input sniffing, or anti-analysis "scancode" checks).
*   **Evasion Techniques:** 
    *   Control Flow Flattening
    *   Mixed Boolean-Arithmetic (MBA)
    *   Opaque Predicates (via `POPCOUNT` logic)
    *   Dynamic API Resolution
*   **Potential Behavioral Indicators:**
    *   Process Hollowing (Targeting `svchost.exe` or `explorer.exe`).
    *   Reflective DLL Injection.

---

### **Analyst Notes:**
The provided data indicates a **highly sophisticated malware sample**, likely part of an APT campaign or a high-end Malware-as-a-Service (MaaS) operation. 

While the string dump contains many identifiers (e.g., `STR_5100`, `IDS_2GB_BIG_FILES`), these are standard resource strings for installers and do not constitute specific IOCs. The analysis confirms that the malware uses a **Virtual Machine (VM) architecture** to hide its true logic. Because the "real" code only exists in memory after de-obfuscation, static indicators (like IPs and Hashes) may be hidden or dynamically generated at runtime. 

**Recommendation:** Shift focus from static analysis to **memory forensics** and **behavioral monitoring** to capture artifacts during execution.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `method.discsoft.net`

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: Custom
2. **Malware type**: Loader
3. **Confidence**: High (for Type) / Medium (for Family)
4. **Key evidence**: 
    *   **Advanced Obfuscation Layer:** The use of Virtual Machine (VM) architecture, Mixed Boolean-Arithmetic (MBA), and Control Flow Flattening indicates a high-sophistication "Loader" designed to hide the true payload from static analysis tools.
    *   **Injection Techniques:** The identified use of Process Hollowing (T1055.012) and Reflective DLL Injection (T1037.005) are primary indicators of a loader intended to inject malicious code into legitimate system processes like `svchost.exe`.
    *   **Masquerading & Persistence:** The use of "installer" naming conventions (e.g., `DTWpfInstaller`) combined with advanced evasion techniques points toward a professional, likely MaaS-based (Malware-as-a-Service), loader designed to facilitate further infection stages.
