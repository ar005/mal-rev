# Threat Analysis Report

**Generated:** 2026-07-19 06:10 UTC
**Sample:** `08da2fefbd4708fce4b5548c044678c468af412c20066840ed816aa5b8bc6a87_08da2fefbd4708fce4b5548c044678c468af412c20066840ed816aa5b8bc6a87.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08da2fefbd4708fce4b5548c044678c468af412c20066840ed816aa5b8bc6a87_08da2fefbd4708fce4b5548c044678c468af412c20066840ed816aa5b8bc6a87.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 118,008 bytes |
| MD5 | `c753860a6ad654da8f4cc05217e0dc6c` |
| SHA1 | `075dd03fbfb8211da9923e2c7ff553d63111596d` |
| SHA256 | `08da2fefbd4708fce4b5548c044678c468af412c20066840ed816aa5b8bc6a87` |
| Overall entropy | 7.229 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3218068125 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 88,064 | 7.044 | ⚠️ Yes |
| `.rsrc` | 16,896 | 7.713 | ⚠️ Yes |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **993** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU

X )UU

X )UU
v4.0.30319
#Strings
	(	8	F	P	^	h	k	z	
<>c__DisplayClass33_0
<RelaunchChrome>b__34_0
<>9__25_0
<ManualFromBase64>b__25_0
<>c__DisplayClass35_0
<OnClosing>b__5_0
<>c__DisplayClass26_0
<.ctor>b__6_0
<>c__DisplayClass27_0
<>c__DisplayClass38_0
<>c__DisplayClass8_0
<StartProgressBar>b__9_0
<>9__0
<PostJsonAsync>b__0
<PerformMerge>b__0
<Scramble>b__0
<Unscramble>b__0
<ExtractFile>b__0
<ShutdownChrome>b__0
<>p__0
<FinishProgressBar>d__11
<InternalPostSend>d__31
__StaticArrayInitTypeSize=51
<>8__1
<>p__1
<>u__1
<>f__AnonymousType0`1
Func`1
Nullable`1
IEnumerable`1
CallSite`1
Task`1
ReadOnlyCollection`1
AsyncTaskMethodBuilder`1
EqualityComparer`1
TaskAwaiter`1
IEnumerator`1
get_Col1
set_Col1
get_Item1
Get_u_x1
<PostDone>d__32
Microsoft.Win32
<appDir>5__2
<httpClient>5__2
<>o__2
<>p__2
<>u__2
Func`2
Tuple`2
Action`2
KeyValuePair`2
Dictionary`2
get_Col2
set_Col2
get_Item2
osv_x2
5A9BD206D4BAA8EE82CA31B227480F98E34BC0F113570A4F4DBE4BBD15151303
__StaticArrayInitTypeSize=53
<zipPath>5__3
<>o__3
<>p__3
Func`3
Action`3
ManualFromBase64
ManualToBase64
<client>5__4
<>o__4
<>p__4
<>f__AnonymousType1`4
Func`4
Action`4
<PostJsonAsync>d__35
<>o__35
B98A42E7E75A66429BF21F48D54033A6083EAF101BD296B5FE5A63134C2B6565
<response>5__5
<>o__5
<>p__5
Action`5
<InitializeAndMerge>d__36
6EED361628C7ED1FE132A21564A37477FF6479E460E0AD7341409019381A6876
<>o__6
<>p__6
Func`6
<InitializedFile>d__37
<FetchUpdatePackage>d__7
<>o__7
<>p__7
<PerformMerge>d__38
get_UTF8
<ExtractFile>d__8
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__f__AnonymousType0_1.get_ID` | `0x402050` | 81566 | ✓ |
| `entry0` | `0x403ee5` | 71700 | ✓ |
| `method.__c__DisplayClass35_0..ctor` | `0x405951` | 58772 | ✓ |
| `method.__ExtractFile_b__0_d.SetStateMachine` | `0x406554` | 47868 | ✓ |
| `method.InitInfo.set_dlbr` | `0x402331` | 2302 | ✓ |
| `method.NotAWordSetup.UnifiedProcessor.DecodeJson` | `0x403599` | 1910 | ✓ |
| `method.NotAWord.SecondPage.set_ExtractionDone` | `0x403113` | 1158 | — |
| `method._FetchUpdatePackage_d__7.MoveNext` | `0x404a54` | 892 | ✓ |
| `method.__c__DisplayClass38_0._PerformMerge_b__0` | `0x405c8c` | 884 | ✓ |
| `method.NotAWord.Helper.CreateDesktopShortcut` | `0x402504` | 864 | ✓ |
| `method.__c__DisplayClass35_0._PostJsonAsync_b__0` | `0x40595c` | 808 | ✓ |
| `method._ExtractFile_d__8.MoveNext` | `0x40475c` | 744 | ✓ |
| `method._InternalPostSend_d__31.MoveNext` | `0x403f78` | 688 | ✓ |
| `method.ComFileOps.ReadAllBytes` | `0x40532c` | 652 | ✓ |
| `method.__f__AnonymousType0_1.GetHashCode` | `0x40209d` | 618 | ✓ |
| `method._PostInit_d__29.MoveNext` | `0x4043ec` | 576 | ✓ |
| `method.ComFileOps.WriteAllBytes` | `0x4055b8` | 468 | ✓ |
| `method._FinishProgressBar_d__11.MoveNext` | `0x404de0` | 424 | ✓ |
| `method._PostDone_d__32.MoveNext` | `0x404238` | 420 | ✓ |
| `method.NotAWordSetup.UnifiedProcessor.ManualFromBase64` | `0x403698` | 416 | ✓ |
| `method.NotAWord.Helper.IsTryableUser` | `0x402990` | 356 | ✓ |
| `method.ComFileOps.ReadAllText` | `0x4051c8` | 356 | ✓ |
| `method._InitializedFile_d__37.MoveNext` | `0x406144` | 356 | ✓ |
| `method.ComFileOps.CopyFile` | `0x405074` | 340 | ✓ |
| `method.NotAWord.MainWindow.ShouldExit` | `0x402fc1` | 330 | ✓ |
| `method._InitializeAndMerge_d__36.MoveNext` | `0x406000` | 308 | ✓ |
| `method.NotAWord.FirstPage.System.Windows.Markup.IComponentConnector.Connect` | `0x402eb8` | 304 | ✓ |
| `method.NotAWord.Helper.RegisterAppInUninstall` | `0x402864` | 268 | ✓ |
| `method.NotAWord.BE_handler.PostSend` | `0x402c2f` | 266 | ✓ |
| `method.NotAWord.FirstPage.Close_Click` | `0x402e79` | 264 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.ComFileOps.CopyFile.c`](code/method.ComFileOps.CopyFile.c)
- [`code/method.ComFileOps.ReadAllBytes.c`](code/method.ComFileOps.ReadAllBytes.c)
- [`code/method.ComFileOps.ReadAllText.c`](code/method.ComFileOps.ReadAllText.c)
- [`code/method.ComFileOps.WriteAllBytes.c`](code/method.ComFileOps.WriteAllBytes.c)
- [`code/method.InitInfo.set_dlbr.c`](code/method.InitInfo.set_dlbr.c)
- [`code/method.NotAWord.BE_handler.PostSend.c`](code/method.NotAWord.BE_handler.PostSend.c)
- [`code/method.NotAWord.FirstPage.Close_Click.c`](code/method.NotAWord.FirstPage.Close_Click.c)
- [`code/method.NotAWord.FirstPage.System.Windows.Markup.IComponentConnector.Connect.c`](code/method.NotAWord.FirstPage.System.Windows.Markup.IComponentConnector.Connect.c)
- [`code/method.NotAWord.Helper.CreateDesktopShortcut.c`](code/method.NotAWord.Helper.CreateDesktopShortcut.c)
- [`code/method.NotAWord.Helper.IsTryableUser.c`](code/method.NotAWord.Helper.IsTryableUser.c)
- [`code/method.NotAWord.Helper.RegisterAppInUninstall.c`](code/method.NotAWord.Helper.RegisterAppInUninstall.c)
- [`code/method.NotAWord.MainWindow.ShouldExit.c`](code/method.NotAWord.MainWindow.ShouldExit.c)
- [`code/method.NotAWordSetup.UnifiedProcessor.DecodeJson.c`](code/method.NotAWordSetup.UnifiedProcessor.DecodeJson.c)
- [`code/method.NotAWordSetup.UnifiedProcessor.ManualFromBase64.c`](code/method.NotAWordSetup.UnifiedProcessor.ManualFromBase64.c)
- [`code/method._ExtractFile_d__8.MoveNext.c`](code/method._ExtractFile_d__8.MoveNext.c)
- [`code/method._FetchUpdatePackage_d__7.MoveNext.c`](code/method._FetchUpdatePackage_d__7.MoveNext.c)
- [`code/method._FinishProgressBar_d__11.MoveNext.c`](code/method._FinishProgressBar_d__11.MoveNext.c)
- [`code/method._InitializeAndMerge_d__36.MoveNext.c`](code/method._InitializeAndMerge_d__36.MoveNext.c)
- [`code/method._InitializedFile_d__37.MoveNext.c`](code/method._InitializedFile_d__37.MoveNext.c)
- [`code/method._InternalPostSend_d__31.MoveNext.c`](code/method._InternalPostSend_d__31.MoveNext.c)
- [`code/method._PostDone_d__32.MoveNext.c`](code/method._PostDone_d__32.MoveNext.c)
- [`code/method._PostInit_d__29.MoveNext.c`](code/method._PostInit_d__29.MoveNext.c)
- [`code/method.__ExtractFile_b__0_d.SetStateMachine.c`](code/method.__ExtractFile_b__0_d.SetStateMachine.c)
- [`code/method.__c__DisplayClass35_0..ctor.c`](code/method.__c__DisplayClass35_0..ctor.c)
- [`code/method.__c__DisplayClass35_0._PostJsonAsync_b__0.c`](code/method.__c__DisplayClass35_0._PostJsonAsync_b__0.c)
- [`code/method.__c__DisplayClass38_0._PerformMerge_b__0.c`](code/method.__c__DisplayClass38_0._PerformMerge_b__0.c)
- [`code/method.__f__AnonymousType0_1.GetHashCode.c`](code/method.__f__AnonymousType0_1.GetHashCode.c)
- [`code/method.__f__AnonymousType0_1.get_ID.c`](code/method.__f__AnonymousType0_1.get_ID.c)

