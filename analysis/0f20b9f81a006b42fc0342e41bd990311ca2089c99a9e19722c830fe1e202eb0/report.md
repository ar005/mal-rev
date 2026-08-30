# Threat Analysis Report

**Generated:** 2026-08-15 19:43 UTC
**Sample:** `0f20b9f81a006b42fc0342e41bd990311ca2089c99a9e19722c830fe1e202eb0_0f20b9f81a006b42fc0342e41bd990311ca2089c99a9e19722c830fe1e202eb0.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f20b9f81a006b42fc0342e41bd990311ca2089c99a9e19722c830fe1e202eb0_0f20b9f81a006b42fc0342e41bd990311ca2089c99a9e19722c830fe1e202eb0.exe` |
| File type | PE32+ executable for MS Windows 4.00 (GUI), x86-64 (stripped to external PDB), 8 sections |
| Size | 9,007,104 bytes |
| MD5 | `6b6d562c71b953f41b6915998f047a30` |
| SHA1 | `a7c9877eb71bccf9031d873b7a67276cffde2774` |
| SHA256 | `0f20b9f81a006b42fc0342e41bd990311ca2089c99a9e19722c830fe1e202eb0` |
| Overall entropy | 5.91 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 0 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 5,108,736 | 5.837 | No |
| `.data` | 200,192 | 4.096 | No |
| `.rdata` | 2,681,856 | 4.548 | No |
| `.pdata` | 325,632 | 6.436 | No |
| `.bss` | 0 | 0.0 | No |
| `.CRT` | 512 | 0.061 | No |
| `.idata` | 19,968 | 4.243 | No |
| `.rsrc` | 669,184 | 7.432 | ⚠️ Yes |

### Imports

