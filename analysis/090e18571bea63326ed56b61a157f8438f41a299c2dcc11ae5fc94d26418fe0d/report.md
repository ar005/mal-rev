# Threat Analysis Report

**Generated:** 2026-07-19 11:45 UTC
**Sample:** `090e18571bea63326ed56b61a157f8438f41a299c2dcc11ae5fc94d26418fe0d_090e18571bea63326ed56b61a157f8438f41a299c2dcc11ae5fc94d26418fe0d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `090e18571bea63326ed56b61a157f8438f41a299c2dcc11ae5fc94d26418fe0d_090e18571bea63326ed56b61a157f8438f41a299c2dcc11ae5fc94d26418fe0d.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 3,963,904 bytes |
| MD5 | `86d34cbba0f6ade83817f2ddc7599d0b` |
| SHA1 | `b7a7fb2d48371d30503eaf35f0c72bc2b8689dde` |
| SHA256 | `090e18571bea63326ed56b61a157f8438f41a299c2dcc11ae5fc94d26418fe0d` |
| Overall entropy | 7.961 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765019016 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `        ` | 54,784 | 7.961 | ⚠️ Yes |
| `        ` | 512 | 0.183 | No |
| `        ` | 6,144 | 7.906 | ⚠️ Yes |
| `.bss` | 0 | 0.0 | No |
| `        ` | 512 | 4.208 | No |
| `        ` | 512 | 1.705 | No |
| `.rsrc` | 1,640,960 | 7.979 | ⚠️ Yes |
| `.idata` | 512 | 1.776 | No |
| `.themida` | 0 | 0.0 | No |
| `.boot` | 2,258,944 | 7.931 | ⚠️ Yes |

### Imports

**kernel32.dll**: `GetModuleHandleA`
**ADVAPI32.dll**: `CloseServiceHandle`
**USER32.dll**: `GetSystemMetrics`

## Extracted Strings

Total strings found: **8433** (showing first 100)