## Behavioral Analysis

Based on the addition of **Chunk 16/16**, the final piece of the provided disassembly, the analysis reaches a definitive conclusion regarding the sophistication of this malware's protection layer.

The inclusion of this final chunk confirms that the complexity is not localized to specific "malicious" functions but is an **architectural constant**. The obfuscation is so thorough that it creates a "seamless wall," where there is no discernible difference between the mechanics of a high-level system call and a low-level UI interaction.

---

### Updated Analysis Summary (Final)
Chunk 16 solidifies the **Gatekeeper** architecture by demonstrating **Extreme Arithmetic Expansion** and **Control Flow Flattening**. The decompiled code shows that every logical transition is buried under layers of `CONCAT`, `CARRY` checks, and bitwise manipulations. This confirms that the malware's "source" code no longer exists in a human-readable form; it has been fully assimilated into a custom Virtual Machine (VM) environment.

A critical finding in this final segment is the **Total Lack of Logical Landmarks**. In standard software, an analyst looks for specific patterns (like a loop for file copying or a string comparison). Here, those markers are replaced by "mathematical noise" that produces the same result but conceives no meaning to a human reader. The use of `LOCK()` and `UNLOCK()` instructions indicates a high level of engineering to ensure that even during heavy de-obfuscation, the code remains stable and thread-safe—a hallmark of **Industrial-Grade Protection**.

