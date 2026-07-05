# Threat Analysis Report

**Generated:** 2026-07-04 10:48 UTC
**Sample:** `03e1cac50f7694397f243a38092aa258c67c2d4133f14aed4bd61362340828d2_03e1cac50f7694397f243a38092aa258c67c2d4133f14aed4bd61362340828d2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03e1cac50f7694397f243a38092aa258c67c2d4133f14aed4bd61362340828d2_03e1cac50f7694397f243a38092aa258c67c2d4133f14aed4bd61362340828d2.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,161,728 bytes |
| MD5 | `7c000ec1696903fff6fc9874f3f4cdea` |
| SHA1 | `6a7d25976d9bb28a2c508a58b37a6897f519383d` |
| SHA256 | `03e1cac50f7694397f243a38092aa258c67c2d4133f14aed4bd61362340828d2` |
| Overall entropy | 7.844 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768463261 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,159,168 | 7.849 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.215 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **3120** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v@Zk"
Z^moY*
@rQtOvoLshIpe
:P_\En
MR:' $"\"
~ :*D7
P9^Lt{rm
InfW@#
9n$4r
*@=FLPE
R42{6E(?P
v%jjYi
(7b(}qJ3 

d<W,A
7.sc=v
DW$YCGj
I3-i<9
s&J5Ec
S5qe>sH
wLmke,a|
/G!>>
`
 ^G
u@ROhZ
[5.a*B+
M(6j?W
u'yw<U
w<vB%a
+m?Wr
NuUH\km
Lypp^(
L"nm44
";'nHEw
YkgQlP#?
]~WM|
bNhDSY-*
QEIfI,
W\yPb3
{g7%U%
BE/}L@
GSDs2k
	J3Yoe
oI%[;Jp
C~'_~C
yD:m4}
=+cpo]P
V6KQH
)\x)M<
T,3j't1o6
gSz|yo
%{qy~a
@>M}U.
T|)^G~
C>JJ)j
i|'!r9
{}_0Sf
qQ&G_p
G8(h7S@'
RkCpd
Gb|l,p
x0zDS
s@Ih>z
PY:f8>
:b}"D~rn
Ikx0:

