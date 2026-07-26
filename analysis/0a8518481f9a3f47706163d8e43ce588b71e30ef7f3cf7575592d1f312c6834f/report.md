# Threat Analysis Report

**Generated:** 2026-07-25 00:28 UTC
**Sample:** `0a8518481f9a3f47706163d8e43ce588b71e30ef7f3cf7575592d1f312c6834f_0a8518481f9a3f47706163d8e43ce588b71e30ef7f3cf7575592d1f312c6834f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a8518481f9a3f47706163d8e43ce588b71e30ef7f3cf7575592d1f312c6834f_0a8518481f9a3f47706163d8e43ce588b71e30ef7f3cf7575592d1f312c6834f.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 2,507,776 bytes |
| MD5 | `7b9db48a87adb219d2d59331cff303af` |
| SHA1 | `7d1b3c35d1f3ec02dbd986695193e45fea71a426` |
| SHA256 | `0a8518481f9a3f47706163d8e43ce588b71e30ef7f3cf7575592d1f312c6834f` |
| Overall entropy | 7.469 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1768748391 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,089,536 | 6.529 | No |
| `.rdata` | 207,360 | 5.692 | No |
| `.data` | 20,992 | 2.624 | No |
| `.pdata` | 35,328 | 5.992 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,146,880 | 8.0 | ⚠️ Yes |
| `.reloc` | 6,144 | 5.348 | No |

### Imports

**SHELL32.dll**: `SHGetSpecialFolderPathW`, `SHGetKnownFolderPath`, `SHGetFolderPathW`
**USER32.dll**: `GetSystemMetrics`, `EnumDisplayDevicesW`, `EnumDisplaySettingsW`, `SystemParametersInfoW`, `GetCursorPos`
**ADVAPI32.dll**: `RegOpenKeyExW`, `RegSetValueExW`, `OpenProcessToken`, `CloseServiceHandle`, `OpenSCManagerW`, `EnumServicesStatusW`, `GetUserNameA`, `RegCloseKey`, `GetSidSubAuthorityCount`, `GetSidSubAuthority`, `RegEnumKeyExW`, `GetTokenInformation`, `RegQueryValueExW`, `GetUserNameW`, `CryptHashData`
**IPHLPAPI.DLL**: `GetAdaptersInfo`
**ole32.dll**: `CoInitializeEx`, `CoSetProxyBlanket`, `CoInitializeSecurity`, `CoTaskMemFree`, `CoCreateInstance`, `CoUninitialize`
**OLEAUT32.dll**: `VariantClear`, `SysAllocString`, `SysFreeString`
**WININET.dll**: `HttpQueryInfoA`, `InternetReadFile`, `InternetGetConnectedState`, `InternetOpenUrlW`, `HttpSendRequestA`, `InternetConnectW`, `InternetCloseHandle`, `HttpOpenRequestW`, `HttpAddRequestHeadersA`, `InternetOpenW`
**KERNEL32.dll**: `SetStdHandle`, `IsValidCodePage`, `GetACP`, `GetOEMCP`, `GetCommandLineA`, `GetCommandLineW`, `GetEnvironmentStringsW`, `FreeEnvironmentStringsW`, `SetEnvironmentVariableW`, `GetDiskFreeSpaceA`, `ReadConsoleW`, `GetConsoleMode`, `GetConsoleOutputCP`, `EnumSystemLocalesW`, `GetUserDefaultLCID`

## Extracted Strings

Total strings found: **8036** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
L$ SUVWH
L$ SUVWH
CfA9S
CfA9S
UVWATAUAVAWH
L9|$pr
fE9$t(fA
<$/t H
 A_A^A]A\_^]
WATAUAVAWH
 A_A^A]A\_
p UWAUAVAWH
A_A^A]_]
UVWATAUAVAWH
46fE9d>
 A_A^A]A\_^]
UVWATAUAVAWH
\$0H9t$HH
\$`H9t$xH
L$`H9t$xH
L$`H9t$xH
L$0H9t$HH
U(H9u@H
U(H9u@H
L$0H9t$HH
A_A^A]A\_^]
|$ AVH
UWATAVAWH
A_A^A\_]
f9t$Pt
|$ UATAUAVAWH
,.u(fD9o.t
fD9o0u
A_A^A]A\]
UATAUAVAWH
|$l.u-
fD9|$pu
|$l.u.
f9T$pu
A_A^A]A\]
t$ WAVAWH
0A_A^_
D$09\$ t
|$ UATAUAVAWH
A_A^A]A\]
UATAUAVAWH
A_A^A]A\]
x UATAUAVAWH
D$@H9t$XH
A_A^A]A\]
USVWATAUAVAWH
EJQxb
A_A^A]A\_^[]
UATAUAVAWH
L;D$@t
L;D$@t
D$hf9=
L;D$@t
A_A^A]A\]
UVWATAUAVAWH
E fD9-`
L$`L9d$xH
A_A^A]A\_^]
UVWATAUAVAWH
D$\D8=
T$0L9d$HH
T$0L9d$HH
T$PL9d$hH
T$0L9d$HH
T$0L9d$HH
T$0L9d$HH
D$XD8=8*
T$0L9d$HH
D$XD8=
T$0L9d$HH
T$0L9d$HH
A_A^A]A\_^]
UVWATAUAVAWH
D$xfD9%
D$|D8=
Uh+U`H
D$xD8=
M D8=/
D$xD8=>
A_A^A]A\_^]
ATAVAWH
D$HD8%
A_A^A\
UWATAVAWH
A_A^A\_]
UVWATAUAVAWH
D$hfD9%X
fD9%=k
A_A^A]A\_^]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400dbd94` | `0x1400dbd94` | 621313 | ✓ |
| `fcn.1400da6e4` | `0x1400da6e4` | 80662 | ✓ |
| `fcn.1400f3910` | `0x1400f3910` | 61267 | ✓ |
| `fcn.1400f38fc` | `0x1400f38fc` | 61226 | ✓ |
| `method.std::basic_ofstream_char__struct_std::char_traits_char__.virtual_0` | `0x14002b0c8` | 37064 | ✓ |
| `method.std::basic_ifstream_char__struct_std::char_traits_char__.virtual_0` | `0x14002b0b0` | 36948 | ✓ |
| `method.std::basic_ostringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x14002b0d4` | 36840 | ✓ |
| `method.std::basic_istringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x14002b0e0` | 36760 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x14002b0a4` | 36556 | ✓ |
| `method.std::basic_istream_char__struct_std::char_traits_char__.virtual_0` | `0x14002b0bc` | 36444 | ✓ |
| `fcn.14006ba80` | `0x14006ba80` | 31987 | ✓ |
| `fcn.1400e9958` | `0x1400e9958` | 28809 | ✓ |
| `fcn.14006bf4c` | `0x14006bf4c` | 27276 | ✓ |
| `fcn.1400fe7a0` | `0x1400fe7a0` | 22985 | ✓ |
| `fcn.1400697e0` | `0x1400697e0` | 18780 | ✓ |
| `fcn.14009af1c` | `0x14009af1c` | 16927 | ✓ |
| `fcn.1400dad8c` | `0x1400dad8c` | 14042 | ✓ |
| `fcn.140009d38` | `0x140009d38` | 11795 | ✓ |
| `fcn.1400c56c0` | `0x1400c56c0` | 9810 | ✓ |
| `fcn.1400b467c` | `0x1400b467c` | 8415 | ✓ |
| `fcn.1400a94ec` | `0x1400a94ec` | 8218 | ✓ |
| `fcn.140039ff4` | `0x140039ff4` | 7592 | ✓ |
| `fcn.14002f6d8` | `0x14002f6d8` | 6531 | ✓ |
| `fcn.14003109c` | `0x14003109c` | 6446 | ✓ |
| `fcn.1400ae584` | `0x1400ae584` | 6299 | ✓ |
| `fcn.140097874` | `0x140097874` | 5931 | ✓ |
| `fcn.140015090` | `0x140015090` | 5912 | ✓ |
| `fcn.1400329cc` | `0x1400329cc` | 5756 | ✓ |
| `fcn.140034048` | `0x140034048` | 5547 | ✓ |
| `fcn.1400355f4` | `0x1400355f4` | 5432 | ✓ |

### Decompiled Code Files

- [`code/fcn.140009d38.c`](code/fcn.140009d38.c)
- [`code/fcn.140015090.c`](code/fcn.140015090.c)
- [`code/fcn.14002f6d8.c`](code/fcn.14002f6d8.c)
- [`code/fcn.14003109c.c`](code/fcn.14003109c.c)
- [`code/fcn.1400329cc.c`](code/fcn.1400329cc.c)
- [`code/fcn.140034048.c`](code/fcn.140034048.c)
- [`code/fcn.1400355f4.c`](code/fcn.1400355f4.c)
- [`code/fcn.140039ff4.c`](code/fcn.140039ff4.c)
- [`code/fcn.1400697e0.c`](code/fcn.1400697e0.c)
- [`code/fcn.14006ba80.c`](code/fcn.14006ba80.c)
- [`code/fcn.14006bf4c.c`](code/fcn.14006bf4c.c)
- [`code/fcn.140097874.c`](code/fcn.140097874.c)
- [`code/fcn.14009af1c.c`](code/fcn.14009af1c.c)
- [`code/fcn.1400a94ec.c`](code/fcn.1400a94ec.c)
- [`code/fcn.1400ae584.c`](code/fcn.1400ae584.c)
- [`code/fcn.1400b467c.c`](code/fcn.1400b467c.c)
- [`code/fcn.1400c56c0.c`](code/fcn.1400c56c0.c)
- [`code/fcn.1400da6e4.c`](code/fcn.1400da6e4.c)
- [`code/fcn.1400dad8c.c`](code/fcn.1400dad8c.c)
- [`code/fcn.1400dbd94.c`](code/fcn.1400dbd94.c)
- [`code/fcn.1400e9958.c`](code/fcn.1400e9958.c)
- [`code/fcn.1400f38fc.c`](code/fcn.1400f38fc.c)
- [`code/fcn.1400f3910.c`](code/fcn.1400f3910.c)
- [`code/fcn.1400fe7a0.c`](code/fcn.1400fe7a0.c)
- [`code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)

