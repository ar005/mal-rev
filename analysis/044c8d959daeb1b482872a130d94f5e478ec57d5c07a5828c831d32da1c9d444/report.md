# Threat Analysis Report

**Generated:** 2026-07-09 22:35 UTC
**Sample:** `044c8d959daeb1b482872a130d94f5e478ec57d5c07a5828c831d32da1c9d444_044c8d959daeb1b482872a130d94f5e478ec57d5c07a5828c831d32da1c9d444.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `044c8d959daeb1b482872a130d94f5e478ec57d5c07a5828c831d32da1c9d444_044c8d959daeb1b482872a130d94f5e478ec57d5c07a5828c831d32da1c9d444.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 124,928 bytes |
| MD5 | `0bd695d2afd86ba2c11e013fc7b936c3` |
| SHA1 | `6f1bcbd567f6cedac259cba1486542929d0a7b7f` |
| SHA256 | `044c8d959daeb1b482872a130d94f5e478ec57d5c07a5828c831d32da1c9d444` |
| Overall entropy | 6.002 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1770441205 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 68,608 | 6.458 | No |
| `.rdata` | 44,032 | 4.725 | No |
| `.data` | 3,072 | 2.344 | No |
| `.pdata` | 5,120 | 4.858 | No |
| `.reloc` | 2,048 | 4.907 | No |
| `.rsrc` | 1,024 | 1.919 | No |

### Imports

**USER32.dll**: `MessageBoxA`
**KERNEL32.dll**: `WriteConsoleW`, `ExpandEnvironmentStringsA`, `CreateFileA`, `GetFileSize`, `ReadFile`, `CloseHandle`, `RaiseException`, `InitOnceExecuteOnce`, `GetTickCount64`, `GetModuleHandleA`, `GetProcAddress`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `UnhandledExceptionFilter`

### Exports

`AudioChecker`, `EnumTimeLocation`, `TimerChecker`, `ord_101`

## Extracted Strings

Total strings found: **431** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.reloc
B.rsrc
|$ AVH
uxHc0
T$u[H
D8L$0u`
E9
tIIc
L$0tA
VWATAVAWH
 A_A^A\_^
WATAUAVAWH
A_A^A]A\_
H;XXs
H;xXu5
WATAUAVAWH
A_A^A]A\_
AUAVAWH
9;|
HcC
u4I9}(
;I9}(tiH
0A_A^A]
AUAVAWH
9{u	9{
u4I9}(
;I9}(tiH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
K0HcQ
C0Hc	H
A_A^A]A\_^[]
@USVWATAUAVAWH
K0HcQD
d$dD;d$l
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
@USVWATAUAVAWH
A_A^A]A\_^[]
WAVAWH
 A_A^_
WAVAWH
D9ucL
9t$Pu	
IH9BtEHcRI
@SVWATAUAVAWH
L!|$(L!
D$0HcH
pA_A^A]A\_^[
SVWATAUAWH
L!d$(L!d$@D
D$HL9gXt
A_A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
0A_A^A]A\_^[
SVWATAUAVAWH
A_A^A]A\_^[
t$ WATAUAVAWH
E0Lc`I
E0HcHD
 A_A^A]A\_
UVWATAUAVAWH
 A_A^A]A\_^]
D$ I;R
D$ I9P
WATAUAVAWH
 A_A^A]A\_
D$0uH
D$0@8{
p0R^G'
t98t H
u3HcH<H
WATAUAVAWH
< t=<	t9
 A_A^A]A\_
UVWAVAWH
H9:tH
0A_A^_^]
WAVAWH
L3
H3B
 A_A^_
