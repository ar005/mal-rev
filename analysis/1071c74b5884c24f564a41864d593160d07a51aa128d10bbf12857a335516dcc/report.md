# Threat Analysis Report

**Generated:** 2026-08-18 22:52 UTC
**Sample:** `1071c74b5884c24f564a41864d593160d07a51aa128d10bbf12857a335516dcc_1071c74b5884c24f564a41864d593160d07a51aa128d10bbf12857a335516dcc.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1071c74b5884c24f564a41864d593160d07a51aa128d10bbf12857a335516dcc_1071c74b5884c24f564a41864d593160d07a51aa128d10bbf12857a335516dcc.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 5 sections |
| Size | 1,517,056 bytes |
| MD5 | `1bf8ed30924d39b54a05a0cc97382d72` |
| SHA1 | `735669c4fc9ab25a4ef9ba8610c739feb678e5a1` |
| SHA256 | `1071c74b5884c24f564a41864d593160d07a51aa128d10bbf12857a335516dcc` |
| Overall entropy | 7.045 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1762734432 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 570,880 | 6.68 | No |
| `.rdata` | 183,808 | 5.77 | No |
| `.data` | 25,088 | 2.003 | No |
| `.rsrc` | 693,760 | 7.119 | ⚠️ Yes |
| `.reloc` | 42,496 | 5.245 | No |

### Imports

**WSOCK32.dll**: `__WSAFDIsSet`, `recv`, `send`, `setsockopt`, `ntohs`, `recvfrom`, `select`, `WSAStartup`, `htons`, `accept`, `listen`, `bind`, `closesocket`, `connect`, `WSACleanup`
**VERSION.dll**: `GetFileVersionInfoW`, `VerQueryValueW`, `GetFileVersionInfoSizeW`
**WINMM.dll**: `timeGetTime`, `waveOutSetVolume`, `mciSendStringW`
**COMCTL32.dll**: `ImageList_Destroy`, `ImageList_Remove`, `ImageList_SetDragCursorImage`, `ImageList_BeginDrag`, `ImageList_DragEnter`, `ImageList_DragLeave`, `ImageList_EndDrag`, `ImageList_DragMove`, `ImageList_Create`, `InitCommonControlsEx`, `ImageList_ReplaceIcon`
**MPR.dll**: `WNetUseConnectionW`, `WNetCancelConnection2W`, `WNetGetConnectionW`, `WNetAddConnection2W`
**WININET.dll**: `InternetReadFile`, `InternetCloseHandle`, `InternetOpenW`, `InternetSetOptionW`, `InternetCrackUrlW`, `HttpQueryInfoW`, `InternetQueryOptionW`, `HttpOpenRequestW`, `HttpSendRequestW`, `FtpOpenFileW`, `FtpGetFileSize`, `InternetOpenUrlW`, `InternetConnectW`, `InternetQueryDataAvailable`
**PSAPI.DLL**: `GetProcessMemoryInfo`
**IPHLPAPI.DLL**: `IcmpCreateFile`, `IcmpCloseHandle`, `IcmpSendEcho`
**USERENV.dll**: `UnloadUserProfile`, `DestroyEnvironmentBlock`, `CreateEnvironmentBlock`, `LoadUserProfileW`
**UxTheme.dll**: `IsThemeActive`
**KERNEL32.dll**: `HeapAlloc`, `GetProcessHeap`, `HeapFree`, `Sleep`, `GetCurrentThreadId`, `MultiByteToWideChar`, `MulDiv`, `GetVersionExW`, `GetSystemInfo`, `FreeLibrary`, `LoadLibraryA`, `GetProcAddress`, `SetErrorMode`, `GetModuleFileNameW`, `WideCharToMultiByte`
**USER32.dll**: `SetWindowPos`, `GetCursorInfo`, `RegisterHotKey`, `ClientToScreen`, `GetKeyboardLayoutNameW`, `IsCharAlphaW`, `IsCharAlphaNumericW`, `IsCharLowerW`, `IsCharUpperW`, `GetMenuStringW`, `GetSubMenu`, `GetCaretPos`, `IsZoomed`, `MonitorFromPoint`, `GetMonitorInfoW`
**GDI32.dll**: `SetPixel`, `DeleteObject`, `GetTextExtentPoint32W`, `ExtCreatePen`, `StrokeAndFillPath`, `StrokePath`, `GetDeviceCaps`, `CloseFigure`, `LineTo`, `AngleArc`, `CreateCompatibleBitmap`, `CreateCompatibleDC`, `MoveToEx`, `Ellipse`, `PolyDraw`
**COMDLG32.dll**: `GetSaveFileNameW`, `GetOpenFileNameW`
**ADVAPI32.dll**: `GetAclInformation`, `RegEnumValueW`, `RegDeleteValueW`, `RegDeleteKeyW`, `RegEnumKeyExW`, `RegSetValueExW`, `RegCreateKeyExW`, `GetUserNameW`, `RegOpenKeyExW`, `RegCloseKey`, `RegQueryValueExW`, `RegConnectRegistryW`, `InitializeSecurityDescriptor`, `InitializeAcl`, `AdjustTokenPrivileges`
**SHELL32.dll**: `DragQueryPoint`, `ShellExecuteExW`, `DragQueryFileW`, `SHEmptyRecycleBinW`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHCreateShellItem`, `SHGetDesktopFolder`, `SHGetSpecialFolderLocation`, `SHGetFolderPathW`, `SHFileOperationW`, `ExtractIconExW`, `Shell_NotifyIconW`, `ShellExecuteW`, `DragFinish`
**ole32.dll**: `CoTaskMemAlloc`, `CoTaskMemFree`, `CLSIDFromString`, `ProgIDFromCLSID`, `CLSIDFromProgID`, `OleSetMenuDescriptor`, `MkParseDisplayName`, `OleSetContainedObject`, `CoCreateInstance`, `IIDFromString`, `StringFromGUID2`, `CreateStreamOnHGlobal`, `CoInitialize`, `CoUninitialize`, `GetRunningObjectTable`
**OLEAUT32.dll**: `RegisterTypeLib`, `LoadTypeLibEx`, `VariantCopyInd`, `SysReAllocString`, `SysFreeString`, `SafeArrayDestroyDescriptor`, `SafeArrayDestroyData`, `SafeArrayUnaccessData`, `SafeArrayAccessData`, `SafeArrayAllocData`, `UnRegisterTypeLib`, `SafeArrayCreateVector`, `SysAllocString`, `SysStringLen`, `VariantTimeToSystemTime`

