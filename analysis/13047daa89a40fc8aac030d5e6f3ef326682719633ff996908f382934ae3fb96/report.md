# Threat Analysis Report

**Generated:** 2026-09-01 21:16 UTC
**Sample:** `13047daa89a40fc8aac030d5e6f3ef326682719633ff996908f382934ae3fb96_13047daa89a40fc8aac030d5e6f3ef326682719633ff996908f382934ae3fb96.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13047daa89a40fc8aac030d5e6f3ef326682719633ff996908f382934ae3fb96_13047daa89a40fc8aac030d5e6f3ef326682719633ff996908f382934ae3fb96.exe` |
| File type | PE32+ executable for MS Windows 6.01 (DLL), x86-64 (stripped to external PDB), 11 sections |
| Size | 2,419,792 bytes |
| MD5 | `8db14e2195be6d828346dc5c9cbc2823` |
| SHA1 | `f3f8d71e4a87023c774d2c4858824e70bf3f54a6` |
| SHA256 | `13047daa89a40fc8aac030d5e6f3ef326682719633ff996908f382934ae3fb96` |
| Overall entropy | 6.811 |
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
| `.text` | 706,560 | 6.275 | No |
| `.data` | 43,008 | 4.377 | No |
| `.rdata` | 1,466,880 | 6.902 | No |
| `.pdata` | 19,456 | 5.241 | No |
| `.xdata` | 2,048 | 3.682 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 1,024 | 4.693 | No |
| `.idata` | 3,584 | 4.041 | No |
| `.CRT` | 512 | 0.259 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 17,408 | 5.409 | No |

### Imports

**KERNEL32.dll**: `AddVectoredContinueHandler`, `AddVectoredExceptionHandler`, `CloseHandle`, `CreateEventA`, `CreateIoCompletionPort`, `CreateThread`, `CreateWaitableTimerExW`, `DeleteCriticalSection`, `DuplicateHandle`, `EnterCriticalSection`, `ExitProcess`, `FreeEnvironmentStringsW`, `GetConsoleMode`, `GetCurrentThreadId`, `GetEnvironmentStringsW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__iob_func`, `_amsg_exit`, `_errno`, `_initterm`, `_lock`, `_unlock`, `abort`, `calloc`, `fputc`, `free`, `fwrite`, `localeconv`, `malloc`

### Exports

`_ctl_parser`, `_nl_expand_alias`, `_nl_msg_cat_cntr`, `bind_textdomain_codeset`, `bindtextdomain`, `dcgettext`, `dcngettext`, `dgettext`, `dngettext`, `gettext`, `libintl_bind_textdomain_codeset`, `libintl_bindtextdomain`, `libintl_dcgettext`, `libintl_dcngettext`, `libintl_dgettext`, `libintl_dngettext`, `libintl_fprintf`, `libintl_fwprintf`, `libintl_gettext`, `libintl_ngettext`, `libintl_printf`, `libintl_set_relocation_prefix`, `libintl_sprintf`, `libintl_swprintf`, `libintl_textdomain`, `libintl_version`, `libintl_vfprintf`, `libintl_vfwprintf`, `libintl_vprintf`, `libintl_vsprintf`, `libintl_vswprintf`, `libintl_vwprintf`, `libintl_wprintf`, `ngettext`, `textdomain`

## Extracted Strings

Total strings found: **9768** (showing first 100)

```
!This program cannot be run in DOS mode.
$
``.data
.rdata
`@.pdata
0@.xdata
0@.bss
.edata
0@.idata
.reloc
AUATUWVSH
([^_]A\A]
([^_]A\A]
([^_]A\A]
AVAUATVSH
 [^A\A]A^
 Go build ID: "THZkodGT-uhI60vdlz_5/GIApjkNf__GhHZ257k58/L80hkid9jcQqnvA-Eou-/irs5wG9Z-hCEzyapgpxI"
 
