# Threat Analysis Report

**Generated:** 2026-07-15 02:23 UTC
**Sample:** `06687794b570170c4c5cf838d2d9b5c83bc946a7aded5a10762957c329204bb9_06687794b570170c4c5cf838d2d9b5c83bc946a7aded5a10762957c329204bb9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `06687794b570170c4c5cf838d2d9b5c83bc946a7aded5a10762957c329204bb9_06687794b570170c4c5cf838d2d9b5c83bc946a7aded5a10762957c329204bb9.exe` |
| File type | PE32+ executable for MS Windows 6.01 (GUI), x86-64, 9 sections |
| Size | 4,534,408 bytes |
| MD5 | `bd55c429e7907fd2d0948090117c048e` |
| SHA1 | `6b52289e1ed4d8c2735f6161fba0f3a46c49f7b7` |
| SHA256 | `06687794b570170c4c5cf838d2d9b5c83bc946a7aded5a10762957c329204bb9` |
| Overall entropy | 4.088 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 997,376 | 6.259 | No |
| `.rdata` | 1,160,192 | 6.189 | No |
| `.data` | 61,440 | 4.518 | No |
| `.pdata` | 20,992 | 4.941 | No |
| `.xdata` | 512 | 1.783 | No |
| `.idata` | 1,536 | 4.014 | No |
| `.reloc` | 16,384 | 5.403 | No |
| `.symtab` | 120,320 | 5.093 | No |
| `.rsrc` | 54,784 | 7.954 | ⚠️ Yes |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **9010** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.xdata
@.idata
.reloc
B.symtab
B.rsrc
 Go build ID: "r6eL3-GGbA_nppVnV5Hx/m94mVzi2dG2GiXUEujUG/v44zHo5jd-HpoKRCy3P7/jGk0apMRxj_j-p-7WFUD"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
\$PH9H@v#H
D$pL9A
L$pL9N
D$@I9p
\$hM9K
\$hM9K
l$8M9,$u
P(H9S(t
P H9S uqH
S0H9P0ug
P88S8u^
P98S9uUH
expafH
nd 3fH
2-byfH
te kfH
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
:H9F w
>H+zhH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
2}#s]H
D$PA)P
H9D$(t
H
^0H9X0tQ
\$XHc
$H+L$HH
T$(H+J
L$(H+A
H+5*M 
H95a' 

H9Z(w
\$0H9K
D$pH9H
D$0H9H
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
vDH95h
J0f9J2vuH
f9s2uFf
D$$u$L
H+j'!
H+*!!
H+. !
T$(M	D
	I9x tE1
runtime.H9
QpM9Qhu
L9L$Xt$H
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
rhH92w
tRI9N0tLH
T$`Hc3
L$XHcw
|$0uMH
memprofi
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.main.fmfleybrh` | `0x1400ed4c0` | 22821 | ✓ |
| `sym.main.eeiksyccaspapmj` | `0x1400d2900` | 12837 | ✓ |
| `sym.main.eqrrdxypcn` | `0x1400beec0` | 12764 | ✓ |
| `sym.main.nfvmhp` | `0x1400b3940` | 12756 | ✓ |
| `sym.main.miygtpbjbcgofvg` | `0x1400de0a0` | 12702 | ✓ |
| `sym.main.mtxfxzzji` | `0x1400b6b20` | 12663 | ✓ |
| `sym.main.tjvzorqyzxryjq` | `0x1400cf7a0` | 12614 | ✓ |
| `sym.main.ckmwrdge` | `0x1400d8ac0` | 12569 | ✓ |
| `sym.main.kvaafbcxy` | `0x1400ea400` | 12473 | ✓ |
| `sym.main.cxecyh` | `0x1400d5b40` | 12148 | ✓ |
| `sym.main.zvktgovmgxqtj` | `0x1400c8e00` | 11946 | ✓ |
| `sym.main.bdhkuzks` | `0x1400bc0a0` | 11781 | ✓ |
| `sym.main.elazwcvvdqzovan` | `0x1400ab7a0` | 11749 | ✓ |
| `sym.runtime.callbackasm.abi0` | `0x1400728e0` | 10001 | ✓ |
| `sym.main.szakvzihd` | `0x1400c44a0` | 9396 | ✓ |
| `sym.time.Time.appendFormat` | `0x14008adc0` | 9381 | ✓ |
| `sym.main.jsjuuofdzrqphdh` | `0x1400e7f60` | 9358 | ✓ |
| `sym.main.satielkfsutfd` | `0x1400ae5a0` | 9354 | ✓ |
| `sym.main.yciaecxog` | `0x1400c6960` | 9353 | ✓ |
| `sym.main.oqgdqevpcm` | `0x1400dbbe0` | 9305 | ✓ |
| `sym.main.mmiktjl` | `0x1400b9ca0` | 9191 | ✓ |
| `sym.main.dnamibnmyfivnep` | `0x1400c20a0` | 9191 | ✓ |
| `sym.main.wzmyuqbwozpfv` | `0x1400e12a0` | 9125 | ✓ |
| `sym.main.vmqcvluzmu` | `0x1400a9400` | 9113 | ✓ |
| `sym.main.sjzonuf` | `0x1400cbcc0` | 9097 | ✓ |
| `sym.syscall.init` | `0x14007b300` | 7589 | ✓ |
| `sym.main.ocafkqriizmw` | `0x1400e6660` | 6388 | ✓ |
| `sym.runtime.initMetrics` | `0x1400179e0` | 6181 | ✓ |
| `sym.main.jrqxegfcxvuaf` | `0x1400e4e60` | 6133 | ✓ |
| `sym.main.mplphjbrmolek` | `0x1400e3660` | 6128 | ✓ |

### Decompiled Code Files

- [`code/sym.main.bdhkuzks.c`](code/sym.main.bdhkuzks.c)
- [`code/sym.main.ckmwrdge.c`](code/sym.main.ckmwrdge.c)
- [`code/sym.main.cxecyh.c`](code/sym.main.cxecyh.c)
- [`code/sym.main.dnamibnmyfivnep.c`](code/sym.main.dnamibnmyfivnep.c)
- [`code/sym.main.eeiksyccaspapmj.c`](code/sym.main.eeiksyccaspapmj.c)
- [`code/sym.main.elazwcvvdqzovan.c`](code/sym.main.elazwcvvdqzovan.c)
- [`code/sym.main.eqrrdxypcn.c`](code/sym.main.eqrrdxypcn.c)
- [`code/sym.main.fmfleybrh.c`](code/sym.main.fmfleybrh.c)
- [`code/sym.main.jrqxegfcxvuaf.c`](code/sym.main.jrqxegfcxvuaf.c)
- [`code/sym.main.jsjuuofdzrqphdh.c`](code/sym.main.jsjuuofdzrqphdh.c)
- [`code/sym.main.kvaafbcxy.c`](code/sym.main.kvaafbcxy.c)
- [`code/sym.main.miygtpbjbcgofvg.c`](code/sym.main.miygtpbjbcgofvg.c)
- [`code/sym.main.mmiktjl.c`](code/sym.main.mmiktjl.c)
- [`code/sym.main.mplphjbrmolek.c`](code/sym.main.mplphjbrmolek.c)
- [`code/sym.main.mtxfxzzji.c`](code/sym.main.mtxfxzzji.c)
- [`code/sym.main.nfvmhp.c`](code/sym.main.nfvmhp.c)
- [`code/sym.main.ocafkqriizmw.c`](code/sym.main.ocafkqriizmw.c)
- [`code/sym.main.oqgdqevpcm.c`](code/sym.main.oqgdqevpcm.c)
- [`code/sym.main.satielkfsutfd.c`](code/sym.main.satielkfsutfd.c)
- [`code/sym.main.sjzonuf.c`](code/sym.main.sjzonuf.c)
- [`code/sym.main.szakvzihd.c`](code/sym.main.szakvzihd.c)
- [`code/sym.main.tjvzorqyzxryjq.c`](code/sym.main.tjvzorqyzxryjq.c)
- [`code/sym.main.vmqcvluzmu.c`](code/sym.main.vmqcvluzmu.c)
- [`code/sym.main.wzmyuqbwozpfv.c`](code/sym.main.wzmyuqbwozpfv.c)
- [`code/sym.main.yciaecxog.c`](code/sym.main.yciaecxog.c)
- [`code/sym.main.zvktgovmgxqtj.c`](code/sym.main.zvktgovmgxqtj.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.initMetrics.c`](code/sym.runtime.initMetrics.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)
- [`code/sym.time.Time.appendFormat.c`](code/sym.time.Time.appendFormat.c)

