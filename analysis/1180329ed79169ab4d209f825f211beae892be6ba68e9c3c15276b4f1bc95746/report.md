# Threat Analysis Report

**Generated:** 2026-08-23 18:38 UTC
**Sample:** `1180329ed79169ab4d209f825f211beae892be6ba68e9c3c15276b4f1bc95746_1180329ed79169ab4d209f825f211beae892be6ba68e9c3c15276b4f1bc95746.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1180329ed79169ab4d209f825f211beae892be6ba68e9c3c15276b4f1bc95746_1180329ed79169ab4d209f825f211beae892be6ba68e9c3c15276b4f1bc95746.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 119,808 bytes |
| MD5 | `b2659dc07d24083f8adf3138d39054b9` |
| SHA1 | `10ba01fdbf8bdc3ff564fbc025bba6f77b1c5620` |
| SHA256 | `1180329ed79169ab4d209f825f211beae892be6ba68e9c3c15276b4f1bc95746` |
| Overall entropy | 5.634 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773888790 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 117,248 | 5.672 | No |
| `.rsrc` | 1,536 | 3.68 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **680** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
 C^r!

 |D^r!
 DD^r!
 HD^r!
 !D^r!
 xE^r!
 hE^r!
 ?C^r!
 TD^r!
 ;@^r!
 QD^r!
 >@^r!

 &@^r!
 -B^r!
 GC^r!
 eF^r!
 yH^r!
 ;H^r!
 ;H^r!
 9H^r!
 wH^r!

 <H^r!
 7H^r!

 8H^r!
 gI^r!

 hI^r!
 VI^r!
 aI^r!
 KI^r!

 9I^r!
 ~C^r!

 aC^r!
 XC^r!
 ?C^r!
 CE^r!
 1E^r!
 *E^r!
 E^r!
 .E^r!
 BE^r!
 wF^r!
 |G^r!
 [G^r!
 8C^r!
 6G^r!
 YG^r!
 XG^r!
 wJ^r!

 jJ^r!
 XJ^r!
 6J^r!
 !J^r!
 
J^r!
 qK^r!
 uK^r!
 kK^r!
 QK^r!

 BK^r!
 <K^r!
 ?K^r!
 %K^r!
 /K^r!
 [G^r!
 WG^r!
 XG^r!
 [G^r!
 ]G^r!
 _G^r!
 [G^r!
 7C^r!
 FD^r!
 =@^r!
 T@^r!
 O@^r!
 8@^r!
 "@^r!
 $@^r!
 <B^r!
 kB^r!

 iB^r!
 !@^r!
 *B^r!
 #@^r!
 DC^r!
 (C^r!
 tE^r!
 <C^r!
 <C^r!
 VF^r!
 BF^r!
 WF^r!
 DG^r!
 FG^r!
 -B^r!
 )@^r!
 gF^r!
 )B^r!
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method...` | `0x415d0c` | 58100 | ✓ |
| `sym.Stub.USB.` | `0x40ebb0` | 5652 | ✓ |
| `method.Stub.Messages.Read` | `0x406b5c` | 5620 | ✓ |
| `method.Stub.Uninstaller.UNS` | `0x40c954` | 2856 | ✓ |
| `method.Stub.Messages.Plugin` | `0x408150` | 2816 | ✓ |
| `entry0` | `0x403238` | 2688 | ✓ |
| `sym.Stub.XLogger.__1` | `0x411238` | 2332 | ✓ |
| `sym.Stub.Main.__2` | `0x404258` | 1280 | ✓ |
| `sym...__4` | `0x415210` | 1060 | ✓ |
| `sym...__5` | `0x415634` | 1016 | ✓ |
| `method.Stub.ClientSocket.Antivirus` | `0x4055a8` | 1000 | ✓ |
| `method.Stub.ClientSocket.Info` | `0x404eac` | 956 | ✓ |
| `method.Stub.ClientSocket.BeginReceive` | `0x406004` | 904 | ✓ |
| `method.Stub.Main.Exclusion` | `0x403cb8` | 824 | ✓ |
| `method.Stub.ClientSocket.Send` | `0x4063d0` | 764 | ✓ |
| `method.Stub.Messages.Monitoring` | `0x408f64` | 696 | ✓ |
| `sym.Stub.Messages.` | `0x40951c` | 648 | ✓ |
| `method.Stub.ClientSocket.ConnectServer` | `0x404c48` | 612 | ✓ |
| `method.Stub.ClientSocket.GPU` | `0x405990` | 588 | ✓ |
| `method.Stub.ClientSocket.BeginConnect` | `0x404a08` | 576 | ✓ |
| `method.Stub.ClientSocket.isDisconnected` | `0x406728` | 576 | ✓ |
| `method.Stub.Messages.TD` | `0x408d30` | 564 | ✓ |
| `sym.Stub.Uninstaller.` | `0x40d47c` | 552 | ✓ |
| `method.Stub.Messages.OpenUrl` | `0x40921c` | 548 | ✓ |
| `method.Stub.ClientSocket.RAM` | `0x405de8` | 540 | ✓ |
| `method.._Lambda___8` | `0x40b394` | 536 | ✓ |
| `method.Stub.ClientSocket.CPU` | `0x405bdc` | 524 | ✓ |
| `sym.Stub.Uninstaller.__2` | `0x40d758` | 500 | ✓ |
| `method.Stub.XLogger.` | `0x411cf0` | 500 | ✓ |
| `method.Settings..cctor` | `0x403068` | 432 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method....c`](code/method....c)
- [`code/method.._Lambda___8.c`](code/method.._Lambda___8.c)
- [`code/method.Settings..cctor.c`](code/method.Settings..cctor.c)
- [`code/method.Stub.ClientSocket.Antivirus.c`](code/method.Stub.ClientSocket.Antivirus.c)
- [`code/method.Stub.ClientSocket.BeginConnect.c`](code/method.Stub.ClientSocket.BeginConnect.c)
- [`code/method.Stub.ClientSocket.BeginReceive.c`](code/method.Stub.ClientSocket.BeginReceive.c)
- [`code/method.Stub.ClientSocket.CPU.c`](code/method.Stub.ClientSocket.CPU.c)
- [`code/method.Stub.ClientSocket.ConnectServer.c`](code/method.Stub.ClientSocket.ConnectServer.c)
- [`code/method.Stub.ClientSocket.GPU.c`](code/method.Stub.ClientSocket.GPU.c)
- [`code/method.Stub.ClientSocket.Info.c`](code/method.Stub.ClientSocket.Info.c)
- [`code/method.Stub.ClientSocket.RAM.c`](code/method.Stub.ClientSocket.RAM.c)
- [`code/method.Stub.ClientSocket.Send.c`](code/method.Stub.ClientSocket.Send.c)
- [`code/method.Stub.ClientSocket.isDisconnected.c`](code/method.Stub.ClientSocket.isDisconnected.c)
- [`code/method.Stub.Main.Exclusion.c`](code/method.Stub.Main.Exclusion.c)
- [`code/method.Stub.Messages.Monitoring.c`](code/method.Stub.Messages.Monitoring.c)
- [`code/method.Stub.Messages.OpenUrl.c`](code/method.Stub.Messages.OpenUrl.c)
- [`code/method.Stub.Messages.Plugin.c`](code/method.Stub.Messages.Plugin.c)
- [`code/method.Stub.Messages.Read.c`](code/method.Stub.Messages.Read.c)
- [`code/method.Stub.Messages.TD.c`](code/method.Stub.Messages.TD.c)
- [`code/method.Stub.Uninstaller.UNS.c`](code/method.Stub.Uninstaller.UNS.c)
- [`code/method.Stub.XLogger..c`](code/method.Stub.XLogger..c)
- [`code/sym...__4.c`](code/sym...__4.c)
- [`code/sym...__5.c`](code/sym...__5.c)
- [`code/sym.Stub.Main.__2.c`](code/sym.Stub.Main.__2.c)
- [`code/sym.Stub.Messages..c`](code/sym.Stub.Messages..c)
- [`code/sym.Stub.USB..c`](code/sym.Stub.USB..c)
- [`code/sym.Stub.Uninstaller..c`](code/sym.Stub.Uninstaller..c)
- [`code/sym.Stub.Uninstaller.__2.c`](code/sym.Stub.Uninstaller.__2.c)
- [`code/sym.Stub.XLogger.__1.c`](code/sym.Stub.XLogger.__1.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 2/2, I have updated and expanded the analysis of the binary sample. The new data confirms several previously suspected techniques and highlights a sophisticated level of anti-analysis engineering.

### Updated Analysis of Binary Sample

#### Core Functionality and Purpose (Updated)
The core functionality remains consistent with previous findings: this is a **malicious loader/backdoor**. However, the second chunk of disassembly provides deeper insight into how the malware protects its "inner" logic.

*   **Complex Stub Architecture:** The functions `method.Stub.ClientSocket.CPU` and `sym.Stub.Uninstaller.__2` are not standard coding practices. They act as **obfuscated wrappers**. Instead of containing direct logic, they use complex mathematical transformations to hide the transition between the loader and the actual malicious payload.
*   **Persistence & Cleanup:** The `Uninstaller` routine remains a key component. Its presence in such an obfuscated state suggests that the "clean" option is likely just as carefully engineered as the malware itself to evade detection during manual inspection.

#### Suspicious and Malicious Behaviors (Enhanced)
The following elements have been reinforced by the new data:

*   **Advanced Anti-Analysis/Anti-Disassembly:** 
    *   **Instruction Overlapping:** The decompiler explicitly flags "overlapping instructions" in `ClientSocket.CPU` and `Uninstaller.__2`. This is a classic technique where a jump target is placed in the middle of an existing instruction, forcing disassemblers to interpret the code incorrectly.
    *   **Opaque Predicates:** The extensive use of complex arithmetic (e.g., `POPCOUNT`, `CONCAT31`, and bitwise operations) to determine simple branch conditions suggests "opaque predicates"—conditions that are always true or false but are computationally difficult for an automated tool to resolve, thus hiding the real code path from analysts.
*   **Malware Persistence via Obfuscation:** The complexity of the `Uninstaller` and `ClientSocket` functions indicates a high level of effort to hide the **C2 communication logic**. By making the code nearly unreadable to human eyes, the developers ensure that even if a researcher identifies the functionality, they may struggle to extract actionable intelligence (like specific C2 protocols or hardcoded IP addresses).

#### Notable Techniques & Patterns (Expanded)
The new disassembly highlights several high-level evasion techniques:

*   **Heavy Obfuscation & Junk Code Insertion:** 
    *   The presence of "Bad instruction" and "Truncating control flow" warnings in almost every function indicates the use of **junk code**. This is designed to break the analysis process by making it difficult for a human to follow any coherent logic.
    *   **Mathematical Obfuscation:** The frequent use of `CONCAT`, `POPCOUNT`, and complex arithmetic results from an obfuscator (such as VMProtect, Themida, or specialized .NET packers). These tools transform simple instructions into long chains of mathematical operations that are difficult to "de-obfuscate."
*   **Refined Identification of Packer/Obfuscator:** 
    *   The `cctor` function for `method.Settings` is a standard .NET constructor, but its mangled appearance confirms that the entire managed assembly has been processed by a **protector**. This means the actual logic of the "Settings" and "Communication" modules is likely encrypted or virtualized within this layer.
*   **Stub-Based Logic:** The repeated use of `.Stub.` in naming conventions (e.g., `method.Stub.XLogger`) confirms that the binary is part of a multi-stage loading process where the primary malicious payload remains hidden until runtime.

---

### Summary for Incident Response (Updated)

This sample is a **highly sophisticated piece of malware** utilizing advanced evasion techniques common in modern APTs and high-level trojan families. 

*   **Threat Level:** High
*   **Primary Risks:** Remote Access, Information Theft, Persistence.
*   **Key Technical Findings:**
    *   **Advanced Obfuscation:** The binary uses instruction overlapping and opaque predicates to thwart automated disassembly tools.
    *   **Protector Presence:** It is highly likely that the core malicious logic (C2 commands, data exfiltration) is hidden within a virtualized or encrypted layer protected by a heavy packer.
    *   **Evasive Maneuvers:** The code specifically targets the "blind spots" of security analysts and automated tools by making the control flow unintelligible without advanced de-obfuscation techniques.

**Recommended Action:** 
1.  **Isolate infected hosts immediately.** 
2.  **Perform memory forensics (e.g., Volatility)** to capture the .NET assembly in its unpacked state during runtime; this is necessary to see the "real" code hidden behind the `.Stub` layers.
3.  **Monitor for non-standard network traffic** associated with `ClientSocket`, as the obfuscation makes it difficult to extract networking parameters from the static file alone.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your report to the relevant MITRE ATT&CK techniques. The primary focus of this malware's behavior is **Defense Evasion**, specifically through complex obfuscation and packing layers.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of "junk code," opaque predicates, and overlapping instructions is designed to complicate manual analysis and thwart automated disassembly tools. |
| **T1027.001** | Packing | The report identifies the use of known protectors (e.g., VMProtect, Themida) to wrap the core malicious logic within a heavily obfuscated layer. |
| **T1568** | Dynamic Resolution (Implied) | While not explicitly stated as an API call, the "Stub-based" architecture and hidden C2 logic suggest the binary avoids standard signatures by resolving its true functionality at runtime. |

### Analyst Notes:
*   **Defense Evasion Focus:** The core of this sample's sophistication lies in **T1027**. By employing "instruction overlapping," the author is specifically targeting the weaknesses of disassemblers (like IDA Pro or Ghidra) to hide malicious logic paths.
*   **Multi-Stage Execution:** The mention of `.Stub.` naming conventions and a "multi-stage loading process" indicates that the initial execution may be purely for unpacking/de-obfuscation before the primary payload (the backdoor) is fully resident in memory. This reinforces why **memory forensics** was prioritized in your recommendations.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Many items in the "Strings" section were excluded as they represent standard .NET environment metadata (e.g., kernel32.dll, System.Drawing) or obfuscated junk data.*

### **IP addresses / URLs / Domains**
*None identified (The analysis notes that C2 infrastructure is currently hidden behind layers of obfuscation).*

### **File paths / Registry keys**
*   `oop.exe` (Identified as a file name, though no specific path was provided).

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.*

### **Other artifacts (Internal Logic & Indicators of Behavior)**
The following items are indicators of the specific obfuscation tools and internal logic structures used by this threat actor:

*   **Malicious Stub Functions:**
    *   `method.Stub.ClientSocket.CPU` (Indicator of hidden C2 communication logic)
    *   `sym.Stub.Uninstaller.__2` (Indicator of hidden persistence/cleanup logic)
    *   `method.Stub.XLogger` (Internal logging component)
*   **C2 Communication Component:** `ClientSocket` (Used for network interaction).
*   **Persistence Component:** `Uninstaller` (Used to manage the presence of the malware on the host).
*   **Obfuscation Techniques:** 
    *   Use of "Instruction Overlapping"
    *   Presence of "Opaque Predicates" (via `POPCOUNT`, `CONCAT31`)
    *   Heavy use of `.Stub.` naming conventions for internal methods.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `method.stub.clientsocket.info`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / backdoor
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Evasion Techniques**: The sample employs sophisticated anti-disassembly methods, including instruction overlapping and opaque predicates (via `POPCOUNT` and `CONCAT31`), to intentionally break automated analysis tools.
    *   **Multi-Stage Architecture**: The use of `.Stub.` naming conventions and a multi-stage loading process indicates the binary is designed to hide its primary payload (the backdoor) until runtime.
    *   **Sophisticated Protective Layers**: The presence of heavy obfuscation and potential professional protectors (like VMProtect or Themida) confirms it is engineered for persistent, high-level threat operations rather than common "commodity" malware.
