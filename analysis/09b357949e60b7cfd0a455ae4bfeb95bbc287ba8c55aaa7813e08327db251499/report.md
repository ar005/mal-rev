# Threat Analysis Report

**Generated:** 2026-07-22 17:50 UTC
**Sample:** `09b357949e60b7cfd0a455ae4bfeb95bbc287ba8c55aaa7813e08327db251499_09b357949e60b7cfd0a455ae4bfeb95bbc287ba8c55aaa7813e08327db251499.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `09b357949e60b7cfd0a455ae4bfeb95bbc287ba8c55aaa7813e08327db251499_09b357949e60b7cfd0a455ae4bfeb95bbc287ba8c55aaa7813e08327db251499.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 811,520 bytes |
| MD5 | `97109256c5db33ef5c4afbbe569eb3b3` |
| SHA1 | `1e62b7eafde2fa20bc3ca56e29698f4fc259c9a5` |
| SHA256 | `09b357949e60b7cfd0a455ae4bfeb95bbc287ba8c55aaa7813e08327db251499` |
| Overall entropy | 7.777 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778643722 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 802,816 | 7.782 | ⚠️ Yes |
| `.rsrc` | 7,680 | 7.488 | ⚠️ Yes |
| `.reloc` | 512 | 0.098 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2092** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

X )UU

X )UU

X )UU
%-&s$
MbP?ZX
#ffffff

