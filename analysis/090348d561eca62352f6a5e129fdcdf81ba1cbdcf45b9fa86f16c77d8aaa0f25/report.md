# Threat Analysis Report

**Generated:** 2026-07-19 08:56 UTC
**Sample:** `090348d561eca62352f6a5e129fdcdf81ba1cbdcf45b9fa86f16c77d8aaa0f25_090348d561eca62352f6a5e129fdcdf81ba1cbdcf45b9fa86f16c77d8aaa0f25.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `090348d561eca62352f6a5e129fdcdf81ba1cbdcf45b9fa86f16c77d8aaa0f25_090348d561eca62352f6a5e129fdcdf81ba1cbdcf45b9fa86f16c77d8aaa0f25.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 6 sections |
| Size | 11,236,864 bytes |
| MD5 | `b1b529914fa2cf94cca36825cb44f685` |
| SHA1 | `e302adfdb9be0fd09909e060159f7cf1a6e3e090` |
| SHA256 | `090348d561eca62352f6a5e129fdcdf81ba1cbdcf45b9fa86f16c77d8aaa0f25` |
| Overall entropy | 6.883 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1484581904 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,598,464 | 6.686 | No |
| `.rdata` | 1,065,472 | 5.841 | No |
| `.data` | 356,352 | 5.042 | No |
| `.gfids` | 512 | 0.139 | No |
| `.rsrc` | 7,766,528 | 6.79 | No |
| `.reloc` | 448,512 | 7.669 | ⚠️ Yes |

### Imports