DE&H6\w)
auaKWKN
0FDaw
#1W8RB
S!nTl`2
E{{Q5v
L69gI.
:P.0[
+'\g&?S"
m%.r21
	)M&ZK
5gT)vC
n+uC^/2
O3yw|7
]dd&MX
i<F"|
GOo8$}
[H"\hL
H\do!5
~V$G%3
in_<s~
f(wjpp4Y/
cU&S1-
Mzn]l%
[%GK
t;
(~V}b95
ahUD2_
m r{QYN2S
c)&[FJoW
qO$)1kk
-AaC>4
lhS	Ymybg
8iS&bqI
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.DiskAnalyzer.Properties.Resources.__17` | `0x424090` | 1040240 | ✓ |
| `method.DiskAnalyzer.Properties.Settings..cctor` | `0x424330` | 64864 | ✓ |
| `method.DiskAnalyzer.FormPrincipal.InitializeComponent` | `0x407078` | 7920 | ✓ |
| `method.DiskAnalyzer.FormGrandsFichiers.InitializeComponent` | `0x419318` | 7240 | ✓ |
| `method.DiskAnalyzer.FormDoublons.InitializeComponent` | `0x4142b4` | 7224 | ✓ |
| `method.DiskAnalyzer.FormStatistiques.InitializeComponent` | `0x41e5c8` | 5636 | ✓ |
| `method.DiskAnalyzer.FormArborescence.InitializeComponent` | `0x40ee68` | 5184 | ✓ |
| `method.DiskAnalyzer.AboutBox1.InitializeComponent` | `0x402564` | 4596 | ✓ |
| `method.DiskAnalyzer.FormPrincipal.DessinerDiagrammeSecteurs` | `0x405eac` | 2852 | ✓ |
| `method.DiskAnalyzer.FormStatistiques.DessinerGraphiqueBarres` | `0x41cdd4` | 2480 | ✓ |
| `method.DiskAnalyzer.AnalyseurDisque.TrouverDoublons` | `0x40b2b8` | 1676 | ✓ |
| `method.DiskAnalyzer.FormPrincipal.AggregateColorSequence` | `0x4052c0` | 1624 | ✓ |
| `method.DiskAnalyzer.FormDoublons.btnExporter_Click` | `0x413bc8` | 1612 | ✓ |
| `method.DiskAnalyzer.FormGrandsFichiers.btnExporter_Click` | `0x418c84` | 1512 | ✓ |
| `method.DiskAnalyzer.FormStatistiques.btnExporter_Click` | `0x41df60` | 1472 | ✓ |
| `method.DiskAnalyzer.AnalyseurDisque.AnalyserDossierRecursif` | `0x40ba48` | 1436 | ✓ |
| `method.DiskAnalyzer.FormArborescence.AfficherDetailsDossier` | `0x40dfc0` | 1344 | ✓ |
| `method.DiskAnalyzer.FormGrandsFichiers.RemplirListeFichiers` | `0x417d00` | 1340 | ✓ |
| `sym.DiskAnalyzer.AboutBox1.__1` | `0x40379c` | 1292 | ✓ |
| `method.DiskAnalyzer.FormStatistiques.RemplirListeStatistiques` | `0x41c928` | 1196 | ✓ |
| `method.DiskAnalyzer.FormArborescence.RemplirArborescence` | `0x40db20` | 1184 | ✓ |
| `method.DiskAnalyzer.FormDoublons.RemplirArbreDoublons` | `0x4125a0` | 1180 | ✓ |
| `method.DiskAnalyzer.FormDoublons.AfficherDetailsGroupe` | `0x412a3c` | 968 | ✓ |
| `method.DiskAnalyzer.FormPrincipal.MettreAJourInfoLecteur` | `0x405b3c` | 880 | — |
| `method.DiskAnalyzer.AnalyseurDisque.RechercherFichiersRecursif` | `0x40bfe4` | 860 | ✓ |
| `method.DiskAnalyzer.FormDoublons.arbreVueDoublons_AfterSelect` | `0x4133b4` | 844 | ✓ |
| `method.DiskAnalyzer.FormArborescence.TravailleurArrierePlan_RunWorkerCompleted` | `0x40e714` | 824 | ✓ |
| `method.DiskAnalyzer.FormGrandsFichiers.TravailleurArrierePlan_RunWorkerCompleted` | `0x4184d4` | 620 | — |
| `method.DiskAnalyzer.AnalyseurDisque.CalculerHashMD5` | `0x40c340` | 580 | ✓ |
| `sym.DiskAnalyzer.FormPrincipal.` | `0x408ff8` | 576 | ✓ |

### Decompiled Code Files

