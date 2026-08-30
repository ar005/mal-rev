# Threat Analysis Report

**Generated:** 2026-08-24 20:29 UTC
**Sample:** `11e8084e7792e38c432e041b5b0e4341cbd21c97e050ab2739e77e7fe30d0d1b_11e8084e7792e38c432e041b5b0e4341cbd21c97e050ab2739e77e7fe30d0d1b.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `11e8084e7792e38c432e041b5b0e4341cbd21c97e050ab2739e77e7fe30d0d1b_11e8084e7792e38c432e041b5b0e4341cbd21c97e050ab2739e77e7fe30d0d1b.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 5 sections |
| Size | 41,984 bytes |
| MD5 | `800768153601e6261bcf573cc23d145a` |
| SHA1 | `0b7a16e29da0d24a5bc570131aaa836f31d2a77f` |
| SHA256 | `11e8084e7792e38c432e041b5b0e4341cbd21c97e050ab2739e77e7fe30d0d1b` |
| Overall entropy | 6.519 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1777606222 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 20,480 | 6.013 | No |
| `.data` | 16,384 | 6.934 | No |
| `.pdata` | 512 | 3.822 | No |
| `.idata` | 2,560 | 3.864 | No |
| `.rsrc` | 1,024 | 3.241 | No |

### Imports

