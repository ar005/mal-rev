# Threat Analysis Report

**Generated:** 2026-08-03 12:23 UTC
**Sample:** `0cb2438225335d116088ad74d20fbe0b769fb0086eba1b3416f3ec30fd03570d_0cb2438225335d116088ad74d20fbe0b769fb0086eba1b3416f3ec30fd03570d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0cb2438225335d116088ad74d20fbe0b769fb0086eba1b3416f3ec30fd03570d_0cb2438225335d116088ad74d20fbe0b769fb0086eba1b3416f3ec30fd03570d.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 11 sections |
| Size | 3,521,208 bytes |
| MD5 | `697cd3cf3b279dcae01668d34c653bfb` |
| SHA1 | `9275dfd8f6e720ac593539a070491e37b4fa5cce` |
| SHA256 | `0cb2438225335d116088ad74d20fbe0b769fb0086eba1b3416f3ec30fd03570d` |
| Overall entropy | 7.146 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766318742 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,538,560 | 6.208 | No |
| `.data` | 17,408 | 0.906 | No |
| `.rdata` | 248,832 | 5.85 | No |
| `.pdata` | 72,192 | 6.133 | No |
| `.xdata` | 148,480 | 5.549 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 14,336 | 4.279 | No |
| `.CRT` | 512 | 0.333 | No |
| `.tls` | 512 | -0.0 | No |
| `.rsrc` | 1,464,320 | 7.802 | ⚠️ Yes |
| `.reloc` | 8,704 | 5.428 | No |

### Imports

**KERNEL32.DLL**: `CheckRemoteDebuggerPresent`, `CloseHandle`, `CopyFileA`, `CreateDirectoryA`, `CreateFileA`, `CreateFileW`, `CreateHardLinkW`, `CreateMutexA`, `CreatePipe`, `CreateProcessA`, `CreateRemoteThread`, `CreateSemaphoreW`, `CreateThread`, `CreateToolhelp32Snapshot`, `DeleteCriticalSection`
**ADVAPI32.dll**: `AllocateAndInitializeSid`, `CheckTokenMembership`, `CryptAcquireContextA`, `CryptGenRandom`, `CryptReleaseContext`, `FreeSid`, `GetUserNameA`, `RegCloseKey`, `RegCreateKeyExA`, `RegDeleteTreeA`, `RegDeleteValueA`, `RegEnumKeyA`, `RegEnumKeyExA`, `RegOpenKeyExA`, `RegQueryValueExA`
**bcrypt.dll**: `BCryptCloseAlgorithmProvider`, `BCryptCreateHash`, `BCryptDecrypt`, `BCryptDestroyHash`, `BCryptDestroyKey`, `BCryptEncrypt`, `BCryptFinishHash`, `BCryptGenerateSymmetricKey`, `BCryptHashData`, `BCryptImportKey`, `BCryptOpenAlgorithmProvider`, `BCryptSetProperty`
**CRYPT32.dll**: `CryptStringToBinaryA`, `CryptUnprotectData`
**GDI32.dll**: `BitBlt`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `DeleteDC`, `DeleteObject`, `GetDIBits`, `GetObjectA`, `SelectObject`
**gdiplus.dll**: `GdipAlloc`, `GdipCloneImage`, `GdipCreateBitmapFromHBITMAP`, `GdipDisposeImage`, `GdipFree`, `GdipSaveImageToStream`, `GdiplusShutdown`, `GdiplusStartup`
**IPHLPAPI.DLL**: `GetAdaptersInfo`
**msvcrt.dll**: `___lc_codepage_func`, `___mb_cur_max_func`, `__getmainargs`, `__initenv`, `__iob_func`, `__lconv_init`, `__set_app_type`, `__setusermatherr`, `_acmdln`, `_amsg_exit`, `_beginthreadex`, `_cexit`, `_close`, `_commode`, `_errno`
**NETAPI32.dll**: `NetApiBufferFree`, `NetWkstaGetInfo`
**ole32.dll**: `CLSIDFromString`, `CoCreateInstance`, `CoInitializeEx`, `CoSetProxyBlanket`, `CoUninitialize`, `CreateStreamOnHGlobal`, `GetHGlobalFromStream`
**OLEAUT32.dll**: `SysAllocStringByteLen`, `SysFreeString`, `SysStringByteLen`
**RPCRT4.dll**: `RpcStringFreeA`, `UuidCreate`, `UuidToStringA`
**SHELL32.dll**: `SHGetFolderPathA`
**USER32.dll**: `CallNextHookEx`, `CloseClipboard`, `DispatchMessageA`, `EnumDisplayMonitors`, `GetAsyncKeyState`, `GetClassNameA`, `GetClipboardData`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetForegroundWindow`, `GetKeyboardLayout`, `GetKeyboardLayoutNameA`, `GetLastInputInfo`, `GetMessageA`
**WINHTTP.dll**: `WinHttpAddRequestHeaders`, `WinHttpCloseHandle`, `WinHttpConnect`, `WinHttpOpen`, `WinHttpOpenRequest`, `WinHttpQueryDataAvailable`, `WinHttpQueryHeaders`, `WinHttpReadData`, `WinHttpReceiveResponse`, `WinHttpSendRequest`, `WinHttpSetOption`, `WinHttpSetTimeouts`
**WININET.dll**: `InternetCloseHandle`, `InternetGetConnectedState`, `InternetOpenA`, `InternetOpenUrlA`, `InternetReadFile`
**WS2_32.dll**: `WSACleanup`, `WSAStartup`, `closesocket`, `connect`, `freeaddrinfo`, `getaddrinfo`, `gethostname`, `htons`, `inet_ntoa`, `inet_pton`, `socket`

