# Threat Analysis Report

**Generated:** 2026-07-09 21:09 UTC
**Sample:** `0434437a073a3f3a49e84d5ecb20c99dd551bacc32bf100fbb8cf67a50642181_0434437a073a3f3a49e84d5ecb20c99dd551bacc32bf100fbb8cf67a50642181.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0434437a073a3f3a49e84d5ecb20c99dd551bacc32bf100fbb8cf67a50642181_0434437a073a3f3a49e84d5ecb20c99dd551bacc32bf100fbb8cf67a50642181.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 16,954,889 bytes |
| MD5 | `8bb75fd48b895157f7844f061a908845` |
| SHA1 | `ea3e94304172189db52b03b3491a346708408033` |
| SHA256 | `0434437a073a3f3a49e84d5ecb20c99dd551bacc32bf100fbb8cf67a50642181` |
| Overall entropy | 7.996 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769777721 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 172,032 | 6.489 | No |
| `.rdata` | 76,800 | 5.751 | No |
| `.data` | 3,584 | 1.839 | No |
| `.pdata` | 9,216 | 5.265 | No |
| `.rsrc` | 62,976 | 7.555 | ⚠️ Yes |
| `.reloc` | 2,048 | 5.281 | No |

### Imports

**USER32.dll**: `CreateWindowExW`, `ShutdownBlockReasonCreate`, `MsgWaitForMultipleObjects`, `ShowWindow`, `DestroyWindow`, `RegisterClassW`, `DefWindowProcW`, `PeekMessageW`, `DispatchMessageW`, `TranslateMessage`, `PostMessageW`, `GetMessageW`, `MessageBoxW`, `MessageBoxA`, `SystemParametersInfoW`
**COMCTL32.dll**: `ord_380`
**KERNEL32.dll**: `GetACP`, `IsValidCodePage`, `GetStringTypeW`, `GetFileAttributesExW`, `SetEnvironmentVariableW`, `FlushFileBuffers`, `GetCurrentDirectoryW`, `LCMapStringW`, `CompareStringW`, `FlsFree`, `GetOEMCP`, `GetCPInfo`, `GetModuleHandleW`, `MulDiv`, `FormatMessageW`
**ADVAPI32.dll**: `OpenProcessToken`, `GetTokenInformation`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `ConvertSidToStringSidW`
**GDI32.dll**: `SelectObject`, `DeleteObject`, `CreateFontIndirectW`

## Extracted Strings

Total strings found: **37214** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`Rich0\
`.rdata
@.data
.pdata
@.rsrc
@.reloc
WATAUAVAWH
0A_A^A]A\_
SUVWAVAWH
A_A^_^][
A_A^_^][
\$ UAVAWH
0A_A^]
0A_A^]
L$ SUVWH
T$hfD+D$df+T$`
@SUVWAVH
T$<f+T$4
PA^_^][
@USVWAVH
A^_^[]
|$ AVH
L$ SUVWH
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
VWAUAVAWH
0A_A^A]_^
@VAUAW
L9t$0t!H
L$ SVWH
@SUVWAV
A^_^][
unHcG(
@SUAUAVAWH
 A_A^A]][
uu
D8n
Ou
D8n
t*D8)t%3
C0L9k 
t*D8)u	
t/D8)u	
 A_A^A]][
~&D8s0u H
t$ AVH
l$ VWATAVAW
A_A^A\_^
\$0tH
l$ VWAVH
@VATAUAVAWH
 A_A^A]A\^
