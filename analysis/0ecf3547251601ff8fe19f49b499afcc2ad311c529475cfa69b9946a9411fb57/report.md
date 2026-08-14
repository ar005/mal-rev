# Threat Analysis Report

**Generated:** 2026-08-14 00:37 UTC
**Sample:** `0ecf3547251601ff8fe19f49b499afcc2ad311c529475cfa69b9946a9411fb57_0ecf3547251601ff8fe19f49b499afcc2ad311c529475cfa69b9946a9411fb57.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ecf3547251601ff8fe19f49b499afcc2ad311c529475cfa69b9946a9411fb57_0ecf3547251601ff8fe19f49b499afcc2ad311c529475cfa69b9946a9411fb57.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 8 sections |
| Size | 2,701,824 bytes |
| MD5 | `42fe651f35fa6b16d280374f757d2817` |
| SHA1 | `078ed4a77beb863900b28035ac74d870e69d270e` |
| SHA256 | `0ecf3547251601ff8fe19f49b499afcc2ad311c529475cfa69b9946a9411fb57` |
| Overall entropy | 6.594 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 708992537 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `CODE` | 29,696 | 6.512 | No |
| `DATA` | 1,024 | 3.152 | No |
| `BSS` | 0 | 0.0 | No |
| `.idata` | 2,560 | 4.174 | No |
| `.tls` | 0 | 0.0 | No |
| `.rdata` | 512 | 0.207 | No |
| `.reloc` | 1,536 | 6.443 | No |
| `.rsrc` | 5,120 | 1.297 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WinExec`, `SetFilePointer`, `SetFileAttributesA`, `SetEndOfFile`, `SetCurrentDirectoryA`, `ReleaseMutex`, `ReadFile`, `GetWindowsDirectoryA`, `GetTempPathA`, `GetShortPathNameA`, `GetModuleFileNameA`, `GetLogicalDriveStringsA`, `GetLocalTime`, `GetLastError`
**user32.dll**: `ReleaseDC`, `GetSysColor`, `GetIconInfo`, `GetDC`, `FillRect`, `DestroyIcon`, `CopyImage`, `CharLowerBuffA`
**advapi32.dll**: `RegSetValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**oleaut32.dll**: `SysFreeString`, `SysReAllocStringLen`
**gdi32.dll**: `StretchDIBits`, `SetDIBits`, `SelectObject`, `GetObjectA`, `GetDIBits`, `DeleteObject`, `DeleteDC`, `CreateSolidBrush`, `CreateDIBSection`, `CreateCompatibleDC`, `CreateCompatibleBitmap`, `BitBlt`
**shell32.dll**: `ShellExecuteA`, `ExtractIconA`

## Extracted Strings

Total strings found: **70793** (showing first 100)

```
This program must be run under Win32
$7
.idata
.rdata
P.reloc
P.rsrc
YZ]_^[
C;D$v
D$+D$
YZ]_^[
_^[YY]
YZ]_^[
:
u0Nt
~KxI[)
SOFTWARE\Borland\Delphi\RTL
FPUMaskValue
t!R:
t
<
t%<t><tQ<t\<
_^[YY]
HBITMAP
YXZQRPR
R;P P|
IVXLCDMT
t=8!uJB8
_^[YY]
_^[YY]
XH;XH~	P
9PD}-RP
PH9PL~
KH+KLQ
;CHRQ~
RP;P ~
_^[YY]
QQQQQS
\PROGRA~1\
QQQQQQSVW
_^[YY]
QQQQQQS3
QQQQQQ
QQQQQQSV
Runtime error     at 00000000
0123456789ABCDEF
kernel32.dll
DeleteCriticalSection
LeaveCriticalSection
EnterCriticalSection
InitializeCriticalSection
VirtualFree
VirtualAlloc
LocalFree
LocalAlloc
GetVersion
GetCurrentThreadId
GetThreadLocale
GetStartupInfoA
GetLocaleInfoA
GetCommandLineA
FreeLibrary
ExitProcess
WriteFile
UnhandledExceptionFilter
RtlUnwind
RaiseException
GetStdHandle
user32.dll
GetKeyboardType
MessageBoxA
advapi32.dll
RegQueryValueExA
RegOpenKeyExA
RegCloseKey
oleaut32.dll
SysFreeString
SysReAllocStringLen
kernel32.dll
TlsSetValue
TlsGetValue
LocalAlloc
GetModuleHandleA
advapi32.dll
RegSetValueExA
RegOpenKeyExA
RegCloseKey
kernel32.dll
WriteFile
WinExec
SetFilePointer
SetFileAttributesA
SetEndOfFile
SetCurrentDirectoryA
ReleaseMutex
ReadFile
GetWindowsDirectoryA
GetTempPathA
GetShortPathNameA
GetModuleFileNameA
GetLogicalDriveStringsA
GetLocalTime
GetLastError
GetFileSize
GetFileAttributesA
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00406638` | `0x406638` | 1262 | ✓ |
| `fcn.004071d0` | `0x4071d0` | 700 | ✓ |
| `fcn.0040536c` | `0x40536c` | 677 | ✓ |
| `fcn.00407678` | `0x407678` | 522 | ✓ |
| `fcn.0040627c` | `0x40627c` | 496 | ✓ |
| `fcn.004021a8` | `0x4021a8` | 474 | ✓ |
| `fcn.00407bd4` | `0x407bd4` | 441 | ✓ |
| `fcn.00402004` | `0x402004` | 418 | ✓ |
| `fcn.00407e90` | `0x407e90` | 400 | ✓ |
| `fcn.00401e74` | `0x401e74` | 397 | ✓ |
| `fcn.00403998` | `0x403998` | 396 | ✓ |
| `fcn.00405080` | `0x405080` | 347 | ✓ |
| `fcn.00406b48` | `0x406b48` | 335 | ✓ |
| `entry0` | `0x4080e4` | 316 | ✓ |
| `fcn.00405834` | `0x405834` | 304 | ✓ |
| `fcn.00405634` | `0x405634` | 296 | ✓ |
| `fcn.004079a0` | `0x4079a0` | 292 | ✓ |
| `fcn.004015d8` | `0x4015d8` | 291 | ✓ |
| `fcn.00403750` | `0x403750` | 282 | ✓ |
| `fcn.004049d0` | `0x4049d0` | 266 | ✓ |
| `fcn.00401d80` | `0x401d80` | 244 | ✓ |
| `fcn.0040386c` | `0x40386c` | 242 | ✓ |
| `fcn.0040364c` | `0x40364c` | 234 | ✓ |
| `fcn.0040184c` | `0x40184c` | 224 | ✓ |
| `fcn.00405e94` | `0x405e94` | 218 | ✓ |
| `fcn.00407d9c` | `0x407d9c` | 217 | ✓ |
| `fcn.004074b4` | `0x4074b4` | 215 | ✓ |
| `fcn.00402fa4` | `0x402fa4` | 211 | ✓ |
| `fcn.0040269c` | `0x40269c` | 209 | ✓ |
| `fcn.00407ad0` | `0x407ad0` | 205 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.004015d8.c`](code/fcn.004015d8.c)
- [`code/fcn.0040184c.c`](code/fcn.0040184c.c)
- [`code/fcn.00401d80.c`](code/fcn.00401d80.c)
- [`code/fcn.00401e74.c`](code/fcn.00401e74.c)
- [`code/fcn.00402004.c`](code/fcn.00402004.c)
- [`code/fcn.004021a8.c`](code/fcn.004021a8.c)
- [`code/fcn.0040269c.c`](code/fcn.0040269c.c)
- [`code/fcn.00402fa4.c`](code/fcn.00402fa4.c)
- [`code/fcn.0040364c.c`](code/fcn.0040364c.c)
- [`code/fcn.00403750.c`](code/fcn.00403750.c)
- [`code/fcn.0040386c.c`](code/fcn.0040386c.c)
- [`code/fcn.00403998.c`](code/fcn.00403998.c)
- [`code/fcn.004049d0.c`](code/fcn.004049d0.c)
- [`code/fcn.00405080.c`](code/fcn.00405080.c)
- [`code/fcn.0040536c.c`](code/fcn.0040536c.c)
- [`code/fcn.00405634.c`](code/fcn.00405634.c)
- [`code/fcn.00405834.c`](code/fcn.00405834.c)
- [`code/fcn.00405e94.c`](code/fcn.00405e94.c)
- [`code/fcn.0040627c.c`](code/fcn.0040627c.c)
- [`code/fcn.00406638.c`](code/fcn.00406638.c)
- [`code/fcn.00406b48.c`](code/fcn.00406b48.c)
- [`code/fcn.004071d0.c`](code/fcn.004071d0.c)
- [`code/fcn.004074b4.c`](code/fcn.004074b4.c)
- [`code/fcn.00407678.c`](code/fcn.00407678.c)
- [`code/fcn.004079a0.c`](code/fcn.004079a0.c)
- [`code/fcn.00407ad0.c`](code/fcn.00407ad0.c)
- [`code/fcn.00407bd4.c`](code/fcn.00407bd4.c)
- [`code/fcn.00407d9c.c`](code/fcn.00407d9c.c)
- [`code/fcn.00407e90.c`](code/fcn.00407e90.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's behavior:

### Core Functionality and Purpose
This binary appears to be a **dropper** or a **downloader loader**. Its primary purpose is to process data (likely from an internal table or external file), resolve file paths, execute secondary payloads, and clean up artifacts. The presence of "Neshta" and "Belarus" in the strings suggests it belongs to a specific strain of older Eastern European malware.

### Suspicious or Malicious Behaviors
*   **Payload Execution:** The code utilizes `WinExec` (in `fcn.00407d9c`) to launch programs. This is a classic method for launching dropped executables or scripts after they have been unpacked or downloaded into memory/disk.
*   **File System Manipulation:** 
    *   The binary uses `SetFileAttributesA` (in `fcn.004071d0`) to modify file attributes—specifically, it appears to be stripping "hidden" attributes (setting value to 0) from files before interacting with them or executing them.
    *   It performs active cleanup of the filesystem using `DeleteFileA` (in `fcn.004079a0`). This is often used to delete temporary dropped payloads or artifacts left behind during a multi-stage infection.
*   **Path Resolution & Parsing:** Several functions (`fcn.0040536c`, `fcn.004049d0`) are dedicated to parsing and validating file paths. It handles quotes, checks for directory separators, and resolves the current execution path. This ensures that the "next stage" of the malware is launched correctly regardless of where it is unpacked.
*   **Anti-Forensics/Persistence Preparation:** The pattern of `SetFileAttributes` followed by `WinExec`, followed by a cleanup routine (`DeleteFile`), is a classic indicator of a multi-stage dropper designed to minimize its footprint on the host system.

### Notable Techniques and Patterns
*   **GDI Manipulation (Potential Decoy or UI Overlay):** A significant amount of code is dedicated to GDI functions (`BitBlt`, `StretchDIBits`, `CreateCompatibleDC` in `fcn.00406638`). While this could be for creating a fake "loading" screen or a decoy GUI, it is also sometimes used in older malware to overlay graphics on the screen or manipulate the desktop to hide malicious windows.
*   **Resource/String Parsing:** The internal logic handles `\r` and `\n` characters during string processing (`fcn.0040386c`). This suggests that the binary may be parsing a configuration block or an embedded list of commands/URLs/file paths.
*   **Delphi Construction:** The "Borland\Delphi" string indicates it was written in Delphi, a common tool for producing high-performance, portable executables often used by malware authors to simplify and obfuscate the underlying logic.
*   **Manual Memory Management:** Functions like `fcn.0040184c` and `fcn.00401d80` show manual management of memory buffers and critical sections, which is common in complex installers or multi-stage droppers that need to manage multiple resources simultaneously.

### Summary of Indicators
*   **Malicious Tooling:** Likely a loader/dropper component.
*   **Persistence Support:** Routine for dropping and executing secondary payloads via `WinExec`.
*   **Evidence Destruction:** Explicit logic for deleting files after use (`DeleteFileA`).
*   **Defense Evasion:** Use of `SetFileAttributes` to manipulate file visibility before execution.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1105** | Ingress Tool Transfer | The binary is identified as a "dropper" or "downloader loader," which serves to deliver additional payloads to the target system. |
| **T1564.001** | Hide Files and Directories | The use of `SetFileAttributesA` to strip "hidden" attributes suggests an attempt to manipulate file visibility and evade basic detection before execution. |
| **T1070.004** | Indicator Removal: File Deletion | The explicit call to `DeleteFileA` for cleanup indicates a routine designed to remove artifacts and drop-files from the host after they have been executed. |
| **T1036** | Masquerading | The use of GDI functions to create potential decoys or UI overlays is a common method to hide malicious windows or activities behind legitimate-looking graphics. |
| **T1059** | Command and Scripting Interpreter | While used broadly, the execution of secondary payloads via `WinExec` (often scripts or batch files in multi-stage attacks) aligns with this technique for executing dropped content. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Generic Windows API calls (e.g., `kernel32.dll`, `GetTempPathA`) and standard system paths have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   **Registry Key:** `SOFTWARE\Borland\Delphi\RTL` (Note: While this is a known path for Delphi installations, its presence confirms the development environment).

### **Mutex names / Named pipes**
*   *None identified in the provided text.*

### **Hashes**
*   *None identified in the provided text.*

### **Other artifacts**
*   **Malware Family/Campaign Identifier:** `Neshta` (Specifically "Neshta 1.0")
*   **Threat Actor / Developer Names:** `Tommy Salo`, `Dziadulja Apanas`
*   **Geographic Origin Indicator:** `Belarus`
*   **Development Environment:** Borland Delphi (Identified via the string: `Delphi-the best. Fuck off all the rest.`)
*   **Suspicious API Patterns:** 
    *   `WinExec` (Used for payload execution)
    *   `SetFileAttributesA` (Used for file attribute manipulation/evasion)
    *   `DeleteFileA` (Used for evidence destruction/cleanup of dropped files)

---

## Malware Family Classification

1. **Malware family**: Neshta (specifically "Neshta 1.0")
2. **Malware type**: Dropper / Downloader
3. **Confidence**: High
4. **Key evidence**:
    *   **Explicit Branding:** The presence of the "Neshta" and "Neshta 1.0" strings in the metadata provides a direct link to this specific malware strain/campaign.
    *   **Execution Chain Behavior:** The combination of `WinExec` (to launch secondary payloads), `SetFileAttributesA` (to manipulate file visibility), and `DeleteFileA` (to remove artifacts) is consistent with multi-stage dropper functionality designed to minimize the footprint on a host system.
    *   **Development Context:** The use of Borland Delphi and specific regional identifiers associated with older Eastern European malware campaigns supports its classification as a known malicious downloader rather than generic commodity malware.
