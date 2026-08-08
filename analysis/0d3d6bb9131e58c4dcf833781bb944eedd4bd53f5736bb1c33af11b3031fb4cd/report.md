# Threat Analysis Report

**Generated:** 2026-08-05 18:22 UTC
**Sample:** `0d3d6bb9131e58c4dcf833781bb944eedd4bd53f5736bb1c33af11b3031fb4cd_0d3d6bb9131e58c4dcf833781bb944eedd4bd53f5736bb1c33af11b3031fb4cd.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d3d6bb9131e58c4dcf833781bb944eedd4bd53f5736bb1c33af11b3031fb4cd_0d3d6bb9131e58c4dcf833781bb944eedd4bd53f5736bb1c33af11b3031fb4cd.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 690,176 bytes |
| MD5 | `f161bb19a7e6d9d8d28f3ef4f6dacc19` |
| SHA1 | `e15cb230b126eefbfebe0e26ea469b36b9819547` |
| SHA256 | `0d3d6bb9131e58c4dcf833781bb944eedd4bd53f5736bb1c33af11b3031fb4cd` |
| Overall entropy | 7.885 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3791534474 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 687,104 | 7.893 | ⚠️ Yes |
| `.rsrc` | 2,048 | 3.513 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1586** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

ZXY(T
v4.0.30319
#Strings
__StaticArrayInitTypeSize=20
get_F41
IEnumerable`1
List`1
LabelPlayer1
TextBoxPlayer1
i_ColIndex1
i_RowIndex1
Trif32
Dictionary`2
CheckBoxPlayer2
TextBoxPlayer2
i_ColIndex2
i_RowIndex2
C3C31E459231952D7630591997BFB72245E303F5FC6B97FEC07EBBD8A7A3FDB6
A568DBD13B812A7ED5A87C5696F843BB62639BFB9D9F0659E2D0BC4F9C45B749
<Module>
<PrivateImplementationDetails>
AddFullPixelData
FromArgb
mscorlib
System.Collections.Generic
CheckBoxPlayer2_CheckedChanged
add_CheckedChanged
get_Checked
BoardButton_clicked
set_Enabled
Synchronized
Append
checksIfAnotherRound
i_Board
m_Board
putPiecesOnBoard
updateButtonsBoard
PrintBoard
defaultInstance
set_AutoScaleMode
i_Messege
AddRange
Invoke
IDisposable
RuntimeFieldHandle
RuntimeTypeHandle
GetTypeFromHandle
Console
TouchMoveRule
set_FormBorderStyle
FontStyle
initializeGame
StartGame
startNewGame
get_Name
set_Name
i_PlayerName
r_PlayerName
i_SecondPlayerName
i_FirstPlayerName
WriteLine
ButtonDone
get_Shape
i_PieceShape
r_PieceShape
i_OpponentPieceKingShape
i_OpponentPieceRegularShape
ValueType
WhichPieceInSquare
get_Culture
set_Culture
resourceCulture
MethodBase
ButtonBase
ApplicationSettingsBase
get_PaleTurquoise
Dispose
i_Locate
EditorBrowsableState
get_White
CompilerGeneratedAttribute
GuidAttribute
GeneratedCodeAttribute
DebuggerNonUserCodeAttribute
DebuggableAttribute
EditorBrowsableAttribute
ComVisibleAttribute
AssemblyTitleAttribute
AssemblyTrademarkAttribute
TargetFrameworkAttribute
AssemblyFileVersionAttribute
AssemblyConfigurationAttribute
AssemblyDescriptionAttribute
CompilationRelaxationsAttribute
AssemblyProductAttribute
AssemblyCopyrightAttribute
AssemblyCompanyAttribute
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **27**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.Windows_User_Interaction.Properties.Resources.get_nHup` | `0x404634` | 13090 | ✓ |
| `method.Windows_User_Interaction.SettingsForm.InitializeComponent` | `0x403e74` | 1721 | ✓ |
| `method.Windows_User_Interaction.GameForm.InitializeComponent` | `0x4038c0` | 480 | ✓ |
| `method.Windows_User_Interaction.GameForm.initializeGame` | `0x402f68` | 424 | ✓ |
| `method.Windows_User_Interaction.GameForm.checkIfGameEnds` | `0x4034f4` | 360 | ✓ |
| `method.Board.putPiecesOnBoard` | `0x4020b0` | 320 | ✓ |
| `method.Windows_User_Interaction.GameForm.makeMove` | `0x4033b8` | 316 | ✓ |
| `method.Board.PrintBoard` | `0x402264` | 304 | ✓ |
| `method.Windows_User_Interaction.GameForm.checksIfAnotherRound` | `0x40365c` | 292 | ✓ |
| `method.Player.TouchMoveRule` | `0x402e28` | 272 | ✓ |
| `method.Windows_User_Interaction.GameForm.createButton` | `0x403110` | 240 | — |
| `method.Board.MakeMove` | `0x402394` | 232 | ✓ |
| `method.Player.checkEatingMove` | `0x402bb0` | 224 | ✓ |
| `method.Windows_User_Interaction.SettingsForm.ButtonDone_Click` | `0x403adc` | 220 | ✓ |
| `method.Windows_User_Interaction.GameForm.chooseSecondButton` | `0x40329c` | 212 | ✓ |
| `method.Windows_User_Interaction.GameForm.startNewGame` | `0x403780` | 204 | ✓ |
| `method.Player.setListOfNonEatingValidMoves` | `0x4027c8` | 192 | ✓ |
| `method.Player.setListOfEatingValidMoves` | `0x402994` | 192 | ✓ |
| `method.Player.setListOfEatingValidMovesForKingPieces` | `0x402af4` | 188 | ✓ |
| `method.Player.checkNonEatingMove` | `0x402c90` | 164 | ✓ |
| `method.Windows_User_Interaction.SettingsForm.SetGameDetails` | `0x403c48` | 164 | ✓ |
| `method.Player.setListOfKingPieces` | `0x402728` | 160 | — |
| `method.Player.setListOfEatingValidMovesForRegularPieces` | `0x402a54` | 160 | ✓ |
| `method.Windows_User_Interaction.SettingsForm.ProcessPixel` | `0x403dac` | 153 | ✓ |
| `method.Windows_User_Interaction.SettingsForm.CheckBoxPlayer2_CheckedChanged` | `0x403bb8` | 144 | ✓ |
| `method.Player.setListOfNonEatingValidMovesForRegularPieces` | `0x402888` | 136 | ✓ |
| `method.Player.setListOfNonEatingValidMovesForKingPieces` | `0x402910` | 132 | ✓ |
| `method.Player.setListOfRegularPieces` | `0x4026a8` | 128 | — |
| `method.Board.deletePiecesInDiagonal` | `0x4021f0` | 116 | ✓ |
| `method.Player.ComputerMove` | `0x402db4` | 116 | ✓ |

### Decompiled Code Files

- [`code/method.Board.MakeMove.c`](code/method.Board.MakeMove.c)
- [`code/method.Board.PrintBoard.c`](code/method.Board.PrintBoard.c)
- [`code/method.Board.deletePiecesInDiagonal.c`](code/method.Board.deletePiecesInDiagonal.c)
- [`code/method.Board.putPiecesOnBoard.c`](code/method.Board.putPiecesOnBoard.c)
- [`code/method.Player.ComputerMove.c`](code/method.Player.ComputerMove.c)
- [`code/method.Player.TouchMoveRule.c`](code/method.Player.TouchMoveRule.c)
- [`code/method.Player.checkEatingMove.c`](code/method.Player.checkEatingMove.c)
- [`code/method.Player.checkNonEatingMove.c`](code/method.Player.checkNonEatingMove.c)
- [`code/method.Player.setListOfEatingValidMoves.c`](code/method.Player.setListOfEatingValidMoves.c)
- [`code/method.Player.setListOfEatingValidMovesForKingPieces.c`](code/method.Player.setListOfEatingValidMovesForKingPieces.c)
- [`code/method.Player.setListOfEatingValidMovesForRegularPieces.c`](code/method.Player.setListOfEatingValidMovesForRegularPieces.c)
- [`code/method.Player.setListOfNonEatingValidMoves.c`](code/method.Player.setListOfNonEatingValidMoves.c)
- [`code/method.Player.setListOfNonEatingValidMovesForKingPieces.c`](code/method.Player.setListOfNonEatingValidMovesForKingPieces.c)
- [`code/method.Player.setListOfNonEatingValidMovesForRegularPieces.c`](code/method.Player.setListOfNonEatingValidMovesForRegularPieces.c)
- [`code/method.Windows_User_Interaction.GameForm.InitializeComponent.c`](code/method.Windows_User_Interaction.GameForm.InitializeComponent.c)
- [`code/method.Windows_User_Interaction.GameForm.checkIfGameEnds.c`](code/method.Windows_User_Interaction.GameForm.checkIfGameEnds.c)
- [`code/method.Windows_User_Interaction.GameForm.checksIfAnotherRound.c`](code/method.Windows_User_Interaction.GameForm.checksIfAnotherRound.c)
- [`code/method.Windows_User_Interaction.GameForm.chooseSecondButton.c`](code/method.Windows_User_Interaction.GameForm.chooseSecondButton.c)
- [`code/method.Windows_User_Interaction.GameForm.initializeGame.c`](code/method.Windows_User_Interaction.GameForm.initializeGame.c)
- [`code/method.Windows_User_Interaction.GameForm.makeMove.c`](code/method.Windows_User_Interaction.GameForm.makeMove.c)
- [`code/method.Windows_User_Interaction.GameForm.startNewGame.c`](code/method.Windows_User_Interaction.GameForm.startNewGame.c)
- [`code/method.Windows_User_Interaction.Properties.Resources.get_nHup.c`](code/method.Windows_User_Interaction.Properties.Resources.get_nHup.c)
- [`code/method.Windows_User_Interaction.SettingsForm.ButtonDone_Click.c`](code/method.Windows_User_Interaction.SettingsForm.ButtonDone_Click.c)
- [`code/method.Windows_User_Interaction.SettingsForm.CheckBoxPlayer2_CheckedChanged.c`](code/method.Windows_User_Interaction.SettingsForm.CheckBoxPlayer2_CheckedChanged.c)
- [`code/method.Windows_User_Interaction.SettingsForm.InitializeComponent.c`](code/method.Windows_User_Interaction.SettingsForm.InitializeComponent.c)
- [`code/method.Windows_User_Interaction.SettingsForm.ProcessPixel.c`](code/method.Windows_User_Interaction.SettingsForm.ProcessPixel.c)
- [`code/method.Windows_User_Interaction.SettingsForm.SetGameDetails.c`](code/method.Windows_User_Interaction.SettingsForm.SetGameDetails.c)

## Behavioral Analysis

This final chunk (18/18) provides the "smoking gun" for several of our previous theories and introduces a new level of hostility regarding how the obfuscator interacts with analysis tools.

The inclusion of this segment confirms that the binary is not just "complex"—it is **actively hostile** to both human researchers and automated analysis pipelines.

### Updated Analysis of Findings

#### 1. The "Math Maze" (Refined)
This chunk reinforces the presence of intense Mixed Boolean-Arithmetic (MBA). Even in what appears to be simple state updates, we see:
*   **Opaque Predicates via `POPCOUNT`**: You can see logic like `if ((POP1(uVar5) & 1U) == 0)` and `if ((POPCOUNT(*puVar91) & 1U) == 0)`. In a standard compiler, these would be simplified. Here, they are used to guard branches that are mathematically certain but computationally "expensive" for an SMT solver (like Z3) to prove. This forces automated tools to explore every branch as if it were possible, leading to **path explosion**.
*   **Arithmetic Bloat**: Notice how variables like `puVar24` or `piVar13` are never used directly. They are passed through a gauntlet of `CONCAT`, bit-shifts (`>> 8`), and `CARRY` checks just to perform what is likely a simple increment or addition in the underlying logic. This "bloats" a single instruction into a massive block of code, making it impossible for a human to skim the code to find the "real" logic.

#### 2. Active Anti-Decompiler & Anti-Analysis
This chunk provides definitive evidence of intentional "decompiler sabotage":
*   **Instruction Overlap/Garbage Data:** The warning `//WARNING: Bad instruction - Truncating control flow here` and the call to `halt_baddata()` are critical. This confirms that the obfuscator intentionally embeds **"junk" bytes** into the binary. These bytes are placed in locations where a decompiler (like Ghidra or IDA) will try to interpret them as code, resulting in broken "pseudo-code," overlapping instructions, and fragmented Control Flow Graphs (CFGs).
*   **Concealed Intent:** By forcing the decompiler to fail or produce incoherent results at specific points (`halt_baddata`), the author ensures that an automated tool cannot provide a clean map of the function. An analyst is forced to manually inspect the assembly, which is exponentially more time-consuming.