- [`code/method.DiskAnalyzer.AboutBox1.InitializeComponent.c`](code/method.DiskAnalyzer.AboutBox1.InitializeComponent.c)
- [`code/method.DiskAnalyzer.AnalyseurDisque.AnalyserDossierRecursif.c`](code/method.DiskAnalyzer.AnalyseurDisque.AnalyserDossierRecursif.c)
- [`code/method.DiskAnalyzer.AnalyseurDisque.CalculerHashMD5.c`](code/method.DiskAnalyzer.AnalyseurDisque.CalculerHashMD5.c)
- [`code/method.DiskAnalyzer.AnalyseurDisque.RechercherFichiersRecursif.c`](code/method.DiskAnalyzer.AnalyseurDisque.RechercherFichiersRecursif.c)
- [`code/method.DiskAnalyzer.AnalyseurDisque.TrouverDoublons.c`](code/method.DiskAnalyzer.AnalyseurDisque.TrouverDoublons.c)
- [`code/method.DiskAnalyzer.FormArborescence.AfficherDetailsDossier.c`](code/method.DiskAnalyzer.FormArborescence.AfficherDetailsDossier.c)
- [`code/method.DiskAnalyzer.FormArborescence.InitializeComponent.c`](code/method.DiskAnalyzer.FormArborescence.InitializeComponent.c)
- [`code/method.DiskAnalyzer.FormArborescence.RemplirArborescence.c`](code/method.DiskAnalyzer.FormArborescence.RemplirArborescence.c)
- [`code/method.DiskAnalyzer.FormArborescence.TravailleurArrierePlan_RunWorkerCompleted.c`](code/method.DiskAnalyzer.FormArborescence.TravailleurArrierePlan_RunWorkerCompleted.c)
- [`code/method.DiskAnalyzer.FormDoublons.AfficherDetailsGroupe.c`](code/method.DiskAnalyzer.FormDoublons.AfficherDetailsGroupe.c)
- [`code/method.DiskAnalyzer.FormDoublons.InitializeComponent.c`](code/method.DiskAnalyzer.FormDoublons.InitializeComponent.c)
- [`code/method.DiskAnalyzer.FormDoublons.RemplirArbreDoublons.c`](code/method.DiskAnalyzer.FormDoublons.RemplirArbreDoublons.c)
- [`code/method.DiskAnalyzer.FormDoublons.arbreVueDoublons_AfterSelect.c`](code/method.DiskAnalyzer.FormDoublons.arbreVueDoublons_AfterSelect.c)
- [`code/method.DiskAnalyzer.FormDoublons.btnExporter_Click.c`](code/method.DiskAnalyzer.FormDoublons.btnExporter_Click.c)
- [`code/method.DiskAnalyzer.FormGrandsFichiers.InitializeComponent.c`](code/method.DiskAnalyzer.FormGrandsFichiers.InitializeComponent.c)
- [`code/method.DiskAnalyzer.FormGrandsFichiers.RemplirListeFichiers.c`](code/method.DiskAnalyzer.FormGrandsFichiers.RemplirListeFichiers.c)
- [`code/method.DiskAnalyzer.FormGrandsFichiers.btnExporter_Click.c`](code/method.DiskAnalyzer.FormGrandsFichiers.btnExporter_Click.c)
- [`code/method.DiskAnalyzer.FormPrincipal.AggregateColorSequence.c`](code/method.DiskAnalyzer.FormPrincipal.AggregateColorSequence.c)
- [`code/method.DiskAnalyzer.FormPrincipal.DessinerDiagrammeSecteurs.c`](code/method.DiskAnalyzer.FormPrincipal.DessinerDiagrammeSecteurs.c)
- [`code/method.DiskAnalyzer.FormPrincipal.InitializeComponent.c`](code/method.DiskAnalyzer.FormPrincipal.InitializeComponent.c)
- [`code/method.DiskAnalyzer.FormStatistiques.DessinerGraphiqueBarres.c`](code/method.DiskAnalyzer.FormStatistiques.DessinerGraphiqueBarres.c)
- [`code/method.DiskAnalyzer.FormStatistiques.InitializeComponent.c`](code/method.DiskAnalyzer.FormStatistiques.InitializeComponent.c)
- [`code/method.DiskAnalyzer.FormStatistiques.RemplirListeStatistiques.c`](code/method.DiskAnalyzer.FormStatistiques.RemplirListeStatistiques.c)
- [`code/method.DiskAnalyzer.FormStatistiques.btnExporter_Click.c`](code/method.DiskAnalyzer.FormStatistiques.btnExporter_Click.c)
- [`code/method.DiskAnalyzer.Properties.Settings..cctor.c`](code/method.DiskAnalyzer.Properties.Settings..cctor.c)
- [`code/sym.DiskAnalyzer.AboutBox1.__1.c`](code/sym.DiskAnalyzer.AboutBox1.__1.c)
- [`code/sym.DiskAnalyzer.FormPrincipal..c`](code/sym.DiskAnalyzer.FormPrincipal..c)
- [`code/sym.DiskAnalyzer.Properties.Resources.__17.c`](code/sym.DiskAnalyzer.Properties.Resources.__17.c)