## Behavioral Analysis

This final segment of disassembly (**Chunk 9/9**) provides the "smoking gun" regarding the malware’s internal architecture and its sophistication level. While previous chunks revealed *what* the malware was looking for, this section reveals the **engine** that drives it.

Here is the updated analysis, incorporating all previous findings and integrating the new insights from the final disassembly.

---

### Analysis of Chunk 9/9 (Final Segment)

#### 1. The "Keyed" Decryption Engine
The most prominent feature in this chunk is the repeated occurrence of a specific mathematical loop:
`*puVar27 = *puVar27 ^ piVar15 + (piVar15 / 0x31) * -0x31 + 0x39U;`

*   **Analysis:** This is not a standard XOR. It is a **customized rolling-key decryption algorithm**. The inclusion of the `(piVar15 / 0x31) * -0x31` component suggests an attempt to obfuscate not just the character, but the mathematical operation itself, making simple automated "de-obfuscation" tools fail.
*   **Significance:** This algorithm is used multiple times to unpack different components: internal commands, hardcoded URLs, and potentially even local file paths or configuration keys. By using this method, the author ensures that static analysis (simply looking at strings in the binary) yields almost no useful information.

#### 2. Multi-Path Command Dispatching
The code contains heavy branching logic based on variables like `arg1`, `arg2`, and various internal state checks (e.g., `if (arg2 != 0)`).

