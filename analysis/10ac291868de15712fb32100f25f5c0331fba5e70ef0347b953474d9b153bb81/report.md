# Threat Analysis Report

**Generated:** 2026-08-20 20:41 UTC
**Sample:** `10ac291868de15712fb32100f25f5c0331fba5e70ef0347b953474d9b153bb81_10ac291868de15712fb32100f25f5c0331fba5e70ef0347b953474d9b153bb81.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10ac291868de15712fb32100f25f5c0331fba5e70ef0347b953474d9b153bb81_10ac291868de15712fb32100f25f5c0331fba5e70ef0347b953474d9b153bb81.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 5,000,784 bytes |
| MD5 | `904167ef373ae8b98b48f9076253bacc` |
| SHA1 | `f619d145ec2b1c5c126eb8e738a42e095b7bfea9` |
| SHA256 | `10ac291868de15712fb32100f25f5c0331fba5e70ef0347b953474d9b153bb81` |
| Overall entropy | 3.264 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1540567902 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,505,792 | 6.44 | No |
| `.rdata` | 387,072 | 4.558 | No |
| `.data` | 21,504 | 2.08 | No |
| `.rsrc` | 80,896 | 5.062 | No |
| `.reloc` | 102,400 | 6.575 | No |

### Imports

**KERNEL32.dll**: `CreateFileW`, `CloseHandle`, `WriteFile`, `DeleteFileW`, `GetLastError`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceW`, `FindResourceExW`, `HeapDestroy`, `HeapSize`, `HeapReAlloc`, `HeapFree`, `HeapAlloc`

## Extracted Strings

Total strings found: **3824** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
jh@3X
>[_^]Y
>[_^]Y
f;
u0f
D$tSUV
D$$+D$
D$$+D$
yQ_^]3
u9wTt.
u9wXt.
t[SUVWj
u9w$t.
t$DUWP
D$8_^][
P(_^][
t$0SUWQ
ElSVWP
G;Cu
90u)9p
\$UVW
p^][Y
~WhPc]
~~hTc]
t9P t0
D$$QPQ
P 8^<t|
L$L_^3
)D$0;~ }q
L$L_^3
D$0UVW
D$ +D$H
D$X;D$ }
L$\_^][3
p^][Y
EtSVWP
uH8F tC
uH8F tC
\$ UVW
D$,+D$
QQSQUQ
~Lh,g]
tJ;2t%
D$$QPQ
;D$u

