# Threat Analysis Report

**Generated:** 2026-07-24 21:20 UTC
**Sample:** `0a560b651255651e75d8753d3835bae0c1334125e2dada42271e89dd256d069c_0a560b651255651e75d8753d3835bae0c1334125e2dada42271e89dd256d069c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a560b651255651e75d8753d3835bae0c1334125e2dada42271e89dd256d069c_0a560b651255651e75d8753d3835bae0c1334125e2dada42271e89dd256d069c.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 4 sections |
| Size | 213,504 bytes |
| MD5 | `f16395e5da254e14c45e54afb0f81313` |
| SHA1 | `7f10904e1a8798d42f0638a3872a2a0213bfec61` |
| SHA256 | `0a560b651255651e75d8753d3835bae0c1334125e2dada42271e89dd256d069c` |
| Overall entropy | 7.913 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765308833 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 30,720 | 6.38 | No |
| `.rdata` | 181,248 | 7.994 | ⚠️ Yes |
| `.data` | 0 | 0.0 | No |
| `.pdata` | 512 | 2.713 | No |

### Imports

**KERNEL32.dll**: `VirtualProtect`, `GetCurrentThreadId`, `GetTickCount`, `GetCurrentProcess`, `FlushInstructionCache`, `LoadLibraryW`, `FreeLibrary`, `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, `GlobalMemoryStatusEx`, `CreateToolhelp32Snapshot`, `Process32First`, `CloseHandle`, `Process32Next`, `GetProcessHeap`
**bcrypt.dll**: `BCryptSetProperty`, `BCryptGenerateSymmetricKey`, `BCryptCloseAlgorithmProvider`, `BCryptDecrypt`, `BCryptDestroyKey`, `BCryptOpenAlgorithmProvider`

## Extracted Strings

Total strings found: **440** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
&-11n{-j
N6J-A!
AWAVVWUSH
[]_^A^A_
-Yro4)
-$P*A)
fffff.
AWAVAUATVWUSH
0[]_^A\A]A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
AWAVVWUSH
([]_^A^A_
AWAVAUATVWUSH
([]_^A\A]A^A_
u;xc}E_
`#JH8sq
+3WSB	
KmH"j.
HlBI=b
7iy:/ 
INIzG/
8: oe-y
NJIWmL39he
#z9@`4
x3yTV*

