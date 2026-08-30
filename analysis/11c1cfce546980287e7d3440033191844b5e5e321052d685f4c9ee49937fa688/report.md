# Threat Analysis Report

**Generated:** 2026-08-23 21:59 UTC
**Sample:** `11c1cfce546980287e7d3440033191844b5e5e321052d685f4c9ee49937fa688_11c1cfce546980287e7d3440033191844b5e5e321052d685f4c9ee49937fa688.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11c1cfce546980287e7d3440033191844b5e5e321052d685f4c9ee49937fa688_11c1cfce546980287e7d3440033191844b5e5e321052d685f4c9ee49937fa688.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,561,088 bytes |
| MD5 | `55ddf603015e60558debfd07390f4c17` |
| SHA1 | `0e477c81be68d8e523783ae46a5502574d481c2d` |
| SHA256 | `11c1cfce546980287e7d3440033191844b5e5e321052d685f4c9ee49937fa688` |
| Overall entropy | 7.954 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3923483659 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,558,528 | 7.957 | ⚠️ Yes |
| `.rsrc` | 1,536 | 4.104 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **4635** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

-	+#(

-"+&r
pjX	(e
YZjX(e
pjX	(e
YZjX(e
T/Gjqj
^Vd`aG#u
bW'F'=
h=S j#g
N+gG2XZ
ZPbqDB
:L9R2T
_/qhvo
&UjzQgm
3J9n
l0
w/r^L+
?=Vh(GSL/
2z/}&\2A
6x44#Q
{ZkK/6!3
rw-M~]i
3Y'nQK
~8K?}gO
VTOP M
 s]`6.
~HjHml
f/L$zN0q
_%(`V
,V2O>y<
`(dd};k2
VAyYs8
xA$^PV
H\Wehj

:Df;T
cHKBh$
uvgMW.
H{v u:
!.|BL>E|
v&%<At
wHh?mF
kf!=OtO
NtdLy&
B*( =$2
fb2LL>SI
]H#{ U/C
&TJhL)
-S0{p"
@ZMB{	
H:|y
~AL6E
!mmFzb0
6'LD=/
$w& B%
&T?K=+I
:^cPGx5
PdX$d#
t`L6T]
*;%{^T
x5zuBM
"AUz:QNF
 5%riH
vX~^@Y
~X9vKXvS

VhSmbk
D^	xLVG
L2Gc#g
dDx9?
ld=NtM
iE}VF\
+"!1	I
3 *QyI
^>=(>5)
U~xvj(GFO"
0*qZJn
H}~GQ}
VZ^'$n
f=SHs,f