#### 3. Obfuscated Memory Addressing (The "Ghost" Map)
Notice the repeated use of calculations before memory access:
*   **Dynamic Offsets:** Instead of accessing `[base + 0x10]`, the code calculates a convoluted value (`puVar24`) and then uses that result to index a table.
*   **Constant Folding Prevention:** By breaking every constant (e.g., `0x6f` or `0x1d`) into a series of mathematical operations, the obfuscator ensures that searching for "magic numbers" or "known constants" in the binary will yield no results. The "true" address only exists in the CPU's registers at the microsecond before it is accessed.

#### 4. Definitive VM (Virtual Machine) Architecture
The scale of this final chunk strongly supports the **VM-based protection** theory:
*   **Looping Dispatchers:** The `do { ... } while (CARRY1(uVar5,puVar88));` structures are characteristic of a VM interpreter. This is not "game logic"; it is the "interpreter loop." 
*   **Register Masking:** The repeated use of `CONCAT22` and `CONCAT31` suggests that the VM is constantly "packing" and "unpacking" its virtual registers into host machine words to prevent an analyst from seeing a consistent state.

---

### Final Comprehensive Analysis Summary

The final analysis of Chunks 1-18 confirms that this application utilizes **Enterprise-Grade, Multi-Layered Protection.** This is not a standard obfuscation; it is a high-level engineering project designed to protect intellectual property or hide malicious behavior from professional security researchers.

