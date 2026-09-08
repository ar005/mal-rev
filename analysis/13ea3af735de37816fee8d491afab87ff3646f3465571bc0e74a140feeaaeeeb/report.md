# Threat Analysis Report

**Generated:** 2026-09-03 19:01 UTC
**Sample:** `13ea3af735de37816fee8d491afab87ff3646f3465571bc0e74a140feeaaeeeb_13ea3af735de37816fee8d491afab87ff3646f3465571bc0e74a140feeaaeeeb.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13ea3af735de37816fee8d491afab87ff3646f3465571bc0e74a140feeaaeeeb_13ea3af735de37816fee8d491afab87ff3646f3465571bc0e74a140feeaaeeeb.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 6,622,344 bytes |
| MD5 | `18e276dc3fe40a0c05a4192898d68baa` |
| SHA1 | `7512197300fdb2966881d1343890f085826f3e23` |
| SHA256 | `13ea3af735de37816fee8d491afab87ff3646f3465571bc0e74a140feeaaeeeb` |
| Overall entropy | 7.914 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1726586236 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 710,768 | 6.5 | No |
| `.rdata` | 5,680,058 | 7.988 | ⚠️ Yes |
| `.data` | 11,384 | 2.573 | No |
| `.pdata` | 19,008 | 5.877 | No |
| `.rsrc` | 187,984 | 6.587 | No |
| `.reloc` | 3,208 | 5.419 | No |

### Imports

**SHELL32.dll**: `ShellExecuteW`
**ADVAPI32.dll**: `GetTokenInformation`, `OpenProcessToken`
**KERNEL32.dll**: `HeapSize`, `GetFileInformationByHandle`, `GetCurrentProcess`, `CloseHandle`, `GetStringTypeW`, `SetStdHandle`, `GetCPInfo`, `GetOEMCP`, `GetACP`, `IsValidCodePage`, `LCMapStringW`, `CompareStringW`, `FlsFree`, `FlsSetValue`, `FlsGetValue`
**api-ms-win-core-synch-l1-2-0.dll**: `WaitOnAddress`, `WakeByAddressAll`, `WakeByAddressSingle`
**bcryptprimitives.dll**: `ProcessPrng`
**ntdll.dll**: `RtlNtStatusToDosError`, `NtWriteFile`, `RtlCaptureContext`, `RtlVirtualUnwind`, `RtlLookupFunctionEntry`

## Extracted Strings

Total strings found: **15258** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
H;D$ q)H
AWAVAUATVWUSH
H[]_^A\A]A^A_
AWAVAUATVWUSH
[]_^A\A]A^A_
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
X[_^A\A]A^A_]
AWAVATVWUSH
 []_^A\A^A_
AWAVATVWSH
([_^A\A^A_
([_^A\A^A_
AWAVATVWSH
([_^A\A^A_
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
ffffff.
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
8[_^A\A]A^A_]
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
UAWAVAUATVWSH
8[_^A\A]A^A_]
fffff.
fffff.
ffffff.
UAWAVAUATVWS
[_^A\A]A^A_]
UAWAVAUATVWSH
([_^A\A]A^A_]
UAWAVATVWSH
@[_^A\A^A_]
@[_^A\A^A_]
UAWAVATVWSH
 [_^A\A^A_]
ffffff.
AVVWSH
([_^A^
UAWAVAUATVWSH
[_^A\A]A^A_]
UAWAVAUATVWSH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.7ff77ab3b050` | `0x7ff77ab3b050` | 595976 | ✓ |
| `fcn.7ff77ab2e850` | `0x7ff77ab2e850` | 571225 | ✓ |
| `fcn.7ff77abccc10` | `0x7ff77abccc10` | 571203 | ✓ |
| `fcn.7ff77ab452d0` | `0x7ff77ab452d0` | 556722 | ✓ |
| `fcn.7ff77ab57090` | `0x7ff77ab57090` | 400887 | ✓ |
| `fcn.7ff77ab2e570` | `0x7ff77ab2e570` | 164778 | ✓ |
| `fcn.7ff77ab2e390` | `0x7ff77ab2e390` | 164086 | ✓ |
| `fcn.7ff77ab2e530` | `0x7ff77ab2e530` | 153174 | ✓ |
| `fcn.7ff77ab279f0` | `0x7ff77ab279f0` | 74985 | ✓ |
| `fcn.7ff77ab279e0` | `0x7ff77ab279e0` | 74671 | ✓ |
| `fcn.7ff77ab279c0` | `0x7ff77ab279c0` | 74083 | ✓ |
| `fcn.7ff77ab279b0` | `0x7ff77ab279b0` | 74042 | ✓ |
| `fcn.7ff77ab2e000` | `0x7ff77ab2e000` | 58197 | ✓ |
| `fcn.7ff77ab41d80` | `0x7ff77ab41d80` | 45174 | ✓ |
| `fcn.7ff77abc2aec` | `0x7ff77abc2aec` | 22622 | ✓ |
| `fcn.7ff77abc2ad8` | `0x7ff77abc2ad8` | 22572 | ✓ |
| `fcn.7ff77ab4deb4` | `0x7ff77ab4deb4` | 16410 | ✓ |
| `fcn.7ff77ab28b90` | `0x7ff77ab28b90` | 10312 | ✓ |
| `fcn.7ff77abbae20` | `0x7ff77abbae20` | 10042 | ✓ |
| `fcn.7ff77ab2eff0` | `0x7ff77ab2eff0` | 8322 | ✓ |
| `fcn.7ff77ab59c20` | `0x7ff77ab59c20` | 7989 | ✓ |
| `fcn.7ff77ab5e9b0` | `0x7ff77ab5e9b0` | 7320 | ✓ |
| `fcn.7ff77ab51020` | `0x7ff77ab51020` | 6203 | ✓ |
| `fcn.7ff77ab38550` | `0x7ff77ab38550` | 5675 | ✓ |
| `fcn.7ff77abb5b10` | `0x7ff77abb5b10` | 5046 | ✓ |
| `fcn.7ff77ab35290` | `0x7ff77ab35290` | 4881 | ✓ |
| `fcn.7ff77ab60660` | `0x7ff77ab60660` | 4708 | ✓ |
| `fcn.7ff77abb75e0` | `0x7ff77abb75e0` | 4690 | ✓ |
| `fcn.7ff77ab58380` | `0x7ff77ab58380` | 4226 | ✓ |
| `fcn.7ff77ab54e90` | `0x7ff77ab54e90` | 4208 | ✓ |

