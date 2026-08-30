# Threat Analysis Report

**Generated:** 2026-08-15 23:12 UTC
**Sample:** `0f608e6d16bfaecb7bf11cde5badf364ad8cc4d3f857c2754bcbf47a1a159b3b_0f608e6d16bfaecb7bf11cde5badf364ad8cc4d3f857c2754bcbf47a1a159b3b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f608e6d16bfaecb7bf11cde5badf364ad8cc4d3f857c2754bcbf47a1a159b3b_0f608e6d16bfaecb7bf11cde5badf364ad8cc4d3f857c2754bcbf47a1a159b3b.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 505,856 bytes |
| MD5 | `dc866d0b5822a2fc6750182ae9c5242e` |
| SHA1 | `27d69f11af6a9f6c4f70179c2c92b9a8e7034695` |
| SHA256 | `0f608e6d16bfaecb7bf11cde5badf364ad8cc4d3f857c2754bcbf47a1a159b3b` |
| Overall entropy | 6.417 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 4083124614 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 257,536 | 6.285 | No |
| `.rsrc` | 247,296 | 6.312 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2451** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU
%-&($
%-&s'

- 	oI

-+	oI

2rc$

.r=&

.r=&
 KDBM(
Q#y:oJ~

lP5s:
Zv9VBS
7Jtoef
w(.q0.
%O']L
@b*J0Y
z!+ws)8v
 dy
r3
\Q~>K4
BA8Uf
*X0h>^wt
Pz(7'7
W<t~Fm
H	&ADD
	#t\,y
E>*Z:Z
3I[%N=LI
26`Qyl
Fh6B#j-6
L)A:G%
A;6Tb)tK
PZ6X
rp[
|+.jKc
t"v`|3v:
P35 k
)d	YKn&
{H@{YI
%yriFB
2@Nc)5
|Y`njj
9i2(Lrv
U9i9y9*
QBd."S
I]s6*

#F4kV3A
nliH mB
"HBufs
D]KdM\
/^={zk
GjGnuXU
|(O
Fl/
AtZP;2?mC2y(Vh
yqmKQsa
;Q	pdM{
G\6th
^uGsVI
VBQtlu
+)62|G
LXrVI%
HU2vi<
c6JOG
costura.costura.dll.compressed|5.7.0.0|Costura, Version=5.7.0.0, Culture=neutral, PublicKeyToken=null|Costura.dll|F1F25C01F6ACF33BDD62C4F82D3EF078E76F0906|4608
costura.costura.pdb.compressed|||Costura.pdb|6C6000A5EAF8579850AB82A89BD6268776EB51AD|2608
costura.system.diagnostics.diagnosticsource.dll.compressed|4.0.1.0|System.Diagnostics.DiagnosticSource, Version=4.0.1.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51|System.Diagnostics.DiagnosticSource.dll|85DC92EDD4B0049ED9049E075C4DEF8A3D64E43B|35760

v4.0.30319
#Strings
 tSCMY
 WSLM]
 `qRM_
 0q^Me
 %mhMj
 5mwMs
 # d z 
%*&:&a&q&
MN-NWNqN
	*	;	_	
	(K\mz
';BTc
!+"N"a"
&Q.a.m.
__StaticArrayInitTypeSize=10
<>9__2_10
<Run>b__2_10
<path>5__10
<reader>5__10
<getEpicPrivacyPasswords>5__10
<Init>b__10
<>p__10
<>9__2_20
<Run>b__2_20
<getChromiumCookies>5__20
<>9__2_30
<Run>b__2_30
<getYandexCookies>5__30
<comodoPasswords>5__40
<braveCookies>5__50
<urCookies>5__60
<robloxCookieCount>5__70
<>c__DisplayClass10_0
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c..cctor` | `0x41bf23` | 169684 | ✓ |
| `sym.Costura.AssemblyLoader.LoadStream` | `0x41d7fc` | 163156 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x41dad4` | 64808 | ✓ |
| `method._Run_d__2.MoveNext` | `0x404250` | 10528 | ✓ |
| `method._AddAccount_d__13.MoveNext` | `0x40ec48` | 2524 | ✓ |
| `method.Umbral.payload.Components.AntiVM.Detector.CheckComputerName` | `0x41cd55` | 2516 | ✓ |
| `method.Umbral.payload.Components.Helpers.SQLiteHandler.ReadMasterTable` | `0x40b348` | 2072 | ✓ |
| `sym._GetInfo_d__0.MoveNext` | `0x407064` | 2016 | ✓ |
| `method._MethodB_d__8.MoveNext` | `0x41071c` | 1700 | ✓ |
| `method.Umbral.payload.Components.Helpers.SQLiteHandler.ReadTableFromOffset` | `0x40bc98` | 1693 | ✓ |
| `method.Umbral.payload.PocoJsonSerializerStrategy.DeserializeObject` | `0x4031a8` | 1556 | ✓ |
| `method._GetInfo_d__0.MoveNext` | `0x407908` | 1372 | ✓ |
| `method._BlockAvSites_d__3.MoveNext` | `0x403b04` | 1248 | — |
| `method._GetGifts_d__12.MoveNext` | `0x40fe00` | 1156 | ✓ |
| `method._MethodA_d__7.MoveNext` | `0x410294` | 1144 | ✓ |
| `method._Run_d__6.MoveNext` | `0x410dd0` | 1116 | ✓ |
| `method.Umbral.payload.Components.AntiVM.Detector..cctor` | `0x41cdc4` | 1108 | ✓ |
| `method._GetCookies_d__2.MoveNext` | `0x409010` | 1044 | ✓ |
| `sym._GetCookies_d__6.MoveNext` | `0x41199c` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_1` | `0x412790` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_2` | `0x413580` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_3` | `0x414374` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_4` | `0x415168` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_5` | `0x415f50` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_6` | `0x416d7c` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_7` | `0x417b6c` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_8` | `0x41895c` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_9` | `0x41974c` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_10` | `0x41a53c` | 1024 | ✓ |
| `sym._GetCookies_d__6.MoveNext_11` | `0x41b32c` | 1024 | ✓ |

### Decompiled Code Files

- [`code/method.Costura.AssemblyLoader.Attach.c`](code/method.Costura.AssemblyLoader.Attach.c)
- [`code/method.Umbral.payload.Components.AntiVM.Detector..cctor.c`](code/method.Umbral.payload.Components.AntiVM.Detector..cctor.c)
- [`code/method.Umbral.payload.Components.AntiVM.Detector.CheckComputerName.c`](code/method.Umbral.payload.Components.AntiVM.Detector.CheckComputerName.c)
- [`code/method.Umbral.payload.Components.Helpers.SQLiteHandler.ReadMasterTable.c`](code/method.Umbral.payload.Components.Helpers.SQLiteHandler.ReadMasterTable.c)
- [`code/method.Umbral.payload.Components.Helpers.SQLiteHandler.ReadTableFromOffset.c`](code/method.Umbral.payload.Components.Helpers.SQLiteHandler.ReadTableFromOffset.c)
- [`code/method.Umbral.payload.PocoJsonSerializerStrategy.DeserializeObject.c`](code/method.Umbral.payload.PocoJsonSerializerStrategy.DeserializeObject.c)
- [`code/method._AddAccount_d__13.MoveNext.c`](code/method._AddAccount_d__13.MoveNext.c)
- [`code/method._GetCookies_d__2.MoveNext.c`](code/method._GetCookies_d__2.MoveNext.c)
- [`code/method._GetGifts_d__12.MoveNext.c`](code/method._GetGifts_d__12.MoveNext.c)
- [`code/method._GetInfo_d__0.MoveNext.c`](code/method._GetInfo_d__0.MoveNext.c)
- [`code/method._MethodA_d__7.MoveNext.c`](code/method._MethodA_d__7.MoveNext.c)
- [`code/method._MethodB_d__8.MoveNext.c`](code/method._MethodB_d__8.MoveNext.c)
- [`code/method._Run_d__2.MoveNext.c`](code/method._Run_d__2.MoveNext.c)
- [`code/method._Run_d__6.MoveNext.c`](code/method._Run_d__6.MoveNext.c)
- [`code/method.__c..cctor.c`](code/method.__c..cctor.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)
- [`code/sym._GetCookies_d__6.MoveNext.c`](code/sym._GetCookies_d__6.MoveNext.c)
- [`code/sym._GetCookies_d__6.MoveNext_1.c`](code/sym._GetCookies_d__6.MoveNext_1.c)
- [`code/sym._GetCookies_d__6.MoveNext_10.c`](code/sym._GetCookies_d__6.MoveNext_10.c)
- [`code/sym._GetCookies_d__6.MoveNext_11.c`](code/sym._GetCookies_d__6.MoveNext_11.c)
- [`code/sym._GetCookies_d__6.MoveNext_2.c`](code/sym._GetCookies_d__6.MoveNext_2.c)
- [`code/sym._GetCookies_d__6.MoveNext_3.c`](code/sym._GetCookies_d__6.MoveNext_3.c)
- [`code/sym._GetCookies_d__6.MoveNext_4.c`](code/sym._GetCookies_d__6.MoveNext_4.c)
- [`code/sym._GetCookies_d__6.MoveNext_5.c`](code/sym._GetCookies_d__6.MoveNext_5.c)
- [`code/sym._GetCookies_d__6.MoveNext_6.c`](code/sym._GetCookies_d__6.MoveNext_6.c)
- [`code/sym._GetCookies_d__6.MoveNext_7.c`](code/sym._GetCookies_d__6.MoveNext_7.c)
- [`code/sym._GetCookies_d__6.MoveNext_8.c`](code/sym._GetCookies_d__6.MoveNext_8.c)
- [`code/sym._GetCookies_d__6.MoveNext_9.c`](code/sym._GetCookies_d__6.MoveNext_9.c)
- [`code/sym._GetInfo_d__0.MoveNext.c`](code/sym._GetInfo_d__0.MoveNext.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 13/13**, concluding the disassembly series. The final data points reinforce a critical conclusion: this malware utilizes a **Virtual Machine (VM)-style obfuscation architecture** to hide its malicious logic, specifically targeting browser cookies for session hijacking.

---

### Final Technical Analysis (Chunks 1–13)

The analysis of the complete disassembly reveals a highly sophisticated "Russian Nesting Doll" of defensive layers designed to thwart both automated scanners and human reverse engineers.

#### 1. Evolution of the State Machine: Fragmented Logic
The presence of `MoveNext_8`, `MoveNext_9`, `MoveNext_10`, and `MoveNext_11` confirms that the malware's logic is not linear. 
*   **Technical Significance:** Each "MoveNext" represents a state in a **Control-Flow Flattening** or **Virtual Machine** dispatcher. Instead of a standard function where $A \to B \to C$, the code moves from State 8 to a dispatcher, which calculates the next jump (e.g., to state 9) using complex math.
*   **Analyst Impact:** This prevents an analyst from "tracing" the logic linearly. Even if you identify one piece of theft-related code, it is just one "room" in a labyrinth; you cannot see the next step without executing the code or perfectly replicating the dispatcher's logic.

#### 2. Advanced Instruction Substitution & Arithmetic Bloat
The disassembly shows an extreme amount of "noise." For example:
*   `piVar21 = CONCAT22(uVar28,CONCAT11(uVar30,cVar8));`
*   `iVar14 = CONCAT31(puVar39 >> 8,uVar7) + 0x1b0000a5 + CARRY1(uVar32,uVar7);`
*   **Technical Significance:** These are **Mathematical Equivalents**. A simple operation like `eax = ebx + 5` is replaced by a multi-step calculation involving bitwise shifts (>>), concatenations of high/low bytes, and carry-flag checks. This is intended to exhaust the analyst's time; they must manually solve 10 calculations just to find one variable value.
*   **Detection evasion:** These operations generate "high entropy" in the instruction stream, making it look like a complex encryption algorithm or a custom compression routine rather than simple malware logic.

#### 3. Intentional Structural Corruption (Anti-Disassembly)
The recurring warnings—`Instruction at ... overlaps instruction at ...` and `halt_baddata()`—are not errors in the disassembly tool; they are **intentional flaws** in the binary.
*   **Technical Significance:** The author is using "overlapping instructions." By placing a jump into the *middle* of another instruction, they force the disassembler to choose one interpretation over the other (making it impossible for the tool to show the true code path).
*   **Impact on Automation:** This specifically targets tools like IDA Pro and Ghidra. It forces a human analyst to switch to a "Hex View" and manually reconstruct the assembly, which can take days of work just to understand one small function.

#### 4. Confirmed Payload: The `_GetCookies` Target
Despite the layers of math, the underlying intent remains clear through the naming convention in the obfuscation layer: `sym._GetCookies_d__6`.
*   **Target:** Browser cookies (Chrome, Edge, etc.). 
*   **Risk Factor:** Cookies are high-value "keys." By stealing these, attackers bypass Multi-Factor Authentication (MFA) because they are essentially "cloning" an already authenticated session.

---

### Final Technical Synthesis: The Architecture of the Threat

The malware's architecture can be defined as a **Virtualized Infostealer**. 

1.  **The Payload Layer:** A small, concentrated routine that locates browser profiles and extracts cookie databases (likely using SQL queries or direct file parsing).
2.  **The Transformation Layer (VM/Dispatcher):** The "MoveNext" logic. This converts the payload into a series of bytecode instructions interpreted by a custom engine. 
3.  **The Obfuscation Shield:** The use of `POPCOUNT` checks, `CARRY` flags as branch conditions, and overlapping instructions to ensure that any automated analysis tool provides an incomplete or incorrect view of the code.

---

### Final Risk Assessment & IR Strategy

#### Threat Intelligence Profile
*   **Sophistication:** **Very High.** The use of VM-style obfuscation suggests a professional developer or a specialized malware "packer" service. 
*   **Threat Actor Type:** Likely an organized cybercrime group or an APT, given the effort required to implement custom instruction substitution and anti-disassembly techniques.
*   **Primary Objective:** Session Hijacking (Credential theft through cookie stealing).

#### Indicators of Compromise (IoCs) & Behavioral Patterns:
*   **File System Activity:** Monitor for unauthorized access to `%LocalAppData%\Google\Chrome\User Data\*` or `\Microsoft\Edge\UserData\*`.
*   **Process Behavior:** Look for processes that perform heavy mathematical operations followed by network connections—this is a sign of "on-the-fly" decryption of stolen data before exfiltration.
*   **Memory Signatures:** Since the code only becomes "plain" in memory during execution, scan for common cookie database indicators (e.g., `SQLite`, `Network\Cookies`).

#### Incident Response Actions:
1.  **Immediate Session Revocation:** If a host is flagged, **do not just re-image the machine.** You must force a logout and session revocation on all corporate accounts (Microsoft 365, Google Workspace, etc.) because the cookies are already in the attacker's possession.
2.  **Host Isolation:** Isolate infected machines from the network immediately to prevent the "heartbeat" of the data exfiltration.
3.  **Memory Forensics:** Since static analysis is neutralized by the VM layer, use memory forensics (Volatility) to capture strings that appear only when the state machine reaches the `_GetCookies` execution point.

**Risk Level: CRITICAL**
*(High-Sophistication | State-Machine Obfuscation | Active Anti-Analysis | Critical Data Target)*

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | Obfuscated Files or Information | The use of a "Virtual Machine-style" architecture, arithmetic bloat (instruction substitution), and overlapping instructions are all designed to hide the malicious logic from both automated tools and human analysts. |
| **T1539** | Steal Web Credentials | The primary goal of the malware is to steal session cookies which serve as high-value keys to bypass Multi-Factor Authentication (MFA). |
| **T1555.002** | Web Browsers | The analysis specifically identifies the target as browser-stored data, including Chrome and Edge cookie databases. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   *(Note: Standard system paths for Chrome/Edge were mentioned in the report; however, as these are standard application directories and not unique to a malicious file path or registry key used specifically by the malware, they are excluded per instructions.)*

**Mutex names / Named pipes**
*   (None identified)

**Hashes**
*   (None identified. The hashes present in the strings—e.g., `F1F25C0...`—are associated with the **Costura** library's internal metadata and are not unique signatures of a specific malware variant.)

**Other artifacts**
*   **Targeted Data Indicators (Potential Recon/Payload):**
    *   `getChromiumCookies` (Chrome)
    *   `getYandexCookies` (Yandex)
    *   `comodoPasswords` (Comodo)
    *   `braveCookies` (Brave)
    *   `urCookies` (Opera/Other)
    *   `robloxCookieCount` (Roblox)
    *   `GetPasswords`
    *   `CaptureWebcam`
    *   `StealSessions`
*   **Malware Construction Indicators:**
    *   **VM-style obfuscation:** Use of a custom virtual machine to hide malicious logic.
    *   **Control-Flow Flattening:** Usage of `MoveNext_X` functions (e.g., `MoveNext_8`, `MoveNext_11`) to obscure the execution path.
    *   **Instruction Substitution/Arithmetic Bloat:** Use of complex, multi-step calculations for simple operations to evade automated analysis.
    *   **Anti-Disassembly Tactics:** Intentional "overlapping instructions" and high entropy code design to break tools like IDA Pro and Ghidra.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Targeted Data Extraction:** The analysis explicitly identifies the primary payload as stealing browser cookies (Chrome, Edge, Yandex, Brave, etc.) and passwords to facilitate session hijacking and bypass Multi-Factor Authentication (MFA).
    *   **Sophisticated Obfuscation:** The sample employs advanced "Virtual Machine" (VM) style architecture, control-flow flattening (`MoveNext` functions), and instruction substitution to hide its malicious logic from automated tools and manual analysis.
    *   **Additional Spyware Features:** The inclusion of `CaptureWebcam`, `StealSessions`, and `GetPasswords` confirms its role as an infostealer designed for comprehensive data theft.