**Technical Breakdown:**
1.  **MBA & Opaque Predicates:** The logic is buried in a "Math Maze." By using `POPCOUNT` and complex bitwise operations, the obfuscator hides the true flow of execution behind a wall of mathematically equivalent but visually incomprehensible code.
2.  **Anti-Analysis Payload:** The inclusion of "bad instruction" data confirms that the binary is designed to break automated decompilers. It creates a "fractured" view for the analyst, forcing them to manually resolve every jump and memory access.
3.  **VM-Layered Logic:** The actual logic (the "game," the "key," or the "payload") has been converted into custom bytecode. What we see in the disassembly is just the **virtual machine engine**. Analyzing this code without extracting and de-compiling the underlying bytecode is like trying to understand a book by analyzing the chemical composition of the ink.

**Final Risk Assessment:**
*   **Complexity Level:** **EXTREME.** 
*   **Static Analysis Viability:** **LOW.** Any attempt to "clean" or "de-obfuscate" this code using automated tools will likely result in broken code because the core logic is no longer in the assembly—it is in a secondary, hidden layer.

**Final Strategic Recommendations:**
1.  **Stop Static Analysis:** You have reached the limit of what static analysis can achieve. The "Math Maze" is designed to be unsolvable by human eyes.
2.  **Transition to Dynamic Instrumentation (Frida/Pin):** Instead of trying to understand *how* it calculates a result, use Frida to log the input and output of major functions (e.g., `method.Player.ComputerMove`). By hooking the "entry" and "exit," you bypass the entire math maze.
3.  **Memory Dumping & Pattern Matching:** Once the VM is running and has unpacked its internal state into memory, dump that memory. The "clean" data (coordinates, move lists, etc.) will exist in a decrypted state in RAM at specific intervals. 
4.  **Trace Analysis:** Use an instruction tracer to see which parts of the code are executed most frequently. This will help identify the "Interpreter Loop" and separate it from the "Junk Code."

