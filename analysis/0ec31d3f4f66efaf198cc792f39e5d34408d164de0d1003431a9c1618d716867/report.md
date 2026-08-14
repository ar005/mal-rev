# Threat Analysis Report

**Generated:** 2026-08-14 00:11 UTC
**Sample:** `0ec31d3f4f66efaf198cc792f39e5d34408d164de0d1003431a9c1618d716867_0ec31d3f4f66efaf198cc792f39e5d34408d164de0d1003431a9c1618d716867.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ec31d3f4f66efaf198cc792f39e5d34408d164de0d1003431a9c1618d716867_0ec31d3f4f66efaf198cc792f39e5d34408d164de0d1003431a9c1618d716867.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 7 sections |
| Size | 15,655,177 bytes |
| MD5 | `a32a8cbbf04e4fe24a293ea6c4bf1044` |
| SHA1 | `315e6ef9a99ba79c394a0369d202ee1228b3fce8` |
| SHA256 | `0ec31d3f4f66efaf198cc792f39e5d34408d164de0d1003431a9c1618d716867` |
| Overall entropy | 7.996 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770697541 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 184,832 | 6.484 | No |
| `.rdata` | 79,872 | 5.755 | No |
| `.data` | 3,584 | 1.826 | No |
| `.pdata` | 9,728 | 5.328 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 61,440 | 7.35 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.271 | No |

### Imports

**USER32.dll**: `TranslateMessage`, `ShutdownBlockReasonCreate`, `GetWindowThreadProcessId`, `SetWindowLongPtrW`, `GetWindowLongPtrW`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `CreateWindowExW`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `GetMessageW`
**KERNEL32.dll**: `GetTimeZoneInformation`, `GetProcessHeap`, `FreeEnvironmentStringsW`, `GetEnvironmentStringsW`, `GetCPInfo`, `GetOEMCP`, `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetLastError`, `FreeLibrary`, `GetProcAddress`, `LoadLibraryExW`, `FormatMessageW`, `GetModuleFileNameW`
**ADVAPI32.dll**: `ConvertSidToStringSidW`, `GetTokenInformation`, `OpenProcessToken`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`

## Extracted Strings

Total strings found: **33961** (showing first 100)