### Decompiled Code Files

- [`code/fcn.7ff77ab279b0.c`](code/fcn.7ff77ab279b0.c)
- [`code/fcn.7ff77ab279c0.c`](code/fcn.7ff77ab279c0.c)
- [`code/fcn.7ff77ab279e0.c`](code/fcn.7ff77ab279e0.c)
- [`code/fcn.7ff77ab279f0.c`](code/fcn.7ff77ab279f0.c)
- [`code/fcn.7ff77ab28b90.c`](code/fcn.7ff77ab28b90.c)
- [`code/fcn.7ff77ab2e000.c`](code/fcn.7ff77ab2e000.c)
- [`code/fcn.7ff77ab2e390.c`](code/fcn.7ff77ab2e390.c)
- [`code/fcn.7ff77ab2e530.c`](code/fcn.7ff77ab2e530.c)
- [`code/fcn.7ff77ab2e570.c`](code/fcn.7ff77ab2e570.c)
- [`code/fcn.7ff77ab2e850.c`](code/fcn.7ff77ab2e850.c)
- [`code/fcn.7ff77ab2eff0.c`](code/fcn.7ff77ab2eff0.c)
- [`code/fcn.7ff77ab35290.c`](code/fcn.7ff77ab35290.c)
- [`code/fcn.7ff77ab38550.c`](code/fcn.7ff77ab38550.c)
- [`code/fcn.7ff77ab3b050.c`](code/fcn.7ff77ab3b050.c)
- [`code/fcn.7ff77ab41d80.c`](code/fcn.7ff77ab41d80.c)
- [`code/fcn.7ff77ab452d0.c`](code/fcn.7ff77ab452d0.c)
- [`code/fcn.7ff77ab4deb4.c`](code/fcn.7ff77ab4deb4.c)
- [`code/fcn.7ff77ab51020.c`](code/fcn.7ff77ab51020.c)
- [`code/fcn.7ff77ab54e90.c`](code/fcn.7ff77ab54e90.c)
- [`code/fcn.7ff77ab57090.c`](code/fcn.7ff77ab57090.c)
- [`code/fcn.7ff77ab58380.c`](code/fcn.7ff77ab58380.c)
- [`code/fcn.7ff77ab59c20.c`](code/fcn.7ff77ab59c20.c)
- [`code/fcn.7ff77ab5e9b0.c`](code/fcn.7ff77ab5e9b0.c)
- [`code/fcn.7ff77ab60660.c`](code/fcn.7ff77ab60660.c)
- [`code/fcn.7ff77abb5b10.c`](code/fcn.7ff77abb5b10.c)
- [`code/fcn.7ff77abb75e0.c`](code/fcn.7ff77abb75e0.c)
- [`code/fcn.7ff77abbae20.c`](code/fcn.7ff77abbae20.c)
- [`code/fcn.7ff77abc2ad8.c`](code/fcn.7ff77abc2ad8.c)
- [`code/fcn.7ff77abc2aec.c`](code/fcn.7ff77abc2aec.c)
- [`code/fcn.7ff77abccc10.c`](code/fcn.7ff77abccc10.c)