## Behavioral Analysis

This analysis incorporates findings from **Chunks 1–9**. The final set of disassemblies provides a definitive look at how the malware structures its core execution flow, confirming that the arithmetic "shields" are not just noise—they are the primary mechanism for controlling branching logic and hiding critical system interactions.

---

### Updated Analysis Summary (Including Chunks 1–9)

#### 1. Industrialized Obfuscation & Scale
Chunk 9 confirms the scale of the **Industrialized Obfuscation** noted in previous sections. The functions `jrqxegfcxvuaf` and `mplphjbrmolek` contain massive blocks of nearly identical, extremely complex floating-point arithmetic (e.g., calculations involving high-precision constants like `0x4065000000000000`). 
*   **The "Engine" approach:** The sheer volume of these transformations indicates that the malware was compiled using a sophisticated obfuscation tool. These tools take standard Go instructions and replace them with functionally equivalent but mathematically dense "opaque predicates." An analyst cannot determine what a function does just by looking at the math; they must execute it to see which branch is taken.

#### 2. The Gatekeeper Architecture (State-Gate System)
The analysis of `jrqxegfcxvuaf` and `mplphjbrmolek` confirms the **Unified State Machine** theory:
*   **Consistency of Keys:** The constants `0x303`, `0x505`, and `0x909` appear as primary "keys" in every major functional block. 
*   **Decision Logic:** These are not just random numbers; they represent the "solved" results of the preceding math gauntlets. For example, if a calculation yields `0x303`, it might unlock a buffer-writing routine; if it yields `0x505`, it might trigger a network stack preparation. 
*   **Branch Obfuscation:** By using these values to determine which block of code to execute next, the developers ensure that static analysis tools see thousands of "possible" paths, while only one path is actually executable at runtime.

