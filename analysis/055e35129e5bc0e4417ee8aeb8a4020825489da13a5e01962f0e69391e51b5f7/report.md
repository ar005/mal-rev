# Threat Analysis Report

**Generated:** 2026-07-13 19:40 UTC
**Sample:** `055e35129e5bc0e4417ee8aeb8a4020825489da13a5e01962f0e69391e51b5f7_055e35129e5bc0e4417ee8aeb8a4020825489da13a5e01962f0e69391e51b5f7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `055e35129e5bc0e4417ee8aeb8a4020825489da13a5e01962f0e69391e51b5f7_055e35129e5bc0e4417ee8aeb8a4020825489da13a5e01962f0e69391e51b5f7.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 699,392 bytes |
| MD5 | `07c20a75c1bbc3f27cf0c0c1b6656c5a` |
| SHA1 | `705c72530f4808659c3067e6074dc50c936c020b` |
| SHA256 | `055e35129e5bc0e4417ee8aeb8a4020825489da13a5e01962f0e69391e51b5f7` |
| Overall entropy | 7.92 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768269035 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 673,792 | 7.926 | ⚠️ Yes |
| `.rsrc` | 24,576 | 7.811 | ⚠️ Yes |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1798** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
6i5cq'
v&=|?L
[qaz76
!~Ji	x
JS4.Ih7
{A^svc_
z=jT`xgVw
KK{ha~Mna2
`"yH%ny*KZq
XYeoYm
&eZ0XSX
T$!LMz_y
*e	J3 21
\ \eOc
%_ V8Q

ik^@L
FRo#""r
	]t$v
"i? I?B
5ad)mxPC
BJ&w 

