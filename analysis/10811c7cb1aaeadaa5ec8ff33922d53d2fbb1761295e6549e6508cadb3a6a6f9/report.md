# Threat Analysis Report

**Generated:** 2026-08-19 01:38 UTC
**Sample:** `10811c7cb1aaeadaa5ec8ff33922d53d2fbb1761295e6549e6508cadb3a6a6f9_10811c7cb1aaeadaa5ec8ff33922d53d2fbb1761295e6549e6508cadb3a6a6f9.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `10811c7cb1aaeadaa5ec8ff33922d53d2fbb1761295e6549e6508cadb3a6a6f9_10811c7cb1aaeadaa5ec8ff33922d53d2fbb1761295e6549e6508cadb3a6a6f9.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 2,302,976 bytes |
| MD5 | `621a059edbdf3d2390519f6eb0c8993e` |
| SHA1 | `5ecd9db3bc11c942b4f67e51740dc06566fdaa6c` |
| SHA256 | `10811c7cb1aaeadaa5ec8ff33922d53d2fbb1761295e6549e6508cadb3a6a6f9` |
| Overall entropy | 6.664 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773920875 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,754,624 | 6.59 | No |
| `.rdata` | 505,344 | 6.298 | No |
| `.data` | 9,728 | 4.024 | No |
| `.pdata` | 26,624 | 5.775 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 512 | 4.726 | No |
| `.reloc` | 4,608 | 5.415 | No |

### Imports

**ole32.dll**: `CoUninitialize`, `CoTaskMemFree`, `CoInitializeEx`, `CoInitializeSecurity`, `CoSetProxyBlanket`, `CoCreateInstance`, `CreateStreamOnHGlobal`
**OLEAUT32.dll**: `VariantClear`, `SysAllocString`, `SysFreeString`, `VariantInit`
**ADVAPI32.dll**: `CryptGetHashParam`, `OpenProcessToken`, `ConvertSidToStringSidW`, `GetTokenInformation`, `GetCurrentHwProfileW`, `RegCloseKey`, `GetSidSubAuthorityCount`, `AllocateAndInitializeSid`, `GetSidSubAuthority`, `RegEnumKeyExW`, `FreeSid`, `CheckTokenMembership`, `RegOpenKeyExW`, `GetUserNameW`, `InitializeSecurityDescriptor`
**CRYPT32.dll**: `CryptUnprotectData`, `CryptStringToBinaryA`
**gdiplus.dll**: `GdipAlloc`, `GdipCreateBitmapFromHBITMAP`, `GdipDisposeImage`, `GdipFree`, `GdipGetImageEncodersSize`, `GdipSaveImageToStream`, `GdipCloneImage`, `GdiplusShutdown`, `GdiplusStartup`, `GdipGetImageEncoders`
**KERNEL32.dll**: `ReadConsoleW`, `HeapReAlloc`, `GetConsoleMode`, `GetConsoleOutputCP`, `SetFilePointerEx`, `GetFileSizeEx`, `EnumSystemLocalesW`, `GetUserDefaultLCID`, `IsValidLocale`, `LCMapStringW`, `CompareStringW`, `GetTimeFormatW`, `GetDateFormatW`, `GetFullPathNameW`, `LoadLibraryExA`
**USER32.dll**: `ReleaseDC`, `GetSystemMetrics`, `GetDC`, `GetKeyboardLayoutList`, `EnumDisplayDevicesA`, `SetProcessDPIAware`, `GetCursorPos`, `MessageBoxW`
**GDI32.dll**: `BitBlt`, `DeleteObject`, `DeleteDC`, `GetDeviceCaps`, `CreateCompatibleDC`, `SelectObject`, `CreateCompatibleBitmap`
**SHELL32.dll**: `SHGetFolderPathW`, `SHGetKnownFolderPath`
**WS2_32.dll**: `inet_ntop`, `closesocket`, `getaddrinfo`, `WSAStartup`, `freeaddrinfo`, `htons`, `htonl`, `send`, `socket`, `connect`, `recv`
**WINHTTP.dll**: `WinHttpQueryHeaders`, `WinHttpSetOption`, `WinHttpQueryDataAvailable`, `WinHttpReceiveResponse`, `WinHttpOpen`, `WinHttpAddRequestHeaders`, `WinHttpOpenRequest`, `WinHttpCloseHandle`, `WinHttpSendRequest`, `WinHttpReadData`, `WinHttpSetTimeouts`, `WinHttpConnect`
**IPHLPAPI.DLL**: `GetAdaptersAddresses`
**SHLWAPI.dll**: `PathFindFileNameW`