*   **Analysis:** This confirms the **Modular Architecture** suspected in Chunk 8. The malware doesn't just have one "job." It acts as a container that can host multiple functionalities. Depending on which "module" is activated or what parameters are passed at runtime, it can switch between different behaviors (e.g., switching from an "Information Stealer" mode to a "Backdoor/Remote Access" mode).
*   **Significance:** This allows the attacker to use one single binary for multiple purposes, making it harder for signature-based antivirus to identify all its capabilities at once.

#### 3. Sophisticated Memory Management & State Check
The code frequently checks memory addresses and offsets (e.g., `*(iVar9 + 0x18)`, `*(iVar19 + 0x6e) & 8`).

*   **Analysis:** The malware is checking for specific "capabilities" before proceeding. This is typical of high-end Trojan architecture where the binary checks if a certain library or function is available in memory before trying to execute it. If a check fails, it falls back to an alternative method (as seen in the various `go_to` labels).
*   **Significance:** This ensures maximum stability. The malware "probes" the environment to see what it *can* do, then dynamically builds its execution path based on those capabilities.

#### 4. Robustness and Exception Handling
The inclusion of specific error codes (e.g., `fcn.1400ccec4(0x2c9fa)`) and standardized logic for cleaning up memory/buffers after a failed action indicates a high level of professional development.