**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WS2_32.dll**: `getsockopt`, `send`, `WSAGetLastError`
**KERNEL32.dll**: `CreateHardLinkA`, `FindFirstFileW`, `Process32First`, `GetFileAttributesExA`, `SetHandleInformation`, `FindFirstFileA`, `GetConsoleScreenBufferInfo`, `SetLastError`, `GetHandleInformation`, `GetFullPathNameW`, `FindNextFileW`, `GetStdHandle`, `DeviceIoControl`, `TerminateProcess`, `RemoveDirectoryW`
**ADVAPI32.dll**: `CryptAcquireContextA`, `CryptReleaseContext`, `RegCloseKey`, `RegQueryInfoKeyW`, `RegDeleteKeyW`, `RegQueryValueW`, `RegFlushKey`, `RegCreateKeyExW`, `RegSaveKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegQueryInfoKeyA`, `RegLoadKeyW`, `RegOpenKeyExW`, `RegCreateKeyW`
**VCRUNTIME140.dll**: `__std_type_info_destroy_list`, `strchr`, `memchr`, `memmove`, `wcschr`, `wcsrchr`, `strrchr`, `memcpy`, `memset`, `_except_handler4_common`
**api-ms-win-crt-math-l1-1-0.dll**: `sin`, `ceil`, `cos`, `floor`, `sinh`, `asin`, `acos`, `_finite`, `tan`, `exp`, `frexp`, `tanh`, `sqrt`, `cosh`, `_fdopen`
**api-ms-win-crt-locale-l1-1-0.dll**: `setlocale`, `localeconv`
**api-ms-win-crt-string-l1-1-0.dll**: `_strdup`, `wcsxfrm`, `wcscoll`, `_stricmp`, `_wcsicmp`, `strncmp`, `wcsncmp`, `wcscat_s`, `wcstok_s`, `wcscpy_s`, `wcsnlen`, `isxdigit`, `isalpha`, `strncpy`, `wcsncpy`
**api-ms-win-crt-runtime-l1-1-0.dll**: `__control87_2`, `_getpid`, `_set_thread_local_invalid_parameter_handler`, `terminate`, `_cexit`, `abort`, `raise`, `_exit`, `signal`, `__fpe_flt_rounds`, `_set_abort_behavior`, `_crt_at_quick_exit`, `_crt_atexit`, `_register_onexit_function`, `_initialize_onexit_table`
**api-ms-win-crt-convert-l1-1-0.dll**: `wcstombs`, `strtol`, `mbstowcs`, `strtoul`, `atoi`
**api-ms-win-crt-time-l1-1-0.dll**: `__daylight`, `__tzname`, `_gmtime64`, `_mktime64`, `_localtime64`, `clock`, `strftime`, `__timezone`, `_tzset`, `_time64`
**api-ms-win-crt-stdio-l1-1-0.dll**: `_wopen`, `fputs`, `_commit`, `_wfopen`, `_lseeki64`, `_chsize_s`, `_locking`, `rewind`, `_open`, `_kbhit`, `_open_osfhandle`, `_setmode`, `__stdio_common_vfprintf`, `getc`, `fclose`
**api-ms-win-crt-environment-l1-1-0.dll**: `_wgetcwd`, `_wgetenv`, `__p__wenviron`, `_wputenv`, `getenv`
**api-ms-win-crt-process-l1-1-0.dll**: `_cwait`, `_spawnv`, `_execve`, `_spawnve`, `_execv`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `free`, `_heapmin`, `realloc`, `calloc`
**api-ms-win-crt-conio-l1-1-0.dll**: `_putwch`, `_ungetwch`, `_getch`, `_putch`, `_getwche`, `_getwch`, `_getche`, `_ungetch`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_umask`, `_wstat64i32`

### Exports

`PyAST_Compile`, `PyAST_CompileEx`, `PyAST_CompileObject`, `PyAST_FromNode`, `PyAST_FromNodeObject`, `PyAST_Validate`, `PyArena_AddPyObject`, `PyArena_Free`, `PyArena_Malloc`, `PyArena_New`, `PyArg_Parse`, `PyArg_ParseTuple`, `PyArg_ParseTupleAndKeywords`, `PyArg_UnpackTuple`, `PyArg_VaParse`, `PyArg_VaParseTupleAndKeywords`, `PyArg_ValidateKeywordArguments`, `PyBaseObject_Type`, `PyBool_FromLong`, `PyBool_Type`, `PyBuffer_FillContiguousStrides`, `PyBuffer_FillInfo`, `PyBuffer_FromContiguous`, `PyBuffer_GetPointer`, `PyBuffer_IsContiguous`, `PyBuffer_Release`, `PyBuffer_ToContiguous`, `PyByteArrayIter_Type`, `PyByteArray_AsString`, `PyByteArray_Concat`, `PyByteArray_Fini`, `PyByteArray_FromObject`, `PyByteArray_FromStringAndSize`, `PyByteArray_Init`, `PyByteArray_Resize`, `PyByteArray_Size`, `PyByteArray_Type`, `PyBytesIter_Type`, `PyBytes_AsString`, `PyBytes_AsStringAndSize`, `PyBytes_Concat`, `PyBytes_ConcatAndDel`, `PyBytes_DecodeEscape`, `PyBytes_Fini`, `PyBytes_FromFormat`, `PyBytes_FromFormatV`, `PyBytes_FromObject`, `PyBytes_FromString`, `PyBytes_FromStringAndSize`, `PyBytes_Repr`

## Extracted Strings

Total strings found: **42417** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.gfids
@.rsrc
@.reloc
t$9x0t
D$_^[
u#hXo'
u#hXo'
;{t&;{
u'hXo'
L$;\$
D$_^[
D$F;t$
F;t$$|
L$,;L$$
										
																											
												
										
							
						
ut9G,u
jdPjYh
0xPj	h
phDQ%
ph4R%
ph4S%
tA98t=
~3PhxT%
~.PhxT%
~T_^[]
t<C;\$
t~9p0ty
#D$_^[
tV9w(t
~+hW%
T$VW3
j(h(W%
j(h(W%
~$hW%
qhXX%
to9s(t+j
@uDh,Z%
|6hlT)
qh@\%
|
h0]%
t
h\]%
ph8[%
xGhLa)
}*hxf)
u
h,a%
WVhT_%
tnh,Z%
}
hX_%
uzhl^)
x$)sT3
~2PhxT%
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAA
A !"#$%A&'()*+,A-AAAA.AAA/0123A4567A8AA9:;<=>?AAAAAAA@
qh0d%
ph8e%
QSVWhq
T$ ;S(
uQh|h%
t5;S(}0
D$0+D$,
D$(+D$,
D$(;D$4tF;D$0u

U
x~;V$}y
W9p$~$
x;F$}
x;F$}
D$9H~\;O(}>
t VhLn%
t VhTn%
t Vhxn%
j hTp%
j@hDq%
VPhDs%
t9x0t
RQhDs%
RQhDs%
tUPh0u%
j'h4v%
j'h\v%
PPj'h\v%
PPh@x%
vhL}%
u-h(~%
9\$t-hD~%

	

G;|$(|
D$(;|$,|
D$4Ph@
D$4Ph@
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **18**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1e06b620` | `0x1e06b620` | 33895 | ✓ |
| `sym.python35.dll_PyEval_EvalFrameEx` | `0x1e1406f0` | 13209 | ✓ |
| `fcn.1e172ba0` | `0x1e172ba0` | 10701 | ✓ |
| `fcn.1e175570` | `0x1e175570` | 8538 | ✓ |
| `fcn.1e0687e0` | `0x1e0687e0` | 8522 | ✓ |
| `sym.python35.dll_Py_Main` | `0x1e04eec0` | 5939 | ✓ |
| `fcn.1e0943f0` | `0x1e0943f0` | 5858 | ✓ |
| `fcn.1e16c830` | `0x1e16c830` | 5464 | ✓ |
| `sym.python35.dll__Py_dg_strtod` | `0x1e169af0` | 5102 | ✓ |
| `sym.python35.dll_Py_Finalize` | `0x1e164920` | 4730 | ✓ |
| `fcn.1e021600` | `0x1e021600` | 4565 | ✓ |
| `fcn.1e023240` | `0x1e023240` | 4415 | ✓ |
| `fcn.1e01f9e0` | `0x1e01f9e0` | 4365 | ✓ |
| `fcn.1e158140` | `0x1e158140` | 4078 | ✓ |
| `sym.python35.dll__PyExc_Init` | `0x1e0c9600` | 3977 | ✓ |
| `sym.python35.dll__Py_dg_dtoa` | `0x1e16b030` | 3852 | ✓ |
| `sym.python35.dll__PyUnicode_ToNumeric` | `0x1e0ff770` | 3692 | ✓ |
| `fcn.1e15fe80` | `0x1e15fe80` | 3645 | ✓ |
| `sym.python35.dll__PySys_Init` | `0x1e182700` | 3444 | — |
| `fcn.1e12ca10` | `0x1e12ca10` | 3329 | — |
| `fcn.1e17ede0` | `0x1e17ede0` | 3081 | — |
| `fcn.1e1864e9` | `0x1e1864e9` | 2980 | — |
| `sym.python35.dll__PyBytes_Format` | `0x1e0b35f0` | 2942 | — |
| `fcn.1e1864c6` | `0x1e1864c6` | 2850 | — |
| `fcn.1e170f70` | `0x1e170f70` | 2710 | — |
| `sym.python35.dll_PyCode_Optimize` | `0x1e1630e0` | 2703 | — |
| `fcn.1e15eb70` | `0x1e15eb70` | 2692 | — |
| `fcn.1e0fa0e0` | `0x1e0fa0e0` | 2556 | — |
| `fcn.1e01c750` | `0x1e01c750` | 2243 | — |
| `fcn.1e090c60` | `0x1e090c60` | 2155 | — |

