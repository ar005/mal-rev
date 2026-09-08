# Threat Analysis Report

**Generated:** 2026-09-03 21:39 UTC
**Sample:** `13ee89082ab51d25549a46829ee13d44b04dce19db1f1334faab7294e5116b90_13ee89082ab51d25549a46829ee13d44b04dce19db1f1334faab7294e5116b90.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13ee89082ab51d25549a46829ee13d44b04dce19db1f1334faab7294e5116b90_13ee89082ab51d25549a46829ee13d44b04dce19db1f1334faab7294e5116b90.exe` |
| File type | PE32+ executable for MS Windows 5.02 (console), x86-64 (stripped to external PDB), 12 sections |
| Size | 8,186,368 bytes |
| MD5 | `26eca4737b804eea06cf2b426865e4d0` |
| SHA1 | `4703f920ef73913be9bb2ce209064db2118dcc3f` |
| SHA256 | `13ee89082ab51d25549a46829ee13d44b04dce19db1f1334faab7294e5116b90` |
| Overall entropy | 7.996 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1754487154 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 128,000 | 6.332 | No |
| `.data` | 512 | 1.27 | No |
| `.rdata` | 11,776 | 5.289 | No |
| `.eh_fram` | 512 | -0.0 | No |
| `.pdata` | 2,560 | 4.947 | No |
| `.xdata` | 3,072 | 4.461 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 4,096 | 4.256 | No |
| `.CRT` | 512 | 0.316 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 8,033,280 | 7.999 | ⚠️ Yes |
| `.reloc` | 512 | 1.766 | No |

### Imports

**KERNEL32.dll**: `AddDllDirectory`, `CloseHandle`, `CopyFileW`, `CreateDirectoryW`, `CreateFileMappingW`, `CreateFileW`, `CreateProcessW`, `DeleteCriticalSection`, `DeleteFileW`, `EnterCriticalSection`, `FindResourceA`, `FormatMessageA`, `FreeLibrary`, `GenerateConsoleCtrlEvent`, `GetCommandLineW`
**msvcrt.dll**: `__C_specific_handler`, `___lc_codepage_func`, `___mb_cur_max_func`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `__wargv`, `__wgetmainargs`, `__winitenv`, `_amsg_exit`, `_cexit`, `_commode`, `_errno`, `_fmode`, `_initterm`
**SHELL32.dll**: `CommandLineToArgvW`, `SHFileOperationW`, `SHGetFolderPathW`

## Extracted Strings

Total strings found: **20523** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.eh_fram
.pdata
@.xdata
.idata
@.reloc
f=MZt

