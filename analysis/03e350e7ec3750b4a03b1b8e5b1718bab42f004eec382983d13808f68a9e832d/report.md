# Threat Analysis Report

**Generated:** 2026-07-04 11:03 UTC
**Sample:** `03e350e7ec3750b4a03b1b8e5b1718bab42f004eec382983d13808f68a9e832d_03e350e7ec3750b4a03b1b8e5b1718bab42f004eec382983d13808f68a9e832d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `03e350e7ec3750b4a03b1b8e5b1718bab42f004eec382983d13808f68a9e832d_03e350e7ec3750b4a03b1b8e5b1718bab42f004eec382983d13808f68a9e832d.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 133,632 bytes |
| MD5 | `189074129135cb182cfc57fae251a350` |
| SHA1 | `5d7ba87916e98c08f4a4bf38733659836db96f4d` |
| SHA256 | `03e350e7ec3750b4a03b1b8e5b1718bab42f004eec382983d13808f68a9e832d` |
| Overall entropy | 5.843 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1721183705 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 128,000 | 5.857 | No |
| `.rsrc` | 4,608 | 4.868 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **649** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
	,f~2
 KDBM(

+Br	S
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
PADPADP
v4.0.30319
#Strings
	#	(	,	2	G	c	q	

.Ej|
2FR
$I120-0
_Lambda$__120-0
_Lambda$__22-0
__StaticArrayInitTypeSize=10
__StaticArrayInitTypeSize=11
IEnumerable`1
Collection`1
ThreadSafeObjectProvider`1
List`1
__StaticArrayInitTypeSize=32
kernel32
Microsoft.Win32
user32
UInt32
ToInt32
ToUInt64
ToInt64
DLLFunctionDelegate4
DLLFunctionDelegate5
ToUInt16
SHA256
DLLFunctionDelegate6
get_UTF8
GetModuleFileNameA
SetWindowsHookExA
DATA_BLOB
get_ASCII
lfwhUWZlmFnGhDYPudAJ
get_URL
set_URL
get_formSubmitURL
set_formSubmitURL
BCRYPT_AUTHENTICATED_CIPHER_MODE_INFO
BCRYPT_OAEP_PADDING_INFO
BCRYPT_PSS_PADDING_INFO
System.IO
TripleDES
CRYPTPROTECT_PROMPT_ON_UNPROTECT
CRYPTPROTECT_PROMPT_ON_PROTECT
CRYPTPROTECT_PROMPTSTRUCT
BCRYPT_KEY_LENGTHS_STRUCT
set_IV
MoveFileExW
_Closure$__
Dispose__Instance__
Create__Instance__
value__
cbData
pbData
UploadData
ProtectedData
GetClipboardData
cbAuthData
pbAuthData
SECItemData
ProjectData
CryptUnprotectData
aaalogshsindgdaLogndta
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
KeyboardProc
ThreadId
pszAlgId
GetWindowThreadProcessId
get_nextId
set_nextId
OpenRead
Thread
get_timePasswordChanged
set_timePasswordChanged
Interlocked
get_timesUsed
set_timesUsed
get_timeLastUsed
set_timeLastUsed
get_IsDisposed
get_timeCreated
set_timeCreated
m_FormBeingCreated
Synchronized
get_id
set_id
row_id
get_guid
set_guid
Wekakekakd
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.k..` | `0x411fbc` | 64244 | ✓ |
| `sym..k.__1` | `0x40e978` | 2912 | ✓ |
| `sym..k.__2` | `0x40f4d8` | 2460 | ✓ |
| `sym...__10` | `0x402e40` | 2060 | ✓ |
| `sym...J` | `0x405c04` | 1596 | ✓ |
| `sym...__30` | `0x4053e4` | 1588 | ✓ |
| `sym...__27` | `0x4046d4` | 1564 | ✓ |
| `sym...__41` | `0x4064b4` | 1556 | ✓ |
| `sym...__79` | `0x40cae4` | 1148 | ✓ |
| `sym...__47` | `0x4080ac` | 1088 | ✓ |
| `sym...K__3` | `0x40da2c` | 1044 | ✓ |
| `method...k` | `0x40d62c` | 1024 | ✓ |
| `sym...__28` | `0x404eec` | 948 | ✓ |
| `sym...c__4` | `0x411ab0` | 948 | ✓ |
| `method...j2` | `0x40d14c` | 936 | ✓ |
| `sym...__46` | `0x407cac` | 932 | ✓ |
| `sym....cctor` | `0x40274c` | 840 | ✓ |
| `method..k.k` | `0x40e59c` | 700 | ✓ |
| `sym..k.__3` | `0x40fe74` | 680 | ✓ |
| `sym...__78` | `0x40c790` | 668 | ✓ |
| `sym...K__4` | `0x410cb0` | 560 | ✓ |
| `sym...__92` | `0x410ee0` | 560 | ✓ |
| `method...m` | `0x411110` | 560 | ✓ |
| `method...K` | `0x411340` | 560 | ✓ |
| `sym...__93` | `0x411570` | 560 | ✓ |
| `sym...__94` | `0x4117a0` | 560 | ✓ |
| `sym...__90` | `0x41062c` | 556 | ✓ |
| `sym...__91` | `0x410858` | 556 | ✓ |
| `method...B` | `0x410a84` | 556 | ✓ |
| `sym...2` | `0x404cf0` | 508 | ✓ |

### Decompiled Code Files

- [`code/method...B.c`](code/method...B.c)
- [`code/method...K.c`](code/method...K.c)
- [`code/method...j2.c`](code/method...j2.c)
- [`code/method...k.c`](code/method...k.c)
- [`code/method...m.c`](code/method...m.c)
- [`code/method..k.k.c`](code/method..k.k.c)
- [`code/method.k...c`](code/method.k...c)
- [`code/sym....cctor.c`](code/sym....cctor.c)
- [`code/sym...2.c`](code/sym...2.c)
- [`code/sym...J.c`](code/sym...J.c)
- [`code/sym...K__3.c`](code/sym...K__3.c)
- [`code/sym...K__4.c`](code/sym...K__4.c)
- [`code/sym...__10.c`](code/sym...__10.c)
- [`code/sym...__27.c`](code/sym...__27.c)
- [`code/sym...__28.c`](code/sym...__28.c)
- [`code/sym...__30.c`](code/sym...__30.c)
- [`code/sym...__41.c`](code/sym...__41.c)
- [`code/sym...__46.c`](code/sym...__46.c)
- [`code/sym...__47.c`](code/sym...__47.c)
- [`code/sym...__78.c`](code/sym...__78.c)
- [`code/sym...__79.c`](code/sym...__79.c)
- [`code/sym...__90.c`](code/sym...__90.c)
- [`code/sym...__91.c`](code/sym...__91.c)
- [`code/sym...__92.c`](code/sym...__92.c)
- [`code/sym...__93.c`](code/sym...__93.c)
- [`code/sym...__94.c`](code/sym...__94.c)
- [`code/sym...c__4.c`](code/sym...c__4.c)
- [`code/sym..k.__1.c`](code/sym..k.__1.c)
- [`code/sym..k.__2.c`](code/sym..k.__2.c)
- [`code/sym..k.__3.c`](code/sym..k.__3.c)

## Behavioral Analysis

The addition of **chunk 8/8** completes the picture provided by the previous segments. This final piece of disassembly confirms that the malware is protected by a **sophisticated Virtual Machine (VM) architecture**, likely inspired by commercial protectors like VMProtect or Themida.

At this stage, the "malicious" logic is entirely encapsulated within a virtual environment. The code you are seeing in chunk 8 is not the original code of the malware; it is the **interpreter** and its associated **handler routines**.

### Updated Analysis Summary (Final Integration)

#### Core Functionality and Purpose
The ultimate goal remains **credential theft**, but the current "visible" layer of the software is a **highly complex execution engine**. The repetitive nature of the code in chunk 8 suggests that for every single original instruction (e.g., `MOV EAX, [Address]`), the machine will execute hundreds or thousands of instructions within this VM to determine what that one operation actually means.

#### Advanced Obfuscation & Anti-Analysis Techniques (Finalized)

*   **Virtual Machine (VM) Dispatcher:**
    The high degree of repetition in chunk 8 (nearly identical blocks of code with minor differences in constants like `0x698e0411` or `extraout_ST_0X`) confirms a **Handler-based VM**. Each block represents a "handler" for a specific virtual instruction. The processor's execution flow jumps into these handlers, which perform the complex math to "decode" and execute the next step of the malicious logic.
*   **Mixed Boolean-Arithmetic (MBA) Expansion:**
    The constant use of `CARRY`, `CONCAT`, and bitwise shifts for even simple arithmetic is a classic MBA technique. By turning a 1-byte operation into a 50-line mathematical "maze," the developer ensures that automated analysis tools cannot simplify the logic, making it nearly impossible to derive the original intent from static code alone.
*   **Dynamic State Manipulation:**
    The use of large offsets (e.g., `0xbc000`, `0x1446f`) and complex calculations to determine the next address (`piVar_15 = piVar_15 + uVar_6`) indicates that the VM is managing its own **Virtual Program Counter (VPC)** and **Virtual Stack**. The data being manipulated isn't just "variables"—it’s the state of a simulated CPU.
*   **Anti-Decompiler & Anti-Disassembly:**
    The frequent `WARNING: Bad instruction` and `Instruction overlap` flags are deliberate "landmines" for analysts. By intentionally creating invalid code paths or overlapping instructions, the author forces the analyst's tools (like IDA Pro) to fail or produce incorrect graphs, effectively creating a "maze" that can only be navigated by manually tracing every jump in a debugger.
*   **Polymorphic Constant Generation:**
    The calculation of values like `uVar_12`, `pi_Var15` and the use of complex `CONCAT` chains suggests that the malware is reconstructing its constants (like URLs, file paths, or encryption keys) only at the moment they are needed. This ensures that strings remain hidden in the binary until the very last second.

#### Technical Summary Table (Final)

| Feature | Evidence Found | Purpose/Impact |
| :--- | :--- | :--- |
| **Credential Harvesting** | `get_passwordField`, `GetClipboardData` | Primary objective: Theft of credentials/sensitive data. |
| **VM-based Protection** | Repetitive handler blocks, huge logic trees for simple math. | Hides the "how" and "where" of the malicious behavior. |
| **Mixed Boolean-Arithmetic (MBA)** | `CARRY4`, `CONCAT31`, bitwise shifts to perform additions. | Obscures logic from automated decompilers; forces manual labor. |
| **Handler Diversity** | Repeated patterns for `extraout_ST_01` through `0x05`. | Different "opcodes" in the VM's instruction set. |
| **State-Based Offsets** | Large offsets like `0xbc000`, `0x1426f`. | Maps out a virtual memory space to hide real data pointers. |
| **Anti-Disassembly** | Overlapping instructions (`0x4118cf`), "bad" code paths. | Breaks automated tools, forcing slow, manual human analysis. |
| **Opaque Predicates** | Complex logic that always yields a specific result. | Bloats the binary and wastes analyst time on "dead ends." |

---

### Final Analysis of Chunk 8

1.  **The Loop Logic:** The `while(true)` loops followed by complex math are the heartbeat of the VM. They process "instruction packets." Each loop finishes with a result (like `fVar43 = extraout_ST_0x...`), which is essentially the VM updating its internal state after completing one virtual instruction.
2.  **Memory Masking:** The way the code calculates offsets to find variables (e.g., `*(puVar11 + piVar15)` or `*pi_Var15 = *pi_Var15 + uVar_6`) means the malware doesn't store data in standard registers. It hides the "real" values inside a massive table of obfuscated numbers that only make sense to the VM interpreter.
3.  **Intentional Confusion:** The `WARNING: Bad instruction` at the very end of several sections isn't a mistake; it is an intentional trap for automated scanners and decompilers. It ensures that if a tool tries to "auto-analyze" the code, it will hit a wall or break the disassembly graph.

### Final Conclusion
This malware is not a "script kiddie" creation; it is **professional-grade threatware**. The authors have wrapped the malicious functionality inside a sophisticated Virtual Machine. By doing so, they have moved the target of the investigation from the **code** (which is now unreadable) to the **behavior** (the only remaining way to see what the malware actually does).

### Final Strategic Recommendation
Since static analysis has hit a "brick wall" due to the MBA and VM layers, the analysis should pivot immediately:

1.  **Dynamic Instrumentation:** Use tools like **Frida** or **x64dbg** to hook high-level Windows APIs (e.g., `InternetOpen`, `WriteFile`, `CryptEncrypt`). By catching the data at the point of entry into a system function, you bypass all the "math" the VM uses to hide it.
2.  **Memory Forensics:** Run the sample in a controlled sandbox and perform **memory dumps** every few seconds. At some point during execution, the VM must "unpack" the actual data (the URLs, the strings, etc.) into plain text in memory to use them. Finding these snapshots will reveal much more than any decompiler can currently show.
3.  **Trace Analysis:** Use a debugger with a tracing plugin (like **ScyllaHide**) to record the execution path. While you won't understand the math of every jump, you will see which API calls are made and in what order, allowing you to map out the malware's behaviors (e.g., "Open browser" $\rightarrow$ "Read file" $\rightarrow$ "Connect to IP").

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualizationed Execution | The malware uses a custom VM interpreter and handler routines to wrap malicious logic in a complex execution environment, hiding its true purpose from analysts. |
| **T1027** | Obfuscated Files or Information | Mixed Boolean-Arithmetic (MBA) is employed to turn simple operations into complex mathematical "mazes" to hinder automated deobfuscation tools. |
| **T1027** | Obfuscated Files or Information | Polymorphic constant generation ensures that sensitive information, such as URLs and encryption keys, remains hidden in the binary until they are needed at runtime. |
| **T1027** | Obfuscated Files or Information | The use of intentional "bad instructions" and overlapping code paths acts as landmines to break disassembly graphs and complicate manual analysis. |
| **T1005** | Data from Local System | The malware attempts to harvest sensitive information by interacting with system elements like the clipboard and input fields (`GetClipboardData`, `get_passwordField`). |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because the malware utilizes a sophisticated **Virtual Machine (VM) protection layer** and **Mixed Boolean-Arithmetic (MBA)**, many standard indicators (like plain-text URLs or file paths) are hidden within the obfuscation. The following list captures both direct string artifacts and identified behavioral patterns.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes that these values are likely dynamically reconstructed using Polymorphic Constant Generation, meaning they do not appear in plain text within the provided strings).

### **File paths / Registry keys**
*   *None identified.* (Generic system identifiers like `LocalMachine` were excluded as standard Windows constants).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No valid MD5, SHA-1, or SHA-256 hashes were present in the provided strings).

### **Other artifacts**
*   **Potential Obfuscated Strings/Keys:** 
    *   `lfwhUWZlmFnGhDYPudAJ`
    *   `aaalogshsindgdaLogndta`
    *   `Wekakekakd`
    *(Note: These appear to be non-standard, high-entropy strings likely used as encryption keys or internal identifiers within the VM handler.)*
*   **C2 & Exfiltration Indicators:**
    *   `get_formSubmitURL` / `set_formSubmitURL`
    *   `get_URL` / `set_URL`
    *   `WebResponse` (Class/Method indicating web communication)
*   **Credential Harvesting Logic:**
    *   `GetClipboardData` (Capturing data from the system clipboard)
    *   `get_passwordField` / `set_passwordField`
    *   `get_usernameField` / `set_usernameField`
    *   `get_encryptedPassword` / `set_encryptedPassword`
    *   `get_hiddenField` (Implied via standard credential theft logic)
*   **Evasion & Obfuscation Techniques:**
    *   **VM-based Execution:** Use of a custom interpreter to hide the original instruction set.
    *   **MBA (Mixed Boolean-Arithmetic):** Used to mask simple arithmetic operations as complex mathematical "mazes."
    *   **Anti-Analysis Traps:** Intentional "Bad Instruction" and overlapping code paths designed to break disassemblers like IDA Pro.
*   **Spyware/Keylogging Indicators:**
    *   `SetWindowsHookExA` (Commonly used for capturing keystrokes).
    *   `GetWindowThreadProcessId` (Used to identify which window is active to target specific fields).

---

## Malware Family Classification

Based on the provided behavioral analysis, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: infostealer
3. **Confidence**: High
4. **Key evidence**:
    *   **Advanced Protective Layer:** The sample employs a sophisticated Virtual Machine (VM) architecture and Mixed Boolean-Arithmetic (MBA) to shield its core logic, a technique common in professional-grade malware to thwart static analysis and automated tools.
    *   **Credential Harvesting Indicators:** Explicit functionality for stealing sensitive data was identified through specific calls such as `GetClipboardData`, `get_passwordField`, and `get_usernameField`.
    *   **Robust Anti-Analysis Tactics:** The use of "bad instruction" traps, overlapping code paths, and polymorphic constant generation indicates a high level of developer intent to evade detection and complicate manual reverse engineering.