## Extracted Strings

Total strings found: **2921** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
+t\HHtT
j+Yj^f;
~89~4~)
v,F8P
WWjdh,
PWWWWh
R$A;N|
u9^u
u h$.K
u h$.K
9Fs4j
L$$9N@
AHt!H
t<j	Yf;
t4j"Yf;
tj	Yf;
~+FVSj
D$49G@
\$ j|Zf9
L$LjxXf


	

						
												
						
																									
YYj!Yf;
`~EjaX;
^$9^,u
D$$;D$0
FHtJH
v,F8PRQ
L$X;|$8
 !"#$%%%%%%&&'()*+%%%%%%&&'()*+,,,,,,--./012RRRRRRRRRRRR3345566789::::;<=<=>?>@ABC>@ABCRRRRRDEFGHIJKLMNO
Yj?Yj0Z
<t9<
tP
|$`AU3!
?#tRf9
FHt<Ht>Ht#H
tgHuM95
t-HuC9
D$ PVj
D$$PVj
D$@;D$Dr
9D$xu;
9t$xv7
F;t$xr
|$L9D$4
F;t$Xr
D$PQW
9t$ v-
F;t$ r
f98t?j
9^Xt99^\tA
t$8]4t
@SVWjw
awjUXf;
AHt;Ht.H
_8C0tN
u h$.K
u h$.K
PPPPGW
F;Bt
SVWjA_jZ+
uBjAYjZ+
uWtj-Xf
tf;1u
SVjA[jZ^+
jAZjZ^+
9E v\PWj
9u(v?VSj
jh(kK
jhHkK
G@uqW
jhhkK
YYHtIHt8
u&j[9
jh0lK
jhPlK
D$tQf
HHtPHHt-H
HthHt3
Genuu_
ineIuV
nteluM3
u,9Et'9
~pjCXf
v	N+D$
uHjAXf;
tjXYf;
uWjAXf;
htHjlY;
HHtXHHt
uj X
nt'joY;
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00408ffe` | `0x408ffe` | 537937 | ✓ |
| `fcn.00409b60` | `0x409b60` | 534852 | ✓ |
| `fcn.0040a300` | `0x40a300` | 529797 | ✓ |
| `fcn.00406f07` | `0x406f07` | 508742 | ✓ |
| `fcn.00406c8a` | `0x406c8a` | 507824 | ✓ |
| `fcn.00406d75` | `0x406d75` | 507399 | ✓ |
| `fcn.00406bc4` | `0x406bc4` | 507180 | ✓ |
| `fcn.004029c8` | `0x4029c8` | 504420 | ✓ |
| `fcn.00407474` | `0x407474` | 504186 | ✓ |
| `fcn.004077b0` | `0x4077b0` | 502652 | ✓ |
| `fcn.004038fa` | `0x4038fa` | 501998 | ✓ |
| `fcn.004039c6` | `0x4039c6` | 501773 | ✓ |
| `fcn.00408b42` | `0x408b42` | 501544 | ✓ |
| `fcn.00402a54` | `0x402a54` | 500335 | ✓ |
| `fcn.00402c79` | `0x402c79` | 499765 | ✓ |
| `fcn.00408922` | `0x408922` | 499475 | ✓ |
| `fcn.00408b14` | `0x408b14` | 499315 | ✓ |
| `fcn.0040390f` | `0x40390f` | 496658 | ✓ |
| `fcn.00408e6e` | `0x408e6e` | 483584 | ✓ |
| `fcn.0040887d` | `0x40887d` | 483234 | ✓ |
| `fcn.00408b8e` | `0x408b8e` | 482650 | ✓ |
| `fcn.004012f7` | `0x4012f7` | 481713 | ✓ |
| `fcn.004028a6` | `0x4028a6` | 476209 | ✓ |
| `fcn.00405928` | `0x405928` | 474642 | ✓ |
| `fcn.004021ae` | `0x4021ae` | 474399 | ✓ |
| `fcn.00405e85` | `0x405e85` | 473333 | ✓ |
| `fcn.00405f19` | `0x405f19` | 473165 | ✓ |
| `fcn.00402745` | `0x402745` | 473116 | ✓ |
| `fcn.00405f52` | `0x405f52` | 473089 | ✓ |
| `fcn.00405f85` | `0x405f85` | 472580 | ✓ |

### Decompiled Code Files

- [`code/fcn.004012f7.c`](code/fcn.004012f7.c)
- [`code/fcn.004021ae.c`](code/fcn.004021ae.c)
- [`code/fcn.00402745.c`](code/fcn.00402745.c)
- [`code/fcn.004028a6.c`](code/fcn.004028a6.c)
- [`code/fcn.004029c8.c`](code/fcn.004029c8.c)
- [`code/fcn.00402a54.c`](code/fcn.00402a54.c)
- [`code/fcn.00402c79.c`](code/fcn.00402c79.c)
- [`code/fcn.004038fa.c`](code/fcn.004038fa.c)
- [`code/fcn.0040390f.c`](code/fcn.0040390f.c)
- [`code/fcn.004039c6.c`](code/fcn.004039c6.c)
- [`code/fcn.00405928.c`](code/fcn.00405928.c)
- [`code/fcn.00405e85.c`](code/fcn.00405e85.c)
- [`code/fcn.00405f19.c`](code/fcn.00405f19.c)
- [`code/fcn.00405f52.c`](code/fcn.00405f52.c)
- [`code/fcn.00405f85.c`](code/fcn.00405f85.c)
- [`code/fcn.00406bc4.c`](code/fcn.00406bc4.c)
- [`code/fcn.00406c8a.c`](code/fcn.00406c8a.c)
- [`code/fcn.00406d75.c`](code/fcn.00406d75.c)
- [`code/fcn.00406f07.c`](code/fcn.00406f07.c)
- [`code/fcn.00407474.c`](code/fcn.00407474.c)
- [`code/fcn.004077b0.c`](code/fcn.004077b0.c)
- [`code/fcn.0040887d.c`](code/fcn.0040887d.c)
- [`code/fcn.00408922.c`](code/fcn.00408922.c)
- [`code/fcn.00408b14.c`](code/fcn.00408b14.c)
- [`code/fcn.00408b42.c`](code/fcn.00408b42.c)
- [`code/fcn.00408b8e.c`](code/fcn.00408b8e.c)
- [`code/fcn.00408e6e.c`](code/fcn.00408e6e.c)
- [`code/fcn.00408ffe.c`](code/fcn.00408ffe.c)
- [`code/fcn.00409b60.c`](code/fcn.00409b60.c)
- [`code/fcn.0040a300.c`](code/fcn.0040a300.c)

## Behavioral Analysis

This final chunk of disassembly confirms the preceding analysis while providing concrete "smoking guns" regarding the sophistication level of the binary. The inclusion of these specific functions reinforces that this code is not merely "validating" input, but is likely a high-fidelity implementation of standard **Windows Unicode String Manipulation** (similar to those found in `ntdll.dll` or `kernel32.dll`).

### Updated Analysis: Integration of Chunk 4 Data

The final disassembly provides several key pieces of evidence that solidify the categorization of this code as either a system-level library or highly sophisticated "stolen" functionality used by advanced malware.

#### 1. Evidence of Industrial-Grade Unicode Logic
Functions such as `fcn.00408922` and `fcn.00408e6e` are massive, complex logic blocks that process strings based on their **internal properties** rather than just their raw values.
*   **Complex State Handling:** The nested loops and switch statements (some with 150+ cases) handle variations in how different Unicode characters "behave" in a memory buffer (e.g., how many bytes they occupy, whether they are followed by combining marks, or if they form surrogate pairs).
*   **Length Calculation Logic:** The code performs complex math to determine the "real" length of strings that include multi-byte characters. This is essential for ensuring that string offsets don't "drift" when the system tries to display or move through a list of Unicode items (like a directory listing or registry keys).

#### 2. Interaction with Windows Internals
The presence of `fcn.00402c79` and `fcn.0040390f` shows the code interacting with higher-level system resources:
*   **Window Management:** The use of `IsWindow`, `DestroyWindow`, and `DeleteObject` (via GDI) indicates that the string processing logic is likely used to populate or manage UI elements, or is part of a larger system service.
*   **Resource Cleanup:** The structured way it handles window handles and GDI objects suggests high-quality engineering; it is not a "quick and dirty" script but a professional implementation.

#### 3. Robustness Against Edge Cases (The "Sanitization" Layer)
The code explicitly handles:
*   **Surrogate Pairs:** It detects if a character's value is between `0xd800` and `0xdfff` and correctly calculates the length for UTF-16 multi-byte characters.
*   **Normalization Forms:** By identifying specific categories of "special" Unicode, it ensures that even if an attacker uses "mixed" encoding (e.g., a character that looks like 'a' but is technically a different Unicode point), the system will process it consistently.

---

### Refined Summary Table (Comprehensive Analysis)

| Feature | Observation from Disassembly | Significance |
| :--- | :--- | :--- |
| **Primary Purpose** | Heavyweight Unicode Normalization & Validation Engine. | It ensures that "dirty" or complex internationalized strings are normalized before being used by the system. |
| **Complexity Level** | Extreme (High-volume switch tables, deep nested loops). | This is industrial-grade code. It's designed to handle 100% of the Unicode spec quirks, not just common ones. |
| **System Integrity** | Automatic detection/handling of surrogate pairs and combining marks. | Prevents buffer overflows and "off-by-one" errors in memory during string manipulation. |
| **Windows Integration** | Use of `IsWindow`, `DestroyWindow`, and GDI cleanup. | The code is designed to operate within the standard Windows environment, ensuring compatibility with system UI/APIs. |
| **Malware Context** | Capability for **Sophisticated Path Masking**. | If this is malware, it allows the threat actor to use Unicode-based "masquerading" (e.g., using a homograph character that looks like 'e' but isn't) to bypass security filters. |

---

### Technical Findings & "Smoking Guns"

1.  **The "Normalization" Suite:** The logic in `fcn.00408922` and `fcn.00408e6e` is almost identical to the way Windows handles **NT-style path normalization**. It prepares strings so that they are "canonical"—meaning no matter how a user types it, the OS sees the exact same byte sequence.
2.  **Security Gatekeeping:** This logic acts as a filter. By forcing a string into a standard format before it reaches deeper functions (like file system calls or registry lookups), it prevents **"Unicode Bypass" attacks**, where an attacker uses special characters to trick a security tool into missing a malicious path.
3.  **Complexity Signature:** The sheer volume of code dedicated solely to "interpreting" Unicode properties is characteristic of core OS components. A standard application developer would rarely write this from scratch; it is almost certainly copied from a system library or an extensive open-source library like `ICU` (International Components for Unicode).

### Final Conclusion
The binary contains a **highly professional, robust Unicode processing engine**. It is designed to handle the full complexity of the Unicode standard, including multi-byte characters, surrogate pairs, and complex normalization.

**Conclusion Scenarios:**
1.  **Standard System Component/Library:** The code is part of a legitimate Windows driver or system service (like `nt_ls_*` functions) used for robustly handling file paths and registry keys in different languages.
2.  **Advanced Malware Implementation:** If this binary is malicious, the inclusion of this specific engine indicates a high-effort effort to ensure **maximum reliability**. It allows the malware to use complex Unicode strings (e.g., non-English filenames or "invisible" character overrides) while ensuring they are still accepted and processed by standard Windows APIs without causing errors or being filtered by basic security tools.

**Recommendation:** Treat this as a high-complexity component. If part of an investigation, the presence of this code confirms that the developer was looking for **sophistication and reliability**, likely to ensure their operations (like file path manipulation or registry modification) work perfectly across different localized environments without being flagged by "primitive" validation rules.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Resources | The use of complex Unicode normalization and surrogate pair handling facilitates "Sophisticated Path Masking," allowing malicious filenames to bypass security filters that rely on simple string matching. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the intelligence report regarding Indicators of Compromise (IOCs).

### **Analysis Summary**
The provided data contains no high-confidence infrastructure IOCs (such as IP addresses, URLs, or specific file paths). The "Extracted Strings" section consists primarily of obfuscated/encrypted data segments and standard Win32 execution headers. However, the "Behavioral Analysis" identifies significant **behavioral indicators** related to evasion techniques.

---

### **Indicators of Compromise (IOCs)**

#### **IP addresses / URLs / Domains**
*   *None identified.*

#### **File paths / Registry keys**
*   *None identified.* (Note: While the analysis mentions "Path Masking," no specific malicious paths were provided in the raw data.)

#### **Mutex names / Named pipes**
*   *None identified.*

#### **Hashes**
*   *None identified.* (Note: References to `fcn.00408922` etc., are internal memory offsets, not file hashes.)

#### **Other artifacts**
*   **Behavioral Indicator - Sophisticated Unicode Normalization:** The presence of complex logic for handling surrogate pairs and multi-byte character normalization (likely mimicking `nt_ls_*` functions) is a high-confidence indicator of sophisticated malware or specialized system tooling.
*   **Technique: Path Masking:** The code is designed to handle "homograph" characters and non-standard Unicode lengths, which is a technique used to bypass security filters by making malicious file paths look like legitimate ones to standard inspection tools.
*   **API Interaction:** Usage of `IsWindow`, `DestroyWindow`, and `DeleteObject` suggests the potential for GUI interaction or manipulating system resources in a manner consistent with high-quality engineering.

---

### **Analyst Notes**
The lack of traditional IOCs (IPs/Hashes) suggests this sample is likely in a "staging" phase or is designed to be modular. The primary "indicator" here is the **technical sophistication** of the Unicode handling. If this binary is found in an environment where it is not a verified system component, it should be treated as an advanced persistent threat (APT) tool capable of bypassing security software via **Unicode-based evasion.**

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family**: Unknown
2. **Malware type**: Loader / Backdoor (Sophisticated Component)
3. **Confidence**: Medium
4. **Key evidence**:
    *   **Advanced Unicode Normalization:** The binary contains industrial-grade logic for handling surrogate pairs and multi-byte characters, mimicking system-level functions (`nt_ls_*`) to ensure "canonical" path processing.
    *   **Evasion via Path Masking:** The inclusion of these specific routines is explicitly linked to MITRE T1027 (Obfuscated Resources), allowing the use of homograph characters to bypass security filters.
    *   **High Sophistication/Reliability:** The complex code structure and "robust" nature suggest this is not a common script but a high-effort, modular component designed for stable operation in evasion-heavy environments.