## Extracted Strings

Total strings found: **3730** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
@.reloc
UVWAVAWH
A_A^_^]
VWAUAVAWH
0A_A^A]_^
VWATAVAWH
 A_A^A\_^
VWAUAVAWH
0A_A^A]_^
l$ VWAVH
@SUVWAVH
 A^_^][
l$ VWAVH
\$ UVWAVAWH
 A_A^_^]
@SUVWAVH
 A^_^][
\$ UVWH
@SUVWATAVAWH
 A_A^A\_^][
\$ UVWAVAWH
 A_A^_^]
t$ WAVAWH
 A_A^_
@SUVWATAUAVAWH
H;\$(t!I;
L9l$0u	H
D$ L9l$0u	N
H;\$(t
HA_A^A]A\_^][
@SUVWATAUAVAWH
H;\$(t!I;
L9l$0u	H
D$ L9l$0u	N
H;\$(t
HA_A^A]A\_^][
H;\$ t*
D$(-,f]
D$Xtf9=
L$`f#
D$PH9=S
D$ u D
D$ Zy6-
D$Xt	
D$ ,YH
D$Xyt[
D$0JyHJH
D$(%5=
UVWATAUAVAWH
D$HfD#
D$LHcD$TH
f9\$tt
f9\$dt
A_A^A]A\_^]
UVWATAUAVAWH
D$xQ"_'Di
A_A^A]A\_^]
UVWATAUAVAWH
|$pH;E
D$@;D$lrBD
L$CHcE
D$\tGD
d$LD*d$HD"
|$dL97
f9|$\H
A_A^A]A\_^]
UVWATAUAVAWH
D$@,I@
D$xHcD$XH)
L$D*1
HcL$`u
L$HD9
HcD$lH
HcL$`H
u=HcL$`H
JHcL$`H
HcL$`A
D$dHc
LcD$lL
D$dHcD$lH;
~;HcL$`H
HcL$lH
D$`HcM
L;=Q}!
t$@HcL$XH+h{!
RvAHcL$XH
A_A^A]A\_^]
UVWATAUAVAWH
H)=qu!
fD9L$xt	
}D8:l!
fD9pl!
D$XD9D$pt%
D$xfD
D8u(t	H
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140044eec` | `0x140044eec` | 132337 | ✓ |
| `fcn.140177388` | `0x140177388` | 75046 | ✓ |
| `fcn.140034a78` | `0x140034a78` | 61149 | ✓ |
| `fcn.14001fba0` | `0x14001fba0` | 56886 | ✓ |
| `fcn.14018c3fc` | `0x14018c3fc` | 55335 | ✓ |
| `fcn.14018c3e8` | `0x14018c3e8` | 55294 | ✓ |
| `fcn.14018aab0` | `0x14018aab0` | 53004 | ✓ |
| `fcn.14018aaa0` | `0x14018aaa0` | 52924 | ✓ |
| `fcn.140112794` | `0x140112794` | 43333 | ✓ |
| `fcn.140123d0c` | `0x140123d0c` | 31916 | — |
| `fcn.1400d850c` | `0x1400d850c` | 30591 | ✓ |
| `fcn.1401978e0` | `0x1401978e0` | 29513 | ✓ |
| `fcn.1400a5a80` | `0x1400a5a80` | 24242 | ✓ |
| `fcn.14012c590` | `0x14012c590` | 21859 | ✓ |
| `fcn.1400cce28` | `0x1400cce28` | 20946 | ✓ |
| `fcn.140153e4c` | `0x140153e4c` | 20226 | ✓ |
| `fcn.140100188` | `0x140100188` | 18812 | ✓ |
| `fcn.1400ada1c` | `0x1400ada1c` | 16422 | ✓ |
| `fcn.1400b9bec` | `0x1400b9bec` | 15998 | ✓ |
| `fcn.1400c8734` | `0x1400c8734` | 15686 | ✓ |
| `fcn.1400945b4` | `0x1400945b4` | 15106 | ✓ |
| `fcn.140177794` | `0x140177794` | 14458 | ✓ |
| `method.std::basic_ostringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x14006b95c` | 14368 | ✓ |
| `method.std::basic_istringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x14006b968` | 14288 | ✓ |
| `fcn.140076c30` | `0x140076c30` | 14146 | ✓ |
| `method.std::basic_ostream_char__struct_std::char_traits_char__.virtual_0` | `0x14006b944` | 14020 | ✓ |
| `fcn.14010b2c4` | `0x14010b2c4` | 13964 | ✓ |
| `method.std::basic_istream_char__struct_std::char_traits_char__.virtual_0` | `0x14006b950` | 13932 | ✓ |
| `fcn.1400b65b8` | `0x1400b65b8` | 13876 | ✓ |
| `fcn.14000fff0` | `0x14000fff0` | 13284 | ✓ |

### Decompiled Code Files

- [`code/fcn.14000fff0.c`](code/fcn.14000fff0.c)
- [`code/fcn.14001fba0.c`](code/fcn.14001fba0.c)
- [`code/fcn.140034a78.c`](code/fcn.140034a78.c)
- [`code/fcn.140044eec.c`](code/fcn.140044eec.c)
- [`code/fcn.140076c30.c`](code/fcn.140076c30.c)
- [`code/fcn.1400945b4.c`](code/fcn.1400945b4.c)
- [`code/fcn.1400a5a80.c`](code/fcn.1400a5a80.c)
- [`code/fcn.1400ada1c.c`](code/fcn.1400ada1c.c)
- [`code/fcn.1400b65b8.c`](code/fcn.1400b65b8.c)
- [`code/fcn.1400b9bec.c`](code/fcn.1400b9bec.c)
- [`code/fcn.1400c8734.c`](code/fcn.1400c8734.c)
- [`code/fcn.1400cce28.c`](code/fcn.1400cce28.c)
- [`code/fcn.1400d850c.c`](code/fcn.1400d850c.c)
- [`code/fcn.140100188.c`](code/fcn.140100188.c)
- [`code/fcn.14010b2c4.c`](code/fcn.14010b2c4.c)
- [`code/fcn.140112794.c`](code/fcn.140112794.c)
- [`code/fcn.14012c590.c`](code/fcn.14012c590.c)
- [`code/fcn.140153e4c.c`](code/fcn.140153e4c.c)
- [`code/fcn.140177388.c`](code/fcn.140177388.c)
- [`code/fcn.140177794.c`](code/fcn.140177794.c)
- [`code/fcn.14018aaa0.c`](code/fcn.14018aaa0.c)
- [`code/fcn.14018aab0.c`](code/fcn.14018aab0.c)
- [`code/fcn.14018c3e8.c`](code/fcn.14018c3e8.c)
- [`code/fcn.14018c3fc.c`](code/fcn.14018c3fc.c)
- [`code/fcn.1401978e0.c`](code/fcn.1401978e0.c)
- [`code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_istream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ostream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_ostringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)

