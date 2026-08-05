# Threat Analysis Report

**Generated:** 2026-08-04 20:23 UTC
**Sample:** `0d199e35b32b51874dae687b2ccf65e3d8a98411db6f59eda2f58cd9a133da5c_0d199e35b32b51874dae687b2ccf65e3d8a98411db6f59eda2f58cd9a133da5c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d199e35b32b51874dae687b2ccf65e3d8a98411db6f59eda2f58cd9a133da5c_0d199e35b32b51874dae687b2ccf65e3d8a98411db6f59eda2f58cd9a133da5c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 16,384 bytes |
| MD5 | `d8b84d5050bfacc7a31399d09b35f533` |
| SHA1 | `81748da4ca73678f9712c7eebd77fca1ee9163a0` |
| SHA256 | `0d199e35b32b51874dae687b2ccf65e3d8a98411db6f59eda2f58cd9a133da5c` |
| Overall entropy | 6.04 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769906432 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 11,264 | 6.282 | No |
| `.rdata` | 2,560 | 5.459 | No |
| `.data` | 512 | 0.041 | No |
| `.pdata` | 512 | 3.907 | No |
| `.rsrc` | 512 | 4.702 | No |

## Extracted Strings

Total strings found: **86** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
<\t	</t
UAVAWH
@@8}@t
|$ ATAVAWH
A_A^A\
@8)t'H
@8lpu
L$ UVWATAVH
D8D$pt
A^A\_^]
@SVAWH
<[uL;
,0<	w
:[ueE3
|$ AVH
"<;<;0!{199
 &0'fg{199
=!!%ozza`{d`e{del{g`e
a`{d`e{del{g`e
:;!0;!x
,%0ou4%%9<64!<:;z?&:;X_
z4%<z7:!z'02<&!0'
.w7:!
<1wowp&wyw=:&!;480wowp&wyw:&wow
<;1:"&w(
z4%<z7:!z6:884;1&j7:!
<1hp&
6:884;1&
z4%<z7:!z'0& 9!
.w7:!
<1wowp&wyw6:884;1
<1wowp&wyw'0& 9!wowp&w(
681{0-0uz6u
:!zd{e
:3!"4'0	
<6':&:3!	
<;1:"&	
 ''0;!
0'&<:;	
<;1:"&
&&<&!4;!
,&!08&zg{e
42<6oue-
41#4%<fg{199
 '98:;{199
[DEBUG] Kernel32 functions resolved

[DEBUG] Advapi32 functions resolved

[DEBUG] WinInet functions resolved

[DEBUG] User32 functions resolved

BOT-%04X%04X-%04X-%04X
[DEBUG] HttpSendRequestA failed. Error: %d

[DEBUG] execute_shell failed. Error: %d

Error: Failed to create file %s
Error: Failed to write file
File uploaded successfully: %s (%d bytes)
Error: File not found: %s
Error: File too large or empty (max 4KB)
Error: Memory allocation failed
FILE:%s|DATA:%s|SIZE:%d
Error: Failed to read file
Error: Cannot get current directory
Error: Cannot access directory: %s
Directory: %s


[DIR]  %s

[FILE] %s (%d bytes)

Error: Interval must be between 1000 and 60000 ms
Check interval set to %d ms
Error: No command specified
Error: File path and data required
Error: File path required
Error: Unknown command code %d
{"bot_id":"
","command_id":"
","result":"
[DEBUG] Bot _start entered

.text$mn
.rdata
.rdata$voltmd
.rdata$zzzdbg
.xdata
.pdata
.rsrc$01
.rsrc$02
p`P
<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<assembly xmlns='urn:schemas-microsoft-com:asm.v1' manifestVersion='1.0'>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level='asInvoker' uiAccess='false' />
      </requestedPrivileges>
    </security>
  </trustInfo>
</assembly>

```

## Disassembly Overview

Functions analyzed: **16** | Decompiled to C: **16**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400010f0` | `0x1400010f0` | 1945 | ✓ |
| `fcn.1400023a0` | `0x1400023a0` | 1337 | ✓ |
| `fcn.1400028e0` | `0x1400028e0` | 1303 | ✓ |
| `fcn.1400034c0` | `0x1400034c0` | 1284 | ✓ |
| `fcn.140002080` | `0x140002080` | 796 | ✓ |
| `fcn.140002fa0` | `0x140002fa0` | 734 | ✓ |
| `fcn.140001aa0` | `0x140001aa0` | 685 | ✓ |
| `fcn.140001d50` | `0x140001d50` | 657 | ✓ |
| `fcn.140003280` | `0x140003280` | 570 | ✓ |
| `fcn.140001890` | `0x140001890` | 516 | ✓ |
| `fcn.140002e30` | `0x140002e30` | 357 | ✓ |
| `entry0` | `0x140001000` | 189 | ✓ |
| `fcn.140001ff0` | `0x140001ff0` | 132 | ✓ |
| `fcn.140003a20` | `0x140003a20` | 71 | ✓ |
| `fcn.1400039d0` | `0x1400039d0` | 67 | ✓ |
| `fcn.140002e00` | `0x140002e00` | 40 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400010f0.c`](code/fcn.1400010f0.c)
- [`code/fcn.140001890.c`](code/fcn.140001890.c)
- [`code/fcn.140001aa0.c`](code/fcn.140001aa0.c)
- [`code/fcn.140001d50.c`](code/fcn.140001d50.c)
- [`code/fcn.140001ff0.c`](code/fcn.140001ff0.c)
- [`code/fcn.140002080.c`](code/fcn.140002080.c)
- [`code/fcn.1400023a0.c`](code/fcn.1400023a0.c)
- [`code/fcn.1400028e0.c`](code/fcn.1400028e0.c)
- [`code/fcn.140002e00.c`](code/fcn.140002e00.c)
- [`code/fcn.140002e30.c`](code/fcn.140002e30.c)
- [`code/fcn.140002fa0.c`](code/fcn.140002fa0.c)
- [`code/fcn.140003280.c`](code/fcn.140003280.c)
- [`code/fcn.1400034c0.c`](code/fcn.1400034c0.c)
- [`code/fcn.1400039d0.c`](code/fcn.1400039d0.c)
- [`code/fcn.140003a20.c`](code/fcn.140003a20.c)

## Behavioral Analysis

Based on my analysis of the provided disassembly and strings, this binary is a **Command and Control (C2) Bot** (likely part of a botnet). It is designed to execute remote commands, exfiltrate local files, and maintain communication with a backend server while employing several techniques to evade detection.

### Core Functionality and Purpose
The primary purpose of this code is to act as a "worker" in a botnet. Its role is to check into a C2 server, identify itself with a unique ID, and perform actions dictated by the server via received commands.

*   **Bot Identification:** The `entry0` function generates a unique identity for each infected machine using a specific pattern (`BOT-xxxx-xxxx-xxxx-xxxx`). This allows a single C2 server to manage thousands of infected "bots" individually.
*   **Command Dispatcher:** Function `fcn.1400010f0` acts as the main logic gate. It parses incoming data and branches into different behaviors based on command codes:
    *   **Code 0x65 (Heartbeat/Status):** A routine check to confirm the bot is still active.
    *   **Code 0x66 (File Exfiltration):** Identifies a local file path and "uploads" its content to the server.
    *   **Code 0x67 (File Retrieval/Read):** Locates a specific file on the disk, checks its size (up to 4KB), and prepares it for transmission.
    *   **Code 0x69 (Configuration Update):** Allows the operator to change the "heartbeat" interval (e.g., how many milliseconds to wait before checking for new commands).

### Suspicious or Malicious Behaviors
The following behaviors are highly indicative of malware:

*   **Data Exfiltration:** The binary contains specific logic and error messages (`File uploaded successfully`, `Error: File path and data required`) indicating it is designed to steal files from the local filesystem.
*   **Information Gathering:** Function `fcn.140001aa0` traverses directories and lists file names and sizes, which is a common behavior in "reconnaissance" modules of malware (searching for documents, credentials, or other sensitive data).
*   **C2 Communication:** The inclusion of the `WinInet` library and logic to construct JSON payloads (`{"bot_id":..., "command_id":..., "result":...}`) confirms that it communicates with a remote server over HTTP/HTTPS.
*   **Remote Shell Execution:** The string `[DEBUG] execute_shell failed. Error: %d` suggests the bot can receive and attempt to run system commands (e.g., via `cmd.exe` or `powershell.exe`).

### Notable Techniques and Patterns
The author of this code employed several common "malware" techniques to hinder analysis:

*   **API Hashing & Obfuscation:** The function `fcn.1400028e0` is a classic example of **dynamic API resolution**. Instead of listing standard Windows functions (like `HttpSendRequestA`) in its Import Address Table (IAT), it hides them behind XORed hashes (`"&0'fg{199"`). This prevents security tools from seeing what the program does just by looking at the file.
*   **String Obfuscation:** Most strings used for internal logic or sensitive operations are XOR-encoded with `0x55`. For example, the string `"z4%<z7:!z6:884;1&j7:!"` is actually a decrypted instruction or value used during runtime.
*   **Modular Communication:** The use of JSON for reporting results back to the C2 server indicates a modern, organized infrastructure where commands are structured and easily parsed by a remote backend.
*   **Beaconing/Heartbeat:** The logic to set an "interval" between 1000ms and 60000ms allows the bot to hide its activity by not constantly hammering the C2 server, making it harder for network defenders to spot as a constant stream of traffic.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1041** | Exfiltration Over C2 Channel | The binary contains specific logic to identify local file paths and "upload" their content to a remote server. |
| **T1083** | File and Directory Discovery | The `fcn.140001aa0` function traverses directories and lists files/sizes to gather information for reconnaissance. |
| **T1059** | Command and Scripting Interpreter | The presence of the "execute_shell" string indicates the bot's capability to execute system commands via cmd or PowerShell. |
| **T1071.001** | Application Layer Protocol: Web Protocols | The binary utilizes the `WinInet` library and JSON payloads to communicate with a remote server over HTTP/HTTPS. |
| **T1027** | Obfuscated Files or Information | The use of XOR encoding (0x55) for strings and API hashing for dynamic resolution are used to hide functionality from static analysis. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, the following Indicators of Compromise (IOCs) have been identified:

**IP addresses / URLs / Domains**
*   *None identified.* (The analysis mentions C2 communication via WinInet but does not list specific hardcoded IP addresses or domains).

**File paths / Registry keys**
*   *None identified.* (The binary uses dynamic pathing and format strings like `%s` rather than hardcoded file paths).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the provided data).

**Other artifacts**
*   **Bot Identification Pattern:** `BOT-xxxx-xxxx-xxxx-xxxx` (Used for generating unique identifiers for infected machines).
*   **C2 Command Codes:** 
    *   `0x65`: Heartbeat/Status check.
    *   `0x66`: File Exfiltration.
    *   `0x67`: File Retrieval/Read.
    *   `0x69`: Configuration Update (e.g., adjusting heartbeat intervals).
*   **Communication Protocol:** JSON-formatted payloads for reporting results to the C2 server: `{"bot_id":"","command_id":"","result":""}`.
*   **Data Logging/Transmission Format:** `FILE:%s|DATA:%s|SIZE:%d` (Internal string used during file handling).
*   **Obfuscation Technique:** XOR encoding with key **0x55** used for internal logic and hidden strings.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: Bot / RAT
3. **Confidence**: High (for type) / Medium (for family)
4. **Key evidence**:
    *   **C2 Architecture & Modular Commands:** The use of a structured command-dispatch system (e.g., codes 0x65, 0x66, 0x67) to handle heartbeats, file exfiltration, and remote configuration updates is characteristic of organized botnets or Remote Access Trojans (RATs).
    *   **Evasive Techniques:** The presence of both string obfuscation (XOR 0x55) and dynamic API hashing indicates a deliberate attempt to bypass static analysis and evade signature-based detection.
    *   **Malicious Capabilities:** The combination of file system reconnaissance (T1083), remote command execution ("execute_shell"), and exfiltration via JSON-wrapped HTTP/HTTPS payloads confirms the sample's purpose as a tool for unauthorized access and data theft.