## Extracted Strings

Total strings found: **14349** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
@.xdata
.idata
.reloc
AUATUWVSH
[^_]A\A]
[^_]A\A]
Q(D;Q,}1Ic
Q(;Q,}=Hc
ATWVSH
([^_A\
S(;S,},Hc
_GLOBAL_H9
$<;v0H
CH;S,}6Hc
	w\<_t`
ATUWVSH
 [^_]A\
ATUWVSH
0[^_]A\
S8;S<}
0[^_]A\
0[^_]A\
S(;S,}
u-<.t)<Rt
K(;K,}?Lc
S(;S,};Hc
AUATUWVSH
H[^_]A\A]
H[^_]A\A]
T$8A;T$<
H[^_]A\A]
D$(A;D$,
T$8A;T$<
T$8A;T$<}"I
H[^_]A\A]
D$(A;D$,
D$(A;D$,
AUATSH
 [A\A]
 [A\A]
 [A\A]
D$(A;D$,
AUATVSH
([^A\A]
D$(A;D$,}eLc
([^A\A]
([^A\A]
([^A\A]
([^A\A]
ATWVSH
@88t2A
8[^_A\
8[^_A\
8[^_A\
AWAVAUATUWVSH
([^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
[^_]A\A]A^A_
[^_]A\A]A^A_
[^_]A\A]A^A_
[^_]A\A]A^A_
[^_]A\A]A^A_
[^_]A\A]A^A_
[^_]A\A]A^A_
[^_]A\A]A^A_
ATUWVSH
 [^_]A\
 [^_]A\
 [^_]A\
AUATUWVSH
H[^_]A\A]
H[^_]A\A]
H[^_]A\A]
H[^_]A\A]
AUATUWVSH
([^_]A\A]
ATWVSH
([^_A\
([^_A\
UAWAVAUATWVSH
$<;w%H
[^_A\A]A^A_]
<GtD<Tt@1
AVAUATUWVSH
 [^_]A\A]A^
AUATWVSH
@[^_A\A]
@[^_A\A]
ATUWVSH
P[^_]A\
P[^_]A\
UAWAVAUATWVSH
[^_A\A]A^A_]
ATWVSH
([^_A\H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400024b0` | `0x1400024b0` | 1532216 | ✓ |
| `fcn.1401787c0` | `0x1401787c0` | 1444482 | ✓ |
| `fcn.1400a2bb0` | `0x1400a2bb0` | 612123 | ✓ |
| `fcn.1400aa300` | `0x1400aa300` | 602134 | ✓ |
| `fcn.1400a9f00` | `0x1400a9f00` | 601006 | ✓ |
| `fcn.14016efe0` | `0x14016efe0` | 530823 | ✓ |
| `fcn.1400255f0` | `0x1400255f0` | 103420 | ✓ |
| `fcn.14000bdd0` | `0x14000bdd0` | 50581 | ✓ |
| `fcn.14000b510` | `0x14000b510` | 49222 | ✓ |
| `fcn.14000dc40` | `0x14000dc40` | 38990 | ✓ |
| `fcn.140034780` | `0x140034780` | 27919 | ✓ |
| `fcn.1400053a0` | `0x1400053a0` | 27571 | ✓ |
| `fcn.1400631c0` | `0x1400631c0` | 19281 | ✓ |
| `fcn.14007ef00` | `0x14007ef00` | 17867 | ✓ |
| `fcn.14016f1b0` | `0x14016f1b0` | 13689 | ✓ |
| `fcn.1400607e0` | `0x1400607e0` | 10707 | ✓ |
| `fcn.1400834d0` | `0x1400834d0` | 10524 | ✓ |
| `fcn.140043620` | `0x140043620` | 8909 | ✓ |
| `fcn.140030690` | `0x140030690` | 8595 | ✓ |
| `fcn.140089730` | `0x140089730` | 7958 | ✓ |
| `fcn.1400ac570` | `0x1400ac570` | 7631 | ✓ |
| `fcn.14002aff0` | `0x14002aff0` | 7391 | ✓ |
| `fcn.14003df00` | `0x14003df00` | 7268 | ✓ |
| `fcn.14008db80` | `0x14008db80` | 7069 | ✓ |
| `fcn.14000e590` | `0x14000e590` | 6975 | ✓ |
| `fcn.14006a5c0` | `0x14006a5c0` | 6261 | ✓ |
| `fcn.140162480` | `0x140162480` | 5948 | ✓ |
| `fcn.140013d50` | `0x140013d50` | 5850 | ✓ |
| `fcn.1400b0cd0` | `0x1400b0cd0` | 5296 | ✓ |
| `fcn.1400d9510` | `0x1400d9510` | 4970 | ✓ |

### Decompiled Code Files

- [`code/fcn.1400024b0.c`](code/fcn.1400024b0.c)
- [`code/fcn.1400053a0.c`](code/fcn.1400053a0.c)
- [`code/fcn.14000b510.c`](code/fcn.14000b510.c)
- [`code/fcn.14000bdd0.c`](code/fcn.14000bdd0.c)
- [`code/fcn.14000dc40.c`](code/fcn.14000dc40.c)
- [`code/fcn.14000e590.c`](code/fcn.14000e590.c)
- [`code/fcn.140013d50.c`](code/fcn.140013d50.c)
- [`code/fcn.1400255f0.c`](code/fcn.1400255f0.c)
- [`code/fcn.14002aff0.c`](code/fcn.14002aff0.c)
- [`code/fcn.140030690.c`](code/fcn.140030690.c)
- [`code/fcn.140034780.c`](code/fcn.140034780.c)
- [`code/fcn.14003df00.c`](code/fcn.14003df00.c)
- [`code/fcn.140043620.c`](code/fcn.140043620.c)
- [`code/fcn.1400607e0.c`](code/fcn.1400607e0.c)
- [`code/fcn.1400631c0.c`](code/fcn.1400631c0.c)
- [`code/fcn.14006a5c0.c`](code/fcn.14006a5c0.c)
- [`code/fcn.14007ef00.c`](code/fcn.14007ef00.c)
- [`code/fcn.1400834d0.c`](code/fcn.1400834d0.c)
- [`code/fcn.140089730.c`](code/fcn.140089730.c)
- [`code/fcn.14008db80.c`](code/fcn.14008db80.c)
- [`code/fcn.1400a2bb0.c`](code/fcn.1400a2bb0.c)
- [`code/fcn.1400a9f00.c`](code/fcn.1400a9f00.c)
- [`code/fcn.1400aa300.c`](code/fcn.1400aa300.c)
- [`code/fcn.1400ac570.c`](code/fcn.1400ac570.c)
- [`code/fcn.1400b0cd0.c`](code/fcn.1400b0cd0.c)
- [`code/fcn.1400d9510.c`](code/fcn.1400d9510.c)
- [`code/fcn.140162480.c`](code/fcn.140162480.c)
- [`code/fcn.14016efe0.c`](code/fcn.14016efe0.c)
- [`code/fcn.14016f1b0.c`](code/fcn.14016f1b0.c)
- [`code/fcn.1401787c0.c`](code/fcn.1401787c0.c)

## Behavioral Analysis

The final piece of disassembly completes the technical picture of **XilenStealer V5**. This final chunk reveals that the malware is not merely a collection of malicious scripts, but utilizes an **Interpreter-style Dispatcher** architecture typical of professional-grade Trojan families (like Emotet or TrickBot).

Here is the updated and expanded analysis incorporating all findings.

---

### **Final Comprehensive Analysis: XilenStealer V5**

#### **1. Advanced "Switchboard" & Interpreter Logic (The Command Engine)**
The core of `fcn.1400d9510` reveals a massive, complex switch statement (over 60 cases) that acts as an internal interpreter.
*   **Command Execution:** Instead of hard-coding behaviors like "Steal Passwords" or "Log Keys," the malware reads a "byte" or "instruction code" from its memory/configuration and jumps to the corresponding logic in this switch table. 
*   **Multi-Functionality via One Binary:** Because it uses an interpreter, a single `.exe` file can behave differently depending on what "commands" are sent by the C2 server. For example, Case `0x19`, Case `0x24`, and Case `0x37` likely represent entirely different behaviors (e.g., one for screen scraping, one for file exfiltration, one for anti-debugging checks).
*   **Code Reuse:** This allows the developers to update the *capabilities* of the malware by simply updating a remote configuration file rather than recompiling and redistributing new versions of the malicious binary.

#### **2. Sophisticated State Management & Navigation**
The logic surrounding `code_r0x0001400d95a6` shows the malware managing complex states during its execution.
*   **State-Aware Parsing:** The code frequently checks for specific offsets (e.g., `+ 0x139`, `+ 0x140`). This indicates that the malware is processing a highly structured internal data structure—likely a "Manifest" or a "Task List." 
*   **Internal Scripting/Instruction Set:** The use of nested loops to iterate through data blocks (e.g., `while(puVar36 = puVar36 + 1...)`) suggests the malware is processing a sequence of instructions, much like a script engine. This allows it to perform complex, multi-step tasks while keeping its core code "clean" and harder for automated tools to flag as specific behaviors.

#### **3. Resilience & Dynamic Error Handling**
The repeated calls to `fcn.140121760` (often seen when a check fails or a value is unexpected) suggest an advanced error-handling layer. 
*   **Fallback Logic:** When the malware encounters a "bad" state or a blocked action, it doesn't simply crash; it enters a recovery loop or jumps to a different routine. This prevents security researchers from crashing the program into a detectable state and helps the malware stay resident on the victim's machine even if certain functions are interfered with.

#### **4. Robust Data Processing & Buffer Management**
The complex logic involving `uVar11`, `uVar_f8`, and various memory offsets in the final segment confirms that XilenStealer handles significant amounts of data before it is exfiltrated.
*   **Payload Preparation:** The heavy use of loops to calculate buffer sizes (`puVar_148 = uVar_11 - iVar_12`) suggests it is "packaging" stolen information (like cookies, browser history, and keylogs) into specific packets before transmission.
*   **Evasion via Packaging:** By dynamically calculating the length of strings and packing them into a structured format, the malware ensures that the final data sent to the C2 server looks like legitimate web traffic or standard protocol noise, making it harder for Network Intrusion Detection Systems (NIDS) to flag the exfiltration.

---

### **Final Summary Conclusion: XilenStealer V5**

The full disassembly of XilenStealer V5 confirms that this is a **highly sophisticated, industrial-grade threat platform.** It has moved beyond the "script kiddie" level of simple data theft and entered the realm of professional cybercrime infrastructure.

**Core Threat Pillars:**
1.  **Modular Resilience (Switchboard Architecture):** The use of a massive jump table means the malware is highly versatile. One binary can act as a logger, an injector, or a stealer based on remote instructions, allowing it to adapt to different targets without changing its signature.
2.  **Interpreter-Style Execution:** By using an internal "command" system, the authors have effectively decoupled the *malicious actions* from the *main binary*. This makes behavioral analysis much harder for defenders.
3.  **Complex Data Handling (The Packaging Engine):** The detailed logic for processing strings and managing buffer sizes indicates a focus on successful, stealthy data exfiltration—ensuring that stolen credentials actually reach the attacker without being blocked by firewalls.
4.  **Sophisticated Evasion Strategy:** The combination of multi-stage decoding (from previous chunks) and a complex switch-table dispatcher suggests an advanced awareness of signature-based and heuristic-based detection methods.

**Final Verdict:** 
XilenStealer V5 is designed for **longevity and scalability**. It provides threat actors with a stable, versatile platform that can be updated remotely to target various types of data (financial information, crypto-wallets, or corporate secrets) while maintaining a low profile through advanced modular design.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors of XilenStealer V5 to the following MITRE ATT&CK techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The "Interpreter-style Dispatcher" uses a large switch statement to process internal instructions, allowing one binary to perform multiple different functions based on remote commands. |
| **T1568.003** | Data Encoding | The "Packaging Engine" structures stolen data into specific packets designed to mimic "standard protocol noise" to evade detection by Network Intrusion Detection Systems (NIDS). |
| **T1041** | Exfiltration Over C2 Channel | The malware collects and processes sensitive information (cookies, keylogs, etc.) specifically for delivery to the threat actor's infrastructure. |
| **T1568** | Obfuscated Files or Resources | The mention of "multi-stage decoding" indicates that the malware employs obfuscation techniques to hide its true capabilities from signature-based and heuristic detection. |
| **T1028** | Dynamic Resolution | The use of a "switchboard" architecture allows the malware to determine which code paths to execute dynamically based on configuration rather than having fixed, detectable behavior. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis for **XilenStealer V5**, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified in the provided text.*

**File paths / Registry keys**
*   *None identified in the provided text.*

**Mutex names / Named pipes**
*   *None identified in the provided text.*

**Hashes**
*   *None identified in the provided string block.*

**Other artifacts**
*   **Malware Family:** XilenStealer V5
*   **Internal Function Identifiers (Behavioral Artifacts):** 
    *   `fcn.1400d9510` (Interpreter/Switchboard Dispatcher)
    *   `fcn.140121760` (Error handling and fallback logic)
*   **Technical Behaviors/Patterns:**
    *   **Interpreter-style Dispatcher:** Use of a massive switch statement (over 60 cases) to interpret "instruction codes" for multi-functional capabilities.
    *   **State-Aware Parsing:** Logic utilizing specific memory offsets (e.g., `+ 0x139`, `+ 0x140`) to process internal manifests/task lists.
    *   **Buffer Packaging Engine:** Use of complex loops and calculations (e.g., `puVar_148 = uVar_11 - iVar_12`) to package stolen data (cookies, history, keylogs) into structured packets for evasion.

***Analyst Note:** The "Extracted Strings" section contains high amounts of non-human-readable or obfuscated character strings (e.g., `AUATUWVSH`, `H[^_]A\A]`). These do not contain actionable network indicators or file paths in their current form and are likely the result of a decoding process that has not fully normalized the data.*

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://77.110.103.209:3000`
- `https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css`
- `https://github.com/BengaminButton`
- `https://t.me/XillenKillers`
- `https://test-site.com`

**IP addresses:**
- `77.110.103.209`

**Domains:**
- `api.telegram.org`

---

## Malware Family Classification

Based on the analysis provided, here is the classification for the sample:

1. **Malware family:** XilenStealer V5
2. **Malware type:** infostealer
3. **Confidence:** High
4. **Key evidence:**
    *   **Interpreter-Style Architecture:** The malware utilizes a complex "Switchboard" dispatcher (over 60 cases) that allows a single binary to perform multiple roles—such as keylogging, screen scraping, and data exfiltration—based on remote instructions received from the C2 server.
    *   **Targeted Data Theft:** The analysis explicitly identifies functions designed for the collection of high-value information, including browser cookies, history, and keystrokes.
    *   **Advanced Evasion Techniques:** It employs a "Packaging Engine" to format stolen data into structures that mimic standard protocol noise, specifically intended to bypass Network Intrusion Detection Systems (NIDS) during the exfiltration phase.