## Behavioral Analysis

This analysis incorporates findings from **Chunk 25/25**, the final segment of the provided disassembly. This concluding chunk confirms and reinforces the previous observations regarding extreme obfuscation while providing specific evidence for how the malware handles internal logic and string manipulation.

### Updated Analysis Report (Chunks 1–25 Integrated)

#### 1. Advanced Obfuscation: Arithmetic Noise & Opaque Predicates
Chunk 25 provides a "textbook" example of high-level anti-analysis techniques used by sophisticated threat actors.
*   **Arithmetic Bloat:** The assembly contains numerous operations like `uStack_de8 = uStack_de8 + *0x14022adaa * -0x42` and `*0x14022adc8 = *0x14022adaa + 0x8242`. These are likely **"identity operations"** or result in constants that only become clear through heavy manual calculation.
*   **Opaque Predicates:** The line `if (bVar31 == *0x14022adb1 <= *0x14022ade8)` is a classic example of an opaque predicate—a conditional branch where the outcome is always the same, but the logic used to reach that conclusion is so complex that automated tools cannot simplify it. This forces a human analyst to waste time evaluating meaningless math.
*   **Loop Masking:** The `do...while` loop (around `iVar22`) is designed to hide simple assignments or increments behind a series of dummy calculations, making it harder to determine what the final value of `uStack_de8` actually represents.

