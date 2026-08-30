# Threat Analysis Report

**Generated:** 2026-08-16 20:55 UTC
**Sample:** `0fcbbe1cd6339c8d4ceb07fbbd614898a65dc1cc4222bd1290f1166710027ac6_0fcbbe1cd6339c8d4ceb07fbbd614898a65dc1cc4222bd1290f1166710027ac6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0fcbbe1cd6339c8d4ceb07fbbd614898a65dc1cc4222bd1290f1166710027ac6_0fcbbe1cd6339c8d4ceb07fbbd614898a65dc1cc4222bd1290f1166710027ac6.exe` |
| File type | PE32+ executable for MS Windows 4.00 (GUI), x86-64 Mono/.Net assembly, 2 sections |
| Size | 133,120 bytes |
| MD5 | `7aa01525f4fa37bd64e1c74195e02e23` |
| SHA1 | `29c12077264792b7f91f3c21203b8e2ff68f96a5` |
| SHA256 | `0fcbbe1cd6339c8d4ceb07fbbd614898a65dc1cc4222bd1290f1166710027ac6` |
| Overall entropy | 5.482 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774991226 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 130,560 | 5.511 | No |
| `.rsrc` | 2,048 | 3.599 | No |

## Extracted Strings

Total strings found: **906** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc

X )UU

-4	ri

&%r	

&%r#	

&%r7	

&%rA	

&%rK	

&%rU	

&%r_	

&%rk	

&%ru	

&%r#

&%r3

&%rA

&%rO

&%r_