```
!This program cannot be run in DOS mode.
$
        H
`        
        0-
        
        `
@.rsrc
@.idata
.themida
\	8zNw
~?$AoG
]qd;Hr
|#lDfShEP,2
"k[c&:
	|x}E9
%tSc7H>
Kt`!M)
$A>#D
!&q)*/
'}lH6
mIe6,&
#*{{e'
7)eO`a
:3E{Jy
(\Xh{L
/Z;k~
S.=4sY
z
q3Wz0_,
j{FU!k
bVg9c$St
{#x@"9C
<FDU(1
Ik)r^#r
z|_h]J[
.C[mNk
tuWJH`=
l7-eXE
}/{ZPj~n4\
qgUp-]
VQ
PC
`!S4DR
+{!^Ge
#L
Z[7
QHVF$
MWBN)
xZ5!a[l
Lk?6 G
jrkC||}[
7-e^{3
-3Ah@/g
4&45H9a
!GaeG
kG(N/zZ
(O.}X:
8L8w"]
@H^x!K
j#*&Ib
H<nK0>
\8.>rE5y+
u[l[/#
~VZFHi;
~\La~K
q7hUy
V}xxg,
x?;~y
4J[q]JAsP
ps=@wG
FFY;E~
qV^]sS
oLDV+E
2ZC$>_
#v|{{U
1)KGJ(3
>`@^,
&
q 37X"Gi
H{L@7M
&{I#`
|xDCf!u
\5@'_H
/[/ U
QK>`3WhB
rdn/D""
U"_]y#
3?{ShM
J.l?	3
%A:{Ap;
	+9Z# 
im:d.v
$B3
3W2>
(=E84}?
%IDATx
4iVZi
s8+(|'
:IDATx
,$}FkZk
uIDATx
Y=D=#|
%9}Xi#
x3CU)B
gh]QSn
```

## Disassembly Overview

Functions analyzed: **15** | Decompiled to C: **15**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x910058` | 391 | ✓ |
| `fcn.009d82ae` | `0x9d82ae` | 132 | ✓ |
| `fcn.00b17040` | `0xb17040` | 117 | ✓ |
| `fcn.009101df` | `0x9101df` | 105 | ✓ |
| `fcn.00aa3ce4` | `0xaa3ce4` | 45 | ✓ |
| `fcn.00a7c493` | `0xa7c493` | 29 | ✓ |
| `fcn.00b02316` | `0xb02316` | 28 | ✓ |
| `fcn.00a919d6` | `0xa919d6` | 11 | ✓ |
| `fcn.00b357aa` | `0xb357aa` | 9 | ✓ |
| `fcn.00b0593e` | `0xb0593e` | 5 | ✓ |
| `fcn.00adca28` | `0xadca28` | 4 | ✓ |
| `fcn.0099df4c` | `0x99df4c` | 4 | ✓ |
| `fcn.00aa8f34` | `0xaa8f34` | 3 | ✓ |
| `fcn.00a23e47` | `0xa23e47` | 2 | ✓ |
| `fcn.00b1a0f9` | `0xb1a0f9` | 2 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.009101df.c`](code/fcn.009101df.c)
- [`code/fcn.0099df4c.c`](code/fcn.0099df4c.c)
- [`code/fcn.009d82ae.c`](code/fcn.009d82ae.c)
- [`code/fcn.00a23e47.c`](code/fcn.00a23e47.c)
- [`code/fcn.00a7c493.c`](code/fcn.00a7c493.c)
- [`code/fcn.00a919d6.c`](code/fcn.00a919d6.c)
- [`code/fcn.00aa3ce4.c`](code/fcn.00aa3ce4.c)
- [`code/fcn.00aa8f34.c`](code/fcn.00aa8f34.c)
- [`code/fcn.00adca28.c`](code/fcn.00adca28.c)
- [`code/fcn.00b02316.c`](code/fcn.00b02316.c)
- [`code/fcn.00b0593e.c`](code/fcn.00b0593e.c)
- [`code/fcn.00b17040.c`](code/fcn.00b17040.c)
- [`code/fcn.00b1a0f9.c`](code/fcn.00b1a0f9.c)
- [`code/fcn.00b357aa.c`](code/fcn.00b357aa.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary sample:

### Core Functionality and Purpose
The binary functions as a **packer or loader stub**. The code shown does not contain high-level logic (like file manipulation or network protocols) but instead consists of heavily obfuscated routines designed to decrypt and unpack a secondary payload. The primary purpose is to "wrap" the actual malicious functionality, making it difficult for static analysis tools to identify the malware's true capabilities until it is executed in memory.

### Suspicious and Malicious Behaviors
*   **Known Packer Usage:** The presence of `@.themida` in the strings confirms the use of **Themida**, a well-known commercial protector/packer. Themida is frequently used by malware authors to hide code from antivirus scanners and hinder manual analysis.
*   **De-obfuscation Loops:** The `entry0` function contains complex, repetitive arithmetic involving bitwise shifts (`* 0x02`), carry flags (`CARRY1`), and nested conditional logic. This is a classic signature of an **unpacking stub**, where the code "calculates" the next set of instructions to execute by decoding them on-the-fly.
*   **Anti-Analysis & Junk Code:** Several functions (e.g., `fcn.009d82ae`, `fcn.00b17040`) are flagged as "bad instruction data" or "truncated." This is a common technique where the author inserts non-functional code or invalid instructions to break disassembly tools (like IDA Pro) and confuse analysts.
*   **Indirect Branching:** The function `fcn.009101df` shows signs of an obfuscated jump table and indirect calls (`*(pcVar3 + 0x61bba)`). By using calculated addresses rather than direct jumps, the malware hides its execution flow from static analysis tools.

### Notable Techniques & Patterns
*   **Code Obfuscation:** The heavy use of "junk" variables (like `uVar7`, `bVar11`) and complex arithmetic to perform simple operations is intended to increase the complexity of manual reverse engineering.
*   **Stack Manipulation:** The code references multiple stack offsets (`puStackX_8`, `puStackX_18`), which suggests the use of a custom "virtual machine" or a sophisticated state machine common in advanced packers to manage the execution flow of the unpacked payload.
*   **High-Entropy Data:** While the strings provided are largely non-human-readable/garbage, this is typical for packed binaries where the actual malicious code is stored as encrypted data blobs within the `.rsrc` or other sections.

### Summary Conclusion
This is a **highly obfuscated loader**. It does not perform its primary "malicious" task (e.g., stealing data) in this specific layer; instead, it serves to protect the core malware from detection. The use of **Themida** and complex **decryption loops** indicates a sophisticated threat actor or a high-quality "packer as a service" used by cybercriminals.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Programs | The use of the Themida packer, junk code to break disassemblers, and indirect branching are all employed to hide functionality and evade static analysis. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the list of extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   No standard MD5, SHA1, or SHA256 hashes were present in the provided string dump.

**Other artifacts**
*   **Protector/Packer:** `Themida` (Identified via the `@.themida` string). The use of this specific commercial packer is a significant behavioral indicator used to obfuscate malicious payloads and evade signature-based detection.
*   **Code Obfuscation Patterns:** The presence of "junk" instructions, indirect branching (`*(pcVar3 + 0x61bba)`), and complex decryption loops (e.g., `fcn.009d82ae`, `fcn.00b17040`) indicates a sophisticated loader stub designed to hinder static analysis.

---
**Analyst Note:** The lack of network-based IOCs (IPs/Domains) is expected at this stage of the investigation, as the behavioral analysis confirms this specific sample is a **packer/loader**. Its primary function is to decrypt and inject a secondary payload into memory; therefore, its "malicious" indicators are typically revealed only after it has been executed in a controlled environment.

---

## Malware Family Classification

1. **Malware family**: Unknown (Loader stub)
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Known Packer Usage:** The identification of the `@.themida` string confirms the use of the Themida protector, a known commercial tool used to wrap and hide malicious payloads from static analysis.
*   **Evasive Techniques:** The presence of decryption loops, "junk" code (intended to break disassemblers like IDA Pro), and indirect branching indicates a sophisticated design focused on concealing execution flow.
*   **Lack of Functional Logic:** The absence of network artifacts (IPs/Domains) or direct malicious actions (file encryption, data theft) confirms that this specific layer is a wrapper designed only to decrypt and execute a secondary, yet-to-be-revealed payload.