---

### Core Functionality (Updated & Finalized)

*   **Arithmetic Expansion as Obfuscation:**
    The sheer density of instructions required to perform a single addition or comparison is staggering. By replacing standard assembly with complex mathematical equivalents, the author ensures that manual analysis of the logic flow becomes mathematically exhausting for a human researcher.
*   **Homogeneous Complexity (The "Universal Layer"):**
    Chunk 16 proves there are no "easy" parts of the code. The uniform complexity across different logical blocks confirms the use of a **Unified Logic Wrapper**. Every instruction is processed by a translation engine that ensures consistency, making it impossible to "skip ahead" to find the payload.
*   **Instruction Substitution & State-Machine Symmetry:**
    The repetition of `POPCOUNT` and bitwise parity checks as gatekeepers for jumps indicates that the malware uses a **State Machine**. The code doesn't check "if the file exists"; it performs 20 calculations to reach a numerical value, then checks if that number is even or odd (via `POPCOUNT`) to decide the next jump.
*   **Anti-Decompilation Tactics:**
    The frequent "Bad instruction" warnings and "Truncated control flow" notes are not accidental. They indicate **Overlapping Instructions** and **Invalid Opcode Insertion**. These are designed to break decompiler logic, making it nearly impossible for automated tools to generate a clean call graph or sense the true entry/exit points of functions.

