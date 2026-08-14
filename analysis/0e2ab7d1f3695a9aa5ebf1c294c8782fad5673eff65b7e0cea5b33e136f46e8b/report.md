# Threat Analysis Report

**Generated:** 2026-08-11 18:53 UTC
**Sample:** `0e2ab7d1f3695a9aa5ebf1c294c8782fad5673eff65b7e0cea5b33e136f46e8b_0e2ab7d1f3695a9aa5ebf1c294c8782fad5673eff65b7e0cea5b33e136f46e8b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e2ab7d1f3695a9aa5ebf1c294c8782fad5673eff65b7e0cea5b33e136f46e8b_0e2ab7d1f3695a9aa5ebf1c294c8782fad5673eff65b7e0cea5b33e136f46e8b.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 821,248 bytes |
| MD5 | `bc9f6b481ceee95985c423d5d9fe7795` |
| SHA1 | `4546f57f723e6fe89896285ac4803f65b2fe0b65` |
| SHA256 | `0e2ab7d1f3695a9aa5ebf1c294c8782fad5673eff65b7e0cea5b33e136f46e8b` |
| Overall entropy | 7.707 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771221045 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 818,688 | 7.713 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.178 | No |
| `.reloc` | 512 | 0.098 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1948** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
"333?6
v4.0.30319
#Strings
<>9__35_0
<InitializeComponent>b__35_0
IEnumerable`1
Expression`1
ReadOnlyCollection`1
IList`1
get_Panel1
Func`2
get_Panel2
Func`3
<Module>
System.Drawing.Drawing2D
get_LCID
get_AF
System.IO
get_DWeQ
Lambda
btnYeniSayfa
btnPanoyaKopyala
btnKopyala
CizimeBasla
lblResimAciklama
lblMetinAciklama
btnYaziTanima
ExtractColorData
yeniNokta
FromArgb
mscorlib
btnKlasorAc
SilgiModuAc
System.Collections.Generic
Microsoft.VisualBasic
HandwritePad
Form1_Load
Form2_Load
Form3_Load
Form4_Load
add_Load
TryAdd
get_Checked
set_Checked
set_Enabled
set_DoubleBuffered
formatted
Synchronized
<NotAdi>k__BackingField
<CizgiKalinligi>k__BackingField
<MetinIcerigi>k__BackingField
<CizgiRengi>k__BackingField
<OlusturmaTarihi>k__BackingField
<OnizlemeResmi>k__BackingField
<TuvalYukseklik>k__BackingField
<TuvalGenislik>k__BackingField
<Noktalar>k__BackingField
<DosyaYolu>k__BackingField
threshold
get_Hand
Append
parseMethod
toStringMethod
GetMethod
Clipboard
suankiDarbe
FlatButtonAppearance
get_FlatAppearance
set_SplitterDistance
defaultInstance
set_AutoScaleMode
set_SizeMode
PictureBoxSizeMode
set_SmoothingMode
set_InterpolationMode
set_Image
sourceImage
FromImage
SetImage
get_Message
AddRange
MethodInfoCache
Invoke
Enumerable
IDisposable
RuntimeTypeHandle
GetTypeFromHandle
DrawRectangle
Single
btnYenile
Compile
chkTanimaEkle
GaleriyiYukle
DarbeSayisiniGuncelle
DurumGuncelle
TuvalBoyutuGuncelle
set_Title
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c._InitializeComponent_b__35_0` | `0x408bfb` | 25302 | ✓ |
| `method.HandwritePad.Form1.InitializeComponent` | `0x403a54` | 5151 | ✓ |
| `method.HandwritePad.Form4.InitializeComponent` | `0x407484` | 4716 | ✓ |
| `method.HandwritePad.Form2.InitializeComponent` | `0x405254` | 2406 | ✓ |
| `method.HandwritePad.Form3.InitializeComponent` | `0x40647c` | 2113 | ✓ |
| `method.HandwritePad.HandwritingEngine.DarbeAnaliz` | `0x4027f8` | 912 | ✓ |
| `method.HandwritePad.Form1.ExtractColorData` | `0x402f70` | 776 | ✓ |
| `method.HandwritePad.Form3.NotKartiOlustur` | `0x405d78` | 628 | ✓ |
| `method.HandwritePad.Form3.Kart_Click` | `0x4060ec` | 552 | ✓ |
| `method.HandwritePad.Form4.btnResimFarkliKaydet_Click` | `0x406e3c` | 488 | ✓ |
| `method.HandwritePad.HandwritingEngine.TuvaliYenidenCiz` | `0x4024cc` | 472 | ✓ |
| `method.HandwritePad.Form2.btnTanimaBaslat_Click` | `0x404f10` | 372 | ✓ |
| `method.HandwritePad.Form3.GaleriyiYukle` | `0x405c04` | 372 | — |
| `method.HandwritePad.Form1.btnRenk_Click` | `0x403788` | 364 | ✓ |
| `method.HandwritePad.Form4.btnMetinFarkliKaydet_Click` | `0x407104` | 280 | ✓ |
| `method.HandwritePad.HandwritingEngine.KayitliNotlariGetir` | `0x402cfc` | 276 | ✓ |
| `method.HandwritePad.Form4.btnHerIkisiKaydet_Click` | `0x4072d4` | 264 | ✓ |
| `method.HandwritePad.HandwritingEngine.DarbeSinirlari` | `0x402b88` | 260 | ✓ |
| `method.HandwritePad.Form2.btnMetniKaydet_Click` | `0x40511c` | 256 | ✓ |
| `method.HandwritePad.Form3.Kart_Paint` | `0x405fec` | 256 | ✓ |
| `method.HandwritePad.HandwritingEngine.CizimeDevam` | `0x402348` | 236 | ✓ |
| `method.HandwritePad.HandwritingEngine.TuvaliTemizle` | `0x40222c` | 232 | ✓ |
| `method.HandwritePad.Form1.btnOzelRenk_Click` | `0x4038f4` | 224 | ✓ |
| `method.HandwritePad.Form4.btnMetinKaydet_Click` | `0x407024` | 224 | ✓ |
| `method.HandwritePad.HandwritingEngine.YaziTanimaYap` | `0x402720` | 216 | ✓ |
| `method.HandwritePad.Form1.btnKalem_Click` | `0x4035a4` | 212 | ✓ |
| `method.HandwritePad.Form4.btnResimKaydet_Click` | `0x406d68` | 212 | ✓ |
| `method.HandwritePad.Form3.btnSeciliSil_Click` | `0x406314` | 208 | ✓ |
| `method.HandwritePad.Form1.btnSilgi_Click` | `0x403678` | 192 | — |
| `method.HandwritePad.Form4.MetinIcerigiOlustur` | `0x40721c` | 184 | ✓ |

