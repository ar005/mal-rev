# Threat Analysis Report

**Generated:** 2026-08-31 15:24 UTC
**Sample:** `12815f32a4ba6e894e5d124a7e7c5cf77e8e173bf97162754c70d95cb1cae57e_12815f32a4ba6e894e5d124a7e7c5cf77e8e173bf97162754c70d95cb1cae57e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12815f32a4ba6e894e5d124a7e7c5cf77e8e173bf97162754c70d95cb1cae57e_12815f32a4ba6e894e5d124a7e7c5cf77e8e173bf97162754c70d95cb1cae57e.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 5 sections |
| Size | 113,664 bytes |
| MD5 | `8bc8e88292db8cece3a5152157f7f733` |
| SHA1 | `04b1441de34808783a970901a89baade29fad644` |
| SHA256 | `12815f32a4ba6e894e5d124a7e7c5cf77e8e173bf97162754c70d95cb1cae57e` |
| Overall entropy | 6.368 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1781528516 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 79,872 | 6.55 | No |
| `.rdata` | 19,456 | 5.193 | No |
| `.data` | 5,120 | 3.062 | No |
| `.rsrc` | 512 | 5.105 | No |
| `.reloc` | 7,680 | 4.729 | No |

### Imports

**WININET.dll**: `InternetOpenA`, `InternetOpenUrlA`, `InternetOpenW`, `InternetOpenUrlW`, `InternetReadFile`, `InternetCloseHandle`
**SHLWAPI.dll**: `PathFileExistsW`
**KERNEL32.dll**: `SetStdHandle`, `WriteConsoleW`, `GetConsoleOutputCP`, `WriteConsoleA`, `LoadLibraryA`, `InitializeCriticalSectionAndSpinCount`, `Sleep`, `CreateProcessW`, `CloseHandle`, `CreateFileW`, `ExpandEnvironmentStringsW`, `GetLocaleInfoW`, `DeleteFileW`, `WriteFile`, `GetTickCount`
**USER32.dll**: `wsprintfW`
**SHELL32.dll**: `ShellExecuteW`

## Extracted Strings

Total strings found: **565** (showing first 100)

```
!This program cannot be run in DOS mode.
$
2Yc<v8ov8ov8o
vog8ov8o
ow8oRichv8o
`.rdata
@.data
@.reloc
tBhZA
FYY;uu
FYY;uu
t}9>uyj
M9^Lth
t_9]u
F 98u
F09^(u
8]t	V
u.j^9
QQSVWd
0WWWWW
AAFFf;
p;qt~
0WWWWW
0WWWWW
j
YQPVh
D$+d$SVW
D$+d$SVW
D$+d$SVW
F@uwV
F@uwV
F@WuyV
9}t$9}
9ut)9u
s[S;7|G;w
tR99u2
GWh,\A
t"SS9]
u,9Et'9
tSSSSS
tSSSSS
tSSSSS
tVVVVV
tVVVVV
tVVVVV
t h\A
E9Xt
tVVVVV
tVVVVV
tVVVVV
t$hDkA
0A@@Ju
0SSSSS
>=Yt1j
QQSVWh
j@j ^V
t)jXP
t+WWVPV
FVh,\A
tSSSSS
C PjPV
C$PjQV
C*PjTV
C+PjUV
C,PjVV
C-PjWV
C.PjRV
C/PjSV
0SSSSS
PPPPPPPP
0SSSSS
@9]|FVW
tNhDuA
t=h@uA
Y;Fu!
G9^t;
Y;Fu.j
u49^t/
Vj@hhrA
u%hHuA
PPPPPPPP
URPQQh
;t$,v-
kUQPXY]Y[
8
u
AA
VW|[;
u,VVWV
t VV9u
^SSSSS
^SSSSS
v	N+D$
<xt<Xt	
bad allocation
Tunnel
Tunnel
RtlGetVersion
http://178.16.54.109/lkdomain.exe
slack.exe
Teams.exe
Zoom.exe
sapgui.exe
PBIDesktop.exe
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00404d4a` | `0x404d4a` | 16863 | ✓ |
| `fcn.00405fd1` | `0x405fd1` | 5632 | ✓ |
| `fcn.0040cd99` | `0x40cd99` | 5334 | ✓ |
| `fcn.00403946` | `0x403946` | 5178 | ✓ |
| `fcn.0040ec8c` | `0x40ec8c` | 1843 | ✓ |
| `fcn.004128fb` | `0x4128fb` | 1474 | ✓ |
| `fcn.00410d03` | `0x410d03` | 1051 | ✓ |
| `fcn.00409966` | `0x409966` | 933 | ✓ |
| `fcn.0040a2f0` | `0x40a2f0` | 869 | ✓ |
| `fcn.0040dcb0` | `0x40dcb0` | 869 | ✓ |
| `fcn.0040f5ad` | `0x40f5ad` | 844 | ✓ |
| `fcn.004094fc` | `0x4094fc` | 839 | ✓ |
| `fcn.0040ba94` | `0x40ba94` | 790 | ✓ |
| `fcn.0040b16d` | `0x40b16d` | 770 | ✓ |
| `fcn.0040c243` | `0x40c243` | 741 | ✓ |
| `fcn.0040bf62` | `0x40bf62` | 737 | ✓ |
| `fcn.00402dc0` | `0x402dc0` | 690 | ✓ |
| `fcn.0040e546` | `0x40e546` | 596 | ✓ |
| `fcn.0040af3c` | `0x40af3c` | 561 | ✓ |
| `fcn.00413c60` | `0x413c60` | 559 | ✓ |
| `fcn.004108d6` | `0x4108d6` | 539 | ✓ |
| `fcn.0040b46f` | `0x40b46f` | 539 | ✓ |
| `fcn.00411fc6` | `0x411fc6` | 497 | ✓ |
| `fcn.0040d7e7` | `0x40d7e7` | 485 | ✓ |
| `fcn.00401150` | `0x401150` | 484 | ✓ |
| `fcn.00401380` | `0x401380` | 447 | ✓ |
| `fcn.004102c4` | `0x4102c4` | 442 | ✓ |
| `fcn.00410023` | `0x410023` | 436 | ✓ |
| `fcn.00410b53` | `0x410b53` | 432 | ✓ |
| `method.std::basic_filebuf_char__struct_std::char_traits_char__.virtual_4` | `0x40440e` | 431 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401150.c`](code/fcn.00401150.c)
- [`code/fcn.00401380.c`](code/fcn.00401380.c)
- [`code/fcn.00402dc0.c`](code/fcn.00402dc0.c)
- [`code/fcn.00403946.c`](code/fcn.00403946.c)
- [`code/fcn.00404d4a.c`](code/fcn.00404d4a.c)
- [`code/fcn.00405fd1.c`](code/fcn.00405fd1.c)
- [`code/fcn.004094fc.c`](code/fcn.004094fc.c)
- [`code/fcn.00409966.c`](code/fcn.00409966.c)
- [`code/fcn.0040a2f0.c`](code/fcn.0040a2f0.c)
- [`code/fcn.0040af3c.c`](code/fcn.0040af3c.c)
- [`code/fcn.0040b16d.c`](code/fcn.0040b16d.c)
- [`code/fcn.0040b46f.c`](code/fcn.0040b46f.c)
- [`code/fcn.0040ba94.c`](code/fcn.0040ba94.c)
- [`code/fcn.0040bf62.c`](code/fcn.0040bf62.c)
- [`code/fcn.0040c243.c`](code/fcn.0040c243.c)
- [`code/fcn.0040cd99.c`](code/fcn.0040cd99.c)
- [`code/fcn.0040d7e7.c`](code/fcn.0040d7e7.c)
- [`code/fcn.0040dcb0.c`](code/fcn.0040dcb0.c)
- [`code/fcn.0040e546.c`](code/fcn.0040e546.c)
- [`code/fcn.0040ec8c.c`](code/fcn.0040ec8c.c)
- [`code/fcn.0040f5ad.c`](code/fcn.0040f5ad.c)
- [`code/fcn.00410023.c`](code/fcn.00410023.c)
- [`code/fcn.004102c4.c`](code/fcn.004102c4.c)
- [`code/fcn.004108d6.c`](code/fcn.004108d6.c)
- [`code/fcn.00410b53.c`](code/fcn.00410b53.c)
- [`code/fcn.00410d03.c`](code/fcn.00410d03.c)
- [`code/fcn.00411fc6.c`](code/fcn.00411fc6.c)
- [`code/fcn.004128fb.c`](code/fcn.004128fb.c)
- [`code/fcn.00413c60.c`](code/fcn.00413c60.c)
- [`code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_4.c`](code/method.std__basic_filebuf_char__struct_std__char_traits_char__.virtual_4.c)

## Behavioral Analysis

This updated analysis incorporates your new findings while maintaining the context of the initial report. The additional disassembly provides deeper insight into how the malware manages its internal state, handles network communication protocols, and manages memory for its modules.

### Updated Report: Modular Trojan & Downloader (Analysis 2/2)

#### Core Functionality (Updated)
The analysis confirms that this binary is not a simple downloader; it is a sophisticated **command-and-control (C2) agent**. The added code reveals several underlying mechanisms:

*   **Robust Communication Protocol:** Functions like `fcn.00413c60` and `fcn.0040b16d` indicate that the malware does not just receive commands; it parses a complex, likely proprietary, protocol. The heavy use of state-checking loops suggests it can handle multiple stages of an attack within a single session with the C2 server.
*   **Advanced Memory Management:** The usage of `HeapAlloc`, `HeapReAlloc`, and the dynamic resizing logic in `fcn.004108d6` indicates that the malware handles variable-sized payloads. This is consistent with its modular nature; it allocates exactly what it needs to store or execute a specific "module" (e.g., `lb1..lb19.exe`) upon receipt.
*   **Localization & Global Reach:** The extensive use of `GetLocaleInfoA`, `IsValidCodePage`, and complex conversions between MultiByte and Wide strings (`fcn.00411fc6`, `fcn.004102c4`) confirms that the threat actor designed this for global distribution. This ensures it functions correctly across different regions/languages without crashing due to character encoding issues.

#### New Suspicious & Malicious Behaviors
*   **Dynamic Environment Adaptation:** The binary uses `ExpandEnvironmentStringsW` with `%temp%` and `GetTickCount` to determine where to write files and how much time has elapsed (potentially for "sleep" cycles or heartbeat check-ins). 
*   **Advanced Path Generation:** In `fcn.0041150`, the malware dynamically constructs a filename using `wsprintfW`. This is used to generate paths in the `%temp%` directory, which is a common technique to bypass static path detection by security products.
*   **Data Integrity/Validation:** The complex logic in functions like `fcn.0040b16d` and `fcn.0040c243` suggests it performs validation on data received from the C2 server before processing it, ensuring that its "modules" are correctly formatted and functional.
*   **Persistence & Context Awareness:** The check for specific locales and the handling of system-level handles in `fcn.0040e546` suggest the malware adjusts its behavior based on the local environment to remain stealthy or to target specifically configured corporate systems.

#### Technical Detail Analysis (New Functions)
*   **`fcn.0041150` (Downloader Logic):** This is a core execution path for downloading components. It sets up a custom User-Agent string (`Mozilla/5.0...`) to blend in with standard web traffic and utilizes `InternetOpenW`/`InternetOpenUrlW` to fetch files from the remote C2 infrastructure.
*   **`fcn.00413c60` (Protocol Handling):** This function acts as a packet processor or parser. It evaluates different hex values and internal flags to determine how to handle the next instruction in its task list.
*   **`fcn.0040e546` (System Resource Initialization):** This part of the code prepares various system handles (files, pipes, etc.) and validates their types. It is likely used during the initialization phase of a new module to establish communication channels or hidden file paths.

---

### Updated Summary Table of Indicators

| Category | Indicator/Technique | Impact / Threat Analysis |
| :--- | :--- | :--- |
| **Network** | `178.16.54.109` & `InternetOpenW` | C2 infrastructure for retrieving modular components and receiving commands. |
| **Execution** | `%temp%` / Dynamic Naming | Uses temporary directories to hide malicious executables from basic forensic scanning. |
| **Evasion** | Multi-Locale Support | Ensures the malware remains stable across different regions, increasing its utility as a wide-scale threat. |
| **Mechanism** | Heap Management (`HeapReAlloc`) | Allows for flexible memory usage depending on the size of the modules it downloads. |
| **Protocol** | State-based Parsing | Suggests a persistent backend where the malware can be "tasked" with different goals over time. |
| **Targeting** | `Slack`, `Zoom`, `Teams` | Targeted harvesting of credentials or internal data from corporate communication platforms. |

### Final Conclusion (Update)
The additional disassembly confirms that this is a **sophisticated, professional-grade trojan**. It is designed with high-level coding practices—such as robust error handling for string conversions and dynamic memory management—which are typical of high-end Advanced Persistent Threat (APT) tools. The malware’s ability to handle complex communication protocols and adapt its footprint based on the host's environment suggests it is meant for long-term, multi-stage operations within corporate networks.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided report to the relevant MITRE ATT&CK techniques and sub-techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The malware uses `InternetOpenW` and `InternetOpenUrlW` to download modular components (e.g., `lb1..lb19.exe`) from a remote C2 infrastructure. |
| **T1036** | Masquerading | The use of dynamic filename generation via `wsprintfW` in the `%temp%` directory is used to bypass static detection by security products. |
| **T1071** | Application Layer Protocol | The malware utilizes a custom User-Agent string and standard web functions to blend its communication with legitimate web traffic. |
| **T1102** | Web Service | The use of `InternetOpenW` indicates the leverage of web services as a primary channel for command and control and data retrieval. |
| **T1568** | Dynamic Resolution | The extensive use of `HeapAlloc` and `HeapReAlloc` to manage variable-sized payloads allows the malware to dynamically handle different modules in memory. |
| **T1539** | Steal Web Credentials | The targeting of communication platforms like Slack, Zoom, and Teams indicates an intent to harvest credentials or sensitive internal data. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   `178.16.54.109` (C2 Infrastructure)
*   `http://178.16.54.109/lkdomain.exe`
*   `http://178.16.54.109/lb1.exe` through `http://178.16.54.109/lb20.exe` (Modular payload download points)
*   `http://ip-api.com/json/` (Used for geographic profiling/reconnaissance)