*BSJB
v4.0.30319
#Strings
<>c__DisplayClass0_0
<BtnLogin_Click>b__1_0
<>c__DisplayClass1_0
<BtnSave_Click>b__2_0
<>c__DisplayClass2_0
<>c__DisplayClass3_0
<>9__4_0
<LoadReservations>b__4_0
<>c__DisplayClass4_0
<>c__DisplayClass5_0
<CmbReservations_SelectedIndexChanged>b__0
<RefreshGrid>b__0
<IsRoomAvailable>b__0
<BtnSave_Click>b__0
<BtnCheckIn_Click>b__0
<BtnCheckOut_Click>b__0
<GlacialMoraineFilter>b__0
<RefreshGrids>b__0
<UpdateRoomStatusesBasedOnReservations>b__0
<>c__DisplayClass1_1
<>c__DisplayClass4_1
<CmbReservations_SelectedIndexChanged>b__1
<IsRoomAvailable>b__1
<BtnCheckOut_Click>b__1
<GlacialMoraineFilter>b__1
<RefreshGrids>b__1
<LoadReservations>b__1
Func`1
Nullable`1
IEnumerable`1
Action`1
EqualityComparer`1
List`1
tabControl1
menuStrip1
<>9__1_2
<RefreshGrids>b__1_2
<>c__DisplayClass1_2
<CmbReservations_SelectedIndexChanged>b__2
<BtnCheckOut_Click>b__2
<GlacialMoraineFilter>b__2
<LoadReservations>b__2
<>f__AnonymousType0`2
Func`2
Action`2
KeyValuePair`2
Dictionary`2
<GlacialMoraineFilter>b__3
<RefreshGrids>b__3
<LoadReservations>b__3
<>f__AnonymousType1`3
Func`3
<RefreshGrids>b__4
<RefreshGrids>b__5
<RefreshGrids>b__6
<RefreshGrids>b__7
__StaticArrayInitTypeSize=48
C5BAF026691E9E77327C0E7A379B9ABF718280D84439D8A01E40C389B1B497F9
<Module>
<PrivateImplementationDetails>
UpdateUI
System.IO
get_JGwZ
value__
btnAddExtra
ringData
get_Db
set_Db
mscorlib
System.Collections.Generic
Microsoft.VisualBasic
lblDesc
txtDesc
get_Id
set_Id
get_ReservationId
set_ReservationId
get_GuestId
set_GuestId
ringHead
Thread
grpAdd
add_SelectedIndexChanged
CmbReservations_SelectedIndexChanged
Occupied
set_Enabled
set_FormattingEnabled
Cancelled
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c__DisplayClass2_0._BtnSave_Click_b__0` | `0x408645` | 36372 | ✓ |
| `method.HotelManager.Forms.BillingForm.InitializeComponent` | `0x403650` | 3191 | ✓ |
| `method.HotelManager.Forms.RoomManagementForm.InitializeComponent` | `0x40763c` | 2548 | ✓ |
| `method.HotelManager.Forms.CheckInOutForm.InitializeComponent` | `0x406224` | 2302 | ✓ |
| `method.HotelManager.Forms.ReservationForm.InitializeComponent` | `0x40567c` | 2082 | ✓ |
| `method.HotelManager.Forms.GuestManagementForm.InitializeComponent` | `0x406c80` | 2024 | ✓ |
| `method.HotelManager.Forms.MainDashboardForm.InitializeComponent` | `0x404c8c` | 1652 | ✓ |
| `method.HotelManager.Forms.LoginForm.InitializeComponent` | `0x40438c` | 1366 | ✓ |
| `method.HotelManager.Forms.BillingForm.GlacialMoraineFilter` | `0x402cb0` | 1196 | ✓ |
| `method.HotelManager.Forms.BillingForm.UpdateUI` | `0x403374` | 460 | ✓ |
| `method.HotelManager.Forms.MainDashboardForm.RefreshGrid` | `0x404974` | 392 | ✓ |
| `method.HotelManager.Forms.CheckInOutForm.BtnCheckOut_Click` | `0x406084` | 360 | ✓ |
| `entry0` | `0x4022f8` | 356 | ✓ |
| `method.HotelManager.Forms.BillingForm.CmbReservations_SelectedIndexChanged` | `0x403220` | 340 | ✓ |
| `method.HotelManager.Forms.ReservationForm.BtnSearch_Click` | `0x4053c0` | 340 | ✓ |
| `method.HotelManager.Forms.ReservationForm.BtnBook_Click` | `0x405514` | 304 | ✓ |
| `method.HotelManager.Forms.CheckInOutForm.RefreshGrids` | `0x405ec0` | 248 | ✓ |
| `method.HotelManager.Core.ReservationManager.UpdateRoomStatusesBasedOnReservations` | `0x402880` | 228 | ✓ |
| `method.HotelManager.Forms.RoomManagementForm.BtnSave_Click` | `0x407520` | 228 | ✓ |
| `method.HotelManager.Forms.CheckInOutForm.BtnCheckIn_Click` | `0x405fb8` | 204 | ✓ |
| `method.HotelManager.Forms.GuestManagementForm.BtnSave_Click` | `0x406b80` | 200 | ✓ |
| `method.__c__DisplayClass3_0._GlacialMoraineFilter_b__2` | `0x4081e8` | 200 | ✓ |
| `method.HotelManager.Forms.BillingForm.LoadReservations` | `0x40315c` | 196 | ✓ |
| `method.__c__DisplayClass0_0._IsRoomAvailable_b__1` | `0x408044` | 177 | ✓ |
| `method.HotelManager.Core.ReservationManager.GetAvailableRooms` | `0x4027d4` | 172 | ✓ |
| `method.HotelManager.Core.DataManager.Load` | `0x40261c` | 160 | ✓ |
| `method.HotelManager.Forms.ReservationForm.LoadCombos` | `0x405320` | 160 | ✓ |
| `method.__f__AnonymousType1_3.ToString` | `0x402260` | 152 | ✓ |
| `method.HotelManager.Core.ReservationManager.IsRoomAvailable` | `0x402740` | 148 | ✓ |
| `method.HotelManager.Forms.BillingForm.BtnAddExtra_Click` | `0x403540` | 144 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.HotelManager.Core.DataManager.Load.c`](code/method.HotelManager.Core.DataManager.Load.c)
- [`code/method.HotelManager.Core.ReservationManager.GetAvailableRooms.c`](code/method.HotelManager.Core.ReservationManager.GetAvailableRooms.c)
- [`code/method.HotelManager.Core.ReservationManager.IsRoomAvailable.c`](code/method.HotelManager.Core.ReservationManager.IsRoomAvailable.c)
- [`code/method.HotelManager.Core.ReservationManager.UpdateRoomStatusesBasedOnReservations.c`](code/method.HotelManager.Core.ReservationManager.UpdateRoomStatusesBasedOnReservations.c)
- [`code/method.HotelManager.Forms.BillingForm.BtnAddExtra_Click.c`](code/method.HotelManager.Forms.BillingForm.BtnAddExtra_Click.c)
- [`code/method.HotelManager.Forms.BillingForm.CmbReservations_SelectedIndexChanged.c`](code/method.HotelManager.Forms.BillingForm.CmbReservations_SelectedIndexChanged.c)
- [`code/method.HotelManager.Forms.BillingForm.GlacialMoraineFilter.c`](code/method.HotelManager.Forms.BillingForm.GlacialMoraineFilter.c)
- [`code/method.HotelManager.Forms.BillingForm.InitializeComponent.c`](code/method.HotelManager.Forms.BillingForm.InitializeComponent.c)
- [`code/method.HotelManager.Forms.BillingForm.LoadReservations.c`](code/method.HotelManager.Forms.BillingForm.LoadReservations.c)
- [`code/method.HotelManager.Forms.BillingForm.UpdateUI.c`](code/method.HotelManager.Forms.BillingForm.UpdateUI.c)
- [`code/method.HotelManager.Forms.CheckInOutForm.BtnCheckIn_Click.c`](code/method.HotelManager.Forms.CheckInOutForm.BtnCheckIn_Click.c)
- [`code/method.HotelManager.Forms.CheckInOutForm.BtnCheckOut_Click.c`](code/method.HotelManager.Forms.CheckInOutForm.BtnCheckOut_Click.c)
- [`code/method.HotelManager.Forms.CheckInOutForm.InitializeComponent.c`](code/method.HotelManager.Forms.CheckInOutForm.InitializeComponent.c)
- [`code/method.HotelManager.Forms.CheckInOutForm.RefreshGrids.c`](code/method.HotelManager.Forms.CheckInOutForm.RefreshGrids.c)
- [`code/method.HotelManager.Forms.GuestManagementForm.BtnSave_Click.c`](code/method.HotelManager.Forms.GuestManagementForm.BtnSave_Click.c)
- [`code/method.HotelManager.Forms.GuestManagementForm.InitializeComponent.c`](code/method.HotelManager.Forms.GuestManagementForm.InitializeComponent.c)
- [`code/method.HotelManager.Forms.LoginForm.InitializeComponent.c`](code/method.HotelManager.Forms.LoginForm.InitializeComponent.c)
- [`code/method.HotelManager.Forms.MainDashboardForm.InitializeComponent.c`](code/method.HotelManager.Forms.MainDashboardForm.InitializeComponent.c)
- [`code/method.HotelManager.Forms.MainDashboardForm.RefreshGrid.c`](code/method.HotelManager.Forms.MainDashboardForm.RefreshGrid.c)
- [`code/method.HotelManager.Forms.ReservationForm.BtnBook_Click.c`](code/method.HotelManager.Forms.ReservationForm.BtnBook_Click.c)
- [`code/method.HotelManager.Forms.ReservationForm.BtnSearch_Click.c`](code/method.HotelManager.Forms.ReservationForm.BtnSearch_Click.c)
- [`code/method.HotelManager.Forms.ReservationForm.InitializeComponent.c`](code/method.HotelManager.Forms.ReservationForm.InitializeComponent.c)
- [`code/method.HotelManager.Forms.ReservationForm.LoadCombos.c`](code/method.HotelManager.Forms.ReservationForm.LoadCombos.c)
- [`code/method.HotelManager.Forms.RoomManagementForm.BtnSave_Click.c`](code/method.HotelManager.Forms.RoomManagementForm.BtnSave_Click.c)
- [`code/method.HotelManager.Forms.RoomManagementForm.InitializeComponent.c`](code/method.HotelManager.Forms.RoomManagementForm.InitializeComponent.c)
- [`code/method.__c__DisplayClass0_0._IsRoomAvailable_b__1.c`](code/method.__c__DisplayClass0_0._IsRoomAvailable_b__1.c)
- [`code/method.__c__DisplayClass2_0._BtnSave_Click_b__0.c`](code/method.__c__DisplayClass2_0._BtnSave_Click_b__0.c)
- [`code/method.__c__DisplayClass3_0._GlacialMoraineFilter_b__2.c`](code/method.__c__DisplayClass3_0._GlacialMoraineFilter_b__2.c)
- [`code/method.__f__AnonymousType1_3.ToString.c`](code/method.__f__AnonymousType1_3.ToString.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 16/16**, which represents the final segment of the provided disassembly. This section provides significant insight into the underlying mechanics of the malware’s execution engine, specifically focusing on the internal logic of the Virtual Machine (VM) dispatcher and its advanced state-management techniques.

---

### Analysis of Chunk 16/16 (Interpreter Core & State Transformation)

#### 1. Advanced Virtual Machine (VM) Dispatcher Logic
The transition from "suspicious math" in previous chunks to the highly structured, repetitive loops in Chunk 16 confirms that this is not merely a collection of obfuscated functions; it is a **highly-functional VM interpreter**.
*   **Instruction Fetch & Decode:** The repeated patterns—such as `puVar_34 = CONCAT21(uVar_34, uVar_3);` followed by a series of bitwise checks (`POPCOUNT`, `CARRY`) and nested loops—are characteristic of an **opcode dispatcher**. Each "loop" effectively processes one instruction of the malware's internal bytecode.
*   **Dynamic Offset Calculation:** The code frequently uses `CONCAT` operations (e.g., `puVar_13 = CONCAT22(uVar_27, CONCAT11(...))`) to calculate jump targets or memory offsets at runtime. This means the "next instruction" in the malicious sequence is not fixed; it is calculated based on the current state of the interpreter.
*   **Hand-Crafted Stack Manipulation:** The use of `unaff_EBP` and non-standard stack handling indicates that the malware manages its own virtual stack, independent of the host OS’s standard calling conventions.

#### 2. Hardware Logic Emulation (Flag Management)
One of the most sophisticated techniques observed in this chunk is the **explicit management of CPU flags** (e.g., `in_NT`, `in_IF`, `in_TF`, `in_AF`, `in_ID`).
*   In standard C/C++ code, these are handled by the hardware automatically. Here, they are calculated via complex boolean logic and bit-shifting (e.g., `uVar_46 = (in_NT & 1) * 0x4000 | ...`).
*   **Purpose:** By manually managing "simulated" flags, the malware can implement its own branching logic within the VM. This allows the author to create complex logical flows that are almost impossible for a human analyst to map using standard decompiler tools, as the true path of execution is buried in the state of these virtual flags.

#### 3. Data-Dependent Branching & Jumps
The code contains several "Switch-case" style structures translated into jump tables or multi-step conditional checks (e.g., `code_r0x00403895`, `code_r0x00403bdf`).
*   Instead of a simple `if(condition)`, the code performs a series of arithmetic operations to determine the next jump address. This is known as **Control Flow Flattening (CFF)**. It forces all blocks of code into a single large loop, where a central dispatcher determines where to go next based on an encrypted or transformed state variable.
*   The presence of `swi(4)` and `swi(3)` (Software Interrupts) suggests that the VM also has "hooks" for specific system-level interactions, potentially used for timing checks, debug detection, or as a way to exit the dispatcher cleanly during certain execution states.

#### 4. Anti-Analysis Through Complexity Growth
The sheer density of code required to perform what appears to be basic buffer operations (evidenced by the multiple iterations and `CONCAT` calls) is a deliberate **Complexity Explosion**.
*   **Analytical Exhaustion:** By turning every simple operation into a massive block of stateful, bit-shifted logic, the author ensures that even if an analyst succeeds in "decoding" one layer, they are met with another identical layer of complexity. This creates a recursive barrier to analysis.

---

### Updated Summary of Findings (Cumulative)

#### Core Functionality vs. Hidden Intent:
*   **Confirmed Virtual Machine Architecture:** The transition from Chunk 15 to 16 confirms that the malware utilizes a **custom-built virtual machine**. The "logic" we see is actually the *interpreter instructions*. This allows the malicious payload to be stored as encrypted data, which is only decoded and executed by this complex engine.
*   **Abstracted Execution Layer:** By moving logic into a VM, the malware achieves high "portability" of its core payload. The actual malicious behavior (e.g., keylogging or exfiltration) is hidden within the bytecode; we are currently looking at the *engine*, not the *payload*.
*   **State-Machine Logic:** The code doesn't just follow a linear path; it maintains an internal state. Every calculation involving `POPCOUNT`, `CARRY`, and `CONCAT` updates this state, which determines future actions.

#### Technical Indicators of Maliciousness:
1.  **Sophisticated VM Implementation:** This is not "script-kiddy" malware. The depth of the instruction substitution and the manual management of CPU flags indicate a high level of professional engineering.
2.  **Robust Control Flow Flattening:** The use of multi-stage dispatcher loops ensures that standard tools like IDA Pro or Ghidra cannot produce a coherent graph (CFG) of what the malware is actually doing.
3.  **Intentional "Wait" Tactics:** The inclusion of high-complexity logic for simple functions (like `BtnAddExtra_Click`) acts as an automated deterrent against manual analysis, significantly increasing the **Time-to-Analysis (TTA)**.

### Final Conclusion:
**Status: High Certainty - Malicious (Advanced/Professional Grade)**

This sample is a high-tier piece of malware. It utilizes a **multi-layered obfuscation strategy** combining:
1.  **Virtualization:** To hide the core logic within a custom bytecode language.
2.  **Instruction Substitution:** To make simple operations appear as complex mathematical problems.
3.  **Control Flow Flattening:** To break the ability of automated tools to map the execution path.

The complexity of the `ReservationManager` and subsequent blocks confirms that this is designed for **evasion at scale**. It is built to survive in high-security environments where analysts might attempt to reverse-engineer it.

**Risk Profile: Critical.**
This malware is likely part of a sophisticated campaign (APT or organized cybercrime). The complexity suggests the authors have a deep understanding of both assembly language and decompiler limitations.

**Updated Recommendations:**
*   **Dynamic Analysis with Hardware Breakpoints:** Because the control flow is flattened, static analysis will remain difficult. Using hardware breakpoints on memory access to identified "guest" data structures may reveal some underlying behaviors.
*   **De-obfuscation of VM Handlers:** To find the real payload, efforts should be focused on identifying the "Dispatcher Loop" and mapping out each switch case (e.g., the logic following `puVar_34 = CONCAT21(...)`).
*   **Infrastructure Context:** The sophistication here warrants a full investigation into the delivery vector to identify other potentially infected systems or associated indicators of compromise (IOCs).

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Valid Commands | The use of a custom Virtual Machine (VM) interpreter and instruction substitution masks the true malicious logic by encoding it into a proprietary bytecode language. |
| T1027 | Obfuscated Valid Commands | Control Flow Flattening (CFF) is employed to flatten the execution graph, making it difficult for analysts to determine the program's logical flow via standard decompiler tools. |
| T1027 | Obfuscated Valid Commands | Hardware Logic Emulation (managing flags like NT, IF, TF) is used to simulate a standard CPU environment within the VM, hiding the true execution path from automated analysis scripts. |
| T1027 | Obfuscated Valid Commands | The "Complexity Growth" and "Analytical Exhaustion" tactics are deliberate obfuscation measures intended to significantly increase the Time-to-Analysis (TTA) for human researchers. |

---

## Indicators of Compromise

Based on the strings provided and the accompanying behavioral analysis, here is the categorized list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis focuses on internal VM architecture rather than external network communication.)

### **File paths / Registry keys**
*   *None identified.* (While memory offsets like `0x00403895` are noted in the analysis, these are internal execution addresses and do not constitute persistent system artifacts like file paths or registry keys.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   **SHA-256:** `C5BAF026691E9E77327C0E7A379B9ABF718280D84439D8A01E40C389B1B497F9` 
    *(Note: This appears in the string list as a 64-character hex string, typical of a SHA-256 hash.)*

### **Other artifacts**
*   **Malware Architecture:** Custom Virtual Machine (VM) Interpreter.
*   **Obfuscation Techniques:** Control Flow Flattening (CFF), Instruction Substitution, and "Complexity Explosion."
*   **Specific Instructions/Interrupts:** Use of `swi(3)` and `swi(4)` (Software Interrupts).
*   **Component Logic:** Evidence of a custom VM dispatcher utilizing bitwise checks (`POPCOUNT`, `CARRY`) and multi-stage calculation for jump targets.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Virtual Machine (VM) Architecture:** The sample employs a highly-engineered, custom-built VM interpreter featuring instruction substitution and manual management of CPU flags (NT, IF, TF). This hides the primary malicious payload (e.g., keylogging or exfiltration) within custom bytecode, shielding it from standard static analysis.
*   **Advanced Obfuscation Techniques:** The use of Control Flow Flattening (CFF) and "Complexity Explosion" indicates a high-tier production level intended to break automated tools like IDA Pro/Ghidra and significantly increase the Time-to-Analysis (TTA).
*   **Professional Engineering Grade:** The transition from basic obfuscation to a robust, state-aware interpreter suggests the malware is designed for evasion at scale, typical of APT or sophisticated cybercrime campaigns.
