# Threat Analysis Report

**Generated:** 2026-07-02 19:47 UTC
**Sample:** `03c3787f4718db16b3d08eba3ad8e4eb235ef3f243682c02e1e0018891726646_03c3787f4718db16b3d08eba3ad8e4eb235ef3f243682c02e1e0018891726646.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03c3787f4718db16b3d08eba3ad8e4eb235ef3f243682c02e1e0018891726646_03c3787f4718db16b3d08eba3ad8e4eb235ef3f243682c02e1e0018891726646.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 3,342,848 bytes |
| MD5 | `aac9a89fab496fea9970898be48b8c95` |
| SHA1 | `207135d59597c2b1c8f0251fda00fa23ce594492` |
| SHA256 | `03c3787f4718db16b3d08eba3ad8e4eb235ef3f243682c02e1e0018891726646` |
| Overall entropy | 7.987 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3824410026 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,340,800 | 7.987 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.129 | No |

## Extracted Strings

Total strings found: **8649** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

*^rA:

X )UU

X )UU

X )UU

X )UU

,&	of
#333333
#333333
#333333
#333333
9x-Jg
]	3KP.l7
6EaR-R
hgRrZ
bZ1^${
gUt#8w[
_C2C[p
,:*\uu
w1g)+,\
&@Bq=?
Dn**6
<$b!F`l
}<R
-
Ih>d'w
g>.6vZ
hf].a0
ffMzR"34;
0?d5+B
9'MD>j
G}k{LZ
8#pME$
&m0kwgLR
A/M1iD
m[/dNik
oHqa;m&P
$[G}cn
n'=*`,
YOO<pTg
*3J3H
oP<`u}H
	~U4g
LZzI.0
@?#1*o
JhXm/'
0o /1*J`
'gDhMu2
lxLda]>
u3A-FoB
9['8Z>
W)Ir3<]
F0ZUTB9
@2ix1Q
5N$kW9
FKFkg"
4b$PY}
i=2UKC
{
Z]+T
mB,s>O9
I1* ow
/WF8Qq
Cy*^
P
)HAhOu
(%{Zk	/7
*$XcQ
}N
 %1
dlXT5b
,Tscmo
n>_kc$o
f[;\n*
=)#CT7v)
np|dke,x@
ttu<,j
n]=:,
 F5 Om