**File paths / Registry keys**
*   *None identified.* (Note: While `%temp%` was mentioned in the analysis, no specific malicious file paths were provided in the strings).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None found in the provided text.*

**Other artifacts**
*   **User-Agent:** `Mozilla/5.0...` (Used to blend with standard web traffic during downloads).
*   **Targeted Applications:** 
    *   `slack.exe`
    *   `Teams.exe`
    *   `Zoom.exe`
    *   `sapgui.exe`
    *   `PBIDesktop.exe`
    *   `tableau.exe`
    *(These indicate the malware targets corporate communication and business intelligence tools for data harvesting).*
*   **C2 Behavior:** State-based parsing/protocol handling (suggests a sophisticated, multi-stage command structure).
*   **Module Indicator:** The sequential naming of payloads (`lb1` through `lb20`) suggests a modular toolkit.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://178.16.54.109/lb1.exe`
- `http://178.16.54.109/lb10.exe`
- `http://178.16.54.109/lb11.exe`
- `http://178.16.54.109/lb12.exe`
- `http://178.16.54.109/lb13.exe`
- `http://178.16.54.109/lb14.exe`
- `http://178.16.54.109/lb15.exe`
- `http://178.16.54.109/lb16.exe`
- `http://178.16.54.109/lb17.exe`
- `http://178.16.54.109/lb18.exe`
- `http://178.16.54.109/lb19.exe`
- `http://178.16.54.109/lb2.exe`
- `http://178.16.54.109/lb20.exe`
- `http://178.16.54.109/lb3.exe`
- `http://178.16.54.109/lb4.exe`
- `http://178.16.54.109/lb5.exe`
- `http://178.16.54.109/lb6.exe`
- `http://178.16.54.109/lb7.exe`
- `http://178.16.54.109/lb8.exe`
- `http://178.16.54.109/lb9.exe`
- `http://178.16.54.109/lkdomain.exe`
- `http://ip-api.com/json/`

**IP addresses:**
- `178.16.54.109`

---

## Malware Family Classification

1. **Malware family**: Custom / Modular Trojan
2. **Malware type**: Backdoor / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Modular Architecture:** The sample is not a standalone payload but a sophisticated "orchestrator" that downloads and manages a suite of components (e.g., `lb1` through `lb20`) using dynamic memory allocation (`HeapReAlloc`).
*   **Advanced C2 Communication:** It utilizes a state-based, multi-stage parsing protocol to interpret commands from the C2 server, indicating it is designed for long-term persistence and flexible task execution rather than one-time actions.
*   **Targeted Corporate Espionage:** The inclusion of specific strings targeting enterprise software (SAP, Tableau, Slack, Zoom) indicates a clear intent to harvest high-value corporate data and credentials from professional environments.
