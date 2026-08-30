# Threat Analysis Report

**Generated:** 2026-08-15 17:21 UTC
**Sample:** `0f0382c0a26ab086d40ed788733860d08acde953210f609e92a8da2b4112f31a_0f0382c0a26ab086d40ed788733860d08acde953210f609e92a8da2b4112f31a.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f0382c0a26ab086d40ed788733860d08acde953210f609e92a8da2b4112f31a_0f0382c0a26ab086d40ed788733860d08acde953210f609e92a8da2b4112f31a.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 10 sections |
| Size | 9,077,760 bytes |
| MD5 | `8a1ef55162742d5e82187ecd86900e33` |
| SHA1 | `aabc18822b6cc932ca233320f77f48f583d7416b` |
| SHA256 | `0f0382c0a26ab086d40ed788733860d08acde953210f609e92a8da2b4112f31a` |
| Overall entropy | 8.0 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1780433117 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 8,704 | 5.911 | No |
| `.data` | 512 | 1.413 | No |
| `.rdata` | 9,059,328 | 8.0 | ⚠️ Yes |
| `.pdata` | 1,024 | 3.074 | No |
| `.xdata` | 512 | 3.685 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 2,560 | 3.79 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 2,720 | 2.437 | No |
| `.reloc` | 512 | 1.973 | No |

### Imports

**KERNEL32.dll**: `CloseHandle`, `CopyFileW`, `CreateDirectoryW`, `CreateProcessW`, `CreateThread`, `DeleteCriticalSection`, `EnterCriticalSection`, `GetLastError`, `GetModuleFileNameW`, `GetModuleHandleA`, `GetProcessHeap`, `GetStartupInfoA`, `GetSystemInfo`, `GlobalMemoryStatusEx`, `HeapAlloc`
**msvcrt.dll**: `__getmainargs`, `__initenv`, `__iob_func`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_cexit`, `_commode`, `_fmode`, `_initterm`, `atexit`, `abort`, `calloc`, `exit`
**USER32.dll**: `GetCursorPos`, `wsprintfW`

## Extracted Strings

Total strings found: **19697** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
@.reloc
AWAVAUATUWVSH
X[^_]A\A]A^A_
8MZuDHcP<H
xoLc5/
AUATUWVSH
([^_]A\A]
[^_]A\
D$,9D$$
H;D$Xr
D$P9D$H
D$T9D$L
UAWAVAUATWVSH
[^_A\A]A^A_]
H=CCG t}
([^_]H
@' t	H
ntdll.dll
q]uXj=
mU"bx;
X)I
1zA:4
MaYf
B
8wV@	(
a}:"X0
yA;|_t
LwNpmD+a7
B.As@
,AXx_<J	7
u:Se);6
xE(E-o!U
n-fYoO
)+~s4r
joCysn 
x2"[*8
kRl3Gk
}0lqNM
W;v!py
[
q#oBA{
?<ke]<
9|118!
]!"p]tI
qCVq]us
H0/MsF
	\R6	U
,,zy{
x_tD8I
E~FPJQ\YM
5K	;A
!,WT<
H0/UsN7
F7-s@Y
eI<t7
eI<t7]
 y_tIL