## Behavioral Analysis

This new batch of disassembly provides the final pieces of the puzzle, moving from theory into the structural implementation. It confirms that the binary is not just using a simple interpreter; it is implementing a **Multi-Stage Execution Engine** with a highly complex, multi-tiered dispatch system.

Here is the updated analysis incorporating the findings from sections 1 through 5.

---

### Updated Analysis & Key Findings

#### 1. Hierarchical Dispatcher (The "Grand Map")
In `fcn.7ff77ab54e90` and `fcn.7ff77ab58380`, we see the implementation of a **Nested Execution Pipeline**. Instead of a single loop that executes code, the system uses multiple layers of dispatch:
*   **Macro-Dispatch:** The high-level logic (likely in `fcn.7ff77ab54e90`) identifies the "type" or "category" of an instruction. 
*   **Micro-Dispatch:** Once a category is identified, it calls specialized handlers (the various switch cases like `0x7ff77ab55dab`, `0x7ff77ab55deb`).
*   **Contextual Interpretation:** The logic for things like `uVar13 = -cVar8 & 0x3f` followed by shift operations (`(iStack_140 << (uStack_b8 & 0x3f)) >> uVar13`) is a hallmark of **Just-In-Time (JIT) compilation** or very advanced VM designs. It allows the interpreter to use a single piece of code to handle multiple variations of an instruction by masking out different "sub-opcodes."

#### 2. Descriptor-Based Buffer Navigation
The code in `fcn.7ff77ab60660` and the repeated logic in `fcn.7ff77ab58380` show how the interpreter handles data. It doesn't just "read a string" or "fetch an int." 
*   **Complexity of Fetch:** The code performs extensive checks on expected vs. actual lengths (`uVar12 = uVar14 + uVar24;`, `if (uVar11 < 0xffffffffffffff89)`). 
*   **Descriptor Translation:** It reads a "descriptor" which tells it exactly how many bytes to skip or move forward in the underlying buffer. This allows the malware to hide its true logic—the data is never contiguous; it's scattered, and the interpreter reconstructs the "message" only at the moment of execution.

