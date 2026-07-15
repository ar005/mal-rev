# Threat Analysis Report

**Generated:** 2026-07-12 08:00 UTC
**Sample:** `04d8f7258ab93a2ec9c18e14636b5d0d1fb6fa0ac7c82b29973d213473c57602_04d8f7258ab93a2ec9c18e14636b5d0d1fb6fa0ac7c82b29973d213473c57602.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04d8f7258ab93a2ec9c18e14636b5d0d1fb6fa0ac7c82b29973d213473c57602_04d8f7258ab93a2ec9c18e14636b5d0d1fb6fa0ac7c82b29973d213473c57602.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 4 sections |
| Size | 18,432 bytes |
| MD5 | `67661bdf4e4f3cabd300e776f785358f` |
| SHA1 | `245695b29409d751cf09e38a47ab54b75bfad7de` |
| SHA256 | `04d8f7258ab93a2ec9c18e14636b5d0d1fb6fa0ac7c82b29973d213473c57602` |
| Overall entropy | 6.021 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775162118 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 10,752 | 6.109 | No |
| `.rdata` | 5,120 | 4.9 | No |
| `.data` | 512 | 1.719 | No |
| `.reloc` | 1,024 | 6.23 | No |

### Imports

**KERNEL32.dll**: `CreateProcessA`, `CopyFileA`, `GetComputerNameA`, `CreateFileA`, `WriteFile`, `GetTempPathA`, `TerminateProcess`, `OpenProcess`, `CreateToolhelp32Snapshot`, `Process32First`, `Process32Next`, `CreateDirectoryA`, `GetThreadContext`, `SetThreadContext`, `VirtualAlloc`
**ADVAPI32.dll**: `CryptReleaseContext`, `RegCreateKeyExA`, `RegDeleteValueA`, `RegSetValueExA`, `CryptGenRandom`, `CryptAcquireContextA`, `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`, `RegDeleteKeyA`
**WINHTTP.dll**: `WinHttpReadData`, `WinHttpSetOption`, `WinHttpOpenRequest`, `WinHttpConnect`, `WinHttpReceiveResponse`, `WinHttpCrackUrl`, `WinHttpOpen`, `WinHttpCloseHandle`, `WinHttpSendRequest`
**SHELL32.dll**: `ord_680`, `SHGetFolderPathA`
**WS2_32.dll**: `bind`, `ioctlsocket`, `htons`, `ntohs`, `recvfrom`, `sendto`, `socket`, `WSAStartup`, `inet_pton`, `inet_ntop`, `accept`, `closesocket`, `connect`, `listen`, `recv`

## Extracted Strings

Total strings found: **259** (showing first 100)

```
!This program cannot be run in DOS mode.
$
(Rich]S
`.rdata
@.data
.reloc
PWWhxA@
S<"u;F3
l$`<"t"
\$\<,t-
$~"j
]
jPhhC@
D$<hE@
D$<h E@
D$<h,E@
D$<h8E@
D$<hLE@
D$pPhXE@
D$`Ph\E@
D$\hdE@
D$<hpE@
D$pPhXE@
D$`Ph\E@
uVhE@
uEh8E@
< tPF
tKVWjD^V3
PWWWWWW
WUUUUh
PPPPPPV
SUVWh(F@
D$$hPF@
0VhtF@
YY95Pi@
UVjD^V3
D$0PUUj
T$(f;F
D$,^t%
f;D$,u
D$0PSSh
9\$t
D$tPSSh
DH.AF
D$$j
PS
QQPh46@
PPWh46@
D$$SVPh
u
9-Xi@
Windows
SOFTWARE\Microsoft\Windows NT\CurrentVersion
ProductName
Global\x47_Micro_Mutex
svchost.exe
\svchost.exe
cmd.exe /c ping 127.0.0.1 -n 3 > nul & del "
\Microsoft\Windows
\wininit.exe
Software\Microsoft\Windows\CurrentVersion\Run
Windows Initializer
micro_unknown
0123456789ABCDEF
micro_
{"auth":"
x47c_K9$mP2vL8nQ
","type":"command_result","bot_id":"
","command":"
","message":"
","success":true}
","type":"register","bot_id":"
","version":"3.2","os":"
","peers":
,"socks5_port":
"commands":[
hybrid_execute
command
Executed and broadcasted via P2P
download_execute
dl/exc
uninstall
update
update_url
p2p_connect
BOOTSTRAP
p2p_manual_ping
p2p_status
botkiller_scan
botkiller_clean
update.exe
dl/exec
{"type":"pong","id":"
broadcast_command
{"type":"broadcast_command","command":"
","id":"
{"type":"ping","id":"
"neighbors":[
"ip":"
njrat.exe
darkcomet.exe
nanocore.exe
quasar.exe
remcos.exe
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004017b6` | `0x4017b6` | 1809 | ✓ |
| `fcn.00403338` | `0x403338` | 764 | ✓ |
| `fcn.00402d38` | `0x402d38` | 728 | ✓ |
| `fcn.00401059` | `0x401059` | 676 | ✓ |
| `fcn.00402b3f` | `0x402b3f` | 505 | ✓ |
| `fcn.0040311d` | `0x40311d` | 459 | ✓ |
| `fcn.00401540` | `0x401540` | 450 | ✓ |
| `fcn.004021dc` | `0x4021dc` | 450 | ✓ |
| `fcn.00401ec7` | `0x401ec7` | 442 | ✓ |
| `fcn.00401334` | `0x401334` | 362 | ✓ |
| `fcn.00402677` | `0x402677` | 327 | ✓ |
| `fcn.004011a9` | `0x4011a9` | 306 | ✓ |
| `fcn.00403010` | `0x403010` | 269 | ✓ |
| `fcn.00402a4a` | `0x402a4a` | 245 | ✓ |
| `fcn.0040239e` | `0x40239e` | 218 | ✓ |
| `fcn.00402081` | `0x402081` | 204 | ✓ |
| `fcn.004025b9` | `0x4025b9` | 184 | ✓ |
| `fcn.00401103` | `0x401103` | 166 | ✓ |
| `fcn.00402824` | `0x402824` | 166 | ✓ |
| `fcn.0040149e` | `0x40149e` | 162 | ✓ |
| `fcn.0040214d` | `0x40214d` | 143 | ✓ |
| `fcn.0040248c` | `0x40248c` | 140 | ✓ |
| `fcn.004028f7` | `0x4028f7` | 137 | ✓ |
| `fcn.00401730` | `0x401730` | 134 | ✓ |
| `fcn.00402980` | `0x402980` | 123 | ✓ |
| `fcn.004027be` | `0x4027be` | 102 | ✓ |
| `fcn.00402568` | `0x402568` | 81 | ✓ |
| `fcn.004032e8` | `0x4032e8` | 80 | ✓ |
| `fcn.00402518` | `0x402518` | 80 | ✓ |
| `fcn.004029fb` | `0x4029fb` | 79 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401059.c`](code/fcn.00401059.c)
- [`code/fcn.00401103.c`](code/fcn.00401103.c)
- [`code/fcn.004011a9.c`](code/fcn.004011a9.c)
- [`code/fcn.00401334.c`](code/fcn.00401334.c)
- [`code/fcn.0040149e.c`](code/fcn.0040149e.c)
- [`code/fcn.00401540.c`](code/fcn.00401540.c)
- [`code/fcn.00401730.c`](code/fcn.00401730.c)
- [`code/fcn.004017b6.c`](code/fcn.004017b6.c)
- [`code/fcn.00401ec7.c`](code/fcn.00401ec7.c)
- [`code/fcn.00402081.c`](code/fcn.00402081.c)
- [`code/fcn.0040214d.c`](code/fcn.0040214d.c)
- [`code/fcn.004021dc.c`](code/fcn.004021dc.c)
- [`code/fcn.0040239e.c`](code/fcn.0040239e.c)
- [`code/fcn.0040248c.c`](code/fcn.0040248c.c)
- [`code/fcn.00402518.c`](code/fcn.00402518.c)
- [`code/fcn.00402568.c`](code/fcn.00402568.c)
- [`code/fcn.004025b9.c`](code/fcn.004025b9.c)
- [`code/fcn.00402677.c`](code/fcn.00402677.c)
- [`code/fcn.004027be.c`](code/fcn.004027be.c)
- [`code/fcn.00402824.c`](code/fcn.00402824.c)
- [`code/fcn.004028f7.c`](code/fcn.004028f7.c)
- [`code/fcn.00402980.c`](code/fcn.00402980.c)
- [`code/fcn.004029fb.c`](code/fcn.004029fb.c)
- [`code/fcn.00402a4a.c`](code/fcn.00402a4a.c)
- [`code/fcn.00402b3f.c`](code/fcn.00402b3f.c)
- [`code/fcn.00402d38.c`](code/fcn.00402d38.c)
- [`code/fcn.00403010.c`](code/fcn.00403010.c)
- [`code/fcn.0040311d.c`](code/fcn.0040311d.c)
- [`code/fcn.004032e8.c`](code/fcn.004032e8.c)
- [`code/fcn.00403338.c`](code/fcn.00403338.c)

## Behavioral Analysis

### Overview
The binary is a sophisticated piece of malware, specifically a **Remote Access Trojan (RAT)** or a high-end **Backdoor**. It is designed to establish persistence on a Windows system, communicate with a Command and Control (C2) server, bypass local security measures, and maintain communication via peer-to-peer (P2P) infrastructure.

### Core Functionality
*   **Command & Control (C2) Communication:** The malware uses the `WinHttp` library to send JSON-formatted data to a C2 server (`ult.wraithbot.net`). It sends information including an authentication key, "boot ID," system version, and available proxy ports.
*   **Persistence Mechanisms:** The code manipulates several Windows Registry keys (e.g., `Software\Microsoft\Windows\CurrentVersion\Run`) to ensure it starts automatically upon login under the guise of a legitimate-sounding name ("Windows Initializer").
*   **Process Hollowing / Injection:** The routine `fcn.00402d38` is a classic implementation of process hollowing. It spawns a child process (potentially a system executable), allocates memory in that child, overwrites it with its own code/payload using `WriteProcessMemory`, and then resumes the execution thread to "hide" inside the legitimate process.
*   **Firewall Manipulation:** The malware executes `netsh` commands to automatically create firewall exceptions for itself (labeled as "Windows Initializer") and opens specific ports for P2P communication (e.g., UDP 4711).

### Suspicious and Malicious Behaviors
*   **Anti-Analysis & Anti-Tampering:**
    *   **Process Scanning:** The function `fcn.00402b3f` uses the ToolHelp API to take a snapshot of all running processes. It checks for names associated with security tools or known threats (listed in the strings, such as "antivirus" related terms or other RATs).
    *   **Active Termination:** If it identifies any of these "threats," it attempts to terminate them using `TerminateProcess`.
    *   **Evasive Command Execution:** It uses obfuscated command strings containing a "dummy" operation (like a pinging the local machine) followed by an `&` operator to hide its real actions, such as deleting files or setting registry keys.
*   **System Hijacking:**
    *   The malware modifies system file associations for `ms-settings` and `mscfile`. This is a common technique to hijack Windows Settings menus so that when a user tries to open settings, the malicious executable is launched instead.
*   **Stealthy Persistence:** It creates and copies files into systemic paths (e.g., masquerading as `wininit.exe`) or other system directories to blend in with legitimate OS files.

### Notable Techniques & Patterns
*   **P2P Infrastructure:** The presence of "p2p" keywords, a list of peer IPs/identities, and the creation of specific UDP firewall rules suggest it uses P2P (Peer-to-Peer) networking to remain active even if its primary C2 domain is blocked.
*   **Mutex Protection:** It creates a global mutex (`Global\x47_Micro_Mutex`) to ensure only one instance of the malware is running at any given time, which helps evade some basic detection techniques and prevents resource conflicts.
*   **Data Exfiltration (via WinHttp):** The usage of `WinHttp` with custom JSON headers indicates a sophisticated backend, likely designed to blend in with legitimate web traffic.
*   **Execution via System Tools:** By invoking `cmd.exe`, `netsh.exe`, and `powershell`-like logic for its actions, the malware attempts to hide its activity behind trusted system binaries.

### Summary Table of Indicators
| Category | Observed Evidence |
| :--- | :--- |
| **Persistence** | Registry Run Key ("Windows Initializer"), hijacking `.ms-settings` / `.mscfile` paths. |
| **Evasion** | Process hollowing (via `WriteProcessMemory`), termination of "threat" processes, and firewall rule modification. |
| **Network** | WinHttp usage for C2; P2P network logic via UDP 4711. |
| **Anti-Analysis** | Toolhelp32 search for other malware/security tools; use of `ping` to hide command execution. |

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1071.001** | Application Layer Protocol: Web Protocols | The malware utilizes the `WinHttp` library and JSON formatting to communicate with its C2 server over standard web protocols. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | The malware modifies the "Run" registry key to ensure it executes automatically upon user login under a deceptive name. |
| **T1055.012** | Process Injection: Process Hollowing | The malware uses `WriteProcessMemory` to inject its payload into a spawned child process to hide its activities within a legitimate executable. |
| **T1562.001** | Impair Defenses: Disable or Modify Tools | The malware uses `netsh` to modify firewall rules and actively terminates security-related processes to bypass local protections. |
| **T1027** | Obfuscated Files or Information | Use of "dummy" commands (like ping) followed by an `&` operator is a technique to mask the true intent of command execution from security logs. |
| **T1543** | Create or Modify System Binary | The malware places copies of itself in system directories and masquerades as legitimate files like `wininit.exe`. |
| **T1059.003** | Command and Scripting Interpreter: Windows Command Shell | The malware invokes `cmd.exe` to execute network configurations and other system commands to blend in with normal administrative activity. |
| **T1564** | Spoofing Configuration File | Modifying registry keys for `ms-settings` and `mscfile` redirects system configuration prompts to the malicious executable. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `ult.wraithbot.net` (C2 Domain)

**File paths / Registry keys**
*   `Software\Microsoft\Windows\CurrentVersion\Run` (Persistence Key)
*   `Software\Classes\ms-settings\Shell\Open\command` (Hijacked Path)
*   `Software\Classes\mscfile\shell\open\command` (Hijacked Path)

**Mutex names / Named pipes**
*   `Global\x47_Micro_Mutex`

**Hashes**
*   *(None identified in provided strings)*

**Other artifacts**
*   **C2 Communication Pattern:** JSON-formatted data transmitted via `WinHttp` containing fields such as `auth`, `bot_id`, `type`, and `socks5_port`.
*   **P2P Networking:** Use of UDP port **4711** for peer-to-peer communication.
*   **Command Obfuscation:** Use of the "ping &" tactic (e.g., `cmd.exe /c ping 127.0.0.1 -n 3 > nul & ...`) to mask malicious commands.
*   **Firewall Rules:** Creation of specific firewall rules named `"Windows Initializer"` and `"P2P_UDP_4711"`.
*   **Process Hollowing:** Use of `WriteProcessMemory` and `NtUnmapViewOfSection` to inject code into system processes.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: RAT (Remote Access Trojan) / Backdoor
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Persistence & Evasion:** The malware employs advanced techniques including process hollowing (`WriteProcessMemory`), hijacking system shortcuts (`ms-settings` and `mscfile`), and the use of "ping" commands to mask malicious activities in logs, which are characteristic of a high-end RAT.
*   **Robust Networking Infrastructure:** The integration of both standard web communication (WinHttp with JSON payloads) and peer-to-peer (P2P) networking via UDP 4711 indicates a sophisticated design intended to maintain persistent connections even if primary C2 domains are blocked.
*   **System Manipulation & Defense Evasion:** The use of `netsh` to create firewall exceptions, the active termination of security processes, and the creation of specific mutexes for instance control confirm its role as a stable backdoor meant for long-term unauthorized access.