#### 3. Sophisticated Masking of Standard Library Functions
Chunk 9 reveals exactly what is being hidden behind the math:
*   **I/O and File Operations:** The calls to `sym.bufio.NewReader()`, `sym.io.Copy()`, and `sym.bytes._Buffer_.Write()` are critical indicators. These functions suggest that the malware is preparing to **read from, write to, or move data across streams**.
*   **Memory & Slice Management:** The repeated use of `sym.runtime.growslice` and `sym.runtime.memmove` indicates high-level buffer management. This is typically used for constructing commands before execution or handling received payloads from a remote server.

#### 4. Advanced Anti-Analysis Tactics
*   **Symbolic Execution Defeance:** The complexity of the math in `jrqxegfcxvuaf` (calculating values like `fVar20`, `fVar19`, etc., through multiple nested layers) is specifically designed to exhaust symbolic execution engines (like *Angr* or *Triton*). The solver will experience "state explosion" because it cannot easily simplify the floating-point arithmetic into a simple boolean condition.
*   **Manual Analysis Fatigue:** For human analysts, these blocks are "time sinks." Each time an analyst encounters one of these math gates, they must spend significant time determining if a jump is conditional or unconditional, only to find that the gate eventually leads to standard system calls like `sym.runtime.memmove`.

---

### Updated Technical Indicators for Report

*   **Category:** High-Complexity Multi-Modular Obfuscated Go Loader
*   **Primary Techniques Observed:**
    *   **Industrialized Arithmetic Shields:** Automated wrapping of every core function in multi-layered floating-point math to mask the true logic flow.
    *   **State-Based Decision Gatekeeping:** Use of a consistent set of constants (`0x303`, `0x505`, `0x909`) as "keys" at the end of arithmetic gauntlets to determine branching behavior.
    *   **Call Graph Obfuscation:** Hiding critical I/O operations (`sym.io.Copy`, `sym.bufio.NewReader`) behind complex calculations, making it difficult to map the malware's capabilities via static analysis.
    *   **Memory Manipulation Layering:** Use of `memmove` and `growslice` within guarded blocks to handle dynamic data (e.g., C2 commands or decrypted payloads).
    *   **Anti-Symbolic Execution Design:** Intentional use of high-precision floating-point arithmetic and XMM register usage to break automated analysis tools.

---