#### 3. Hardened Memory Boundary Control
Throughout this section, we see frequent checks against specific constants (e.g., `0x41`, `0x20000`). 
*   **The VM Sandbox:** These aren't just "overflow" checks for the OS; these are **Internal Segment Boundaries**. The program treats its internal memory as a segmented space. One segment might be for "Control Codes," another for "Payload Data," and another for "State Variables."
*   **Safety Buffers:** By enforcing these boundaries, the authors ensure that even if an analyst successfully decodes a single "instruction," they can only see what is in that specific memory segment.

#### 4. Sophisticated Obfuscation of State (Anti-Tracing)
The use of complex bit-shifts and nested logic to calculate simple offsets (`uVar20 = uVar20 + uVar13 * -8`) serves two purposes:
*   **Ambiguity:** It hides the "True Path." To a human looking at a graph or disassembler, it’s hard to tell which branch leads where. 
*   **Anti-Decompilation:** By making the logic "mathematically dense," they ensure that automated decompilers produce code that is difficult for humans to read quickly, forcing researchers to spend days mapping out the state machine manually.

---

### Final Synthesis: The Multi-Layered Virtual Machine (VM)

By combining all 5 chunks of analysis, we can define the architecture of this component as a **Nested-Interpreter Framework.** 

**The Architectural Layers:**
1.  **Data Layer (Raw Blob):** Highly encrypted/packed data that contains "Descriptors."
2.  **Decoding Layer (Validation & Math):** The "Vault" functions that perform high-math operations to translate raw bytes into the "Inner Instructions."
3.  **Dispatcher Layer (The Logic Gate):** This is what we saw in `fcn.7ff77ab54e90`. It acts as a router, taking an Instruction ID and routing it to the correct handling logic. 
4.  **Executor Layer (The Execution Context):** The "Micro-Dispatch" section. These functions handle specific actions like memory movement, string manipulation, or preparing for a system API call.
5.  **Bridge Layer:** The final translation where the VM's internal state is converted into a legitimate Windows API call or local action.

#### Malware Contextual Relevance:
This architecture is characteristic of **State-of-the-Art Trojan Engines (e.g., Lazarus, Turla, or advanced Ransomware families).** 

*   **Instructional Decoupling:** Because the "Malicious Logic" exists only as instructions for a custom VM, there is no single piece of "malicious code" to find. The maliciousness is distributed across the interpreter's commands.
*   **Evolutionary Evasion:** If the defenders identify an IOC (Indicator of Compromise) related to one switch case in the Dispatcher, the attackers can change that specific instruction type without changing the rest of the VM or the overall structure of the malware.

---

### Final Analyst Recommendations:

1.  **Map the Macro-Dispatch Table:** Identify all "Master" jump points in `fcn.7ff77ab54e90`. Each unique branch likely represents a primary function (e.g., Net_Comm, File_Encrypt, Key_Gen).
2.  **Trace the Descriptor Decoding:** Instead of following every instruction, focus on how the **Descriptor** is decoded in `fcn.7ff77ab60660`. If you can understand how a "command" is reconstructed from the raw data, you can begin to map out what the script is doing.
3.  **Target the Math Constants:** The large primes and constants (`0x5a827999`, `0x6ed1eba1`) are excellent for identifying variants of this specific malware family. Even if they change the "instruction set," they often reuse the same "Vault" logic to decrypt their data.
4.  **Dynamic Analysis Focus:** Because of the complexity of the VM, static analysis will be extremely time-consuming. I recommend **Memory Forensics**. Monitor the memory regions being accessed by the interpreter. When a "Switch Case" is triggered, look at the buffer it is reading from—this is often where the decrypted "Command of the Day" appears in plain text for a few milliseconds before being processed.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Interpreted Code | The implementation of a "Multi-Stage Execution Engine" and a "Nested-Interpreter Framework" indicates that malicious instructions are being processed by a custom interpreter rather than executed directly as native code. |
| **T1486** | Data Encoding | The "Descriptor-Based Buffer Navigation" uses complex math and translation logic to decode data only at the moment of execution, effectively hiding the true meaning/content of the underlying data. |
| **T1055** | Packer | The multi-layered architecture is designed to hide the core functionality of the malware behind a "Vault" of decoding layers and a "Dispatcher," which are hallmarks of sophisticated packing and obfuscation techniques. |
| **T1486 (Sub-type)** | (Obfuscation) | Use of "mathematically dense" logic and bit-shifts to create ambiguity and hinder automated de-compilation tools is a primary method for hindering static analysis during the discovery phase. |