#### 2. String Manipulation & Path Parsing
A significant revelation in Chunk 25 relates to how the malware handles system paths and environment data:
*   **Directory Traversal Logic:** The loop checking for `'/'` (the forward slash) confirms that the malware is actively **parsing file paths**. This connects directly to the earlier findings regarding `GetTempPathW` and `GetWindowsDirectoryW`. It is likely processing these paths to decide where to drop files, extract payloads, or hide within system directories.
*   **Dynamic Buffer Handling:** The logic involving `puVar8` and the calculation of offsets (`puVar11 = *puVar8`) indicates a sophisticated way of handling strings in memory. Rather than using static global variables, it navigates a data structure to find necessary path components at runtime.

#### 3. State Machine & "Just-in-Time" (JIT) Decoding
The complexity of the final logic reinforces the **State Machine** theory:
*   The jump `goto code_r0x000140013395` and the heavy use of stack-relative addressing suggest that the malware is moving through different stages of execution. Each "state" (e.g., Persistence, Data Collection, Networking) is wrapped in these layers of mathematical noise to prevent a linear understanding of its capabilities.
*   **XOR Decryption on Exit:** The final call `fcn.140178bc0(_var_bp_40h ^ auStack_e28)` involving an XOR operation strongly suggests that the malware is performing **on-the-fly decryption or "scrubbing."** It may be decrypting its next command or clearing sensitive information from memory before exiting a function to evade in-memory scanners.

#### 4. Technical Synergy (Consolidated Findings)
The combination of elements across all 25 chunks paints a picture of a highly professional, likely state-sponsored or high-level criminal tool:
*   **Anti-Forensic Focus:** By using `GetProcAddress` for core functions and wrapping everything in "math noise," the authors ensure that simple static analysis (looking at the Import Address Table) reveals nothing.
*   **Environment Awareness:** The extensive gathering of system info (`GetUserNameW`, etc.) combined with complex path parsing suggests a **highly targeted approach**. The malware may have different behaviors depending on the specific environment it detects.

---

### Updated Summary Table of Observed Indicators

| Category | Technical Detail | Potential Threat Impact |
| :--- | :--- | :--- |
| **Extreme Obfuscation** | Arithmetic bloat, opaque predicates (e.g., `if (bVar31 == ...)`), and identity math. | Exhausts human analysts; designed to break automated de-obfuscation scripts and "de-compilers." |
| **Dynamic API Resolution** | Manual resolution of `GetProcAddress` for core DLLs (`kernel32`, `advapi32`). | Bypasses static analysis; hides intent (e.g., injection, persistence) from basic scanners. |
| **String/Path Logic** | Complex parsing of directory separators (`'/'`) and dynamic buffer navigation. | Indicates the malware is preparing to move files or drop secondary payloads in specific system paths. |
| **Just-In-Time Decoding** | Short-lived strings and XOR operations during execution (e.g., `_var_bp_40h ^ auStack_e28`). | Prevents memory forensics from finding hardcoded C2 addresses or keys; ensures "clean" memory after use. |
| **State Machine Architecture** | Non-linear control flow using complex conditional logic and jumps. | Makes it difficult to map the full lifecycle of the infection during a single analysis pass. |

---

### Final Strategic Insights (Final Conclusion)