AWAVAUATUWVSL
[^_]A\A]A^A_
[^_]A\A]A^A_
AVAUATUWVSL
[^_]A\A]A^
[^_]A\A]A^
AWAVAUATUWVSH
[^_]A\A]A^A_
H9D$xH
H9D$xu
t$0H9t$@
AWAVAUATUWVSH
[^_]A\A]A^A_
t$HL9t$
t$XL9t$
t$PL9t$
H9L$pM
H9L$pu
AWAVAUATUWVSH
?v[ff.
[^_]A\A]A^A_
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
\$8H9\$P
L9T$ ty
AWAVAUATUWVSH
[^_]A\A]A^A_
|$8H9|$@
L9D$@tyA
AWAVAUATUWVSH
[^_]A\A]A^A_
[^_]A\A]A^A_
AWAVAUATUWVSH
h[^_]A\A]A^A_
AWAVAUATUWVSH
l$,ff.
[^_]A\A]A^A_
AUATUWVSH
([^_]A\A]
([^_]A\A]
AVAUATUWVS
[^_]A\A]A^A_
L$8ff.
AUATUWVSH
x[^_]A\A]
AWAVAUATUWVSH
([^_]A\A]A^A_
AWAVAUATUWVSH
X[^_]A\A]A^A_
AWAVAUATUWVSH
D$8uiH
[^_]A\A]A^A_
AWAVAUATUWVSH
x[^_]A\A]A^A_
ATUWVSH
[^_]A\
AWAVAUATUWVSH
L$|D9L$T
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
H9|$`u	I9
ATUWVSH
0[^_]A\
AVAUATUWVS
[^_]A\A]A^A_
[^_]A\A]A^A_H
AWAVAUATUWVSH
[^_]A\A]A^A_
ATUWVSH
 [^_]A\
AWAVAUATUWVSH
([^_]A\A]A^A_
AUATUWVSH
([^_]A\A]
S(+{HH
([^_]A\A]
([^_]A\A]
AWAVAUATUWVSH
8[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
@wBH9|$P
H)D$PH
H)D$PH
H)D$PH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400077c0` | `0x1400077c0` | 101350 | ✓ |
| `fcn.140007d70` | `0x140007d70` | 99909 | ✓ |
| `fcn.14000d640` | `0x14000d640` | 77182 | ✓ |
| `fcn.140004290` | `0x140004290` | 11759 | ✓ |
| `fcn.14000af40` | `0x14000af40` | 8217 | ✓ |
| `fcn.14000f0d0` | `0x14000f0d0` | 5966 | ✓ |
| `fcn.14001cd3a` | `0x14001cd3a` | 5426 | ✓ |
| `fcn.140012d30` | `0x140012d30` | 5360 | ✓ |
| `fcn.140014220` | `0x140014220` | 5344 | ✓ |
| `fcn.140001e90` | `0x140001e90` | 4171 | ✓ |
| `fcn.140002ee0` | `0x140002ee0` | 4018 | ✓ |
| `fcn.140010840` | `0x140010840` | 3614 | ✓ |
| `fcn.1400121c0` | `0x1400121c0` | 2915 | ✓ |
| `fcn.140009170` | `0x140009170` | 2863 | ✓ |
| `fcn.14001bdb3` | `0x14001bdb3` | 2737 | ✓ |
| `fcn.1400192ae` | `0x1400192ae` | 2540 | ✓ |
| `fcn.140009ca0` | `0x140009ca0` | 2012 | ✓ |
| `fcn.14000a680` | `0x14000a680` | 1631 | ✓ |
| `fcn.1400059a0` | `0x1400059a0` | 1616 | ✓ |
| `fcn.14000cf60` | `0x14000cf60` | 1533 | ✓ |
| `fcn.14000e9c0` | `0x14000e9c0` | 1476 | ✓ |
| `fcn.140018b5d` | `0x140018b5d` | 1243 | ✓ |
| `fcn.14001b662` | `0x14001b662` | 1243 | ✓ |
| `fcn.140007370` | `0x140007370` | 1021 | ✓ |
| `fcn.140003ea0` | `0x140003ea0` | 1006 | ✓ |
| `fcn.1400182fd` | `0x1400182fd` | 970 | ✓ |
| `fcn.14001ae02` | `0x14001ae02` | 970 | ✓ |
| `fcn.140015700` | `0x140015700` | 912 | ✓ |
| `fcn.14001625e` | `0x14001625e` | 906 | ✓ |
| `fcn.14001778e` | `0x14001778e` | 899 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001e90.c`](code/fcn.140001e90.c)
- [`code/fcn.140002ee0.c`](code/fcn.140002ee0.c)
- [`code/fcn.140003ea0.c`](code/fcn.140003ea0.c)
- [`code/fcn.140004290.c`](code/fcn.140004290.c)
- [`code/fcn.1400059a0.c`](code/fcn.1400059a0.c)
- [`code/fcn.140007370.c`](code/fcn.140007370.c)
- [`code/fcn.1400077c0.c`](code/fcn.1400077c0.c)
- [`code/fcn.140007d70.c`](code/fcn.140007d70.c)
- [`code/fcn.140009170.c`](code/fcn.140009170.c)
- [`code/fcn.140009ca0.c`](code/fcn.140009ca0.c)
- [`code/fcn.14000a680.c`](code/fcn.14000a680.c)
- [`code/fcn.14000af40.c`](code/fcn.14000af40.c)
- [`code/fcn.14000cf60.c`](code/fcn.14000cf60.c)
- [`code/fcn.14000d640.c`](code/fcn.14000d640.c)
- [`code/fcn.14000e9c0.c`](code/fcn.14000e9c0.c)
- [`code/fcn.14000f0d0.c`](code/fcn.14000f0d0.c)
- [`code/fcn.140010840.c`](code/fcn.140010840.c)
- [`code/fcn.1400121c0.c`](code/fcn.1400121c0.c)
- [`code/fcn.140012d30.c`](code/fcn.140012d30.c)
- [`code/fcn.140014220.c`](code/fcn.140014220.c)
- [`code/fcn.140015700.c`](code/fcn.140015700.c)
- [`code/fcn.14001625e.c`](code/fcn.14001625e.c)
- [`code/fcn.14001778e.c`](code/fcn.14001778e.c)
- [`code/fcn.1400182fd.c`](code/fcn.1400182fd.c)
- [`code/fcn.140018b5d.c`](code/fcn.140018b5d.c)
- [`code/fcn.1400192ae.c`](code/fcn.1400192ae.c)
- [`code/fcn.14001ae02.c`](code/fcn.14001ae02.c)
- [`code/fcn.14001b662.c`](code/fcn.14001b662.c)
- [`code/fcn.14001bdb3.c`](code/fcn.14001bdb3.c)
- [`code/fcn.14001cd3a.c`](code/fcn.14001cd3a.c)

## Behavioral Analysis

This analysis incorporates the disassembly from **Chunk 5/5**, which constitutes the final portion of the provided code. This segment provides definitive evidence regarding the internal "engine" and "infrastructure" used to sustain the malicious payload within a compiled environment.

### New Observations & Functional Analysis (Chunk 5)

#### 1. Internal Object Mapping and Type Checking (`fcn.140007370`)
This function demonstrates complex conditional logic based on bitwise masks of memory addresses (e.g., `(arg2_00[1] & 0x80)`, `& 0x40`, `& 0x20`).
*   **Mechanism:** These checks are the standard way a Python interpreter identifies **object types**. In Nuitka, because everything (integers, strings, lists) is an object, it must constantly check "type flags" before performing operations. The complex logic to calculate offsets for different lengths of data indicates that the code is preparing to handle various types of internal pointers.
*   **Significance:** This confirms that the binary is not just a simple script; it contains the heavy-duty machinery required to manage the "types" of any data the malicious script might manipulate (e.g., switching logic between an integer counter and a string command).

#### 2. Sophisticated Buffer Traversal (`fcn.140003ea0`)
This function involves complex nested loops, pointer arithmetic, and offset calculations to traverse memory regions.
*   **Mechanism:** The pattern of calculating `(uVar8 >> 3) * -8` or similar math is typical for navigating **linked lists or contiguous arrays of objects** where the "next" item's position depends on the current object’s size.
*   **Significance:** This provides a mechanism for the malware to navigate complex internal data structures (like lists of IP addresses, a list of stolen credentials, or a dictionary of commands) efficiently without manual iteration in high-level code that would be easier to spot.

#### 3. String Formatting & Numerical Conversion (`fcn.14001778e`)
This function contains logic for converting numbers to strings, including handling signs (positive/negative), special characters (+/-), and leading zeros.
*   **Mechanism:** This is a classic implementation of `itoa` or a similar standard library utility, but specialized for the **Python Standard Library's string formatting.** 
*   **Significance:** The presence of this code implies that the script likely performs data manipulation—perhaps formatting stolen system information into a JSON string or a CSV format before exfiltration.

#### 4. Redundant String/Buffer Handlers (`fcn.1400182fd`, `fcn.14001ae02`)
These two functions are nearly identical in structure and logic, serving as "twin" implementations of buffer handling.
*   **Mechanism:** This is a hallmark of Nuitka's **redundancy strategy**. It creates multiple ways to access the same functionality (e.g., one for Unicode-safe strings and one for standard byte strings) to ensure that no matter how the original Python code was written, it will execute correctly in the compiled binary.
*   **Significance:** These are "cloaking" functions. They consume space and complexity, making it harder for an analyst to determine which specific piece of code is performing a malicious action versus what is just standard library overhead.

#### 5. Interning & Hash Lookups (`fcn.140015700`)
This function is very dense, involving bit-shifting and masking (e.g., `(uVar23 >> 1) + 3 + (uVar23 >> 3)`).
*   **Mechanism:** This is almost certainly part of the **Python String Interning or Hash Table** lookup mechanism. It allows for $O(1)$ lookups by ensuring that common strings/keys are stored in a specific way to speed up execution.
*   **Significance:** This confirms the binary has the capability to handle large "dictionaries" (key-value pairs). In malware, this is often used to map system commands or local configuration keys to remote server actions.

---

### Updated Technical Framework (Cumulative)

The integration of Chunk 5 completes our understanding of the underlying architecture:

| Phase | Action | Technical Implementation | Significance |
| :--- | :--- | :--- | :--- |
| **Initialization** | Environment Prep | `SetEnvironmentVariableW` | Sets up paths for Python/Nuitka components. |
| **Resolution** | Path Discovery | `GetTempPathW`, `SHGetFolderPathW` | Identifies where to "unpack" the hidden payload. |
| **Extraction** | Resource Loading | `FindResource`, `LoadResource` | Extracts the internal application from inside the `.exe`. |
| **Validation** | Integrity Check | Signature/Magic Number check (e.g., 'KAY') | Ensures the unpacked data is intact before execution. |
| **Mapping** | Memory Management | Large `malloc` calls; `memmove` operations | Places the "payload" into memory for runtime use. |
| **Translation** | **Runtime Logic Conversion** | **Switch Tables, Buffer Parsing (Chunk 4)** | **Nuitka-generated code to handle Python string/data types.** |
| **Engine Core** | **Data Management Infrastructure** | **Interning, Multi-type Support, Number Formatting (Chunk 5)** | **The heavy lifting required for the script's internal logic (Dicts, Lists, Strings).** |
| **Handoff** | Dynamic Loading | `LoadLibraryExW` & `GetProcAddress("run_code")` | Finds and executes the core logic of the actual program. |

---

### Final Synthesis & Risk Assessment

The inclusion of Chunk 5 provides the final "puzzle pieces" for the malware's profile:

**1. The Sophistication of the Wrapper (The "Trojan Horse")**
This binary is not a simple script; it is a **robustly engineered execution environment**. By using Nuitka, the attacker has effectively wrapped their Python-based toolkit in a high-performance C wrapper. This provides several advantages for the attacker:
*   **Evasion:** Most automated tools look for "scripting" behaviors (like `cmd.exe` calling a `.py` file). Here, all script logic is compiled into machine code.
*   **Complexity as Obfuscation:** The "infrastructure" functions (Chunk 4 and 5) act as a massive amount of **noise**. They are mathematically complex and logically dense but aren't "malicious"—they are just the mechanics of running Python in C.

**2. Hidden Functional Depth**
The presence of `fcn.14001778e` (Number to String) and `fcn.140015700` (Interning/Hash Tables) indicates that the final payload is likely **not just a simple "one-off" command.** It is designed to handle complex data structures—likely for sophisticated tasks like:
*   Compiling gathered intelligence into specific formats.
*   Mapping local system environment variables to remote C2 instructions.
*   Handling complex network protocols (where it needs to store and retrieve multiple states).

**3. Final Conclusion on Intent**
The analyst can now state with high confidence that this is a **sophisticated, multi-stage execution wrapper.** It uses the Nuitka compiler to create a "compilation shield." The actual malicious logic is likely hidden inside the `run_code` routine, which leverages these heavy-duty data handling functions to process its findings without raising typical "scripting" alarms.

**Refined Strategy for Final Analysis:**
The heavy lifting of "Data Handling" is now confirmed in Chunks 4 and 5. The next step in an incident response scenario would be **Memory Forensics at the `run_code` entry point.** By dumping the memory at the moment `GetProcAddress("run_code")` is called, investigators can bypass all of the Nuitka-generated "noise" seen in these chunks and examine the raw logic of the underlying script.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or system tools | The use of Nuitka creates a complex, "noisy" C wrapper with redundant handlers to hide Python logic and complicate manual analysis. |
| **T1496** | Archive Extraction | The malware utilizes `FindResource` and `LoadResource` to extract an internal application/payload from within the `.exe`. |
| **T1106** | Dynamic Resolution | The use of `GetProcAddress("run_code")` allows the payload to resolve its core execution logic at runtime rather than through static imports. |
| **T1036** | Deceptive Element | (Optional) The "redundant" and complex logic functions act as a diversionary layer to mask malicious code from analysts. |

### Analyst Notes on Mapping:
*   **Obfuscation Strategy:** While the behavior is technically "standard Python-to-C conversion," its presence in this context constitutes **T1027**. The analysis specifically highlights how the complexity serves as a "cloaking" mechanism to hide the actual intent of the script.
*   **Dynamic Resolution (T1106):** This is a direct mapping for the `GetProcAddress` behavior. It is a standard technique used by malware to bypass static analysis tools that look for specific suspicious function names in the Import Address Table (IAT).
*   **Archive Extraction (T1496):** The "Extraction" phase described in your technical framework—where internal components are pulled from within the `.exe`—is a classic indicator of a staged payload being hidden inside an initial loader.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** The provided data primarily contains metadata related to the **Nuitka compiler framework**, which is used to wrap Python scripts into executable binaries. Many items in the source text are standard library artifacts or internal compiler logic rather than specific infrastructure (like C2 IPs) intended for immediate blocking.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions using `GetTempPathW` and `SHGetFolderPathW`, but no specific hardcoded paths were extracted).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Execution Framework:** Nuitka (Identified via strings: `NUITKA_ONEFILE_START`, `NUITKA_ONEFILE_PARENT`, `NUITKA_ONEFILE_DIRECTORY`, `NUITKA_ORIGINAL_ARGV0`).
*   **Internal Entry Point:** `run_code` (This is the specific function name used by Nuitka to transition from the C-wrapper to the core logic).
*   **Integrity Check / Magic Number:** `KAY` (Identified in behavioral analysis as a potential signature check for the unpacked payload).

---

### **Analyst Summary**
The technical indicators suggest this is a **polyglot/wrapped malware specimen**. The presence of Nuitka-specific identifiers and the `run_code` entry point indicate that the malicious logic is not immediately visible in the high-level code but is embedded within the binary. 

While no immediate network IOCs (IPs/Domains) are present, the primary "artifact" for a SOC team would be the **Nuitka wrapper behavior**:
1.  The sample uses standard environment calls to find temporary paths (`GetTempPathW`) to unpack its true payload.
2.  It uses `run_code` as a transition point.
3.  Investigation should focus on memory forensics at the `run_code` entry point to extract the decrypted Python logic and associated network indicators.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High (regarding its role as a delivery vehicle)
4. **Key evidence**:
    *   **Nuitka Compilation Wrapper:** The presence of specific Nuitka signatures (`NUITKA_ONEFILE`, `run_code`) and complex, repetitive C-logic for handling Python data types indicates the sample is designed to hide malicious script logic inside a compiled "noise" layer.
    *   **Multi-stage Execution & Extraction:** The use of `FindResource`, `LoadResource`, and `GetTempPathW` confirms the sample acts as a stager/loader, extracting an internal payload from its own resource section into memory or a temporary directory.
    *   **Evasion via Dynamic Resolution:** The use of `GetProcAddress("run_code")` is a classic technique to bypass static analysis, ensuring that the primary malicious logic (the core script) only executes after the initial layers are successfully navigated.
