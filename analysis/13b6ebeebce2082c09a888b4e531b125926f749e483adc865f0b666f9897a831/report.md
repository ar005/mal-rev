# Threat Analysis Report

**Generated:** 2026-09-02 22:05 UTC
**Sample:** `13b6ebeebce2082c09a888b4e531b125926f749e483adc865f0b666f9897a831_13b6ebeebce2082c09a888b4e531b125926f749e483adc865f0b666f9897a831.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13b6ebeebce2082c09a888b4e531b125926f749e483adc865f0b666f9897a831_13b6ebeebce2082c09a888b4e531b125926f749e483adc865f0b666f9897a831.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 8 sections |
| Size | 8,531,968 bytes |
| MD5 | `8205cfed7bd057990d49bdbcd11cbc26` |
| SHA1 | `52b7a79a4848f5be6ebcd06d359d28b58d754316` |
| SHA256 | `13b6ebeebce2082c09a888b4e531b125926f749e483adc865f0b666f9897a831` |
| Overall entropy | 6.65 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766613929 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 447,488 | 6.657 | No |
| `.managed` | 2,452,480 | 6.447 | No |
| `hydrated` | 0 | 0.0 | No |
| `.rdata` | 5,393,408 | 6.021 | No |
| `.data` | 18,432 | 4.617 | No |
| `.pdata` | 214,016 | 6.361 | No |
| `.rsrc` | 2,048 | 3.558 | No |
| `.reloc` | 3,072 | 5.434 | No |

### Imports

**ADVAPI32.dll**: `RegOpenKeyExW`, `RegSetValueExW`, `RegCloseKey`, `RegEnumKeyExW`, `RegQueryValueExW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `SetLastError`, `CreateDirectoryW`, `GetLastError`, `CopyFileW`, `CreateFileW`, `WriteFile`, `CloseHandle`, `GetModuleHandleW`, `OpenProcess`, `ReadProcessMemory`, `VirtualProtectEx`, `WriteProcessMemory`, `LocalFree`
**ole32.dll**: `CoGetApartmentType`, `CoTaskMemAlloc`, `CoUninitialize`, `CoInitializeEx`, `CoCreateGuid`, `CoTaskMemFree`, `CoWaitForMultipleHandles`
**USER32.dll**: `LoadStringW`
**api-ms-win-crt-math-l1-1-0.dll**: `modf`, `tanh`, `pow`, `log10`, `floor`, `ceil`
**api-ms-win-crt-heap-l1-1-0.dll**: `calloc`, `_callnewh`, `free`, `malloc`
**api-ms-win-crt-string-l1-1-0.dll**: `wcsncmp`, `strcmp`, `_stricmp`, `strcpy_s`, `strlen`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_execute_onexit_table`, `abort`, `_configure_narrow_argv`, `_seh_filter_dll`, `terminate`, `_cexit`, `_crt_atexit`, `_initialize_narrow_environment`, `_initterm_e`, `_register_onexit_function`, `_initialize_onexit_table`, `_initterm`

### Exports

`01cJmxzpCUMd3t3xJs0QSMNtAYqfpFc3`, `0O4kqQlNyXHTB8b`, `0UkS7P1ugIFyfeuovWAV7TgbcRm0m8h`, `19AAdNjwh2uxtdmULblLCiK9yXuu8j`, `1D3NKdRG00EXrfrxRegvj`, `1oxHU8nINsYoH00356DA0zCJIPi6`, `1uE7hjJQV5AgbicpXDKZMY`, `2PDLMw4KO4FLKUbPhJnBdXwkbguf7Oy`, `2SSBEVs1bQKV`, `2pL83doRpAr5sd07eZLw3qNMKayeKur`, `2tVhYej734pnZN8T03HQN5CL7W`, `2zlG9hx7gjAD1sFSzZuurrZjZdK`, `3SCm1o8E6h7`, `3eKk1f9rpjHXB`, `3mJ3g8fXK`, `40r0mEEKAGvrQgVNBZp`, `4MQncLAC0xAjAXir`, `5BTmddyc2RrC`, `5MQw1Pe`, `5OFzuvlKwY3Ut9gFlBLfgdxPw`, `6TUwMKgs9BdjamJlqQPZn8QE`, `6luAV4S65MDK7u0tL`, `6ua3kVcLCsLWkyeBTXbkyyReN3yfh`, `72FUQdZEHxUsZCqeiIx`, `7GI46VWzz5Po`, `7SPM3ZM9z1yWKmpfesx0xvEmcRwNz`, `7qZDrbxaZrcOYQYe7T7tdNh6i`, `81tPyBnu3dKp2KLpKz67E7x9em1`, `85DsZcL`, `8QHVy9USVRiVaqVRD`, `8keMryDbcoLqtlaqWf`, `8oYeP0tMmp971fs`, `9ZC6Q4t89s9dsPpKoxULGFxHvW`, `9eSSrkb`, `AXiVeRpW0BJjLThzuL5GJzZKQCng`, `AhUBQHnhq`, `BfOib0BJ5Q7J0KazXq`, `CCehVG4EMj4Y2DsAfpvaaWJw4lRX`, `CCnAYsjMoiVV8Kz6jATiHu1WySljTFb`, `CPtaSeSScTnVKTr2ZbDp`, `CRMAydcL6eCPPRZTrUzPIvdvrTvgkt5V`, `CW2Ucmvvi66BRYFLV5blKl0xMwx`, `D8081xhI93Lpc5El`, `DZxvQ49U`, `E2fNhYRj1gViT9bFaF1c1KC7uB091`, `E3NvsvlyTZqqYhnar9yqklVGK0D9`, `EKqJ7ivyffLiuiM1R9JRezhLLiPc0Ulq`, `ENRdVoLiGYgMIb`, `EizFZBEaA75X`, `Em8gYVoe4DM6kubYd0`

## Extracted Strings

Total strings found: **22820** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.managed
`hydrated
.rdata
@.data
.pdata
@.rsrc
@.reloc
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
AQAWAVAUATWVSh
L$XAQL
0]AZAZ[^_A\A]A^A_AZ
0]AZAZ[^_A\A]A^A_AZ
fffffff
uoH;W
rfH;V
riH;=Z
r6H;7d
fffffff
|$ AVH
APAWAVAUATSAPVWUPRH
APAWAVAUATSAPVWUPRH
APAWAVAUATSAPVWUPRH
AWAVAUATSVWUH
AWAVAUATSVWUH
o|$0fD
oD$@fD
oL$PfD
oT$`fD
o\$pfD
]_^[A\A]A^A_
AWAVAUATSVWUH
o|$0fD
oD$@fD
oL$PfD
oT$`fD
o\$pfD
]_^[A\A]A^A_
SATAUAWH
hA_A]A\[
|$ AVH
WATAUAVAWH
 A_A^A]A\_
