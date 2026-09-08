# Threat Analysis Report

**Generated:** 2026-09-02 16:12 UTC
**Sample:** `1378230336dacaae827b7b4cc4f26ca444c78fa088871829f031541a4bf706d7_1378230336dacaae827b7b4cc4f26ca444c78fa088871829f031541a4bf706d7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1378230336dacaae827b7b4cc4f26ca444c78fa088871829f031541a4bf706d7_1378230336dacaae827b7b4cc4f26ca444c78fa088871829f031541a4bf706d7.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 6 sections |
| Size | 148,992 bytes |
| MD5 | `391834c89904263ce2abf1cafd036bf0` |
| SHA1 | `aab7d5f5fb2c3405fdfd06b7c7c7532279b1fcc7` |
| SHA256 | `1378230336dacaae827b7b4cc4f26ca444c78fa088871829f031541a4bf706d7` |
| Overall entropy | 7.212 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1662686821 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 97,792 | 6.634 | No |
| `.itext` | 1,536 | 2.934 | No |
| `.rdata` | 1,536 | 3.537 | No |
| `.data` | 40,960 | 7.986 | ⚠️ Yes |
| `.pdata` | 2,048 | 7.899 | ⚠️ Yes |
| `.reloc` | 4,096 | 6.739 | No |

### Imports

**gdi32.dll**: `SetPixel`, `SetDCBrushColor`, `SelectPalette`, `GetTextColor`, `GetDeviceCaps`, `CreateSolidBrush`
**USER32.dll**: `DefWindowProcW`, `CreateMenu`, `EndDialog`, `GetDlgItem`, `GetKeyNameTextW`, `GetMessageW`, `GetWindowTextW`, `IsDlgButtonChecked`, `LoadImageW`, `LoadMenuW`, `DialogBoxParamW`
**KERNEL32.dll**: `SetLastError`, `LoadLibraryW`, `GetTickCount`, `GetLastError`, `GetCommandLineW`, `GetCommandLineA`, `FreeLibrary`

## Extracted Strings

Total strings found: **403** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.itext
`.rdata
@.data
.pdata
.reloc
r;Ew
X_^ZY[
=j&&LZ66lA??~
}{))R>
f""D~**T
V22dN::t
o%%Jr..\$
&&Lj66lZ??~A
99rKJJ
==zGdd
""Df**T~
;22dV::tN



$$Hl\\
C77nYmm
%%Jo..\r
55j_WW
&Lj&6lZ6?~A?
~=zG=d
"Df"*T~*
2dV2:tN:

