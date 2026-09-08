# Threat Analysis Report

**Generated:** 2026-09-02 16:03 UTC
**Sample:** `137326ac5fc9563532826dccf4442886bef1ec94a41654b9cbb6c963d78a35d2_137326ac5fc9563532826dccf4442886bef1ec94a41654b9cbb6c963d78a35d2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `137326ac5fc9563532826dccf4442886bef1ec94a41654b9cbb6c963d78a35d2_137326ac5fc9563532826dccf4442886bef1ec94a41654b9cbb6c963d78a35d2.exe` |
| File type | PE32+ executable for MS Windows 6.01 (DLL), x86-64, 19 sections |
| Size | 11,175,320 bytes |
| MD5 | `b3d8a3d3b59bfe7ff75919be2a0b9a05` |
| SHA1 | `6c908e921ecb2f9e23ae89efbb35275aaa4e46b4` |
| SHA256 | `137326ac5fc9563532826dccf4442886bef1ec94a41654b9cbb6c963d78a35d2` |
| Overall entropy | 6.316 |
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
| `.text` | 3,340,800 | 6.111 | No |
| `.data` | 27,136 | 2.178 | No |
| `.rdata` | 4,920,832 | 6.155 | No |
| `.pdata` | 93,184 | 5.585 | No |
| `.xdata` | 1,536 | 3.952 | No |
| `.bss` | 0 | 0.0 | No |
| `.edata` | 512 | 1.902 | No |
| `.idata` | 3,584 | 4.128 | No |
| `.CRT` | 512 | 0.259 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 31,232 | 5.434 | No |
| `/4` | 2,048 | 1.693 | No |
| `/19` | 74,752 | 6.018 | No |
| `/31` | 13,312 | 4.718 | No |
| `/45` | 31,744 | 5.446 | No |
| `/57` | 9,728 | 3.738 | No |
| `/70` | 2,560 | 4.518 | No |
| `/81` | 76,800 | 2.694 | No |
| `/92` | 5,632 | 1.787 | No |

### Imports

**KERNEL32.dll**: `AddVectoredContinueHandler`, `AddVectoredExceptionHandler`, `CloseHandle`, `CreateEventA`, `CreateIoCompletionPort`, `CreateThread`, `CreateWaitableTimerExW`, `DeleteCriticalSection`, `DuplicateHandle`, `EnterCriticalSection`, `ExitProcess`, `FreeEnvironmentStringsW`, `GetConsoleMode`, `GetCurrentThreadId`, `GetEnvironmentStringsW`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__iob_func`, `_amsg_exit`, `_beginthread`, `_errno`, `_initterm`, `_lock`, `_unlock`, `abort`, `calloc`, `fputc`, `free`, `fwrite`, `localeconv`

### Exports

`GetInstallDetailsPayload`, `SignalInitializeCrashReporting`, `_cgo_dummy_export`

## Extracted Strings

Total strings found: **32185** (showing first 100)

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
 Go build ID: "KX4_HSfASSv0z-CgVVBX/jx_d6STqczc3jpWaqRX_/WQkRgndxlJl5_sf0rOPE/jmOenUPwLH-MxlhzCufM"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