&%r{

&%r%

&%r_

&%r3

&%rC

&%rW

&%rc

&%rs

-r5"

,R	,O

&%r <

&%r8<

&%rF<

&%rR<

&%r\<

&%rn<

&%r$=

&%r,=

&%r8=

&%rJ=

&%r\=

&%rh=

&%rv=

&%r">

&%r2>

&%r@>

&%rJ>

&%rZ>

&%rj>

&%rx>
v4.0.30319
#Strings
	,	6	C	
	&
-
7
V

3?NR
<FetchRulesIfNeeded>d__120
<ExecuteAndPostResult>d__150
<>c__DisplayClass150_0
<>c__DisplayClass170_0
<>c__DisplayClass131_0
<>9__123_0
<BuildBankInventory>b__123_0
<>9__114_0
<RunTcpMode>b__114_0
<>c__DisplayClass114_0
<>c__DisplayClass105_0
<>9__165_0
<FetchDll>b__165_0
<>c__DisplayClass116_0
<>9__136_0
<BuildWalletsListJson>b__136_0
<>9__147_0
<ExecuteCommandLine>b__147_0
<>9__198_0
<WebcamCaptureWorker>b__198_0
<>9__209_0
<StartDesktopCapture>b__209_0
<>c__DisplayClass209_0
<>c__DisplayClass149_0
<>9__0
<MainAsync>b__0
<TryDispatchNextCommand>b__0
<CollectViaDllInjection>b__0
<TcpReadLoop>b__0
<GetEnabledWalletIdsFromRules>b__0
<ExecuteAndPostResult>b__0
<>9__123_1
<BuildBankInventory>b__123_1
<>c__DisplayClass105_1
<>c__DisplayClass116_1
<>8__1
<>9__1
<MainAsync>b__1
<RunTcpMode>b__1
<StartDesktopCapture>b__1
<TcpReadLoop>b__1
<>u__1
Func`1
IEnumerable`1
IOrderedEnumerable`1
ConfiguredTaskAwaitable`1
Task`1
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x1400030cc` | 131072 | ✓ |
| `method.__f__AnonymousType0_2.GetHashCode` | `0x1400020bd` | 131072 | ✓ |
| `method._ToStringList_d__126.System.Collections.IEnumerable.GetEnumerator` | `0x14000d36f` | 19790 | ✓ |
| `method.__TryDispatchNextCommand_b__0_d.SetStateMachine` | `0x14000ed94` | 17208 | ✓ |
| `method.Paramount.Agent.Program.ToBool` | `0x140005435` | 15926 | ✓ |
| `method.__c._FetchDll_b__165_0` | `0x14000b2c3` | 7972 | ✓ |
| `method.Paramount.Agent.Program.StopDesktopCapture` | `0x1400094cb` | 7558 | ✓ |
| `method.Paramount.Agent.Program..cctor` | `0x140009550` | 7456 | ✓ |
| `method._MainAsync_d__105.MoveNext` | `0x14000bd7c` | 2204 | ✓ |
| `method.Paramount.Agent.Program.IsAnalysisEnvironment` | `0x140002844` | 2160 | ✓ |
| `method.Paramount.Agent.Program.CollectViaDllInjection` | `0x1400069f0` | 1880 | ✓ |
| `method.Paramount.Agent.Program.GetDiscordTokens` | `0x140007838` | 1776 | ✓ |
| `method.Paramount.Agent.Program.GetPcInfo` | `0x14000545c` | 1692 | ✓ |
| `method.Paramount.Agent.Program.IsLikelyVirtualMachineOrSandbox` | `0x1400022ac` | 1432 | ✓ |
| `method.__MainAsync_b__1_d.MoveNext` | `0x14000dda0` | 1296 | ✓ |
| `method._RunTcpMode_d__114.MoveNext` | `0x14000c94c` | 1184 | ✓ |
| `method._TryDispatchNextCommand_d__149.MoveNext` | `0x14000d378` | 1172 | ✓ |
| `method.__RunTcpMode_b__1_d.MoveNext` | `0x14000e2c0` | 1140 | ✓ |
| `method.Paramount.Agent.Program.BuildWalletsZip` | `0x140004454` | 1128 | ✓ |
| `method.Paramount.Agent.Program.GetDiscordTokensFromMemory` | `0x140007f28` | 1124 | ✓ |
| `method.Paramount.Agent.Program.FmList` | `0x140005cc0` | 936 | ✓ |
| `method.__MainAsync_b__0_d.MoveNext` | `0x14000d9f0` | 928 | ✓ |
| `method.Paramount.Agent.Program.CollectJsonFiles` | `0x1400071e0` | 888 | ✓ |
| `method.Paramount.Agent.Program.WebcamCaptureWorker` | `0x140008d00` | 884 | ✓ |
| `method._PostCommandResultAsync_d__148.MoveNext` | `0x14000c628` | 788 | ✓ |
| `method.__TcpReadLoop_b__2_d.MoveNext` | `0x14000e8fc` | 768 | ✓ |
| `method._TcpSendInventoryUpdate_d__117.MoveNext` | `0x14000cdfc` | 764 | ✓ |
| `method.Paramount.Agent.Program.ExecuteCommandLine` | `0x140005014` | 728 | ✓ |
| `method.Paramount.Agent.Program.FetchDll` | `0x140006414` | 640 | ✓ |
| `method._ExecuteAndPostResult_d__150.MoveNext` | `0x14000b78c` | 616 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Paramount.Agent.Program..cctor.c`](code/method.Paramount.Agent.Program..cctor.c)
- [`code/method.Paramount.Agent.Program.BuildWalletsZip.c`](code/method.Paramount.Agent.Program.BuildWalletsZip.c)
- [`code/method.Paramount.Agent.Program.CollectJsonFiles.c`](code/method.Paramount.Agent.Program.CollectJsonFiles.c)
- [`code/method.Paramount.Agent.Program.CollectViaDllInjection.c`](code/method.Paramount.Agent.Program.CollectViaDllInjection.c)
- [`code/method.Paramount.Agent.Program.ExecuteCommandLine.c`](code/method.Paramount.Agent.Program.ExecuteCommandLine.c)
- [`code/method.Paramount.Agent.Program.FetchDll.c`](code/method.Paramount.Agent.Program.FetchDll.c)
- [`code/method.Paramount.Agent.Program.FmList.c`](code/method.Paramount.Agent.Program.FmList.c)
- [`code/method.Paramount.Agent.Program.GetDiscordTokens.c`](code/method.Paramount.Agent.Program.GetDiscordTokens.c)
- [`code/method.Paramount.Agent.Program.GetDiscordTokensFromMemory.c`](code/method.Paramount.Agent.Program.GetDiscordTokensFromMemory.c)
- [`code/method.Paramount.Agent.Program.GetPcInfo.c`](code/method.Paramount.Agent.Program.GetPcInfo.c)
- [`code/method.Paramount.Agent.Program.IsAnalysisEnvironment.c`](code/method.Paramount.Agent.Program.IsAnalysisEnvironment.c)
- [`code/method.Paramount.Agent.Program.IsLikelyVirtualMachineOrSandbox.c`](code/method.Paramount.Agent.Program.IsLikelyVirtualMachineOrSandbox.c)
- [`code/method.Paramount.Agent.Program.StopDesktopCapture.c`](code/method.Paramount.Agent.Program.StopDesktopCapture.c)
- [`code/method.Paramount.Agent.Program.ToBool.c`](code/method.Paramount.Agent.Program.ToBool.c)
- [`code/method.Paramount.Agent.Program.WebcamCaptureWorker.c`](code/method.Paramount.Agent.Program.WebcamCaptureWorker.c)
- [`code/method._ExecuteAndPostResult_d__150.MoveNext.c`](code/method._ExecuteAndPostResult_d__150.MoveNext.c)
- [`code/method._MainAsync_d__105.MoveNext.c`](code/method._MainAsync_d__105.MoveNext.c)
- [`code/method._PostCommandResultAsync_d__148.MoveNext.c`](code/method._PostCommandResultAsync_d__148.MoveNext.c)
- [`code/method._RunTcpMode_d__114.MoveNext.c`](code/method._RunTcpMode_d__114.MoveNext.c)
- [`code/method._TcpSendInventoryUpdate_d__117.MoveNext.c`](code/method._TcpSendInventoryUpdate_d__117.MoveNext.c)
- [`code/method._ToStringList_d__126.System.Collections.IEnumerable.GetEnumerator.c`](code/method._ToStringList_d__126.System.Collections.IEnumerable.GetEnumerator.c)
- [`code/method._TryDispatchNextCommand_d__149.MoveNext.c`](code/method._TryDispatchNextCommand_d__149.MoveNext.c)
- [`code/method.__MainAsync_b__0_d.MoveNext.c`](code/method.__MainAsync_b__0_d.MoveNext.c)
- [`code/method.__MainAsync_b__1_d.MoveNext.c`](code/method.__MainAsync_b__1_d.MoveNext.c)
- [`code/method.__RunTcpMode_b__1_d.MoveNext.c`](code/method.__RunTcpMode_b__1_d.MoveNext.c)
- [`code/method.__TcpReadLoop_b__2_d.MoveNext.c`](code/method.__TcpReadLoop_b__2_d.MoveNext.c)
- [`code/method.__TryDispatchNextCommand_b__0_d.SetStateMachine.c`](code/method.__TryDispatchNextCommand_b__0_d.SetStateMachine.c)
- [`code/method.__c._FetchDll_b__165_0.c`](code/method.__c._FetchDll_b__165_0.c)
- [`code/method.__f__AnonymousType0_2.GetHashCode.c`](code/method.__f__AnonymousType0_2.GetHashCode.c)

## Behavioral Analysis

### Analysis Summary: Infostealer & Remote Access Trojan (RAT)

Based on the provided strings and disassembled code, this binary is a sophisticated **Infostealer** and potentially a **Remote Access Trojan (RAT)** designed to gather sensitive information from a victim's machine, exfiltrate it to a remote server, and perform spying activities. The presence of extensive obfuscation in the disassembly suggests a high level of intent to evade analysis.

### Core Functionality and Purpose
The primary purpose of this malware is to identify and steal sensitive digital assets and personal information. The naming conventions (e.g., "Bank," "Wallet," "Discord") suggest it specifically targets users of financial services and social media platforms, likely for the purposes of credential theft or cryptocurrency theft.

### Suspicious and Malicious Behaviors

*   **Information Stealing (Infostealer):**
    *   **Credential Theft:** The code contains functions to collect **Discord tokens** (`GetDiscordTokens`) and sensitive personal information (`GetPcInfo`).
    *   **Financial Targeting:** There is specific logic for building a "Bank Inventory" (`BuildBankInventory`), fetching "Wallets," and searching for "Wallet" information.
    *   **Clipboard Monitoring:** The inclusion of `GetClipboardData` and `SetClipboardData` suggests the malware monitors the system clipboard to intercept passwords or cryptocurrency addresses as they are copied.

*   **Spyware & Surveillance:**
    *   **Visual Surveillance:** The binary contains functions for **Webcam Capture** (`WebcamCaptureWorker`) and **Desktop Capture** (`StartDesktopCapture`). This allows the attacker to record the user's surroundings or view their screen in real-time.
    *   **Geolocation Tracking:** `FetchGeoInfo` indicates the malware attempts to determine the victim’s physical location via their IP address.

*   **Persistence & Command and Control (C2):**
    *   **Dual Communication Modes:** The code supports both **TCP mode** (`RunTcpMode`, `TcpReadLoop`) for direct, potentially persistent interaction with a remote operator, and **HTTP/HTTPS posting** (`PostCommandResultAsync`, `ExecuteAndPostResult`) to exfiltrate gathered data.
    *   **Loader Behavior:** The functions `FetchDll` and `ExecuteCommandLine` indicate the binary acts as a "loader" or "dropper," designed to download additional malicious modules (DLLs) from a remote server and execute them on the system.

*   **Anti-Analysis & Evasion:**
    *   **Environment Awareness:** The code explicitly checks for analysis environments via `IsAnalysisEnvironment` and `IsLikelyVirtualMachineOrSandbox`. This is used to prevent the malware from running in a researcher's sandbox or a VM, which would alert the attacker.
    *   **Obfuscation:** The disassembly shows "bad instruction data" and "truncated control flow," which are common signs of **control-flow obfuscation**. This technique is designed to break automated decompiler tools and frustrate manual analysis by human researchers.

### Notable Techniques & Patterns
*   **DLL Injection:** The function `CollectViaDllInjection` confirms the use of DLL injection, a common technique to hide malicious activity within the memory space of legitimate processes (like web browsers) to bypass security software.
*   **Data Serialization:** Use of JSON formats (`BuildWalletsListJson`, `rulesJson`) for internal data management and communication with C2 servers.
*   **Resource Masking:** The presence of "Base64" strings related to icons and images suggests the malware may display a fake, legitimate-looking GUI or pop-up while it performs its malicious actions in the background.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055.001** | Process Injection: DLL | The presence of the `CollectViaDllInjection` function confirms that the malware injects code into other processes to hide its activity. |
| **T1005** | Data from Local System | The malware systematically collects Discord tokens, system information, and monitors clipboard data for sensitive credentials. |
| **T1071** | Application Layer Protocol | The use of both TCP and HTTP/HTTPS protocols for communication indicates the use of standard network protocols for C2 and exfiltration. |
| **T1105** | Ingress Tool Transfer | The `FetchDll` functionality identifies the malware's role as a "loader" designed to pull additional malicious modules from remote servers. |
| **T1497** | Virtualization/Sandbox Evasion | Specific checks for analysis environments and virtual machines are used to detect and bypass security researcher tools. |
| **T1027** | Obfuscated Files or Information | The use of control-flow obfuscation (e.g., "bad instruction data") is intended to hinder manual and automated reverse engineering. |
| **T1059** | Command and Scripting Interpreter | The `ExecuteCommandLine` function indicates the ability to execute arbitrary commands on the victim's system. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified in the provided text. While variables like `<baseHttpUrl>` and `<publicIp>` were found, no specific hardcoded IP addresses or domains were present.)*

**File paths / Registry keys**
*   `Parmount.Agent.tmp.2b0ec031348c40b99b7504fc67dce4ca` (Potential temporary file/artifact)

**Mutex names / Named pipes**
*   *(None identified in the provided strings.)*

**Hashes**
*   *(No MD5, SHA-1, or SHA-256 hashes were found in the input string.)*

**Other artifacts**
*   **C2 Communication Patterns:** 
    *   Dual communication modes: TCP (via `RunTcpMode` and `TcpReadLoop`) and HTTP/HTTPS posting (via `PostCommandResultAsync` and `ExecuteAndPostResult`).
*   **Data Exchange Formats:** Use of JSON for internal data management (`rulesJson`, `resultJson`, `BuildWalletsListJson`).
*   **Targeted Information Indicators:** 
    *   Discord Token extraction (`GetDiscordTokens`)
    *   Financial/Cryptocurrency targeting ("Bank", "Wallet")
    *   Geo-location tracking via IP (`FetchGeoInfo`)
*   **Spyware Capabilities:**
    *   Webcam capture (`WebcamCaptureWorker`, `_lastWeb_frameB64`)
    *   Desktop capture (`StartDesktopCapture`)
    *   Clipboard monitoring (`GetClipboardData`, `SetClipboardData`)
*   **Evasion/Technical Indicators:**
    *   `IsAnalysisEnvironment` and `IsLikelyVirtualMachineOrSandbox` (Anti-VM/Sandbox checks)
    *   `CollectViaDllInjection` (Technique for hiding activity in other processes)
    *   `FetchDll` / `ExecuteCommandLine` (Loader behavior for fetching additional modules)

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Infostealer / RAT (Remote Access Trojan)
3. **Confidence**: High

4. **Key evidence**:
*   **Comprehensive Information Theft:** The sample contains specific functions for stealing Discord tokens, gathering financial "Bank" and "Wallet" data, and monitoring the system clipboard to intercept credentials.
*   **Spyware & Surveillance Capabilities:** The inclusion of `WebcamCaptureWorker`, `StartDesktopCapture`, and `FetchGeoInfo` demonstrates a clear intent to conduct real-time spying and location tracking of the victim.
*   **Advanced Evasion & Persistence:** The malware employs sophisticated evasion techniques including anti-VM/sandbox checks (`IsAnalysisEnvironment`), control-flow obfuscation, and DLL injection (`CollectViaDllInjection`) to hide its presence while acting as a loader for additional malicious modules via `FetchDll`.