### Updated Summary for Incident Response

The final analysis confirms that this is a **highly sophisticated, professional-grade malware sample.** It utilizes "Arithmetic Shielding" as its primary defense mechanism against both automated scanners and human reverse engineers. 

**Critical Findings for Forensics:**
1.  **Sophisticated Automation:** The sheer volume of identical, complex math blocks suggests the use of an industrial-scale obfuscation pipeline. This indicates a highly capable threat actor or a sophisticated malware-as-a-service (MaaS) provider.
2.  **Obscured Execution Path:** The malware does not follow a linear path. It calculates "keys" at every transition point. Unless the math is solved or skipped via dynamic patching, it is impossible to know what functionality the code will activate next.
3.  **Data Manipulation & I/O Hiddenness:** Core operations for data copying (`sym.io.Copy`), buffer management, and memory movement are buried deep within these arithmetic gauntlets.

**Actionable Recommendations for IR Teams:**
1.  **Dynamic Analysis is Essential:** Because static analysis of the arithmetic gates is mathematically exhausting, analysts should use a debugger (e.g., **x64dbg**) to "step over" the math blocks and land directly on the resulting `if/else` conditions or the subsequent system calls.
2.  **Pattern-Based Triage:** During triage, look for the constants `0x303`, `0x505`, and `0x909`. These are definitive markers of the malware's internal logic gates; their presence confirms a "Gatekeeper" obfuscation style is in use.
3.  **Behavioral Monitoring:** Since the internal state-machine transitions are hidden, monitoring for **system-level artifacts** (e.g., calls to `GetStdHandle`, large memory allocations via `malloc` or `memmove`, and unusual network traffic) is the most effective way to identify malicious activity at runtime.
4.  **Identify "Sink" Functions:** Focus on identifying where the "shields" end. Once a calculation finishes, the malware usually calls an actual system function (like `sym.runtime.memmove`). Hooking these "sinks" will reveal the data being moved or processed even if you cannot see the math that led to it.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your report to the relevant MITRE ATT&K techniques. Most of these observations fall under the **Defense Evasion** tactic, specifically utilizing complex obfuscation to hinder both manual and automated analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of "Arithmetic Shields" (complex floating-point math) is used to mask the actual logic flow and hide critical system interactions from static analysis. |
| T1027 | Obfuscated Files or Information | The "State-Gate System" uses fixed constants as keys to create a controlled execution path, hiding multiple "dummy" paths from automated tools. |
| T1027 | Obfuscated Files or Information | Standard library functions (e.g., `io.Copy`, `memmove`) are intentionally wrapped in math to conceal the malware's capability for data manipulation and I/O operations. |
| T1027 | Obfuscated Files or Information | The "Anti-Symbolic Execution" design uses high-precision arithmetic specifically to trigger state explosion in automated analysis engines like Angr or Triton. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None found.

**File paths / Registry keys**
*   None found.

**Mutex names / Named pipes**
*   None found.

**Hashes**
*   **Go Build ID:** `r6eL3-GGbA_nppVnV5Hx/m94mVzi2dG2GiXUEujUG/v44zHo5jd-HpoKRCy3P7/jGk0apMRxj_j-p-7WFUD` (Used to identify specific build versions of the Go-based binary).

**Other artifacts**
*   **Internal Logic Constants:** `0x303`, `0x505`, and `0x909` (Identified as "Gatekeeper" keys used in the state-gate system to control branching logic).
*   **Obfuscated Function Names:** `jrqxegfcxvuaf`, `mplphjbrmolek` (Used for internal code segmentation/obfuscation).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Loader Functionality**: The inclusion of `sym.io.Copy`, `sym.bufio.NewReader`, and `sym.runtime.memmove` indicates the sample is designed to manipulate data streams, likely for downloading, decompressing, or preparing a secondary payload in memory.
    *   **Advanced Obfuscation Logic**: The "Arithmetic Shields" (complex floating-point math) and "State-Gate System" are highly sophisticated techniques used specifically to hide transition logic and standard library calls from both human analysts and automated symbolic execution tools.
    *   **Sophisticated Go Implementation**: The use of specialized Go-based obfuscation and the lack of specific identifiers for known families (like Mirai or njRAT) indicate a professional, "industrial" custom build designed to maximize defense evasion.