### Decompiled Code Files

- [`code/method.HandwritePad.Form1.ExtractColorData.c`](code/method.HandwritePad.Form1.ExtractColorData.c)
- [`code/method.HandwritePad.Form1.InitializeComponent.c`](code/method.HandwritePad.Form1.InitializeComponent.c)
- [`code/method.HandwritePad.Form1.btnKalem_Click.c`](code/method.HandwritePad.Form1.btnKalem_Click.c)
- [`code/method.HandwritePad.Form1.btnOzelRenk_Click.c`](code/method.HandwritePad.Form1.btnOzelRenk_Click.c)
- [`code/method.HandwritePad.Form1.btnRenk_Click.c`](code/method.HandwritePad.Form1.btnRenk_Click.c)
- [`code/method.HandwritePad.Form2.InitializeComponent.c`](code/method.HandwritePad.Form2.InitializeComponent.c)
- [`code/method.HandwritePad.Form2.btnMetniKaydet_Click.c`](code/method.HandwritePad.Form2.btnMetniKaydet_Click.c)
- [`code/method.HandwritePad.Form2.btnTanimaBaslat_Click.c`](code/method.HandwritePad.Form2.btnTanimaBaslat_Click.c)
- [`code/method.HandwritePad.Form3.InitializeComponent.c`](code/method.HandwritePad.Form3.InitializeComponent.c)
- [`code/method.HandwritePad.Form3.Kart_Click.c`](code/method.HandwritePad.Form3.Kart_Click.c)
- [`code/method.HandwritePad.Form3.Kart_Paint.c`](code/method.HandwritePad.Form3.Kart_Paint.c)
- [`code/method.HandwritePad.Form3.NotKartiOlustur.c`](code/method.HandwritePad.Form3.NotKartiOlustur.c)
- [`code/method.HandwritePad.Form3.btnSeciliSil_Click.c`](code/method.HandwritePad.Form3.btnSeciliSil_Click.c)
- [`code/method.HandwritePad.Form4.InitializeComponent.c`](code/method.HandwritePad.Form4.InitializeComponent.c)
- [`code/method.HandwritePad.Form4.MetinIcerigiOlustur.c`](code/method.HandwritePad.Form4.MetinIcerigiOlustur.c)
- [`code/method.HandwritePad.Form4.btnHerIkisiKaydet_Click.c`](code/method.HandwritePad.Form4.btnHerIkisiKaydet_Click.c)
- [`code/method.HandwritePad.Form4.btnMetinFarkliKaydet_Click.c`](code/method.HandwritePad.Form4.btnMetinFarkliKaydet_Click.c)
- [`code/method.HandwritePad.Form4.btnMetinKaydet_Click.c`](code/method.HandwritePad.Form4.btnMetinKaydet_Click.c)
- [`code/method.HandwritePad.Form4.btnResimFarkliKaydet_Click.c`](code/method.HandwritePad.Form4.btnResimFarkliKaydet_Click.c)
- [`code/method.HandwritePad.Form4.btnResimKaydet_Click.c`](code/method.HandwritePad.Form4.btnResimKaydet_Click.c)
- [`code/method.HandwritePad.HandwritingEngine.CizimeDevam.c`](code/method.HandwritePad.HandwritingEngine.CizimeDevam.c)
- [`code/method.HandwritePad.HandwritingEngine.DarbeAnaliz.c`](code/method.HandwritePad.HandwritingEngine.DarbeAnaliz.c)
- [`code/method.HandwritePad.HandwritingEngine.DarbeSinirlari.c`](code/method.HandwritePad.HandwritingEngine.DarbeSinirlari.c)
- [`code/method.HandwritePad.HandwritingEngine.KayitliNotlariGetir.c`](code/method.HandwritePad.HandwritingEngine.KayitliNotlariGetir.c)
- [`code/method.HandwritePad.HandwritingEngine.TuvaliTemizle.c`](code/method.HandwritePad.HandwritingEngine.TuvaliTemizle.c)
- [`code/method.HandwritePad.HandwritingEngine.TuvaliYenidenCiz.c`](code/method.HandwritePad.HandwritingEngine.TuvaliYenidenCiz.c)
- [`code/method.HandwritePad.HandwritingEngine.YaziTanimaYap.c`](code/method.HandwritePad.HandwritingEngine.YaziTanimaYap.c)
- [`code/method.__c._InitializeComponent_b__35_0.c`](code/method.__c._InitializeComponent_b__35_0.c)