**KERNEL32.dll**: `HeapFree`, `GetProcessHeap`, `CreateMutexW`, `OpenMutexW`, `Sleep`, `GetCurrentProcess`, `ExitProcess`, `CreateThread`, `OpenProcess`, `GetSystemDirectoryW`, `VirtualProtect`, `GetModuleFileNameW`, `GetModuleHandleW`, `GetProcAddress`, `LoadLibraryW`
**USER32.dll**: `GetClipboardSequenceNumber`, `CloseClipboard`, `OpenClipboard`, `wsprintfW`, `SetClipboardData`, `IsClipboardFormatAvailable`, `EmptyClipboard`, `GetClipboardData`
**ADVAPI32.dll**: `OpenProcessToken`, `RegCloseKey`, `RegCreateKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `RegSetValueExW`, `GetUserNameW`, `GetTokenInformation`
**ole32.dll**: `CoCreateInstance`, `CoUninitialize`, `CoInitializeEx`
**OLEAUT32.dll**: `SysFreeString`, `SysAllocString`, `VariantInit`

## Extracted Strings

Total strings found: **446** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Richgt
`.data
.pdata
@.idata
@.rsrc
1DF4A9231DCD4F5F
RtlGetVersion
.rdata
.rdata$voltmd
.rdata$zzzdbg
.text$mn
.xdata
.pdata
.idata$5
.idata$2
.idata$3
.idata$4
.idata$6
.rsrc$01
.rsrc$02
t$ UWATAVAWH
A_A^A\_]
@SUVWH
D f9,Kt
UWATAVAWH
A_A^A\_]
@USVWATAUAVAWH
A_A^A]A\_^[]
@USVWAVH
A^_^[]
tSHcA<E3
@SUVWAVAWH
(A_A^_^][
@USVWATAUAVAWH
A_A^A]A\_^[]
UVWATAUAVAWH
`A_A^A]A\_^]
UVWATAUAVAWH
?,t
fA9
A_A^A]A\_^]
@USVWATAVAWH
PA_A^A\_^[]
SUVWATAUAVAWH
A_A^A]A\_^][
@USVWATAUAVAWH
@SUVWH
UAVAWH
UVWATAUAVAWH
@A_A^A]A\_^]
UVWATAUAVAWH
D`4uB
A_A^A]A\_^]
SUVWATAUAVAWH
8A_A^A]A\_^][
@SUVWAVH
0A^_^][
@SUVWH
@SUVWAVAWH
UVWATAUAVAWH
<$,tfE9$t
fE9$t
A_A^A]A\_^]
@SVWAVH
(A^_^[
@SUVWAVAWH
(A_A^_^][
@SUVWATAVAWH
PA_A^A\_^][
@SUVWH
p`P
0
db8[z|0
Y;Yn'k
|>-Wa&
>a#e*k
\F&YXe
[yu<nQ.
N6&ig-
]bG~IE
%2Y!6V
]8hBFV
5~gufL
g:<dLN,
Z
z^Cg8
Keiy;~x
++&\01
[5CvyxQ
g^'a<G`
GzKJAg
M9M9M=M
M8M(M?M4M
M#M+M"M
,M)M;M,M=M$M~M
McM)M!M!M
M4M>M9M(M M
|McM{McMzM
McM{M}McM
M{McM|MxMtM
|MtM{McM
MxM|McM|M}MzMcM|M~M}M
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140004614` | `0x140004614` | 2127 | ✓ |
| `fcn.140002600` | `0x140002600` | 1433 | ✓ |
| `fcn.140003b94` | `0x140003b94` | 893 | ✓ |
| `fcn.140002e70` | `0x140002e70` | 861 | ✓ |
| `fcn.140003688` | `0x140003688` | 756 | ✓ |
| `fcn.140001a24` | `0x140001a24` | 697 | ✓ |
| `fcn.14000404c` | `0x14000404c` | 642 | ✓ |
| `fcn.1400031d0` | `0x1400031d0` | 638 | ✓ |
| `fcn.1400054f4` | `0x1400054f4` | 632 | ✓ |
| `fcn.14000132c` | `0x14000132c` | 631 | ✓ |
| `fcn.1400042d0` | `0x1400042d0` | 631 | ✓ |
| `entry0` | `0x140002330` | 570 | ✓ |
| `fcn.140003450` | `0x140003450` | 566 | ✓ |
| `fcn.140001ce0` | `0x140001ce0` | 559 | ✓ |
| `fcn.140002bb8` | `0x140002bb8` | 522 | ✓ |
| `fcn.140001828` | `0x140001828` | 507 | ✓ |
| `fcn.140004e64` | `0x140004e64` | 427 | ✓ |
| `fcn.140001f94` | `0x140001f94` | 416 | ✓ |
| `fcn.140005a8c` | `0x140005a8c` | 278 | ✓ |
| `fcn.140005850` | `0x140005850` | 278 | ✓ |
| `fcn.1400015a4` | `0x1400015a4` | 273 | ✓ |
| `fcn.140002220` | `0x140002220` | 271 | ✓ |
| `fcn.140003f44` | `0x140003f44` | 263 | ✓ |
| `fcn.140001724` | `0x140001724` | 260 | ✓ |
| `fcn.140005968` | `0x140005968` | 183 | ✓ |
| `fcn.140004548` | `0x140004548` | 168 | ✓ |
| `fcn.14000256c` | `0x14000256c` | 146 | ✓ |
| `fcn.140002dc4` | `0x140002dc4` | 145 | ✓ |
| `fcn.140001f10` | `0x140001f10` | 132 | ✓ |
| `fcn.140005164` | `0x140005164` | 125 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.14000132c.c`](code/fcn.14000132c.c)
- [`code/fcn.1400015a4.c`](code/fcn.1400015a4.c)
- [`code/fcn.140001724.c`](code/fcn.140001724.c)
- [`code/fcn.140001828.c`](code/fcn.140001828.c)
- [`code/fcn.140001a24.c`](code/fcn.140001a24.c)
- [`code/fcn.140001ce0.c`](code/fcn.140001ce0.c)
- [`code/fcn.140001f10.c`](code/fcn.140001f10.c)
- [`code/fcn.140001f94.c`](code/fcn.140001f94.c)
- [`code/fcn.140002220.c`](code/fcn.140002220.c)
- [`code/fcn.14000256c.c`](code/fcn.14000256c.c)
- [`code/fcn.140002600.c`](code/fcn.140002600.c)
- [`code/fcn.140002bb8.c`](code/fcn.140002bb8.c)
- [`code/fcn.140002dc4.c`](code/fcn.140002dc4.c)
- [`code/fcn.140002e70.c`](code/fcn.140002e70.c)
- [`code/fcn.1400031d0.c`](code/fcn.1400031d0.c)
- [`code/fcn.140003450.c`](code/fcn.140003450.c)
- [`code/fcn.140003688.c`](code/fcn.140003688.c)
- [`code/fcn.140003b94.c`](code/fcn.140003b94.c)
- [`code/fcn.140003f44.c`](code/fcn.140003f44.c)
- [`code/fcn.14000404c.c`](code/fcn.14000404c.c)
- [`code/fcn.1400042d0.c`](code/fcn.1400042d0.c)
- [`code/fcn.140004548.c`](code/fcn.140004548.c)
- [`code/fcn.140004614.c`](code/fcn.140004614.c)
- [`code/fcn.140004e64.c`](code/fcn.140004e64.c)
- [`code/fcn.140005164.c`](code/fcn.140005164.c)
- [`code/fcn.1400054f4.c`](code/fcn.1400054f4.c)
- [`code/fcn.140005850.c`](code/fcn.140005850.c)
- [`code/fcn.140005968.c`](code/fcn.140005968.c)
- [`code/fcn.140005a8c.c`](code/fcn.140005a8c.c)

## Behavioral Analysis

### Overview
This binary appears to be a sophisticated **malware loader or dropper**. Its primary purpose is to de-obfuscate and prepare an internal payload, potentially for injection into another process or for subsequent execution as a secondary stage of an attack. The code exhibits multiple indicators of malicious intent, including heavy use of string encryption/decryption, dynamic API resolution, and "timestomping" to evade forensic detection.

### Key Behaviors & Suspicious Activities

*   **Multi-Stage Payload Decryption:**
    *   Several functions (e.g., `fcn.1400031d0`, `fcn.140003f44`, `fcn.1400054f4`) perform **XOR operations** on memory buffers (using keys like `0x75` and `0x42`). This is a classic technique to hide strings, configuration data, or embedded shellcode from static analysis tools.
    *   The routine in `fcn.1400031d0` specifically reads the binary's own file into memory and performs XOR operations on it if the "MZ" header is detected. This suggests the binary contains an encrypted secondary stage that is decrypted in-memory only during execution.

*   **Evasive Persistence & File Manipulation:**
    *   **Timestomping:** The function `fcn.14000220` retrieves system file timestamps and applies them to new files (likely the dropped payload). This is a common anti-forensics technique used to make a newly created malicious file appear as if it has existed on the system for a long time.
    *   **Registry Interaction:** The binary interacts with the Windows Registry (`RegCreateKeyExW`, `RegSetValueExW`) to store configuration data or potentially establish persistence.

*   **Anti-Analysis & Obfuscation Techniques:**
    *   **Dynamic API Resolution:** Instead of a standard Import Address Table (IAT), many functions use "stub" calls and custom resolvers (`fcn.140002dc4`, `fcn.1400051e4`). This is used to hide the program's true capabilities from simple static analysis.
    *   **Memory Permissions Manipulation:** The code frequently calls `VirtualProtect` to change memory regions (likely from Read/Write to Execute). This is a hallmark of **shellcode preparation** or "hollowing," where a piece of memory is prepared to run and execute malicious instructions.

*   **Process & Thread Management:**
    *   The entry point (`entry0`) initiates multiple threads using `CreateThread`. These concurrent threads likely handle different tasks, such as maintaining a connection to a C2 (Command and Control) server while the primary thread handles decryption or injection.
    *   A "Mutex" check is performed early in the execution, which is often used by malware to ensure only one instance of the infection is running at any given time.

### Notable Technical Patterns
*   **Shellcode Preparation:** The combination of `VirtualProtect` (to grant execute permissions) and the XOR-based decoding loops strongly suggests that the final stage of this program's execution is a shellcode payload.
*   **Dynamic Loading:** The usage of `GetModuleHandleW` and `GetProcAddress` with dynamically calculated offsets shows an intent to hide the use of sensitive Windows APIs (like those for networking or process injection).
*   **Delayed Execution:** A loop calling `Sleep(60000)` (60 seconds) and later `120000` is often used to bypass "sandbox" environments that only monitor a file for a few minutes after execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027.001 | Obfuscated Files (XOR) | The malware utilizes XOR operations to mask strings, configuration data, and the embedded "MZ" payload from static analysis tools. |
| T1070.006 | Timestomping | The binary actively modifies file timestamps to make newly dropped payloads appear as older, legitimate files to evade forensic detection. |
| T1112 | Registry Run Keys / Startup Folder | The use of `RegCreateKeyExW` and `RegSetValueExW` indicates an attempt to store configuration data or establish persistence within the Windows Registry. |
| T1106 | Dynamic Resolution | The malware uses custom resolvers and `GetProcAddress` to resolve functions at runtime, hiding its true capabilities from the Import Address Table (IAT). |
| T1055 | Process Injection | The frequent use of `VirtualProtect` to change memory permissions is a primary indicator of preparing shellcode for execution or injection into another process. |

---

## Indicators of Compromise

Based on the provided string dump and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   *None identified.* (Note: The behavior analysis confirms registry interaction via `RegCreateKeyExW` and `RegSetValueExW`, but no specific keys or paths were provided in the source text.)

**Mutex names / Named pipes**
*   *None identified.* (Note: A mutex check is mentioned as a behavioral indicator, but no specific naming string was provided.)

**Hashes**
*   `1DF4A9231DCD4F5F` (Note: This 16-character hex string does not follow standard MD5 or SHA formats; it may be an internal identifier or key).

**Other artifacts**
*   **XOR Decryption Keys:** `0x75`, `0x42` (Used for decrypting memory buffers/payloads)
*   **Anti-Sandbox Sleep Durations:** `60,000` ms, `120,000` ms (Identified as a technique to bypass automated sandboxes).

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
* **Multi-Stage Payload Decryption:** The binary uses XOR operations (keys `0x75`, `0x42`) to decrypt an embedded "MZ" header, which is a classic signature of a loader designed to unpack or reveal a secondary malicious payload in memory.
* **Advanced Evasion Tactics:** The presence of "timestomping" (modifying file timestamps), anti-sandbox sleep loops (60s/120s), and dynamic API resolution indicates a high level of sophistication intended to bypass both automated analysis and manual forensic scrutiny.
* **Shellcode Preparation:** The repeated use of `VirtualProtect` to change memory permissions, combined with the decryption of internal buffers, strongly identifies the primary role of this binary as a vehicle for injecting or executing shellcode.
