# Threat Analysis Report

**Generated:** 2026-08-11 19:04 UTC
**Sample:** `0e2bd6cefeabfc90fc29501d26c4460cab14c8fbe549c7fda58aa0934389f399_0e2bd6cefeabfc90fc29501d26c4460cab14c8fbe549c7fda58aa0934389f399.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0e2bd6cefeabfc90fc29501d26c4460cab14c8fbe549c7fda58aa0934389f399_0e2bd6cefeabfc90fc29501d26c4460cab14c8fbe549c7fda58aa0934389f399.exe` |
| File type | PE32+ executable for MS Windows 5.02 (GUI), x86-64, 21 sections |
| Size | 3,568,197 bytes |
| MD5 | `730ccb76af5ee3d2b98d37eb63254581` |
| SHA1 | `0422fa3b9ecb22c81b19e6ee5cd8f847713eae6e` |
| SHA256 | `0e2bd6cefeabfc90fc29501d26c4460cab14c8fbe549c7fda58aa0934389f399` |
| Overall entropy | 6.543 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771392234 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 860,672 | 6.161 | No |
| `.data` | 321,024 | 7.908 | ⚠️ Yes |
| `.rdata` | 234,496 | 7.415 | ⚠️ Yes |
| `/4` | 512 | -0.0 | No |
| `.pdata` | 52,736 | 6.031 | No |
| `.xdata` | 75,776 | 4.834 | No |
| `.bss` | 0 | 0.0 | No |
| `.idata` | 9,728 | 4.73 | No |
| `.CRT` | 512 | 0.37 | No |
| `.tls` | 512 | -0.0 | No |
| `.reloc` | 6,656 | 5.341 | No |
| `/14` | 512 | 0.844 | No |
| `/29` | 17,920 | 5.879 | No |
| `/41` | 2,560 | 4.518 | No |
| `/55` | 2,560 | 4.761 | No |
| `/67` | 1,536 | 3.034 | No |
| `/80` | 512 | 2.988 | No |
| `/91` | 1,536 | 4.354 | No |
| `/107` | 2,560 | 4.069 | No |
| `/123` | 512 | 2.356 | No |
| `.rsrc` | 179,712 | 7.641 | ⚠️ Yes |

### Imports

**ADVAPI32.dll**: `GetTokenInformation`, `GetUserNameA`, `OpenProcessToken`, `RegCloseKey`, `RegOpenKeyExA`
**COMCTL32.dll**: `InitCommonControlsEx`
**CRYPT32.dll**: `CertCloseStore`, `CertOpenSystemStoreA`
**dwmapi.dll**: `DwmIsCompositionEnabled`
**GDI32.dll**: `CreateCompatibleDC`, `DeleteDC`, `GetDeviceCaps`, `GetStockObject`
**IMM32.dll**: `ImmGetDefaultIMEWnd`
**IPHLPAPI.DLL**: `GetAdaptersInfo`
**KERNEL32.dll**: `AddVectoredExceptionHandler`, `CloseHandle`, `CreateEventA`, `CreateSemaphoreA`, `DeleteCriticalSection`, `DuplicateHandle`, `EnterCriticalSection`, `FileTimeToSystemTime`, `FormatMessageA`, `FreeEnvironmentStringsA`, `FreeLibrary`, `GetComputerNameA`, `GetConsoleOutputCP`, `GetCurrentProcess`, `GetCurrentProcessId`
**ucrtbase.dll**: `__C_specific_handler`, `___lc_codepage_func`, `___mb_cur_max_func`, `__acrt_iob_func`, `__daylight`, `__intrinsic_setjmpex`, `__p___argc`, `__p___argv`, `__p___wargv`, `__p__acmdln`, `__p__commode`, `__p__environ`, `__p__fmode`, `__p__wenviron`, `__setusermatherr`
**NETAPI32.dll**: `NetApiBufferFree`, `NetWkstaGetInfo`
**ole32.dll**: `CoInitializeEx`, `CoUninitialize`
**OLEAUT32.dll**: `SysAllocString`, `SysFreeString`, `SysStringLen`
**POWRPROF.dll**: `GetActivePwrScheme`
**SensApi.dll**: `IsNetworkAlive`
**SHELL32.dll**: `SHGetFolderPathA`
**SHLWAPI.dll**: `PathFindFileNameA`
**USER32.dll**: `GetAsyncKeyState`, `GetCursorPos`, `GetDC`, `GetDesktopWindow`, `GetKeyboardType`, `GetSystemMetrics`, `GetWindowRect`, `MonitorFromPoint`, `ReleaseDC`
**UxTheme.dll**: `GetThemeAppProperties`, `IsAppThemed`
**VERSION.dll**: `GetFileVersionInfoSizeA`
**WININET.dll**: `InternetCloseHandle`, `InternetGetConnectedStateExA`, `InternetOpenA`