## Behavioral Analysis

This final analysis incorporates the fifth and final disassembly chunk (5/5) into the investigation of **HandwritePad**. The latest data confirms that the protection mechanisms are not localized to specific "sensitive" areas; rather, they are applied globally across all components of the application, from UI interactions to core processing logic.

### Final Comprehensive Analysis: HandwritePad (Chunk 5/5)

#### Core Functionality (Finalized Scope)
The inclusion of these final functions completes our map of the software’s capabilities and confirms how deeply they are buried within the obfuscation layer:

*   **Advanced Image Processing:** The presence of `btnResimKaydet_Click` (Save Image) alongside `btnMetinKaydet_Click` (Save Text) reinforces that this application handles both raw image data and structured text. The extreme complexity surrounding these functions suggests that any "save" action may involve complex encoding, compression, or encryption routines before hitting the disk.
*   **Core Engine Processing:** The function `YaziTanimaYap` (Make Writing/Handwriting) is a critical component of the "Handwriting Engine." This is likely the core algorithm that transforms text into stylized handwriting. Its heavy protection suggests it contains proprietary algorithms that the developers do not want replicated or analyzed.
*   **Tool Integration:** Functions like `btnKalem_Click` (Pen Click) and `btnOzelRenk_Click` (Special Color/Custom Color) represent the user-facing tools. The fact that even these "simple" UI interactions are wrapped in massive amounts of mathematical noise confirms a **uniform protection policy**.
*   **Content Generation:** `MetinIcerigiOlustur` (Create Text Content) indicates internal logic for processing data. Even though this is an internal helper function, it exhibits the same pattern of "instruction inflation" as the public-facing buttons.

