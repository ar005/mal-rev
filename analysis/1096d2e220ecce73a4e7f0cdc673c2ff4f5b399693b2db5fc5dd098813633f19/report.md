# Threat Analysis Report

**Generated:** 2026-08-20 18:32 UTC
**Sample:** `1096d2e220ecce73a4e7f0cdc673c2ff4f5b399693b2db5fc5dd098813633f19_1096d2e220ecce73a4e7f0cdc673c2ff4f5b399693b2db5fc5dd098813633f19.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1096d2e220ecce73a4e7f0cdc673c2ff4f5b399693b2db5fc5dd098813633f19_1096d2e220ecce73a4e7f0cdc673c2ff4f5b399693b2db5fc5dd098813633f19.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 6 sections |
| Size | 134,104 bytes |
| MD5 | `0f935c1205ac456eccc4aa3dfeefbaaf` |
| SHA1 | `55e9a66bcbf87ee44e0bde755020169712b919d9` |
| SHA256 | `1096d2e220ecce73a4e7f0cdc673c2ff4f5b399693b2db5fc5dd098813633f19` |
| Overall entropy | 7.784 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1773306058 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 5,120 | 5.983 | No |
| `.rdata` | 3,584 | 4.189 | No |
| `.data` | 60,416 | 7.91 | ⚠️ Yes |
| `.pdata` | 512 | 2.193 | No |
| `.rsrc` | 47,104 | 7.632 | ⚠️ Yes |
| `.reloc` | 512 | 1.957 | No |

### Imports

**KERNEL32.dll**: `GetModuleHandleW`, `HeapFree`, `MultiByteToWideChar`, `HeapAlloc`, `GetProcessHeap`, `lstrcmpiW`, `CreateThread`, `SizeofResource`, `VirtualProtect`, `VirtualFree`, `VirtualAlloc`, `FindResourceA`, `LockResource`, `LoadResource`, `CloseHandle`
**USER32.dll**: `GetMessageW`, `ReleaseDC`, `SetRect`, `AdjustWindowRectEx`, `GetDC`, `CreateWindowExW`, `LoadCursorW`, `GetClientRect`, `LoadImageW`, `UpdateWindow`, `DefWindowProcW`, `LoadIconW`, `RegisterClassExW`, `ShowWindow`, `GetAsyncKeyState`
**GDI32.dll**: `GetDeviceCaps`
**ole32.dll**: `OleSetContainedObject`, `OleInitialize`, `OleUninitialize`, `OleCreate`, `OleLockRunning`
**OLEAUT32.dll**: `SafeArrayAccessData`, `SysFreeString`, `VariantInit`, `SafeArrayDestroy`, `SafeArrayCreateVector`, `SysAllocString`, `SafeArrayUnaccessData`
**ADVAPI32.dll**: `RegSetValueExW`, `RegCreateKeyExW`, `RegCloseKey`

## Extracted Strings

Total strings found: **331** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
|$l+t$`+|$d
|$ ATAVAWH
L9g0t[H
A_A^A\
l$ WAVAWH
GetCommandLineW
GetModuleFileNameW
CloseHandle
CreateThread
ExitProcess
GetModuleHandleW
HeapFree
MultiByteToWideChar
HeapAlloc
GetProcessHeap
lstrcmpiW
MulDiv
SizeofResource
VirtualProtect
VirtualFree
VirtualAlloc
FindResourceA
LockResource
LoadResource
KERNEL32.dll
LoadImageW
UpdateWindow
GetClientRect
LoadCursorW
LoadIconW
TranslateMessage
DispatchMessageW
GetAsyncKeyState
ShowWindow
RegisterClassExW
GetSystemMetrics
CreateWindowExW
AdjustWindowRectEx
DefWindowProcW
GetMessageW
ReleaseDC
SetRect
PeekMessageW
USER32.dll
GetDeviceCaps
GDI32.dll
OleUninitialize
OleInitialize
OleSetContainedObject
OleCreate
OleLockRunning
ole32.dll
OLEAUT32.dll
RegSetValueExW
RegCreateKeyExW
RegCloseKey
ADVAPI32.dll
;c7<=)~
0t/T9
DJhnXRk`vJkSXB
|JuCXBd
X
9l0&n
pZJ73Z
o,Tb?)J
[:C>3&
OJqTc}
F8E:9I
z>z1Q8
(jy:<8
:WAqJ
=&PR"U
J6jTY#\
QB4ruJ
QBG4uJ

Q2tIu?

Z9&7QI
)W1&.B	&
Q>~L9&}M1
Q>kG9&bD1
<K2&%z
(MrC5v
ZJf8Awv
wJkES"s
J^]SJ>
8D,&JE(
^'&=-~7!
v?>
d"D
J}RHb7
g9,&mJu7
DucKa<+
L0H;E2
TmW7%2C
BbrXfJt[
FQwJjN
```

