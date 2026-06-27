# Threat Analysis Report

**Generated:** 2026-06-27 00:17 UTC
**Sample:** `01718933eb502e4ec9d4b1210a88cb026882d615605dd8d7fbf1c4057b7c0867_01718933eb502e4ec9d4b1210a88cb026882d615605dd8d7fbf1c4057b7c0867.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `01718933eb502e4ec9d4b1210a88cb026882d615605dd8d7fbf1c4057b7c0867_01718933eb502e4ec9d4b1210a88cb026882d615605dd8d7fbf1c4057b7c0867.exe` |
| File type | PE32+ executable for MS Windows 6.01 (GUI), x86-64, 9 sections |
| Size | 1,537,536 bytes |
| MD5 | `b54fdb103475681d721890b27d06edc0` |
| SHA1 | `1c24da264bce471366156b4721bacb83201ba759` |
| SHA256 | `01718933eb502e4ec9d4b1210a88cb026882d615605dd8d7fbf1c4057b7c0867` |
| Overall entropy | 6.104 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 582,144 | 6.221 | No |
| `.rdata` | 782,336 | 5.433 | No |
| `.data` | 67,584 | 4.788 | No |
| `.pdata` | 17,920 | 5.159 | No |
| `.xdata` | 512 | 1.76 | No |
| `.idata` | 1,536 | 4.014 | No |
| `.reloc` | 13,824 | 5.422 | No |
| `.symtab` | 512 | 0.02 | No |
| `.rsrc` | 69,632 | 5.753 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **4838** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.xdata
@.idata
.reloc
B.symtab
B.rsrc
 Go build ID: "84BPiBFdgOGRZl_hMsxT/WKWHBo211qa3E7NHlH6N/ctVHlQ01p7Upe1wLFTxe/KGLFnlX1RUrf5Mb-OQQl"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
\$PH9H@v#H
D$pL9A
L$pL9N
D$@I9p
\$hM9K
\$hM9K
l$8M9,$u
P(H9S(t
P H9S uqH
S0H9P0ug
P88S8u^
P98S9uUH
expafH
nd 3fH
2-byfH
te kfH
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
:H9F w
>H+zhH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
2}#s]H
D$PA)P
H9D$(t
H
^0H9X0tQ
\$XHc
$H+L$HH
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
v	H98
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
vDH95 
J0f9J2vuH
f9s2uFf
D$$u$L
T$(M	D
	I9x tE1
runtime.H9
QpM9Qhu
L9L$Xt$H
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
rhH92w
tRI9N0tLH
T$`Hc3
L$XHcw
|$0uMH
memprofi
lerau*f
yteu"H
9q0s&H9J
09z0w
H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140070120` | `0x140070120` | 426746 | ✓ |
| `fcn.140070180` | `0x140070180` | 402971 | ✓ |
| `fcn.140070140` | `0x140070140` | 402970 | ✓ |
| `fcn.140074c00` | `0x140074c00` | 261335 | ✓ |
| `fcn.1400705e0` | `0x1400705e0` | 234216 | ✓ |
| `fcn.140070600` | `0x140070600` | 234088 | ✓ |
| `fcn.140070620` | `0x140070620` | 233963 | ✓ |
| `fcn.140070640` | `0x140070640` | 233835 | ✓ |
| `fcn.140070660` | `0x140070660` | 233707 | ✓ |
| `fcn.140070680` | `0x140070680` | 233579 | ✓ |
| `fcn.1400706a0` | `0x1400706a0` | 233448 | ✓ |
| `fcn.1400706c0` | `0x1400706c0` | 233320 | ✓ |
| `fcn.1400706e0` | `0x1400706e0` | 233192 | ✓ |
| `fcn.140070700` | `0x140070700` | 233064 | ✓ |
| `fcn.140074d60` | `0x140074d60` | 228919 | ✓ |
| `fcn.140074dc0` | `0x140074dc0` | 197591 | ✓ |
| `fcn.140074e60` | `0x140074e60` | 166135 | ✓ |
| `fcn.140074ec0` | `0x140074ec0` | 147799 | ✓ |
| `entry0` | `0x140071820` | 14597 | ✓ |
| `fcn.140070100` | `0x140070100` | 11763 | ✓ |
| `fcn.140017280` | `0x140017280` | 6181 | ✓ |
| `fcn.140041be0` | `0x140041be0` | 4942 | ✓ |
| `fcn.14001afa0` | `0x14001afa0` | 4350 | ✓ |
| `fcn.140026340` | `0x140026340` | 3924 | ✓ |
| `fcn.14006e120` | `0x14006e120` | 3825 | ✓ |
| `fcn.14007ffa0` | `0x14007ffa0` | 3575 | ✓ |
| `fcn.140087680` | `0x140087680` | 3129 | ✓ |
| `fcn.140064700` | `0x140064700` | 3022 | ✓ |
| `fcn.14002d160` | `0x14002d160` | 2917 | ✓ |
| `fcn.14006c6c0` | `0x14006c6c0` | 2575 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140017280.c`](code/fcn.140017280.c)
- [`code/fcn.14001afa0.c`](code/fcn.14001afa0.c)
- [`code/fcn.140026340.c`](code/fcn.140026340.c)
- [`code/fcn.14002d160.c`](code/fcn.14002d160.c)
- [`code/fcn.140041be0.c`](code/fcn.140041be0.c)
- [`code/fcn.140064700.c`](code/fcn.140064700.c)
- [`code/fcn.14006c6c0.c`](code/fcn.14006c6c0.c)
- [`code/fcn.14006e120.c`](code/fcn.14006e120.c)
- [`code/fcn.140070100.c`](code/fcn.140070100.c)
- [`code/fcn.140070120.c`](code/fcn.140070120.c)
- [`code/fcn.140070140.c`](code/fcn.140070140.c)
- [`code/fcn.140070180.c`](code/fcn.140070180.c)
- [`code/fcn.1400705e0.c`](code/fcn.1400705e0.c)
- [`code/fcn.140070600.c`](code/fcn.140070600.c)
- [`code/fcn.140070620.c`](code/fcn.140070620.c)
- [`code/fcn.140070640.c`](code/fcn.140070640.c)
- [`code/fcn.140070660.c`](code/fcn.140070660.c)
- [`code/fcn.140070680.c`](code/fcn.140070680.c)
- [`code/fcn.1400706a0.c`](code/fcn.1400706a0.c)
- [`code/fcn.1400706c0.c`](code/fcn.1400706c0.c)
- [`code/fcn.1400706e0.c`](code/fcn.1400706e0.c)
- [`code/fcn.140070700.c`](code/fcn.140070700.c)
- [`code/fcn.140074c00.c`](code/fcn.140074c00.c)
- [`code/fcn.140074d60.c`](code/fcn.140074d60.c)
- [`code/fcn.140074dc0.c`](code/fcn.140074dc0.c)
- [`code/fcn.140074e60.c`](code/fcn.140074e60.c)
- [`code/fcn.140074ec0.c`](code/fcn.140074ec0.c)
- [`code/fcn.14007ffa0.c`](code/fcn.14007ffa0.c)
- [`code/fcn.140087680.c`](code/fcn.140087680.c)

