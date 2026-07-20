# Threat Analysis Report

**Generated:** 2026-07-19 12:42 UTC
**Sample:** `0937a3594dbec19fcc3341db1333b19f9656a45b3195867fa0a885e3ebd02e80_0937a3594dbec19fcc3341db1333b19f9656a45b3195867fa0a885e3ebd02e80.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0937a3594dbec19fcc3341db1333b19f9656a45b3195867fa0a885e3ebd02e80_0937a3594dbec19fcc3341db1333b19f9656a45b3195867fa0a885e3ebd02e80.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 42,714,048 bytes |
| MD5 | `ce3fda17b9c740b5158b86efafd45e87` |
| SHA1 | `d962b9e6b18064aed75401ab177e319ef51b3622` |
| SHA256 | `0937a3594dbec19fcc3341db1333b19f9656a45b3195867fa0a885e3ebd02e80` |
| Overall entropy | 7.999 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769088824 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 180,224 | 6.513 | No |
| `.rdata` | 75,264 | 5.822 | No |
| `.data` | 3,584 | 1.821 | No |
| `.pdata` | 8,192 | 5.303 | No |
| `.rsrc` | 36,352 | 7.907 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.272 | No |

### Imports

**USER32.dll**: `DestroyIcon`, `DefWindowProcW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `DestroyWindow`, `DispatchMessageW`, `TranslateMessage`, `PeekMessageW`, `ShowWindow`, `RegisterClassW`, `GetMessageW`, `PostMessageW`, `MessageBoxA`, `MessageBoxW`, `MoveWindow`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `LCMapStringW`, `CompareStringW`, `FlsFree`, `FlsSetValue`, `FlsGetValue`, `GetOEMCP`, `GetCPInfo`, `LoadLibraryExW`, `GetProcAddress`
**ADVAPI32.dll**: `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `OpenProcessToken`, `ConvertSidToStringSidW`, `GetTokenInformation`
**GDI32.dll**: `SelectObject`, `CreateFontIndirectW`, `DeleteObject`

## Extracted Strings

Total strings found: **94724** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
AWAVATVWSH
([_^A\A^A_
AWAVAUATVWUSH
|$@ff.
[]_^A\A]A^A_
AWAVATVWUSH
 []_^A\A^A_
AWAVVWSH
[_^A^A_
AVVWUSH
 []_^A^
AVVWSH
8[_^A^
AVVWSH
8[_^A^
AWAVVWS
[_^A^A_
AVVWSH
D$lD+D$d+T$`H
AWAVVWUSH
l$D+l$<
H[]_^A^A_
AWAVATVWS
[_^A\A^A_
AWAVATVWS
[_^A\A^A_
AWAVAUATVWUS
[]_^A\A]A^A_
AWAVAUATVWS
[_^A\A]A^A_
AWAVAUATVWUS
[]_^A\A]A^A_
AVVWSH
8[_^A^
AWAVAUATVWUS
|$0fffff.
[]_^A\A]A^A_
ffffff.
AWAVAUATVWUS
[]_^A\A]A^A_
AWAVAUATVWUS
[]_^A\A]A^A_
AWAVATVWS
[_^A\A^A_
HcF(H9
AWAVAUATVWUS
[]_^A\A]A^A_
fffff.
n0Hcn(A
ffffff.
AVVWUS
[]_^A^
uaLcO(M
ffffff.
AVVWUSH
`[]_^A^
fffff.
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVVWSH
 [_^A^A_
ffffff.
AWAVAUATVWSH
 [_^A\A]A^A_
ffffff.
AVVWSH
([_^A^
AWAVVWSH
0[_^A^A_
Whffff.
ffffff.
AWAVATVWSH
8[_^A\A^A_
ffffff.
AWAVAUATVWUS
d$0ffffff.
[]_^A\A]A^A_
fffff.
AVVWSH
([_^A^
AWAVVWSH
0[_^A^A_
AVVWSH
8[_^A^
ffffff.
AWAVVWSH
 [_^A^A_
AWAVAUATVWUS
[]_^A\A]A^A_
AWAVAUATVWUSH
ffffff.
H[]_^A\A]A^A_
AWAVAUATVWUS
[]_^A\A]A^A_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400174fc` | `0x1400174fc` | 42221 | ✓ |
| `fcn.14001c50c` | `0x14001c50c` | 36450 | ✓ |
| `fcn.14001c4f8` | `0x14001c4f8` | 36400 | ✓ |
| `section..text` | `0x140001000` | 14571 | ✓ |
| `fcn.1400271a4` | `0x1400271a4` | 12801 | ✓ |
| `fcn.14000a8d0` | `0x14000a8d0` | 9657 | ✓ |
| `fcn.140004040` | `0x140004040` | 7729 | ✓ |
| `fcn.140029d28` | `0x140029d28` | 5645 | ✓ |
| `fcn.140025e8c` | `0x140025e8c` | 4750 | ✓ |
| `fcn.140028e84` | `0x140028e84` | 4020 | ✓ |
| `fcn.1400098e0` | `0x1400098e0` | 2872 | ✓ |
| `fcn.140022c60` | `0x140022c60` | 2201 | ✓ |
| `fcn.1400095a0` | `0x1400095a0` | 2184 | ✓ |
| `fcn.14000d790` | `0x14000d790` | 2022 | ✓ |
| `fcn.1400178f8` | `0x1400178f8` | 1946 | ✓ |
| `fcn.140001ab0` | `0x140001ab0` | 1913 | ✓ |
| `fcn.140012880` | `0x140012880` | 1909 | ✓ |
| `fcn.140017188` | `0x140017188` | 1777 | ✓ |
| `fcn.14002be30` | `0x14002be30` | 1661 | ✓ |
| `fcn.1400022d0` | `0x1400022d0` | 1494 | ✓ |
| `fcn.140029df0` | `0x140029df0` | 1451 | ✓ |
| `fcn.140023bec` | `0x140023bec` | 1405 | ✓ |
| `fcn.140022c68` | `0x140022c68` | 1353 | ✓ |
| `fcn.140007a70` | `0x140007a70` | 1242 | ✓ |
| `fcn.1400101c4` | `0x1400101c4` | 1231 | ✓ |
| `fcn.1400259f0` | `0x1400259f0` | 1180 | ✓ |
| `fcn.14001e758` | `0x14001e758` | 1141 | ✓ |
| `fcn.14001525c` | `0x14001525c` | 1124 | ✓ |
| `fcn.140007460` | `0x140007460` | 1118 | ✓ |
| `fcn.140003be0` | `0x140003be0` | 1117 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001ab0.c`](code/fcn.140001ab0.c)
- [`code/fcn.1400022d0.c`](code/fcn.1400022d0.c)
- [`code/fcn.140003be0.c`](code/fcn.140003be0.c)
- [`code/fcn.140004040.c`](code/fcn.140004040.c)
- [`code/fcn.140007460.c`](code/fcn.140007460.c)
- [`code/fcn.140007a70.c`](code/fcn.140007a70.c)
- [`code/fcn.1400095a0.c`](code/fcn.1400095a0.c)
- [`code/fcn.1400098e0.c`](code/fcn.1400098e0.c)
- [`code/fcn.14000a8d0.c`](code/fcn.14000a8d0.c)
- [`code/fcn.14000d790.c`](code/fcn.14000d790.c)
- [`code/fcn.1400101c4.c`](code/fcn.1400101c4.c)
- [`code/fcn.140012880.c`](code/fcn.140012880.c)
- [`code/fcn.14001525c.c`](code/fcn.14001525c.c)
- [`code/fcn.140017188.c`](code/fcn.140017188.c)
- [`code/fcn.1400174fc.c`](code/fcn.1400174fc.c)
- [`code/fcn.1400178f8.c`](code/fcn.1400178f8.c)
- [`code/fcn.14001c4f8.c`](code/fcn.14001c4f8.c)
- [`code/fcn.14001c50c.c`](code/fcn.14001c50c.c)
- [`code/fcn.14001e758.c`](code/fcn.14001e758.c)
- [`code/fcn.140022c60.c`](code/fcn.140022c60.c)
- [`code/fcn.140022c68.c`](code/fcn.140022c68.c)
- [`code/fcn.140023bec.c`](code/fcn.140023bec.c)
- [`code/fcn.1400259f0.c`](code/fcn.1400259f0.c)
- [`code/fcn.140025e8c.c`](code/fcn.140025e8c.c)
- [`code/fcn.1400271a4.c`](code/fcn.1400271a4.c)
- [`code/fcn.140028e84.c`](code/fcn.140028e84.c)
- [`code/fcn.140029d28.c`](code/fcn.140029d28.c)
- [`code/fcn.140029df0.c`](code/fcn.140029df0.c)
- [`code/fcn.14002be30.c`](code/fcn.14002be30.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This fourth chunk of disassembly provides the "final piece" of the puzzle regarding how this binary functions as an execution engine. It specifically highlights the transition from the **Loader** (the C/C++ code) to the **Payload** (the Python logic).

The analysis below incorporates these new findings into the existing framework.

---

### Updated Analysis Summary
The binary is confirmed as a **highly capable, multi-layered "wrapper" or "bootloader."** This final chunk confirms that it contains an integrated environment for handling Python's internal mechanics—specifically path resolution, exception handling (traceback), and module discovery. The complexity of the code is not just to "hide" logic, but to provide a fully functional execution environment for a bundled Python application (likely produced via PyInstaller or a similar tool).

---

### New Technical Observations & Findings

#### 1. Path Translation & Resolution (`fcn.140003be0`)
This function is heavily involved in resolving where the "actual" code lives. It handles several critical tasks:
*   **Internal to External Mapping:** It takes an internal reference (likely a path inside the packed bundle) and transforms it into a valid OS-level absolute path (`fcn.14001a40`). 
*   **`__file__` Manipulation:** The code explicitly interacts with the `__file__` attribute of the Python modules. This is necessary because, in "OneFile" mode, the script needs to know it is running from a temporary folder rather than its original bundled location.
*   **Safety Checks:** It includes checks for "maximum path length," ensuring that the dynamic expansion into the `Temp` directory doesn't break due to Windows path limitations.

#### 2. Robust Error Handling & Tracebacks
The disassembly shows a significant block of code dedicated to:
*   **Traceback Integration:** It references `traceback` and `format_exception`. 
*   **Meaning:** If the *inner* Python script crashes, this loader is designed to catch that exception and format it. This ensures that if an error occurs in the "payload" phase, the user sees a standard Python traceback (or a formatted version of one) rather than just a silent crash of the .exe.

#### 3. Artifacts of Packaging Tooling
The presence of specific string checks—even those that appear slightly obfuscated or as unique identifiers (e.g., `"KajvSVBdtnFgM ArkCxpxlksZubrB script from archive!"`)—indicates the use of a standardized build pipeline. 
*   **Analysis:** These are "sanity checks." The loader checks if the internal archive is valid before attempting to jump into the Python execution loop. If the integrity check fails, it prints an error message indicating the script could not be loaded from the bundle.

---

### Comprehensive Technical Synthesis

By combining all four chunks of disassembly, we can map out the exact lifecycle of a process launched by this binary:

1.  **Initialization (Chunk 1 & 2):** The loader starts, sets up environmental variables, and identifies required system libraries (like Tcl/Tk for GUIs).
2.  **Environment Preparation (Chunk 3):** It creates a hidden window (to hide the console) and prepares a working directory in the system's `Temp` folder.
3.  **Extraction & Mapping (Chunk 4):** It extracts the compressed Python files into the temporary directory, maps their internal paths to the new physical locations, and validates that the "script from archive" is present.
4.  **Execution (The "Black Box"):** The loader hands control over to a hidden child process or a specialized thread where the actual Python interpreter begins running the payload's logic (which may involve SIMD-accelerated math via NumPy/SciPy).

---

### Refined Analysis of Risk & Behavior

*   **Infrastructure as an Enabler:** The complexity observed (Tcl/Tk, AVX instructions, Traceback handling) is **not a sign of sophisticated manual malware coding**, but rather the hallmark of **standardized automation**. This loader provides "everything" a developer needs to run a complex Python app.
*   **The "Trojan Horse" Nature:** Because this loader is so robust, it can be used by both legitimate developers (to bundle their apps) and malicious actors (to wrap malware). The loader itself does not "malbehave"—it simply provides the environment for whatever code is inside it to behave.
*   **Evidence of Sophistication:** While likely a standard tool, the inclusion of SIMD-optimized math kernels suggests that any payload running within this structure is intended to perform significant computation or data processing.

### Final Recommendations to Investigators

The analysis confirms that **the loader's primary purpose is to provide a "seamless" environment for a Python application.** 

**Investigative Strategy:**
1.  **Ignore the Loader's C++ Logic:** Do not spend extensive time reverse-engineering the `fcn` calls in the disassembly; they are standard boilerplate for handling Python environments and file system paths.
2.  **Focus on the Extraction Point:** The most critical moment is when `fcn.140003be0` (or similar) successfully validates the "script from archive." This is where the transition to the payload occurs.
3.  **Dynamic Analysis / Memory Forensics:** 
    *   Run the sample in a sandbox and monitor for **file writes to `\AppData\Local\Temp\` or `%TEMP%`.**
    *   Once the file is written, **dump that directory.** It will contain the `.py` or `.pyc` files. 
    *   **Decompile the Python scripts:** Using a tool like `uncompyle6` or `pycdc`, you can convert the `.pyc` files back into readable `.py` source code to see the actual malicious intent.
4.  **Identify the Payload Purpose:** Look for calls to network libraries, credential theft, or encryption routines within the *extracted* Python files to determine the ultimate goal of the attack.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059.004** | Command and Scripting Interpreter: Python | The binary is explicitly identified as an execution engine designed to handle Python-specific logic, including path resolution and traceback handling. |
| **T1036** | Masquerading | The "wrapper" or "bootloader" architecture allows the malicious payload to hide behind a legitimate-looking executable and its associated environment (e.g., hidden windows). |
| **T1027** | Obfuscated Files or Information | The use of archives, internal integrity checks ("script from archive"), and bundling ensures that the primary malicious code is not visible until runtime extraction. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the identified Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **Temporary Directory Usage:** The analysis indicates the malware utilizes the system's `Temp` folder and `%TEMP%` directory to extract and execute its payload. (Note: While these are standard Windows locations, they are flagged here as a primary stage for payload staging).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Specific Unique String:** `"KajvSVBdtnFgM ArkCxpxlksZubrB script from archive!"` (Identified as a "sanity check" string used to verify the integrity of internal archives/payloads).
*   **Internal Function Offsets (Binary Analysis):** 
    *   `fcn.140003be0` (Related to path translation and resolution)
    *   `fcn.14001a40` (Relates to internal-to-external path mapping)
*   **Environment/Framework Artifacts:** 
    *   Use of **Tcl/Tk** libraries for GUI elements.
    *   Integration of **SIMD-optimized math kernels** (likely via NumPy or similar).
    *   Evidence of **PyInstaller** "OneFile" bundling characteristics (e.g., handling `__file__` attribute, `traceback` module usage, and internal script extraction).

---

### **Analyst Note**
The provided text does not contain immediate network-based indicators (IPs/URLs). The primary threat profile is a **PyInstaller-style wrapper**. The core risk resides in the "Black Box" payload that is extracted into the `%TEMP%` directory. Investigative efforts should focus on performing memory forensics or file system monitoring of the `\Temp\` directory to capture the de-obfuscated Python scripts (.py / .pyc) once the loader successfully executes its extraction routine.

---

## Malware Family Classification

1. **Malware family**: custom (PyInstaller-style wrapper)
2. **Malware type**: loader / dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Wrapped Execution Environment:** The binary acts as a multi-layered "bootloader" specifically designed to provide a full execution environment for Python payloads, including complex tasks like path resolution, `__file__` manipulation, and traceback handling.
*   **Staged Payload Extraction:** It follows a classic "dropper" pattern by extracting encrypted or bundled content from an internal archive into the system's `%TEMP%` directory before executing it as a Python script.
*   **Standardized Tooling Indicators:** The analysis identifies hallmarks of automated packaging tools (like PyInstaller) rather than custom-written malware code, used to obfuscate the final payload's true intent until runtime.