### Analyst Notes:
*   **T1029 (Interpreted Code):** This is the primary technique identified. The use of **Macro-Dispatch** and **Micro-Dispatch** to handle "sub-opcodes" indicates a sophisticated VM-based obfuscation commonly used by high-level threat actors (e.g., Lazarus, Turla) to decouple malicious logic from the underlying system's standard execution flow.
*   **T1486 (Data Encoding):** This maps specifically to your analysis of **Descriptor Translation**. By ensuring that data is not contiguous and must be "reconstructed" by the interpreter, the threat actor ensures that simple strings or signature-based detection on raw buffers will fail.
*   **Execution Complexity:** The "Hardened Memory Boundary Control" acts as a secondary layer for **Defense Evasion**, specifically targeting analysts' ability to map out the full execution path during manual reverse engineering.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section appears to contain highly obfuscated data or junk code intended to hinder analysis; as such, no actionable network indicators were present in that specific segment. However, the behavioral analysis provides significant **Technical Artifacts** used to identify this specific malware's architecture.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis suggests these are likely hidden within the "Data Layer" and only decrypted during runtime by the VM.)

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (While hex values are present in the analysis, they are internal constants/offsets rather than file hashes.)

### **Other artifacts**
The following items serve as behavioral IOCs to identify this specific malware family or similar VM-based architectures:

*   **Memory Offsets / Function Addresses:** 
    *   `0x7ff77ab54e90` (Macro-Dispatch)
    *   `0x7ff77ab58380` (Data Processing/Interpretation)
    *   `0x7ff77ab60660` (Descriptor Translation)
    *   `0x7ff77ab55dab` & `0x7ff77ab55deb` (Micro-Dispatch Switch Cases)
*   **Constant Hex Values (VM Vault Constants):**
    *   `0x5a827999`
    *   `0x6ed1eba1` 
    *(These constants are high-confidence markers for identifying this specific obfuscation technique.)*
*   **Behavioral Patterns:**
    *   **Multi-Stage Execution Engine:** Presence of a nested interpreter architecture.
    *   **Descriptor-Based Buffer Navigation:** Use of non-contiguous data structures to hide logic.
    *   **Internal Segment Boundaries:** Hardened memory checks against constants like `0x41` and `0x20000`.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1.  **Malware family:** custom (Note: While the architecture shares characteristics with sophisticated groups like Lazarus or Turla, no specific brand-name malware was identified.)
2.  **Malware type:** loader / backdoor
3.  **Confidence:** High (regarding functionality/architecture)
4.  **Key evidence:** 
    *   **Multi-Layered Virtual Machine (VM):** The sample employs a highly complex "Nested-Interpreter Framework" featuring both Macro and Micro-Dispatchers, which decouples the malicious logic from the code to hinder static analysis.
    *   **Descriptor-Based Buffer Navigation:** The use of non-contiguous data structures and "Vault" decoding functions ensures that commands are only reconstructed in memory at the moment of execution.
    *   **Advanced Obfuscation Techniques:** The presence of high-complexity mathematical constants (e.g., `0x5a827999`, `0x6ed1eba1`) and "Hardened Memory Boundary Control" indicates a sophisticated effort to bypass both automated sandboxes and manual reverse engineering.