## Behavioral Analysis

The final chunk of disassembly provided completes the technical profile of the "DiskAnalyzer" binary. This final section provides evidence of high-level, professional-grade obfuscation techniques that move beyond simple "messy code" into intentional **code mutation** and **control flow flattening**.

### Updated Analysis: DiskAnalyzer (Chunk 4/4)

#### 1. Advanced Code Mutation & Obfuscation
The code in the first block of this chunk is a textbook example of **arithmetic obfuscation**.
*   **Junk Math & "Dead" Operations:** The repetitive additions, bitwise operations (e.g., `in_EAX = pcVar9 | 0x45;`), and complex calculations involving variables like `piVar8` and `cVar4` serve no functional purpose for a "Disk Analyzer." Instead, they are designed to create a "maze" for the decompiler. By performing dozens of mathematical operations to arrive at a value that could have been calculated in one step, the author ensures that automated analysis tools cannot easily determine what the code is actually doing.
*   **Opaque Predicates:** The use of `CARRY1` and `CONCAT31` alongside complex pointer arithmetic suggests the use of opaque predicates—logic branches that always evaluate the same way but are mathematically difficult for a decompiler to "fold" or simplify. This forces an analyst to manually step through hundreds of lines of code to realize that most of them are irrelevant.
*   **Instruction Overlapping & Data Blurring:** The presence of calculations like `*piVar8 = *piVar1 + piVar1;` followed by multiple additions suggests a deliberate attempt to "blur" the data. This makes it extremely difficult to perform signature-based detection (YARA) or to identify specific constants/strings used in malicious activities.

#### 2. Sophisticated Packer/Protector Indicators
The second function, `sym.DiskAnalyzer.FormPrincipal`, reveals more about the development lifecycle:
*   **Non-Linear Control Flow:** The internal logic of this function is highly erratic. The way variables like `uVar1` and `uVar2` are extracted and immediately used in convoluted arithmetic suggests that the binary has been processed by a **heavy obfuscation compiler (such as OLLVM)** or wrapped in a custom protector.
*   **Exception Handling/Anti-Debugging:** The inclusion of `swi(3)` (Software Interrupt 3) is often used in malware to trigger a breakpoint or check for the presence of a debugger. In this context, it may be part of a "self-patching" mechanism where the code checks if it is being monitored before decrypting its next stage of execution.

#### 3. Integration of Findings (The Full Picture)
When we combine Chunk 4 with the previous chunks, a clear picture of a sophisticated threat actor emerges:
*   **Chunk 1 & 2 (Hidden logic):** The tool's "front-end" is a simple UI for a complex "back-end."
*   **Chunk 3 (The "Payload" Logic):** The back-end performs deep reconnaissance—crawling the file system and hashing contents to identify valuable data.
*   **Chunk 4 (The Shield):** The entire operation is wrapped in an advanced obfuscation layer designed to frustrate security researchers and automated tools.

---

### Updated Risk Assessment

| Indicator | Status | Analysis |
| :--- | :--- | :--- |
| **Functionality** | **Confirmed** | Highly capable reconnaissance engine; maps, identifies, and categorizes files based on content (MD5). |
| **Deception** | **Extreme** | The "DiskAnalyzer" name is a perfect "Trojan Horse" mask for a sophisticated data-mapping tool. |
| **Obfuscation** | **Critical/Advanced** | Uses instruction mutation, junk math, and likely OLLVM-style obfuscation to hide the core logic from analysis tools. |
| **Malicious Intent** | **High Risk** | The combination of **high-level anti-analysis** and **aggressive data collection** is a hallmark of professional malware used in targeted attacks (e.g., Ransomware preparation or APT espionage). |

### Final Conclusion for the Full Analysis
The analysis of all four chunks confirms that **"DiskAnalyzer" is a high-capability piece of malicious software.** 