u$D8r(tH
D81uUL9r
uED8r(tH
vAD8s(tH
u$D8r(tH
fD91uTL9r
uED8r(tH
v@D8s(tH
UVWATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180002384` | `0x180002384` | 22689 | ✓ |
| `fcn.180008868` | `0x180008868` | 12682 | ✓ |
| `fcn.180008830` | `0x180008830` | 12668 | ✓ |
| `fcn.180002284` | `0x180002284` | 5998 | ✓ |
| `fcn.180002414` | `0x180002414` | 5720 | ✓ |
| `fcn.18000a098` | `0x18000a098` | 1977 | ✓ |
| `fcn.180010940` | `0x180010940` | 1661 | ✓ |
| `fcn.180001ac0` | `0x180001ac0` | 1394 | ✓ |
| `fcn.180004b64` | `0x180004b64` | 1281 | ✓ |
| `fcn.180005d24` | `0x180005d24` | 1233 | ✓ |
| `fcn.180004694` | `0x180004694` | 1230 | ✓ |
| `fcn.180001a1c` | `0x180001a1c` | 1169 | ✓ |
| `fcn.18000e0a8` | `0x18000e0a8` | 1141 | ✓ |
| `fcn.18000cd20` | `0x18000cd20` | 1038 | ✓ |
| `fcn.18000d2c0` | `0x18000d2c0` | 937 | ✓ |
| `fcn.180010fe0` | `0x180010fe0` | 920 | ✓ |
| `fcn.180009cac` | `0x180009cac` | 845 | ✓ |
| `fcn.18000d724` | `0x18000d724` | 817 | ✓ |
| `fcn.1800067a4` | `0x1800067a4` | 776 | ✓ |
| `fcn.18000e9d0` | `0x18000e9d0` | 774 | ✓ |
| `fcn.1800052d8` | `0x1800052d8` | 756 | ✓ |
| `fcn.18000ab54` | `0x18000ab54` | 701 | ✓ |
| `fcn.180005a90` | `0x180005a90` | 660 | ✓ |
| `fcn.180008520` | `0x180008520` | 653 | ✓ |
| `fcn.18000ba8c` | `0x18000ba8c` | 633 | ✓ |
| `fcn.18000a7b0` | `0x18000a7b0` | 623 | ✓ |
| `fcn.180005068` | `0x180005068` | 621 | ✓ |
| `fcn.180010238` | `0x180010238` | 614 | ✓ |
| `fcn.18000c4c0` | `0x18000c4c0` | 555 | ✓ |
| `fcn.180003788` | `0x180003788` | 535 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001a1c.c`](code/fcn.180001a1c.c)
- [`code/fcn.180001ac0.c`](code/fcn.180001ac0.c)
- [`code/fcn.180002284.c`](code/fcn.180002284.c)
- [`code/fcn.180002384.c`](code/fcn.180002384.c)
- [`code/fcn.180002414.c`](code/fcn.180002414.c)
- [`code/fcn.180003788.c`](code/fcn.180003788.c)
- [`code/fcn.180004694.c`](code/fcn.180004694.c)
- [`code/fcn.180004b64.c`](code/fcn.180004b64.c)
- [`code/fcn.180005068.c`](code/fcn.180005068.c)
- [`code/fcn.1800052d8.c`](code/fcn.1800052d8.c)
- [`code/fcn.180005a90.c`](code/fcn.180005a90.c)
- [`code/fcn.180005d24.c`](code/fcn.180005d24.c)
- [`code/fcn.1800067a4.c`](code/fcn.1800067a4.c)
- [`code/fcn.180008520.c`](code/fcn.180008520.c)
- [`code/fcn.180008830.c`](code/fcn.180008830.c)
- [`code/fcn.180008868.c`](code/fcn.180008868.c)
- [`code/fcn.180009cac.c`](code/fcn.180009cac.c)
- [`code/fcn.18000a098.c`](code/fcn.18000a098.c)
- [`code/fcn.18000a7b0.c`](code/fcn.18000a7b0.c)
- [`code/fcn.18000ab54.c`](code/fcn.18000ab54.c)
- [`code/fcn.18000ba8c.c`](code/fcn.18000ba8c.c)
- [`code/fcn.18000c4c0.c`](code/fcn.18000c4c0.c)
- [`code/fcn.18000cd20.c`](code/fcn.18000cd20.c)
- [`code/fcn.18000d2c0.c`](code/fcn.18000d2c0.c)
- [`code/fcn.18000d724.c`](code/fcn.18000d724.c)
- [`code/fcn.18000e0a8.c`](code/fcn.18000e0a8.c)
- [`code/fcn.18000e9d0.c`](code/fcn.18000e9d0.c)
- [`code/fcn.180010238.c`](code/fcn.180010238.c)
- [`code/fcn.180010940.c`](code/fcn.180010940.c)
- [`code/fcn.180010fe0.c`](code/fcn.180010fe0.c)

## Behavioral Analysis

This updated analysis incorporates the findings from both segments of the disassembly provided.

### Updated Technical Analysis

The additional disassembly confirms and deepens the initial assessment: this is not a standard piece of malware; it is a highly engineered **virtualized execution environment (VM)**. The binary does not execute its primary malicious logic in native x86/x64 instructions but instead hosts a custom interpreter that "runs" a proprietary bytecode.

#### 1. Advanced VM Architecture & Dispatcher Logic
The functions `fcn.18000e9d0`, `fcn.1800052d8`, and `fcn.18000ba8c` exhibit classic traits of a **Virtual Machine Dispatcher**. 
*   **Handler Selection:** The code frequently uses complex nested loops to determine which "handler" to execute based on an internal instruction pointer or opcode. In `fcn.18000e9d0`, the logic branching into `fcn.18000e520`, `fcn.18000e740`, and `fcn.18000e624` suggests different "opcodes" for different operations (e.g., memory manipulation, API wrapping, or state changes).
*   **Instruction Decoding:** The logic in `fcn.18000ba8c` involving large jumps and table lookups (`puVar13 = *puVar13; ... for (; uVar2 != uVar8; uVar2 = uVar2 + 0x10)`) is indicative of the VM "walking" through an instruction table to find the correct routine to execute.
*   **Register/Stack Emulation:** The frequent use of `LOCK()` and `UNLOCK()` (seen in `fcn.18000c4c0`) suggests that the malware’s internal VM handles its own multi-threaded state or reference counting for objects, likely to manage complex tasks without being easily traced by standard thread-tracking tools.

#### 2. Enhanced Data Handling & File I/O
While Chunk 1 established the intent to write files (specifically targeting `.asar` files), Chunk 2 reveals the complexity of how that data is processed:
*   **WriteFile Wrapper:** In `fcn.18000e9d0`, there is a direct call to `_sym.imp.KERNEL32.dll_WriteFile`. The code surrounding it includes checks for `GetConsoleMode` and complex buffer validation, indicating that the malware has built-in "subroutines" to handle file I/O reliably even in restricted environments.
*   **Buffer Manipulation:** Functions like `fcn.18000ab54` involve intensive bitwise operations and loop-based data transformations (e.g., `*puVar1 = *puVar1 | *puVar17`). This is likely used to decrypt or "unpack" the payload into memory before it is written to disk or executed.

#### 3. Sophisticated Evasion & Anti-Analysis
The second chunk reveals several techniques designed to thwart automated analysis:
*   **Exception Manipulation:** `fcn.180010238` interacts with `RaiseException`. The way it constructs specific codes (like `0xc000000d`) and performs bitwise operations on arguments before the call suggests it may be using "exception-based" control flow—a technique where the malware intentionally triggers an exception that it then handles itself to jump to a new location, confusing standard debuggers.
*   **Junk Code & Complexity Bloat:** Functions like `fcn.180003788` and `fcn.1800052d8` contain extremely dense logic with many redundant calculations. This is intended to exhaust the time of a human analyst performing manual deconstruction.
*   **Manual API Resolution:** The reliance on `_sym.imp.` suggests the malware manually resolves its imports at runtime, reducing its footprint in the Import Address Table (IAT) and making it harder for static analysis tools to flag known malicious APIs.

---

### Updated Summary for Incident Response

**Revised Classification:** 
**Sophisticated Malware Dropper / Modular Trojan with VM-based Obfuscation.**

**Key Indicators of Compromise (IOCs) & Behavior:**
*   **Targeting:** High-confidence intent to target **Electron-based applications** (e.g., Discord, Slack, VS Code, etc.) by modifying or injecting into `\resources\upd.asar` files.
*   **Evasion Technique:** The malware utilizes a **Virtual Machine (VM) protection layer**. This means that traditional signature-based detection of "malicious logic" will likely fail because the logic is hidden within the custom bytecode interpreted by the binary.
*   **Persistence/Action on Infection:** 
    1.  The malware identifies target applications via file system crawling (`FindFirstFileExW`).
    2.  It decrypts its payload using a multi-stage, loop-heavy routine (likely in `fcn.18000ab54`).
    3.  It writes the decrypted payload to disk (using `WriteFile`) and potentially modifies `.asar` files or other related binaries.
*   **Advanced Techniques:** 
    *   **Exception-based Control Flow:** Uses custom exceptions to mask its execution path from debuggers.
    *   **Thread Synchronization:** Uses internal locking mechanisms to manage state, suggesting a sophisticated multi-tasking architecture.

**Detection Recommendations:**
1.  **File Integrity Monitoring (FIM):** Alert on any unauthorized modification of files in `%LOCALAPPDATA%` or `%APPDATA%` ending in `.asar` or located in `\resources\` folders.
2.  **Behavioral Heuristics:** Monitor for processes that perform an unusual amount of loop-heavy, bitwise operations immediately followed by calls to `WriteFile` on application resource files.
3.  **Network Monitoring:** While this chunk does not show a clear C2 IP, the "loader" nature suggests it may eventually attempt to reach out to a remote server to fetch the specific modules required to modify the targeted apps.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&C framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1029** | Obfuscated Files or Information | The malware utilizes a custom virtual machine (VM) architecture, junk code, and exception-based control flow to hide its true logic from static and dynamic analysis. |
| **T1036** | Dynamic Resolution | The reliance on `_sym.imp` indicates the binary resolves API addresses at runtime to minimize its footprint in the Import Address Table (IAT). |
| **T1083** | File and Directory Discovery | The use of `FindFirstFileExW` is used to scan the filesystem for specific targets, such as `.asar` files within application folders. |
| **T1027** | Encrypter/Packer | The intensive bitwise operations and buffer transformations are used to decrypt or "unpack" the payload into memory before it is written to disk. |

---

## Indicators of Compromise

Based on the analysis provided, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.* (The report notes a "loader" nature but does not provide specific C2 infrastructure in this segment.)

**File paths / Registry keys**
*   `%LOCALAPPDATA%\resources\upd.asar` (Targeted file for injection/modification in Electron-based applications)

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.* (The strings provided appear to be fragmented machine code or compiler artifacts rather than cryptographic hashes.)

**Other artifacts**
*   **Targeted Software:** Discord, Slack, VS Code (identified via the targeting of `.asar` files).
*   **Malware Type:** Sophisticated Malware Dropper / Modular Trojan.
*   **Evasion Techniques:** 
    *   Virtual Machine (VM) protection layer (custom bytecode interpreter).
    *   Exception-based control flow (using `RaiseException` with specific codes like `0xc000000d`).
    *   Manual API Resolution (hiding imports from the IAT).
    *   High-complexity "Junk Code" and loop-heavy bitwise operations for de-obfuscation.
*   **Behaviors:** Use of `FindFirstFileExW` to scan for targets; usage of `WriteFile` on application resource files.

---

## Malware Family Classification

1. **Malware family**: Unknown (Custom)
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **VM-Based Execution Layer:** The analysis confirms the use of a highly engineered virtual machine (VM) dispatcher to execute proprietary bytecode, effectively hiding the primary malicious logic from signature-based and static analysis tools.
*   **Targeted Targeting of Electron Applications:** The malware specifically targets `.asar` files located in resources folders of applications like Discord, Slack, and VS Code—a common behavior for loaders designed to inject modules or steal tokens/session data.
*   **Advanced Evasion Techniques:** The sample utilizes sophisticated anti-analysis measures including manual API resolution (to hide the IAT), exception-based control flow (via `RaiseException`), and junk code insertion to hinder reverse engineering.
