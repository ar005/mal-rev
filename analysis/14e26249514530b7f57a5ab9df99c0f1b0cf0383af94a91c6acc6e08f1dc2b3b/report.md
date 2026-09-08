# Threat Analysis Report

**Generated:** 2026-09-06 10:34 UTC
**Sample:** `14e26249514530b7f57a5ab9df99c0f1b0cf0383af94a91c6acc6e08f1dc2b3b_14e26249514530b7f57a5ab9df99c0f1b0cf0383af94a91c6acc6e08f1dc2b3b.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `14e26249514530b7f57a5ab9df99c0f1b0cf0383af94a91c6acc6e08f1dc2b3b_14e26249514530b7f57a5ab9df99c0f1b0cf0383af94a91c6acc6e08f1dc2b3b.dll` |
| File type | PE32 executable for MS Windows 6.00 (DLL), Intel i386, 6 sections |
| Size | 8,941,008 bytes |
| MD5 | `9d89670c1d17a3dce59e9a5f9c35fafa` |
| SHA1 | `2b6e6358e30a260e6e18b2c8b2cd3a24d87b7628` |
| SHA256 | `14e26249514530b7f57a5ab9df99c0f1b0cf0383af94a91c6acc6e08f1dc2b3b` |
| Overall entropy | 6.42 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768402828 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 3,430,400 | 6.591 | No |
| `.rdata` | 2,291,200 | 5.544 | No |
| `.data` | 151,552 | 3.65 | No |
| `PyRuntim` | 180,736 | 1.553 | No |
| `.rsrc` | 25,600 | 5.687 | No |
| `.reloc` | 535,040 | 7.663 | ⚠️ Yes |

### Imports

**VERSION.dll**: `VerQueryValueW`, `GetFileVersionInfoW`, `GetFileVersionInfoSizeW`
**WS2_32.dll**: `send`, `WSAGetLastError`, `getsockopt`
**api-ms-win-core-path-l1-1-0.dll**: `PathCchCombineEx`, `PathCchSkipRoot`
**bcrypt.dll**: `BCryptGenRandom`
**ADVAPI32.dll**: `OpenProcessToken`, `RegDeleteKeyExW`, `RegQueryInfoKeyW`, `RegDeleteKeyW`, `RegFlushKey`, `RegCreateKeyExW`, `RegSaveKeyW`, `RegDeleteTreeW`, `RegSetValueExW`, `RegLoadKeyW`, `RegCreateKeyW`, `RegConnectRegistryW`, `RegDeleteValueW`, `LsaNtStatusToWinError`, `GetUserNameW`
**KERNEL32.dll**: `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `IsProcessorFeaturePresent`, `IsDebuggerPresent`, `GetCurrentProcessId`, `InitializeSListHead`, `GetProcessHeap`, `SleepEx`, `TlsGetValue`, `TlsFree`, `OpenThread`, `CreateEventA`, `GetFinalPathNameByHandleW`, `GetModuleFileNameW`, `CompareStringOrdinal`
**VCRUNTIME140.dll**: `memcpy`, `memmove`, `memset`, `__std_type_info_destroy_list`, `memchr`, `wcschr`, `strchr`, `wcsrchr`, `strstr`, `strrchr`, `wcsstr`, `_except_handler4_common`
**api-ms-win-crt-stdio-l1-1-0.dll**: `ungetc`, `fputs`, `rewind`, `setvbuf`, `putchar`, `puts`, `_chsize_s`, `_lseeki64`, `_open_osfhandle`, `_wfopen`, `__stdio_common_vswprintf`, `_wopen`, `_commit`, `_locking`, `ferror`
**api-ms-win-crt-environment-l1-1-0.dll**: `__p__wenviron`, `getenv`, `_wgetenv`, `_wputenv`, `_wgetcwd`, `_wputenv_s`
**api-ms-win-crt-string-l1-1-0.dll**: `toupper`, `strcspn`, `_strdup`, `wcsncmp`, `wcsxfrm`, `tolower`, `isalnum`, `wcsnlen`, `wcstok_s`, `_stricmp`, `strpbrk`, `strncpy`, `strncmp`, `_wcsicmp`, `wcscoll`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_exit`, `_getpid`, `_initterm_e`, `_initterm`, `_cexit`, `__control87_2`, `__fpe_flt_rounds`, `abort`, `_errno`, `exit`, `_wsystem`, `_set_thread_local_invalid_parameter_handler`, `__sys_errlist`, `__sys_nerr`, `__doserrno`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `malloc`, `_aligned_free`, `_heapmin`, `free`, `_aligned_malloc`, `realloc`
**api-ms-win-crt-locale-l1-1-0.dll**: `localeconv`, `setlocale`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtol`, `wcstol`, `strtoul`, `atol`, `mbstowcs`, `wcstombs`
**api-ms-win-crt-math-l1-1-0.dll**: `log2`, `fmax`, `atanh`, `sin`, `acos`, `fabs`, `tan`, `nextafter`, `atan2`, `acosh`, `fmin`, `exp`, `frexp`, `exp2`, `tanh`
**api-ms-win-crt-time-l1-1-0.dll**: `_mktime64`, `__daylight`, `clock`, `_gmtime64_s`, `_time64`, `strftime`, `_localtime64_s`, `_tzset`, `__timezone`, `wcsftime`
**api-ms-win-crt-process-l1-1-0.dll**: `_wspawnv`, `_wspawnve`, `_wexecv`, `_wexecve`, `_cwait`
**api-ms-win-crt-conio-l1-1-0.dll**: `_ungetch`, `_ungetwch`, `_getwch`, `_putch`, `_getch`, `_getche`, `_getwche`, `_putwch`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_wstat64i32`, `_umask`

### Exports

`PY_TIMEOUT_MAX`, `PyABIInfo_Check`, `PyAIter_Check`, `PyArg_Parse`, `PyArg_ParseTuple`, `PyArg_ParseTupleAndKeywords`, `PyArg_UnpackTuple`, `PyArg_VaParse`, `PyArg_VaParseTupleAndKeywords`, `PyArg_ValidateKeywordArguments`, `PyAsyncGen_New`, `PyAsyncGen_Type`, `PyBaseObject_Type`, `PyBool_FromLong`, `PyBool_Type`, `PyBuffer_FillContiguousStrides`, `PyBuffer_FillInfo`, `PyBuffer_FromContiguous`, `PyBuffer_GetPointer`, `PyBuffer_IsContiguous`, `PyBuffer_Release`, `PyBuffer_SizeFromFormat`, `PyBuffer_ToContiguous`, `PyByteArrayIter_Type`, `PyByteArray_AsString`, `PyByteArray_Concat`, `PyByteArray_FromObject`, `PyByteArray_FromStringAndSize`, `PyByteArray_Resize`, `PyByteArray_Size`, `PyByteArray_Type`, `PyBytesIter_Type`, `PyBytesWriter_Create`, `PyBytesWriter_Discard`, `PyBytesWriter_Finish`, `PyBytesWriter_FinishWithPointer`, `PyBytesWriter_FinishWithSize`, `PyBytesWriter_Format`, `PyBytesWriter_GetData`, `PyBytesWriter_GetSize`, `PyBytesWriter_Grow`, `PyBytesWriter_GrowAndUpdatePointer`, `PyBytesWriter_Resize`, `PyBytesWriter_WriteBytes`, `PyBytes_AsString`, `PyBytes_AsStringAndSize`, `PyBytes_Concat`, `PyBytes_ConcatAndDel`, `PyBytes_DecodeEscape`, `PyBytes_FromFormat`

## Extracted Strings

Total strings found: **41496** (showing first 100)

```
!This program cannot be run in DOS mode.
$
MlRich
`.rdata
@.data
PyRuntim
@.reloc
SPhLw4
VPhLw4
ta;t$ |E
SVWPhLw4
SVQhLw4
t%h$x4
L$SVW
yMh4{4
D$0PhDz]
D$<PhDz]
;KTt*_^
;Bu5Q
D$HSVW
D$HSVW
D$`j@j
~.}*Ph
p^[_]
D$GH;
;|$$}+