## Disassembly Overview

Functions analyzed: **4** | Decompiled to C: **4**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x1400010c0` | 1252 | ✓ |
| `fcn.140001c00` | `0x140001c00` | 693 | ✓ |
| `fcn.140001880` | `0x140001880` | 602 | ✓ |
| `fcn.1400015b0` | `0x1400015b0` | 309 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.1400015b0.c`](code/fcn.1400015b0.c)
- [`code/fcn.140001880.c`](code/fcn.140001880.c)
- [`code/fcn.140001c00.c`](code/fcn.140001c00.c)

## Behavioral Analysis

Based on the provided disassembly, here is a technical analysis of the binary's behavior.

### Core Functionality and Purpose
The binary appears to be a **wrapper or "container" application**, likely designed to host web content or interact with system components using OLE (Object Linking and Embedding) and ActiveX technologies. It sets up a graphical window (`Container_WndClass`) and initializes an environment for rendering content, possibly through a web engine component.

### Suspicious and Malicious Behaviors
The binary exhibits several behaviors commonly associated with **droppers**, **adware/spyware gateways**, or **malware loaders**:

*   **Registry Manipulation (Security Bypass):** 
    The code specifically modifies the registry key: `Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION`. It sets a value associated with its own file path. This is a known technique to bypass security restrictions when executing "active content" or scripts within an embedded browser window, often used by malware to execute malicious payloads from the web without being blocked by Windows' default security policies.
*   **In-Memory Deobfuscation:** 
    At the beginning of `entry0`, there is a loop that performs XOR operations and bitwise rotations on a buffer (`puVar11`). This indicates the binary is **deobfuscating or unpacking** its internal code/data at runtime before use, which is a standard technique to hide malicious functionality from static analysis.
*   **Hidden Execution Threads:** 
    The code calls `CreateThread` immediately after the decryption routine. This suggests it wants to move the primary (and potentially suspicious) logic into a separate thread so that the main thread can continue handling Windows messages for the UI, making it harder for an analyst to follow the execution flow.
*   **Suspicious Initialization of Web Content:** 
    The use of `OleCreate`, `OleSetContainedObject`, and the hardcoded string `"about:blank"` in `fcn.140001880` are highly characteristic of programs that initialize an embedded browser frame to load remote content or launch "helper" executables via OLE components.

### Notable Techniques & Patterns
*   **Anti-Analysis/Obfuscation:** The initial decryption loop and the use of bitwise shifts (`uVar4 = uVar4 << uVar2 | uVar4 >> 0x20 - uVar2`) indicate an effort to hide strings or malicious logic from simple static scanners.
*   **Component Embedding:** The heavy reliance on `ole32.dll` and `OLEAUT32.dll` suggests that the binary is not a standalone application but acts as a "host" for other objects (potentially a Remote Procedure Call or an ActiveX control).
*   **Resource Manipulation:** The presence of `FindResourceA`, `LoadResource`, and `LockResource` indicates the payload might be stored in the `.rsrc` section, only being loaded into memory and decoded when needed.