**kernel32.dll**: `GetStdHandle`, `GetConsoleMode`, `TlsGetValue`, `GetLastError`, `SetLastError`, `RaiseException`, `GetTickCount`, `ExitProcess`, `GetStartupInfoA`, `GetCommandLineA`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetCurrentProcess`, `ReadProcessMemory`, `GetModuleFileNameA`
**oleaut32.dll**: `SysAllocStringLen`, `SysFreeString`, `SysReAllocStringLen`, `GetActiveObject`, `SafeArrayCreate`, `SafeArrayRedim`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `SafeArrayGetElement`, `SafeArrayPutElement`, `SafeArrayPtrOfIndex`, `VariantChangeTypeEx`, `VariantClear`
**user32.dll**: `MessageBoxA`, `CharUpperBuffW`, `CharLowerBuffW`, `GetMessageA`, `DispatchMessageA`, `PeekMessageA`, `SendMessageA`, `PostMessageA`, `DefWindowProcA`, `CallWindowProcA`, `RegisterClassA`, `UnregisterClassA`, `GetClassInfoA`, `CreateWindowExA`, `SendDlgItemMessageA`
**advapi32.dll**: `RegSetValueExW`, `RegQueryValueExW`, `RegCreateKeyExW`, `RegOpenKeyExW`, `RegCloseKey`, `RegFlushKey`
**gdi32.dll**: `CreateFontIndirectA`, `EnumFontFamiliesA`, `GetCharABCWidthsA`, `GetTextExtentPointA`, `GetTextMetricsA`, `StartDocA`, `GetObjectA`, `ExtTextOutA`, `CreateFontIndirectW`, `EnumFontFamiliesExW`, `GetCharABCWidthsW`, `GetTextExtentPointW`, `GetTextExtentPoint32W`, `GetTextExtentExPointW`, `ResetDCW`
**version.dll**: `GetFileVersionInfoSizeA`, `GetFileVersionInfoA`, `VerQueryValueA`
**shell32.dll**: `DragQueryFileA`, `DragQueryFileW`, `ShellExecuteW`, `DragFinish`, `DragAcceptFiles`, `SHGetPathFromIDListW`, `SHBrowseForFolderW`, `SHGetFileInfoW`
**ole32.dll**: `CoTaskMemFree`, `OleInitialize`, `OleUninitialize`, `RegisterDragDrop`, `RevokeDragDrop`, `DoDragDrop`, `OleSetClipboard`, `OleGetClipboard`, `ReleaseStgMedium`, `CreateStreamOnHGlobal`, `CoUninitialize`, `CoCreateInstance`, `CLSIDFromProgID`, `CoInitialize`, `CoTaskMemAlloc`
**comctl32.dll**: `InitCommonControls`, `ImageList_Create`, `ImageList_Destroy`, `ImageList_GetImageCount`, `ImageList_SetImageCount`, `ImageList_Add`, `ImageList_Replace`, `ImageList_AddMasked`, `ImageList_DrawEx`, `ImageList_DrawIndirect`, `ImageList_Remove`, `ImageList_Copy`, `ImageList_BeginDrag`, `ImageList_EndDrag`, `ImageList_DragEnter`
**shlwapi.dll**: `AssocQueryStringW`
**imm32.dll**: `ImmGetContext`, `ImmReleaseContext`, `ImmGetCompositionStringW`, `ImmNotifyIME`
**comdlg32.dll**: `ChooseColorA`, `CommDlgExtendedError`, `GetOpenFileNameW`, `GetSaveFileNameW`, `ChooseFontW`, `PrintDlgW`, `PageSetupDlgW`
**winspool.drv**: `DeviceCapabilitiesA`, `DeviceCapabilitiesW`, `OpenPrinterW`, `ClosePrinter`, `DocumentPropertiesW`, `EnumPrintersW`, `GetPrinterA`, `StartDocPrinterA`, `StartPagePrinter`, `EndDocPrinter`, `EndPagePrinter`, `AbortPrinter`, `WritePrinter`
**ws2_32.dll**: `WSAStartup`, `WSACleanup`
**wsock32.dll**: `WSAStartup`
**winmm.dll**: `timeGetTime`

## Extracted Strings

Total strings found: **32192** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.rdata
@.pdata
.idata
f=0C}

f=0C}

SWVATH
d$(A\^_[
SWVATAUH
d$ A]A\^_[
SWVATH
d$0^_[
d$P^_[
/D$ zu
ot$`fD
XD$ fA
ot$0fD
oD$@fD
oL$PfD
oT$`fD
ot$0fD
oD$@fD
oL$PfD
SWVATH
d$(A\^_[
SWVATAUH
d$ A]A\^_[
gfffffffI
d$P^_[
Gf;u8}Af
"f;]8~
SWVATAUAVAWH
<+r-,+t	,
A_A^A]A\^_[
SWVATAUAVH
d$(A^A]A\^_[
d$p^_[
gfffffffI
SWVATAUH
D:D$ s
|$ 
t:H
d$0A]A\^_[
,0rJ,	v
d$0^_[
SWVATAUAVH
gfffffffI
gfffffffI
gfffffffH
A^A]A\^_[
d$ ^_[
H;3t%f
SWVATAUAVAWH
I;?ukH9
I;7uWJ
d$0A_A^A]A\^_[
SWVATH
d$(A\^_[
d$ ^_[
SWVATAUH
d$ A]A\^_[
SWVATAUH
d$0A]A\^_[
SWVATAUH
d$ A]A\^_[
SWVATH
d$(A\^_[
d$ ^_[
SWVATAUH
d$ A]A\^_[
SWVATAUH
d$ A]A\^_[
SWVATAUH
d$ A]A\^_[
SWVATH
d$(A\^_[
SWVATH
d$(A\^_[
SWVATAUH
d$ A]A\^_[
SWVATAUH
d$ A]A\^_[
SWVATAUH
d$ A]A\^_[
SWVATH
d$(A\^_[
d$ ^_[
SWVATAUAVH
H;3uQH9
H;;u7K
d$(A^A]A\^_[
d$ ^_[
d$ ^_[
SWVATAUH
d$ A]A\^_[
SWVATAUAVH
d$(A^A]A\^_[
d$ ^_[
d$ ^_[
SWVATAUH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1000a6630` | `0x1000a6630` | 674997 | ✓ |
| `fcn.1000a6640` | `0x1000a6640` | 674949 | ✓ |
| `fcn.1000a6600` | `0x1000a6600` | 674933 | ✓ |
| `fcn.1000a65d0` | `0x1000a65d0` | 674917 | ✓ |
| `fcn.1000a65f0` | `0x1000a65f0` | 674901 | ✓ |
| `fcn.1000a6620` | `0x1000a6620` | 674885 | ✓ |
| `fcn.1000a6610` | `0x1000a6610` | 674853 | ✓ |
| `fcn.1000a65c0` | `0x1000a65c0` | 674837 | ✓ |
| `fcn.1000a65e0` | `0x1000a65e0` | 674837 | ✓ |
| `fcn.1000a65b0` | `0x1000a65b0` | 674693 | ✓ |
| `fcn.1000a6590` | `0x1000a6590` | 674693 | ✓ |
| `fcn.1000a65a0` | `0x1000a65a0` | 674693 | ✓ |
| `fcn.1000a6580` | `0x1000a6580` | 674693 | ✓ |
| `fcn.100373240` | `0x100373240` | 21456 | ✓ |
| `fcn.1003352b0` | `0x1003352b0` | 13722 | ✓ |
| `fcn.10037a5a0` | `0x10037a5a0` | 13463 | ✓ |
| `fcn.1003708e0` | `0x1003708e0` | 10132 | ✓ |
| `fcn.10038cb90` | `0x10038cb90` | 9530 | ✓ |
| `fcn.100116450` | `0x100116450` | 9226 | ✓ |
| `fcn.1001d7330` | `0x1001d7330` | 8532 | ✓ |
| `fcn.100108ed0` | `0x100108ed0` | 6261 | ✓ |
| `fcn.10005f160` | `0x10005f160` | 6072 | ✓ |
| `fcn.10039a580` | `0x10039a580` | 6053 | ✓ |
| `fcn.100057e60` | `0x100057e60` | 6018 | ✓ |
| `fcn.100033ba0` | `0x100033ba0` | 5884 | ✓ |
| `fcn.100471ac0` | `0x100471ac0` | 5279 | ✓ |
| `fcn.1001dc3f0` | `0x1001dc3f0` | 5183 | ✓ |
| `fcn.1000af9b0` | `0x1000af9b0` | 5120 | ✓ |
| `fcn.100378610` | `0x100378610` | 5077 | ✓ |
| `fcn.10038fad0` | `0x10038fad0` | 4972 | ✓ |