## Extracted Strings

Total strings found: **24799** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
.pdata
@.xdata
.idata
.reloc
B.rsrc
f=MZt

AVAUATUWVSI
[^_]A\A]A^
[^_]A\A]A^
ATUWVSH
 [^_]A\
AVAUATUWVSH
urHcq<
0[^_]A\A]A^
(HcA<H
AUATUWVS
[^_]A\A]
AWAVAUATUWVSH
H[^_]A\A]A^A_
AVAUATUWVSH
D$XH+D$8H
p[^_]A\A]A^
AWAVAUATUWVSH
X[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
AWAVAUATUWVSH
[^_]A\A]A^A_
D$(+D$ 
AUATUWVSI

[^_]A\A]

[^_]A\A]
ATUWVSH
;7}/H9
 [^_]A\
AWAVAUATUWVSH
h[^_]A\A]A^A_
\$0H9u 
AWAVAUATUWVSH
8[^_]A\A]A^A_
ATUWVSH
[^_]A\
ATUWVSH
 [^_]A\
J(A;J,}SHc
I(D;I,}FIc
ATUWVSH
 [^_]A\
<_t_<ntS
S(;S,}.Hc
_GLOBAL_H9
$<;v0H
CH;S,}6Hc
<_u*;K8s
AUATUWVSH
C8;C<}
8[^_]A\A]
8[^_]A\A]
u-<.t)<Rt
S(;S,}
C8;C<}"H
<stZ<f
AWAVAUATUWVSH
([^_]A\A]A^A_
<Gtx<Ttt1
S8;S<}[H
C(;C,}VLc
C(;C,}
AWAVAUATUWVSH
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
AUATUWVSH
([^_]A\A]
UAWAVAUATWVSH
0<	w-A
C<Gtl<Tth1
[^_A\A]A^A_]
AVAUATUWVSH
 [^_]A\A]A^