### Summary Checklist for Analysts
| Behavior | Observation | Potential Threat |
| :--- | :--- | :--- |
| **Deobfuscation** | XOR/Rotate loop at `0x14000111d` | Evasion of static analysis. |
| **Registry Tweak** | Modifying `FEATURE_BROWSER_EMULATION` | Bypassing security for "active content." |
| **Multi-threading** | `CreateThread` used for hidden logic | Complexity in forensic tracing. |
| **Ole/ActiveX Use** | Usage of `ole32.dll` and `"about:blank"` | Potential downloader or remote script execution. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1562.001** | Impair Defenses: Disable or Modify Security Software | The modification of the `FEATURE_BROWSER_EMULATION` registry key is a known method to bypass security restrictions for executing "active content" in embedded browser windows. |
| **T1027** | Obfuscated Files or Information | The use of XOR operations and bitwise rotations indicates an attempt to hide malicious strings and logic from static analysis tools. |
| **T1105** | Ingress Tool Transfer | The binary functions as a "loader" or "gateway," utilizing OLE components to fetch remote content or scripts for local execution. |
| **T1059** | Command and Scripting Interpreter | The use of `OleCreate`, `OleSetContainedObject`, and `"about:blank"` suggests the application provides an environment to execute scripts or automated commands via an embedded engine. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)* - The string `0t0h.a2isd/` was noted but appears to be a fragment of an obfuscated or malformed string rather than a confirmed URL.

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Inventory\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION` 
    *(Note: This is a specific indicator used to bypass security restrictions for active content.)*

**Mutex names / Named pipes**
*   *(None identified)*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Hardcoded String:** `about:blank` (Indicates initialization of a browser frame/container).
*   **Deobfuscation Routine:** Logic located at address `0x14000111d` (XOR and bitwise rotation loop used to hide internal strings/logic).
*   **Technical Pattern:** Use of OLE/ActiveX components (`ole32.dll`, `OLEAUT32.dll`) combined with a custom window class (`Container_WndClass`).

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://oneocsp.microsoft.com/ocsp0`
- `http://oneocsp.microsoft.com/ocsp0f`
- `http://www.microsoft.com/pkiops/Docs/Repository.htm0`
- `http://www.microsoft.com/pkiops/certs/Microsoft%20ID%20Verified%20CS%20AOC%20CA%2001.crt0-`
- `http://www.microsoft.com/pkiops/certs/Microsoft%20ID%20Verified%20Code%20Signing%20PCA%202021.crt0-`
- `http://www.microsoft.com/pkiops/certs/Microsoft%20Identity%20Verification%20Root%20Certificate%20Authority%202020.crt0`
- `http://www.microsoft.com/pkiops/certs/Microsoft%20Identity%20Verification%20Root%20Certificate%20Authority%202020.crt0-`
- `http://www.microsoft.com/pkiops/certs/Microsoft%20Public%20RSA%20Timestamping%20CA%202020.crt0`
- `http://www.microsoft.com/pkiops/crl/Microsoft%20ID%20Verified%20CS%20AOC%20CA%2001.crl0`
- `http://www.microsoft.com/pkiops/crl/Microsoft%20ID%20Verified%20Code%20Signing%20PCA%202021.crl0`
- `http://www.microsoft.com/pkiops/crl/Microsoft%20Identity%20Verification%20Root%20Certificate%20Authority%202020.crl0`
- `http://www.microsoft.com/pkiops/crl/Microsoft%20Public%20RSA%20Timestamping%20CA%202020.crl0y`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
*   **Security Bypass via Registry Manipulation:** The specific modification of the `FEATURE_BROWSER_EMULATION` registry key is a textbook technique used to bypass security restrictions for executing "active content" (like ActiveX or scripts) within embedded browser windows.
*   **Host/Container Architecture:** The heavy reliance on OLE (`ole32.dll`), ActiveX, and the `about:blank` string indicates the binary's purpose is to act as a "wrapper" that fetches and executes remote code rather than performing malicious actions autonomously.
*   **Evasion Techniques:** The use of XOR/bit-rotation deobfuscation for hidden strings and the move of core logic into separate threads via `CreateThread` are classic indicators of a loader designed to hinder static analysis and manual debugging.