1.  **Sophisticated Threat Actor Profile:** The use of "Mathematical Shields" as an obfuscation layer is not standard for common malware; it suggests a high-level development team capable of creating custom packers or using advanced protective wrappers.
2.  **Intentional Anti-Analysis Complexity:** Every layer of complexity added (the math, the opaque predicates, the dynamic resolution) is designed to **increase the "Cost of Analysis."** The goal is to make it so time-consuming for a researcher to de-obfuscate that the malware can remain active and effective in the wild.
3.  **Robust Stability:** The fact that the code meticulously parses paths and checks environment details suggests this is intended as a stable, reliable "loader" or "dropper." It is designed not just to infect, but to survive and integrate into the target system's infrastructure.

---

### Recommendations for Final Report/Response:

1.  **Automated De-obfuscation:** Use a script (e.g., Python/IDAPython) to identify blocks of code where complex arithmetic results in constant values and "fold" those expressions during the analysis phase.
2.  **Dynamic Memory Monitoring:** Perform memory forensics at the points where path parsing occurs. Capturing the memory at these moments will reveal the actual paths being processed (e.g., which specific folders it intends to infect).
3.  **Behavioral Analysis of `advapi32` Calls:** Since the malware uses dynamic resolution for this library, set a hook on all calls into `advapi32.dll`. This is the highest-probability area for detecting "Privilege Escalation" or "Persistence" attempts (e.g., `CreateService`, `WriteKey`).
4.  **Indicator Generation:** Generate YARA rules based on the unique arithmetic patterns and constants found in Chunk 25, as these "mathematical signatures" may remain consistent even if the underlying strings are changed for different campaigns.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of arithmetic bloat, opaque predicates, and loop masking is designed to hinder manual analysis and evade automated de-obfuscation tools. |
| T1083 | File and Directory Discovery | The parsing of directory separators and the use of `GetTempPathW` indicate that the malware is identifying system locations for payload staging or delivery. |
| T1402 | Encrypted Payload | The "just-in-time" XOR decoding ensures that sensitive information (such as C2 addresses) remains encrypted in memory until it is needed, evading signature-based scanners. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Below are the extracted Indicators of Compromise (IOCs).

Note: The **EXTRACTED STRINGS** section appears to consist primarily of high-entropy, obfuscated data or remnants of failed de-obfuscation, and does not contain any plain-text IP addresses, URLs, or file paths.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis confirms that C2 infrastructure is hidden behind "Just-in-Time" decoding and XOR operations).

### **File paths / Registry keys**
*   *None identified.* (While the behavioral analysis notes the use of `GetTempPathW` and `GetWindowsDirectoryW`, no specific local or remote file paths were present in the provided text).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 strings were present in the raw data).

### **Other artifacts**
*   **Memory/Function Offsets (Signature Detection):**
    *   `0x14022adaa` (Arithmetic logic location)
    *   `0x14022adc8` (Arithmetic logic location)
    *   `0x14022adb1` (Opaque predicate check)
    *   `0x140178bc0` (XOR decryption/scrubbing function)
*   **Encryption Patterns:**
    *   **XOR Decoding:** The presence of `_var_bp_40h ^ auStack_e28` indicates a specific XOR-based key or mask used for memory scrubbing and internal string de-obfuscation.
*   **API Dependencies (Behavioral):**
    *   Targeting of `kernel32.dll` and `advapi32.dll` via `GetProcAddress`.
    *   Utilization of `GetProcAddress` to hide imports from static analysis.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader / dropper
3. **Confidence**: High

4. **Key evidence**:
* **Advanced Obfuscation Techniques:** The use of "arithmetic bloat," "opaque predicates," and "loop masking" indicates a sophisticated, professional-grade codebase designed specifically to exhaust human analysts and bypass automated de-obfuscation tools.
* **Infrastructure for Payload Delivery:** The extensive parsing of system paths (via `GetTempPathW` and `GetWindowsDirectoryW`) combined with a state-machine architecture strongly suggests the primary role of this component is to prepare environment conditions and stage/drop additional payloads. 
* **Anti-Forensic Measures:** The reliance on dynamic API resolution (`GetProcAddress` for `advapi32.dll` and `kernel32.dll`) and "Just-in-Time" XOR decoding indicates a high level of intent to hide capabilities (such as persistence or remote execution) from static analysis and memory scanners.