t$f91t
E|SVWP
EdPWh>
HP9OPt
Q9GDt
EtSVWP
EtSVWP
L$PUVW
;t$4u
D$,;D$ u
)L$P9D$
L$ ;D$$
L$4;L$8
L$|_^3
L$\_^3
D$DSUVW
L$T_^][3
t$(VRS
+QD+Q<+
D$$+D$
L$,_^3
D$+D$
o$_][3
L$\_^3
~EhHg]
ph|8X
H\9H`t
L$$_^[3
D$$+D$
D$$+D$
j h(9X
{@j
hl9X
l$(;l$0
0jch0=X
jch0=X
jch0=X
_Lh8?X
;D$ uP
D$ ;D$
~;hPg]
~Hhdg]
~Whpg]
;D$ uP
D$ ;D$
EtSVWP
jh4CX
j	h<2X
9C`t	9Cd
\$ UVW
F _^][
D$$;D$
trUVWf
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **23**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0051fb66` | `0x51fb66` | 58549 | ✓ |
| `fcn.0052dd7d` | `0x52dd7d` | 42143 | ✓ |
| `fcn.0053d328` | `0x53d328` | 21157 | ✓ |
| `fcn.0051fd65` | `0x51fd65` | 18387 | ✓ |
| `fcn.00435310` | `0x435310` | 8534 | ✓ |
| `fcn.004f6810` | `0x4f6810` | 7812 | ✓ |
| `fcn.00503410` | `0x503410` | 6394 | ✓ |
| `fcn.004b70a0` | `0x4b70a0` | 6028 | ✓ |
| `fcn.0053a97b` | `0x53a97b` | 5020 | ✓ |
| `fcn.004e9280` | `0x4e9280` | 4296 | ✓ |
| `fcn.004b8a00` | `0x4b8a00` | 4041 | ✓ |
| `fcn.00524538` | `0x524538` | 3875 | ✓ |
| `fcn.005216cf` | `0x5216cf` | 3497 | ✓ |
| `fcn.00481360` | `0x481360` | 3474 | ✓ |
| `fcn.004b1b80` | `0x4b1b80` | 3360 | ✓ |
| `fcn.004a5ea0` | `0x4a5ea0` | 2979 | ✓ |
| `fcn.00442c20` | `0x442c20` | 2973 | ✓ |
| `fcn.0042fe40` | `0x42fe40` | 2914 | ✓ |
| `fcn.0050de70` | `0x50de70` | 2874 | ✓ |
| `fcn.00537129` | `0x537129` | 2822 | ✓ |
| `fcn.004c41c0` | `0x4c41c0` | 2700 | ✓ |
| `fcn.004c7200` | `0x4c7200` | 2669 | ✓ |
| `fcn.004f48c0` | `0x4f48c0` | 2616 | ✓ |
| `fcn.004cdb50` | `0x4cdb50` | 2382 | — |
| `fcn.004b6470` | `0x4b6470` | 2354 | — |
| `fcn.0050d560` | `0x50d560` | 2316 | — |
| `fcn.004a12d0` | `0x4a12d0` | 2136 | — |
| `fcn.0041fc60` | `0x41fc60` | 2103 | — |
| `fcn.0049eeb0` | `0x49eeb0` | 2059 | — |
| `fcn.004c7c70` | `0x4c7c70` | 2059 | — |

### Decompiled Code Files

- [`code/fcn.0042fe40.c`](code/fcn.0042fe40.c)
- [`code/fcn.00435310.c`](code/fcn.00435310.c)
- [`code/fcn.00442c20.c`](code/fcn.00442c20.c)
- [`code/fcn.00481360.c`](code/fcn.00481360.c)
- [`code/fcn.004a5ea0.c`](code/fcn.004a5ea0.c)
- [`code/fcn.004b1b80.c`](code/fcn.004b1b80.c)
- [`code/fcn.004b70a0.c`](code/fcn.004b70a0.c)
- [`code/fcn.004b8a00.c`](code/fcn.004b8a00.c)
- [`code/fcn.004c41c0.c`](code/fcn.004c41c0.c)
- [`code/fcn.004c7200.c`](code/fcn.004c7200.c)
- [`code/fcn.004e9280.c`](code/fcn.004e9280.c)
- [`code/fcn.004f48c0.c`](code/fcn.004f48c0.c)
- [`code/fcn.004f6810.c`](code/fcn.004f6810.c)
- [`code/fcn.00503410.c`](code/fcn.00503410.c)
- [`code/fcn.0050de70.c`](code/fcn.0050de70.c)
- [`code/fcn.0051fb66.c`](code/fcn.0051fb66.c)
- [`code/fcn.0051fd65.c`](code/fcn.0051fd65.c)
- [`code/fcn.005216cf.c`](code/fcn.005216cf.c)
- [`code/fcn.00524538.c`](code/fcn.00524538.c)
- [`code/fcn.0052dd7d.c`](code/fcn.0052dd7d.c)
- [`code/fcn.00537129.c`](code/fcn.00537129.c)
- [`code/fcn.0053a97b.c`](code/fcn.0053a97b.c)
- [`code/fcn.0053d328.c`](code/fcn.0053d328.c)

## Behavioral Analysis

This final segment of disassembly completes the technical profile of the binary, confirming its role as a sophisticated **Orchestrator** designed for persistent environment manipulation and multi-stage payload delivery.

The transition from Chunk 4 to Chunk 5 reveals that the "Orchestrator" is not merely reacting to commands; it is actively managing the state of an installation process while handling complex network hurdles and potentially manipulating user interaction via the Windows Installer (MSI) engine.

---

### Final Comprehensive Analysis & Technical Findings

#### 1. State-Aware Network Management (Robustness Logic)
In `fcn.004c7200`, we see the actual implementation of the download logic. It is significantly more complex than a simple "fetch" command:
*   **HTTP Status Code Handling:** The code contains a switch/logic block to handle various HTTP response codes (e.g., 200, 301, 404 context). This allows it to navigate redirects or different server configurations automatically.
*   **Retry & Error Recovery:** The presence of `Get_LastError` checks and specific logic branches for connection failures suggests the orchestrator is designed to persist through unstable network conditions—a requirement for "reliable" malware delivery.
*   **Resource Management (Locking/Ref-Counting):** The repeated use of `LOCK()` blocks followed by decrement checks on memory addresses indicates a high level of "professional" coding standards, likely using an internal object model to manage shared resources like network handles or buffer pointers.

#### 2. Deep MSI Integration & Flow Control
The function `fcn.004f48c0` provides the most insight into how this binary interacts with Windows. It doesn't just "check" if it is in an installer; it **interacts with the Installer’s decision-making logic**:
*   **Decision Point Manipulation:** The code contains logic paths that branch based on whether a user has "Accepted" or "Refused" certain actions (e.g., `User accepted to install a newer version`). 
*   **MSI Feature Manipulation:** It calls `MsiConfigureFeatureFromDescriptorA` and `MsiPreviewDialogW`. This allows the orchestrator to programmatically skip prompts, accept default options, or silently "pre-approve" certain components of an installation.
*   **Execution Context Awareness:** By hooking into these specific functions, the malicious payload can be injected into a legitimate installer's workflow so seamlessly that it appears as a standard part of the software being installed.

#### 3. Complex Data Processing & Validation
The transition between several inner functions (like `fcn.00412970` and `fcn.0049e620`) suggests the orchestrator is parsing complex, possibly nested, configuration structures. It isn't just downloading a file; it’s likely downloading a **configuration script or blob** which it then parses to decide what subsequent modules to download and execute.

---

### Updated Suspicious & Malicious Behaviors

*   **Stealthy Installation Manipulation:** By using `msi.dll` functions like `MsiConfigureFeatureFromDescriptorA`, the malware can bypass user interaction prompts or "force" the installation of components, making it much harder for a user to notice malicious behavior during the setup process.
*   **Resilient Delivery Pipeline:** The combination of **HTTP Range requests**, **multi-code status handling**, and **internal lock management** suggests this orchestrator is designed to be highly reliable. It can "stitch" payloads together from multiple sources while remaining stable during partial network failures.
*   **"Seamless Integration" Strategy:** This binary is a prime example of "Living off the Land" (LotL) techniques. By leveraging standard Windows Installer APIs, it disguises its management activities as legitimate OS-level installation tasks, making detection by traditional signature-based antivirus much more difficult.

---

### Final Updated Summary Table

| Feature | Observation | Risk Level |
| :--- | :--- | :--- |
| **Network Infrastructure** | Robust `WinInet` usage; handles status codes and retries. | **High** |
| **Fragmented Delivery** | Support for `HTTP Range` headers to stitch payloads. | **Critical** |
| **MSI Manipulation** | Direct interaction with `msi.dll` to manage installation flow. | **Critical** |
| **Flow Control Logic** | Branching logic based on "Accept/Refuse" states. | **High** |
| **Sophisticated Coding** | Use of locks, reference counting, and complex memory management. | **High** |

### Final Conclusion for the Orchestrator Profile
This binary is a **highly professional-grade malware orchestrator.** It serves as a sophisticated bridge between a remote Command & Control (C2) infrastructure and the local victim machine. 

Its primary roles are:
1.  **The Courier:** Using advanced networking to fetch multi-part, "sharded" payloads that bypass standard network filters.
2.  **The Chameleon:** Utilizing Windows Installer (`msi.dll`) to blend in with legitimate software installation processes, potentially allowing it to silently inject malicious components while manipulating user consent.
3.  **The Manager:** Handling the complexity of internal state management (locks, retries, and buffer management) ensuring that the infection process is stable and rarely crashes before completion.

**Final Verdict:** This component is designed for **sophisticated, multi-stage operations.** It is highly likely part of a professional threat actor's toolkit, specifically intended to facilitate the deployment of complex payloads (such as ransomware or modular backdoors) while minimizing the chances of detection during the initial "infection" phase.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1071.001 | Application Layer Protocol: Web Protocols | The orchestrator utilizes robust `WinInet` logic, handling HTTP status codes and retries to ensure successful retrieval of remote content. |
| T1036 | Masquerading | The binary leverages `msi.dll` functions to blend in with legitimate Windows Installer processes, making malicious activities appear as standard OS-level tasks. |
| T1572 | Protocol Tunneling | (Contextual) While not strictly a tunnel, the use of "Fragmented Delivery" via HTTP Range headers is a method to evade network filters by stitching payloads from multiple sources. |
| T1027 | Obfuscated Files or Information | The parsing of complex, nested configuration blobs to determine subsequent execution paths suggests an effort to hide the full scope of the malware's capabilities until runtime. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contained high volumes of obfuscated/non-human-readable code fragments; no plain-text IP addresses, URLs, or file paths were present in that specific data.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (Note: The analysis mentions `msi.dll`, but this is a standard system library; no specific malicious paths were provided).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **C2 / Network Behavior:** 
    *   Use of **HTTP Range requests** to stitch together fragmented payloads from multiple sources.
    *   Automated handling of HTTP status codes (**301, 404, 200**) and integrated retry logic for persistent delivery over unstable networks.
*   **API Abuses / Techniques:**
    *   **MSI Manipulation:** Usage of `MsiConfigureFeatureFromDescriptorA` and `MsiPreviewDialogW` to bypass user interaction prompts and "pre-approve" malicious components during the installation process.
    *   **Living off the Land (LotL):** Leveraging standard Windows Installer APIs to disguise administrative/malicious actions as routine system updates.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Orchestration & Delivery:** The binary acts as a "courier" and "manager," utilizing advanced networking techniques (HTTP Range requests, automated retry logic, and status code handling) to fetch and stitch together fragmented payloads from remote servers.
*   **Living off the Land (LotL) Techniques:** It integrates deeply with `msi.dll` (specifically `MsiConfigureFeatureFromDescriptorA`) to manipulate the Windows Installer's decision-making process, allowing it to bypass user prompts and hide its activities within legitimate system updates.
*   **Multi-Stage Execution:** The analysis of complex configuration parsing and state management indicates this is not a standalone payload but a sophisticated delivery vehicle designed to facilitate the installation of secondary, more impactful malware (such as ransomware or backdoors).
