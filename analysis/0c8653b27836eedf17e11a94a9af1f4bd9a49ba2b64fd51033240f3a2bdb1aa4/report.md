# Threat Analysis Report

**Generated:** 2026-07-31 15:26 UTC
**Sample:** `0c8653b27836eedf17e11a94a9af1f4bd9a49ba2b64fd51033240f3a2bdb1aa4_0c8653b27836eedf17e11a94a9af1f4bd9a49ba2b64fd51033240f3a2bdb1aa4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c8653b27836eedf17e11a94a9af1f4bd9a49ba2b64fd51033240f3a2bdb1aa4_0c8653b27836eedf17e11a94a9af1f4bd9a49ba2b64fd51033240f3a2bdb1aa4.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 335,872 bytes |
| MD5 | `095c32757a1db06106df2c9d647cfee1` |
| SHA1 | `096773528e455699892bbbb060c20d390d229399` |
| SHA256 | `0c8653b27836eedf17e11a94a9af1f4bd9a49ba2b64fd51033240f3a2bdb1aa4` |
| Overall entropy | 6.66 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1777142583 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 55,808 | 6.381 | No |
| `.rdata` | 38,912 | 4.702 | No |
| `.data` | 233,472 | 6.344 | No |
| `.pdata` | 4,096 | 4.547 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.876 | No |

### Imports

**KERNEL32.dll**: `AddVectoredExceptionHandler`, `RemoveVectoredExceptionHandler`, `GetModuleHandleA`, `GetProcAddress`, `LoadLibraryW`, `QueryPerformanceCounter`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetSystemTimeAsFileTime`, `InitializeSListHead`, `SetUnhandledExceptionFilter`, `GetStartupInfoW`, `GetModuleHandleW`, `WriteConsoleW`, `RtlUnwindEx`

## Extracted Strings