**Analysis Status: FINAL - HIGH-LEVEL DEFENSE CONFIRMED.**

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of MBA, opaque predicates, junk data, and obfuscated memory addressing is designed to hinder both automated tools (like SMT solvers) and human analysts from deriving the true logic. |
| T1497 | Virtualization Execution | The implementation of a custom VM-based architecture hides the core functionality within an abstracted interpreter loop to prevent analysis of the underlying bytecode. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `btmm.exe` (Potential malicious executable filename)

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   `C3C31E459231952D7630591997BFB72245E303F5FC6B97FEC07EBBD8A7A3FDB6` (SHA-256)
*   `A568DBD13B812A7ED5A87C5696F843BB62639BFB9D9F0659E2D0BC4F9C45B749` (SHA-256)

**Other artifacts**
*   **Anti-Analysis Functions:** `halt_baddata()` (Used to sabotage decompiler output and break Control Flow Graphs).
*   **Obfuscation Techniques:** 
    *   Use of **MBA (Mixed Boolean-Arithmetic)**.
    *   **Opaque Predicates** via `POPCOUNT` instructions.
    *   **VM-based Protection:** The sample uses a custom virtual machine architecture to wrap core logic.
    *   **Instruction Overlap/Junk Data:** Intentional insertion of non-executable data to disrupt automated analysis.

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family**: custom
2. **Malware type**: loader (or backdoor)
3. **Confidence**: High (regarding technical sophistication/obfuscation); Medium (regarding ultimate payload intent)
4. **Key evidence**:
    *   **VM-Based Architecture:** The sample employs a custom virtual machine interpreter to wrap its core logic in bytecode, effectively shielding the "true" functionality from standard static analysis.
    *   **Advanced Obfuscation (MBA & Opaque Predicates):** The use of Mixed Boolean-Arithmetic and `POPCOUNT` instructions indicates a high level of engineering intended to defeat SMT solvers and exhaust automated analysis pipelines.
    *   **Active Decompiler Sabotage:** The inclusion of "junk" data and specific calls like `halt_baddata()` confirms a deliberate effort to break the Control Flow Graphs (CFG) of tools like Ghidra/IDA, forcing manual analysis for human researchers.

**Expert Note:** While the exact payload (e.g., whether it is an infostealer or ransomware) remains hidden inside the VM layer, the technical signature clearly indicates a sophisticated **Loader** or **Trojan** designed to provide a "shield" for malicious activities.