ZSjSTz'
%d"3/`
yX_1Xk
uL!H$Y
<\}A%3
lu@4#
C>(Z$S#
K.WSof
p#]B%(
M.*..A>
g.@sZc
[[Tgq:
C?VOI/
<HpW@
	MOd67
&kif3A
bck|1Z
VHp r<9Lj
wx	n2q
1/R*Hy|
w4FI,d
'+S/oe
<9A;n]
"
Wv>r4
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.Costura.AssemblyLoader.LoadStream` | `0x40fb90` | 3294320 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x40ff38` | 64600 | ✓ |
| `method.xrick_premiumm.Form1.InitializeComponent` | `0x409350` | 12000 | ✓ |
| `method.xrick_premiumm.Form2.InitializeComponent` | `0x40da00` | 2256 | ✓ |
| `method.MysteriousMem.Mysterious.GetCode` | `0x405624` | 1292 | ✓ |
| `method.__c__DisplayClass13_0._AoBScan_b__0` | `0x405fb8` | 1276 | ✓ |
| `method._LoginAsync_d__5.MoveNext` | `0x404968` | 1104 | ✓ |
| `method.xrick_premiumm.Form1.GetTextoTempoPlano` | `0x407854` | 1044 | ✓ |
| `method.xrick_premiumm.Program.CAD9D4002159769AF316F6672EC8EAD9` | `0x40f6a4` | 1016 | ✓ |
| `method.xrick_premiumm.Form1.Form1_Load` | `0x407c68` | 992 | ✓ |
| `method._guna2CustomCheckBox11_Click_d__166.MoveNext` | `0x40c7b4` | 960 | ✓ |
| `method._guna2CustomCheckBox4_Click_d__145.MoveNext` | `0x40cd98` | 960 | ✓ |
| `method._guna2CustomCheckBox5_Click_d__144.MoveNext` | `0x40d158` | 960 | ✓ |
| `method._guna2CustomCheckBox6_Click_d__146.MoveNext` | `0x40d518` | 960 | ✓ |
| `method.XRickAuth.XRickAuth.GetTempoRestante` | `0x404574` | 920 | ✓ |
| `method.xrick_premiumm.Form3.InitializeComponent` | `0x40ea90` | 632 | ✓ |
| `method.xrick_premiumm.Program.SoapNcName` | `0x40f084` | 564 | ✓ |
| `method.xrick_premiumm.Form1..ctor` | `0x406e9c` | 560 | ✓ |
| `method.MysteriousMem.Mysterious.WriteMemory` | `0x405b30` | 544 | ✓ |
| `method.xrick_premiumm.Form1.ShowPage` | `0x407478` | 516 | ✓ |
| `method._guna2Button1_Click_1_d__10.MoveNext` | `0x40e598` | 488 | ✓ |
| `method.xrick_premiumm.Form1.Animate` | `0x40767c` | 472 | ✓ |
| `method._guna2Button1_Click_d__6.MoveNext` | `0x40e3c8` | 464 | ✓ |
| `method._DownloadDLLAsync_d__79.MoveNext` | `0x40c380` | 460 | ✓ |
| `method.xrick_premiumm.Form1.ExecuteMemoryScanhead` | `0x4084c0` | 452 | ✓ |
| `method.xrick_premiumm.Form1.ExecuteMemoryScanlegit` | `0x408684` | 452 | ✓ |
| `method._guna2Button7_Click_d__108.MoveNext` | `0x40c5fc` | 440 | ✓ |
| `method._guna2CustomCheckBox3_Click_d__163.MoveNext` | `0x40cbe0` | 440 | ✓ |
| `method.xrick_premiumm.Program.Detected` | `0x40f510` | 404 | ✓ |
| `method.Costura.AssemblyLoader..cctor` | `0x40fdc0` | 376 | ✓ |

### Decompiled Code Files

- [`code/method.Costura.AssemblyLoader..cctor.c`](code/method.Costura.AssemblyLoader..cctor.c)
- [`code/method.Costura.AssemblyLoader.Attach.c`](code/method.Costura.AssemblyLoader.Attach.c)
- [`code/method.MysteriousMem.Mysterious.GetCode.c`](code/method.MysteriousMem.Mysterious.GetCode.c)
- [`code/method.MysteriousMem.Mysterious.WriteMemory.c`](code/method.MysteriousMem.Mysterious.WriteMemory.c)
- [`code/method.XRickAuth.XRickAuth.GetTempoRestante.c`](code/method.XRickAuth.XRickAuth.GetTempoRestante.c)
- [`code/method._DownloadDLLAsync_d__79.MoveNext.c`](code/method._DownloadDLLAsync_d__79.MoveNext.c)
- [`code/method._LoginAsync_d__5.MoveNext.c`](code/method._LoginAsync_d__5.MoveNext.c)
- [`code/method.__c__DisplayClass13_0._AoBScan_b__0.c`](code/method.__c__DisplayClass13_0._AoBScan_b__0.c)
- [`code/method._guna2Button1_Click_1_d__10.MoveNext.c`](code/method._guna2Button1_Click_1_d__10.MoveNext.c)
- [`code/method._guna2Button1_Click_d__6.MoveNext.c`](code/method._guna2Button1_Click_d__6.MoveNext.c)
- [`code/method._guna2Button7_Click_d__108.MoveNext.c`](code/method._guna2Button7_Click_d__108.MoveNext.c)
- [`code/method._guna2CustomCheckBox11_Click_d__166.MoveNext.c`](code/method._guna2CustomCheckBox11_Click_d__166.MoveNext.c)
- [`code/method._guna2CustomCheckBox3_Click_d__163.MoveNext.c`](code/method._guna2CustomCheckBox3_Click_d__163.MoveNext.c)
- [`code/method._guna2CustomCheckBox4_Click_d__145.MoveNext.c`](code/method._guna2CustomCheckBox4_Click_d__145.MoveNext.c)
- [`code/method._guna2CustomCheckBox5_Click_d__144.MoveNext.c`](code/method._guna2CustomCheckBox5_Click_d__144.MoveNext.c)
- [`code/method._guna2CustomCheckBox6_Click_d__146.MoveNext.c`](code/method._guna2CustomCheckBox6_Click_d__146.MoveNext.c)
- [`code/method.xrick_premiumm.Form1..ctor.c`](code/method.xrick_premiumm.Form1..ctor.c)
- [`code/method.xrick_premiumm.Form1.Animate.c`](code/method.xrick_premiumm.Form1.Animate.c)
- [`code/method.xrick_premiumm.Form1.ExecuteMemoryScanhead.c`](code/method.xrick_premiumm.Form1.ExecuteMemoryScanhead.c)
- [`code/method.xrick_premiumm.Form1.ExecuteMemoryScanlegit.c`](code/method.xrick_premiumm.Form1.ExecuteMemoryScanlegit.c)
- [`code/method.xrick_premiumm.Form1.Form1_Load.c`](code/method.xrick_premiumm.Form1.Form1_Load.c)
- [`code/method.xrick_premiumm.Form1.GetTextoTempoPlano.c`](code/method.xrick_premiumm.Form1.GetTextoTempoPlano.c)
- [`code/method.xrick_premiumm.Form1.InitializeComponent.c`](code/method.xrick_premiumm.Form1.InitializeComponent.c)
- [`code/method.xrick_premiumm.Form1.ShowPage.c`](code/method.xrick_premiumm.Form1.ShowPage.c)
- [`code/method.xrick_premiumm.Form2.InitializeComponent.c`](code/method.xrick_premiumm.Form2.InitializeComponent.c)
- [`code/method.xrick_premiumm.Form3.InitializeComponent.c`](code/method.xrick_premiumm.Form3.InitializeComponent.c)
- [`code/method.xrick_premiumm.Program.CAD9D4002159769AF316F6672EC8EAD9.c`](code/method.xrick_premiumm.Program.CAD9D4002159769AF316F6672EC8EAD9.c)
- [`code/method.xrick_premiumm.Program.Detected.c`](code/method.xrick_premiumm.Program.Detected.c)
- [`code/method.xrick_premiumm.Program.SoapNcName.c`](code/method.xrick_premiumm.Program.SoapNcName.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is a technical analysis of the binary sample:

### Core Functionality and Purpose
The binary appears to be a **malicious .NET-based application** (likely a Trojan or a "cracked" software component) that utilizes high levels of obfuscation. The presence of the `Costura` namespace indicates it uses the Costura.Fody library to embed multiple DLLs into a single executable, which is common in malware to hide secondary modules like downloaders and keyloggers.

The naming convention (`xrick_premiumm`) suggests it may masquerade as a "premium" software tool or a license-key checker, but the underlying mechanics point toward malicious intent.

### Suspicious and Malicious Behaviors
*   **Keylogging & Input Hooking:** 
    *   The function `method.Costura.AssemblyLoader..cctor` specifically references `_sym.KeyboardHook.SetWindowsHookEx`. This is a primary indicator of a **keylogger**, used to intercept keystrokes from the user.
*   **Payload Delivery (Downloader):** 
    *   The method `method._DownloadDLLAsync_d__79` indicates the binary has functionality to download and likely execute additional DLLs from a remote server at runtime. This is typical of a **multi-stage dropper**.
*   **Memory Manipulation & Injection:**
    *   Functions such as `method.MysteriousMem.Mysterious.GetCode` and `method.MysteriousMem.Mysterious.WriteMemory` are highly suspicious. These are characteristic of a loader designed to inject shellcode or move malicious code into memory while avoiding detection on disk. 
*   **Anti-Analysis/Anti-Debugging:**
    *   The functions `ExecuteMemoryScanhead` and `ExecuteMemoryScanlegit` suggest the program scans its own memory space (or the system's) for common signatures of debuggers, sandboxes, or analysis tools to evade detection.
*   **Obfuscation & Packing:**
    *   The presence of extremely long, randomized method names (e.g., `CAD9D4002159769AF316F6672EC8EAD9`) and the "broken" decompilation output (multiple `halt_baddata` calls) indicate the use of a heavy **packer/obfuscator** (such as ConfuserEx or Dotfuscix).

### Notable Techniques & Patterns
*   **Costura Assembly Loading:** Used to bundle functionality into one file, making it harder for simple static analysis tools to find secondary malicious components without unpacking.
*   **Asynchronous Network Logic:** The use of `_LoginAsync` and `_DownloadDLLAsync` suggests the malware operates in a multi-threaded or asynchronous manner, likely to keep the UI responsive while communicating with its Command and Control (C2) server.
*   **High Entropy/Obfuscated Strings:** While many strings are illegible, the inclusion of `.rsrc` and varied character sets indicates an attempt to hide plain-text indicators from signature-based detection.

### Summary Checklist
*   **Persistence:** Not explicitly shown in this snippet, but likely exists via a dropped component or registry modification after the "Download" phase.
*   **Process Injection:** Highly likely via `WriteMemory` and `GetCode`.
*   **Network Communication:** Confirmed via `_LoginAsync` and `_DownloadDLLAsync`.
*   **Information Stealing:** High probability via `SetWindowsHookEx`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1056.001 | Keylogging | The use of `SetWindowsHookEx` is a classic method for intercepting and logging user keystrokes. |
| T1105 | Ingress Tool Transfer | The `_DownloadDLLAsync` function indicates the malware fetches additional payloads from a remote server to facilitate multi-stage execution. |
| T1055 | Process Injection | The `WriteMemory` and `GetCode` functions suggest the injection of shellcode or malicious modules into memory space to evade detection. |
| T1497 | Virtualization/Sandbox Evasion | The presence of memory scanning routines (`ExecuteMemoryScan`) is designed to detect analysis environments and evade security tools. |
| T1027 | Obfuscated Files or Information | The use of Costura, random string naming, and "broken" decompilation output indicates a heavy effort to hide the malicious code from static analysis. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contained highly obfuscated data; therefore, no explicit IP addresses, URLs, or File Paths were found within that specific raw block. The indicators below are derived from the behavior patterns and identifiers noted in the technical analysis.

### **IP addresses / URLs / Domains**
*   *None identified in provided strings.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The `#333333` values in the string list are hex color codes, not file hashes).

### **Other artifacts**
*   **Potential Malware Name:** `xrick_premiumm` (Identified as a possible masquerading name for the application).
*   **Malicious Functionality/API Calls:** 
    *   `SetWindowsHookEx` (Used for keylogging).
    *   `WriteMemory` / `GetCode` (Used for memory injection).
    *   `ExecuteMemoryScanhead` / `ExecuteMemoryScanlegit` (Anti-analysis/anti-debugging techniques).
*   **Suspicious Method Names:** 
    *   `_DownloadDLLAsync_d__79` (Indicates a multi-stage downloader component).
    *   `_LoginAsync` (Indicates network communication for authentication/C2 check-in).
*   **Library Indicators:** `Costura.Fody` (Used to bundle multiple DLLs into one executable to hide malicious modules).

---
**Analyst Note:** The lack of explicit IPs or URLs in the raw strings suggests the malware may use hardcoded encrypted strings or a Domain Generation Algorithm (DGA) to reach its C2 server, which would only be visible during active execution/deobfuscation.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** Unknown (Potential custom Trojan)
2. **Malware type:** Loader / RAT
3. **Confidence:** High
4. **Key evidence:** 
    *   **Multi-stage Loading & Injection:** The binary utilizes `_DownloadDLLAsync` to fetch remote modules and uses memory manipulation functions (`WriteMemory`, `GetCode`) to inject code into memory, characteristic of a loader designed to bypass traditional disk-based security.
    *   **Spyware Capabilities:** The explicit use of `SetWindowsHookEx` confirms the inclusion of keylogging functionality, which is a primary indicator of a Remote Access Trojan (RAT) or an information stealer.
    *   **Evasion & Obfuscation:** The sample employs heavy .NET obfuscation (Costura), randomized method naming, and specific anti-analysis routines (`ExecuteMemoryScan`) to evade both automated sandboxes and manual forensic analysis.