Total strings found: **4920** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Rich0a
`.rdata
@.data
.pdata
@.fptable
.reloc
9D$(s"
@pH9D$Xt
@pH9D$XuwH
D$PHc@<H
D$PHc@<H
Hc$Hk
u0HcH<
WATAUAVAWH
A_A^A]A\_
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
G0HcX
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
@SVWATAUAVAWH
A_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
|$$Hc^
@A_A^A]A\_^[
UVWATAUAVAWH
G0Lch
G0HcX
D$hIcu
 A_A^A]A\_^]
99~YHc^
t98t H
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
u3HcH<H
WAVAWH
 A_A^_
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
D$0@8{
u$D8r(tH
D81u`L9r
uPD8r(tH
vWD8s(tH
u$D8r(tH
fD91u_L9r
uPD8r(tH
vVD8s(tH
UVWATAUAVAWH
PA_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
@USVWATAUAVH
,/<-w
H
D8t$ht
H
D8t$ht
H
A^A]A\_^[]
f9)u4H9j
u%@8j(t
v@8k(t
8D$@tH
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
fD9t$b
K@H;v
KHH;l
KhH;z
KpH;p
KxH;f
@UATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400061c8` | `0x1400061c8` | 16523 | ✓ |
| `fcn.1400061b4` | `0x1400061b4` | 16482 | ✓ |
| `fcn.140007b54` | `0x140007b54` | 1985 | ✓ |
| `fcn.14000dde0` | `0x14000dde0` | 1677 | ✓ |
| `fcn.140003bcc` | `0x140003bcc` | 1213 | ✓ |
| `fcn.14000c24c` | `0x14000c24c` | 1171 | ✓ |
| `fcn.140001920` | `0x140001920` | 1020 | ✓ |
| `fcn.14000b710` | `0x14000b710` | 922 | ✓ |
| `fcn.14000da20` | `0x14000da20` | 920 | ✓ |
| `fcn.14000b1a0` | `0x14000b1a0` | 920 | ✓ |
| `fcn.140007758` | `0x140007758` | 862 | ✓ |
| `fcn.14000bb64` | `0x14000bb64` | 817 | ✓ |
| `fcn.14000cb98` | `0x14000cb98` | 815 | ✓ |
| `fcn.140001d30` | `0x140001d30` | 755 | ✓ |
| `fcn.140008620` | `0x140008620` | 712 | ✓ |
| `fcn.140002858` | `0x140002858` | 667 | ✓ |
| `section..text` | `0x140001000` | 664 | ✓ |
| `fcn.1400020d0` | `0x1400020d0` | 660 | ✓ |
| `fcn.14000827c` | `0x14000827c` | 623 | ✓ |
| `fcn.14000a3f4` | `0x14000a3f4` | 604 | ✓ |
| `fcn.14000570c` | `0x14000570c` | 589 | ✓ |
| `fcn.14000408c` | `0x14000408c` | 584 | ✓ |
| `fcn.14000462c` | `0x14000462c` | 557 | ✓ |
| `fcn.1400097d4` | `0x1400097d4` | 555 | ✓ |
| `fcn.140002b00` | `0x140002b00` | 517 | ✓ |
| `fcn.140008084` | `0x140008084` | 501 | ✓ |
| `fcn.140003840` | `0x140003840` | 499 | ✓ |
| `fcn.140007d9c` | `0x140007d9c` | 462 | ✓ |
| `fcn.140005124` | `0x140005124` | 445 | ✓ |
| `fcn.14000adb4` | `0x14000adb4` | 445 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001920.c`](code/fcn.140001920.c)
- [`code/fcn.140001d30.c`](code/fcn.140001d30.c)
- [`code/fcn.1400020d0.c`](code/fcn.1400020d0.c)
- [`code/fcn.140002858.c`](code/fcn.140002858.c)
- [`code/fcn.140002b00.c`](code/fcn.140002b00.c)
- [`code/fcn.140003840.c`](code/fcn.140003840.c)
- [`code/fcn.140003bcc.c`](code/fcn.140003bcc.c)
- [`code/fcn.14000408c.c`](code/fcn.14000408c.c)
- [`code/fcn.14000462c.c`](code/fcn.14000462c.c)
- [`code/fcn.140005124.c`](code/fcn.140005124.c)
- [`code/fcn.14000570c.c`](code/fcn.14000570c.c)
- [`code/fcn.1400061b4.c`](code/fcn.1400061b4.c)
- [`code/fcn.1400061c8.c`](code/fcn.1400061c8.c)
- [`code/fcn.140007758.c`](code/fcn.140007758.c)
- [`code/fcn.140007b54.c`](code/fcn.140007b54.c)
- [`code/fcn.140007d9c.c`](code/fcn.140007d9c.c)
- [`code/fcn.140008084.c`](code/fcn.140008084.c)
- [`code/fcn.14000827c.c`](code/fcn.14000827c.c)
- [`code/fcn.140008620.c`](code/fcn.140008620.c)
- [`code/fcn.1400097d4.c`](code/fcn.1400097d4.c)
- [`code/fcn.14000a3f4.c`](code/fcn.14000a3f4.c)
- [`code/fcn.14000adb4.c`](code/fcn.14000adb4.c)
- [`code/fcn.14000b1a0.c`](code/fcn.14000b1a0.c)
- [`code/fcn.14000b710.c`](code/fcn.14000b710.c)
- [`code/fcn.14000bb64.c`](code/fcn.14000bb64.c)
- [`code/fcn.14000c24c.c`](code/fcn.14000c24c.c)
- [`code/fcn.14000cb98.c`](code/fcn.14000cb98.c)
- [`code/fcn.14000da20.c`](code/fcn.14000da20.c)
- [`code/fcn.14000dde0.c`](code/fcn.14000dde0.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This updated analysis incorporates the findings from your second disassembly chunk. The additional code confirms and expands upon the initial assessment that this binary is a sophisticated piece of malware, specifically a **highly-obfuscated loader or "packer" shell.**

The new data reveals more advanced techniques related to anti-analysis, manual function resolution (API hashing), and complex internal state management.

---

### Updated Analysis: Technical Findings

#### 1. Advanced Obfuscation & Control Flow Flattening
Several functions (like `fcn.14000a3f4`) exhibit a "dispatch" pattern. Instead of clear, linear logic, the code uses large switch-like blocks or tables to determine where to jump next based on input parameters and internal state. 
*   **Significance:** This is a technique used to frustrate automated analysis tools (like IDA's decompiler) by breaking the logical flow into many small chunks, making it harder for an analyst to follow the "story" of the code.

#### 2. API Hashing & Indirect Branching
The presence of `_sym.imp.KERNEL32.dll_EncodePointer` and comparisons against hardcoded hex constants (e.g., `-0x1fbcb0b3`, `-0x7fffffda`) suggests the use of **API Hashing**. 
*   **Mechanism:** Instead of importing a function like `GetProcAddress` by name, the malware calculates a hash of the string "GetProcAddress" and compares it to these constants.
*   **Significance:** This hides the program's true intentions from static analysis, as the actual names of the Windows functions being used aren't visible in the Import Address Table (IAT).

#### 3. Advanced Anti-Debugging (SWI/Interrupt Logic)
The use of `swi(3)` (a software interrupt) is a classic anti-analysis technique. 
*   **Mechanism:** When an `swi` instruction is executed, it triggers an exception. If a debugger is attached, the debugger will intercept this "trap." The malware can then check how the environment responded to that specific trap to determine if a human or a tool is watching.
*   **Significance:** This confirms the author's intent to evade security researchers and automated sandbox environments.

#### 4. Custom Memory & State Management
Functions like `fcn.1400097d4` and `fcn.1400084ec` show heavy use of `LOCK()` and `UNLOCK()` instructions alongside manual offset calculations (e.g., `+ 0x10`, `+ 0xE0`).
*   **Mechanism:** The code is manually managing its own internal "registry" or state machine in memory, likely to track threads or progress through the unpacking process.
*   **Significance:** This indicates a complex multi-staged execution environment where the loader manages several different tasks (decryption, injection, and anti-analysis) simultaneously.

#### 5. Data Processing & Encoding Handling
The function `fcn.14000adb4` contains logic for handling Unicode characters and bit-shifting (`uVar3 = uVar1 & 0x3f | uVar3 << 6`).
*   **Significance:** This suggests the malware may be processing system information (like computer names or usernames) or preparing strings that will eventually be passed to legitimate Windows APIs, possibly for exfiltration.

---

### Updated Summary Table of Behaviors

| Feature | Observation from Analysis | Significance |
| :--- | :--- | :--- |
| **Process Injection** | `NtMapViewOfSection` & `NtUnmapViewOfSection` | Indicates "Manual Mapping" to run code without a file on disk. |
| **API Hashing** | Comparison against hardcoded hex constants (e.g., `-0x1fbcb0b3`) | Obscures the intended Win32 API calls from static analysis tools. |
| **Anti-Analysis** | `swi(3)` instructions and detailed CPU checks (`cpuid`). | Detects debuggers, sandboxes, and virtual machines before executing malicious logic. |
| **Control Flow Hiding** | Extensive use of dispatch tables & indirect branching. | Makes the code difficult for humans to read/trace during manual reverse engineering. |
| **Memory Manipulation** | Manual offset management and `LOCK` mechanisms. | Suggests a sophisticated, multi-threaded loader managing complex internal states. |
| **Sideloading / Proxying**| Attempted loading of `fakedll.dll`. | A high-confidence indicator of a "Stager" used to drop the final payload. |

### Final Conclusion (Updated)
The binary is highly characteristic of a **modern, sophisticated malware loader.** It is designed specifically to be "invisible" to both static analysis (via API hashing and control flow obfuscation) and dynamic analysis (via `swi(3)` traps and hardware capability checks). 

Its primary purpose appears to be the creation of a "safe" execution environment. By manually mapping its components into memory and stripping away standard Win32 signatures, it aims to bypass EDR (Endpoint Detection and Response) systems before delivering a second-stage payload—likely hidden within or delivered via `fakedll.dll`.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of control flow flattening and API hashing is designed to hide the program's logic and conceal intended system calls from static analysis. |
| **T1497** | Virtualization/Sandbox Detection | The inclusion of `swi(3)` interrupts and `cpuid` checks indicates an intentional attempt to detect if the malware is running in a researcher-controlled environment. |
| **T1055** | Process Injection | The use of `NtMapViewOfSection` and `NtUnmapViewOfSection` for "Manual Mapping" allows the loader to execute code while evading standard Windows API monitoring. |
| **T1574.002** | DLL Side-Loading | The attempt to load a file named `fakedll.dll` is a high-confidence indicator of using a stager to proxy malicious code into a legitimate process. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `fakedll.dll` (Identified as a high-confidence indicator of a "Stager" used to drop the final payload).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified (Note: The hex constants `-0x1fbcb0b3` and `-0x7fffffda` appear in the text, but these are internal API hashing constants rather than file hashes like MD5/SHA256).

**Other artifacts**
*   **API Hashing Constants:** `-0x1fbcb0b3`, `-0x7fffffda` (Used to obfuscate calls to Windows APIs).
*   **Manual Mapping Indicators:** `NtMapViewOfSection`, `NtUnmapViewOfSection` (Used for executing code without a file on disk).
*   **Anti-Analysis Techniques:** `swi(3)` instruction, `cpuid` checks.

---

## Malware Family Classification

Based on the provided analysis report, here is the classification for the sample:

1. **Malware family**: custom (or Unknown)
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    * **Advanced Evasion Techniques:** The sample utilizes high-level obfuscation such as Control Flow Flattening and API Hashing to hide its logic from static analysis and bypass EDR systems.
    * **Sophisticated Execution Environment:** The use of "Manual Mapping" (via `NtMapViewOfSection`) and a stager (`fakedll.dll`) indicates the primary purpose is to inject and execute secondary payloads in memory while avoiding on-disk detection.
    * **Anti-Analysis Logic:** The integration of `swi(3)` traps, `cpuid` checks, and complex state management confirms it is designed specifically to detect and evade security researchers and automated sandboxes.