x%Jo%.\r.
a5j_5W
ggV}++
Lj&&lZ66~A??
bS11*?
Xt,,4.
RRvM;;
MMfU33
PPxD<<%
Bc!! 0
~~zG==
Df""T~**;
dV22tN::
xxJo%%\r..8$
pp|B>>q
aaj_55
UUPx((
cccc||||wwww{{{{
kkkkoooo
gggg++++
YYYYGGGG
&&&&6666????
uuuu				
nnnnZZZZ
RRRR;;;;
[[[[jjjj
9999JJJJLLLLXXXX
CCCCMMMM3333
PPPP<<<<
~~~~====dddd]]]]
ssss````
""""****
^^^^
2222::::



IIII
$$$$\\\\
7777mmmm
llllVVVV
eeeezzzz
xxxx%%%%....
pppp>>>>
ffffHHHH
aaaa5555WWWW
UUUU((((
BBBBhhhhAAAA
='9-6d
_jbF~T
11#?*0
,4$8_@
t\lHBW
QPeA~S
.6$:g

>4$8,@
p\lHtW
+HpXhE
T6$:.

6'9-
d
T[$:.6
RRRR				jjjj
00006666
CCCCDDDD
TTTT{{{{
####====
BBBB
ffff((((
vvvv[[[[
IIIImmmm
%%%%rrrr
]]]]eeee
llllppppHHHHPPPP
FFFFWWWW
kkkk::::
AAAAOOOOgggg
tttt""""
nnnnGGGG
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00419479` | `0x419479` | 2951 | ✓ |
| `fcn.00418496` | `0x418496` | 1870 | ✓ |
| `fcn.00408230` | `0x408230` | 1838 | ✓ |
| `fcn.004150e0` | `0x4150e0` | 1748 | ✓ |
| `fcn.00401a9c` | `0x401a9c` | 1552 | ✓ |
| `fcn.00416688` | `0x416688` | 1332 | ✓ |
| `fcn.00404d08` | `0x404d08` | 1295 | ✓ |
| `fcn.0040cfcc` | `0x40cfcc` | 1251 | ✓ |
| `fcn.004104b4` | `0x4104b4` | 1199 | ✓ |
| `fcn.00405218` | `0x405218` | 1141 | ✓ |
| `fcn.004091c8` | `0x4091c8` | 1120 | ✓ |
| `fcn.0040f82c` | `0x40f82c` | 1113 | ✓ |
| `fcn.004020ac` | `0x4020ac` | 1073 | ✓ |
| `fcn.00409c64` | `0x409c64` | 1070 | ✓ |
| `fcn.004139c4` | `0x4139c4` | 979 | ✓ |
| `fcn.0041205c` | `0x41205c` | 971 | ✓ |
| `fcn.00415d28` | `0x415d28` | 894 | ✓ |
| `fcn.0040fc88` | `0x40fc88` | 888 | ✓ |
| `fcn.00417034` | `0x417034` | 886 | ✓ |
| `fcn.00416124` | `0x416124` | 875 | ✓ |
| `fcn.00410000` | `0x410000` | 821 | ✓ |
| `fcn.0040e8ac` | `0x40e8ac` | 812 | ✓ |
| `fcn.0040ae74` | `0x40ae74` | 775 | ✓ |
| `fcn.00406f48` | `0x406f48` | 758 | ✓ |
| `fcn.00417458` | `0x417458` | 735 | ✓ |
| `fcn.004157b4` | `0x4157b4` | 717 | ✓ |
| `fcn.0040a68c` | `0x40a68c` | 714 | ✓ |
| `fcn.00418083` | `0x418083` | 711 | ✓ |
| `fcn.00415a84` | `0x415a84` | 675 | ✓ |
| `fcn.00417db6` | `0x417db6` | 669 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401a9c.c`](code/fcn.00401a9c.c)
- [`code/fcn.004020ac.c`](code/fcn.004020ac.c)
- [`code/fcn.00404d08.c`](code/fcn.00404d08.c)
- [`code/fcn.00405218.c`](code/fcn.00405218.c)
- [`code/fcn.00406f48.c`](code/fcn.00406f48.c)
- [`code/fcn.00408230.c`](code/fcn.00408230.c)
- [`code/fcn.004091c8.c`](code/fcn.004091c8.c)
- [`code/fcn.00409c64.c`](code/fcn.00409c64.c)
- [`code/fcn.0040a68c.c`](code/fcn.0040a68c.c)
- [`code/fcn.0040ae74.c`](code/fcn.0040ae74.c)
- [`code/fcn.0040cfcc.c`](code/fcn.0040cfcc.c)
- [`code/fcn.0040e8ac.c`](code/fcn.0040e8ac.c)
- [`code/fcn.0040f82c.c`](code/fcn.0040f82c.c)
- [`code/fcn.0040fc88.c`](code/fcn.0040fc88.c)
- [`code/fcn.00410000.c`](code/fcn.00410000.c)
- [`code/fcn.004104b4.c`](code/fcn.004104b4.c)
- [`code/fcn.0041205c.c`](code/fcn.0041205c.c)
- [`code/fcn.004139c4.c`](code/fcn.004139c4.c)
- [`code/fcn.004150e0.c`](code/fcn.004150e0.c)
- [`code/fcn.004157b4.c`](code/fcn.004157b4.c)
- [`code/fcn.00415a84.c`](code/fcn.00415a84.c)
- [`code/fcn.00415d28.c`](code/fcn.00415d28.c)
- [`code/fcn.00416124.c`](code/fcn.00416124.c)
- [`code/fcn.00416688.c`](code/fcn.00416688.c)
- [`code/fcn.00417034.c`](code/fcn.00417034.c)
- [`code/fcn.00417458.c`](code/fcn.00417458.c)
- [`code/fcn.00417db6.c`](code/fcn.00417db6.c)
- [`code/fcn.00418083.c`](code/fcn.00418083.c)
- [`code/fcn.00418496.c`](code/fcn.00418496.c)
- [`code/fcn.00419479.c`](code/fcn.00419479.c)

## Behavioral Analysis

This fourth chunk of disassembly provides the "missing link" between the **raw decryption** of previous stages and the **execution/initialization** of the final malicious payload. While chunks 1-3 focused on how the loader hides data, chunk 4 reveals how the loader reconstructs and prepares that data for use as a functional tool.

### Updated Analysis & New Findings

#### 1. The "Decision Tree" Execution (Advanced Switchboard Logic)
The first large block of code in this chunk is an expansive nested conditional structure.
*   **Observation:** The code evaluates several results from `fcn.00406de8` and performs different actions based on the values returned. For example, it checks if a value is equal to 0, then branches into different paths that define lengths (e.g., `0x17c`, `0x201`, `0x2cf`).
*   **Implication:** This confirms the **Switchboard Architecture**. The loader isn't just one-size-fits-all; it is a "Swiss Army Knife" dropper. Depending on which "branch" the logic takes, it will assemble different features for the attacker—such as switching between a credential stealer, a remote access trojan (RAT), or a secondary downloader.

#### 2. Capability Mapping & Magic Constants
The function `fcn.00417458` is extremely significant for forensic analysis.
*   **Observation:** It contains an extensive list of "Magic Numbers" (e.g., `0x45471d17`, `0x459f1cd7`, `0x69268c17`). Each of these constants acts as a signature for a specific feature or capability.
*   **Implication:** This is **Capability Resolution**. The loader scans the newly unpacked code and looks for these "keys." If it finds one, it triggers a specific initialization routine (like `fcn.0041205c` or `fcn.00416fa0`). This allows the malware to remain modular—only the features "activated" by those specific constants will be enabled in that specific instance of the infection.

#### 3. Dynamic Memory Mapping (The "Shadow IAT")
Function `fcn.00406f48` and portions of `fcn.004157b4` exhibit behaviors typical of **manual API resolving**.
*   **Observation:** These functions loop through data blocks and assign specific offsets to internal structures (e.g., `0x80`, `0xa0`, `0xb8`). 
*   **Implication:** The loader is likely constructing a "Shadow" Import Address Table (IAT). Instead of relying on the Windows loader to link functions, it manually maps the necessary function addresses into its own internal tables. This allows the payload to run without having a suspicious, standard IAT that would alert scanners.

#### 4. State-Dependent Integrity Checks
Function `fcn.0040a68c` contains complex logic involving bitwise comparisons and strict state checks (e.g., checking if `var_314h == 0x5c005c`).
*   **Observation:** This is not just decoding; it's a "sanity check." The loader ensures that the environment, the memory layout, and the integrity of the unpacked buffers are correct before passing control to the final payload.
*   **Implication:** This provides a **protection layer against debuggers.** If an analyst tries to jump into the code prematurely or if they modify a single byte of the decompressed buffer, these "sanity checks" will fail, and the loader will likely crash or enter an infinite loop, effectively stalling the analysis.

---

### Updated Summary Table (Cumulative)

| Feature | Observation | Risk Level | Technical Detail |
| :--- | :--- | :--- | :--- |
| **Payload Type** | **Modular Multi-Stage Loader** | **Critical** | Uses a "Decision Tree" to choose which features/modules to activate at runtime. |
| **Anti-Analysis** | **Dynamic IAT Reconstruction** | **High** | Manually maps function pointers to bypass standard IAT analysis and hide API calls. |
| **Capability Resolution** | **Magic Constant Identification** | **Critical** | Uses a series of "Keys" (e.g., `0x45471d17`) to detect and activate specific malicious functionalities. |
| **Data Obfuscation** | **Advanced Bit-Packing** | **High** | Compresses multiple configuration parameters into single words; only readable after the "Switchboard" passes. |
| **Integrity Check** | **State-Based Verification** | **High** | Validates memory offsets and integrity constants before final execution to deter manual debugging. |

---

### Incident Response & Forensic Notes (Update)

*   **Strategic Behavior:** The analysis confirms that the "payload" is not a single static entity. It is a dynamic assembly of features. **Forensic investigators should expect different capabilities to appear in different infections from the same source.**
*   **Detection Strategy:** Because of the "Switchboard" and "Capability Resolution," traditional YARA rules targeting specific *functions* will likely fail. Instead, look for:
    1.  The **Decision Tree logic** (the repeated `0x406de8` calls).
    2.  The **Magic Constants** found in `fcn.00417458`. These are static values that can be used to identify this specific loader family.
*   **Memory Forensics:** The transition from `fcn.00406f48` to the final execution represents the "Point of No Return." In a memory dump, you should look for **high-entropy buffers being populated with structured data.** Once the "Switchboard" completes its logic, the buffer will transform from "encrypted garbage" to a structured set of instructions and data.
*   **Warning on Triage:** Do not attempt to jump directly into one of the sub-functions (like `0x416fa0`) during live debugging. The complex state machine in `fcn.0040a68c` means that if you skip the "Switchboard" or "Integrity Check," the payload will likely fail to initialize, and you won't see its true behavior.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors in your technical analysis to the corresponding MITRE ATT&CK techniques. 

Most of these behaviors fall under the **Defense Evasion (TA0006)** tactic, specifically utilizing obfuscation to hide intent and hinder manual analysis.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The "Switchboard" logic uses conditional branching to hide the true functionality of the payload until runtime, preventing analysts from identifying the full scope of capabilities. |
| T1027 | Obfuscated Files or Information | The use of "Magic Constants" (e.g., `0x45471d17`) as keys ensures that specific malicious features are only activated if certain conditions are met, masking the intent from static analysis. |
| T1027 | Obfuscated Files or Information | The construction of a "Shadow IAT" via manual API resolution hides the list of imported functions, allowing the code to execute without alerting scanners that look for standard Import Address Table entries. |
| T1027 | Obfuscated Files or Information | State-dependent integrity checks serve as an anti-debugging layer, designed to crash or stall the loader if a researcher attempts to tamper with memory or step through the execution flow. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: As a threat intelligence analyst, I have filtered out standard Windows system files (e.g., `KERNEL32.dll`, `USER32.dll`) and common PE section headers to focus only on actionable intelligence.

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   *None identified in the provided text.*

### **Mutex names / Named pipes**
*   *None identified in the provided text.*

### **Hashes**
*   *No MD5/SHA1/SHA256 hashes were present in the source strings.*

### **Other artifacts (C2 patterns, Magic Constants, & Detection Points)**
These indicators are highly relevant for YARA rule creation and identifying specific "Switchboard" logic within this loader family.

**Capability Resolution "Magic Numbers":**
*   `0x45471d17`
*   `0x459f1cd7`
*   `0x69268c17`
*(Note: These are used by the loader to identify and activate specific malicious modules.)*

**Integrity Check Constants:**
*   `0x5c005c`
*(Note: This is used in state-dependent checks to detect if a debugger or analyst is attempting to modify the buffer.)*

**Internal Function Offsets (Behavioral Signatures):**
The following addresses are key points of interest for memory forensics and automated sandbox analysis:
*   `0x406de8`: Switchboard decision tree logic.
*   `0x417458`: Capability resolution (Magic Number checking).
*   `0x406f48` / `0x4157b4`: Dynamic IAT reconstruction/Mapping.
*   `0x40a68c`: State-based integrity checks.

**Behavioral Note for Detection Logic:**
The presence of GDI functions (`CreateSolidBrush`, `GetDeviceCaps`, `SetPixel`) alongside high-entropy, "garbled" strings suggests the loader uses heavy obfuscation to hide its final payload's graphical or interactive components (e.g., a fake login screen or remote interaction UI).

---

## Malware Family Classification

Based on the behavioral analysis provided, here is the classification of the sample:

1. **Malware family:** Custom (Modular Loader)
2. **Malware type:** Loader / Dropper
3. **Confidence:** High

4. **Key evidence:**
*   **Switchboard Architecture & Capability Resolution:** The use of a "Decision Tree" and specific "Magic Constants" (e.g., `0x45471d17`) indicates the sample is not a single-purpose tool but a modular loader designed to deliver various payloads (RATs, stealers, or secondary downloaders) depending on the configuration found during execution.
*   **Advanced Evasion Techniques:** The implementation of a "Shadow IAT" (manual API resolution) and "State-Dependent Integrity Checks" demonstrates a high level of sophistication intended to bypass automated sandboxes, signature-based detection, and manual reverse engineering.
*   **Multi-Stage Execution:** The analysis highlights that the "payload" is dynamically assembled in memory, meaning the sample serves as a sophisticated wrapper/delivery vehicle for other malicious functionalities rather than being the primary infection tool itself.