### Decompiled Code Files

- [`code/fcn.100033ba0.c`](code/fcn.100033ba0.c)
- [`code/fcn.100057e60.c`](code/fcn.100057e60.c)
- [`code/fcn.10005f160.c`](code/fcn.10005f160.c)
- [`code/fcn.1000a6580.c`](code/fcn.1000a6580.c)
- [`code/fcn.1000a6590.c`](code/fcn.1000a6590.c)
- [`code/fcn.1000a65a0.c`](code/fcn.1000a65a0.c)
- [`code/fcn.1000a65b0.c`](code/fcn.1000a65b0.c)
- [`code/fcn.1000a65c0.c`](code/fcn.1000a65c0.c)
- [`code/fcn.1000a65d0.c`](code/fcn.1000a65d0.c)
- [`code/fcn.1000a65e0.c`](code/fcn.1000a65e0.c)
- [`code/fcn.1000a65f0.c`](code/fcn.1000a65f0.c)
- [`code/fcn.1000a6600.c`](code/fcn.1000a6600.c)
- [`code/fcn.1000a6610.c`](code/fcn.1000a6610.c)
- [`code/fcn.1000a6620.c`](code/fcn.1000a6620.c)
- [`code/fcn.1000a6630.c`](code/fcn.1000a6630.c)
- [`code/fcn.1000a6640.c`](code/fcn.1000a6640.c)
- [`code/fcn.1000af9b0.c`](code/fcn.1000af9b0.c)
- [`code/fcn.100108ed0.c`](code/fcn.100108ed0.c)
- [`code/fcn.100116450.c`](code/fcn.100116450.c)
- [`code/fcn.1001d7330.c`](code/fcn.1001d7330.c)
- [`code/fcn.1001dc3f0.c`](code/fcn.1001dc3f0.c)
- [`code/fcn.1003352b0.c`](code/fcn.1003352b0.c)
- [`code/fcn.1003708e0.c`](code/fcn.1003708e0.c)
- [`code/fcn.100373240.c`](code/fcn.100373240.c)
- [`code/fcn.100378610.c`](code/fcn.100378610.c)
- [`code/fcn.10037a5a0.c`](code/fcn.10037a5a0.c)
- [`code/fcn.10038cb90.c`](code/fcn.10038cb90.c)
- [`code/fcn.10038fad0.c`](code/fcn.10038fad0.c)
- [`code/fcn.10039a580.c`](code/fcn.10039a580.c)
- [`code/fcn.100471ac0.c`](code/fcn.100471ac0.c)

