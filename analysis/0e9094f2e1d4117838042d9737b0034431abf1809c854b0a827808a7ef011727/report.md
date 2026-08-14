# Threat Analysis Report

**Generated:** 2026-08-12 20:30 UTC
**Sample:** `0e9094f2e1d4117838042d9737b0034431abf1809c854b0a827808a7ef011727_0e9094f2e1d4117838042d9737b0034431abf1809c854b0a827808a7ef011727.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e9094f2e1d4117838042d9737b0034431abf1809c854b0a827808a7ef011727_0e9094f2e1d4117838042d9737b0034431abf1809c854b0a827808a7ef011727.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 14,271,313 bytes |
| MD5 | `c902493950638467a537b8474dcaa6d6` |
| SHA1 | `1b6e66e17635ed9ba7ebce887356ba465d89211e` |
| SHA256 | `0e9094f2e1d4117838042d9737b0034431abf1809c854b0a827808a7ef011727` |
| Overall entropy | 7.992 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1781349480 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 181,760 | 6.465 | No |
| `.rdata` | 80,896 | 5.753 | No |
| `.data` | 3,584 | 1.816 | No |
| `.pdata` | 9,728 | 5.315 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 19,456 | 7.911 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.264 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `VirtualProtect`, `InitializeCriticalSectionEx`, `GetOEMCP`, `GetCPInfo`, `GetLastError`, `FreeLibrary`, `GetProcAddress`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **28492** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
UVWAUAWH
0A_A]_^]
SUVWAVAWH
A_A^_^][
A_A^_^][
\$ UAVAWH
0A_A^]
0A_A^]
L$ SUVWH
L$ SUVWH
T$hfD+D$df+T$`
@SUVWAVH
T$<f+T$4
PA^_^][
\$ UVW
|$ AVH
L$ SUVWH
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
L$ SUVWAV
A^_^][
L$ SUVWAV
A^_^][
L$ SUVWATAUAVAW
A_A^A]A\_^][
UVWATAWH
0A_A\_^]
@UVATAU
A]A\^]
L9t$0t
tR@80tMH
L$ SVWH
@SUWAVAW
A_A^_][
H9{ t)
H9{(t(
H9{8t#
H9{@t&
l$ ATAVAWH
 A_A^A\
l$ VWAV
u[HcG0
l$ VATAUAVAWH
0A_A^A]A\^
MLcF0H
@SVAVH
t$ WAVAWH
VWATAVAWH
~#D8e0u
0A_A^A\_^
l$ VWAV
@UVWATAUAVAW
A_A^A]A\_^]
l$ VWATAVAW
A_A^A\_^
|$ AVH
UVWAVAWH
 A_A^_^]
WAVAWH
0A_A^_
@SUVWAV
A^_^][
@VATAUAVAWH
 A_A^A]A\^
@SUATAU
A]A\][
D$hH+D$pHi
|$8fff
SUVWATAUAVAWH
8A_A^A]A\_^][
SUVWATAUAVAWH
MP;H(s
MP;H8s
]Lu*A;|$
L$@E)}P
A;Exs`
E;E8v#A
L$@A9MP
tDE;u$t>H
T$8E+T$
XA_A^A]A\_^][
tHH9
uC
I@L9{8uH
~0L9{0
y<L9{0
\$ UVAVH
@USVWAVAWH
fD98uA
A_A^_^[]
uxHc<
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140018184` | `0x140018184` | 40065 | ✓ |
| `fcn.14001c150` | `0x14001c150` | 37955 | ✓ |
| `fcn.14001c13c` | `0x14001c13c` | 37914 | ✓ |
| `section..text` | `0x140001000` | 17899 | ✓ |
| `fcn.140027420` | `0x140027420` | 12313 | ✓ |
| `fcn.140004b70` | `0x140004b70` | 9279 | ✓ |
| `fcn.14000b6c0` | `0x14000b6c0` | 6129 | ✓ |
| `fcn.140029db0` | `0x140029db0` | 5703 | ✓ |
| `fcn.14002610c` | `0x14002610c` | 4735 | ✓ |
| `fcn.140001ca0` | `0x140001ca0` | 2338 | ✓ |
| `fcn.1400230ac` | `0x1400230ac` | 2201 | ✓ |
| `fcn.14001759c` | `0x14001759c` | 1946 | ✓ |
| `fcn.140012498` | `0x140012498` | 1898 | ✓ |
| `fcn.14001715c` | `0x14001715c` | 1777 | ✓ |
| `fcn.1400028a0` | `0x1400028a0` | 1773 | ✓ |
| `fcn.14002bd10` | `0x14002bd10` | 1661 | ✓ |
| `fcn.140029e80` | `0x140029e80` | 1451 | ✓ |
| `fcn.14000d3d0` | `0x14000d3d0` | 1433 | ✓ |
| `fcn.140023dac` | `0x140023dac` | 1421 | ✓ |
| `fcn.140014eb0` | `0x140014eb0` | 1397 | ✓ |
| `fcn.1400230b4` | `0x1400230b4` | 1353 | ✓ |
| `fcn.140005f70` | `0x140005f70` | 1325 | ✓ |
| `fcn.14000fecc` | `0x14000fecc` | 1263 | ✓ |
| `fcn.14000b1e0` | `0x14000b1e0` | 1238 | ✓ |
| `fcn.14000ad40` | `0x14000ad40` | 1179 | ✓ |
| `fcn.14001e3a0` | `0x14001e3a0` | 1171 | ✓ |
| `fcn.14000a000` | `0x14000a000` | 1169 | ✓ |
| `fcn.140025c80` | `0x140025c80` | 1164 | ✓ |
| `fcn.140014a40` | `0x140014a40` | 1133 | ✓ |
| `fcn.14001d830` | `0x14001d830` | 1119 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ca0.c`](code/fcn.140001ca0.c)
- [`code/fcn.1400028a0.c`](code/fcn.1400028a0.c)
- [`code/fcn.140004b70.c`](code/fcn.140004b70.c)
- [`code/fcn.140005f70.c`](code/fcn.140005f70.c)
- [`code/fcn.14000a000.c`](code/fcn.14000a000.c)
- [`code/fcn.14000ad40.c`](code/fcn.14000ad40.c)
- [`code/fcn.14000b1e0.c`](code/fcn.14000b1e0.c)
- [`code/fcn.14000b6c0.c`](code/fcn.14000b6c0.c)
- [`code/fcn.14000d3d0.c`](code/fcn.14000d3d0.c)
- [`code/fcn.14000fecc.c`](code/fcn.14000fecc.c)
- [`code/fcn.140012498.c`](code/fcn.140012498.c)
- [`code/fcn.140014a40.c`](code/fcn.140014a40.c)
- [`code/fcn.140014eb0.c`](code/fcn.140014eb0.c)
- [`code/fcn.14001715c.c`](code/fcn.14001715c.c)
- [`code/fcn.14001759c.c`](code/fcn.14001759c.c)
- [`code/fcn.140018184.c`](code/fcn.140018184.c)
- [`code/fcn.14001c13c.c`](code/fcn.14001c13c.c)
- [`code/fcn.14001c150.c`](code/fcn.14001c150.c)
- [`code/fcn.14001d830.c`](code/fcn.14001d830.c)
- [`code/fcn.14001e3a0.c`](code/fcn.14001e3a0.c)
- [`code/fcn.1400230ac.c`](code/fcn.1400230ac.c)
- [`code/fcn.1400230b4.c`](code/fcn.1400230b4.c)
- [`code/fcn.140023dac.c`](code/fcn.140023dac.c)
- [`code/fcn.140025c80.c`](code/fcn.140025c80.c)
- [`code/fcn.14002610c.c`](code/fcn.14002610c.c)
- [`code/fcn.140027420.c`](code/fcn.140027420.c)
- [`code/fcn.140029db0.c`](code/fcn.140029db0.c)
- [`code/fcn.140029e80.c`](code/fcn.140029e80.c)
- [`code/fcn.14002bd10.c`](code/fcn.14002bd10.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This final chunk of disassembly completes the technical picture of the binary. The continued appearance of complex, multi-layered logic reinforces the conclusion that this is a **large, mature runtime environment** rather than a custom piece of malware code.

The new segments provide specific evidence regarding how the Python interpreter handles Windows system interactions and internal memory management.

### Updated Technical Analysis (Chunk 3/3)

#### 1. Window Management & "Hidden" Logic (`fcn.14000a000`)
This function is a significant find, but its purpose is consistent with specific Python packaging behaviors:
*   **Windows API Interaction:** The function calls `RegisterClassW`, `CreateWindowExW`, `ShowWindow`, and a loop containing `PeekMessageW` and `DispatchMessageW`.
*   **Contextual Meaning:** In the context of PyInstaller (or similar tools), this is used to create a **"Hidden Window."** Because Python's interpreter often relies on a windowing system to process events even in CLI mode, these calls ensure that the application remains functional and stable when running as a background process or without an attached console.
*   **Security Context:** While "hidden windows" can be used by malware to hide activity, here it is integrated into a standardized sequence of initialization for the Python environment. The presence of `GetConsoleOutputCP` and `SetConsoleCtrlHandler` further suggests this is part of the boilerplate required to ensure the script runs correctly regardless of how the user launched it.

#### 2. Complex Memory Manipulation & String Handling (`fcn.140025c80`, `fcn.14001d830`)
*   **Buffer Management:** These functions contain heavy logic for calculating offsets, lengths, and memory copies (e.g., the loops calculating `uVar16 = iVar13 + uVar16` and performing bitwise operations on addresses).
*   **Analysis:** This is indicative of **Python's Internal String/Buffer Handling**. Because Python supports a wide variety of string types (Unicode, various encodings) and memory views, the underlying C-code must be extremely "defensive" and complex to handle edge cases. 
*   **Conclusion:** These are not obfuscated "hiding" routines; they are optimized, industrial-strength implementations of standard data structures used by the Python interpreter.

#### 3. System I/O and Environment Setup (`fcn.1400230b4`)
*   **Environment Variables:** The inclusion of `SetEnvironmentVariableW` and the logic to parse environment variables from the system block is a core part of the Python startup sequence (initializing `sys.path`, `PYTHONPATH`, etc.).
*   **Standard Streams:** The use of `ReadFile` and `ReadConsoleW` in `fcn.14001d830` relates to how the interpreter interacts with `stdin`, `stdout`, and `stderr`.

---

### Final Cumulative Analysis Summary

The analysis of all three chunks confirms that this binary is a **highly standard, sophisticated Python runtime loader.** 

*   **Confidence Score:** **High**. The presence of Tcl/Tk libraries, highly optimized Unicode decoding (Chunk 2), hidden-window management for CLI stability (Chunk 3), and robust memory/buffer handling (Chunk 3) are definitive hallmarks of a professional distribution tool like **PyInstaller**.
*   **The "Shell" vs. "Core" Distinction:** This is the most critical finding for Incident Response. The complexity you see in these `fcn` blocks is not a sign of a sophisticated attacker's evasion; it is the complexity of the **Python language itself** being ported into a standalone executable.
*   **Malicious Intent Location:** The "malice" (if any) is almost certainly **not** within these functions. These are boilerplate components required to make Python work as an `.exe`. The actual malicious payload—the instructions for data theft, persistence, or C2 communication—is contained within the **embedded scripts/bytecode**, which are only loaded *after* these complex initialization routines finish.

### Final Recommendations for Incident Response (IR)

1.  **Cease Manual De-obfuscation of Loader Functions:** The manual analysis of the disassembly has reached a point of diminishing returns. Because these functions are standard Python library code, searching for "hidden" triggers within them will not yield results.
2.  **Immediate Action: Payload Extraction:** Use **`pyinstxtractor.py`** to unpack the executable. This is the industry-standard way to "peel" the wrapper off a PyInstaller bundle. 
3.  **Analyze the Extracted `.pyc` Files:** Once unpacked, you will likely find several `.pyc` files (compiled Python bytecode). Use **`uncompyle6`** or **`pycdc`** to convert these back into human-readable `.py` source code. 
    *   *Target the extracted scripts for:* Hardcoded IP addresses/domains, file paths being modified, registry keys being changed, and credential harvesting logic.
4.  **Behavioral Monitoring:** While running the sample in a controlled sandbox, monitor:
    *   The creation of temporary files (common during the "unpacking" phase of these loaders).
    *   Network connections made *after* the initial execution period.
    *   Spawning of `cmd.exe` or `powershell.exe` processes by the loader.

**Final Conclusion:** This is a classic "wrapper" scenario. The binary acts as a container; it is very good at its job of concealing the actual malicious code from static analysis of the `.exe` file alone. Transition to **dynamic analysis and payload extraction** to identify the true intent.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Hideerself | The use of `CreateWindowExW` and `ShowWindow` to create a "hidden window" allows the process to run in the background without an interactive console. |
| T1059 | Command and Scripting Interpreter | The entire structure is identified as a Python runtime, indicating that the core logic is executed through an interpreted scripting language. |
| T1027 | Obfuscated Files or Information | The complex, multi-layered buffer management and memory manipulation serve to wrap and conceal the actual payload from initial static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted Indicator of Compromise (IOC) report:

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: The analysis mentions `SetEnvironmentVariableW`, but no specific registry paths or file paths were provided.)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Malware Type/Technique:** Python Runtime Loader (PyInstaller-style wrapper).
*   **Behavioral Indicator:** Use of "Hidden Window" logic (`RegisterClassW`, `CreateWindowExW`, `ShowWindow`) to execute script logic in the background without a console window.
*   **Technical Note:** The analysis confirms that the core malicious functionality is likely contained within embedded `.pyc` files/bytecode rather than the extracted strings, which consist of standard Python interpreter boilerplate (Unicode decoding, buffer management, and environment setup).

***

**Analyst Note:** The provided data describes a "Wrapper" scenario. While no direct infrastructure IOCs (like IP addresses or specific file paths) were found in the text, the behavioral analysis indicates that the primary malicious payload is hidden within a Python bytecode layer, which requires `pyinstxtractor` and `uncompyle6` for further extraction of actionable indicators.

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

**1. Malware family:** Unknown (Generic Python Wrapper)
**2. Malware type:** loader 
**3. Confidence:** High
**4. Key evidence:**
*   **Standard Runtime Environment:** The technical analysis confirms the binary is a standard, sophisticated Python runtime (likely PyInstaller). The complexity observed in the disassembly belongs to the Python interpreter's core logic (Unicode handling, memory management, and environment setup) rather than custom malicious code.
*   **Wrapper Functionality:** The presence of "Hidden Window" logic (`CreateWindowExW`, `ShowWindow`) and standard initialization routines indicates the binary acts as a container/wrapper designed to execute scripts in the background without an interactive console.
*   **Layered Obfuscation:** The analysis identifies a clear distinction between the "Shell" (the .exe) and the "Core" (the embedded Python bytecode). This is a common technique used by various threat actors to hide malicious payloads within a legitimate-looking execution environment.