---

### Sophistication Indicators (Finalized)

#### 1. Industrial-Grade Symmetry
The fact that every function—regardless of its purpose—is wrapped in the exact same "maze" suggests the use of a professional protector (e.g., **VMProtect** or **Themida**). This is not a custom script; it is an engineered protection suite designed to withstand long-term manual analysis.

#### 2. Semantic Erasure
By using `CONCAT`, `CARRY1`, and complex bit-shifting for basic pointer arithmetic, the author has erased the "meaning" of the code. The logic (the *what*) is hidden inside a mathematical shell (the *how*).

#### 3. Execution Stability (Locking Mechanisms)
The inclusion of `LOCK()`/`UNLOCK()` suggests that even in its obfuscated state, the malware is designed to be robust and stable across multi-core systems. This is common in high-end malware where it must remain stable while performing multiple simultaneous tasks (e.g., listening for a command while encrypting files).

#### 4. Tooling-Awareness
The deliberate "noise" and "bad data" sections indicate that the developers are aware of how tools like Hex-Rays or Ghidra work. They have specifically included elements designed to make those tools produce incorrect or incomplete output.

---

### Technical Tactics Identified (Finalized)

*   **Gatekeeper Branching:** Utilizing `POPCOUNT` and bitwise parity as jump conditions instead of standard comparison flags.
*   **Arithmetic Expansion:** Expanding simple operations into multi-step mathematical "hurdles."
*   **State Machine Persistence:** Using internal "Key" constants to gate the flow of a long, automated state sequence.
*   **Instruction Substitution:** Replacing clear assembly with opaque math that achieves the same outcome but obscures intent.
*   **Control Flow Flattening:** Breaking the logic into many small pieces and feeding them into a central dispatcher (the VM engine).

---

### Updated Intelligence for Incident Response

*   **Sophistication Level: Elite.** This is a high-tier, professional protector. Analysis should assume that any manual effort to "read" this code is significantly less efficient than automated methods.
*   **Detection Strategy:**
    1.  **Signature of Symmetry:** Detect the use of **VM_PROTECT** signatures or similar "homogenized complexity." If multiple functions show identical, complex arithmetic logic for simple tasks (like closing a window), flag as high-confidence packed malware.
    2.  **Identify the "Exit Point":** Since static analysis is neutralized by the "maze," focus on **Dynamic Trace Correlation**. Monitor the system for moments where the code leaves the VM environment to call standard Windows APIs (`VirtualAlloc`, `CreateProcess`, etc.). This transition point is usually the only time the "real" logic is visible.
    3.  **Automated De-obfuscation:** Use symbolic execution engines (e.g., **angr**) to "fold" the arithmetic. Because the math always leads to a single result, these tools can simplify hundreds of lines of `CONCAT/CARRY` into a single jump statement.
    4.  **Memory Forensics:** Perform memory dumps during operation. The code may only exist in its "true" form in RAM for a split second before it is re-wrapped or discarded by the VM's handler.

---

### Summary for the Record (Final)
*   **Malware Type:** High-Complexity, Unified-Logic Virtual Machine (VM).
*   **Obfuscation Style:** State Machine Symmetry, Arithmetic Expansion, Instruction Substitution, and Control Flow Flattening.
*   **Critical Observation:** The "maze" is not a perimeter around the payload; it **is** the architecture of the entire application. This creates an extremely high barrier for manual analysis.
*   **Technical Note:** The consistent use of `POPCOUNT` as a branch gate, combined with deliberate anti-decompiler tactics (overlaid instructions/bad data), indicates a professional effort to waste the time and resources of security researchers. Only dynamic analysis or symbolic execution can effectively pierce this layer.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your report to the relevant MITRE ATT&K techniques. The malware utilizes advanced evasion tactics primarily focused on hindering manual analysis and defeating automated decompilation tools through virtualization and complex code obfuscation.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | This encompasses the use of Arithmetic Expansion, Instruction Substitution, Control Flow Flattening, and "mathematical noise" to hide the logic flow from human analysts. |
| **T1055** | Packer | The "Industrial-Grade Protection" (similar to VMProtect) and the migration of code into a custom Virtual Machine (VM) environment indicate the use of packers/protectors to shield functionality. |
| **T1027.002** | (Optional/Note) *Obfuscated Code* | Specifically addresses the "State-Machine Symmetry" and "Gatekeeper Branching" used to hide transition logic from automated analysis tools. |