PZtI'|^;
I:;o}F
DB6As@@NU
Vf,}z_t
5qrsF;
EsFU1Mg
p)o|F=E
R5J&7
}*&'p]u
1XlZI<
Q14|DG
UM7hdF
k/kl:Cs
NW	6z
.[[<?n
1gR/)H
+i6%fM
6^xHN
!@v;}$,
JWR@"u
$EW	^,r
U&/7Z%
;&|^wSb
3ia3pqY
KmgqEp
?}./Yw
Wg|b6Q
LsW'WLr
EV)(	 
39#@_U<=
{mlO0C[
Xax7U	
?fYSXwv
x4N	8u
`Bz>l5~O&
}J{Z6~
\w.Ax5
#7S\ 7Y
<~^t 
qU"SG:+q
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140002f80` | `0x140002f80` | 6131 | ✓ |
| `fcn.140002340` | `0x140002340` | 2910 | ✓ |
| `fcn.140001b40` | `0x140001b40` | 1874 | ✓ |
| `fcn.140001020` | `0x140001020` | 1024 | ✓ |
| `fcn.140001f70` | `0x140001f70` | 974 | ✓ |
| `fcn.140001e00` | `0x140001e00` | 368 | ✓ |
| `fcn.140001620` | `0x140001620` | 367 | ✓ |
| `fcn.140002850` | `0x140002850` | 258 | ✓ |
| `fcn.140001580` | `0x140001580` | 155 | ✓ |
| `fcn.1400014a0` | `0x1400014a0` | 135 | ✓ |
| `fcn.140002a90` | `0x140002a90` | 128 | ✓ |
| `entry1` | `0x140001c10` | 123 | ✓ |
| `fcn.1400026c0` | `0x1400026c0` | 106 | ✓ |
| `fcn.140001da0` | `0x140001da0` | 96 | ✓ |
| `fcn.140002da0` | `0x140002da0` | 64 | ✓ |
| `fcn.140002b10` | `0x140002b10` | 55 | ✓ |
| `fcn.140002bd0` | `0x140002bd0` | 54 | ✓ |
| `fcn.140002d60` | `0x140002d60` | 50 | ✓ |
| `fcn.140002e60` | `0x140002e60` | 31 | ✓ |
| `fcn.140001bc0` | `0x140001bc0` | 31 | ✓ |
| `entry0` | `0x140001420` | 29 | ✓ |
| `fcn.140002e40` | `0x140002e40` | 22 | ✓ |
| `entry2` | `0x140001bf0` | 21 | ✓ |
| `fcn.140002e10` | `0x140002e10` | 11 | ✓ |
| `fcn.140002e30` | `0x140002e30` | 11 | ✓ |
| `fcn.140002de0` | `0x140002de0` | 11 | ✓ |
| `fcn.140002df0` | `0x140002df0` | 11 | ✓ |
| `fcn.140002e00` | `0x140002e00` | 11 | ✓ |
| `sub.msvcrt.dll__cexit` | `0x140002ea8` | 6 | ✓ |
| `sub.msvcrt.dll___iob_func` | `0x140002e88` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/entry2.c`](code/entry2.c)
- [`code/fcn.140001020.c`](code/fcn.140001020.c)
- [`code/fcn.1400014a0.c`](code/fcn.1400014a0.c)
- [`code/fcn.140001580.c`](code/fcn.140001580.c)
- [`code/fcn.140001620.c`](code/fcn.140001620.c)
- [`code/fcn.140001b40.c`](code/fcn.140001b40.c)
- [`code/fcn.140001bc0.c`](code/fcn.140001bc0.c)
- [`code/fcn.140001da0.c`](code/fcn.140001da0.c)
- [`code/fcn.140001e00.c`](code/fcn.140001e00.c)
- [`code/fcn.140001f70.c`](code/fcn.140001f70.c)
- [`code/fcn.140002340.c`](code/fcn.140002340.c)
- [`code/fcn.1400026c0.c`](code/fcn.1400026c0.c)
- [`code/fcn.140002850.c`](code/fcn.140002850.c)
- [`code/fcn.140002a90.c`](code/fcn.140002a90.c)
- [`code/fcn.140002b10.c`](code/fcn.140002b10.c)
- [`code/fcn.140002bd0.c`](code/fcn.140002bd0.c)
- [`code/fcn.140002d60.c`](code/fcn.140002d60.c)
- [`code/fcn.140002da0.c`](code/fcn.140002da0.c)
- [`code/fcn.140002de0.c`](code/fcn.140002de0.c)
- [`code/fcn.140002df0.c`](code/fcn.140002df0.c)
- [`code/fcn.140002e00.c`](code/fcn.140002e00.c)
- [`code/fcn.140002e10.c`](code/fcn.140002e10.c)
- [`code/fcn.140002e30.c`](code/fcn.140002e30.c)
- [`code/fcn.140002e40.c`](code/fcn.140002e40.c)
- [`code/fcn.140002e60.c`](code/fcn.140002e60.c)
- [`code/fcn.140002f80.c`](code/fcn.140002f80.c)
- [`code/sub.msvcrt.dll___iob_func.c`](code/sub.msvcrt.dll___iob_func.c)
- [`code/sub.msvcrt.dll__cexit.c`](code/sub.msvcrt.dll__cexit.c)

## Behavioral Analysis

### Analysis Summary
The provided code is characteristic of a **malware dropper and installer**. It uses several advanced techniques to evade detection, establish persistence, and execute malicious commands with elevated privileges.

---

### Core Functionality and Purpose
The program's primary purpose is to "drop" a payload onto the system, hide its presence by masquerading as a legitimate service, and ensure it remains running across reboots. It acts as a wrapper for a more complex set of instructions (likely delivered via PowerShell).

---

### Suspicious and Malicious Behaviors

*   **Process Injection & In-Memory Execution:**
    *   In `fcn.140002f80`, the code allocates memory (`VirtualAlloc`), decrypts/decodes a block of data (evidenced by the XOR loop and manual buffer copying), and then uses `CreateThread` to execute this new, decrypted code. This is a classic technique to run malicious code without it ever touching the disk in its "raw" form.
*   **Anti-Analysis & Sandbox Evasion:**
    *   **Delayed Execution:** The code calls `Sleep(0x5dc)` (roughly 15 minutes). This is a common tactic to bypass automated sandboxes that only monitor a sample for a few minutes.
    *   **Human Interaction Check:** The code compares the current cursor position with a previously recorded one after the sleep period (`GetCursorPos`). If the mouse moves, it implies a human is present; if not, it may indicate an automated sandbox environment.
*   **Persistence via Scheduled Tasks & Registry:**
    *   The sample generates a complex PowerShell command to create a **Scheduled Task** named `WU_CompatCheck`. It sets high-level privileges (`RunLevel Highest`) and forces the task to run as the **SYSTEM** account. 
    *   It also attempts to add a key to the `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` registry key, ensuring it starts every time the user logs in.
*   **Defense Evasion (Anti-Antivirus):**
    *   The PowerShell command explicitly includes: `Add-MpPreference -ExclusionPath ...`. This is a direct instruction to **Windows Defender** to ignore any files or folders associated with this malware's path.
*   **Masquerading and File Manipulation:**
    *   In `fcn.140001620`, the code copies itself (or a related component) into a system-like directory: `C:\ProgramData\Microsoft\WwanSvc` and renames it to `WwanPrvSvc.exe`. "Wwan" typically refers to Wireless Wide Area Network, making the name look like a legitimate Windows networking service.

---

### Notable Techniques & Patterns Observed

*   **Multi-Stage Execution:** The binary uses a small "loader" (the current code) to unpack and execute an embedded payload in memory, while also using a PowerShell script as a secondary persistence mechanism.
*   **PowerShell as a Loader:** By constructing the complex PowerShell string inside the C code, the malware attempts to hide its true intentions from simple static analysis of the binary's strings (as the full command is only assembled at runtime).
*   **System API Abuse:**
    *   `VirtualProtect`: Used in `fcn.140001580` and `fcn.140001e00` to change memory permissions, often used to bypass memory protections or hooks.
    *   `CreateProcessW`: Executed with a heavily obfuscated/constructed command line to launch the PowerShell stager.
*   **Fake Branding:** Using names like `WU_CompatCheck` (Windows Update Compatibility Check) and `WwanPrvSvc.exe` is a common tactic to blend into standard Windows system logs and folders, making it harder for an admin to spot during a manual audit.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Process Injection | The use of `VirtualAlloc`, manual memory decoding, and `CreateThread` indicates an attempt to execute malicious code directly in memory to avoid detection. |
| **T1497** | Virtualization/Sandbox Evasion | The implementation of a 15-minute sleep timer and mouse cursor positioning checks are classic tactics used to bypass automated analysis environments. |
| **T1053** | Scheduled Task/Job | The creation of the `WU_CompatCheck` task ensures that the malware executes with high privileges and maintains persistence on a schedule. |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys | Adding a key to the `HKCU\...\Run` path ensures the malicious process starts automatically every time the user logs in. |
| **T1562.001** | Impair Defenses: Disable or Remove Security Software | The specific use of `Add-MpPreference -ExclusionPath` is an attempt to white-list the malware's directory within Windows Defender. |
| **T1036** | Masquerading | The choice of names like `WwanPrvSvc.exe` and its placement in a system-like folder are designed to blend in with legitimate Windows networking services. |
| **T1059.001** | Command and Scripting Interpreter: PowerShell | Using complex, dynamically constructed PowerShell strings allows the attacker to hide the full scope of their commands from static analysis. |
| **T1027** | Obfuscated Files or Information | The use of an XOR loop to decode data before execution demonstrates an attempt to hide malicious payloads from signature-based detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Path:** `C:\ProgramData\Microsoft\WwanSvc` (Used for staging and masquerading)
*   **Filename:** `WwanPrvSvc.exe` (Malicious executable masquerading as a networking service)

**Mutex names / Named pipes**
*   **Scheduled Task Name:** `WU_CompatCheck` (Used for persistence; mimics "Windows Update Compatibility Check")

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Defense Evasion Command:** `Add-MpPreference -ExclusionPath ...` (Specifically used to disable Windows Defender protections for the malware's directory).
*   **Persistence Mechanism:** Scheduled Task creation with `RunLevel Highest` and execution under the `SYSTEM` account.
*   **Anti-Analysis Behavior:** 
    *   **Sleep Timer:** `0x5dc` (Approximately 15 minutes) used to bypass sandbox analysis.
    *   **Human Interaction Check:** Use of `GetCursorPos` to determine if a user is present before executing malicious payloads.
*   **Execution Technique:** In-memory execution via `VirtualAlloc`, `CreateThread`, and `VirtualProtect` to execute decrypted/decoded code without touching the disk in raw form.

---

## Malware Family Classification

1. **Malware family**: custom (or Unknown)
2. **Malware type**: dropper / loader
3. **Confidence**: High

4. **Key evidence**:
*   **In-Memory Execution & Staging:** The sample employs classic loader behavior by using `VirtualAlloc`, `CreateThread`, and XOR decoding to execute a decrypted payload directly in memory, avoiding disk-based detection of the raw malicious code.
*   **Advanced Evasion Techniques:** It incorporates multiple layers of anti-analysis, including a long sleep timer (15 minutes) to bypass sandboxes, mouse movement checks (`GetCursorPos`) to detect human interaction, and explicit commands to add its own directory to the Windows Defender exclusion list.
*   **Persistence & Masquerading:** The malware attempts to maintain a permanent presence via a Scheduled Task (`WU_CompatCheck`) and a Registry Run key, while using names like `WwanPrvSvc.exe` and `ProgramData` paths to mimic legitimate system services and blend in with Windows infrastructure.