PAWAVAUATWVSQRUH
8]XX[^_A\A]A^A_XX
8]XX[^_A\A]A^A_XXH
QAWAVAUATWVSh
0]AZAZ[^_A\A]A^A_AZ
L+A L;
A(H+Q H;
|$ AVH
UVWATAUAVAWH
A_A^A]A\_^]
|$ AVH
(H9W
@WAUAVAWH
(A_A^A]_
(A_A^A]_
tTH;xn
|$ ATAVAWH
0A_A^A\
VWATAUAVAWH
A_A^A]A\_^
|$ AVH
c(I;C0u
c(I;C0u
c8I;C@u
cHI;CPu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
c(I;C0u
c8I;C@u
cHI;CPu
cXI;C`u
chI;Cpu
SUVWATAUAVH
{H9|$ t
@A^A]A\_^][
SWAUAVH
8A^A]_[
|$ AVL
|$ AVL
|$ AVH
VAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800b7640` | `0x1800b7640` | 2082723 | ✓ |
| `fcn.18009bef0` | `0x18009bef0` | 1898767 | ✓ |
| `fcn.18009bfb0` | `0x18009bfb0` | 1896223 | ✓ |
| `fcn.18009c070` | `0x18009c070` | 1891311 | ✓ |
| `fcn.18009c010` | `0x18009c010` | 1889247 | ✓ |
| `fcn.18009be90` | `0x18009be90` | 1887103 | ✓ |
| `fcn.1800a3da0` | `0x1800a3da0` | 1856731 | ✓ |
| `fcn.180281c30` | `0x180281c30` | 1597280 | ✓ |
| `fcn.18023d770` | `0x18023d770` | 1532321 | ✓ |
| `fcn.180002d81` | `0x180002d81` | 1507866 | ✓ |
| `fcn.1800991a0` | `0x1800991a0` | 1370482 | ✓ |
| `fcn.180096f70` | `0x180096f70` | 1328482 | ✓ |
| `fcn.180095950` | `0x180095950` | 1296352 | ✓ |
| `fcn.1800a5420` | `0x1800a5420` | 1266569 | ✓ |
| `fcn.18010b5a0` | `0x18010b5a0` | 1255729 | ✓ |
| `fcn.1800a4170` | `0x1800a4170` | 1233274 | ✓ |
| `fcn.1800a4400` | `0x1800a4400` | 1232455 | ✓ |
| `fcn.18014f1a0` | `0x18014f1a0` | 828593 | ✓ |
| `fcn.1801734b0` | `0x1801734b0` | 699007 | ✓ |
| `fcn.18029d050` | `0x18029d050` | 635753 | ✓ |
| `fcn.180299a20` | `0x180299a20` | 634153 | ✓ |
| `fcn.18029a8a0` | `0x18029a8a0` | 625448 | ✓ |
| `fcn.180294e70` | `0x180294e70` | 624393 | ✓ |
| `fcn.180294e30` | `0x180294e30` | 622232 | ✓ |
| `fcn.18029bc10` | `0x18029bc10` | 618504 | ✓ |
| `fcn.18029e8e0` | `0x18029e8e0` | 616617 | ✓ |
| `fcn.180295c50` | `0x180295c50` | 616312 | ✓ |
| `fcn.18029dbc0` | `0x18029dbc0` | 611000 | ✓ |
| `fcn.1801d7140` | `0x1801d7140` | 605914 | ✓ |
| `fcn.1801d7070` | `0x1801d7070` | 599690 | ✓ |

### Decompiled Code Files

- [`code/fcn.180002d81.c`](code/fcn.180002d81.c)
- [`code/fcn.180095950.c`](code/fcn.180095950.c)
- [`code/fcn.180096f70.c`](code/fcn.180096f70.c)
- [`code/fcn.1800991a0.c`](code/fcn.1800991a0.c)
- [`code/fcn.18009be90.c`](code/fcn.18009be90.c)
- [`code/fcn.18009bef0.c`](code/fcn.18009bef0.c)
- [`code/fcn.18009bfb0.c`](code/fcn.18009bfb0.c)
- [`code/fcn.18009c010.c`](code/fcn.18009c010.c)
- [`code/fcn.18009c070.c`](code/fcn.18009c070.c)
- [`code/fcn.1800a3da0.c`](code/fcn.1800a3da0.c)
- [`code/fcn.1800a4170.c`](code/fcn.1800a4170.c)
- [`code/fcn.1800a4400.c`](code/fcn.1800a4400.c)
- [`code/fcn.1800a5420.c`](code/fcn.1800a5420.c)
- [`code/fcn.1800b7640.c`](code/fcn.1800b7640.c)
- [`code/fcn.18010b5a0.c`](code/fcn.18010b5a0.c)
- [`code/fcn.18014f1a0.c`](code/fcn.18014f1a0.c)
- [`code/fcn.1801734b0.c`](code/fcn.1801734b0.c)
- [`code/fcn.1801d7070.c`](code/fcn.1801d7070.c)
- [`code/fcn.1801d7140.c`](code/fcn.1801d7140.c)
- [`code/fcn.18023d770.c`](code/fcn.18023d770.c)
- [`code/fcn.180281c30.c`](code/fcn.180281c30.c)
- [`code/fcn.180294e30.c`](code/fcn.180294e30.c)
- [`code/fcn.180294e70.c`](code/fcn.180294e70.c)
- [`code/fcn.180295c50.c`](code/fcn.180295c50.c)
- [`code/fcn.180299a20.c`](code/fcn.180299a20.c)
- [`code/fcn.18029a8a0.c`](code/fcn.18029a8a0.c)
- [`code/fcn.18029bc10.c`](code/fcn.18029bc10.c)
- [`code/fcn.18029d050.c`](code/fcn.18029d050.c)
- [`code/fcn.18029dbc0.c`](code/fcn.18029dbc0.c)
- [`code/fcn.18029e8e0.c`](code/fcn.18029e8e0.c)

## Behavioral Analysis

Based on the provided disassembly and string data, here is an analysis of the binary's behavior and characteristics:

### Core Functionality and Purpose
The code appears to be part of a **highly obfuscated, virtualized, or "packed" executable**. Rather than performing direct system calls for typical actions (like file I/O or network communication), it utilizes a complex internal execution engine. 

A primary indicator is the repetitive structure of the functions (`fcn.18009be0` through `fcn.18009be90`). These function as **dispatchers** for an internal virtual machine (VM). They interpret "opcodes" or state changes to drive the program's logic, a technique commonly used by packers and protectors to hide the true intent of the malware from static analysis.

### Suspicious or Malicious Behaviors
While the provided snippets do not show direct high-level actions (like stealing files), they exhibit several behaviors consistent with advanced malware:

*   **Custom VM / Interpreter Loop:** Functions like `fcn.180096f70` and `fcn.1800991a0` act as dispatchers. They check internal values (e.g., comparing offsets to constants like `0x47`, `0x6f`, `0x54`, `0x72`) to determine which sub-routine to execute. This is a classic way to hide malicious logic behind a layer of "fake" instruction sets.
*   **Code Obfuscation & Shielding:** The repeated structure and reliance on cross-references rather than direct execution suggest the code has been processed by an obfuscator (e.g., VMProtect or similar). This is designed to hinder analysts from finding the true "malicious payload."
*   **Data Manipulation/Decryption Hooks:** Function `fcn.180281c30` contains loops that swap and process data blocks, while `fcn.1800a5420` uses complex bitwise arithmetic and overflow checks (e.g., `SCARRY4`). These are common patterns in **decryption routines** where the malware decrypts its next stage or "unpacks" its primary payload into memory.

### Notable Techniques or Patterns
*   **Opcode Handling:** The use of ASCII-like constants (such as `0x47` ('G') and `0x6f` ('o')) inside dispatcher functions suggests the malware is interpreting a custom command set to perform actions like data movement, logic checks, or environment sensing.
*   **State Management:** The "getter/setter" style of the functions in the `18009xxx` range suggests that the program maintains a complex internal state machine. It validates memory locations and "sets up" variables before jumping to different code blocks based on those values.
*   **Indirection Layering:** The high frequency of calls to internal "helper" functions (like `fcn.1800072f0` or `fcn.18014c1c0`) indicates a design intended to separate the malicious logic from the underlying system interactions, making it harder to trace where a specific action (like opening a socket) originates.
*   **Obfuscated Logic:** The use of very large offsets and non-standard calling conventions suggests a "spaghetti" code structure designed specifically to exhaust manual analysis time.

### Summary for Incident Response
The sample exhibits **high indicators of sophisticated obfuscation**. It is likely a loader or a protected component of an advanced malware suite (e.g., a Trojan, ransomware, or spyware). The presence of a custom interpreter suggests that the true malicious capabilities (such as process injection, keylogging, or C2 communication) are hidden within the "virtual" instructions and would only be visible during dynamic analysis/debugging of the unpacked state.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The sample utilizes a custom virtual machine (VM), opcode-based dispatchers, and complex state management to hide its true logic from static analysis. |
| **T1027.001** | Obfuscated Executable Files | The analysis identifies specific decryption routines and bitwise arithmetic used to unpack or decrypt additional payload stages into memory. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here is the intelligence extraction:

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified. (Note: The string `.rdata`, `.pdata`, etc., are standard PE header sections and were excluded as false positives).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Malware Family/Type Indicators:** The analysis indicates the presence of a **Custom Virtual Machine (VM)** architecture and heavy obfuscation likely utilizing a packer like **VMProtect**.
*   **Technical Patterns:** 
    *   Use of **dispatcher functions** (`fcn.18009be0` through `fcn.18009be90`) to handle internal opcodes.
    *   **Decryption/Unpacking Loops:** Identified in `fcn.180281c30` and `fcn.1800a5420`.
    *   **Instruction Obfuscation:** Use of non-standard calling conventions and "spaghetti" code structures to hinder static analysis.

---
**Analyst Note:** 
The provided data does not contain direct infrastructure IOCs (such as C2 IP addresses or specific file paths). The string segment appears to consist primarily of high-entropy, obfuscated data typical of a protected loader. The primary "indicators" in this case are behavioral—specifically the use of a custom interpreter to hide malicious functionality.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for this sample:

1.  **Malware family**: Unknown
2.  **Malware type**: Loader
3.  **Confidence**: Medium
4.  **Key evidence**:
    *   **Virtual Machine Architecture:** The identification of a custom internal VM and dispatcher functions (`fcn.18009be0` through `fcn.18009be90`) indicates the sample is designed to hide its primary malicious logic within a proprietary instruction set.
    *   **Decryption/Unpacking Routines:** The detection of complex bitwise arithmetic and loop-based data processing (`fcn.180281c30` and `fcn.1800a5420`) is characteristic of loaders designed to decrypt and inject subsequent stages into memory.
    *   **Sophisticated Obfuscation:** The lack of direct indicators (IPs, URLs) combined with the "spaghetti" code structure suggests a high-level protection layer (similar to VMProtect) used primarily to shield the core functionality of an underlying threat.