#### Technical Observations & Obfuscation Markers
Chunk 5/5 provides the final pieces of evidence regarding the developer's intent to thwart analysis:

1.  **Systematic Anti-Disassembly:** The recurring `WARNING: Control flow encountered bad instruction data` and `overlapping instruction` errors across almost every function in this chunk (e.g., at `0x406617`, `0x4070fd`, `0x402834`, `0x403dc8`, and `0x406e3f`) are definitive markers of **anti-disassembly tactics**. By creating "overlapping" code, the developer ensures that a linear disassembler (like Ghidra or IDA) cannot accurately map the flow of logic. This forces a human analyst to spend hours manually cleaning segments that would otherwise be clear.
2.  **Massive Code Inflation:** The sheer scale of the `btnKalem_Click` and `YaziTanimaYap` functions is alarming. In a standard application, these functions would occupy dozens of lines; here, they are expanded into hundreds of lines of complex math (`CONCAT31`, `POP_COUNT`, `CARRY4`). This is designed to **exhaust the analyst**. It forces any security researcher to sift through thousands of "junk" instructions to find a single line of real logic.
3.  **Instructional Noise as a Shield:** The repeated use of complex, multi-step calculations for simple tasks (like choosing a color or using a pen) is a classic technique used in both high-end DRM and sophisticated malware to hide secondary behaviors (such as **keylogging, data exfiltration, or anti-debugging checks**) inside the "noise" of the primary application features.

#### Analysis of Specific Routines
*   **`btnMetinKaydet_Click` & `btnResimKaydet_Click`:** These are high-interest points because they handle data persistence. Because they are heavily obfuscated, it is currently impossible to determine if they perform standard saving or if they also transmit user data to a remote server.
*   **`YaziTanimaYap` (The Handwriting Core):** This is the "engine" of the app. The complexity here suggests either highly sophisticated geometry math or a very aggressive protection layer to prevent competitors from stealing the handwriting style logic.
*   **`btnKalem_Click`:** While it seems like a simple tool selection, the sheer amount of "unreachable blocks" and "overlapping instructions" in its vicinity suggests that this section of the code is heavily "muddled" to prevent any automated analysis of how the pen behaves on the canvas.

---

### Final Summary for Analysts
The completion of the disassembly (Chunk 5/5) confirms that **HandwritePad** utilizes a sophisticated, multi-layered protection suite. There is no distinction in the code between "simple" features and "complex" ones; every component is equally hidden behind high-complexity math and intentional anti-disassembly hurdles.

The transition from "dense logic" to **"intentional obfuscation"** is now fully confirmed. The repeated use of overlapping instructions means that automated tools will continue to provide incomplete or incorrect information regarding the program's flow.

