# Threat Analysis Report

**Generated:** 2026-07-01 19:13 UTC
**Sample:** `038da7941cb395df589983f3b09346694fe2a3a9e458a295ebfd5bd7c9fdb434_038da7941cb395df589983f3b09346694fe2a3a9e458a295ebfd5bd7c9fdb434.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `038da7941cb395df589983f3b09346694fe2a3a9e458a295ebfd5bd7c9fdb434_038da7941cb395df589983f3b09346694fe2a3a9e458a295ebfd5bd7c9fdb434.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 2,613,248 bytes |
| MD5 | `802aa7a4a57b22e797ebeb2b3b638527` |
| SHA1 | `6179f1929d3b2cdeb9d453ef1ec5ce3c88521923` |
| SHA256 | `038da7941cb395df589983f3b09346694fe2a3a9e458a295ebfd5bd7c9fdb434` |
| Overall entropy | 7.975 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3787254337 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,610,176 | 7.976 | ⚠️ Yes |
| `.rsrc` | 2,048 | 3.72 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **6126** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

,Z	rD

-rx	
	*rC,
Ww2(t'K
9Gc0L
qL@E{h
8Lm1[rg	
p+Z,NV
bgvkw$
)};zp4
VC_E\7`YA
sDY1RLiEL
jN8z~j4t
A&[JjS
3| yxGX
=\Xp?,
CXg=le
I*dr6B
lZ}~El
X=+
^|
_Z;j0
if?Y!~B
r[NMFG->
rq3T+:a
n`f?(y4
h6!+Fq3
|aZrDNw
e'L?]f
L7+%<[
/2}t.Xt
]~P{{{
hG^.l5
J'
/r1]xWX
GjMPET
rzR}R:R
/:f	"W^
ZN!qEA
m9sG,D
5!,}*&IW
@1f(T:
Hi8R-T
I`a28[
uIZ`@+C
RCc"3M
PJL>"
\J{!<!
.BP53
p|-fTTcF
sxN[m7JQ
H_;>Y<
tg#YU;
Jb>S1t
3s14eja
K"$# 9
w$Ru20L
!v!"`z
dbu9r
BjUZ7F
I]zA#]t
A-	~Y
/]:S.,	I
F>";{G
rwM!7_
cBM$=q
%&;j@Q
Qq+r^7
2:2]FGE
t98ID~RS
cv<C v
5b1Fv'l
C?Yt=t
Empes8
Rh]GWJ
dDFH'@
~w!wLg
zv-}_=1
B^;jw
;qGZ)[sW
)c<:X
bDKT13
%ep[Ih
HnwD@@
x_Q$8i
aLDqIx
IaO
{tm
8dtf{6[=
1x`Q:T
y *GBy
e `mt	1
tT l{{
t^0;p~
v1Y}Y|
]<ARnQ
IKE2@+
AxUpp
Xc*C<

UyD:B&e
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.SQLiteReader.SQLiteReader.IsOdd` | `0x40244f` | 2621440 | ✓ |
| `sym.Costura.AssemblyLoader.LoadStream` | `0x40e960` | 2578080 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x40ebfc` | 64868 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.ExtractTokens` | `0x403c21` | 16320 | ✓ |
| `method.__c._SendToTelegram_b__75_0` | `0x407be9` | 11242 | ✓ |
| `method.FirefoxHistory.set_LastVisit` | `0x40c41b` | 7604 | ✓ |
| `method.CreditCard.set_number` | `0x40ad4f` | 5624 | ✓ |
| `method.SQLiteReader.SQLiteReader..cctor` | `0x402d37` | 3818 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.GatherSystemInfo` | `0x4055dc` | 2084 | ✓ |
| `method.chrome_v20_decryption_CSharp.Chromium..cctor` | `0x409fa0` | 2082 | ✓ |
| `entry0` | `0x403268` | 1792 | ✓ |
| `method.chrome_v20_decryption_CSharp.CryptoWallets.GrabBrowserWallets` | `0x40d274` | 1764 | ✓ |
| `method.chrome_v20_decryption_CSharp.CryptoWallets.GrabCryptoWallets` | `0x40c4ac` | 1676 | ✓ |
| `method.chrome_v20_decryption_CSharp.CryptoWallets.GrabCryptoDeFiWallet` | `0x40e22b` | 1584 | ✓ |
| `method.chrome_v20_decryption_CSharp.CryptoWallets..cctor` | `0x40e25c` | 1552 | ✓ |
| `method.chrome_v20_decryption_CSharp.Firefox.WriteFirefoxData` | `0x40bdd4` | 1280 | ✓ |
| `method.SQLiteReader.SQLiteReader.ReadTableFromOffset` | `0x4028cc` | 1148 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.SendToTelegram` | `0x407018` | 1128 | ✓ |
| `method.chrome_v20_decryption_CSharp.Chromium.deriveV20MasterKey` | `0x409b3c` | 1008 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.ScanFileSystem` | `0x40517c` | 960 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.WriteCookies` | `0x405f9c` | 932 | ✓ |
| `method.chrome_v20_decryption_CSharp.Chromium.GetV20MasterKey` | `0x408f48` | 876 | ✓ |
| `method.chrome_v20_decryption_CSharp.Chromium.GetV20_2MasterKey` | `0x4092b4` | 876 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.SendToPanel` | `0x406cb4` | 868 | ✓ |
| `method.chrome_v20_decryption_CSharp.CryptoWallets.GrabTrustWallet` | `0x40d958` | 868 | ✓ |
| `method.chrome_v20_decryption_CSharp.Firefox.DecryptFirefoxPBE` | `0x40b01c` | 860 | ✓ |
| `method.chrome_v20_decryption_CSharp.CryptoWallets.GrabMetaMaskWallet` | `0x40dcbc` | 860 | ✓ |
| `method.chrome_v20_decryption_CSharp.CryptoWallets.CopyElectrumFilesWithSizeLimit` | `0x40cb60` | 852 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.ExtractDiscordTokens` | `0x403c34` | 828 | ✓ |
| `method.chrome_v20_decryption_CSharp.Program.ExtractWindowsCredentials` | `0x404d58` | 800 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Costura.AssemblyLoader.Attach.c`](code/method.Costura.AssemblyLoader.Attach.c)
- [`code/method.CreditCard.set_number.c`](code/method.CreditCard.set_number.c)
- [`code/method.FirefoxHistory.set_LastVisit.c`](code/method.FirefoxHistory.set_LastVisit.c)
- [`code/method.SQLiteReader.SQLiteReader..cctor.c`](code/method.SQLiteReader.SQLiteReader..cctor.c)
- [`code/method.SQLiteReader.SQLiteReader.IsOdd.c`](code/method.SQLiteReader.SQLiteReader.IsOdd.c)
- [`code/method.SQLiteReader.SQLiteReader.ReadTableFromOffset.c`](code/method.SQLiteReader.SQLiteReader.ReadTableFromOffset.c)
- [`code/method.__c._SendToTelegram_b__75_0.c`](code/method.__c._SendToTelegram_b__75_0.c)
- [`code/method.chrome_v20_decryption_CSharp.Chromium..cctor.c`](code/method.chrome_v20_decryption_CSharp.Chromium..cctor.c)
- [`code/method.chrome_v20_decryption_CSharp.Chromium.GetV20MasterKey.c`](code/method.chrome_v20_decryption_CSharp.Chromium.GetV20MasterKey.c)
- [`code/method.chrome_v20_decryption_CSharp.Chromium.GetV20_2MasterKey.c`](code/method.chrome_v20_decryption_CSharp.Chromium.GetV20_2MasterKey.c)
- [`code/method.chrome_v20_decryption_CSharp.Chromium.deriveV20MasterKey.c`](code/method.chrome_v20_decryption_CSharp.Chromium.deriveV20MasterKey.c)
- [`code/method.chrome_v20_decryption_CSharp.CryptoWallets..cctor.c`](code/method.chrome_v20_decryption_CSharp.CryptoWallets..cctor.c)
- [`code/method.chrome_v20_decryption_CSharp.CryptoWallets.CopyElectrumFilesWithSizeLimit.c`](code/method.chrome_v20_decryption_CSharp.CryptoWallets.CopyElectrumFilesWithSizeLimit.c)
- [`code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabBrowserWallets.c`](code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabBrowserWallets.c)
- [`code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabCryptoDeFiWallet.c`](code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabCryptoDeFiWallet.c)
- [`code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabCryptoWallets.c`](code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabCryptoWallets.c)
- [`code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabMetaMaskWallet.c`](code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabMetaMaskWallet.c)
- [`code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabTrustWallet.c`](code/method.chrome_v20_decryption_CSharp.CryptoWallets.GrabTrustWallet.c)
- [`code/method.chrome_v20_decryption_CSharp.Firefox.DecryptFirefoxPBE.c`](code/method.chrome_v20_decryption_CSharp.Firefox.DecryptFirefoxPBE.c)
- [`code/method.chrome_v20_decryption_CSharp.Firefox.WriteFirefoxData.c`](code/method.chrome_v20_decryption_CSharp.Firefox.WriteFirefoxData.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.ExtractDiscordTokens.c`](code/method.chrome_v20_decryption_CSharp.Program.ExtractDiscordTokens.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.ExtractTokens.c`](code/method.chrome_v20_decryption_CSharp.Program.ExtractTokens.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.ExtractWindowsCredentials.c`](code/method.chrome_v20_decryption_CSharp.Program.ExtractWindowsCredentials.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.GatherSystemInfo.c`](code/method.chrome_v20_decryption_CSharp.Program.GatherSystemInfo.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.ScanFileSystem.c`](code/method.chrome_v20_decryption_CSharp.Program.ScanFileSystem.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.SendToPanel.c`](code/method.chrome_v20_decryption_CSharp.Program.SendToPanel.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.SendToTelegram.c`](code/method.chrome_v20_decryption_CSharp.Program.SendToTelegram.c)
- [`code/method.chrome_v20_decryption_CSharp.Program.WriteCookies.c`](code/method.chrome_v20_decryption_CSharp.Program.WriteCookies.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)

## Behavioral Analysis

This final segment of disassembly provides a deep look into the **protection layer** used by the malware. While previous chunks focused on the *payload* (what data is stolen), this section highlights the *delivery and evasion mechanism* (how it hides from security).

The following analysis integrates these findings with the previous reports.

---

### Updated Analysis of Findings

#### 1. Advanced Anti-Analysis & Obfuscation Techniques
The disassembly in chunk 5/5 provides clear evidence of high-level obfuscation techniques intended to defeat both automated scanners (AV/EDR) and manual reverse engineering:

*   **Control Flow Flattening:** The repeated use of `while(true)` loops combined with complex, multi-step calculations to determine the next jump destination is a classic indicator of "Control Flow Flattening." This replaces a straightforward logical flow with a central dispatcher, making it extremely difficult for an analyst to follow the code's logic linearly.
*   **Opaque Predicates & Carry Flag Manipulation:** The frequent use of `CARRY1`, `CARRY4`, and `CONCAT` functions suggests that the malware is using "opaque predicates"—logical branches where the outcome is always the same but is calculated through complex math so that a disassembler cannot determine which path is taken.
*   **Instruction Overlapping & Junk Code:** The warning `"WARNING: Bad instruction - Truncating control flow"` indicates that the author has deliberately overlapped instructions or inserted "junk" bytes. This causes disassemblers to misinterpret where an instruction begins, often leading them to follow a "dead end" or incorrect path while the CPU correctly executes the hidden malicious logic.
*   **Dynamic Address Calculation:** Instead of jumping to fixed addresses (e.g., `JMP 0x401000`), the malware calculates jump targets at runtime (e.g., `pcVar8 = CONCAT31(Var12,uVar4) + 0x6f287000`). This prevents automated tools from mapping out the program's behavior before it runs.

#### 2. Decryption/Unpacking Routine
The repeated calls to `func_0x00222808()` with varying arguments suggests a **multi-stage decryption or unpacking routine**. 
*   The complex mathematical operations surrounding these calls (e.g., `uVar16 = extraout_ECX + *apuStack_c[0] + uVar2`) are likely used to decrypt the next "chunk" of the malware's code into memory.
*   **Implication:** The actual stealing logic for Discord tokens and Crypto wallets may be encrypted in the file and only decrypted in memory just before execution, making static analysis much harder.

#### 3. Resilience against Automated Analysis
The "noisy" nature of this specific code block—the heavy use of bitwise shifts (`>> 0x10`), complex arithmetic for simple increments, and overlapping instructions—is designed to **timeout or crash automated decompilers**. This ensures that the malware remains functional while becoming a "black box" to security researchers.

---

### Comprehensive Summary of Findings (Cumulative)

The binary is confirmed as a **highly sophisticated, multi-vector Infostealer** equipped with professional-grade protection layers.

*   **Primary Payload:** A comprehensive "grab-all" suite targeting:
    *   **Cryptocurrency:** Specific targets include Trust Wallet and Electrum wallets.
    *   **Social Media/Identity:** Target of Discord session tokens (bypassing 2FA).
    *   **System Assets:** Harvesting of Windows credentials, credit cards, and browser history across Chrome, Edge, Brave, and Firefox.
*   **Exfiltration Method:** Integration with the Telegram Bot API for rapid data delivery to a Command & Control (C2) server.
*   **Evasion Strategy:** The use of advanced obfuscation (Control Flow Flattening, Junk Code, and Dynamic Decryption) indicates this is a **Malware-as-a-Service (MaaS)** product intended to remain undetected on high-value targets for as long as possible.

---

### Updated Risk Profile

| Feature | Risk Level | Technical Detail |
| :--- | :--- | :--- |
| **Primary Motivation** | **Critical** | Targeted theft of Crypto, Discord accounts (for secondary scams), and System Credentials. |
| **Exfiltration Method** | **High** | Integrated Telegram Bot API for immediate data exfiltration. |
| **Targeted Infrastructure** | **Extreme** | Multi-browser support; targets "hot" and "cold" crypto wallet types. |
| **Anti-Analysis Tactics** | **Critical** | Use of Control Flow Flattening, Opaque Predicates, and Junk Code to evade EDR/AV signatures. |
| **Data Reach** | **Critical** | Full compromise of digital identity (Discord), financial assets, and local system access. |

---

### Final Conclusion & Recommendations

This is not a novice-level script; it is a **top-tier professional infostealer**. The complexity of the obfuscation in the final segment proves that the authors possess significant expertise in malware development and anti-forensics.

**High-Priority Actions for Incident Response:**
1.  **Isolate & Sanitize:** Any machine where this binary was executed must be treated as "burned." Isolate it from the network immediately.
2.  **Session Revocation:** Because Discord tokens were targeted, **all session tokens** for compromised accounts must be invalidated (forcing a logout of all devices). 
3.  **Credential Reset:** Force an immediate password and 2FA reset on any accounts accessed via the infected machine (Google, Microsoft, Banking, etc.).
4.  **Crypto Security:** Move assets from "hot" wallets to cold storage immediately. If a wallet was linked to the infected system, it must be considered compromised.
5.  **Indicator of Compromise (IoC) Note:** The presence of `chrome_v20` and specific folder-scanning logic indicates the malware specifically targets local state files; scan for unauthorized access to `%LocalAppData%` related browser folders during forensics.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your analysis to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Programs | The use of control flow flattening, opaque predicates, and junk code is designed to hinder manual reverse engineering and evade automated detection. |
| **T1027.001** | Packing | The multi-stage decryption/unpacking routine is used to hide the primary malicious payload from static analysis until execution. |
| **T1555** | Credentials from Web Browsers | The malware specifically targets browser data (Chrome, Edge, Brave, Firefox) to steal passwords, history, and session tokens (e.g., Discord). |
| **T1083** | File and Directory Discovery | The presence of specific logic to scan `%LocalAppData%` folders indicates a targeted search for local wallet files and browser state data. |
| **T1567** | Exfiltration Over Web Service | The integration of the Telegram Bot API facilitates the automated exfiltration of stolen assets to a remote infrastructure. |
| **T1036** | Modify Authentication Check | By targeting Discord session tokens, the malware successfully bypasses multi-factor authentication (MFA) for secondary exploitation. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (While "Telegram Bot API" is mentioned as an exfiltration method, no specific Telegram handles, bot tokens, or IP addresses were provided in the text.)

**File paths / Registry keys**
*   *None identified.* (The term `chrome_v20` is mentioned in the analysis regarding search logic for local state files, but no specific absolute file paths—e.g., `%AppData%` or `C:\...`—were provided.)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None found.* (The "Extracted Strings" block contains obfuscated binary data/junk code, but no recognizable MD5, SHA1, or SHA256 hashes were present.)

**Other artifacts**
*   **C2/Exfiltration Pattern:** Integration with the **Telegram Bot API** for rapid data exfiltration.
*   **Targeted Data Assets:** 
    *   Discord session tokens (used to bypass 2FA).
    *   "Trust Wallet" and "Electrum" crypto wallets.
    *   System credentials and credit card information from Chrome, Edge, Brave, and Firefox.
*   **Evasion Techniques:** Control Flow Flattening, Opaque Predicates, and Junk Code insertion (designed to bypass automated EDR/AV detection).

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: Unknown (Note: Exhibits characteristics typical of a "Malware-as-a-Service" (MaaS) model).
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Targeted Data Collection:** The malware is designed to perform a "grab-all" operation, specifically targeting high-value assets including Discord session tokens (to bypass 2FA), specific cryptocurrency wallets (Trust Wallet, Electrum), and system/browser credentials across multiple platforms (Chrome, Edge, Brave, Firefox).
    *   **Advanced Evasion Techniques:** The implementation of professional-grade protection layers—including Control Flow Flattening, Opaque Predicates, and dynamic decryption routines—indicates a sophisticated effort to bypass automated EDR/AV detection.
    *   **Modern Exfiltration Method:** The integration with the Telegram Bot API is a standard method for modern infostealers to provide immediate data delivery to attackers while maintaining an asynchronous communication channel.