8cpu.u
UUUUUUUUH!
33333333H!
\$PH9H@v(H
,$M9+t
P(H9S(t
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
runtime L
 error: L
:H9F w
>H+zhH
L$HI9QhuH
D$hH98
P`f9P2tiH
\$0f9C2u
2}#s]H
D$PA)P
N0H9H0tR
\$XHcr
$H+L$HH
T$(H+J
L$(H+A
H9iZ 
H+5GP 

H9Z(w
tX9s(s

\$0H9K
D$pH9H
D$0H9H
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
effffff
J0f9J2vsH
f9K2uQH
D$$u$L
	I9x tE1
ProcessPH
RtlGetVeH
Version
timeBegiH
nPeriod
timeEndPH
dPeriod
runtime.H9
HxM9Hpu
H9T$Xt H
@`H9D$`u
runtime.H9
reflect.H9
D$"\nH
D$ \rH
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
I9N0tfH
T$`Hcc`
L$XHc
|$0uGH
memprofiL9
lerau)f
yteu!H
S89Q8s"H9K
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.main.Generates` | `0x29fa0e5a0` | 10361 | ✓ |
| `sym.runtime.callbackasm.abi0` | `0x29f9f8a40` | 10001 | ✓ |
| `sym.syscall.init` | `0x29f9fe300` | 7589 | ✓ |
| `sym.__gdtoa` | `0x29fa29a10` | 5895 | ✓ |
| `sym.runtime.findRunnable` | `0x29f9c9d80` | 4746 | ✓ |
| `sym.main.Northwest` | `0x29fa0b580` | 4390 | ✓ |
| `sym.main.main` | `0x29fa0a480` | 4351 | ✓ |
| `sym.runtime._sweepLocked_.sweep` | `0x29f9aede0` | 4120 | ✓ |
| `sym.runtime.gcMarkTermination` | `0x29f9a13c0` | 3952 | ✓ |
| `sym.main.Affordable` | `0x29fa095c0` | 3749 | ✓ |
| `sym.runtime.procresize` | `0x29f9cf780` | 3421 | ✓ |
| `sym.runtime.newstack` | `0x29f9d9b60` | 3114 | ✓ |
| `sym.runtime.typesEqual` | `0x29f9ed260` | 2995 | ✓ |
| `sym.runtime._pageAlloc_.find` | `0x29f9b5ee0` | 2894 | ✓ |
| `sym.internal_cpu.doinit` | `0x29f981e20` | 2781 | ✓ |
| `sym.main.Administrators` | `0x29fa0d160` | 2757 | ✓ |
| `sym.main.Developmental` | `0x29fa0c6c0` | 2712 | ✓ |
| `sym.__mingw_pformat` | `0x29fa28e00` | 2471 | ✓ |
| `sym.runtime.schedtrace` | `0x29f9d1ba0` | 2447 | ✓ |
| `sym.runtime.traceAdvance` | `0x29f9f38e0` | 2398 | ✓ |
| `sym.main._nl_msg_cat_cntr.func1` | `0x29fa24240` | 2352 | ✓ |
| `sym.main.libintl_fprintf.func1` | `0x29fa21920` | 2352 | ✓ |
| `sym.main.libintl_sprintf.func1` | `0x29fa20a00` | 2352 | ✓ |
| `sym.main.libintl_vwprintf.func1` | `0x29fa1e0e0` | 2352 | ✓ |
| `sym.main.Programming.func2` | `0x29fa13660` | 2352 | ✓ |
| `sym.main.Administrators.func4` | `0x29fa15140` | 2352 | ✓ |
| `sym.main.Administrators.func5` | `0x29fa15a80` | 2352 | ✓ |
| `sym.main.Administrators.func6` | `0x29fa163c0` | 2352 | ✓ |
| `sym.main.Developmental.func4` | `0x29fa17a00` | 2352 | ✓ |
| `sym.main.Northwest.func2` | `0x29fa18340` | 2352 | ✓ |

### Decompiled Code Files

- [`code/sym.__gdtoa.c`](code/sym.__gdtoa.c)
- [`code/sym.__mingw_pformat.c`](code/sym.__mingw_pformat.c)
- [`code/sym.internal_cpu.doinit.c`](code/sym.internal_cpu.doinit.c)
- [`code/sym.main.Administrators.c`](code/sym.main.Administrators.c)
- [`code/sym.main.Administrators.func4.c`](code/sym.main.Administrators.func4.c)
- [`code/sym.main.Administrators.func5.c`](code/sym.main.Administrators.func5.c)
- [`code/sym.main.Administrators.func6.c`](code/sym.main.Administrators.func6.c)
- [`code/sym.main.Affordable.c`](code/sym.main.Affordable.c)
- [`code/sym.main.Developmental.c`](code/sym.main.Developmental.c)
- [`code/sym.main.Developmental.func4.c`](code/sym.main.Developmental.func4.c)
- [`code/sym.main.Generates.c`](code/sym.main.Generates.c)
- [`code/sym.main.Northwest.c`](code/sym.main.Northwest.c)
- [`code/sym.main.Northwest.func2.c`](code/sym.main.Northwest.func2.c)
- [`code/sym.main.Programming.func2.c`](code/sym.main.Programming.func2.c)
- [`code/sym.main._nl_msg_cat_cntr.func1.c`](code/sym.main._nl_msg_cat_cntr.func1.c)
- [`code/sym.main.libintl_fprintf.func1.c`](code/sym.main.libintl_fprintf.func1.c)
- [`code/sym.main.libintl_sprintf.func1.c`](code/sym.main.libintl_sprintf.func1.c)
- [`code/sym.main.libintl_vwprintf.func1.c`](code/sym.main.libintl_vwprintf.func1.c)
- [`code/sym.main.main.c`](code/sym.main.main.c)
- [`code/sym.runtime._pageAlloc_.find.c`](code/sym.runtime._pageAlloc_.find.c)
- [`code/sym.runtime._sweepLocked_.sweep.c`](code/sym.runtime._sweepLocked_.sweep.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.findRunnable.c`](code/sym.runtime.findRunnable.c)
- [`code/sym.runtime.gcMarkTermination.c`](code/sym.runtime.gcMarkTermination.c)
- [`code/sym.runtime.newstack.c`](code/sym.runtime.newstack.c)
- [`code/sym.runtime.procresize.c`](code/sym.runtime.procresize.c)
- [`code/sym.runtime.schedtrace.c`](code/sym.runtime.schedtrace.c)
- [`code/sym.runtime.traceAdvance.c`](code/sym.runtime.traceAdvance.c)
- [`code/sym.runtime.typesEqual.c`](code/sym.runtime.typesEqual.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)

## Behavioral Analysis

This final analysis incorporates the findings from **Chunk 8/8**, completing the technical picture of the loader's internal logic. This final segment confirms that the malware is not just using standard obfuscation, but a highly sophisticated, state-driven reconstruction engine designed to hide its behavior within the "noise" of the Go runtime.

### Final Cumulative Analysis

#### 1. Multi-Stage & Layered Decryption (Refining "JIT Unpacking")
The final disassembly confirms that the XOR operations are not one-off decryptions but part of a multi-stage process. 
*   **Layered XORing:** The code frequently performs operations like `uVar2 = *(*0x20 + iVar7 + -0x3e3) ^ *(*0x20 + iVar7 + -0x21b)` followed immediately by re-assigning the result. This suggests that data is decrypted in layers; even if an analyst finds one key, there may be another layer of "scrambling" that only becomes clear when the full execution flow is mapped.
*   **Segmented Decoding:** The structure shows distinct loops for different memory segments (the `while` loops counting to 4). This indicates that the loader treats its internal payload as a collection of modules, decrypting each specific module's "header" and "body" just before it is required by the runtime.

#### 2. State-Machine Orchestration
The inclusion of complex conditional jumps (e.g., `if (puVar16 == 0x2)`, `if (puVar16 == 0x3)`) reveals a **state-machine architecture**. 
*   **Execution Path Branching:** Instead of a linear execution path, the loader uses internal state variables to decide which decryption logic or jump table to use. This makes "linear" analysis nearly impossible; an analyst cannot simply read the code from top to bottom because the branch taken depends on dynamically calculated values and previously decrypted keys.
*   **Impact:** This is a deliberate tactic to break automated symbolic execution tools, as the tool must perfectly solve every state calculation to determine which path of the "maze" the malware will actually take.

#### 3. Exploitation of Go Runtime Structures (The "Trojan Horse")
One of the most sophisticated findings in this final chunk is how the loader interacts with internal Go symbols like `mapassign_fast64`.
*   **Object Reconstruction:** After a block of data is XORed, it isn't just left in memory; it is immediately processed into structures that mimic standard Go types. The code at the end (around `code_r0x00029fa18633`) shows the manual construction of internal structs (using offsets like `-0x2ab`, `-0x2a3`).
*   **Significance:** This means the malware is "weaving" its malicious components into the standard Go memory space. By using `mapassign_fast64` and similar functions, it ensures that to an EDR or a manual observer, these operations look like high-frequency internal management tasks of the Go runtime rather than a loader preparing malicious code.

#### 4. "Maze of Constants" as Functional Gatekeepers
The presence of highly specific constants (e.g., `0x29fa18868`, `0x29fa18b9a`) used in jump targets and offsets confirms that the malware is designed to be **self-consistent but opaque**. These aren't random numbers; they are precisely calculated offsets for a custom internal virtual machine or state manager. This ensures that even if a researcher identifies one "gate," they may not realize it leads back into the same core logic used by other functions.

---

### Final Summary for Threat Intelligence (Final Update)

The completion of the disassembly confirms that this loader is a **high-tier, professionalized delivery vehicle** likely associated with an advanced threat actor or sophisticated criminal group. It utilizes a "Defense in Depth" strategy against both automated and human analysis.

**Critical Sophistication Indicators:**

1.  **Automated Code Bloat & Template Generation:** By using nearly identical logic across different "module names," the developers have created a massive, time-consuming surface area for analysts. This dilutes the effort required to analyze the core malicious functionality by burying it in a forest of redundant "junk" code.
2.  **Just-in-Time (JIT) Multi-Layered Unpacking:** The loader avoids staying "naked" in memory. It employs multiple layers of XOR-based decryption, ensuring that the actual malicious payload is only fully decrypted in segments at the very moment it needs to be executed by the Go runtime.
3.  **Runtime Integration & Masking:** By utilizing standard Go internal functions (like `mapassign_fast64`) and mimicking internal Go structures, the loader blends its malicious behavior into the "background noise" of a complex, high-performance language environment. This makes it extremely difficult for heuristic engines to flag the loading process as anomalous.
4.  **Deterministic State Navigation:** The use of a state machine (the `if (puVar16 == ...)` checks) ensures that only the necessary code is "revealed" at any given time, frustrating dynamic analysis and making the path to the payload non-linear.

**Final Conclusion:**
This loader represents an **advanced tier of malware engineering.** It moves beyond simple obfuscation into the realm of **architectural evasion**. It leverages the complexity of Go not just as a language choice, but as a cloak to hide stateful decryption and multi-stage unpacking. It is specifically engineered to defeat signature-based detection (through XOR layering), heuristic analysis (by hiding in standard Go behavior), and manual reverse engineering (via template expansion and "maze" logic).

**Recommendation:**
Detection should focus on the **behavioral artifacts** of the state machine transitions and the specific, repetitive patterns of the multi-layer XOR loops rather than looking for unique strings or static markers, as these have been effectively scrubbed from the binary.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of multi-stage XOR operations and segmented decoding ensures that payload components remain encrypted until the specific moment they are required by the runtime. |
| T1027 | Obfuscated Files or Information | The state-machine architecture and "maze of constants" create a non-linear execution path designed to thwart automated symbolic execution and manual reverse engineering. |
| T1027 | Obfuscated Files or Information | By utilizing standard Go internal functions (e.g., `mapassign_fast64`) and mimicking internal structures, the loader blends its activities into common "noise" to evade heuristic detection. |
| T1027 | Obfuscated Files or Information | The use of automated code bloat and template generation creates a massive, repetitive surface area that complicates analysis by burying malicious logic in voluminous junk code. |

---

## Indicators of Compromise

Based on the provided strings and behavior analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   **Go Build ID:** `THZkodGT-uhI60vdlz_5/GIApjkNf__GhHZ257k58/L80hkid9jcQqnvA-Eou-/irs5wG9Z-hCEzyapgpxI`
    *   *Note: While not a file hash (MD5/SHA), this specific Go build identifier can be used to link different samples compiled from the same source environment.*

### **Other artifacts**
*   **Specific Memory Offsets / Jump Constants:** 
    *   `0x29fa18868`
    *   `0x29fa18b9a`
    *   *(Note: These are identified in the analysis as "Maze of Constants" used for state-machine navigation and jump targets.)*
*   **Specific Code Location:** 
    *   `code_r0x00029fa18633` (Identified as a specific area where internal structures are reconstructed).
*   **Go Runtime Manipulation (Behavioral Signature):**
    *   Use of `mapassign_fast64` and other internal Go symbols to mask malicious memory operations as standard runtime activities.
*   **State-Machine Behavior:** 
    *   Multi-layered XOR logic utilizing specific offsets (e.g., `-0x3e3`, `-0x21b`).
    *   Iterative "while" loops counting to 4 for segment-based decoding.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High (for type) / Medium (for family)
4. **Key evidence**:
    *   **Sophisticated Architectural Evasion:** The use of a state-machine architecture and a "maze of constants" creates non-linear execution paths, specifically designed to thwart automated symbolic execution and frustrate manual reverse engineering.
    *   **Go Runtime Masking:** The loader deliberately blends into the "noise" of the Go runtime by utilizing internal functions (like `mapassign_fast64`) and mimicking internal structures to hide its unpacking activities from heuristic engines.
    *   **Advanced Multi-Stage Unpacking:** Instead of a single decryption step, it uses layered XORing and segment-based decoding to ensure that malicious payloads are only "exposed" in memory at the exact moment they are required for execution.