```
!This program cannot be run in DOS mode.
$
}RichCZ
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
L$ SUVWH
L$ SVWH
L$ SVWH
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
@UVWAT
L9t$0t
tM@8(tHH
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
t$ WATAUAVAWH
~#E8n0u
0A_A^A]A\_
SUVWATAUAWH
0A_A]A\_^][
0A_A]A\_^][
l$ VWATAVAW
A_A^A\_^
|$ AVH
l$ VWAVH
WAVAWH
0A_A^_
@SUVWAV
A^_^][
@VATAUAVAWH
 A_A^A]A\^
@SUATAU
A]A\][
D$hH+D$pHi
t);\$8u#3
|$8fff
SUVWATAUAVAWH
8A_A^A]A\_^][
SUVWATAUAVAWH
MP;H(s
MP;H8s
]Lu*A;|$
L$@E)}P
A;Exsg
E;E8v#A
L$@A9MP
tDE;u$t>H
T$8E+T$
XA_A^A]A\_^][
tHH9
uC
I@L9{8uH
t$HL9{0
~0L9{0
y<L9{0
\$ UVAVH
@USWATAVAWH
fD9 uA
A_A^A\_[]
u0HcH<
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
t$ WATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140018c5c` | `0x140018c5c` | 40457 | ✓ |
| `fcn.14001ca40` | `0x14001ca40` | 38835 | ✓ |
| `fcn.14001ca2c` | `0x14001ca2c` | 38794 | ✓ |
| `main` | `0x140001000` | 14511 | ✓ |
| `fcn.140028080` | `0x140028080` | 12889 | ✓ |
| `fcn.14000a620` | `0x14000a620` | 6161 | ✓ |
| `fcn.140003e40` | `0x140003e40` | 5935 | ✓ |
| `fcn.14002ac50` | `0x14002ac50` | 5703 | ✓ |
| `fcn.140026d6c` | `0x140026d6c` | 4735 | ✓ |
| `fcn.140001c80` | `0x140001c80` | 2338 | ✓ |
| `fcn.140023d0c` | `0x140023d0c` | 2201 | ✓ |
| `fcn.14001822c` | `0x14001822c` | 1946 | ✓ |
| `fcn.140011400` | `0x140011400` | 1898 | ✓ |
| `fcn.140017c3c` | `0x140017c3c` | 1777 | ✓ |
| `fcn.14002cbb0` | `0x14002cbb0` | 1661 | ✓ |
| `fcn.140014f04` | `0x140014f04` | 1532 | ✓ |
| `fcn.14000c310` | `0x14000c310` | 1468 | ✓ |
| `fcn.14002ad20` | `0x14002ad20` | 1451 | ✓ |
| `fcn.140002880` | `0x140002880` | 1422 | ✓ |
| `fcn.140024a0c` | `0x140024a0c` | 1421 | ✓ |
| `fcn.140015500` | `0x140015500` | 1397 | ✓ |
| `fcn.140023d14` | `0x140023d14` | 1353 | ✓ |
| `fcn.14001455c` | `0x14001455c` | 1336 | ✓ |
| `fcn.140005230` | `0x140005230` | 1325 | ✓ |
| `fcn.14000edec` | `0x14000edec` | 1263 | ✓ |
| `fcn.14000a140` | `0x14000a140` | 1238 | ✓ |
| `fcn.140009ca0` | `0x140009ca0` | 1179 | ✓ |
| `fcn.14001ec90` | `0x14001ec90` | 1171 | ✓ |
| `fcn.1400268e0` | `0x1400268e0` | 1164 | ✓ |
| `fcn.140008ee0` | `0x140008ee0` | 1152 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001c80.c`](code/fcn.140001c80.c)
- [`code/fcn.140002880.c`](code/fcn.140002880.c)
- [`code/fcn.140003e40.c`](code/fcn.140003e40.c)
- [`code/fcn.140005230.c`](code/fcn.140005230.c)
- [`code/fcn.140008ee0.c`](code/fcn.140008ee0.c)
- [`code/fcn.140009ca0.c`](code/fcn.140009ca0.c)
- [`code/fcn.14000a140.c`](code/fcn.14000a140.c)
- [`code/fcn.14000a620.c`](code/fcn.14000a620.c)
- [`code/fcn.14000c310.c`](code/fcn.14000c310.c)
- [`code/fcn.14000edec.c`](code/fcn.14000edec.c)
- [`code/fcn.140011400.c`](code/fcn.140011400.c)
- [`code/fcn.14001455c.c`](code/fcn.14001455c.c)
- [`code/fcn.140014f04.c`](code/fcn.140014f04.c)
- [`code/fcn.140015500.c`](code/fcn.140015500.c)
- [`code/fcn.140017c3c.c`](code/fcn.140017c3c.c)
- [`code/fcn.14001822c.c`](code/fcn.14001822c.c)
- [`code/fcn.140018c5c.c`](code/fcn.140018c5c.c)
- [`code/fcn.14001ca2c.c`](code/fcn.14001ca2c.c)
- [`code/fcn.14001ca40.c`](code/fcn.14001ca40.c)
- [`code/fcn.14001ec90.c`](code/fcn.14001ec90.c)
- [`code/fcn.140023d0c.c`](code/fcn.140023d0c.c)
- [`code/fcn.140023d14.c`](code/fcn.140023d14.c)
- [`code/fcn.140024a0c.c`](code/fcn.140024a0c.c)
- [`code/fcn.1400268e0.c`](code/fcn.1400268e0.c)
- [`code/fcn.140026d6c.c`](code/fcn.140026d6c.c)
- [`code/fcn.140028080.c`](code/fcn.140028080.c)
- [`code/fcn.14002ac50.c`](code/fcn.14002ac50.c)
- [`code/fcn.14002ad20.c`](code/fcn.14002ad20.c)
- [`code/fcn.14002cbb0.c`](code/fcn.14002cbb0.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

Based on the additional disassembly provided in chunk 3/3, I have updated and expanded the analysis of the binary's functionality. The newest segment contains "smoking gun" evidence regarding the construction of the file while further detailing how the author uses a complex environment to mask the core payload.

### Updated Analysis Summary

The final set of disassembled functions confirms that this is not a custom-written malware binary in the traditional sense, but rather a **standard PyInstaller bundle**. The specific references to "PyInstallerOnefileHiddenWindow" and the massive amounts of internal string/memory management code confirm that the executable's primary role is to host a Python environment.

---

### New Findings & Technical Details

#### 1. Definitive Confirmation: PyInstaller Infrastructure
The function `fcn.140008ee0` contains a very specific string constant: **"PyInstallerOnefileHiddenWindow"**.
*   **Analysis:** This confirms that the executable was created using **PyInstaller** in "onefile" mode. This mode bundles the entire Python interpreter and all required libraries into a single `.exe`. The "HiddenWindow" portion indicates it is configured to run without a console window, which is a common technique used by both legitimate tools (like background services) and malware (to hide activity from the user).
*   **Significance:** This confirms that the majority of the complex code in this chunk belongs to the PyInstaller bootloader. It handles the unpacking of the internal files into a temporary directory, sets up environment variables, and prepares the Python environment before launching the actual script.

#### 2. Environment Manipulation (Environment Variables)
The function `fcn.140023d14` involves calls to **`SetEnvironmentVariableW`**.
*   **Analysis:** In a PyInstaller context, this is typically used by the bootloader to set `PYTHONHOME`, `PATH`, and other variables necessary to locate bundled libraries (DLLs/so files).
*   **Security Note:** While setting environment variables can be used for malicious purposes (e.g., changing the path for a system utility), here it confirms the "bootstrap" nature of the code—it is preparing the stage for the Python script to run.

#### 3. Complex String & Memory Parsing
Functions like `fcn.140015500` and `fcn.14000a140` are massive, complex loops involving heavy logic to parse memory blocks.
*   **Analysis:** These appear to be internal **Python C-API functions** for handling strings and variable-length character data (likely handling Unicode or multi-byte characters). The complexity of these functions is a result of the Python language's requirement to handle many different types of string encodings.
*   **Security Note:** These functions represent "heavy" code that provides no direct evidence of malicious intent but creates significant overhead for an analyst trying to navigate the binary manually.

#### 4. File System Iteration (Search Logic)
The function `fcn.140024a0c` uses **`FindFirstFileExW`** and **`FindNextFileW`**.
*   **Analysis:** This code is scanning for files based on specific patterns or names. In the context of PyInstaller, this is often part of the library-loading process where the interpreter looks for available modules in the unpacked directory.

---

### Updated Summary of Behavior & Risks

The analysis now provides a near-complete picture of the binary's structure:

1.  **Layered Wrapping (Confirmed):** The presence of "PyInstallerOnefileHiddenWindow" confirms that this is a **wrapper**. The malicious logic is not located in these assembly instructions; it resides in Python `.pyc` files stored inside the executable’s resources.
2.  **Complexity as Obfuscation:** The inclusion of Tcl/Tk support (from chunk 1), AVX math libraries (from chunk 2), and complex string-handling logic (from chunk 3) creates a massive "noise" floor. This makes it very difficult to identify specific malicious behaviors through static analysis of the `.exe` alone.
3.  **Execution Flow:** The code is designed to:
    *   Start in a hidden window.
    *   Bootstrap a Python environment (setting variables, loading DLLs).
    *   Extract/load internal resources.
    *   Execute a script (the actual payload) within that environment.

### Final Recommendation for Analysis

Because the binary is confirmed as a PyInstaller bundle, **further manual disassembly of this specific executable will yield diminishing returns.** The "malicious" actions (e.g., keylogging, data exfiltration, etc.) are likely contained in the Python script itself.

**Next Steps:**
1.  **Extraction:** Use `pyinstxtractor.py` to unpack the executable. This is the industry-standard tool for this specific scenario.
2.  **Identify Py Files:** Look for files ending in `.pyc` (e.g., `main.pyc` or files within a `lib` folder).
3.  **Decompile Script:** Use `uncompyle6` or `pycdc` to convert the `.pyc` files back into readable Python source code. This is where you will find the actual logic, hardcoded IPs, and intended behaviors of the malware.

**Conclusion:** The binary is a sophisticated "wrapper" for a Python script. While the assembly looks complex and potentially suspicious, it is mostly standard boilerplate code used to create portable Python applications. The core threat is hidden one layer deeper in the bundled scripts.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of a PyInstaller "onefile" bundle hides the actual Python scripts within a complex binary, while the "HiddenWindow" configuration masks activity from the user. |
| T1134 | Modify Environment Variables | The execution of `SetEnvironmentVariableW` is used to configure environment variables (like PATH and PYTHONHOME) required to bootstrap the internal payload. |
| T1083 | File and Directory Discovery | The use of `FindFirstFileExW` and `FindNextFileW` indicates the system is scanning the filesystem for specific files or libraries. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (While `FindFirstFileExW` and `FindNextFileW` were used in behavior, no specific malicious paths were listed).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **PyInstallerOnefileHiddenWindow**: (Internal identifier indicating the use of a PyInstaller "onefile" bundle with a hidden window flag. This identifies the packer/wrapper type used to bundle the Python payload).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Wrapper
3. **Confidence**: High

**Key evidence**:
*   **PyInstaller Infrastructure:** The presence of the specific string `PyInstallerOnefileHiddenWindow` confirms that the binary functions as a standard PyInstaller wrapper, designed to bundle and execute Python scripts while hiding the console window from the user.
*   **Obfuscation via "Noise":** The analysis highlights that the complex memory management, Tcl/Tk support, and AVX math libraries serve as significant overhead (noise) to mask the core payload, a common technique to hinder manual disassembly of the host executable.
*   **Decoupled Logic:** The behavior indicates that while the binary is suspicious and designed for evasion, the actual malicious functionality (e.g., keylogging or data theft) resides in encapsulated Python `.pyc` files rather than the assembly code of the .exe itself.