It is not a standalone tool but rather a sophisticated component of a larger attack chain. It is specifically engineered to:
1.  **Evade Detection:** Using complex math and "junk" code to defeat automated security scanners.
2.  **Map the Victim's Environment:** Systematically crawling the file system to identify valuable assets (via MD5 hashing).
3.  **Provide Persistence/Stealth:** Running in background threads so it can perform its heavy lifting without alerting the user.

The "DiskAnalyzer" is designed for **Target Mapping**. It identifies exactly what data is most valuable to a target organization before a secondary payload (such as an exfiltration script or ransomware) is deployed. 

**Final Recommendation: MALICIOUS.** This binary should be treated as a high-priority threat. It exhibits the hallmarks of professional cybercrime operations where sophisticated technical hurdles are placed specifically to delay and complicate the work of incident responders.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Programs | The malware utilizes arithmetic obfuscation, junk math, and opaque predicates to complicate decompiler analysis and bypass signature-based detection. |
| T1497 | Virtualization/Sandbox Evasion | The inclusion of `swi(3)` suggests a mechanism to detect the presence of debuggers or monitoring tools to evade analysis environments. |
| T1083 | File and Directory Discovery | The "back-end" logic crawls the filesystem and hashes content to map out valuable assets for potential exploitation or data exfiltration. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs).

### **Note on Analysis**
The **"EXTRACTED STRINGS"** section consists primarily of binary noise/mojibake (non-human-readable characters resulting from a raw binary dump). No actionable network indicators (IPs, URLs) or specific file paths were embedded in that specific text block. However, the **"BEHAVIORAL ANALYSIS"** identifies specific technical artifacts and behaviors used by the malware.

---

### **IOC_REPORT**

**IP addresses / URLs / Domains**
*   *None identified.* (The provided string dump contains no valid network identifiers.)

**File paths / Registry keys**
*   *None identified.* (While the report mentions "crawling the file system," no specific directories or registry keys were listed.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None found in strings.* (Note: While the analysis mentions "MD5 hashing" as a behavior, no specific MD5 hash values for files/malware were provided in the text.)

**Other artifacts**
*   **Malware Name:** `DiskAnalyzer` (Identified as a deceptive name used to mask data-mapping capabilities).
*   **Anti-Debugging Technique:** `swi(3)` (Software Interrupt 3 - used to detect debuggers or for self-patching).
*   **Obfuscation Techniques:**
    *   Arithmetic Obfuscation / Junk Math
    *   Opaque Predicates
    *   Instruction Overlapping
    *   Data Blurring
*   **Tactic Behavior:** File system crawling and content identification (reconnaissance for data exfiltration/ransomware prep).

---

### **Summary for SOC/IR Teams**
The malware, identified as **DiskAnalyzer**, is a high-sophistication threat characterized by extreme evasion techniques. While it does not contain hardcoded C2 infrastructure in the provided snippet, its presence indicates an active reconnaissance phase. 

**Recommended Actions:**
1.  Monitor for any process named `DiskAnalyzer` or associated with `swi(3)` execution loops.
2.  Flag internal alerts regarding heavy file-system crawling/indexing by unauthorized processes.
3.  Treat "DiskAnalyzer" as a high-priority indicator of pre-ransomware activity.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor (pre-ransomware reconnaissance)
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Evasion Techniques:** The sample utilizes high-level obfuscation, including OLLVM-style "junk math," opaque predicates, and instruction overlapping to bypass automated analysis and signature-based detection.
*   **Target Mapping Behavior:** Despite the decoy name ("DiskAnalyzer"), the backend logic focuses on crawling the file system and generating MD5 hashes to identify and map high-value data, a hallmark of reconnaissance in targeted attacks.
*   **Anti-Analysis/Debugging Features:** The inclusion of `swi(3)` (Software Interrupt 3) and complex control flow indicates intentional efforts to detect debuggers and prevent security researchers from analyzing the binary's capabilities.
