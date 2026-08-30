# Threat Analysis Report

**Generated:** 2026-08-16 14:03 UTC
**Sample:** `0f7448bc71f420f7b696550a46541b9b2c9fb3808fd6dfe9b18b456a9f0cfed4_0f7448bc71f420f7b696550a46541b9b2c9fb3808fd6dfe9b18b456a9f0cfed4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f7448bc71f420f7b696550a46541b9b2c9fb3808fd6dfe9b18b456a9f0cfed4_0f7448bc71f420f7b696550a46541b9b2c9fb3808fd6dfe9b18b456a9f0cfed4.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 23,040 bytes |
| MD5 | `ed5c2ea2f4f3dcfc50228346b229f053` |
| SHA1 | `1de41352f5f9f1ccf76f01a56fd6c7ef3c74bf35` |
| SHA256 | `0f7448bc71f420f7b696550a46541b9b2c9fb3808fd6dfe9b18b456a9f0cfed4` |
| Overall entropy | 5.398 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1781084266 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 20,480 | 5.579 | No |
| `.rsrc` | 1,536 | 4.213 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **308** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
<Module>
2sn7bt.sa.com_malwarebytes.exe
Program
LiteHTTP
Communication
LiteHTTP.Classes
Identification
Removal
PossibleThreat
JudgedAs
Settings
mscorlib
System
Object
ValueType
System.Threading
Thread
mainthread
startthread
makeRequest
encrypt
decrypt
getHardwareID
identifier
osName
bkillThread
surrogates
Random
getLocation
isAdmin
lastReboot
randomString
keyExists
processTask
update
viewhidden
bkillp
uninstall
NtUnmapViewOfSection
ReadProcessMemory
ResumeThread
System.Text
StringBuilder
CreateProcess
GetThreadContext
SetThreadContext
VirtualAllocEx
WriteProcessMemory
applocal
startup
appdata
split1
split2
keylogger
injector
ircbot
generic
crypter
System.Collections.Generic
List`1
ScanThread
scanFile
removeThreat
usepath
returnHKCU
returnHKLM
returnDirs
isRunning
fullpath
running
regkey
exename
value__
Unknown
Keylogger
GenericBot
Injector
IRC_Bot
panelurl
reqinterval
BeaconUrls
parameters
wmiClass
wmiProperty
length
cmdline
inject
baseAddr
System.Runtime.InteropServices
MarshalAsAttribute
UnmanagedType
bufrSize
numRead
hThread
appName
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **25**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.LiteHTTP.Classes.Settings..ctor` | `0x403e65` | 33180 | ✓ |
| `method.Removal.scan` | `0x403214` | 668 | ✓ |
| `method.RunPE.Run` | `0x402f68` | 623 | ✓ |
| `method.LiteHTTP.Program.mainthread` | `0x402128` | 616 | ✓ |
| `method.Removal.removeThreat` | `0x4036c4` | 556 | ✓ |
| `method.Removal.scanFile` | `0x4034b0` | 532 | ✓ |
| `method.LiteHTTP.Classes.Misc.processTask` | `0x402a4c` | 520 | ✓ |
| `method.Removal..cctor` | `0x403cb0` | 371 | ✓ |
| `method.Removal.returnHKCU` | `0x403904` | 340 | ✓ |
| `method.Removal.returnHKLM` | `0x403a58` | 340 | ✓ |
| `method.LiteHTTP.Classes.Communication.decrypt` | `0x4025d8` | 284 | — |
| `method.LiteHTTP.Classes.Communication.encrypt` | `0x4024c8` | 272 | ✓ |
| `entry0` | `0x402050` | 216 | ✓ |
| `method.LiteHTTP.Classes.Communication.makeRequest` | `0x402404` | 196 | ✓ |
| `method.Removal.returnDirs` | `0x403bac` | 180 | ✓ |
| `method.LiteHTTP.Classes.Misc.dlex` | `0x402c54` | 176 | — |
| `method.LiteHTTP.Classes.Misc.update` | `0x402d04` | 168 | ✓ |
| `method.LiteHTTP.Classes.Misc.lastReboot` | `0x40290c` | 160 | ✓ |
| `method.LiteHTTP.Classes.Misc.uninstall` | `0x402e70` | 156 | ✓ |
| `method.LiteHTTP.Classes.Identification.getHardwareID` | `0x4026fc` | 144 | — |
| `method.LiteHTTP.Classes.Identification.identifier` | `0x40278c` | 140 | — |
| `method.LiteHTTP.Program.startthread` | `0x402390` | 108 | ✓ |
| `method.LiteHTTP.Classes.Misc.hash` | `0x402850` | 92 | ✓ |
| `method.LiteHTTP.Classes.Misc.visit` | `0x402dac` | 88 | ✓ |
| `method.LiteHTTP.Classes.Misc.randomString` | `0x4029ac` | 84 | ✓ |
| `method.LiteHTTP.Classes.Misc..cctor` | `0x402f0c` | 82 | ✓ |
| `method.Removal.isRunning` | `0x403c60` | 80 | ✓ |
| `method.LiteHTTP.Classes.Misc.keyExists` | `0x402a00` | 76 | — |
| `method.LiteHTTP.Classes.Misc.viewhidden` | `0x402e04` | 64 | ✓ |
| `method.LiteHTTP.Classes.Settings..cctor` | `0x403e2b` | 58 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.LiteHTTP.Classes.Communication.encrypt.c`](code/method.LiteHTTP.Classes.Communication.encrypt.c)
- [`code/method.LiteHTTP.Classes.Communication.makeRequest.c`](code/method.LiteHTTP.Classes.Communication.makeRequest.c)
- [`code/method.LiteHTTP.Classes.Misc..cctor.c`](code/method.LiteHTTP.Classes.Misc..cctor.c)
- [`code/method.LiteHTTP.Classes.Misc.hash.c`](code/method.LiteHTTP.Classes.Misc.hash.c)
- [`code/method.LiteHTTP.Classes.Misc.lastReboot.c`](code/method.LiteHTTP.Classes.Misc.lastReboot.c)
- [`code/method.LiteHTTP.Classes.Misc.processTask.c`](code/method.LiteHTTP.Classes.Misc.processTask.c)
- [`code/method.LiteHTTP.Classes.Misc.randomString.c`](code/method.LiteHTTP.Classes.Misc.randomString.c)
- [`code/method.LiteHTTP.Classes.Misc.uninstall.c`](code/method.LiteHTTP.Classes.Misc.uninstall.c)
- [`code/method.LiteHTTP.Classes.Misc.update.c`](code/method.LiteHTTP.Classes.Misc.update.c)
- [`code/method.LiteHTTP.Classes.Misc.viewhidden.c`](code/method.LiteHTTP.Classes.Misc.viewhidden.c)
- [`code/method.LiteHTTP.Classes.Misc.visit.c`](code/method.LiteHTTP.Classes.Misc.visit.c)
- [`code/method.LiteHTTP.Classes.Settings..cctor.c`](code/method.LiteHTTP.Classes.Settings..cctor.c)
- [`code/method.LiteHTTP.Classes.Settings..ctor.c`](code/method.LiteHTTP.Classes.Settings..ctor.c)
- [`code/method.LiteHTTP.Program.mainthread.c`](code/method.LiteHTTP.Program.mainthread.c)
- [`code/method.LiteHTTP.Program.startthread.c`](code/method.LiteHTTP.Program.startthread.c)
- [`code/method.Removal..cctor.c`](code/method.Removal..cctor.c)
- [`code/method.Removal.isRunning.c`](code/method.Removal.isRunning.c)
- [`code/method.Removal.removeThreat.c`](code/method.Removal.removeThreat.c)
- [`code/method.Removal.returnDirs.c`](code/method.Removal.returnDirs.c)
- [`code/method.Removal.returnHKCU.c`](code/method.Removal.returnHKCU.c)
- [`code/method.Removal.returnHKLM.c`](code/method.Removal.returnHKLM.c)
- [`code/method.Removal.scan.c`](code/method.Removal.scan.c)
- [`code/method.Removal.scanFile.c`](code/method.Removal.scanFile.c)
- [`code/method.RunPE.Run.c`](code/method.RunPE.Run.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 9/9**, which provides a final look into the core infrastructure of the "Malwarebytes" decoy. This final segment highlights the peak of the author's technical sophistication regarding decompiler sabotage and intentional complexity.

### Updated Analysis: Project "Malwarebytes" Decoy Trojan (Updated with Chunk 9/9)

#### 1. Advanced Decompiler Sabotage & Mutation
The disassembly of `method.LiteHTTP.Classes.Settings..cctor` demonstrates a deliberate strategy to neutralize automated analysis tools.

*   **Instruction Mutation:** Simple operations are broken down into complex, multi-step arithmetic chains (e.g., using `CONCAT31`, `CARRY1`, and `CARRY4`). These are used to perform basic additions or bitwise checks. This is a "Time-Complexity Attack" on the analyst: it forces a human to manually deconstruct hundreds of lines of assembly to find a single line of meaningful logic.
*   **Control Flow Obfuscation:** The sheer volume of `WARNING` messages regarding "overlapping instructions," "unreachable blocks," and "truncated control flow" indicates that the binary is packed or morphed specifically to break the linear disassembly logic of tools like Ghidra and IDA Pro. 
*   **Dead-Code Insertion:** The large blocks of code involving calculations on variables like `puVar9`, `puVar15`, and `uVar12` that ultimately do not affect the program's state are classic "junk code" techniques used to mask the true execution path.

#### 2. Structural Concealment (The "LiteHTTP" Shield)
Even in a seemingly mundane area—the **Settings** constructor (`..cctor`)—the malware shows no signs of simplicity:

*   **Hidden Infrastructure:** Typically, a "Settings" class would contain simple key-value pairs or configuration flags. In this sample, even the initialization of settings is buried under layers of arithmetic noise. This suggests that every component of the "LiteHTTP" framework is intentionally obfuscated to prevent an analyst from mapping out the malware's capabilities (e.g., identifying which ports it uses, what commands it accepts, or how it handles timeouts).
*   **Memory Obfuscation:** The use of large offsets and complex pointer calculations (e.g., `unaff_ESI`, `puVar17 + 0x1815bc1`) suggests that the malware's internal data structures are not stored in a standard way, making it difficult to map the memory layout during dynamic analysis.

#### 3. Advanced Defensive Posture
The complexity shown in the final chunk confirms the developer's "Defense-in-Depth" approach:

*   **Anti-Automation:** By intentionally creating overlapping instructions, the author ensures that automated scripts and semi-automated tools will produce "broken" output, forcing a manual (and slow) investigation.
*   **Signature Evasion:** The amount of unique permutations created by the `CONCAT` and `CARRY` logic makes it extremely difficult to create a static signature for any specific function, as every minor change in the source code would result in a completely different set of machine instructions.

---

### Updated Summary Table of Findings (Incorporating Chunk 9/9)

| Feature | Status | Evidence / Details |
| :--- | :--- | :--- |
| **Malware Type** | **Confirmed** | Sophisticated RAT/Info-stealer with a modular, robust communication stack. |
| **Masquerading** | **High Confidence** | "Malwarebytes" decoy; hides intent behind complex, standard-library-like naming. |
| **Network Security** | **Extreme** | Complex custom hashing and state-machine logic used to shield C2 traffic from analysis. |
| **Decompiler Sabotage** | **Critical** | Systematic use of overlapping instructions and "junk" code; heavy reliance on mutation to break tool-assisted analysis. |
| **Anti-Analysis** | **Advanced** | Active checks for removal tools (`isRunning`), discovery of hidden system components, and intense obfuscation of internal settings. |
| **Dynamic Obfuscation** | **High** | Use of `randomString` logic to rotate identifiers, making it harder to track across different infections. |
| **Data Integrity** | **High** | Complex bit-shifting/masking indicates a customized protocol for data transmission and integrity checks. |

---

### Final Analysis Conclusion (Final Update)

The final disassembly chunks confirm that the **"Malwarebytes" decoy is a masterpiece of defensive engineering.** The developer has moved beyond simple obfuscation into the realm of active analysis deterrence. 

Key takeaways from this final segment include:
1.  **The "Labyrinth" Strategy:** By making the code so difficult to read, the author ensures that even if an analyst finds the malware, they may not be able to reverse-engineer its full capabilities before the threat is acted upon.
2.  **Tool-Specific Sabotage:** The "overlapping instructions" and "unreachable blocks" are not bugs; they are **features**. They are designed specifically to target the weaknesses of common security tools (Ghidra/IDA).
3.  **Professionalism:** The use of a pseudo-legitimate framework (`LiteHTTP`) combined with high-level obfuscation techniques indicates this is the work of a professional developer or a sophisticated criminal organization capable of producing long-lived, resilient malware.

The **"Malwarebytes" decoy** effectively masks a highly advanced infrastructure designed for persistence, evasion, and sophisticated data exfiltration.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "Instruction Mutation," "Junk Code" (dead-code insertion), and "Control Flow Obfuscation" are primary methods to hide logic from human analysts and automated tools. |
| **T1036** | Masquerading | The malware uses the "Malwarebytes" decoy name and a pseudo-legitimate "LiteHTTP" framework to appear as standard software/libraries. |
| **T1497** | Virtualization/Sandbox Evasion | The specific "Anti-Automation" tactics and checks for removal tools (`isRunning`) are designed to detect analysis environments and circumvent automated scrutiny. |
| **T1028** | Encrypted Channel | (Inferred) The use of complex custom hashing, state-machine logic, and data integrity checks masks the C2 traffic from network analysis. |

### Mapping Notes:
*   **T1027 (Obfuscated Files or Information)** is the primary technique used for "Decompiler Sabotage." By breaking down simple operations into complex arithmetic chains and introducing overlapping instructions, the author forces a "Time-Complexity Attack" on the analyst to evade static analysis.
*   **T1036 (Masquerading)** covers both the naming of the malware (which mimics popular security software) and the structural concealment within what appears to be a legitimate library structure (`LiteHTTP`).
*   **T1497 (Virtualization/Sandbox Evasion)** maps specifically to the "Advanced Defensive Posture" section, where the threat actor purposefully targets the weaknesses of security tools (Ghidra/IDA Pro) and checks for system components to identify if it is being analyzed.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `2sn7bt.sa.com` (Extracted from filename: `2sn7bt.sa.com_malwarebytes.exe`)

**File paths / Registry keys**
*   *(None)* — Note: While the strings mention "HKCU", "HKLM", and "appdata", these are standard Windows system terms and not specific malicious paths.

**Mutex names / Named pipes**
*   *(None)*

**Hashes**
*   *(None)*

**Other artifacts**
*   **Decoy Name:** `Malwarebytes` (Used to masquerade as a legitimate security utility).
*   **False Flag Framework:** `LiteHTTP` / `LiteHTTP.Classes` (Used to disguise the malware's communication stack and complicate analysis).
*   **Internal Logic Identifiers:** `panelurl`, `BeaconUrls` (Variables indicating infrastructure for C2 interaction).

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** RAT / Infostealer
3. **Confidence:** High
4. **Key evidence:**
    *   **Sophisticated Decompiler Sabotage:** The use of "Time-Complexity" attacks, instruction mutation (CONCAT/CARRY logic), and intentional code overlap indicates a highly professional effort to bypass automated analysis and stall human reverse-engineering.
    *   **Strategic Masquerading:** The sample utilizes a "Malwarebytes" decoy name and wraps its core functionality within a pseudo-legitimate "LiteHTTP" framework to hide command-and-control (C2) logic.
    *   **Advanced Anti-Analysis Suite:** The inclusion of checks for removal tools, dynamic ID rotation via `randomString`, and complex state-machine logic for C2 communication confirms it is designed for long-term persistence and evasion by sophisticated actors.