### Analyst Notes:
*   **Control Flow Flattening & Arithmetic Expansion:** While these are specific programming techniques, in the MITRE ATT&CK framework, they fall under **T1027**. They are intended to make the "source code" unreadable even when successfully decompiled.
*   **Anti-Decompilation Tactics:** The use of "Overlapping Instructions" and "Invalid Opcode Insertion" is a specific implementation of **T1027**, designed specifically to crash or mislead tools like Ghidra or IDA Pro (Hex-Rays).
*   **Virtual Machine Architecture:** Because the malware uses a "Unified Logic Wrapper" where every instruction is processed by a translation engine, it is classified under **T1055**. This tells incident responders that standard static analysis will likely fail, and they should move toward dynamic trace correlation or symbolic execution.

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral reports, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: References to `System.IO` and `Microsoft.Win32` are standard .NET library imports and are not specific file paths or registry keys).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
The following 64-character hex strings were identified within the code logic. In the context of this malware, these likely serve as internal decryption keys, integrity checks, or constants used in the "Arithmetic Expansion" phase of the de-obfuscation process:
*   `5A9BD206D4BAA8EE82CA31B227480F98E34BC0F113570A4F4DBE4BBD15151303`
*   `B98A42E7E75A66429BF21F48D54033A6083EAF101BD296B5FE5A63134C2B6565`
*   `6EED361628C7ED1FE132A21564A37477FF6479E460E0AD7341409019381A6876`
*   `AF7EA99F2A7DE2009FBE4E508E640EE2489D6EBFEA3559BB8FF50F1EA0ADC17D`

### **Other artifacts**
**Malware Infrastructure/Protection Indicators:**
*   **Known Protectors:** Evidence of **VMProtect** or **Themida** (identified by "Industrial-Grade Symmetry" and "Homogeneous Complexity").
*   **Obfuscation Techniques:** 
    *   Control Flow Flattening
    *   Arithmetic Expansion (using `CONCAT`, `CARRY` checks, and bitwise manipulations)
    *   Instruction Substitution (replacing standard instructions with complex mathematical equivalents)
    *   Overlapping Instructions/Invalid Opcode Insertion (to break decompiler logic).

**Behavioral Indicators:**
*   **Control Flow Gatekeeping:** Use of `POPCOUNT` and bitwise parity checks as jump conditions instead of standard comparison flags.
*   **Multi-core Synchronization:** Use of `LOCK()` and `UNLOCK()` instructions to maintain stability during the execution of obfuscated code blocks.
*   **Suspicious Function Names (Internal Logic):**
    *   `FetchUpdatePackage`
    *   `ExtractFile`
    *   `PerformMerge`
    *   `Scramble`/`Unscramble`
    *   `ManualFromBase64` / `ManualToBase64`
    *   `PostJsonAsync` (Potential C2 communication method)

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

**1. Malware family:** Unknown (High-Complexity Protective Wrapper)
**2. Malware type:** Loader / Dropper
**3. Confidence:** High (for Type), Medium (for Family)

**4. Key evidence:**
*   **Payload Delivery Indicators:** The presence of internal function names such as `FetchUpdatePackage`, `ExtractFile`, and `PostJsonAsync` strongly indicates the sample’s primary role is to communicate with a remote server, fetch an additional payload, decrypt/decompress it (`Scramble`/`Unscramble`), and execute it.
*   **Industrial-Grade Obfuscation:** The analysis confirms "Gatekeeper" architecture using Arithmetic Expansion, Control Flow Flattening, and Virtual Machine (VM) translation. This level of protection is designed to shield the core malicious logic from automated detection and manual reverse engineering. 
*   **Sophisticated Infrastructure:** The inclusion of `LOCK()`/`UNLOCK()` instructions for thread safety and a "Unified Logic Wrapper" suggests a highly engineered piece of malware, likely used as a professional-grade entry point (loader) for more complex threats like ransomware or modular RATs.