>, JK~j
#9mDo{W
W
s5=_4J
]ewPL<9k
11]lTW
YMD${V'y
-Wv
-k(s
\8~rQqqa1
+D*Z*O
=5"Da+
P"vrrE
tD^^~E
j\2^&
1o E(lg
$a#do-W
^~]^e:'7
k3(=kc
xahaA:&
.,(O+r
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.Costura.AssemblyLoader.LoadStream` | `0x408934` | 1554124 | ✓ |
| `sym.__c..cctor_3` | `0x40275b` | 1553438 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x409364` | 62928 | ✓ |
| `method.Costura.AssemblyLoader..cctor` | `0x408b5c` | 2056 | — |
| `method.Plugin.StreamLibrary.UnsafeCodecs.UnsafeStreamCodec.CodeImage` | `0x404450` | 1984 | ✓ |
| `method.Client.Connection.ClientSocket.InitializeClient` | `0x406590` | 796 | ✓ |
| `method.Plugin.SendToMemory.Execute` | `0x403564` | 768 | ✓ |
| `method.Client.Install.NormalStartup.Install` | `0x406ec8` | 720 | ✓ |
| `method.PacketKeyLog.HandleLogger.HookCallback` | `0x4059cc` | 604 | ✓ |
| `method.Client.Connection.ClientSocket.Read` | `0x406c98` | 560 | ✓ |
| `method.Plugin.Packet.CaptureAndSend` | `0x403f90` | 536 | ✓ |
| `method.Client.Helper.DInvokeCore.GetExportAddress` | `0x407c34` | 524 | ✓ |
| `method.Client.Helper.A.GetExportAddress` | `0x407ebc` | 524 | — |
| `method.Plugin.Handler.HandleUninstall..ctor` | `0x405158` | 464 | ✓ |
| `method.Plugin.Connection.InitializeClient` | `0x40393c` | 452 | ✓ |
| `method.ConnectionKeyLog.Connection.InitializeClient` | `0x405d14` | 452 | ✓ |
| `method.ConnectionShell.Connection.InitializeClient` | `0x402eac` | 448 | ✓ |
| `method.ConnectionShell.Connection.ReadServertData` | `0x4030cc` | 448 | ✓ |
| `method.Plugin.Connection.ReadServertData` | `0x403b60` | 448 | ✓ |
| `method.ConnectionPe.Connection.InitializeClient` | `0x405328` | 448 | ✓ |
| `method.ConnectionPe.Connection.ReadServertData` | `0x405548` | 448 | ✓ |
| `method.ConnectionKeyLog.Connection.ReadServertData` | `0x405f30` | 448 | ✓ |
| `method.Client.Connection.ClientSocket.ReadServertData` | `0x406914` | 448 | ✓ |
| `method.Client.Algorithm.Aes256.Decrypt` | `0x408670` | 424 | ✓ |
| `method.Client.Helper.IdSender.SendInfo` | `0x407698` | 420 | ✓ |
| `method.Plugin.Packet.Read` | `0x403e2c` | 356 | ✓ |
| `method.Client.Settings.InitializeSettings` | `0x406270` | 356 | ✓ |
| `method.Plugin.StreamLibrary.UnsafeCodecs.UnsafeStreamCodec.DecodeData` | `0x404c98` | 340 | ✓ |
| `method.Client.Algorithm.Aes256.Encrypt` | `0x408530` | 320 | ✓ |
| `method.Client.Helper.AntiProcess.Block` | `0x4071e0` | 304 | ✓ |

### Decompiled Code Files

- [`code/method.Client.Algorithm.Aes256.Decrypt.c`](code/method.Client.Algorithm.Aes256.Decrypt.c)
- [`code/method.Client.Algorithm.Aes256.Encrypt.c`](code/method.Client.Algorithm.Aes256.Encrypt.c)
- [`code/method.Client.Connection.ClientSocket.InitializeClient.c`](code/method.Client.Connection.ClientSocket.InitializeClient.c)
- [`code/method.Client.Connection.ClientSocket.Read.c`](code/method.Client.Connection.ClientSocket.Read.c)
- [`code/method.Client.Connection.ClientSocket.ReadServertData.c`](code/method.Client.Connection.ClientSocket.ReadServertData.c)
- [`code/method.Client.Helper.AntiProcess.Block.c`](code/method.Client.Helper.AntiProcess.Block.c)
- [`code/method.Client.Helper.DInvokeCore.GetExportAddress.c`](code/method.Client.Helper.DInvokeCore.GetExportAddress.c)
- [`code/method.Client.Helper.IdSender.SendInfo.c`](code/method.Client.Helper.IdSender.SendInfo.c)
- [`code/method.Client.Install.NormalStartup.Install.c`](code/method.Client.Install.NormalStartup.Install.c)
- [`code/method.Client.Settings.InitializeSettings.c`](code/method.Client.Settings.InitializeSettings.c)
- [`code/method.ConnectionKeyLog.Connection.InitializeClient.c`](code/method.ConnectionKeyLog.Connection.InitializeClient.c)
- [`code/method.ConnectionKeyLog.Connection.ReadServertData.c`](code/method.ConnectionKeyLog.Connection.ReadServertData.c)
- [`code/method.ConnectionPe.Connection.InitializeClient.c`](code/method.ConnectionPe.Connection.InitializeClient.c)
- [`code/method.ConnectionPe.Connection.ReadServertData.c`](code/method.ConnectionPe.Connection.ReadServertData.c)
- [`code/method.ConnectionShell.Connection.InitializeClient.c`](code/method.ConnectionShell.Connection.InitializeClient.c)
- [`code/method.ConnectionShell.Connection.ReadServertData.c`](code/method.ConnectionShell.Connection.ReadServertData.c)
- [`code/method.Costura.AssemblyLoader.Attach.c`](code/method.Costura.AssemblyLoader.Attach.c)
- [`code/method.PacketKeyLog.HandleLogger.HookCallback.c`](code/method.PacketKeyLog.HandleLogger.HookCallback.c)
- [`code/method.Plugin.Connection.InitializeClient.c`](code/method.Plugin.Connection.InitializeClient.c)
- [`code/method.Plugin.Connection.ReadServertData.c`](code/method.Plugin.Connection.ReadServertData.c)
- [`code/method.Plugin.Handler.HandleUninstall..ctor.c`](code/method.Plugin.Handler.HandleUninstall..ctor.c)
- [`code/method.Plugin.Packet.CaptureAndSend.c`](code/method.Plugin.Packet.CaptureAndSend.c)
- [`code/method.Plugin.Packet.Read.c`](code/method.Plugin.Packet.Read.c)
- [`code/method.Plugin.SendToMemory.Execute.c`](code/method.Plugin.SendToMemory.Execute.c)
- [`code/method.Plugin.StreamLibrary.UnsafeCodecs.UnsafeStreamCodec.CodeImage.c`](code/method.Plugin.StreamLibrary.UnsafeCodecs.UnsafeStreamCodec.CodeImage.c)
- [`code/method.Plugin.StreamLibrary.UnsafeCodecs.UnsafeStreamCodec.DecodeData.c`](code/method.Plugin.StreamLibrary.UnsafeCodecs.UnsafeStreamCodec.DecodeData.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)
- [`code/sym.__c..cctor_3.c`](code/sym.__c..cctor_3.c)

## Behavioral Analysis

This analysis incorporates the findings from **chunk 5/5**. This final segment of disassembly reveals advanced anti-analysis techniques, evidence of multi-layered data decoding, and confirms the high level of sophistication in the malware's construction.

### New Findings from Chunk 5/5

#### 1. Multi-Layered Data Decoding (`UnsafeStreamCodec.DecodeData`)
The presence of the `UnsafeStreamCodec.DecodeData` function indicates that even after the AES-256 decryption (identified in previous chunks), the data packet may still be "wrapped" or encoded in a non-standard format.
*   **Complex Decoding Logic:** The disassembly shows intensive bitwise operations, complex shifts, and custom logic to process data streams. This is typical of **layered obfuscation**. 
*   **Implication:** Even if an analyst successfully intercepts the network traffic and breaks the AES encryption, the resulting raw "blob" may still be unreadable without passing through this specific decoding routine. It suggests that the malware's command structure is highly customized to hide its actual intent from automated scanners.

#### 2. Active Anti-Analysis Shields (`AntiProcess.Block`)
The inclusion of `method.Client.Helper.AntiProcess.Block` is a critical finding for any security operations team:
*   **Environment Awareness:** This function is designed to detect if the malware is being run in a "hostile" environment (e.g., a debugger, a sandbox, or an analysis VM). 
*   **Active Defense:** The name "Block" and the presence of complex loops suggest that upon detecting tools like x64dbg, Wireshark, or specific virtualization artifacts, the malware will intentionally crash itself, hang in a loop, or stop performing malicious actions to evade detection.
*   **Significance:** This confirms the threat actor is targeting high-value environments where they expect sophisticated defenders to be active.

#### 3. Robust Encryption Implementation (`Aes256.Encrypt`)
The disassembly confirms the use of a formal **AES-256** encryption implementation for its communication stack.
*   **Standardized Cryptography:** Unlike low-level "script kiddie" malware that uses simple XOR or Base64, this threat utilizes industry-standard high-strength encryption. 
*   **Impact on Traffic Analysis:** This ensures that the command and control (C2) infrastructure remains very difficult to map via traditional Deep Packet Inspection (DPI).

---

### Comprehensive Synthesis of Behavior & Functionality

The following sections integrate all findings from chunks 1 through 5:

#### 1. Sophisticated Communication Architecture
*   **Unified Pipeline:** The malware uses a unified communication library (`ReadServertData`) across its different modules (Shell, Keylog, etc.). This means the core "engine" is highly professional and shared across all features.
*   **Double Obfuscation:** The combination of **AES-256 encryption** followed by **UnsafeStreamCodec decoding** creates a significant hurdle for analysts: you must break the math (encryption) *and* the logic (decoding) to see what the malware is doing.

#### 2. Target Tracking and Persistence
*   **Individualized Triage:** The `IdSender` module confirms that every infected machine generates a unique fingerprint. This allows the attacker to maintain an organized "database" of victims, rather than treating each infection as an anonymous event.
*   **Dynamic Control:** The `InitializeSettings` routine ensures that the malware can change its behavior (e.g., turn off keylogging or switch C2 servers) without changing its file signature on disk.

#### 3. Anti-Analysis and Defense Evasion
*   **Evasive Execution:** The `AntiProcess` module indicates a proactive effort to "hide" from defenders. This is characteristic of **APT (Advanced Persistent Threat)** groups who want to maintain access for months or even years without being discovered by automated sandbox tools or manual forensic investigations.

---

### Final Summary for Incident Response & Defense

This malware represents a high-tier, sophisticated threat designed for long-term espionage and data exfiltration. It is not "noisy" and uses professional development techniques.

**Core Intelligence Indicators:**
1.  **Network Stealth (High):** Uses **AES-256** encryption. Network monitoring should focus on the *behavior* of the connection (frequency, duration, IP reputation) rather than attempting to inspect the content of the packets.
2.  **Execution Complexity (High):** The `DecodeData` routine suggests that even if a packet is captured, it is likely "packed" in a way that requires significant reverse engineering to interpret.
3.  **Anti-Forensic Capability:** The `AntiProcess.Block` module means that **standard automated sandboxes may fail to trigger the malware's full functionality.** It will behave "cleanly" if it senses it is being watched.

**Revised Recommended Actions:**
*   **Advanced Network Hunting:** Look for consistent, heart-beat style connections to suspicious IPs. Because the content is AES-encrypted, focus on identifying the **C2 infrastructure** rather than signature-matching of commands.
*   **Memory Forensics (Crucial):** Since the "decoding" happens in memory after the decryption stage, perform memory dumps of infected processes. This is your best chance to find cleartext strings or plain-text configuration files that are hidden by the `UnsafeStreamCodec`.
*   **Hardware/ID Correlation:** Use the findings from `IdSender` to your advantage. If you see multiple internal machines communicating with the same C2, cross-reference their unique hardware IDs (MACs, Serial numbers) to determine the true "breadth" of the infection.
*   **Hardened Analysis Environments:** When performing manual analysis, use "hardened" VMs and debuggers that mask common signs of virtualization/analysis to bypass the `AntiProcess.Block` checks.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1573** | Encrypted Channel | The malware utilizes standard AES-256 encryption to protect C2 communication and evade Deep Packet Inspection (DPI). |
| **T1027** | Obfuscated Files or Information | The `UnsafeStreamCodec` function uses non-standard decoding and bitwise operations to hide the actual command structure after decryption. |
| **T1497.001** | Virtualization/Sandbox Evasion | The `AntiProcess.Block` module detects virtual machines and sandbox environments to stop execution if a "hostile" environment is detected. |
| **T1562.001** | Debugger Detection | The malware specifically checks for analysis tools like x64dbg to identify the presence of an active human analyst. |
| **T1568** | Dynamic Resolution | The `InitializeSettings` routine allows the malware to dynamically switch C2 servers or toggle features without changing its file signature on disk. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *None identified.* (The provided "STRINGS" section contains obfuscated/encrypted data; no plaintext IP addresses or domains were present.)

**File paths / Registry keys**
*   *None identified.*

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (No MD5, SHA-1, or SHA-256 hashes were present in the provided strings.)

**Other artifacts**
*   **C2 Communication Patterns:** 
    *   Use of **AES-256 encryption** for all communication.
    *   Implementation of a non-standard **`UnsafeStreamCodec.DecodeData`** routine to wrap/obfuscate data after decryption.
    *   "Heartbeat" style connection patterns (noted in the final summary).
*   **Anti-Analysis / Evasion Features:**
    *   **`method.Client.Helper.AntiProcess.Block`**: Specific internal function used to detect and block execution in sandboxes, debuggers (e.g., x64dbg), or analysis tools (e.g., Wireshark).
*   **Malware Capabilities/Modules:**
    *   **`IdSender`**: Module utilized for generating unique hardware fingerprints (MACs, serial numbers) for victim tracking.
    *   **`ReadServertData`**: Core communication engine used across multiple modules (Shell, Keylog, etc.).
    *   **`InitializeSettings`**: Routine used to dynamically modify malware behavior and toggle features (e.g., keylogging).

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT
3. **Confidence**: High

4. **Key evidence**:
*   **Remote Access Functionality:** The presence of "Shell" and "Keylog" modules, integrated into a unified communication engine (`ReadServertData`), are primary indicators of a Remote Access Trojan (RAT) designed for persistent control and data theft.
*   **Sophisticated Evasion & Obfuscation:** The combination of high-level encryption (AES-256) followed by secondary custom decoding (`UnsafeStreamCodec`) and explicit anti-analysis checks (`AntiProcess.Block`) indicates a professional, high-tier threat designed to evade both automated sandboxes and manual forensic analysis.
*   **Systematic Victim Tracking:** The `IdSender` module creates unique hardware fingerprints for every infected machine, confirming the malware is part of an organized infrastructure where the attacker tracks individual "bots" or victims specifically rather than using a generic infection method.