**Security Risk Status: High (Persistent & Systematic Obfuscation)**
The primary risk remains the **lack of visibility**. Because the "Save" functions, "Handwriting Engine," and even basic tool buttons are all hidden behind a wall of noise, it is impossible to rule out the presence of a secondary payload or unauthorized data transmission during standard operations.

**Final Recommendations:**
1.  **Isolated Environment (Mandatory):** Due to the high level of obfuscation—a hallmark of both "hardened" commercial software and sophisticated malware—all interactions with this binary must occur in a completely isolated, non-networked virtual machine.
2.  **Dynamic Analysis over Static:** Since static analysis is being actively frustrated by code inflation and bad instruction data, focus on **behavioral monitoring**. Use tools like *Process Monitor (ProcMon)* to watch for file creation/deletion and *Wireshark* to monitor for any outbound network traffic when the "Save" buttons are clicked.
3.  **Memory Forensics:** Since the binary is hard to read on disk, perform memory dumps while the application is running. This may allow you to see "de-obfuscated" code in the RAM that was hidden by the anti-disassembly tricks on the disk.
4.  **API Hooking (Frida):** Use Frida to hook common Windows APIs related to file I/O and network connectivity. This will bypass the obfuscated "junk" code and show you exactly what the application does when a user attempts to save their work.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of "instruction inflation" and complex mathematical noise is a deliberate attempt to exhaust analysts and hide core logic. |
| T1027 | Obfuscated Files or Information | The presence of "overlapping instructions" and "bad instruction data" are specific anti-disassembly tactics designed to break linear disassembly tools like Ghidra or IDA Pro. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) and technical artifacts:

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: While `gvgx.exe` appears in the strings as a filename, no specific directory path was provided).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Executable Name:** `gvgx.exe` (Identified within the string dump).
*   **Suspicious Memory Offsets (Anti-Disassembly):** The following offsets were identified as containing "overlapping instructions" and "bad instruction data," used to hinder automated analysis:
    *   `0x406617`
    *   `0x4070fd`
    *   `0x402834`
    *   `0x403dc8`
    *   `0x406e3f`
*   **Suspicious Function Names:** The following functions were flagged as high-interest points due to heavy obfuscation and potential risk of secondary payloads (hidden data exfiltration/encryption):
    *   `btnResimKaydet_Click` (Potential data exfiltration point)
    *   `btnMetinKaydet_Click` (Potential data exfiltration point)
    *   `YaziTanimaYap` (Core logic heavily obscured by "instruction inflation")

---
**Analyst Note:** 
The analysis confirms a **High Risk** profile due to systematic, professional-grade obfuscation. While no clear network C2 infrastructure was revealed in the static strings, the use of "overlapping instructions" and "code inflation" (e.g., `CONCAT31`, `POP_COUNT`) suggests the binary is designed to hide its true behavior from automated security tools. Dynamic analysis via memory forensics and API hooking is recommended to confirm if the "Save" functions interact with external network endpoints.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: Trojan (potential Infostealer/Dropper)
3. **Confidence**: Medium-High
4. **Key evidence**:
    *   **Advanced Anti-Analysis Techniques:** The use of "overlapping instructions," "bad instruction data," and "instruction inflation" across the entire binary is a hallmark of sophisticated malware designed to thwart static analysis and frustrate human researchers.
    *   **Intentional Obfuscation of Data Handling:** The extreme complexity surrounding "Save" functions (`btnResimKaydet_Click` and `btnMetinKaydet_Click`) suggests these points are critical; they likely hide secondary behaviors such as data exfiltration or the loading of additional payloads.
    *   **Systematic Evasion Strategy:** Unlike some malware that only obfuscates its communication modules, this sample applies "uniform protection" to all features (even simple UI elements), indicating a high-level effort to mask its true functionality from automated security scanners.