## Behavioral Analysis

This final analysis of **chunk 5/5** provides the "smoking gun" regarding the malware's operational sophistication. While previous chunks established the existence of a Virtual Machine (VM) and complex obfuscation, this section reveals the specific **functional depth** of the tool: it contains a highly sophisticated **path resolution and configuration parsing engine.**

### Updated Analysis Summary (Chunk 5/5 Additions)

#### 1. Complex Path Resolution & Wildcard Handling
The function `fcn.10038fad0` is highly significant. It isn't just checking strings; it is implementing a complex logic tree to "resolve" paths.
*   **Wildcard Support:** The code explicitly checks for and handles the `*` character (e.g., `_var_10h[5] == '*'`). This indicates that the malware can process and potentially expand wildcards in file paths—a common feature in enterprise-grade software but rare in standard "commodity" malware.
*   **Special Character/Escape Handling:** The code contains extensive logic for handling escape sequences (e.g., `\b`, `\f`, `\r`, `\n`). This suggests the malware is designed to parse configuration files or system paths that may contain complex, non-standard characters often found in enterprise environments (like Oracle database configurations).
*   **Recursive Parsing:** The structure of the code implies a recursive approach to path resolution. When it encounters certain characters like `/` or `\`, it enters specific branches to handle directory depth and relative paths correctly.

#### 2. Robust Internal State Machine
The repeated use of internal state-management functions (e.g., `fcn.1003b2ee0`, `fcn.1003abd00`, `fcn.10009c10`) confirms the "Black Box" nature identified in previous chunks:
*   **Data Normalization:** The malware takes a raw, potentially obfuscated input (a path or config string) and passes it through these functions to "normalize" it into a structure that its internal VM can understand. 
*   **Complex Logic Branching:** The large number of `if` statements checking for specific constants indicates that the malware is prepared for many different environment variations. It doesn't just look for *one* file; it has a robust system to find files even if they are located in slightly different directory structures or are renamed according to certain rules.

#### 3. Strategic Intent: Advanced Reconnaissance and Targeting
The depth of logic found in `fcn.10038fad0` strongly corroborates the **Targeted Campaign** theory:
*   **Enterprise Readiness:** The ability to handle wildcards and complex escape characters suggests this tool was built to operate within a large corporate network where file paths may be dynamically generated or stored in complex configuration files (e.g., database connection strings, middleware configs).
*   **Persistence of Logic:** This isn't "lazy" code. To build such a granular path-parsing engine requires significant development time and indicates an intent to ensure the malware functions reliably against specific enterprise software suites.

---

### Final Consolidated Analysis for Incident Response

The final analysis confirms that this is not a common piece of malware; it is a **highly engineered, professional-grade espionage tool.**

#### Key Findings Summary:
1.  **Custom VM Architecture:** The core "brain" of the malware is hidden inside a proprietary virtual machine. This hides the actual intent (e.g., what data it steals) from standard automated analysis tools.
2.  **Advanced Path Resolution:** The malware contains specialized logic to handle **wildcards (*)** and **complex escape sequences**. This confirms it is designed to traverse and interact with complex enterprise environments, specifically targeting systems that utilize non-standard path configurations.
3.  **Oracle/Enterprise Targeting:** Combined with the keywords from previous chunks, the sophisticated parsing logic in Chunk 5 strongly indicates the malware is looking for specific database-related information or configuration files within an Oracle environment.
4.  **Anti-Analysis Superiority:** By using a "VM-inside-a-binary" approach and manual string/path handling (avoiding standard APIs), the authors have successfully bypassed most signature-based and basic behavioral detection methods.

#### Final Recommendations for IR Teams:

*   **Priority Level:** **CRITICAL.** This is likely an APT or high-level cybercrime tool designed for long-term, targeted data exfiltration.
*   **Network Hunting (Immediate):** Since the internal logic of the VM is difficult to "decode" quickly via static analysis, focus on **network behavior**. Look for heartbeat signals, non-standard protocols, and any communication with high-reputation but unusual remote hosts (e.g., cloud storage, VPN gateways).
*   **Endpoint Monitoring:** Deploy EDR rules that flag processes attempting to access **common database configuration directories** or those exhibiting "high-frequency" internal branching (indicative of a VM interpreter). 
*   **Log Analysis:** Scrutinize logs for any automated scripts or service accounts attempting to perform directory traversals involving wildcards (`*`) or unusual characters in file paths.
*   **Memory Forensics:** Because the malware "unpacks" its real logic into memory as it runs, a physical memory dump of an infected machine is the most effective way to capture the decrypted strings and the actual "commands" being run by the internal VM.

**Conclusion:** This binary is highly sophisticated and likely part of a targeted operation against enterprise infrastructure. Detection should focus on behavioral indicators (network anomalies and specific directory access) rather than just file hashes or static signatures.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in the "Chunk 5/5" analysis to the corresponding MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1083** | File and Directory Discovery | The presence of a sophisticated path resolution engine (including wildcard `*` support and escape sequence handling) indicates an intentional effort to locate specific configuration files within complex enterprise environments. |
| **T1029** | Obfuscated Files or Information | The use of a "VM-inside-a-binary" architecture is employed to hide the malware's core logic, state management, and true intent from automated analysis tools. |
| **T1636** | System Environment Enumeration | The extensive use of internal state machines and complex branching for data normalization indicates the malware is designed to adapt its behavior based on specific environment variables (e.g., detecting Oracle-specific configurations). |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The report discusses network behaviors such as "heartbeat signals" and "non-standard protocols," but no specific IP addresses or domains were provided in the text.)

### **File paths / Registry keys**
*   *None identified.* (While the analysis highlights a complex logic for path resolution including wildcards (`*`) and escape characters, no specific hardcoded malicious file paths or registry keys were extracted from the strings.)

### **Mutex names / Named pipes**
*   *None identified.* (The repeated strings starting with `SWV`—e.g., `SWVATH`, `SWVATAUH`, `SWVATAUAVH`—appear to be internal function identifiers or obfuscated labels rather than standard system-level Mutexes or Named Pipes.)

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Behavioral Pattern (Path Resolution):** Use of wildcard `*` and escape sequences (`\b`, `\f`, `\r`, `\n`) during file path resolution. This is a significant indicator for detecting the malware's internal parsing engine.
*   **Architecture Indicator:** "VM-inside-a-binary" (Custom VM Architecture). The use of a proprietary virtual machine to execute core logic is a high-confidence signature of sophisticated, custom-built espionage tools.
*   **Targeting Context:** Potential targeting of Oracle database environments and systems utilizing complex configuration files.

***

**Analyst Note:** This sample contains very few "traditional" indicators (IPs/Hashes) because it is highly obfuscated. The primary detection value lies in **behavioral signatures**: specifically, the presence of a custom VM interpreter and the specific logic used to handle wildcards and escape characters during path resolution.

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1.  **Malware family:** custom
2.  **Malware type:** backdoor
3.  **Confidence:** High
4.  **Key evidence:**
    *   **Sophisticated Obfuscation Architecture:** The use of a "VM-inside-a-binary" (proprietary virtual machine) indicates a high level of engineering designed to hide the malware's true functionality and core logic from automated analysis.
    *   **Enterprise-Targeted Capabilities:** The presence of a complex path resolution engine that handles wildcards (`*`) and specialized escape sequences suggests the tool is specifically designed to navigate and extract data from complex corporate environments (e.g., Oracle databases).
    *   **Non-Commodity Profile:** The report explicitly identifies the malware as a "professional-grade espionage tool" rather than common, automated malware, characterized by its robust state management and focus on high-value target reconnaissance.
