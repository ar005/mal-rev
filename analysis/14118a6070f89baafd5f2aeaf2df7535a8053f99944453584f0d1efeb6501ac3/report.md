# Threat Analysis Report

**Generated:** 2026-09-03 22:38 UTC
**Sample:** `14118a6070f89baafd5f2aeaf2df7535a8053f99944453584f0d1efeb6501ac3_14118a6070f89baafd5f2aeaf2df7535a8053f99944453584f0d1efeb6501ac3.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14118a6070f89baafd5f2aeaf2df7535a8053f99944453584f0d1efeb6501ac3_14118a6070f89baafd5f2aeaf2df7535a8053f99944453584f0d1efeb6501ac3.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 396,288 bytes |
| MD5 | `d10a619145bfd62a5f65584b4cbcd033` |
| SHA1 | `984176e90d1358ae9bd5147de4357db2110f6e4e` |
| SHA256 | `14118a6070f89baafd5f2aeaf2df7535a8053f99944453584f0d1efeb6501ac3` |
| Overall entropy | 7.759 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776194342 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 393,728 | 7.775 | ⚠️ Yes |
| `.rsrc` | 1,536 | 3.74 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1468** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
(`e*<~
| 6dda 
 UUUU_
 UUUU_
| 6dda 
 UUUU_
 UUUU_