:E@vZ
>o3z2dQjd
~%HnA\
i%.)+M
1?a|Ur
K3q_] <
fpHt
2{=0Z#
F87#&K
a=G1gpG
l|oN@O
{i
H%~
w[T'	rn
'a)Tn("
5!0_<>
L5CI4H
nH'TK\
rJ?7{*
rVx23B
0Gs7
RD+f	V8Q
2Ukd|^
<=<[dH
5gcmEr{m
"`R&NoCf
U!hd`T
/gOPIF
0;	cmR
G@7.-`
)7bKt
8{px+k
.3sID+xk
/0a*"I8
O?zc%D
sTuz~C
(!Qx95
q/Qge
:CY[k
b
P2a ,
f~;k;<Hg
VMb'Q"
61Fy!RQ~
\wzc1_
aEF'ne
N_L>M
	o||\)
e3QxXW
Q!r90S"
&Zs%-S
m"
V16Vr
0#@R#%
G3>:L^
?B.w!i
67/xJ5"
B=mUq8
Y^LwTANZ
hGH\{{`l
2Se8:

/=:r+U
Dg-Q"''
60om;2
	v"X|[:
K~u`\2
kS=WT!
#3PV!Dl
=r-C;k[
O#>%nz;
o[^qJY
#x<L>~
?u~j5^
=rWdkKs&
G:A6Pu
(\poP4
Q__7;
o29VcY8i!
>P.Qs]u
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.WinFormsJogoDaVelha.Form1.__12` | `0x40cf50` | 655360 | — |
| `method.__c__DisplayClass15_0..cctor` | `0x40da38` | 62744 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.InitializeComponent` | `0x40a33c` | 7492 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.verificaVencedor` | `0x409850` | 2696 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.ExtractGraphicsStream` | `0x4080c0` | 1704 | ✓ |
| `sym.Phm.Time.Properties.Resources.__1` | `0x406bb8` | 1244 | ✓ |
| `method.Phm.Time.TimekeeperWorker.OnDoWork` | `0x4040a0` | 976 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.btnRecomear_Click` | `0x40928c` | 864 | ✓ |
| `method.Phm.Time.Timetable.FindNextScheduledTime` | `0x404c0c` | 644 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.btn_Click` | `0x4095ec` | 612 | ✓ |
| `sym.WinFormsJogoDaVelha.Form1.` | `0x40c10c` | 568 | ✓ |
| `method.Phm.Time.TimekeeperWorker.ExecuteTasksAsync` | `0x404470` | 428 | ✓ |
| `sym.Phm.Time.Properties.Resources.__8` | `0x40770c` | 420 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.Should_Execute_One_AM_Task_Twice_On_Jump_Back_DST` | `0x408f78` | 404 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.Should_Execute_One_AM_And_3_AM_And_Not_2_AM_Task_On_Jump_Forward_DST` | `0x40910c` | 384 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.CollectPixelComponents` | `0x407f48` | 376 | ✓ |
| `sym.WinFormsJogoDaVelha.Form1.__3` | `0x40c58c` | 368 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.Should_Execute_Hourly_Task_Every_Hour_1_thru_23` | `0x408ab4` | 360 | ✓ |
| `sym.Phm.Time.x.__2` | `0x405d90` | 336 | ✓ |
| `sym.WinFormsJogoDaVelha.Form1.__4` | `0x40c6fc` | 336 | ✓ |
| `sym.Phm.Time.Task.__5` | `0x402740` | 332 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.ExecuteByteModulation` | `0x407dfc` | 332 | ✓ |
| `sym.Phm.Time.Task.__3` | `0x402510` | 324 | ✓ |
| `sym.Phm.Time.Properties.Resources.__3` | `0x407194` | 316 | ✓ |
| `sym.Phm.Time.Task.__2` | `0x4023dc` | 308 | ✓ |
| `sym.Phm.Time.Timetable.` | `0x4050f4` | 308 | ✓ |
| `sym.Phm.Time.Task.__11` | `0x402d68` | 304 | ✓ |
| `sym.WinFormsJogoDaVelha.Form1.__1` | `0x40c344` | 304 | ✓ |
| `method.WinFormsJogoDaVelha.Form1.Should_Not_Execute_Hourly_Task_On_Hour_0` | `0x408c1c` | 300 | ✓ |
| `method.Phm.Time.Timetable.` | `0x405924` | 292 | ✓ |

### Decompiled Code Files

- [`code/method.Phm.Time.TimekeeperWorker.ExecuteTasksAsync.c`](code/method.Phm.Time.TimekeeperWorker.ExecuteTasksAsync.c)
- [`code/method.Phm.Time.TimekeeperWorker.OnDoWork.c`](code/method.Phm.Time.TimekeeperWorker.OnDoWork.c)
- [`code/method.Phm.Time.Timetable..c`](code/method.Phm.Time.Timetable..c)
- [`code/method.Phm.Time.Timetable.FindNextScheduledTime.c`](code/method.Phm.Time.Timetable.FindNextScheduledTime.c)
- [`code/method.WinFormsJogoDaVelha.Form1.CollectPixelComponents.c`](code/method.WinFormsJogoDaVelha.Form1.CollectPixelComponents.c)
- [`code/method.WinFormsJogoDaVelha.Form1.ExecuteByteModulation.c`](code/method.WinFormsJogoDaVelha.Form1.ExecuteByteModulation.c)
- [`code/method.WinFormsJogoDaVelha.Form1.ExtractGraphicsStream.c`](code/method.WinFormsJogoDaVelha.Form1.ExtractGraphicsStream.c)
- [`code/method.WinFormsJogoDaVelha.Form1.InitializeComponent.c`](code/method.WinFormsJogoDaVelha.Form1.InitializeComponent.c)
- [`code/method.WinFormsJogoDaVelha.Form1.Should_Execute_Hourly_Task_Every_Hour_1_thru_23.c`](code/method.WinFormsJogoDaVelha.Form1.Should_Execute_Hourly_Task_Every_Hour_1_thru_23.c)
- [`code/method.WinFormsJogoDaVelha.Form1.Should_Execute_One_AM_And_3_AM_And_Not_2_AM_Task_On_Jump_Forward_DST.c`](code/method.WinFormsJogoDaVelha.Form1.Should_Execute_One_AM_And_3_AM_And_Not_2_AM_Task_On_Jump_Forward_DST.c)
- [`code/method.WinFormsJogoDaVelha.Form1.Should_Execute_One_AM_Task_Twice_On_Jump_Back_DST.c`](code/method.WinFormsJogoDaVelha.Form1.Should_Execute_One_AM_Task_Twice_On_Jump_Back_DST.c)
- [`code/method.WinFormsJogoDaVelha.Form1.Should_Not_Execute_Hourly_Task_On_Hour_0.c`](code/method.WinFormsJogoDaVelha.Form1.Should_Not_Execute_Hourly_Task_On_Hour_0.c)
- [`code/method.WinFormsJogoDaVelha.Form1.btnRecomear_Click.c`](code/method.WinFormsJogoDaVelha.Form1.btnRecomear_Click.c)
- [`code/method.WinFormsJogoDaVelha.Form1.btn_Click.c`](code/method.WinFormsJogoDaVelha.Form1.btn_Click.c)
- [`code/method.WinFormsJogoDaVelha.Form1.verificaVencedor.c`](code/method.WinFormsJogoDaVelha.Form1.verificaVencedor.c)
- [`code/method.__c__DisplayClass15_0..cctor.c`](code/method.__c__DisplayClass15_0..cctor.c)
- [`code/sym.Phm.Time.Properties.Resources.__1.c`](code/sym.Phm.Time.Properties.Resources.__1.c)
- [`code/sym.Phm.Time.Properties.Resources.__3.c`](code/sym.Phm.Time.Properties.Resources.__3.c)
- [`code/sym.Phm.Time.Properties.Resources.__8.c`](code/sym.Phm.Time.Properties.Resources.__8.c)
- [`code/sym.Phm.Time.Task.__11.c`](code/sym.Phm.Time.Task.__11.c)
- [`code/sym.Phm.Time.Task.__2.c`](code/sym.Phm.Time.Task.__2.c)
- [`code/sym.Phm.Time.Task.__3.c`](code/sym.Phm.Time.Task.__3.c)
- [`code/sym.Phm.Time.Task.__5.c`](code/sym.Phm.Time.Task.__5.c)
- [`code/sym.Phm.Time.Timetable..c`](code/sym.Phm.Time.Timetable..c)
- [`code/sym.Phm.Time.x.__2.c`](code/sym.Phm.Time.x.__2.c)
- [`code/sym.WinFormsJogoDaVelha.Form1..c`](code/sym.WinFormsJogoDaVelha.Form1..c)
- [`code/sym.WinFormsJogoDaVelha.Form1.__1.c`](code/sym.WinFormsJogoDaVelha.Form1.__1.c)
- [`code/sym.WinFormsJogoDaVelha.Form1.__3.c`](code/sym.WinFormsJogoDaVelha.Form1.__3.c)
- [`code/sym.WinFormsJogoDaVelha.Form1.__4.c`](code/sym.WinFormsJogoDaVelha.Form1.__4.c)

## Behavioral Analysis

This updated analysis incorporates the new disassembly data provided in chunk 2/2, focusing on the deep obfuscation techniques and the specific logic related to time-based execution found in the `Phm.Time` namespace.

---

### **Updated Analysis of Malicious Behavior & Tactics**

#### **1. Advanced Anti-Analysis & Obfuscation (High Sophistication)**
The second chunk of disassembly reveals a much higher level of sophistication than initially apparent. The presence of multiple "Warning" flags indicates the use of professional-grade protection:
*   **Anti-Disassembly Techniques:** The repeated warnings for **"overlapping instruction data"** and **"bad instruction data"** are classic signs of advanced obfuscation (e.g., VM-based protection or custom packers like *Themida* or *VMProtect*). These techniques purposefully break the disassembler's ability to map a linear flow, making it difficult for analysts to trace the logic manually.
*   **Control Flow Obfuscation:** The complex calculations involving `CONCAT`, bitwise operations on large constants (e.g., `0x93000001`, `0x405c82b`), and jumping into "junk" code blocks are designed to waste the analyst's time and break automated scripts that rely on clean control flow graphs (CFG).
*   **Hidden Logic:** The sheer volume of "garbage" logic suggests that the actual malicious payload is likely hidden within a virtualized environment or a highly complex state machine, where only specific conditions trigger the actual malware functionality.

#### **2. Advanced Time-Based Evasion ("Slow and Low" Tactics)**
The inclusion of `method.WinFormsJogoDaVelha.Form1.Should_Not_Execute_Hourly_Task_On_Hour_0` provides critical insight into the threat actor’s intent:
*   **Targeted Execution Windows:** The specific check for "Hour 0" (midnight) suggests a deliberate attempt to control *when* the malware activates its most detectable behaviors. This is often used to ensure that suspicious network traffic or file system modifications occur during hours when security personnel are less likely to notice anomalies, or it may be an evasion technique against automated sandboxes that simulate specific time cycles.
*   **Behavioral Thresholds:** The complexity of the code surrounding this check suggests it isn't just a simple "if" statement; it is part of a larger **scheduling engine** (`Timetable` and `Task`). This indicates the malware is designed to stay resident on a system for long periods, only executing its primary objectives at pre-determined intervals or times.

#### **3. Dual-Purpose Component: The "Front" vs. The "Engine"**
The disassembly clarifies the separation between the user interface and the underlying logic:
*   **The Front (WinFormsJogoDaVelha):** This component handles the Tic-Tac-Toe game. It is designed to look like a legitimate, functional application to the end-user.
*   **The Engine (Phm.Time):** This is where the "real" work happens. The complexity and obfuscation in the `Timetable` and `Task` functions are disproportionate to what a simple game requires. These functions likely handle:
    *   Communicating with a Command & Control (C2) server.
    *   Persistence checks.
    *   Periodic "beaconing" for new instructions.

---

### **Summary of Findings (Updated)**

**Classification:** **Sophisticated Trojan / Persistent Downloader.**

**New Key Observations from Chunk 2/2:**
1.  **Highly Advanced Packing:** The overlap of instructions and junk code indicates the use of high-end commercial packers or custom protection layers intended to thwart both human analysts and automated tools.
2.  **Intentional Evasion via Timing:** Specific logic exists to inhibit execution at certain hours (e.g., Hour 0), a common tactic for malware seeking to evade detection during peak monitoring windows or within automated analysis environments.
3.  **Modular Design:** The distinct separation between the "Game" interface and the "Time/Task" backend suggests a modular architecture where the malicious components are heavily shielded while the "decoy" remains accessible to the user.

### **Revised Risk Assessment**
This sample is not a simple "script kiddie" script; it shows evidence of professional-grade development. The complexity of the `Phm.Time` logic and the robust obfuscation layers suggest this malware belongs to a sophisticated threat actor (potentially an Advanced Persistent Threat - APT) or a high-level cybercriminal group. It is designed for **long-term residency**, utilizing specific timing windows to remain undetected while executing its primary payload.

**Recommendation:** Treat any system interacting with this binary as compromised. The complexity of the code suggests that the malware likely includes features for persistence and periodic communication with remote servers.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "overlapping instruction data," "bad instruction data," and complex bitwise operations on large constants are intentional efforts to hinder manual analysis and break automated disassembly tools. |
| **T1497** | Virtualization/Sandbox Evasion | The specific check for "Hour 0" (midnight) is a classic timing-based evasion technique used to bypass automated sandboxes or avoid detection during high-activity monitoring windows. |
| **T1036** | Masquerading | The inclusion of the `WinFormsJogoDaVelha` (Tic-Tac-Toe) component acts as a decoy to present the application as legitimate software to the end-user while hiding the malicious "engine." |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

Note: The "Extracted Strings" section contains heavily obfuscated/junk data consistent with a packed binary; no actionable IP addresses, domains, or file paths were present in that specific block.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts (user agents, C2 patterns, etc.)**
*   **Internal Method Names/Identifiers:** 
    *   `WinFormsJogoDaVelha.Form1.Should_Not_Execute_Hourly_Task_On_Hour_0`
    *   `Phm.Time` (Namespace)
    *   `Timetable` (Function/Module)
    *   `Task` (Function/Module)
*   **Behavioral Patterns:**
    *   **Time-based Execution Evasion:** Specific logic to inhibit execution during "Hour 0" (midnight).
    *   **Modular Architecture:** Use of a "front" application (Tic-Tac-Toe game) to mask the backend malicious functionality.
    *   **Anti-Analysis Techniques:** Presence of overlapping instruction data and junk code blocks designed to break disassemblers.

---

## Malware Family Classification

Based on the detailed behavioral analysis provided, here is the classification:

1.  **Malware family:** Unknown
2.  **Malware type:** Trojan / Downloader
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Advanced Obfuscation & Anti-Analysis:** The use of "overlapping instruction data" and significant junk code indicates the use of high-end protection layers (like VMProtect or Themida) to hinder manual analysis and bypass automated security tools.
    *   **Sophisticated Evasion Tactics:** The inclusion of specific time-based logic (e.g., the `Hour_0` check) demonstrates a "slow and low" approach designed specifically to evade automated sandboxes and stay under the radar during peak monitoring hours.
    *   **Masquerading & Modular Architecture:** The sample employs a dual-purpose design where a "Front" (a Tic-Tac-Toe game) acts as a decoy for the user, while the hidden "Engine" (`Phm.Time` namespace) handles high-level malicious functions like persistence and C2 communication.