@SATAUAV
fD94xu
A^A]A\[
D$hH+D$pHi
SUVWATAUAVAWH
8A_A^A]A\_^][
SUVWATAUAVAWH
MP;H(s
MP;H8s
]Lu*A;|$
L$@E)}P
A;Exsf
E;E8v#A
L$@A9MP
tDE;u$t>H
T$8E+T$
XA_A^A]A\_^][
I@L9{8uH
t$HL9{0
}0L9{0
x<L9{0
K49K<u
@USWAUAVAWH
fD9(uA
A_A^A]_[]
u/HcH<H
WATAUAVAWH
A_A^A]A\_
WATAUAVAWH
 A_A^A]A\_
VWATAVAWH
 A_A^A\_^
WATAUAVAWH
A_A^A]A\_
H;XXs
H;xXu5
AUAVAWH
9;|
HcC
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400154f4` | `0x1400154f4` | 41265 | ✓ |
| `fcn.14001a410` | `0x14001a410` | 37350 | ✓ |
| `fcn.14001a3fc` | `0x14001a3fc` | 37300 | ✓ |
| `fcn.140025434` | `0x140025434` | 12817 | ✓ |
| `section..text` | `0x140001000` | 12386 | ✓ |
| `fcn.14000a230` | `0x14000a230` | 6161 | ✓ |
| `fcn.140027fc8` | `0x140027fc8` | 5645 | ✓ |
| `fcn.14002411c` | `0x14002411c` | 4750 | ✓ |
| `fcn.14002719c` | `0x14002719c` | 4156 | ✓ |
| `fcn.1400211cc` | `0x1400211cc` | 2201 | ✓ |
| `fcn.140005820` | `0x140005820` | 2013 | ✓ |
| `fcn.140016300` | `0x140016300` | 1946 | ✓ |
| `fcn.140011038` | `0x140011038` | 1909 | ✓ |
| `fcn.140015d84` | `0x140015d84` | 1777 | ✓ |
| `fcn.140029ea0` | `0x140029ea0` | 1661 | ✓ |
| `fcn.1400076b0` | `0x1400076b0` | 1570 | ✓ |
| `fcn.14000bf20` | `0x14000bf20` | 1501 | ✓ |
| `fcn.140028090` | `0x140028090` | 1451 | ✓ |
| `fcn.140021e5c` | `0x140021e5c` | 1405 | ✓ |
| `fcn.1400211d4` | `0x1400211d4` | 1353 | ✓ |
| `fcn.140004d30` | `0x140004d30` | 1292 | ✓ |
| `fcn.140009d30` | `0x140009d30` | 1270 | ✓ |
| `fcn.14000ea78` | `0x14000ea78` | 1231 | ✓ |
| `fcn.140009870` | `0x140009870` | 1211 | ✓ |
| `fcn.140023c80` | `0x140023c80` | 1180 | ✓ |
| `fcn.140008bd0` | `0x140008bd0` | 1152 | ✓ |
| `fcn.14001c610` | `0x14001c610` | 1141 | ✓ |
| `fcn.140013a14` | `0x140013a14` | 1124 | ✓ |
| `fcn.14000c5c0` | `0x14000c5c0` | 1123 | ✓ |
| `fcn.14001bacc` | `0x14001bacc` | 1101 | ✓ |

### Decompiled Code Files

- [`code/fcn.140004d30.c`](code/fcn.140004d30.c)
- [`code/fcn.140005820.c`](code/fcn.140005820.c)
- [`code/fcn.1400076b0.c`](code/fcn.1400076b0.c)
- [`code/fcn.140008bd0.c`](code/fcn.140008bd0.c)
- [`code/fcn.140009870.c`](code/fcn.140009870.c)
- [`code/fcn.140009d30.c`](code/fcn.140009d30.c)
- [`code/fcn.14000a230.c`](code/fcn.14000a230.c)
- [`code/fcn.14000bf20.c`](code/fcn.14000bf20.c)
- [`code/fcn.14000c5c0.c`](code/fcn.14000c5c0.c)
- [`code/fcn.14000ea78.c`](code/fcn.14000ea78.c)
- [`code/fcn.140011038.c`](code/fcn.140011038.c)
- [`code/fcn.140013a14.c`](code/fcn.140013a14.c)
- [`code/fcn.1400154f4.c`](code/fcn.1400154f4.c)
- [`code/fcn.140015d84.c`](code/fcn.140015d84.c)
- [`code/fcn.140016300.c`](code/fcn.140016300.c)
- [`code/fcn.14001a3fc.c`](code/fcn.14001a3fc.c)
- [`code/fcn.14001a410.c`](code/fcn.14001a410.c)
- [`code/fcn.14001bacc.c`](code/fcn.14001bacc.c)
- [`code/fcn.14001c610.c`](code/fcn.14001c610.c)
- [`code/fcn.1400211cc.c`](code/fcn.1400211cc.c)
- [`code/fcn.1400211d4.c`](code/fcn.1400211d4.c)
- [`code/fcn.140021e5c.c`](code/fcn.140021e5c.c)
- [`code/fcn.140023c80.c`](code/fcn.140023c80.c)
- [`code/fcn.14002411c.c`](code/fcn.14002411c.c)
- [`code/fcn.140025434.c`](code/fcn.140025434.c)
- [`code/fcn.14002719c.c`](code/fcn.14002719c.c)
- [`code/fcn.140027fc8.c`](code/fcn.140027fc8.c)
- [`code/fcn.140028090.c`](code/fcn.140028090.c)
- [`code/fcn.140029ea0.c`](code/fcn.140029ea0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This final segment of disassembly provides definitive confirmation of the binary's purpose and nature. The analysis now moves from "highly likely a Python wrapper" to "confirmed PyInstaller bootloader."

Here is the updated and expanded analysis incorporating Chunk 3:

### 1. Confirmed Bootloader Signature
The most significant finding in this section is the hardcoded string: **`L"PyInstallerOnefileHiddenWindow"`**.
*   **Context:** This is a specific internal identifier used by the PyInstaller tool. When a Python script is bundled into a single executable ("onefile"), the bootloader creates a hidden window to handle console input/output (stdin/stdout) without displaying a command prompt to the end-user.
*   **Function `fcn.140008bd0`:** This function acts as the primary initialization routine. It calls several Windows API functions:
    *   **`GetStartupInfoW`**: To determine how the application should start.
    *   **`CreateProcessW`**: Used to spawn the secondary process (the actual unpacked Python interpreter).
    *   **`RegisterClassW` & `CreateWindowExW`**: These are used to create the "Hidden Window" mentioned in the string. 
*   **Significance:** This confirms that this binary's primary role is not to perform malicious actions directly, but to act as a **wrapper/loader** for a Python-based application.

### 2. Advanced String and Buffer Processing
The functions **`fcn.140009d30`** and **`fcn.14001c610`** contain heavy logic regarding buffer management and character encoding.
*   **Decoding Logic:** The extensive use of bitwise shifts (`>>`), masks (`& 0x1f`), and nested loops in `fcn.140009d30` is characteristic of **UTF-8 or multi-byte character decoding**. Because Python handles Unicode as a first-class citizen, its C-based interpreter contains complex code to ensure strings are handled correctly across different systems.
*   **Write/Read Operations:** `fcn.14001c610` interacts with the `WriteFile` API and manages buffers during these operations. This is consistent with a system that handles large amounts of data or string output from a script.

### 3. Environment and Resource Initialization
*   **Environment Variables (`fcn.1400211d4`)**: This function utilizes **`SetEnvironmentVariableW`**. In the context of PyInstaller, this is used to set critical environment variables (like `PYTHONPATH` or `PYTHONHOME`) so that the bundled Python libraries can be located correctly after being unpacked into a temporary folder.
*   **File System Traversal (`fcn.140021e5c`)**: The presence of **`FindFirstFileExW`** and **`FindNextFileW`** indicates the bootloader is scanning for bundled `.pyc` files or dynamic libraries (`.dll/.so`) within its own internal structure.

### 4. Interpreter Dispatching
Function **`fcn.140013a14`** contains a large conditional tree (the "Ladder" of `if/else` and `case` logic).
*   **Interpretation:** This is likely an **opcode dispatcher** or a specialized handler for internal Python objects. It maps various types of internal data to specific C-functions. The complexity here isn't "obfuscation"; it is the overhead required to provide the flexibility of a high-level language (Python) over lower-level machine code.

---

### Updated Summary of Findings

| Component | Observation | Analysis |
| :--- | :--- | :--- |
| **Bootloader Identity** | String `L"PyInstallerOnefileHiddenWindow"` and `CreateProcessW` calls. | **Confirmed:** This is a PyInstaller "onefile" bootloader. Its role is to unpack/launch the Python environment. |
| **I/O Management** | Hidden window creation via `CreateWindowExW`. | Standard procedure for PyInstaller to allow console output while hiding the command prompt from the user. |
| **Decoding Logic** | Complex bitwise logic in `fcn.140009d30` related to buffer lengths and offsets. | High-level string/Unicode handling characteristic of the Python C-API implementation. |
| **System Setup** | Use of `SetEnvironmentVariableW` and `FindFirstFileExW`. | Infrastructure used to locate and "wire up" bundled Python libraries and modules. |
| **Malicious Indicators** | No evidence of keylogging, injection, or unauthorized network/data exfiltration found in these segments. | The complexity is a result of the massive scope of the Python interpreter being included in the binary. |

### Final Conclusion for Analysis

The investigation of all three chunks provides a clear picture: **This binary is a standard PyInstaller wrapper.**

The "complexity" observed in the disassembly (the large switch tables, high density of math/bit-shifting in string handling, and extensive logic for file discovery) is not a signature of manual malware crafting. Instead, it is the "footprint" of a very large software project—the Python language itself—being bundled into a single executable.

**The Triage Verdict:**
1.  **Is it malicious?** The *loader* (this binary) is functionally identical to those used by thousands of legitimate tools (e.g., Blender, various converters, and system utilities). 
2.  **Does the "wrapper" hide anything?** While the wrapper itself is standard, PyInstaller can be used to bundle any script. Therefore, while this specific code confirms a **Python environment**, a final determination on the *payload* (the actual Python script) would require extracting and analyzing the `.pyc` files from the bundled package.

The binary's behavior—creating a hidden window, setting environment variables, and managing complex string buffers—is consistent with its role as an automated launcher for scripted content.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The binary functions as a wrapper for a Python interpreter (confirmed by `PyInstaller` signatures) to execute scripts. |
| **T1614** | System Environment Variables | The use of `SetEnvironmentVariableW` is specifically noted to configure paths like `PYTHONPATH` for the internal environment. |
| **T1083** | File and Directory Discovery | The presence of `FindFirstFileExW` and `FindNextFileW` indicates the system is scanning for bundled `.pyc` files and libraries. |
| **T1036** | Masquerading | The creation of a "Hidden Window" (`CreateWindowExW`) hides the execution environment and console output from the end-user. |
| **T1127** | Obfuscated Executables | The use of a PyInstaller wrapper masks the original Python source code by bundling it into a single, complex binary. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *(None identified)*

### **File paths / Registry keys**
*   *(None identified - only standard Windows API calls were referenced without specific hardcoded paths).*

### **Mutex names / Named pipes**
*   *(None identified)*

### **Hashes**
*   *(None identified)*

### **Other artifacts**
*   **Internal Identifier:** `PyInstallerOnefileHiddenWindow` 
    *   *Note: This identifies the binary as a PyInstaller-wrapped executable. While not a direct indicator of malicious intent, it is a high-fidelity signature for identifying wrapped Python scripts/tools.*

***

**Analyst Note:** The provided text describes a standard **PyInstaller bootloader**. The "complexity" and "garbled strings" noted in the raw data are characteristic of a large software library (Python) being bundled into a single executable. No active command-and-control (C2) infrastructure, specific malicious file paths, or hardcoded credentials were identified in this sample.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Confirmed Bootloader Signature:** The presence of the string `L"PyInstallerOnefileHiddenWindow"` and the usage of `CreateProcessW` confirm this is a standard PyInstaller bootloader used to execute Python scripts packaged as single executables.
*   **Routine Environment Setup:** The use of `SetEnvironmentVariableW` (for `PYTHONPATH`) and `FindFirstFileExW` are characteristic of the initialization required by the Python interpreter rather than malicious commands or C2 communication.
*   **Absence of Malicious Payloads:** Detailed analysis shows no evidence of common malware behaviors such as keylogging, code injection, or unauthorized data exfiltration; the complexity observed is attributed to the inclusion of the Python standard library.