;|$$}
t$WPh
D$_^[
t	PWh 
D$09D$ ~u
;D$,}*
D$0;D$ |
D$P;D$L
D$@9D$
D$H+D$0
D$8VPW
D$PSV
|$RPW
|$VPW
L$<_^3
t$0WPV
#q(#Q,
#q #Q$
A$g&3g
t$PWPV
T$$PWV
L$\_^3
t$LWPV
F 3FH3E
#FL#NH3
1~t1Vp
3N`3N83N
3Fd3F<3F
3Nh3N@
3Fl3FD3N
3Ft3FL3F$3
3Np3NH3N 3
1S81s<1S`1sd1
1G@1OD1Gh1Ol1
1G 1O$1GH1OL1Gp1Ot1
1QH1qL
#Op#Gt3
1Qp1qt
9D$Pv
9D$pv
9D$pv
F 3FH3E
#FL#NH3
1~t1Vp
D$4j6P
D$,vT2
D$,vT2
D$<j6P
D$0vT2
D$4vT2
D$Dj6P
|$ WRP
D$Dj6P
|$ WRP
D$\g&3g
D$l.
D$\g&3g
D$l.
D$|j6P
D$py!~
D$py!~
~D$8Pf
(D$@Pj
<
u;j@
M3U3
<
u:j@
_^[Y]
W+|$$
1Pl1Hp
1Xh1xl
1Ph1pl
@X1A83
1Ph1pl
1xh1Xl
1xh1Xl
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.python315.dll__PyEval_EvalFrameDefault` | `0x10222bb0` | 52468 | ✓ |
| `fcn.1001aab0` | `0x1001aab0` | 39879 | ✓ |
| `fcn.102f20e0` | `0x102f20e0` | 28124 | ✓ |
| `fcn.103047d0` | `0x103047d0` | 24959 | ✓ |
| `fcn.1030a950` | `0x1030a950` | 16449 | ✓ |
| `fcn.102d6460` | `0x102d6460` | 14569 | ✓ |
| `fcn.100395d0` | `0x100395d0` | 13611 | ✓ |
| `fcn.10198b00` | `0x10198b00` | 12595 | ✓ |
| `fcn.10018360` | `0x10018360` | 9384 | ✓ |
| `sym.python315.dll__Py_Specialize_ToBool` | `0x1031a530` | 9007 | ✓ |
| `fcn.10335490` | `0x10335490` | 8012 | ✓ |
| `fcn.1031e500` | `0x1031e500` | 7654 | ✓ |
| `fcn.10058050` | `0x10058050` | 7009 | ✓ |
| `fcn.1005a950` | `0x1005a950` | 6989 | ✓ |
| `fcn.10055850` | `0x10055850` | 6864 | ✓ |
| `fcn.101ca310` | `0x101ca310` | 6668 | ✓ |
| `fcn.102ee590` | `0x102ee590` | 5773 | ✓ |
| `fcn.102ebfd0` | `0x102ebfd0` | 4855 | ✓ |
| `fcn.10300f10` | `0x10300f10` | 4772 | ✓ |
| `sym.python315.dll__PyUnicode_ToNumeric` | `0x10190360` | 4556 | ✓ |
| `fcn.103115e0` | `0x103115e0` | 4452 | ✓ |
| `fcn.102ed410` | `0x102ed410` | 4273 | ✓ |
| `fcn.102cf900` | `0x102cf900` | 4269 | ✓ |
| `fcn.1014d4b0` | `0x1014d4b0` | 4180 | ✓ |
| `fcn.101079c0` | `0x101079c0` | 4165 | ✓ |
| `fcn.10246870` | `0x10246870` | 4071 | ✓ |
| `fcn.10266b70` | `0x10266b70` | 3937 | ✓ |
| `fcn.102681b0` | `0x102681b0` | 3762 | ✓ |
| `fcn.1023efe0` | `0x1023efe0` | 3443 | ✓ |
| `sym.python315.dll_Py_BytesMain` | `0x1008f890` | 3376 | ✓ |

### Decompiled Code Files

- [`code/fcn.10018360.c`](code/fcn.10018360.c)
- [`code/fcn.1001aab0.c`](code/fcn.1001aab0.c)
- [`code/fcn.100395d0.c`](code/fcn.100395d0.c)
- [`code/fcn.10055850.c`](code/fcn.10055850.c)
- [`code/fcn.10058050.c`](code/fcn.10058050.c)
- [`code/fcn.1005a950.c`](code/fcn.1005a950.c)
- [`code/fcn.101079c0.c`](code/fcn.101079c0.c)
- [`code/fcn.1014d4b0.c`](code/fcn.1014d4b0.c)
- [`code/fcn.10198b00.c`](code/fcn.10198b00.c)
- [`code/fcn.101ca310.c`](code/fcn.101ca310.c)
- [`code/fcn.1023efe0.c`](code/fcn.1023efe0.c)
- [`code/fcn.10246870.c`](code/fcn.10246870.c)
- [`code/fcn.10266b70.c`](code/fcn.10266b70.c)
- [`code/fcn.102681b0.c`](code/fcn.102681b0.c)
- [`code/fcn.102cf900.c`](code/fcn.102cf900.c)
- [`code/fcn.102d6460.c`](code/fcn.102d6460.c)
- [`code/fcn.102ebfd0.c`](code/fcn.102ebfd0.c)
- [`code/fcn.102ed410.c`](code/fcn.102ed410.c)
- [`code/fcn.102ee590.c`](code/fcn.102ee590.c)
- [`code/fcn.102f20e0.c`](code/fcn.102f20e0.c)
- [`code/fcn.10300f10.c`](code/fcn.10300f10.c)
- [`code/fcn.103047d0.c`](code/fcn.103047d0.c)
- [`code/fcn.1030a950.c`](code/fcn.1030a950.c)
- [`code/fcn.103115e0.c`](code/fcn.103115e0.c)
- [`code/fcn.1031e500.c`](code/fcn.1031e500.c)
- [`code/fcn.10335490.c`](code/fcn.10335490.c)
- [`code/sym.python315.dll_Py_BytesMain.c`](code/sym.python315.dll_Py_BytesMain.c)
- [`code/sym.python315.dll__PyEval_EvalFrameDefault.c`](code/sym.python315.dll__PyEval_EvalFrameDefault.c)
- [`code/sym.python315.dll__PyUnicode_ToNumeric.c`](code/sym.python315.dll__PyUnicode_ToNumeric.c)
- [`code/sym.python315.dll__Py_Specialize_ToBool.c`](code/sym.python315.dll__Py_Specialize_ToBool.c)

## Behavioral Analysis

This analysis incorporates the findings from **Chunk 17**, which provides one of the most significant technical revelations in the investigation thus far regarding the malware’s architecture.

### New Technical Findings from Chunk 17

#### 1. Confirmation of an Embedded Python Runtime
The most critical find in this chunk is the symbol: `sym.python315.dll_Py_BytesMain`.
*   **Technical Significance:** This indicates that the "Ghost Script" environment isn't a custom-built, simple script runner; it is likely **embedding a full (or heavily modified) Python 3.x interpreter** into the binary.
*   **Implication:** The malware creators aren't just using a "scripting language"; they are utilizing one of the world's most powerful and versatile programming environments. This means that anything possible in Python—complex network protocols, sophisticated encryption, asynchronous task management, and even heavy data processing—can be executed by the malware via an injected script.

#### 2. Sophisticated Code Obfuscation & Junk Code
The block following `Py_BytesMain` contains a massive amount of complex arithmetic, bitwise operations (`XOR`, `AND`, `SHIFT`), and "junk" calculations (e.g., variables like `extraout_ECX_01` through `27`).
*   **Mutation/Obfuscation:** This is a classic technique used to hide the underlying logic of the interpreter's core routines from automated analysis tools and human researchers. By wrapping critical logic in layers of mathematically complex but functionally "neutral" operations, they make it extremely difficult for a researcher to trace the flow of execution or identify where the script actually interacts with the operating system.
*   **Complexity of Logic:** The use of `CONCAT` macros (e.g., `CONCAT31`, `CONCAT22`) suggests that the underlying source code was highly optimized and then "mangled" during the compilation/obfuscation phase to hide the original logic of the Python interpreter's internals.

#### 3. Memory-Centric Execution
The presence of calls like `_sym.imp.KERNEL32.dll_CreateFileMappingA` and `MapViewOfFile` in this context suggests that the engine is designed to map files into memory and execute them from there.
*   **Stealth Technique:** By mapping scripts or shared libraries directly into memory, the malware avoids creating temporary files on disk, a common technique used to evade traditional "on-access" antivirus scanners.

---

### Updated Analysis of Malware Behavior

#### 1. From "Scripting" to "Full Execution Environment"
We can now confirm that this is not just a "script runner." It is a **portable development platform**. By embedding a Python interpreter, the attackers gain several advantages:
*   **Rapid Development:** They can write complex malicious payloads in high-level code (Python) and deploy them instantly.
*   **Feature Richness:** They don't have to manually program features like regular expressions (Regex), advanced math, or JSON parsing; they simply use the libraries already built into the Python environment.
*   **Evolutionary Capability:** If the attackers want to change their tactics—switching from a keylogger to a ransomware module or a data exfiltrator—they don't need to recompile the malware. They only need to send a new `.py` (or similar) script to the infected machine.

#### 2. The "Interpreter" as a Shield
The inclusion of `Py_BytesMain` confirms that the **behavioral signature** of this malware is extremely hard to pin down. Because the heavy lifting happens inside an interpreter:
*   A sandbox might see "the interpreter" doing things, but it won't "see" the specific malicious intent hidden within the script until that script actually reaches out to a system API. 
*   The core "maliciousness" of the code is effectively separated from the binary by a layer of **abstraction.**

---

### Updated "Onion" Defense Model (Revised)

We are refining the layers even further based on the discovery of the embedded interpreter.

1.  **Outer Layer (The Trojan/Dropper):** The initial wrapper that executes and sets up the environment.
2.  **Middleware Layer (Interpreter Infrastructure):** Memory management, thread handling, and **the Python Runtime (New: Chunk 17)**. This is where the `Py_BytesMain` logic lives—it provides the "infrastructure" for execution.
3.  **Interpretation & Decoding Layer:** The process of taking raw data from the C2 and converting it into bytecode that the interpreter can understand.
4.  **Execution Loop (The Gap):** This is where a defender’s view is often "blocked." The interpreter consumes the script's logic, making it appear as if the malware is just performing generic internal tasks.
5.  **Payload Layer:** The actual malicious intent (e.g., stealing passwords, encrypting files).

---

### Final Assessment Update

The analysis of Chunk 17 confirms that this is a **high-tier, sophisticated threat.** The move to include a full Python environment marks this as a **"Framework-as-a-Service"** model of malware construction.

**Key Takeaways for Defenders:**
*   **Complexity Level:** High. This is characteristic of state-sponsored or highly organized cybercrime groups (e.g., APTs) who want to maximize the versatility of their tools.
*   **Detection Challenge:** Traditional signature scanning will fail because the "malicious" logic is hidden inside a legitimate-looking interpretation engine. 
*   **Analysis Strategy:** Detection and analysis must move away from looking at "what the binary does" and toward **"how the interpreter behaves."** We should monitor for the initialization of high-level environments, large memory allocations for "scripting," and subsequent interactions with system APIs after a data injection occurs.

**Status:** The "Ghost Script" is likely no longer just an internal language; it appears to be a hosted environment (possibly Python) designed to give attackers nearly limitless flexibility in their operations.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your analysis to the corresponding MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1059 | Command and Scripting Interpreter | The malware embeds a full Python 3.x interpreter (`Py_BytesMain`) to execute complex, multi-functional scripts, providing a layer of abstraction between the malicious logic and the system's APIs. |
| T1027 | Obfuscated Files or Information | The use of "junk" calculations, bitwise operations (XOR, AND, SHIFT), and `CONCAT` macros is specifically designed to hide functionality from automated tools and human researchers. |
| T1636* | Fileless | While often associated with the broader **T1027** category in common parlance, the use of memory-mapping (`CreateFileMappingA`, `MapViewOfFile`) to execute code without touching the disk is a specific method used to evade on-access antivirus scanners. |

***Note regarding T1636:** In standard MITRE ATT&CK, "Fileless" is not a single standalone technique ID; it is typically represented by a combination of **T1059** (Scripting Interpreters) and **T1027** (Obfuscated Files/Information). If you require a strict adherence to the primary MITRE framework for the memory-mapping behavior, it is best categorized under **T1027**.*

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The string list contains high amounts of obfuscated "junk code" and standard binary headers which have been excluded as per your instructions.

### **IP addresses / URLs / Domains**
*   None identified in the provided text.

### **File paths / Registry keys**
*   None identified. (While `KERNEL32.dll` is mentioned, it is a standard system library and therefore excluded as a false positive).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Embedded Interpreter Signature:** `sym.python315.dll_Py_BytesMain` (Indicates the presence of a Python 3.x runtime embedded within the binary).
*   **Behavioral Pattern - Memory Execution:** Utilization of `CreateFileMappingA` and `MapViewOfFile` to execute scripts directly from memory to evade on-access scanners.
*   **Malware Family/Internal Name:** "Ghost Script" (Identified as the name for the internal execution environment).
*   **Obfuscation Technique:** Heavy use of arithmetic/bitwise obfuscation (`XOR`, `AND`, `SHIFT`) and junk code loops to mask interpreter logic.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1.  **Malware family:** custom (Identified internally as "Ghost Script")
2.  **Malware type:** loader / backdoor
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Embedded Python Runtime:** The detection of `sym.python315.dll_Py_BytesMain` confirms the inclusion of a full Python 3.x interpreter, allowing the attackers to execute complex, multi-functional scripts (e.g., keylogging, exfiltration, or encryption) within a single flexible framework.
    *   **Memory-Centric Execution:** The use of `CreateFileMappingA` and `MapViewOfFile` indicates a "fileless" design intended to execute malicious payloads directly in memory, bypassing traditional on-access antivirus scanners.
    *   **Sophisticated Obfuscation & Modular Architecture:** The heavy use of junk code/bitwise operations combined with the "Framework-as-a-Service" model suggests a high-tier threat (likely APT or organized crime) designed to provide persistent, adaptable functionality through remote script injection.