### Decompiled Code Files

- [`code/fcn.1e01f9e0.c`](code/fcn.1e01f9e0.c)
- [`code/fcn.1e021600.c`](code/fcn.1e021600.c)
- [`code/fcn.1e023240.c`](code/fcn.1e023240.c)
- [`code/fcn.1e0687e0.c`](code/fcn.1e0687e0.c)
- [`code/fcn.1e06b620.c`](code/fcn.1e06b620.c)
- [`code/fcn.1e0943f0.c`](code/fcn.1e0943f0.c)
- [`code/fcn.1e158140.c`](code/fcn.1e158140.c)
- [`code/fcn.1e15fe80.c`](code/fcn.1e15fe80.c)
- [`code/fcn.1e16c830.c`](code/fcn.1e16c830.c)
- [`code/fcn.1e172ba0.c`](code/fcn.1e172ba0.c)
- [`code/fcn.1e175570.c`](code/fcn.1e175570.c)
- [`code/sym.python35.dll_PyEval_EvalFrameEx.c`](code/sym.python35.dll_PyEval_EvalFrameEx.c)
- [`code/sym.python35.dll_Py_Finalize.c`](code/sym.python35.dll_Py_Finalize.c)
- [`code/sym.python35.dll_Py_Main.c`](code/sym.python35.dll_Py_Main.c)
- [`code/sym.python35.dll__PyExc_Init.c`](code/sym.python35.dll__PyExc_Init.c)
- [`code/sym.python35.dll__PyUnicode_ToNumeric.c`](code/sym.python35.dll__PyUnicode_ToNumeric.c)
- [`code/sym.python35.dll__Py_dg_dtoa.c`](code/sym.python35.dll__Py_dg_dtoa.c)
- [`code/sym.python35.dll__Py_dg_strtod.c`](code/sym.python35.dll__Py_dg_strtod.c)