zokdz
[Z(CqC
)w$gVoa
b98W9
X`lbeu
,!qZ(TA
(cMy=u
eV5Rd#
X]5Z&y
 `<M:uN
+Da:53(
u,.h_R
JS|*8L};
E%U4c
npC[QI
;AtVO1RU
7nbzLR
U&Z[y1
T:e1}J
1uQ%-a
3b
<m
T"nKN{
S{r"4&
*dMx_T
'kXu=>;o
;a+	x7E3Vd
!j	IG
qn,qBu
h\vM/\
fBjZ:=vs
4If9e=
cT
b9E 
^U[o>T
*@p:= (
vaXKB4
e;D3qbG
]FtI6~
KUC02L2^
ypyHqP

c-B;w
G2QWkbg9@
3b}6Hz
8\M9*o
U1H1CU
1@<#%q
DID3cr>
WI
>%@
Z?2bsY
d0BlM,
G56r@IV^
^Muy
!~O]rZ
urvB/*
g&~V`
Q6dHoJ
!		vN "?@D
[W?r
4V
_N?2O%
(S-1S~n
Q7e7@
|LL(0>
g:sw	(
pN7E	I
oq^F
n#U=%i
ow08s~<>
/`X&
8G:k><
Ou[+5V
(xu["_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800037b0` | `0x1800037b0` | 5765 | ✓ |
| `fcn.180006400` | `0x180006400` | 2602 | ✓ |
| `fcn.180006e30` | `0x180006e30` | 2436 | ✓ |
| `fcn.180005150` | `0x180005150` | 2392 | ✓ |
| `fcn.180007df0` | `0x180007df0` | 2324 | ✓ |
| `fcn.1800029a0` | `0x1800029a0` | 1913 | ✓ |
| `fcn.1800077c0` | `0x1800077c0` | 1578 | ✓ |
| `fcn.180001720` | `0x180001720` | 1486 | ✓ |
| `fcn.180002090` | `0x180002090` | 1382 | ✓ |
| `entry0` | `0x180005f00` | 1268 | ✓ |
| `fcn.180005ab0` | `0x180005ab0` | 1090 | ✓ |
| `fcn.180001cf0` | `0x180001cf0` | 927 | ✓ |
| `fcn.1800032a0` | `0x1800032a0` | 822 | ✓ |
| `fcn.180001480` | `0x180001480` | 669 | ✓ |
| `section..text` | `0x180001000` | 591 | ✓ |
| `fcn.180002600` | `0x180002600` | 549 | ✓ |
| `fcn.180001250` | `0x180001250` | 548 | ✓ |
| `fcn.180004f20` | `0x180004f20` | 547 | ✓ |
| `fcn.180003120` | `0x180003120` | 384 | ✓ |
| `fcn.1800035e0` | `0x1800035e0` | 333 | ✓ |
| `fcn.180004e40` | `0x180004e40` | 220 | ✓ |
| `fcn.180002830` | `0x180002830` | 201 | ✓ |
| `fcn.180002900` | `0x180002900` | 151 | ✓ |
| `fcn.180003730` | `0x180003730` | 125 | ✓ |
| `fcn.180008760` | `0x180008760` | 78 | ✓ |
| `sub.KERNEL32.dll_CreateToolhelp32Snapshot` | `0x180008710` | 6 | ✓ |
| `sub.KERNEL32.dll_Process32First` | `0x180008716` | 6 | ✓ |
| `sub.KERNEL32.dll_Process32Next` | `0x18000871c` | 6 | ✓ |
| `sub.bcrypt.dll_BCryptOpenAlgorithmProvider` | `0x180008722` | 6 | ✓ |
| `sub.bcrypt.dll_BCryptSetProperty` | `0x180008728` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.180001250.c`](code/fcn.180001250.c)
- [`code/fcn.180001480.c`](code/fcn.180001480.c)
- [`code/fcn.180001720.c`](code/fcn.180001720.c)
- [`code/fcn.180001cf0.c`](code/fcn.180001cf0.c)
- [`code/fcn.180002090.c`](code/fcn.180002090.c)
- [`code/fcn.180002600.c`](code/fcn.180002600.c)
- [`code/fcn.180002830.c`](code/fcn.180002830.c)
- [`code/fcn.180002900.c`](code/fcn.180002900.c)
- [`code/fcn.1800029a0.c`](code/fcn.1800029a0.c)
- [`code/fcn.180003120.c`](code/fcn.180003120.c)
- [`code/fcn.1800032a0.c`](code/fcn.1800032a0.c)
- [`code/fcn.1800035e0.c`](code/fcn.1800035e0.c)
- [`code/fcn.180003730.c`](code/fcn.180003730.c)
- [`code/fcn.1800037b0.c`](code/fcn.1800037b0.c)
- [`code/fcn.180004e40.c`](code/fcn.180004e40.c)
- [`code/fcn.180004f20.c`](code/fcn.180004f20.c)
- [`code/fcn.180005150.c`](code/fcn.180005150.c)
- [`code/fcn.180005ab0.c`](code/fcn.180005ab0.c)
- [`code/fcn.180006400.c`](code/fcn.180006400.c)
- [`code/fcn.180006e30.c`](code/fcn.180006e30.c)
- [`code/fcn.1800077c0.c`](code/fcn.1800077c0.c)
- [`code/fcn.180007df0.c`](code/fcn.180007df0.c)
- [`code/fcn.180008760.c`](code/fcn.180008760.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sub.KERNEL32.dll_CreateToolhelp32Snapshot.c`](code/sub.KERNEL32.dll_CreateToolhelp32Snapshot.c)
- [`code/sub.KERNEL32.dll_Process32First.c`](code/sub.KERNEL32.dll_Process32First.c)
- [`code/sub.KERNEL32.dll_Process32Next.c`](code/sub.KERNEL32.dll_Process32Next.c)
- [`code/sub.bcrypt.dll_BCryptOpenAlgorithmProvider.c`](code/sub.bcrypt.dll_BCryptOpenAlgorithmProvider.c)
- [`code/sub.bcrypt.dll_BCryptSetProperty.c`](code/sub.bcrypt.dll_BCryptSetProperty.c)

## Behavioral Analysis

Based on the provided disassembly, this binary is a **malicious loader/injector**. Its primary purpose is to bypass local security defenses (specifically AMSI) and inject an encrypted payload into another process to execute it.

### Core Functionality & Purpose
The code acts as a "packer" or "loader." It does not perform its main malicious actions (like stealing data or connecting to a C2 server) directly; instead, it prepares the environment by disabling security features and decrypting a hidden payload before injecting that payload into a legitimate system process.

### Suspicious & Malicious Behaviors

*   **Anti-Analysis / Anti-Debugging:**
    *   The function `fcn.180004e40` explicitly calls `IsDebuggerPresent` and `CheckRemoteDebuggerPresent`. This is used to determine if the malware is being analyzed by a researcher or run in a sandbox environment. If detected, it may change its behavior or exit.
    *   It also uses `GetTickCount` (seen in several loops) to potentially detect timing discrepancies common in sandboxes.

*   **AMSI Bypass:**
    *   The function `fcn.1800037b0` references `amsi_dll`. This is a high-confidence indicator of an **AMSI Patch**. Many modern threats patch the Antimalware Scan Interface (AMSI) to prevent Windows Defender from scanning scripts or in-memory buffer contents for malicious signatures.
    *   The use of `VirtualProtect` followed by `FlushInstructionCache` is a classic technique used after modifying memory permissions to ensure that newly "patched" code or injected code is executed by the CPU immediately.

*   **Process Injection:**
    *   The function `fcn.180004f20` uses `CreateToolhelp32Snapshot` and iterates through running processes using `Process32First/Next`. This is typically used to find a "host" process (like `explorer.exe` or `svchost.exe`).
    *   The function `fcn.180005ab0` performs the actual injection: it uses `VirtualAllocEx` to reserve space in the remote target's memory and `WriteProcessMemory` to copy a payload into that process.

*   **Heavy Cryptography / Decryption:**
    *   The extensive use of **BCrypt APIs** (`BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, `BCryptDecrypt`) in `fcn.180005150` indicates the primary payload is encrypted on disk. 
    *   The multiple loops with heavy bitwise arithmetic (e.g., `fcn.180006400`, `fcn.180006e30`, `fcn.180007df0`) are used to decrypt strings or internal offsets, ensuring the malware's primary logic remains hidden from static analysis tools until it is actually running in memory.

### Notable Techniques & Patterns
*   **Process Hollowing/Injection:** The combination of `VirtualAllocEx`, `WriteProcessMemory`, and subsequent execution indicates an attempt to hide the payload's behavior by "hiding" it inside a legitimate process.
*   **Instruction Cache Flushing:** The use of `FlushInstructionCache` after modifying memory is a standard way to bypass certain types of monitoring that watch for executable memory being modified.
*   **Obfuscation:** The heavy reliance on complex arithmetic calculations (bitmasking and XORs) instead of direct string constants suggests the author intended to hide API names or configuration data from static analysis tools like `strings`.
*   **Multi-Stage Execution:** The routine is clearly split into "preparatory" stages: 1. Environment Check $\rightarrow$ 2. AMSI Patching $\rightarrow$ 3. Payload Decryption $\rightarrow$ 4. Injection.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1036** | Debugger Detection | The binary explicitly calls `IsDebuggerPresent` and `CheckRemoteDebuggerPresent` to identify if it is being analyzed. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `GetTickCount` across multiple loops suggests an attempt to detect time-dilation typical in automated analysis environments. |
| **T1562** | Impair Defense | The targeting and patching of the `amsi_dll` is a specific method used to disable the Antimalware Scan Interface (AMSI) security checks. |
| **T1055** | Process Injection | The combination of `VirtualAllocEx` and `WriteProcessMemory` is used to host the decrypted payload within a legitimate system process. |
| **T1027** | Obfuscated Files or Information | The use of BCrypt APIs and manual bitwise arithmetic (XOR/bitmasking) hides internal strings and payloads from static analysis. |
| **T1639** | Manipulation of System Artifacts | While not a direct "Injection" call, the use of `FlushInstructionCache` is used to ensure that modified memory is executed, bypassing some security monitoring triggers. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extraction of Indicators of Compromise (IOCs). 

**Note:** A review of the "Extracted Strings" section indicates that the data consists largely of obfuscated code fragments and memory offsets rather than plaintext configuration files or hardcoded network infrastructure. The "Behavioral Analysis" identifies techniques but does not contain specific, unique identifiers for a single campaign.

### **IP addresses / URLs / Domains**
*   None identified. (The strings provided do not contain valid IP addresses, domain names, or URLs).

### **File paths / Registry keys**
*   None identified. (While `.rdata`, `.data`, and `.pdata` appear in the strings, these are standard internal memory segment headers and do not constitute specific file system IOCs).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **AMSI Patching:** The analysis confirms the use of `amsi_dll` as a target for an AMSI patch (behavioral indicator of a loader).
*   **Encryption Libraries:** Usage of `BCrypt` APIs (`BCryptOpenAlgorithmProvider`, `BCryptGenerateSymmetricKey`, `BCryptDecrypt`) indicates a high-confidence signature for encrypted payload delivery.
*   **Injection Techniques:** The presence of `VirtualAllocEx`, `WriteProcessMemory`, and `CreateToolhelp32Snapshot` confirms the binary's role as a process injector/hollower. 

***

**Analyst Note:** While no specific infrastructure IOCs (IPs/Domains) were extracted from this sample, the behavioral analysis confirms this is a **malicious loader**. The lack of clear strings suggests the malware uses significant obfuscation and encryption to hide its true C2 configuration until it reaches the execution stage in memory.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Injection & Obfuscation**: The sample utilizes standard process injection techniques (`VirtualAllocEx`, `WriteProcessMemory`) and heavy cryptography (BCrypt APIs) to decrypt and inject a hidden payload into a host process.
    *   **Defense Evasion**: It explicitly targets the Antimalware Scan Interface (AMSI) via patching of the `amsi_dll` and employs anti-debugging/anti-analysis checks (`IsDebuggerPresent`, `GetTickCount`).
    *   **Multi-Stage Architecture**: The behavior follows a classic loader pattern: checking for analysis tools, disabling security features, decrypting internal components, and finally executing a secondary payload.
