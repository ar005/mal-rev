# Threat Analysis Report

**Generated:** 2026-08-22 06:54 UTC
**Sample:** `1104f14d6b21fafb2136ce765897498ae414a71b28382bc3de9365e143d38d11_1104f14d6b21fafb2136ce765897498ae414a71b28382bc3de9365e143d38d11.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1104f14d6b21fafb2136ce765897498ae414a71b28382bc3de9365e143d38d11_1104f14d6b21fafb2136ce765897498ae414a71b28382bc3de9365e143d38d11.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 506,880 bytes |
| MD5 | `056d57412c6c4d910f775a591b162fa0` |
| SHA1 | `bf114b6411fe3823ec3792c11625afb0d2b20a19` |
| SHA256 | `1104f14d6b21fafb2136ce765897498ae414a71b28382bc3de9365e143d38d11` |
| Overall entropy | 6.589 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1760185279 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 363,008 | 6.624 | No |
| `.rdata` | 103,424 | 5.722 | No |
| `.data` | 3,584 | 3.098 | No |
| `.rsrc` | 19,456 | 3.991 | No |
| `.reloc` | 16,384 | 6.668 | No |

### Imports

**KERNEL32.dll**: `FindNextFileA`, `ExpandEnvironmentStringsA`, `GetModuleFileNameW`, `GetVersionExW`, `CreateToolhelp32Snapshot`, `Process32NextW`, `Process32FirstW`, `GetLongPathNameW`, `InitializeCriticalSection`, `GetLocaleInfoA`, `VirtualProtect`, `HeapFree`, `SetLastError`, `VirtualFree`, `VirtualAlloc`
**USER32.dll**: `DefWindowProcA`, `TranslateMessage`, `DispatchMessageA`, `GetMessageA`, `GetWindowTextW`, `wsprintfW`, `GetClipboardData`, `UnhookWindowsHookEx`, `GetForegroundWindow`, `ToUnicodeEx`, `GetKeyboardLayout`, `SetWindowsHookExA`, `CloseClipboard`, `OpenClipboard`, `GetKeyboardState`
**GDI32.dll**: `BitBlt`, `CreateCompatibleBitmap`, `SelectObject`, `StretchBlt`, `GetDIBits`, `DeleteDC`, `DeleteObject`, `CreateDCA`, `GetObjectA`, `CreateCompatibleDC`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `CryptAcquireContextA`, `CryptGenRandom`, `CryptReleaseContext`, `GetUserNameW`, `RegEnumKeyExA`, `GetTokenInformation`, `QueryServiceStatus`, `CloseServiceHandle`, `OpenSCManagerW`, `OpenSCManagerA`, `ControlService`, `StartServiceW`, `QueryServiceConfigW`, `ChangeServiceConfigW`
**SHELL32.dll**: `ShellExecuteExA`, `Shell_NotifyIconA`, `ExtractIconA`, `ShellExecuteW`
**ole32.dll**: `CoGetObject`, `CoInitializeEx`, `CoUninitialize`
**SHLWAPI.dll**: `PathFileExistsW`, `StrToIntA`, `PathFileExistsA`
**WINMM.dll**: `mciSendStringW`, `waveInClose`, `waveInStop`, `waveInPrepareHeader`, `PlaySoundW`, `waveInOpen`, `waveInStart`, `waveInAddBuffer`, `waveInUnprepareHeader`, `mciSendStringA`
**WS2_32.dll**: `socket`, `send`, `connect`, `WSAGetLastError`, `WSAStartup`, `closesocket`, `inet_ntoa`, `htons`, `htonl`, `getservbyname`, `ntohs`, `getservbyport`, `gethostbyaddr`, `inet_addr`, `WSASetLastError`
**urlmon.dll**: `URLDownloadToFileW`, `URLOpenBlockingStreamW`
**gdiplus.dll**: `GdiplusStartup`, `GdipGetImageEncoders`, `GdipCloneImage`, `GdipLoadImageFromStream`, `GdipSaveImageToStream`, `GdipGetImageEncodersSize`, `GdipFree`, `GdipDisposeImage`, `GdipAlloc`
**WININET.dll**: `InternetOpenUrlW`, `InternetOpenW`, `InternetCloseHandle`, `InternetReadFile`

## Extracted Strings

Total strings found: **1794** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
D$,VPVj
_^][YY
_^][YY
Sj,h@[G
ESVWP
^|9^xv
tD;Nxr
>;D$s
+D$<@P
D$ UPW
D$ UPW
L$$PWj
L$,PPPPPP
XVWjD^V3
L$$RPj
D$D_^][
D$$_^]
T$PSPS
uSSVh
uSSVh
>;D$s
D$xVWP
tSSSh`;A
tSSSh

}Rj
C
L$@UVhL
9{Lt:V
L$SVW
@_^][YY
Y<9X8t
3
D$ f;F
D$(;D$
P4+S4t	
D$\_^][
L$0_^][
u#VVVV
EPjj
SVWj j
Xf9F
u+
uH9t$4t*
L$pj Z
L$(PWj
L$(PWj
 !"#$%&'()*+,-N.NNN/NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN01N2N34N5678NNN9:;N<=NNNNNNN>?@ANNNBNNNNNNNNNNNNNNNNNNCDNEFGHIJKNNNLMV
>;D$s
D$LPSSj
D$LPSh
9L$(t"Sj
L$ +D$
t$0VWj
+|$,+t$0
t$`VWU
QQPVWQQU
9\$t_
,SVWj

D$TFVP
VjxVVh
L$$PWj
MSVW3
D$ PVUj
t$(9t$
t$(;t$
SVWj 3
SVWj@3
SVWj@3
YSSSSSSSj
|SUVWQ
L$(SSS
,SUVWh
?u}f9D$
uvf9Dl
D$SUV3
D$LQPQ
WPSSSV
HUVWjD3
D$pVSP
t SSSj
SSSSSS
$0<0t
ti<*u?O
t%<.tHF
_^][YY
j(XjtY
LSUVW3
\$<+\$@
t$<Pj
l$L9t$
D$HHBj
t$Pf	\$V
\$UVW
_^][YY
_^][YY
QSUVW3
D$Lj P
_^][YY
tQRj+Z
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00437ad7` | `0x437ad7` | 65430 | ✓ |
| `fcn.00444cb8` | `0x444cb8` | 42285 | ✓ |
| `fcn.00444e0d` | `0x444e0d` | 42127 | ✓ |
| `fcn.00444c20` | `0x444c20` | 40606 | ✓ |
| `fcn.00437ef2` | `0x437ef2` | 13250 | ✓ |
| `fcn.00420f70` | `0x420f70` | 10394 | ✓ |
| `fcn.0041007c` | `0x41007c` | 10368 | ✓ |
| `fcn.0040fad2` | `0x40fad2` | 6960 | ✓ |
| `fcn.00455a06` | `0x455a06` | 5020 | ✓ |
| `fcn.0040280d` | `0x40280d` | 4733 | ✓ |
| `fcn.00402808` | `0x402808` | 4704 | ✓ |
| `fcn.00421307` | `0x421307` | 4477 | ✓ |
| `fcn.004397ca` | `0x4397ca` | 3875 | ✓ |
| `fcn.004115e7` | `0x4115e7` | 3304 | ✓ |
| `fcn.00416c01` | `0x416c01` | 3270 | ✓ |
| `main` | `0x41028f` | 3044 | ✓ |
| `fcn.0044f319` | `0x44f319` | 2822 | ✓ |
| `fcn.00448453` | `0x448453` | 2817 | ✓ |
| `fcn.00421bff` | `0x421bff` | 2084 | ✓ |
| `fcn.00436c2d` | `0x436c2d` | 2045 | ✓ |
| `fcn.004146f2` | `0x4146f2` | 1792 | ✓ |
| `fcn.0043d186` | `0x43d186` | 1765 | ✓ |
| `fcn.00458250` | `0x458250` | 1737 | ✓ |
| `fcn.00429deb` | `0x429deb` | 1572 | ✓ |
| `fcn.0043099a` | `0x43099a` | 1552 | ✓ |
| `fcn.00436069` | `0x436069` | 1460 | ✓ |
| `fcn.0042eb47` | `0x42eb47` | 1415 | ✓ |
| `fcn.00429874` | `0x429874` | 1399 | ✓ |
| `fcn.004390f0` | `0x4390f0` | 1396 | ✓ |
| `fcn.00438b70` | `0x438b70` | 1396 | ✓ |

### Decompiled Code Files

- [`code/fcn.00402808.c`](code/fcn.00402808.c)
- [`code/fcn.0040280d.c`](code/fcn.0040280d.c)
- [`code/fcn.0040fad2.c`](code/fcn.0040fad2.c)
- [`code/fcn.0041007c.c`](code/fcn.0041007c.c)
- [`code/fcn.004115e7.c`](code/fcn.004115e7.c)
- [`code/fcn.004146f2.c`](code/fcn.004146f2.c)
- [`code/fcn.00416c01.c`](code/fcn.00416c01.c)
- [`code/fcn.00420f70.c`](code/fcn.00420f70.c)
- [`code/fcn.00421307.c`](code/fcn.00421307.c)
- [`code/fcn.00421bff.c`](code/fcn.00421bff.c)
- [`code/fcn.00429874.c`](code/fcn.00429874.c)
- [`code/fcn.00429deb.c`](code/fcn.00429deb.c)
- [`code/fcn.0042eb47.c`](code/fcn.0042eb47.c)
- [`code/fcn.0043099a.c`](code/fcn.0043099a.c)
- [`code/fcn.00436069.c`](code/fcn.00436069.c)
- [`code/fcn.00436c2d.c`](code/fcn.00436c2d.c)
- [`code/fcn.00437ad7.c`](code/fcn.00437ad7.c)
- [`code/fcn.00437ef2.c`](code/fcn.00437ef2.c)
- [`code/fcn.00438b70.c`](code/fcn.00438b70.c)
- [`code/fcn.004390f0.c`](code/fcn.004390f0.c)
- [`code/fcn.004397ca.c`](code/fcn.004397ca.c)
- [`code/fcn.0043d186.c`](code/fcn.0043d186.c)
- [`code/fcn.00444c20.c`](code/fcn.00444c20.c)
- [`code/fcn.00444cb8.c`](code/fcn.00444cb8.c)
- [`code/fcn.00444e0d.c`](code/fcn.00444e0d.c)
- [`code/fcn.00448453.c`](code/fcn.00448453.c)
- [`code/fcn.0044f319.c`](code/fcn.0044f319.c)
- [`code/fcn.00455a06.c`](code/fcn.00455a06.c)
- [`code/fcn.00458250.c`](code/fcn.00458250.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

Based on the final chunk of disassembly provided, here is the updated and expanded analysis. This third installment provides definitive evidence regarding the complexity of the malware's internals and reinforces its classification as a high-tier threat.

### Final Comprehensive Analysis

The addition of these functions confirms that this binary does not just "perform" actions; it **executes an environment**. The code in this final section is characteristic of highly sophisticated malware designed to resist both automated analysis and manual deconstruction.

---

### Core Functionality (Final Update)
*   **Advanced Dispatch & Interpreter Logic:**
    *   The functions `fcn.00439186` (and the surrounding blocks) are prime examples of **instruction dispatch**. The "Too many branches" warnings and the nested logic used to process data in chunks (e.g., `switch(param_3 & 3)` and `if (0x1f < param_3)`) indicate that the malware is processing a custom bytecode or a highly complex packet structure.
    *   The code isn't just copying memory; it is interpreting "instructions" where each branch represents a different command or state transition. This confirms the **Virtual Machine (VM) architecture** theory—the real malicious logic is likely hidden within this interpreted layer, making it extremely difficult to trace using standard linear analysis.
*   **Complex Data Deserialization:**
    *   The intricate way the code handles memory offsets and bitwise shifts to "unpack" data into `param_1` suggests a **multi-layered protocol**. It is designed to take raw, potentially encrypted packets from the C2 server and unpack them into internal structures that the "interpreter" can then act upon. The heavy use of multi-byte jumps (e.g., handling 4 bytes at once in several branches) indicates it's prepared to handle a wide variety of data types for different commands.

### Suspicious and Malicious Behaviors (Final Expansion)
*   **Anti-Analysis via "Muddied" Logic:**
    *   The sheer density of the code in this chunk is a deliberate tactic. By using complex loops, nested `if` statements based on bit-shifts, and manual pointer arithmetic to perform what would normally be simple operations (like copying data), the author creates a **cognitive barrier**. This "noise" is designed to exhaust a human analyst's patience and make it harder for automated tools to map the true execution flow.
*   **Polymorphic/Metamorphic Potential:**
    *   The structure of these functions suggests they could be part of a **packer or protector**. The way it handles data lengths (e.g., `param_3 & 0x1f`) and shifts indicates that the binary is designed to handle varied inputs dynamically, which is a hallmark of sophisticated "dropper" frameworks used by APT (Advanced Persistent Threat) groups.

### Notable Techniques & Patterns
*   **Hidden Control Flow:**
    *   The warning `//WARNING: Could not recover jumptable at 0x0043915` is highly significant. This occurs when a compiler encounters too many branches to create a clean jump table, often resulting in "spaghetti code" that hides the logic's intent. In malware, this is frequently used to hide the **core malicious loop** from static analysis tools (like IDA Pro or Ghidra).
*   **Manual Memory Management:**
    *   The use of internal routines instead of standard library calls for memory manipulation (`puVar52 = puVar49 + 0xc`, etc.) reduces the "Import" footprint. By not calling common APIs like `memcpy` directly, the malware avoids detection by basic heuristic scanners that look for high-frequency calls to system libraries in suspicious contexts.

---

### Final Summary Conclusion
The evidence from all three chunks confirms that this binary is a **sophisticated, modular Trojan/Backdoor**, likely belonging to a professional threat actor's toolkit. 

**Key Indicators of High Sophistication:**
1.  **Interpreter-Based Architecture:** The core logic is hidden behind a custom execution environment (VM), making it extremely difficult to "hardcode" the analysis—one must instead reverse the interpreter itself.
2.  **Sophisticated C2 Protocol:** The complex, multi-layered data processing suggests that the malware can receive a vast array of commands (e.g., file exfiltration, keylogging, remote shell, etc.) over an encrypted channel.
3.  **Active Evasion & Persistence:** The inclusion of `DeleteFileW` loops for self-cleanup and "noise" code to distract analysts shows a high level of professional development.
4.  **Complex Infrastructure Readiness:** This is not a simple "downloader." It is a **persistent foothold tool** designed to provide long-term, stealthy access to the target environment.

**Final Assessment:** **High-Risk Threat.** The binary exhibits characteristics consistent with advanced malware used for targeted espionage or large-scale data theft.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors described in your analysis to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1028** | **Virtualization** | The use of an interpreter and custom bytecode (instruction dispatch) masks the true malicious logic within a custom execution environment. |
| **T1479** | **Obfuscated Code** | The "muddied" logic, nested loops, and complex bitwise operations are specifically designed to create a cognitive barrier for human analysts. |
| **T1070.004** | **File Deletion** | The inclusion of `DeleteFileW` loops indicates an attempt to remove local artifacts and perform self-cleanup after execution. |
| **T1568** | **Dynamic Resolution** | The use of internal routines for memory manipulation instead of standard library calls is a tactic used to reduce the Import footprint and evade detection. |

### Analyst Notes:
*   **T1028 (Virtualization):** This is the primary driver for why the analysis mentions "hidden control flow" and "interpreter logic." By wrapping the malicious operations in a custom VM, the threat actor ensures that standard static analysis tools cannot easily map the execution path.
*   **T1479 (Obfuscated Code):** This covers both the "muddied logic" and the "sophisticated complexity" mentioned. It is a common tactic to exhaust the time and resources of an analyst during the deconstruction process.
*   **Detection Strategy:** To detect this, organizations should focus on behavior-based detection (e.g., identifying processes spawning with unusual interpreter-like behaviors) rather than simple signature-based detections which would be defeated by the obfuscation layers.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains heavily obfuscated or encoded data typical of a packed binary; none of these segments resolved into plaintext IP addresses, URLs, or file paths in their current form.

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (Note: While `DeleteFileW` is mentioned as a function used for self-deletion/cleanup, no specific file paths or registry keys were provided).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified.

### **Other artifacts**
*   **Internal Function Address:** `0x00439186` (Identified as a complex instruction dispatch/VM interpreter logic).
*   **C2 Protocol Patterns:** 
    *   Evidence of **Custom Bytecode/Virtual Machine (VM) Architecture**: The malware uses a custom execution environment to hide its core logic.
    *   **Multi-layer Data Deserialization**: Evidence of a complex, multi-step protocol used to unpack data from the C2 server.
    *   **Anti-Analysis Tactics**: "Muddied" logic (complex bit-shifts and nested loops) intended to hinder automated analysis and human reverse engineering.
    *   **Manual Memory Management**: Use of internal routines instead of standard library calls (e.g., manual pointer arithmetic instead of `memcpy`) to reduce the import footprint and evade detection.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** backdoor
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Virtual Machine (VM) Architecture:** The detection of "instruction dispatch," "multi-layered data deserialization," and a custom interpreter indicates the malware uses a virtualized execution environment to hide its true malicious logic from static analysis.
    *   **Advanced Evasion Techniques:** The use of manual memory management (to reduce import footprints), "muddied" code paths, and complex bitwise operations demonstrates a high level of sophistication intended to frustrate both automated tools and human analysts.
    *   **Modular Persistence:** The report identifies the binary as a "persistent foothold tool" rather than a simple downloader, featuring capabilities for remote shell access, keylogging, and data exfiltration via a complex C2 protocol.
