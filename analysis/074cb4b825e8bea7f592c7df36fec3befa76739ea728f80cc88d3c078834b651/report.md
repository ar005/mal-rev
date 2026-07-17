# Threat Analysis Report

**Generated:** 2026-07-16 17:48 UTC
**Sample:** `074cb4b825e8bea7f592c7df36fec3befa76739ea728f80cc88d3c078834b651_074cb4b825e8bea7f592c7df36fec3befa76739ea728f80cc88d3c078834b651.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `074cb4b825e8bea7f592c7df36fec3befa76739ea728f80cc88d3c078834b651_074cb4b825e8bea7f592c7df36fec3befa76739ea728f80cc88d3c078834b651.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 482,968 bytes |
| MD5 | `910a4fd3e0fbf3c3c07a44f3c266512e` |
| SHA1 | `4ab3625fd9fea9ab92e85f2cfea1cf6fbe0a5a0c` |
| SHA256 | `074cb4b825e8bea7f592c7df36fec3befa76739ea728f80cc88d3c078834b651` |
| Overall entropy | 6.04 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3081575580 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 465,408 | 5.982 | No |
| `.rsrc` | 2,048 | 3.694 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **3089** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
"  zXUa~
(	`G 
(?("58h
(XY=1~
(yEqe(
(E@z98
(aJ>= 
(/,zL8H
(+!,H8
(<lln(
(H1,i8
![a _C	/a~
(tuwO~
(gk7T8
({|6 
 c=MXe @
( $_.0a~
c Vr
Xa~
(W9[;8
(S*&k8^
(]
.;(
%pe ]x^
l2e {y~
(!~vj8-
(`K)j 
(X5OA~
 bHl4 
(){/V~
(&q?98)
(5WK] 
(@"6P(
75:f I
/ HwqBa~
fR .HF*a~
(nrIg(
(}jQA8#
(TbK/ 
(E+&= 
Ba .Q,la~
(8E^L8L
(6gLL~-
(AnPI8
(JHS8(
((0XR~
 Xw(#a~
(x{3\~^
*RY |m
({%[J~}
(>>e_~
(9ygk(
(ls+J~9
(% 
1(
(O`J2~i
(uXtG 
(H=O8Y
(37S1 
(@)$g8
(RH-H8-
(y&+P 
(G8sO 
(s"dP~
(U)oT(
(D7K18
(,i:c8^
(|t^E 
(Q6r^8
(I_68-
(3~ha8
(>=tE8;
(GQRV~
(p~@h8
(h'1(
(K7Hb(
(7PZ8-
(u?Des
(#]\`s
(r&t.8)
(8h=_(
(F)\/~
(/5Q;(
(4~\B 
(g@Dn~
({gWZ 
(N#*\8
(rxc>s"
(?VI18R
(8q<N(
(Hd1;~
(#pkJ~
(	.GW(
(/%BG8P
(e~7:(
(M$fc 
(@k0C8
(g"F^8
(? +T8
($hn 
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.hN1PaimOyNXIp6dT757..ctor` | `0x44987c` | 81812 | ✓ |
| `method.uNg1eF3TSSjPqhtYypp..cctor` | `0x44d070` | 51212 | ✓ |
| `method.yXpb30pL3Tcwjh1HhXV.OiqpI4n2EI` | `0x439d54` | 24680 | ✓ |
| `method.UTrCiYP2jE1GIXQLu9t.XHMueDPghOW6nQ8W4PS.hcwvMW6fUN` | `0x42264c` | 14872 | — |
| `method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.e2f1ixDE0J` | `0x41eee8` | 8804 | ✓ |
| `method._ConnectAsync_d__30.MoveNext` | `0x4176b8` | 8008 | ✓ |
| `method._ReceiveAsync_d__39.MoveNext` | `0x419f5c` | 6368 | ✓ |
| `method.yXpb30pL3Tcwjh1HhXV.dWCVF5uOef` | `0x4422dc` | 4720 | ✓ |
| `method.yXpb30pL3Tcwjh1HhXV.EyyVAeuhRV` | `0x440354` | 4580 | ✓ |
| `method.Ye9uTemalEPuYMVkbKH.sRumF7ewI8` | `0x4468d0` | 4544 | ✓ |
| `method.yXpb30pL3Tcwjh1HhXV.yNvVQargoY` | `0x44354c` | 3604 | ✓ |
| `method.yXpb30pL3Tcwjh1HhXV.Lu2VSuNjcJ` | `0x444598` | 3536 | ✓ |
| `method.yXpb30pL3Tcwjh1HhXV.absVDnG741` | `0x441538` | 3492 | ✓ |
| `method.AKgvipvBDNHeji41Dps.FDQfrovGDnp1T4mjXBD.a3IvS66KoY` | `0x427480` | 3068 | ✓ |
| `method.PowerShellAir.Services.ClientService.mFfhcWev7r` | `0x411354` | 2852 | ✓ |
| `method._SendAsync_d__37.MoveNext` | `0x41bc64` | 2620 | ✓ |
| `method.PowerShellAir.Services.NetworkManager.Receive` | `0x40dab0` | 2500 | ✓ |
| `method._DisconnectAsync_d__36.MoveNext` | `0x419650` | 2232 | ✓ |
| `method._TryReconnectAsync_d__34.MoveNext` | `0x41c6f4` | 2220 | ✓ |
| `method.PowerShellAir.Transport.TcpTransport.ReceiveAsync` | `0x4033a0` | 2160 | ✓ |
| `method.PowerShellAir.Utils.SandboxDetector..cctor` | `0x409db4` | 1980 | ✓ |
| `method.PowerShellAir.Services.MessageProtocol.TryParseDllData` | `0x40ee1c` | 1952 | ✓ |
| `method.yXpb30pL3Tcwjh1HhXV.rurpKqxQ3m` | `0x438bb0` | 1904 | ✓ |
| `method.oMcIdRldV6iqqAQBhvf.LOD9GmTEFk` | `0x42eb60` | 1672 | ✓ |
| `method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.r2x1MGcSVO` | `0x41e2b8` | 1636 | ✓ |
| `method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.kFu1xZ9gZd` | `0x42114c` | 1624 | ✓ |
| `method.aJeVfAl1ZkpbNbMwTJ8.DY89dn0eMr` | `0x4290d8` | 1500 | ✓ |
| `method.PowerShellAir.Services.AssemblyLoaderService.ExecutePlugin` | `0x413c94` | 1464 | ✓ |
| `method.PowerShellAir.Services.CryptoService.AesDecrypt` | `0x40ace8` | 1456 | ✓ |
| `method.kdg3DTm405wASabd7QK.DY89dn0eMr` | `0x448db4` | 1356 | ✓ |

### Decompiled Code Files

- [`code/method.AKgvipvBDNHeji41Dps.FDQfrovGDnp1T4mjXBD.a3IvS66KoY.c`](code/method.AKgvipvBDNHeji41Dps.FDQfrovGDnp1T4mjXBD.a3IvS66KoY.c)
- [`code/method.PowerShellAir.Services.AssemblyLoaderService.ExecutePlugin.c`](code/method.PowerShellAir.Services.AssemblyLoaderService.ExecutePlugin.c)
- [`code/method.PowerShellAir.Services.ClientService.mFfhcWev7r.c`](code/method.PowerShellAir.Services.ClientService.mFfhcWev7r.c)
- [`code/method.PowerShellAir.Services.CryptoService.AesDecrypt.c`](code/method.PowerShellAir.Services.CryptoService.AesDecrypt.c)
- [`code/method.PowerShellAir.Services.MessageProtocol.TryParseDllData.c`](code/method.PowerShellAir.Services.MessageProtocol.TryParseDllData.c)
- [`code/method.PowerShellAir.Services.NetworkManager.Receive.c`](code/method.PowerShellAir.Services.NetworkManager.Receive.c)
- [`code/method.PowerShellAir.Transport.TcpTransport.ReceiveAsync.c`](code/method.PowerShellAir.Transport.TcpTransport.ReceiveAsync.c)
- [`code/method.PowerShellAir.Utils.SandboxDetector..cctor.c`](code/method.PowerShellAir.Utils.SandboxDetector..cctor.c)
- [`code/method.Ye9uTemalEPuYMVkbKH.sRumF7ewI8.c`](code/method.Ye9uTemalEPuYMVkbKH.sRumF7ewI8.c)
- [`code/method._ConnectAsync_d__30.MoveNext.c`](code/method._ConnectAsync_d__30.MoveNext.c)
- [`code/method._DisconnectAsync_d__36.MoveNext.c`](code/method._DisconnectAsync_d__36.MoveNext.c)
- [`code/method._ReceiveAsync_d__39.MoveNext.c`](code/method._ReceiveAsync_d__39.MoveNext.c)
- [`code/method._SendAsync_d__37.MoveNext.c`](code/method._SendAsync_d__37.MoveNext.c)
- [`code/method._TryReconnectAsync_d__34.MoveNext.c`](code/method._TryReconnectAsync_d__34.MoveNext.c)
- [`code/method.aJeVfAl1ZkpbNbMwTJ8.DY89dn0eMr.c`](code/method.aJeVfAl1ZkpbNbMwTJ8.DY89dn0eMr.c)
- [`code/method.kdg3DTm405wASabd7QK.DY89dn0eMr.c`](code/method.kdg3DTm405wASabd7QK.DY89dn0eMr.c)
- [`code/method.oMcIdRldV6iqqAQBhvf.LOD9GmTEFk.c`](code/method.oMcIdRldV6iqqAQBhvf.LOD9GmTEFk.c)
- [`code/method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.e2f1ixDE0J.c`](code/method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.e2f1ixDE0J.c)
- [`code/method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.kFu1xZ9gZd.c`](code/method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.kFu1xZ9gZd.c)
- [`code/method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.r2x1MGcSVO.c`](code/method.rtCX7l7z0PAKYjVgPjj.DTGgcH725TqKU9kMkyE.r2x1MGcSVO.c)
- [`code/method.uNg1eF3TSSjPqhtYypp..cctor.c`](code/method.uNg1eF3TSSjPqhtYypp..cctor.c)
- [`code/method.yXpb30pL3Tcwjh1HhXV.EyyVAeuhRV.c`](code/method.yXpb30pL3Tcwjh1HhXV.EyyVAeuhRV.c)
- [`code/method.yXpb30pL3Tcwjh1HhXV.Lu2VSuNjcJ.c`](code/method.yXpb30pL3Tcwjh1HhXV.Lu2VSuNjcJ.c)
- [`code/method.yXpb30pL3Tcwjh1HhXV.OiqpI4n2EI.c`](code/method.yXpb30pL3Tcwjh1HhXV.OiqpI4n2EI.c)
- [`code/method.yXpb30pL3Tcwjh1HhXV.absVDnG741.c`](code/method.yXpb30pL3Tcwjh1HhXV.absVDnG741.c)
- [`code/method.yXpb30pL3Tcwjh1HhXV.dWCVF5uOef.c`](code/method.yXpb30pL3Tcwjh1HhXV.dWCVF5uOef.c)
- [`code/method.yXpb30pL3Tcwjh1HhXV.rurpKqxQ3m.c`](code/method.yXpb30pL3Tcwjh1HhXV.rurpKqxQ3m.c)
- [`code/method.yXpb30pL3Tcwjh1HhXV.yNvVQargoY.c`](code/method.yXpb30pL3Tcwjh1HhXV.yNvVQargoY.c)
- [`code/sym.hN1PaimOyNXIp6dT757..ctor.c`](code/sym.hN1PaimOyNXIp6dT757..ctor.c)

## Behavioral Analysis

Based on the analysis of the provided strings and decompiled code, this binary is a **malicious loader/backdoor**, likely designed to facilitate remote access, command execution, and modular payload delivery. The naming conventions (e.g., `PowerShellAir`) suggest it may be part of a framework used to deliver secondary stages or "plugins" to an infected host.

### Core Functionality
The primary purpose of this code is to establish a stable communication channel with a remote server and execute received commands or plugins. It acts as a "dropper" or "loader" that sits on the system to manage the lifecycle of other malicious components.

### Suspicious and Malicious Behaviors
*   **Command & Control (C2) Communication:** 
    *   The presence of `TcpTransport`, `ConnectAsync`, `SendAsync`, and `ReceiveAsync` indicates the malware establishes a TCP connection to communicate with an external server.
    *   The naming of these functions in the context of "PowerShell" suggests it might be used to tunnel commands or interact with PowerShell scripts remotely.
*   **Encryption & Obfuscation:** 
    *   The `CryptoService` and `AesDecrypt` functions indicate that communication with the C2 server is encrypted using AES, making it difficult for network security tools to inspect the traffic.
    *   Internal strings are obfuscated (`ObfuscatedString`, `StringEncryption`), which is used to hide malicious URLs, IP addresses, and file paths from static analysis.
*   **Dynamic Code Execution (Plug-in Architecture):** 
    *   The `AssemblyLoaderService` and its method `ExecutePlugin` are highly suspicious. This indicates the malware can download and execute additional "plugins" or modules in memory. This is a common technique to stay "lightweight" while providing various features (e.g., keylogging, file theft) on demand.
*   **Anti-Analysis / Evasion:** 
    *   The presence of `SandboxDetector` indicates the malware checks if it is being run in an analysis environment (like a sandbox or VM). If detected, the malware may stop executing or change its behavior to evade detection by security researchers.
*   **Masquerading:** 
    *   One of the strings is `SysUpdateSvc`. This is a common tactic where the malware names itself or creates a service with a name mimicking a legitimate "System Update Service" to blend in with standard Windows processes.

### Notable Techniques and Patterns
*   **Heavy Obfuscation:** The decompiled code contains many instances of "Bad instruction" warnings and "Control flow encountered bad data." This suggests the use of **Control Flow Flattening** or other advanced obfuscators (like those used in .NET environments) to hinder reverse engineering.
*   **Modular Design:** The structure suggests a sophisticated multi-stage attack. Rather than performing all malicious actions at once, it acts as a "loader" that pulls down specific modules (via `AssemblyLoaderService`) only when needed.
*   **Network Resilience:** The inclusion of `TryReconnectAsync` and `HeartbeatService` indicates the malware is designed to maintain a persistent connection with the C2 server despite network instability or firewall interference.

### Summary for Incident Response
This sample is highly likely part of a **Remote Access Trojan (RAT)** or a sophisticated **malware loader**. It uses encrypted communication, dynamic assembly loading to execute secondary payloads, and anti-analysis checks to remain persistent on an infected host. It should be treated as a high-priority threat capable of delivering further infections or exfiltrating data.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1071 | Application Layer Protocol | The use of `TcpTransport`, `ConnectAsync`, and references to PowerShell indicates the malware uses standard network protocols for C2 communication. |
| T1027 | Obfuscated Executables or Scripts | The presence of `CryptoService` (AES), `ObfuscatedString`, and "Control Flow Flattening" is used to hide malicious code from static analysis. |
| T1620 | Reflective Loader | The `AssemblyLoaderService` is used to load and execute additional modules in memory, allowing the malware to remain "lightweight" while performing multi-functional tasks. |
| T1497 | Virtualization/Sandbox Detection | The inclusion of a `SandboxDetector` indicates an active attempt to identify and evade analysis environments like VMs or sandboxes. |
| T1036 | Masquerading | The use of the name `SysUpdateSvc` is intended to blend in with legitimate system processes to evade detection by users or administrators. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (Note: The analysis indicates that these are likely obfuscated/encrypted within the binary using `StringEncryption`.)

**File paths / Registry keys**
*   `SysUpdateSvc.exe` (Identified as a masquerading filename for system services)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   `b530839b-35a3-4cd2-82a0-9374a912b692` (GUID - Identified as a unique identifier within the code structure)

**Other artifacts**
*   **C2/Communication Patterns:**
    *   `TcpTransport`
    *   `HeartbeatService`
    *   `TryReconnectAsync`
    *   `ConnectAsync`, `SendAsync`, `ReceiveAsync` (Standard .NET networking methods utilized for C2 communication)
*   **Malware Components/Modules:**
    *   `PowerShellAir` (Project/Module name)
    *   `AssemblyLoaderService` (Used for dynamic plugin execution)
    *   `CryptoService` / `AesDecrypt` (Encryption routines)
*   **Evasion & Obfuscation:**
    *   `SandboxDetector` (Anti-analysis mechanism)
    *   `ObfuscatedString` / `StringEncryption` (Techniques used to hide malicious strings)

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader, backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Modular Execution & Reflective Loading:** The presence of `AssemblyLoaderService` and `ExecutePlugin` indicates a modular architecture designed to download and execute additional payloads (plugins) in memory, which is the primary characteristic of a sophisticated loader/backdoor.
*   **Advanced Evasion Techniques:** The use of `SandboxDetector`, `Control Flow Flattening` (evidenced by "bad instruction" warnings), and string encryption shows a high level of intentional effort to bypass automated security analysis and manual reverse engineering.
*   **Persistence & Masquerading:** The naming convention `SysUpdateSvc` is a classic masquerading technique used to blend in with legitimate system processes, while the inclusion of `HeartbeatService` and `TryReconnectAsync` ensures a stable, persistent connection to its Command & Control (C2) server.