D$@I9p
\$hM9K
P(H9S(t
expafH
nd 3fH
2-byfH
te kfH
\$hH9H@v#H
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
runtime H
 error: H
:H9F w
2H+phH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
H9D$(t
H
H9X0tO
\$XHcz
$H+L$HH
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
v	H9Hr
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
vDH950f
J0f9J2vsH
f9s2uFf
D$$u$L
T$(M	D
L$0H+Y
runtime.H9
QpM9Qhu
L9L$Xt#H
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t6H9rPt0H
rpH92w
tRI9N0tLH
T$`Hc
L$XHc
|$0uMH
memprofi
lerau*f
yteu"H
9q0s&H9J
09z0w
H
H9X(v
L
HPH9w
H(H9w
H95\Y.
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.runtime.callbackasm.abi0` | `0x29f9ea0e0` | 10001 | ✓ |
| `sym.syscall.init` | `0x29f9eea80` | 7540 | ✓ |
| `dbg.__gdtoa` | `0x29fcaccc0` | 5895 | ✓ |
| `sym.runtime.findRunnable` | `0x29f9bcb00` | 4357 | ✓ |
| `sym.runtime._sweepLocked_.sweep` | `0x29f9a25c0` | 3928 | ✓ |
| `sym.main.GetInstallDetailsPayload.func1` | `0x29fa4a420` | 3832 | ✓ |
| `sym.main._RunPE.func2.4` | `0x29f9f7780` | 3832 | ✓ |
| `sym.main.GetEntryPointRVA.func1.4` | `0x29fa028e0` | 3832 | ✓ |
| `sym.main.Get_ThreadContext.func1.4` | `0x29fa05b20` | 3832 | ✓ |
| `sym.main.Write_ProcessMemory.func1.4` | `0x29fa0a7a0` | 3832 | ✓ |
| `sym.main.LoadFile.func3.4` | `0x29fa10e60` | 3832 | ✓ |
| `sym.main.PERawToVirtual.func1.4` | `0x29fa140a0` | 3832 | ✓ |
| `sym.main.FreePEBuffer.func1.4` | `0x29fa17440` | 3832 | ✓ |
| `sym.main.Virtual_Free.func1.4` | `0x29fa1a7e0` | 3832 | ✓ |
| `sym.main.SectionsRawToVirtual.func2.4` | `0x29fa1da20` | 3832 | ✓ |
| `sym.main.SectionsRawToVirtual.func3.4` | `0x29fa1f380` | 3832 | ✓ |
| `sym.main.AllocPEBuffer.func1.4` | `0x29fa225c0` | 3832 | ✓ |
| `sym.main.RelocateModule.func1.4` | `0x29fa23f20` | 3832 | ✓ |
| `sym.main.ProcessRelocationTable.func1.4` | `0x29fa25880` | 3832 | ✓ |
| `sym.main.ProcessRelocationTable.func2.4` | `0x29fa271e0` | 3832 | ✓ |
| `sym.main.gProcessRelocBlock.func1.4` | `0x29fa28b40` | 3832 | ✓ |
| `sym.main.gApplyRelocations.func1.4` | `0x29fa2a4a0` | 3832 | ✓ |
| `sym.main.Is64Bit.func1.4` | `0x29fa322e0` | 3832 | ✓ |
| `sym.main.GetNTHdrArch.func1.4` | `0x29fa33c40` | 3832 | ✓ |
| `sym.main.AllocAligned.func1.4` | `0x29fa36e80` | 3832 | ✓ |
| `sym.main.Virtual_Alloc.func1.4` | `0x29fa3a0c0` | 3832 | ✓ |
| `sym.main.main.func1.4` | `0x29fa40620` | 3832 | ✓ |
| `sym.main.main.func3.4` | `0x29fa43860` | 3832 | ✓ |
| `sym.main.main.func6.4` | `0x29fa48380` | 3832 | ✓ |
| `sym.main._RunPE.func1.4` | `0x29f9f5ea0` | 3749 | ✓ |

### Decompiled Code Files

- [`code/dbg.__gdtoa.c`](code/dbg.__gdtoa.c)
- [`code/sym.main.AllocAligned.func1.4.c`](code/sym.main.AllocAligned.func1.4.c)
- [`code/sym.main.AllocPEBuffer.func1.4.c`](code/sym.main.AllocPEBuffer.func1.4.c)
- [`code/sym.main.FreePEBuffer.func1.4.c`](code/sym.main.FreePEBuffer.func1.4.c)
- [`code/sym.main.GetEntryPointRVA.func1.4.c`](code/sym.main.GetEntryPointRVA.func1.4.c)
- [`code/sym.main.GetInstallDetailsPayload.func1.c`](code/sym.main.GetInstallDetailsPayload.func1.c)
- [`code/sym.main.GetNTHdrArch.func1.4.c`](code/sym.main.GetNTHdrArch.func1.4.c)
- [`code/sym.main.Get_ThreadContext.func1.4.c`](code/sym.main.Get_ThreadContext.func1.4.c)
- [`code/sym.main.Is64Bit.func1.4.c`](code/sym.main.Is64Bit.func1.4.c)
- [`code/sym.main.LoadFile.func3.4.c`](code/sym.main.LoadFile.func3.4.c)
- [`code/sym.main.PERawToVirtual.func1.4.c`](code/sym.main.PERawToVirtual.func1.4.c)
- [`code/sym.main.ProcessRelocationTable.func1.4.c`](code/sym.main.ProcessRelocationTable.func1.4.c)
- [`code/sym.main.ProcessRelocationTable.func2.4.c`](code/sym.main.ProcessRelocationTable.func2.4.c)
- [`code/sym.main.RelocateModule.func1.4.c`](code/sym.main.RelocateModule.func1.4.c)
- [`code/sym.main.SectionsRawToVirtual.func2.4.c`](code/sym.main.SectionsRawToVirtual.func2.4.c)
- [`code/sym.main.SectionsRawToVirtual.func3.4.c`](code/sym.main.SectionsRawToVirtual.func3.4.c)
- [`code/sym.main.Virtual_Alloc.func1.4.c`](code/sym.main.Virtual_Alloc.func1.4.c)
- [`code/sym.main.Virtual_Free.func1.4.c`](code/sym.main.Virtual_Free.func1.4.c)
- [`code/sym.main.Write_ProcessMemory.func1.4.c`](code/sym.main.Write_ProcessMemory.func1.4.c)
- [`code/sym.main._RunPE.func1.4.c`](code/sym.main._RunPE.func1.4.c)
- [`code/sym.main._RunPE.func2.4.c`](code/sym.main._RunPE.func2.4.c)
- [`code/sym.main.gApplyRelocations.func1.4.c`](code/sym.main.gApplyRelocations.func1.4.c)
- [`code/sym.main.gProcessRelocBlock.func1.4.c`](code/sym.main.gProcessRelocBlock.func1.4.c)
- [`code/sym.main.main.func1.4.c`](code/sym.main.main.func1.4.c)
- [`code/sym.main.main.func3.4.c`](code/sym.main.main.func3.4.c)
- [`code/sym.main.main.func6.4.c`](code/sym.main.main.func6.4.c)
- [`code/sym.runtime._sweepLocked_.sweep.c`](code/sym.runtime._sweepLocked_.sweep.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.findRunnable.c`](code/sym.runtime.findRunnable.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)

## Behavioral Analysis

Based on the final chunk of disassembly (6/6), your analysis is now complete. This final section provides deeper insight into the **execution flow** and the **obfuscation techniques** used to shield the core logic of the reflective loader.

Here is the updated, comprehensive analysis incorporating all findings from chunks 1 through 6.

---

### Updated Analysis Overview
The inclusion of chunk 6/6 confirms that this is not just a "lazy" loader; it is a **highly engineered piece of malware** designed to frustrate both automated sandboxes and human analysts. While previous sections established the "What" (Manual Mapping, Relocations, Memory Management), this section reveals the "How"—specifically how the binary hides its true purpose behind complex control flows and heavy internal processing.

---

### New Evidence from Chunk 6/6: The Execution Engine

The function `sym.main._RunPE.func1.4` provides several critical indicators of high-end malware development:

*   **Complex Control Flow & Obfuscation:**
    *   **Observation:** The disassembly shows deep nesting, repeated loops for seemingly simple logic, and numerous "jump" tables (e.g., `code_r0x00029fa48bd2`).
    *   **Technical Significance:** This is a classic obfuscation technique. By creating "spaghetti code" through complex conditional branching and long jump sequences, the author makes it difficult for static analysis tools to build an accurate Control Flow Graph (CFG). It forces analysts to spend significant time de-obfuscating the logic just to understand the basic next step of the program.

*   **Intensive Pre-Processing (`_RunPE` phase):**
    *   **Observation:** The heavy use of floating-point math, array manipulation (e.g., `afStack_348`, `afStack_370`), and constant transformations suggests that before the "Manual Mapping" even begins, the payload is undergoing significant **in-memory processing**. 
    *   **Malicious Context:** This indicates a multi-stage loading process. The loader doesn't just map the raw bytes; it likely decrypts, decompresses, or reconstructs the PE file's headers and sections in memory before applying relocations. This is designed to ensure that the "real" malicious code only exists in its runnable form for a few milliseconds during execution.

*   **Go Runtime Integration & Sophistication:**
    *   **Observation:** The frequent calls to `sym.runtime` (e.g., `makemap_small`, `convT64`, `panicIndex`) indicate that the loader is written in or compiled from **Golang**. 
    *   **Technical Significance:** Modern malware authors increasingly use Go because it provides high-level functionality while producing statically linked binaries with complex internal logic. This makes "de-compilation" much harder than standard C/C++ code, as the analyst must peel away layers of Go's runtime environment to find the underlying malicious instructions.

---

### Final Synthesis: The Full Execution Lifecycle (Chunks 1–6)

By combining all evidence, we can now map the complete, high-sophistication lifecycle of this threat:

1.  **Environment Validation:** Initial checks (`Is64Bit`, `GetNTHdrArch`) ensure compatibility and determine which offset constants to use for various architectures.
2.  **Obfuscated Routine Preparation:** The code enters a complex set of loops and logic branches (as seen in Chunk 6) to decrypt or "unpack" the inner payload hidden within its data section.
3.  **Manual Memory Allocation:** Instead of calling `LoadLibrary`, it uses `Virtual_Alloc` and `AllocAligned` to carve out private, non-file-backed memory regions for the malicious code.
4.  **The Reflection Engine (Mapping):** 
    *   It maps raw sections into these new buffers (`SectionsRawToVirtual`).
    *   It resolves relative addresses by manually processing the relocation table (`gApplyRelocations`).
5.  **Execution & Persistence:** Once relocated and "fixed," the loader jumps to the Entry Point (EP) of the hidden module, allowing a RAT or Stealer to run completely invisible to standard Windows API hooks.

---

### Updated Final Analysis Report for Documentation

*   **Classification:** **Advanced Reflective Loader / Manual Mapper.**
*   **Malware Architecture:** Likely written in Go; utilizes heavy obfuscation (complex jumps and arithmetic loops) to hide its execution path from automated scanners.
*   **Key Sophistication Indicators:**
    1.  **Manual Mapping (Chunk 5):** Bypasses `InLoadOrderModuleList` by replicating the Windows Loader's behavior internally.
    2.  **Relocation Processing (`gApplyRelocations`):** Essential for hosting complex, multi-functional DLLs rather than simple shellcode snippets.
    3.  **Dynamic Memory Management:** Uses `Virtual_Alloc` to create "anonymous" executable memory, a primary indicator of Reflective Loading.
    4.  **High Obfuscation Level (Chunk 6):** Heavy use of opaque predicates and complex control flow designed to stall manual analysis.

*   **Threat Actor Profile:** This is consistent with **APT-level infrastructure** or high-end **Malware-as-a-Service (MaaS)** products. The technical investment required to build a multi-architecture, obfuscated, manually-mapping loader suggests a professional development cycle aimed at evading advanced EDR (Endpoint Detection and Response) solutions.

*   **Detection & Mitigation Strategy:**
    1.  **Memory Scraping:** Periodically scan for memory regions with `PAGE_EXECUTE_READWRITE` permissions that have no backing file on disk ("Floating Code"). 
    2.  **Call Stack Analysis:** Monitor for calls to `VirtualAlloc` followed by an immediate change in the instruction pointer (`EIP`/`RIP`) to a newly allocated region.
    3.  **Dynamic Instrumentation:** Use tools like Intel PIN or Frida to intercept and log `Virtual_Alloc` calls, specifically looking for large allocations that are subsequently modified via "Relocation" style loops.
    4.  **Heuristic Alerting:** Flag any process where the execution flow enters a memory region that was allocated just moments prior by a different function in the same process space.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your report to the relevant MITRE ATT&CK techniques. 

The malware exhibits high-sophistication tactics specifically designed to bypass signature-based detection and evade memory forensics by avoiding standard Windows API calls for module loading.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Execution | The use of "spaghetti code," jump tables, and deep nested loops is designed to hinder static analysis and complicate the construction of a Control Flow Graph (CFG). |
| **T1027.002** | Obfuscated Files or Programs | The intensive pre-processing phase involving mathematical transformations indicates that the payload is decrypted/decompressed in memory before it can be executed. |
| **T1616** | Reflective Code Loading | The "Manual Mapping" process (using `Virtual_Alloc` to map segments and manually processing relocation tables) allows the loader to execute code without calling standard loaders like `LoadLibrary`. |
| **T1036** | Dynamic Resolution | By resolving addresses internally via manual mapping, the malware avoids appearing in standard module lists (like `InLoadOrderModuleList`), thereby evading detection by many EDR tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   (None identified)

**File paths / Registry keys**
*   (None identified)

**Mutex names / Named pipes**
*   (None identified)

**Hashes**
*   (No standard MD5/SHA1/SHA256 hashes were present in the strings.)

**Other artifacts**
*   **Go Build ID:** `KX4_HSfASSv0z-CgVVBX/jx_d6STqczc3jpWaqRX_/WQkRgndxlJl5_sf0rOPE/jmOenUPwLH-MxlhzCufM` (Used to identify the specific build of the Go-based loader).
*   **Internal Function Names:** `sym.main._RunPE.func1.4` (Identifies a specific obfuscated execution path in the Go runtime).
*   **Memory Offsets/Jump Tables:** `code_r0x00029fa48bd2` (Indicates a non-standard, potentially hardened jump table used to hinder static analysis).
*   **Behavioral Signatures:** 
    *   **Manual Mapping Techniques:** Use of `Virtual_Alloc`, `AllocAligned`, and `gApplyRelocations`.
    *   **Runtime Environment:** Presence of standard Go runtime components (`runtime.H9`, `reflect.H9`, `memprofiler`) used to mask the loader's primary purpose.
    *   **Obfuscation Logic:** High-frequency arithmetic loops involving variables like `afStack_348` and `afStack_370`.

---

## Malware Family Classification

Based on the technical analysis provided, here is the classification for the sample:

1. **Malware family:** custom
2. **Malware type:** loader
3. **Confidence:** High
4. **Key evidence:**
    *   **Reflective Loading & Manual Mapping:** The sample employs advanced "Manual Mapping" techniques (using `Virtual_Alloc` and manual relocation processing) to load a payload into memory while bypassing standard Windows API hooks and avoiding inclusion in the `InLoadOrderModuleList`.
    *   **High-Level Obfuscation via Go Runtime:** The use of the Go programming language, combined with complex "spaghetti" code structures (jump tables, nested loops, and arithmetic transformations), is specifically designed to frustrate static analysis and complicate the construction of a Control Flow Graph.
    *   **Multi-Stage Execution Engine:** The presence of an intensive pre-processing phase indicates that the loader acts as a sophisticated wrapper, decrypting or decompressing a hidden secondary payload (such as a RAT or infostealer) in memory before execution.