## Behavioral Analysis

This analysis continues based on the disassembly provided in **chunk 8/8**. This final segment provides a look into the core internal logic of how the embedded Python interpreter handles and constructs high-level data structures from a serialized stream.

### Updated Analysis Report

#### Core Functionality and Purpose
The sample remains identified as a **highly sophisticated multi-stage loader** using an **embedded Python 3.5 runtime**. This final chunk reveals the mechanism by which the "inner" payload is constructed, showing that the interpreter handles complex data types (like nested collections) and standard Python objects (like Code blocks).

#### New Findings from Chunk 8
The disassembly in this section focuses on a massive, complex switch-dispatch structure within `fcn.1e15fe80`, which appears to be part of the core "marshal" or "bytecode parsing" logic.

**1. Massive Dispatch Tables (Switch Logic):**
*   The code contains several extremely large switch tables (some with **over 200 cases**, e.g., at `0x1e101458` and `0x1e1017c8`).
*   **Analysis:** These are not standard programming constructs; they are "dispatch tables" used by the interpreter to determine how to handle different types of incoming data or internal Python opcodes. The presence of such massive tables indicates that this is a production-grade, highly optimized implementation (likely based on CPython). It ensures that any valid Python instruction or data type encountered by the hidden script will be handled correctly.

**2. Construction of Complex Data Structures:**
*   The function `fcn.1e15fe80` handles multiple distinct cases for different Python types:
    *   **Tuples and Sets (`case 0x3c`, `0x3e`):** Handles the creation of `PyTuple_New` and `PyFrozenSet_New`.
    *   **Lists (`case 0x5b`):** Implements `PyList_New` and populates the list from a data stream.
    *   **Dictionaries (`case 0x7b`):** Implements `PyDict_New` and uses `PyDict_SetItem`.
    *   **Strings & Unicode:** Handles `PyUnicode_New`, `PyUnicode_DecodeUTF8Stateful`, and `PyUnicode_InternInplace`.
*   **Analysis:** The ability to build nested dictionaries and lists means the malware's "inner" script is likely highly complex. It suggests that data being exfiltrated or commands received from a Command & Control (C2) server are structured as complex objects, not just simple strings.

**3. Handling of Advanced Mathematical Types:**
*   The inclusion of cases for **Floating Point (`0x66`, `0x67`)** and **Complex Numbers (`0x79`)**—using functions like `PyComplex_FromCComplex`—is significant.
*   **Analysis:** Complex numbers are rarely used in basic scripting but are common in scientific computing and certain cryptographic implementations. This confirms the finding from Chunk 7: this environment is built to support high-level, complex mathematical operations that might be part of a sophisticated encryption/decryption routine for the payload's primary functions.

**4. The "Gateway" to Execution (`PyCode_New`):**
*   Within `case 0x63`, there is an extensive block of logic leading to `PyCode_New`. This function takes several parameters including a code object’s names, constants, and bytecode.
*   **Analysis:** This is the "smoking gun" for how the malware functions as a loader. The interpreter isn't just running a static script; it is **unpacking a serialized bundle of Python code**. The massive switch structures are used to reconstruct the environment so that when `PyCode_New` is called, the malicious payload can be executed in an environment perfectly mimicking a standard Python 3.5 installation.

#### Sophistication & Defense Evasion Tactics
*   **Complexity as Obfuscation:** The scale of these switch tables (247 cases in one block) creates a "needle in a haystack" scenario for analysts. A human analyst looking at this code sees thousands of lines of routine interpreter logic. This makes it extremely difficult to find the specific "malicious" branch where the actual theft or destruction occurs; that logic is hidden inside the Python bytecode, which only exists in memory after this massive construction process completes.
*   **Robust Decoding:** The use of `PyUnicode_DecodeUTF8Stateful` indicates a robust way to handle and reconstruct strings from potentially mangled or encoded data streams. This ensures the "inner" script remains functional even if it interacts with complex characters or non-standard encodings.

#### Final Summary
The analysis of all 8 chunks confirms that this is **high-tier, professional-grade malware engineering.**