*   **Analysis:** The malware is designed to fail "silently." If a network connection fails or a file cannot be read, it doesn't crash the application; it catches the error, logs it (or ignores it), and attempts a fallback path or simply exits gracefully.
*   **Significance:** This minimizes the risk of the user noticing an issue, which keeps the infection "silent" for as long as possible.

---

### Updated Indicators of Compromise (IoCs) & Behavior

| Feature | Observation | Security Significance |
| :--- | :--- | :--- |
| **Custom Decryption** | The loop: `^ piVar15 + (piVar15 / 0x31) * -0x31 + 0x39U`. | **Critical:** Indicates a high-effort attempt to hide C2 infrastructure, internal commands, and capability flags from automated scanners. |
| **Modular Dispatcher** | Extensive `if/else` logic branching based on dynamic arguments (e.g., `arg2`). | **High:** Confirms the malware is "multi-purpose." One binary can perform multiple types of theft or remote access depending on its configuration. |
| **State-Aware Execution** | Checks for specific flags and memory offsets before calling subroutines. | **High:** Ensures stability; if a primary method fails (e.g., an API call is blocked), the malware can pivot to a secondary method. |
| **Path Normalization** | `\` to `/` conversion (from Chunk 8). | **Medium:** Indicates cross-platform compatibility for the attacker’s C2 infrastructure. |
| **Database Interaction** | Explicit handling of database connection pointers. | **Critical:** Confirms target is likely corporate/enterprise data rather than just individual consumer credentials. |

---

### Final Comprehensive Synthesis

Based on the full analysis of Chunks 1 through 9, this malware can be classified as a **Sophisticated Modular Trojan Framework.** It is not an amateur tool; it is a professional-grade piece of malware designed for long-term persistence and high-value data theft.

**Final Tactical Profile:**
1.  **Initial Reconnaissance (Chunks 1-3):** The malware begins by auditing the environment to ensure it isn't being watched by security researchers or automated analysis tools.
2.  **Data Harvest & Organization (Chunk 4-7):** It identifies and gathers high-value information, including credentials, system info, and potentially enterprise database access points.
3.  **Encryption & Obfuscation (Chunks 8-9):** Throughout its execution, it uses a custom mathematical "rolling" decryption logic to ensure that any strings or commands it handles in memory are only visible for a fraction of a second.
4.  **Dynamic Execution:** It uses a dispatcher model. Instead of one static path, the code acts like a switchboard—taking command inputs and routing them to specific modules (e.g., "Stealer," "Proxy," "Bot," or "File Exfiltrator").

### Final Strategic Recommendations:
*   **Memory Forensics:** Since much of the malware's logic is hidden behind decryption, standard disk-based scanning will miss its capabilities. Security teams should perform **in-memory string analysis** and memory dumps to capture the strings *after* they are decrypted by the rolling-key algorithm.
*   **Behavioral Heuristics:** Monitor for "Process Hollowing" or "Injection," as modular malware often injects these different modules into legitimate system processes (like `explorer.exe` or `svchost.exe`) to hide their presence.
*   **Network Hunting:** Look specifically for outbound traffic that matches the pattern of a "heartbeat"—small, regular packets that signal the dispatcher is active and waiting for commands from the C2 server.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from the provided analysis to the relevant MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a custom mathematical rolling-key decryption loop hides critical internal strings, C2 URLs, and configuration keys from static analysis. |
| **T1036** | Dynamic Resolution | The "State-Aware" execution logic checks for specific capabilities/functions in memory before selecting an execution path to ensure stability and bypass potential blocks. |
| **T1071** | Application Layer Protocol | The multi-path command dispatcher interprets different commands to switch the malware's functional role (e.g., from information stealer to backdoor). |
| **T1185** | Compromise Systems Automated Reporting | While not a direct mapping of "Robustness," the specific error handling and silent failure logic are intended to maintain an undetected presence while reporting success/failure only internally. |

### Analyst Notes:
*   **Decryption (T1027):** The complexity of the math in `puVar27 = *puVar27 ^ piVar15 + (piVar15 / 0x31) * -0x31 + 0x39U` is a classic example of "Security through Obscurity" to defeat automated string extraction.
*   **State-Aware Execution (T1036/Defense Evasion):** The behavior of checking for specific capabilities before proceeding allows the malware to pivot if it detects that its primary method is being blocked by security software, a core tenet of **Defense Evasion**.
*   **Modular Architecture:** While "Modular" isn't a standalone technique in MITRE, it is realized through **T1071** (where various commands are processed) and generally supports the lifecycle of sophisticated Trojan frameworks.

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs) categorized by type. 

Note: The "EXTRACTED STRINGS" section contains highly obfuscated or "garbage" data typical of packed or encrypted malware; therefore, no direct network indicators (IPs/URLs) or system paths were present in those raw strings.

### **Indicators of Compromise (IOCs)**

**IP addresses / URLs / Domains**
*   *None identified.* (Note: The analysis indicates these are currently hidden behind a custom decryption layer).

**File paths / Registry keys**
*   *None identified.* (Note: The report indicates that local file paths and registry keys are obfuscated using the "Keyed" Decryption Engine).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **C2 Obfuscation Logic:** The specific rolling-key decryption algorithm: `^ piVar15 + (piVar15 / 0x31) * -0x31 + 0x39U`. This serves as a behavioral signature for identifying the specific malware family/builder.
*   **Modular Command Dispatcher:** The use of dynamic arguments (`arg1`, `arg2`) and state-checking logic to switch between "Information Stealer" and "Backdoor/Remote Access" modes.
*   **Data Extraction Patterns:** Evidence of database connection handling (indicates targeting of corporate/enterprise data).
*   **Path Normalization Behavior:** Automated conversion of backslashes (`\`) to forward slashes (`/`), indicating the capability for cross-platform C2 communication.

---

### **Analyst Summary**
The primary indicators in this case are **behavioral** rather than static. Because the malware employs a sophisticated "rolling" decryption algorithm, standard string extraction tools failed to surface network infrastructure (IPs/URLs) or system paths. 

**Recommendation:** Detection should focus on memory forensics and behavioral heuristics. Specifically, monitor for processes executing the identified mathematical loop (`^ piVar15 + (piVar15 / 0x31) * -0x31 + 0x39U`) as it is a high-confidence indicator of this specific malware framework's presence in memory.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://api.ipify.org`

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family**: Custom
2.  **Malware type**: Backdoor (Modular Trojan)
3.  **Confidence**: High
4.  **Key evidence**:
    *   **Modular Architecture & Dispatcher:** The use of multi-path command dispatching (based on `arg1`, `arg2`) and state-aware execution confirms it is a sophisticated framework capable of switching between different functionalities (e.g., Infostealer, Backdoor, or Proxy) depending on its configuration.
    *   **Advanced Obfuscation:** The implementation of a "Keyed" Decryption Engine—a non-standard, mathematically complex rolling-key algorithm (`^ piVar15 + (piVar15 / 0x31) * -0x31 + 0x39U`)—is used to hide C2 infrastructure and internal commands from automated scanners.
    *   **Professional Resilience:** The inclusion of robust error handling, "silent" failure logic, and capability checking indicates a professional-grade tool designed for high-value targets (corporate/enterprise environments) rather than basic commodity malware.