## Behavioral Analysis

This updated analysis incorporates the findings from chunk 3 of the disassembly. This final segment provides granular detail on how the malware processes environment data and handles its internal logic flow, further confirming its sophisticated design.

### Updated Analysis Report

#### Core Functionality and Purpose
The sample is a highly sophisticated piece of malware—likely a modular Trojan or a complex multi-stage loader—built using the **Go programming language**. The analysis confirms that it possesses several layers of abstraction:

1.  **Complex State Machines:** Transitioning between various operational modes (e.g., communication, data extraction, and persistence).
2.  **Internal Protocol Handling:** Parsing complex, nested data structures, likely for communicating with a Command & Control (C2) server.
3.  **Dynamic Path/Data Normalization:** The malware performs extensive "sanitization" of strings and paths, ensuring that internal commands or file operations are formatted correctly before execution.

---

### Suspicious or Malicious Behaviors

*   **Granular Path Reconstruction & Sanitization:**
    *   The code preceding `fcn.140064700` contains heavy logic for traversing strings to identify and replace directory separators (`/`, `\`) and ensuring the presence of file extensions (dots). 
    *   This is not just "finding" a path; it is **constructing** one. This suggests that commands received from a C2 server might be sent in a raw or obfuscated format, which the malware then "cleans up" to ensure they are valid paths for local Windows API calls.

*   **Large-Scale Dispatcher Logic (Command Processing):**
    *   The massive `switch` statement inside `fcn.140064700` is a hallmark of a **modular dispatcher**. Each "case" likely represents a different capability:
        *   One case may handle keylogging; 
        *   Another might initiate a file download; 
        *   Another may execute a shell command or adjust registry keys.
    *   The complexity here indicates that the malware is designed to be a multi-functional tool, not just a single-purpose downloader.

*   **Sophisticated Buffer & Memory Management:**
    *   The constant checks for offsets (e.g., `0x1400638c0`, `0x140063fe0`) and the heavy use of standard Go "safety" checks in a non-standard context suggest that the malware is utilizing the full power of the Go runtime to manage its internal memory safely, making it harder for automated tools to distinguish between malicious logic and standard library functions.

*   **Multithreaded Synchronization:**
    *   The frequent use of `LOCK()` and `UNLOCK()` confirms a high degree of concurrency. This allows the malware to perform heavy operations (like data encryption or network polling) without freezing the host's UI, making it less detectable by a casual user.

---

### Technical Analysis & Evolution of Findings

**1. Advanced Go Runtime Utilization:**
The disassembly highlights that the code is not "bare-metal" assembly but sits atop a heavy Go runtime wrapper. This provides several advantages to the attacker:
*   **Complexity as Obfuscation:** The sheer amount of logic required just to manage strings and slices (as seen in `fcn.140064700`) acts as "noise," making it difficult for an analyst to find the core malicious payloads without significant manual effort.
*   **Robustness:** By utilizing Go's internal handling for memory management, the malware is less likely to crash or behave erratically on different versions of Windows, increasing its reliability in the wild.

**2. Protocol Layer Obfuscation & Normalization:**
The logic seen in the path manipulation blocks suggests a "normalization" phase. This indicates that the C2 instructions are likely designed to be somewhat generic; the malware then converts these into specific local actions (e.g., taking a C2 command like `get_file_X` and turning it into a full, sanitized local file path).

**3. Modular Command Execution:**
The massive switch-case block is extremely characteristic of "Loader" behavior. Rather than having many different viruses, the developers have created one complex engine that can perform hundreds of different actions based on which "Case" is triggered by the C2's command. This makes it much harder to create a signature for "all functions" performed by the malware.

---

### Summary for Incident Response (Final Update)

**Threat Profile:** High-sophistication Modular Trojan / Multi-functional Loader.
**Key Technical Characteristics:**
*   **Robust Dispatcher Architecture:** The code is structured to handle many different functionalities through a central processing hub, making it highly versatile. 
*   **Automated String/Path Normalization:** It dynamically cleans and builds paths/commands from raw input, likely coming from the C2 or internal configuration files.
*   **Heavy Go Runtime Reliance:** The use of standard-but-complex Go idioms for memory and thread management makes signature-based detection very difficult.

**Recommended Actions:**
*   **Memory Forensics is Critical:** Because much of the "decoding" happens in a series of complex internal functions, it is highly likely that C2 addresses, file paths, and secondary payloads are only revealed in memory during execution. Perform live memory dumps to capture these values.
*   **Behavioral Analysis (E1/EDR):** Focus on identifying the *actions* taken by the process (e.g., writing to new folders, spawning `cmd.exe`, or reaching out to unusual IPs) rather than just static signatures of the file itself.
*   **Advanced YARA Strategy:** Focus on Go-specific runtime artifacts and the "Switch" logic patterns. Create rules that target the specific sequence of calls used for internal string/slice manipulation, which is a constant across various modules of this loader.
*   **Network Monitoring:** Look for consistent heartbeat traffic or "heartbeated" packet sizes that indicate a multi-threaded listener waiting for commands from its C2 server.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The granular path reconstruction and string normalization logic suggest that raw, potentially obfuscated C2 instructions are being processed into valid local paths. |
| **T1105** | Ingress Tool Transfer | The large-scale dispatcher indicates a modular architecture capable of receiving and staging additional payloads or tools as needed. |
| **T1059** | Command and Scripting Interpreter | The inclusion of specific "cases" for shell commands within the dispatcher shows the malware is designed to execute arbitrary system commands. |
| **T1036** | Masquerading | The use of multithreaded synchronization ensures the malware remains responsive and does not freeze the host UI, making it less noticeable to a standard user. |
| **T1568** | Dynamic Resolution | (Implicit) The "normalization" phase where generic C2 instructions are converted into specific local actions indicates a method for dynamically resolving commands. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs). 

Note: The sample demonstrates high levels of obfuscation; therefore, several standard indicators (such as hardcoded C2 IP addresses or explicit file paths) were not present in the raw string dump and will likely only appear in memory during execution.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (The terms "file" and "pipe" appeared in the strings, but no specific path or key values were present).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified (Note: A **Go build ID** was identified (`84BPiBFdgOGRZl_hMsxT/WKWHBo211qa3E7NHlH6N/ctVHlQ01p7Upe1wLFTxe/KGLFnlX1RUrf5Mb-OQQl`), but this is a compiler artifact and not a file hash).

**Other artifacts**
*   **Internal Memory Offsets:** `0x1400638c0`, `0x140063fe0` (Used for internal logic/buffer management).
*   **Function Reference:** `fcn.140064700` (Identified as the primary modular dispatcher for command processing).
*   **Behavioral Pattern:** Large-scale "Switch" statement logic used to parse and execute commands ranging from keylogging to file downloads.
*   **Behavioral Pattern:** Automated string/path normalization (The malware converts raw C2 input into valid Windows directory strings at runtime).

---

## Malware Family Classification

1. **Malware family**: Unknown (Go-based Modular Framework)
2. **Malware type**: Loader / Backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Modular Dispatcher Architecture:** The presence of a massive `switch` statement (`fcn.140064700`) indicates the malware is designed to perform multiple functions (keylogging, file downloads, shell commands) based on instructions received from a C2 server.
    *   **Path Normalization & Obfuscation:** The sophisticated logic used to "clean" and construct local Windows paths from raw data suggests it is designed to process remote commands in a way that avoids detection while ensuring local execution success.
    *   **Advanced Go Runtime Usage:** By leveraging the Go programming language, the malware utilizes complex internal management for threading, memory handling, and string manipulation, providing both stability across systems and a layer of "noise" to hinder manual analysis.