(
nsD*
| 6dda 
 UUUU_
 UUUU_
&9:`9Y
MIia}`
AY KqE8a}m
'Xda}k
1ZX K
 {11va L
Xe `9I(a}
 625k 
YNea}\
 {11va 
v4.0.30319
#Strings
IfOuYOjl
CompilationRelaxationsAttribute
System.Runtime.CompilerServices
mscorlib
System
Boolean
RuntimeCompatibilityAttribute
SuppressIldasmAttribute
4152e624-8013-420c-a359-384a89915039
IfOuYOjl.exe
<Module>
DynamicDecider
c7etrr8xT5GpJCbQ14.DecisionMaking
Object
<Module>{09D611C0-FB7B-E958-B628-0ADDCF2E3E7D}
ListUser
IfOuYOjl.Collections
ProcessorPredictor
MulticastDelegate
StateStruct
IfOuYOjl.Cryptography
ObjectExecutor
ListSolver
Attribute
ProviderElement`1
UserResponder
AutomatableTransaction
CombinedTemplate
SummarizerAdapter
ValueType
InternalList
AdjustableValidator
UserTracker
TransactionDecider
CustomSummarizer
UserDistributor
InterpreterReceiver
PortableTrackerMode
ValidatorRequester
IfOuYOjl.Validation
ValidatorRecommender
ResourceManager
System.Resources
TrackerSolver
c7etrr8xT5GpJCbQ14.Tracking
GrammarOptions
TransactionNode
<PrivateImplementationDetails>{EA0016C4-44DB-424C-88AE-CA0B93EEAEB9}
__StaticArrayInitTypeSize=12
__StaticArrayInitTypeSize=16
__StaticArrayInitTypeSize=18
__StaticArrayInitTypeSize=22
__StaticArrayInitTypeSize=24
__StaticArrayInitTypeSize=30
__StaticArrayInitTypeSize=32
__StaticArrayInitTypeSize=34
__StaticArrayInitTypeSize=40
__StaticArrayInitTypeSize=64
__StaticArrayInitTypeSize=256
<Module>{bc5f226a-a3aa-4607-9611-acbaa2ce322f}
ThreadEditor
VisibleEditor
AccessibleEditor
IntegratedEditor
ScheduledEditor
EditorParser
DeciderEditor
FinderExplorer
SortedEditor
HiddenEditor
ModularEditor
EditorProfiler
ConcreteEditor
EditorSelector
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.MonitorOrderedTracker` | `0x408d4c` | 14972 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.AttachEncryptor` | `0x40430c` | 13944 | ✓ |
| `method.AlphabeticEditor..cctor` | `0x40ed98` | 12238 | ✓ |
| `method._Module_bc5f226a_a3aa_4607_9611_acbaa2ce322f.p4f2895c48b2147039dd175c808153174` | `0x40d03c` | 5240 | ✓ |
| `entry0` | `0x402278` | 2488 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.EncodeScopeEncryptor` | `0x403c88` | 1652 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.EncryptSequentialEncryptor` | `0x40302c` | 1636 | ✓ |
| `method.IfOuYOjl.Validation.ValidatorRecommender.InternalGetResourceSet` | `0x40881c` | 1292 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.PeekEncryptor` | `0x403770` | 848 | ✓ |
| `method.TransactionNode.TransactAutomatedTransaction` | `0x40cc44` | 808 | ✓ |
| `method.IfOuYOjl.Validation.ValidatorRecommender..cctor` | `0x408540` | 732 | — |
| `method.c7etrr8xT5GpJCbQ14.DecisionMaking.DynamicDecider.DecideDynamicDecider` | `0x40206c` | 524 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.CheckIterableEncryptor` | `0x407984` | 488 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct..cctor` | `0x402eb4` | 372 | ✓ |
| `method.IfOuYOjl.Collections.ListUser.SetupConfigurableAllocator` | `0x402c4c` | 368 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.EncodeConfigurableEncryptor` | `0x407c30` | 304 | ✓ |
| `method.IfOuYOjl.Validation.ValidatorRecommender..ctor` | `0x408488` | 184 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.EncryptEfficientEncryptor` | `0x403ac0` | 148 | ✓ |
| `method.TransactionNode.ManageTransformableTransaction` | `0x40ca40` | 144 | ✓ |
| `method.UserResponder.HandleUser` | `0x408350` | 132 | ✓ |
| `method.TransactionNode.ManageInterruptibleTransaction` | `0x40cb68` | 132 | ✓ |
| `method.IfOuYOjl.Collections.ListUser..cctor` | `0x402e10` | 128 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.EncodeInternalEncryptor` | `0x408054` | 116 | ✓ |
| `method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.RecordVisualTracker` | `0x40c7c8` | 112 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.EncodeMixedEncryptor` | `0x407fd0` | 108 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.InterruptEncryptor` | `0x403c20` | 104 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.ResumeEncryptor` | `0x407e18` | 104 | ✓ |
| `method.TransactionNode.TransactMonoTransaction` | `0x40cf6c` | 104 | ✓ |
| `method.IfOuYOjl.Cryptography.StateStruct.EncodeRandomEncryptor` | `0x407bd0` | 96 | ✓ |
| `method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.RecordCentralTracker` | `0x40c838` | 96 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.AlphabeticEditor..cctor.c`](code/method.AlphabeticEditor..cctor.c)
- [`code/method.IfOuYOjl.Collections.ListUser..cctor.c`](code/method.IfOuYOjl.Collections.ListUser..cctor.c)
- [`code/method.IfOuYOjl.Collections.ListUser.SetupConfigurableAllocator.c`](code/method.IfOuYOjl.Collections.ListUser.SetupConfigurableAllocator.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct..cctor.c`](code/method.IfOuYOjl.Cryptography.StateStruct..cctor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.AttachEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.AttachEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.CheckIterableEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.CheckIterableEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.EncodeConfigurableEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.EncodeConfigurableEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.EncodeInternalEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.EncodeInternalEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.EncodeMixedEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.EncodeMixedEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.EncodeRandomEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.EncodeRandomEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.EncodeScopeEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.EncodeScopeEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.EncryptEfficientEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.EncryptEfficientEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.EncryptSequentialEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.EncryptSequentialEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.InterruptEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.InterruptEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.PeekEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.PeekEncryptor.c)
- [`code/method.IfOuYOjl.Cryptography.StateStruct.ResumeEncryptor.c`](code/method.IfOuYOjl.Cryptography.StateStruct.ResumeEncryptor.c)
- [`code/method.IfOuYOjl.Validation.ValidatorRecommender..ctor.c`](code/method.IfOuYOjl.Validation.ValidatorRecommender..ctor.c)
- [`code/method.IfOuYOjl.Validation.ValidatorRecommender.InternalGetResourceSet.c`](code/method.IfOuYOjl.Validation.ValidatorRecommender.InternalGetResourceSet.c)
- [`code/method.TransactionNode.ManageInterruptibleTransaction.c`](code/method.TransactionNode.ManageInterruptibleTransaction.c)
- [`code/method.TransactionNode.ManageTransformableTransaction.c`](code/method.TransactionNode.ManageTransformableTransaction.c)
- [`code/method.TransactionNode.TransactAutomatedTransaction.c`](code/method.TransactionNode.TransactAutomatedTransaction.c)
- [`code/method.TransactionNode.TransactMonoTransaction.c`](code/method.TransactionNode.TransactMonoTransaction.c)
- [`code/method.UserResponder.HandleUser.c`](code/method.UserResponder.HandleUser.c)
- [`code/method._Module_bc5f226a_a3aa_4607_9611_acbaa2ce322f.p4f2895c48b2147039dd175c808153174.c`](code/method._Module_bc5f226a_a3aa_4607_9611_acbaa2ce322f.p4f2895c48b2147039dd175c808153174.c)
- [`code/method.c7etrr8xT5GpJCbQ14.DecisionMaking.DynamicDecider.DecideDynamicDecider.c`](code/method.c7etrr8xT5GpJCbQ14.DecisionMaking.DynamicDecider.DecideDynamicDecider.c)
- [`code/method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.MonitorOrderedTracker.c`](code/method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.MonitorOrderedTracker.c)
- [`code/method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.RecordCentralTracker.c`](code/method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.RecordCentralTracker.c)
- [`code/method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.RecordVisualTracker.c`](code/method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.RecordVisualTracker.c)

## Behavioral Analysis

This analysis incorporates the final segment of disassembly (**Chunk 3/3**). The addition of this data confirms and reinforces the previous assessments while identifying even more aggressive anti-analysis techniques specifically designed to thwart automated deobfuscation and manual reverse engineering.

The following analysis builds upon the previously identified features: **Multi-stage encryption**, **State-machine communication**, and **Control Flow Flattening**.

### 1. Advanced Anti-Analysis Techniques (Deep Dive)
Chunk 3 provides a clear look at how the author is attempting to "break" the disassembler (e.g., IDA Pro, Ghidra).

*   **Instruction Overlapping & Junk Code:** The recurring `halt_baddata()` warnings and "Bad instruction - Truncating control flow" messages are a major red flag. This indicates that the malware uses **overlapping instructions**. By jumping into the *middle* of what appears to be a multi-byte instruction, the processor executes a different, valid instruction than the one the disassembler displays. This is a deliberate tactic to make static analysis impossible.
*   **Arithmetic Obfuscation (Opaque Predicates):** The code is riddled with complex arithmetic chains (e.g., `puVar15 = CONCAT22(uVar34,CONCAT11(uVar33 | pcVar21[-0x49],uVar30))`). These are often used to calculate values that the analyst expects to be simple constants. Instead of a direct value or an obvious offset, the code forces the decompiler to generate complex logic to reach a single number.
*   **Complex Conditionals for Simple Checks:** Many `if` statements check `SCARRY1`, `CARRY4`, or complex bitwise operations before proceeding. These are likely **Opaque Predicates**—logical checks that always evaluate to true (or false) but are mathematically difficult for a static analysis tool to simplify, forcing an analyst to manually trace every "branch" even when only one is possible at runtime.

### 2. Advanced Logic: The Tracker System
The inclusion of the function `method.c7etrr8xT5GpJCbQ14.Tracking.TrackerSolver.RecordCentralTracker` provides significant insight into the malware's operational goals:

*   **Status Management:** The "Tracker" and "Solver" terminology suggests a management layer. This part of the code likely tracks whether specific tasks (e.g., data exfiltration, file encryption, or module downloading) were successful or failed.
*   **Persistence & Reliability:** Unlike simple malware that performs one action and exits, a "Tracker" system implies a **sophisticated, long-term operation**. It allows the malware to manage its state locally so that if a network connection is dropped, it knows exactly where it left off in its mission once the connection is re-established.
*   **Internal State Synchronization:** This suggests that the "Transaction" logic found in Chunk 2 is the *communication* layer, while the "Tracker" logic in Chunk 3 is the *internal logic* that reconciles those communications with the malware's internal goals.

### 3. Robustness of Control Flow Flattening (CFF)
The repeat occurrence of `DynamicDecider` and `EnsureCustomDecider` confirms that the code has been heavily processed through a "flattener." 
*   In standard code, an `if/else` block looks like a fork in a road. 
*   In this flattened code, all logic is fed into a massive central loop (the decider). The next "block" of code to execute is determined by a variable updated at the end of each segment. This makes it extremely difficult for an analyst to map out the actual logical flow of the program visually in a graph view.

### 4. High-Entropy Data Handling
The use of `CONCAT` and complex bitwise operations (e.g., `puVar10 = CONCAT31(puVar_15 >> 8, ...)` ) suggests that **hardcoded strings or IP addresses are never stored in plaintext.** They are reconstructed piece-by-piece during execution. This is a "lazy" but highly effective way to bypass simple string extraction tools (like `strings` or basic YARA rules).

---

### Final Technical Summary for Incident Response

The final analysis of the provided segments confirms that this is **high-sophistication, professional-grade malware** (likely an APT tool or a high-tier botnet loader). 

1.  **Sophisticated Evasion:** The use of instruction overlapping and opaque predicates indicates the author specifically targets and anticipates use by advanced security researchers.
2.  **Modular Architecture:** The "Transaction" and "Tracker" logic points to a modular framework where the core engine is designed to manage complex tasks over time, likely coordinating multiple functions (e.g., credential theft, secondary payload delivery).
3.  **Persistence of State:** The malware is built to be resilient; it doesn't just perform an action, it *manages* its actions via a state-based system, ensuring that if a process is interrupted or a connection fails, it can resume its task.
4.  **Encryption Diversity:** As established in Chunk 2, the multi-layered encryption approach ensures that even if one "gate" is opened by an analyst, several others remain locked.

**Recommendation:**
*   **Behavioral Analysis:** Because of the heavy packing/obfuscation, static analysis will be extremely time-consuming. Focus on **behavioral monitoring** (e.g., process hollowing, suspicious network heartbeats to non-standard ports).
*   **Memory Forensics:** Since much of the "reconstruction" of data happens in memory during execution, and because it uses complex arithmetic to hide its strings, a memory dump of a running infected process is more likely to yield usable IOCs (IPs, domain names) than static analysis of the file on disk.
*   **Detection Strategy:** Use heuristic-based detection for common "packer" behaviors rather than specific signatures, as the obfuscation logic suggests that each new build of this malware will look significantly different at the binary level while performing the same malicious functions.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of instruction overlapping, junk code, and opaque predicates are designed to thwart static analysis and frustrate de-compilation tools like IDA Pro. |
| T1027 | Obfuscated Files or Information | Control Flow Flattening (CFF) is used to obscure the program's logical flow by routing all execution through a central dispatcher/decider loop. |
| T1027 | Obfuscated Files or Information | The use of complex bitwise operations and `CONCAT` functions to construct strings/IPs at runtime prevents detection via simple string extraction or YARA rules. |
| T1568 | Hide-from-Analysis (Implicit) | While not a single specific sub-technique, the "Tracker" system's state management ensures operational persistence and reliability during multi-stage operations like data exfiltration. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*(None identified. The analysis notes that IPs/URLs are reconstructed piece-by-piece via arithmetic obfuscation to bypass static detection.)*

**File paths / Registry keys**
*   `IfOuYOjl.exe` (Primary executable)
*   `<Module>{09D611C0-FB7B-E958-B628-0ADDCF2E3E7D}` (Internal module identifier)
*   `<Module>{bc5f226a-a3aa-4607-9611-acbaa2ce322f}` (Internal module identifier)

**Mutex names / Named pipes**
*   `m8DE9A20051AFCA5` (Potential mutex or internal hex identifier)
*   `4152e624-8013-420c-a359-384a89915039` (GUID used for internal identification/potential mutex)

**Hashes**
*(No MD5, SHA-1, or SHA-256 hashes were present in the provided text.)*

**Other artifacts**
*   **C2 Patterns:** Use of "Transaction" and "Tracker" logic suggests a state-based communication model designed to resume tasks after failed connections.
*   **Evasion Techniques:** 
    *   Instruction Overlapping (specifically designed to break disassemblers like IDA/Ghidra).
    *   Opaque Predicates (complex arithmetic chains used to hide simple logical branches).
    *   Control Flow Flattening (via `DynamicDecider` and `EnsureCustomDecider`).
*   **Encryption Libraries:** Use of `TripleDES`, `GZipStream`, and `System.Security.Cryptography`.
*   **Obfuscation Logic:** Use of complex bitwise operations and `CONCAT` functions to hide hardcoded strings.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / backdoor
3. **Confidence**: High (regarding capabilities); Medium (regarding specific naming)

4. **Key evidence**:
*   **Sophisticated Obfuscation Architecture:** The use of Control Flow Flattening (CFF), instruction overlapping, and opaque predicates indicates a professional-grade effort to bypass automated deobfuscation tools and thwart manual reverse engineering by analysts.
*   **State-Based Execution Logic:** The "Tracker" and "Transaction" systems confirm the malware is not a simple execution script but a sophisticated agent designed to manage multi-stage operations (e.g., data exfiltration, module downloading) across potentially unstable network connections.
*   **Robust Evasion Techniques:** The reliance on bitwise logic for string construction (`CONCAT`) and multiple encryption layers ensures that critical infrastructure (IPs/Domains) remains hidden from standard static analysis (strings/YARA).