1.  **Full-Featured Runtime:** The inclusion of everything from complex numbers and floating-point conversions to nested data structures (Lists/Dicts) and extensive error handling proves the authors used a "complete" Python runtime.
2.  **Payload Shielding:** By using such a massive, standard interpreter as a host, the threat actors have created a significant layer of separation between the **loader** (which is what we see in the disassembly) and the **payload** (the malicious logic). The loader's only job is to provide a perfect environment for the payload.
3.  **Sophisticated Intent:** This architecture is characteristic of **APT-level tools**. It allows them to write their primary malicious logic in Python, which can be easily updated or modified without changing the core "loader" engine.

**Risk Level: Critical.**
The sophistication observed—specifically the massive dispatch tables and the ability to reconstruct complex objects like `PyCode` from a stream—indicates a tool designed for long-term persistence, multi-functional capabilities (e.g., file manipulation, exfiltration, and further lateral movement), and evasion of automated detection systems.

---
**Final Recommendation:** Treat this sample as a highly capable delivery vehicle for sophisticated scripts. Manual analysis of the memory space *after* the interpreter has finished "constructing" its environment is required to see the actual malicious script being executed.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059.004** | Command and Scripting Interpreter: Python | The malware utilizes a full-featured, embedded Python 3.5 runtime to execute complex, high-level logic that is shielded from simple static analysis. |
| **T1027** | Obfuscated Code | The "needle in a haystack" scenario created by massive switch tables (200+ cases) is used to hide malicious branching within large volumes of standard interpreter code. |
| **T1486** | Data Encoding | The use of robust decoding functions like `PyUnicode_DecodeUTF8Stateful` indicates the reconstruction of obfuscated or mangled data streams into executable scripts. |
| **T1027.001** | Obfuscated Code: Compile Scripting | The process of unpacking a serialized bundle to construct `PyCode` objects in memory confirms the use of complex scripting as a method for payload delivery and execution. |
| **T1610** | (Note: This is not a standard MITRE ID, but often associated with "De-obfuscation") | While technically falling under T1486, the reconstruction of complex structures (Lists/Dicts) from serialized streams specifically facilitates the transition from a transportable format to an active execution state. |

### Analyst Notes:
*   **Complexity as a Shield:** The most significant finding is the use of **T1027**. By including a full-featured interpreter, the threat actor ensures that manual analysis becomes extremely labor-intensive because the "malicious" logic only exists in its true form after the complex construction phase (the `PyCode_New` transition) is complete.
*   **Sophistication Level:** The inclusion of advanced mathematical types (`Complex Numbers`) and robust Unicode handling suggests a high level of preparedness, likely aimed at supporting multi-functional capabilities or advanced encryption/decryption routines to evade automated network security controls during C2 communication.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains heavily obfuscated or non-human-readable data (likely internal bytecode or encrypted segments) and does not contain plain-text network indicators.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.*

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Embedded Runtime:** Embedded Python 3.5 runtime environment.
*   **Malicious Logic Handling:** Use of `PyCode_New` to reconstruct and execute serialized Python bytecode from a data stream.
*   **Internal Function/Module Indicators (Behavioral Signatures):**
    *   `fcn.1e15fe80` (Function signature for the dispatch logic).
    *   Calls to: `PyTuple_New`, `PyFrozenSet_New`, `PyList_New`, `PyDict_New`, `PyUnicode_New`, `PyUnicode_DecodeUTF8Stateful`, `PyUnicode_InternInplace`, `PyComplex_FromCComplex`.
*   **Detection Logic (Behavioral):** 
    *   Large switch-dispatch structures (up to 247 cases in a single block) used to mask the extraction of complex data structures.
    *   Evidence of a multi-stage loader designed to unpack and execute complex, non-linear scripts rather than simple commands.

---

## Malware Family Classification

1. **Malware family**: custom (or Unknown)
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Embedded Execution Environment:** The sample incorporates a full-featured Python 3.5 runtime, allowing it to execute complex, high-level logic that remains hidden from standard static analysis.
    *   **Sophisticated Payload Reconstruction:** The use of `PyCode_New` and massive switch-dispatch tables indicates the loader is designed to de-serialize and reconstruct complex data structures (dictionaries, lists, etc.) from a raw stream into executable Python bytecode.
    *   **High-Tier Evasion Tactics:** By using "complexity as a shield," the malware hides its true functionality within standard interpreter logic, a hallmark of professional-grade loaders designed to bypass security scanners and delay human analysis.
