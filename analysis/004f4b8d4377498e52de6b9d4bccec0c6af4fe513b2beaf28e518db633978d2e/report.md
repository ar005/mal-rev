# Threat Analysis Report

**Generated:** 2026-06-24 00:45 UTC
**Sample:** `004f4b8d4377498e52de6b9d4bccec0c6af4fe513b2beaf28e518db633978d2e_004f4b8d4377498e52de6b9d4bccec0c6af4fe513b2beaf28e518db633978d2e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `004f4b8d4377498e52de6b9d4bccec0c6af4fe513b2beaf28e518db633978d2e_004f4b8d4377498e52de6b9d4bccec0c6af4fe513b2beaf28e518db633978d2e.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 1,105,920 bytes |
| MD5 | `e05db9f6a6f5867675c27c9ed2fa529c` |
| SHA1 | `d2561ec173a3f1b2d0a4d269f9fd55ba5c75362f` |
| SHA256 | `004f4b8d4377498e52de6b9d4bccec0c6af4fe513b2beaf28e518db633978d2e` |
| Overall entropy | 7.829 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3533084023 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,096,704 | 7.837 | ⚠️ Yes |
| `.rsrc` | 8,192 | 5.614 | No |

## Extracted Strings

Total strings found: **2488** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
v4.0.30319
#Strings
Column10
2411C07A4A321B7A165A8203AC011C5A1A6EE5EE47EEED3968F809CCB9DB5690
Column11
IComparer`1
List`1
label1
get_Panel1
Column1
button1
toolStripSeparator1
dataGridView1
textBox1
Column12
ToInt32
Dictionary`2
label2
get_Panel2
Column2
button2
toolStripSeparator2
dataGridView2
textBox2
Column13
label3
Column3
button3
toolStripSeparator3
textBox3
Column14
label4
Column4
button4
textBox4
Column15
label5
Column5
button5
textBox5
label6
Column6
button6
textBox6
label7
Column7
button7
textBox7
label8
Column8
Column9
<Module>
<PrivateImplementationDetails>
mnuWindowTileH
get_pUqJ
System.IO
mnuWindowTileV
posada
HarvestBitmapData
get_SelectedTab
set_SelectedTab
EnsureTab
set_AcceptsTab
SelectTab
FromArgb
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
Thread
add_Load
Form_Load
add_TextChanged
child_TextChanged
add_SelectedIndexChanged
tabDocs_SelectedIndexChanged
get_Checked
set_Checked
set_Enabled
add_FormClosed
child_FormClosed
get_IsDisposed
get_Panel1Collapsed
set_Panel1Collapsed
get_Panel2Collapsed
set_Panel2Collapsed
Synchronized
AppendChild
get_ActiveMdiChild
_tabByChild
lblCmd
DataGridViewBand
txtCommand
Append
get_SplitterDistance
set_SplitterDistance
defaultInstance
btnCascade
mnuWindowCascade
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Baza_Kormit..ctor` | `0x14000698b` | 22108 | ✓ |
| `method.KursovaKutovyiForms.Form1.InitializeComponent` | `0x1400023f8` | 5540 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.SetStatus` | `0x140004e4f` | 4640 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.InitializeComponent` | `0x140004ee8` | 4528 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuViewToolbox_Click` | `0x14000462d` | 2082 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuFileNew_Click` | `0x140003df9` | 1570 | ✓ |
| `method.KursovaKutovyiForms.Properties.Settings..ctor` | `0x140003a57` | 930 | ✓ |
| `method.IndexedByteContainer..ctor` | `0x14000606f` | 676 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.RestoreLayout` | `0x140004b64` | 584 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuWindowTileV_Click` | `0x140004431` | 498 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.SaveLayout` | `0x1400049a4` | 448 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.WireEvents` | `0x140003bc4` | 436 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.RebuildWindowListMenu` | `0x140004478` | 368 | ✓ |
| `method.KursovaKutovyiForms.Form1.HarvestBitmapData` | `0x140002078` | 340 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.RebuildRecentMenu` | `0x1400047d8` | 324 | ✓ |
| `method.Baza_Kormit.add` | `0x1400065c4` | 312 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.txtCommand_KeyDown` | `0x140004314` | 274 | ✓ |
| `method.Baza_Kormit.sort1` | `0x140006880` | 267 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.CreateDocument` | `0x140003e54` | 248 | ✓ |
| `method.Baza_Kormit.show` | `0x1400066fc` | 228 | ✓ |
| `method.Baza_Kormit.rozr` | `0x1400064fc` | 200 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.listToolbox_DoubleClick` | `0x140004244` | 188 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.AddToMru` | `0x140004668` | 168 | ✓ |
| `method.AdvancedMdiExample.DocChildForm..ctor` | `0x140003a78` | 166 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.FillToolbox` | `0x1400041b4` | 144 | ✓ |
| `method.KursovaKutovyiForms.Form1.button1_Click` | `0x140002278` | 139 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.tabDocs_SelectedIndexChanged` | `0x1400040e0` | 136 | ✓ |
| `entry0` | `0x140003981` | 134 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.EnsureTab` | `0x140003f8c` | 132 | ✓ |
| `method.AdvancedMdiExample.AdvancedStudioMdiForm.LoadMru` | `0x140004710` | 128 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.AddToMru.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.AddToMru.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.CreateDocument.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.CreateDocument.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.EnsureTab.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.EnsureTab.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.FillToolbox.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.FillToolbox.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.InitializeComponent.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.InitializeComponent.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.LoadMru.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.LoadMru.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.RebuildRecentMenu.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.RebuildRecentMenu.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.RebuildWindowListMenu.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.RebuildWindowListMenu.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.RestoreLayout.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.RestoreLayout.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.SaveLayout.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.SaveLayout.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.SetStatus.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.SetStatus.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.WireEvents.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.WireEvents.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.listToolbox_DoubleClick.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.listToolbox_DoubleClick.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuFileNew_Click.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuFileNew_Click.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuViewToolbox_Click.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuViewToolbox_Click.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuWindowTileV_Click.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.mnuWindowTileV_Click.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.tabDocs_SelectedIndexChanged.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.tabDocs_SelectedIndexChanged.c)
- [`code/method.AdvancedMdiExample.AdvancedStudioMdiForm.txtCommand_KeyDown.c`](code/method.AdvancedMdiExample.AdvancedStudioMdiForm.txtCommand_KeyDown.c)
- [`code/method.AdvancedMdiExample.DocChildForm..ctor.c`](code/method.AdvancedMdiExample.DocChildForm..ctor.c)
- [`code/method.Baza_Kormit..ctor.c`](code/method.Baza_Kormit..ctor.c)
- [`code/method.Baza_Kormit.add.c`](code/method.Baza_Kormit.add.c)
- [`code/method.Baza_Kormit.rozr.c`](code/method.Baza_Kormit.rozr.c)
- [`code/method.Baza_Kormit.show.c`](code/method.Baza_Kormit.show.c)
- [`code/method.Baza_Kormit.sort1.c`](code/method.Baza_Kormit.sort1.c)
- [`code/method.IndexedByteContainer..ctor.c`](code/method.IndexedByteContainer..ctor.c)
- [`code/method.KursovaKutovyiForms.Form1.HarvestBitmapData.c`](code/method.KursovaKutovyiForms.Form1.HarvestBitmapData.c)
- [`code/method.KursovaKutovyiForms.Form1.InitializeComponent.c`](code/method.KursovaKutovyiForms.Form1.InitializeComponent.c)
- [`code/method.KursovaKutovyiForms.Form1.button1_Click.c`](code/method.KursovaKutovyiForms.Form1.button1_Click.c)
- [`code/method.KursovaKutovyiForms.Properties.Settings..ctor.c`](code/method.KursovaKutovyiForms.Properties.Settings..ctor.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a technical analysis of the binary sample.

### Core Functionality and Purpose
The sample appears to be a **malicious application (likely an Information Stealer or Trojan)** disguised as a standard Windows management utility or developer tool. 

While it contains references to standard UI elements (buttons, panels, and toolbars), the underlying logic is heavily obscured. The "AdvancedMdiExample" names suggest it was built using common templates to look like a legitimate multi-document interface application, but the inclusion of specific functions like `HarvestBitmapData` suggests its true purpose is to collect information from the user's system (such as screenshots or screen content).

### Suspicious and Malicious Behaviors
*   **Heavy Obfuscation & Junk Code:** The most prominent finding is the presence of "junk code." Many functions (e.g., `method.Baza_Kormit..ctor`, `mnuViewToolbox_Click`) contain complex, meaningless arithmetic and bitwise operations on arbitrary memory addresses. This is designed to frustrate automated decompilers and manual analysis by creating a labyrinth of code that does nothing but consume the analyst's time.
*   **Anti-Analysis Techniques:** The decompiler repeatedly flags "bad instruction data" and "overlapping instructions." This indicates the use of **instruction overlapping** or **junk byte insertion**. These techniques are specifically used to break static analysis tools (like Ghidra/IDA), causing them to fail at correctly identifying function boundaries or control flow.
*   **Potential Information Stealing:** The presence of the string `HarvestBitmapData` is a significant indicator of malicious intent. This often points toward capabilities for capturing screen data, potentially looking for sensitive information in visual formats (like login screens or personal documents).

### Notable Techniques and Patterns
*   **Obfuscated Control Flow:** Several functions show identical logic patterns despite having different names in the metadata (e.g., `mnuViewToolbox_Click`, `mnuFileNew_Click`, and `EnsureTab` all exhibit high levels of "junk" complexity). This suggests a **code mutation engine** was used to generate these functions, making it difficult to determine which parts of the code are functional and which are decoys.
*   **Opaque Predicates:** The use of complex calculations (like `(POPCOUNT(cVar1) & 1U) != 0`) to decide whether to enter a block of code is a common way to implement opaque predicates. These conditions always evaluate to the same result but are difficult for automated tools to simplify, hiding the "true" path of execution.
*   **Wrapper/Loader Behavior:** The structure suggests a "packer" or "wrapper" style construction where the malicious payload is hidden inside a standard-looking GUI shell (the MDI interface).

### Summary Checklist
*   **Malicious Intent:** Likely High (Obfuscation + Harvesting keywords).
*   **Anti-Analysis:** High (Junk code, overlapping instructions, decoys).
*   **Primary Capability:** Information theft / Credential harvesting.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&K framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Masquerading | The sample is intentionally disguised as a "standard Windows management utility or developer tool" to blend in with legitimate software. |
| **T1027** | Obfuscated Files or Information | The use of junk code, overlapping instructions, and opaque predicates is specifically designed to frustrate static analysis tools and hide the true execution path. |

### Analysis Notes:
*   **T1036 (Masquerading):** This covers both the "Disguised as a standard utility" aspect and the "Wrapper/Loader Behavior," where the malicious functionality is hidden behind a legitimate-looking GUI shell.
*   **T1027 (Obfuscated Files or Information):** This captures the three distinct anti-analysis behaviors mentioned: **Junk Code** (to waste analyst time), **Overlapping Instructions** (to break tool's ability to identify function boundaries), and **Opaque Predicates** (to hide true control flow logic).
*   **Note on "HarvestBitmapData":** While this indicates a capability for information theft (such as screen scraping), it is a functional goal of the malware rather than a specific delivery or evasion technique; it would typically be categorized under broader goals like **Credential Access** or **Information Theft**, but the behaviors described in your analysis specifically highlight the *protection* and *disguise* techniques.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   `QjFn.exe` (Identified as the primary malicious binary/executable)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `2411C07A4A321B7A165A8203AC011C5A1A6EE5EE47EEED3968F809CCB9DB5690` (Note: This is a high-entropy, 52-character hex string. While it does not match standard MD5 or SHA-1 lengths, it serves as a unique identifier/potential internal key for signature matching.)

**Other artifacts**
*   **Capability Indicator:** `HarvestBitmapData` (Identifies the specific function used for screen scraping or capturing image data).
*   **Technique Identifier:** "Overlapping instructions" and "Junk code" (Used to identify the evasion profile of the sample).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High

4. **Key evidence**:
*   **Information Harvesting Capabilities:** The inclusion of the `HarvestBitmapData` function is a strong indicator of screen-scraping capabilities, aimed at capturing sensitive visual information or credentials.
*   **Advanced Anti-Analysis Techniques:** The use of "junk code," "overlapping instructions," and "opaque predicates" indicates a sophisticated effort to evade automated analysis and hide malicious functionality from security researchers.
*   **Masquerading Tactics:** The sample utilizes an "AdvancedMdiExample" template to present as a legitimate management tool, providing a wrapper to conceal its primary purpose of data exfiltration.