AUATUWVSH
([^_]A\A]
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym._37` | `0x1400037fc` | 839511 | ✓ |
| `fcn.140006cc0` | `0x140006cc0` | 833285 | ✓ |
| `fcn.1400107e0` | `0x1400107e0` | 796710 | ✓ |
| `sym._83` | `0x1400ceec0` | 795093 | ✓ |
| `sym._80` | `0x1400ceda0` | 778841 | ✓ |
| `fcn.140028380` | `0x140028380` | 696532 | ✓ |
| `sym._113` | `0x140029e30` | 683112 | ✓ |
| `sym._152` | `0x1400a98d0` | 161616 | ✓ |
| `sym._162` | `0x1400ab240` | 155472 | ✓ |
| `sym.___6` | `0x1400ab3d0` | 154976 | ✓ |
| `fcn.140039590` | `0x140039590` | 123158 | ✓ |
| `fcn.140039180` | `0x140039180` | 122190 | ✓ |
| `sym._85` | `0x1400278d0` | 94385 | ✓ |
| `sym.tsIwESaIwEE5eraseEyy` | `0x140029340` | 57249 | ✓ |
| `fcn.140009c60` | `0x140009c60` | 26331 | ✓ |
| `fcn.1400d24e0` | `0x1400d24e0` | 14967 | ✓ |
| `sym.S4_RS4_PDsS6_RS6_` | `0x14003c120` | 9489 | ✓ |
| `sym.IPcSsEESt16initializer_listIcE` | `0x140041db0` | 8884 | ✓ |
| `fcn.140011ea6` | `0x140011ea6` | 8226 | ✓ |
| `sym.torIwSt11char_traitsIwEEEEEbRKSt6locale` | `0x14006ae20` | 7898 | ✓ |
| `sym.raitsIcESaIcEE4swapERS4_` | `0x14006fa90` | 7797 | ✓ |
| `fcn.140016fba` | `0x140016fba` | 5417 | ✓ |
| `sym.hims12_GLOBAL__N_113time_get_shimIcEE` | `0x140049520` | 4806 | ✓ |
| `sym.et_shims12_GLOBAL__N_115moneypunct_shimIcLb1EEE` | `0x1400481e0` | 4806 | ✓ |
| `sym.eIcLb1EED1Ev` | `0x140046a50` | 4770 | ✓ |
| `sym.D0Ev` | `0x140045730` | 4770 | ✓ |
| `sym.main` | `0x1400cf490` | 4522 | ✓ |
| `sym.1char_traitsIwEEE21_M_extract_via_formatES4_S4_RSt8ios_baseRSt12_Ios_IostateP2tmPKw` | `0x1400746a0` | 3896 | ✓ |
| `sym._iteratorIwSt11char_traitsIwEEE3getES4_S4_RSt8ios_baseRSt12_Ios_IostateP2tmcc` | `0x1400736f0` | 3896 | ✓ |
| `sym.xx1118basic_stringstreamIcSt11char_traitsIcESaIcEED2Ev` | `0x140076ab0` | 3871 | ✓ |

### Decompiled Code Files

- [`code/fcn.140006cc0.c`](code/fcn.140006cc0.c)
- [`code/fcn.140009c60.c`](code/fcn.140009c60.c)
- [`code/fcn.1400107e0.c`](code/fcn.1400107e0.c)
- [`code/fcn.140011ea6.c`](code/fcn.140011ea6.c)
- [`code/fcn.140016fba.c`](code/fcn.140016fba.c)
- [`code/fcn.140028380.c`](code/fcn.140028380.c)
- [`code/fcn.140039180.c`](code/fcn.140039180.c)
- [`code/fcn.140039590.c`](code/fcn.140039590.c)
- [`code/fcn.1400d24e0.c`](code/fcn.1400d24e0.c)
- [`code/sym.1char_traitsIwEEE21_M_extract_via_formatES4_S4_RSt8ios_baseRSt12_Ios_IostateP2tmPKw.c`](code/sym.1char_traitsIwEEE21_M_extract_via_formatES4_S4_RSt8ios_baseRSt12_Ios_IostateP2tmPKw.c)
- [`code/sym.D0Ev.c`](code/sym.D0Ev.c)
- [`code/sym.IPcSsEESt16initializer_listIcE.c`](code/sym.IPcSsEESt16initializer_listIcE.c)
- [`code/sym.S4_RS4_PDsS6_RS6_.c`](code/sym.S4_RS4_PDsS6_RS6_.c)
- [`code/sym._113.c`](code/sym._113.c)
- [`code/sym._152.c`](code/sym._152.c)
- [`code/sym._162.c`](code/sym._162.c)
- [`code/sym._37.c`](code/sym._37.c)
- [`code/sym._80.c`](code/sym._80.c)
- [`code/sym._83.c`](code/sym._83.c)
- [`code/sym._85.c`](code/sym._85.c)
- [`code/sym.___6.c`](code/sym.___6.c)
- [`code/sym._iteratorIwSt11char_traitsIwEEE3getES4_S4_RSt8ios_baseRSt12_Ios_IostateP2tmcc.c`](code/sym._iteratorIwSt11char_traitsIwEEE3getES4_S4_RSt8ios_baseRSt12_Ios_IostateP2tmcc.c)
- [`code/sym.eIcLb1EED1Ev.c`](code/sym.eIcLb1EED1Ev.c)
- [`code/sym.et_shims12_GLOBAL__N_115moneypunct_shimIcLb1EEE.c`](code/sym.et_shims12_GLOBAL__N_115moneypunct_shimIcLb1EEE.c)
- [`code/sym.hims12_GLOBAL__N_113time_get_shimIcEE.c`](code/sym.hims12_GLOBAL__N_113time_get_shimIcEE.c)
- [`code/sym.main.c`](code/sym.main.c)
- [`code/sym.raitsIcESaIcEE4swapERS4_.c`](code/sym.raitsIcESaIcEE4swapERS4_.c)
- [`code/sym.torIwSt11char_traitsIwEEEEEbRKSt6locale.c`](code/sym.torIwSt11char_traitsIwEEEEEbRKSt6locale.c)
- [`code/sym.tsIwESaIwEE5eraseEyy.c`](code/sym.tsIwESaIwEE5eraseEyy.c)
- [`code/sym.xx1118basic_stringstreamIcSt11char_traitsIcESaIcEED2Ev.c`](code/sym.xx1118basic_stringstreamIcSt11char_traitsIcESaIcEED2Ev.c)

## Behavioral Analysis

Based on the final disassembly provided in chunk 5/5, we can now synthesize the complete picture of this loader. The addition of this section provides the "missing link" between the **VM-based control flow** and the **actual payload processing**.

We are no longer looking at just a "loader"; we are looking at a **multi-stage decryption and transformation engine.**

### Updated Technical Analysis (Chunk 5/5)

#### 1. Sophisticated Decryption & Transformation Pipeline
The most striking feature of this chunk is the heavy mathematical and bitwise manipulation occurring in what appears to be the core "unpacking" loop.
*   **Large Buffer Processing:** The code references a large data block (`0x4b210` bytes). This confirms that the loader's primary job is to process a massive amount of encrypted/encoded data, likely containing several stages of malware or its final payload.
*   **Complex Bitwise Logic:** Instead of simple XORing, the loop uses a series of `XOR`, `shift (<< 0x10)`, and `addition` operations. This is characteristic of custom block ciphers or advanced "rolling" decoders designed to defeat simple automated de-obfuscators.
*   **Conditional Decoding Paths:** The code contains branching logic such as `if (iVar84 == 3)` and `if (iVar84 == 1)`. This indicates that the loader can adapt its decryption method based on internal state or environment checks, ensuring that only "valid" targets receive the fully decrypted payload.

#### 2. Extended Evidence of Decompiler Sabotage
The massive volume of `WARNING: Removing unreachable block` and `WARNING: Could not recover jumptable` in these specific functions (`hims12_...`, `moneypunct_...`, `stringstream_...`) confirms a deliberate attempt to "poison" the decompiler's output.
*   **Why this matters:** By wrapping essential decoding logic inside standard library calls (like `std::stringstream`), the author forces the analyst's tool to struggle with "garbage" code, making it nearly impossible to follow the logical flow of the decryption keys or the state machine without manual reconstruction.

#### 3. Final Stage: Dynamic Execution (The "Hand-off")
Near the end of the primary logic, we see a sequence involving `sym._21(s1)`, `sym._22(iVar134)`, and finally an **indirect call**: `(*(iVar93 + *(iVar93 + 0x28 + *(iVar134 + 0x3c))))()`.
*   **Significance:** This is the "handoff." The loader has successfully decrypted a block of memory, resolved its location/functionality, and is now jumping into that new code. This confirms that the code we are looking at is strictly a **loader/stub**, intended to disappear from the execution flow once it has fulfilled its role of preparing the payload.

---

### Final Cumulative Technical Findings
1.  **Advanced VM Architecture:** Confirmed high-complexity VM with overlapping opcodes and custom state management.
2.  **Sophisticated Decryption Pipeline:** Large block processing (0x4b210 bytes) using complex bitwise operations to decrypt the primary payload.
3.  **Intentional Decompiler Sabotage:** Extensive use of "junk" code and malformed jump tables to hinder automated analysis in Ghidra/IDA Pro.
4.  **System Reconnaissance:** Use of `NetWkstaGetInfo` and `EnumPrintersA` to fingerprint the target environment before proceeding with decryption.
5.  **Standard Library Shielding:** Using heavy C++ STL abstractions as a "cloak" to hide malicious logic behind legitimate-looking library code.

---

### Final Summary Conclusion
The analysis of all five chunks confirms that this is an **elite, high-sophistication malware loader.** 

It utilizes a **defense-in-depth** strategy:
1.  **Code Obfuscation:** It uses a Virtual Machine (VM) to hide the "intent" of the script.
2.  **Anti-Analysis:** It employs decompiler sabotage to slow down human researchers.
3.  **Environment Awareness:** It verifies the target's network status before attempting full decryption.
4.  **Hardened Decryption:** The final stages use complex mathematical transformations to ensure that standard "unpacker" scripts cannot easily extract the payload from the blob.

This is consistent with **state-sponsored (APT) groups** or high-end cybercrime organizations who target corporate infrastructure and require a resilient, multi-layered delivery mechanism.

### Final Recommendation for Analysis:
1.  **Memory Forensics over Static Analysis:** Because of the extreme complexity of the decryption loops and VM, static analysis is reaching its limit of diminishing returns. The most efficient way to find the "payload" is to **run the loader in a debugger**, let it complete the decryption loops (the `0x4b210` blocks), and then perform a **memory dump** just before the final indirect jump occurs.
2.  **Automated Trace Analysis:** Use an instruction tracer (like Intel PIN or a script-based tracker) to record every branch taken by the VM. This will allow you to map the "logic" of the malware without needing to manually decode the mangled assembly.
3.  **Identify the Payload Signature:** Once the memory dump is captured, the cleartext payload can be uploaded to a multi-scanner (e.g., VirusTotal or Hybrid Analysis) to identify the ultimate nature of the attack (e.g., Ransomware, InfoStealer, or Rootkit).

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your technical analysis to the corresponding MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of a complex VM architecture with overlapping opcodes is used to hide the true intent of the code. |
| **T1027** | Obfuscated Files or Information | Complex bitwise logic and multi-stage decryption are employed to mask the final payload from automated analysis tools. |
| **T1027** | Obfuscated Files or Information | Deliberate decompiler sabotage (junk code/malformed jump tables) is used to hinder manual human analysis in Ghidha/IDA Pro. |
| **T1082** | System Information Discovery | The use of `NetWkstaGetInfo` and `EnumPrintersA` identifies system details to profile the target environment. |
| **T1497** | Virtualization/Sandbox Evasion | Conditional decoding paths based on environmental factors ensure that only "valid" targets execute the full payload. |
| **T1027** | Obfuscated Files or Information | The use of Standard Library (STL) wrappers as a "cloak" hides malicious logic behind common, legitimate-looking code structures. |

### Analyst Notes:
*   **Defense-in-Depth:** The malware employs multiple layers of **T1027** to ensure that even if one layer is stripped away (e.g., the outer encryption), the next layer (the VM or decompiler sabotage) prevents the analyst from easily identifying the payload's purpose.
*   **High Sophistication Indicators:** The transition from "Loader" to "Execution Hand-off" via an indirect call suggests a sophisticated stub design intended to minimize the footprint of the loader once the payload is activated in memory.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Standard system information, such as the GCC compiler error links and common library function names (e.g., `stringstream`), have been excluded as false positives.*

**IP addresses / URLs / Domains**
*   None identified (The `gcc.gnu.org` link is a standard compiler utility string).

**File paths / Registry keys**
*   None identified.

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Data Buffers:** `0x4b210` (Identified as the specific byte count for the primary payload's decryption/processing block).
*   **System Reconnaissance APIs:** `NetWkstaGetInfo`, `EnumPrintersA` (Used to fingerprint the environment before proceeding with decryption).
*   **Execution Pattern:** Indirect call at `(*(iVar93 + *(iVar93 + 0x28 + *(iVar134 + 0x3c))))()` (Used as the "hand-off" point for the final payload).
*   **Obfuscation Technique:** Use of extensive junk code and malformed jump tables within standard library wrappers (e.g., `hims12_`, `moneypunct_`) to hinder automated decompiler analysis.

---

## Malware Family Classification

Based on the provided technical analysis, here is the classification of the sample:

**1. Malware family:** custom
**2. Malware type:** loader
**3. Confidence:** High (for Type) / Medium (for Family)

**4. Key evidence:**
*   **Multi-Stage Decryption & VM Architecture:** The sample utilizes a complex, custom Virtual Machine (VM) to hide its control flow and a sophisticated bitwise decryption pipeline (XOR, shifts, and additions) to process large data blocks ($0x4b210$ bytes). This indicates a high level of engineering common in APT-grade tools.
*   **Intentional Decompiler Sabotage:** The use of "junk" code, malformed jump tables, and the wrapping of malicious logic inside standard C++ library functions (like `std::stringstream`) demonstrates a proactive effort to thwart automated analysis and manual reverse engineering.
*   **Environmental Gatekeeping & Hand-off:** The inclusion of reconnaissance APIs (`NetWkstaGetInfo`, `EnumPrintersA`) suggests "anti-analysis" checks where the loader only proceeds to the final indirect call (the payload "hand-off") if the environment is deemed a valid target.
