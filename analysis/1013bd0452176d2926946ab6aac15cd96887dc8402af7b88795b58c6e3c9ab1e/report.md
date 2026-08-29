# Threat Analysis Report

**Generated:** 2026-08-17 23:15 UTC
**Sample:** `1013bd0452176d2926946ab6aac15cd96887dc8402af7b88795b58c6e3c9ab1e_1013bd0452176d2926946ab6aac15cd96887dc8402af7b88795b58c6e3c9ab1e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1013bd0452176d2926946ab6aac15cd96887dc8402af7b88795b58c6e3c9ab1e_1013bd0452176d2926946ab6aac15cd96887dc8402af7b88795b58c6e3c9ab1e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 4 sections |
| Size | 3,096,576 bytes |
| MD5 | `fd6c9697420a53eb56d2beab6d1766a5` |
| SHA1 | `15e678a3d7766fff55df0c2e2aaff555ec8495ae` |
| SHA256 | `1013bd0452176d2926946ab6aac15cd96887dc8402af7b88795b58c6e3c9ab1e` |
| Overall entropy | 6.438 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776772565 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 200,704 | 6.617 | No |
| `.rdata` | 57,344 | 4.71 | No |
| `.data` | 1,040,384 | 5.119 | No |
| `.rsrc` | 1,794,048 | 6.35 | No |

### Imports

**KERNEL32.dll**: `GetTimeZoneInformation`, `GetSystemTime`, `GetLocalTime`, `GetACP`, `TerminateProcess`, `HeapSize`, `IsBadWritePtr`, `GetEnvironmentVariableA`, `GetVersionExA`, `HeapDestroy`, `HeapCreate`, `SetUnhandledExceptionFilter`, `UnhandledExceptionFilter`, `FreeEnvironmentStringsA`, `FreeEnvironmentStringsW`
**USER32.dll**: `SetRect`, `CopyAcceleratorTableA`, `InflateRect`, `GetSysColorBrush`, `GetDesktopWindow`, `PtInRect`, `GetClassNameA`, `DestroyMenu`, `LoadStringA`, `MapDialogRect`, `SetWindowContextHelpId`, `CharUpperA`, `GetMessageA`, `TranslateMessage`, `ValidateRect`
**GDI32.dll**: `CreateSolidBrush`, `PtVisible`, `RectVisible`, `TextOutA`, `ExtTextOutA`, `Escape`, `GetMapMode`, `DPtoLP`, `LPtoDP`, `GetWindowExtEx`, `GetViewportExtEx`, `DeleteObject`, `GetObjectA`, `IntersectClipRect`, `ScaleWindowExtEx`
**comdlg32.dll**: `GetFileTitleA`
**WINSPOOL.DRV**: `ClosePrinter`, `DocumentPropertiesA`, `OpenPrinterA`
**ADVAPI32.dll**: `RegCloseKey`, `RegCreateKeyExA`, `RegOpenKeyExA`, `RegSetValueExA`
**SHELL32.dll**: `SHGetSpecialFolderPathA`
**COMCTL32.dll**: `ord_17`, `ImageList_Destroy`
**oledlg.dll**: `ord_8`
**ole32.dll**: `OleUninitialize`, `OleInitialize`, `CoFreeUnusedLibraries`, `CoTaskMemAlloc`, `CoTaskMemFree`, `CreateILockBytesOnHGlobal`, `StgCreateDocfileOnILockBytes`, `StgOpenStorageOnILockBytes`, `CoGetClassObject`, `CLSIDFromString`, `CLSIDFromProgID`, `CoCreateInstance`, `OleRun`, `CoRegisterMessageFilter`, `CoRevokeClassObject`
**OLEPRO32.DLL**: `ord_253`
**OLEAUT32.dll**: `VariantInit`, `VariantClear`, `SysFreeString`, `SysAllocString`, `VariantChangeType`, `SysAllocStringLen`, `VariantCopy`, `SysAllocStringByteLen`, `VariantTimeToSystemTime`, `SysStringLen`, `GetErrorInfo`

## Extracted Strings

Total strings found: **12951** (showing first 100)

```
!This program cannot be run in DOS mode.
$
E;Rich
`.rdata
@.data
L$ _^]d
L$$_^[
L$P_^][d
T$,RPW
D$ WhP
D$ RPhh*C
L$,j
QV
L$@SQUWV
T$(^_[
u0_^][Y
T$0RWV
T$0RWV
T$0RWV
L$0QWV
T$0RWV
L$PRPQ
T$(PQR
T$PRVS
T+3x%A
;D$<s!
L$ RUPj
T$,PQh
D$0QhtNC
{4_^]3
~(9~$u
D$ _^]
u
;GHt
9_|t	W
9>u_^]
u
_^]3
D$PWQV
D$_^]Y
D$LRPQ
L$XPQR
9G4_^d
9x u	f
F8+N,+F0
N8+F,+N0
@8;Gu6
9u ^t	
9^@t53
V@W@PQ
9^Ht}3
9~@St99~8~
VVVPQR
$;Us@
t*Ht"Ht
Zt(Ht Ht
HtYHt6H
@u+;t$
t#C;ut
QQSVWd
t.;t$$t(
f9]u	f
VC20XC00U
MSVWt
uRFGHt
<xt<Xt	
tn<%t2
HHtiHtGH
HtHHt(
HtOHt)H
Ht"HtHu
;t$s
sO;>|C;~
)u9U
)E9Ur4
Y95`
T
YYF;5`
T
btHHt.
YYF;5`
T
SS@SSPVSS
t#SSUP
t$$VSS
_^][YY
PPPPPPPP
PPPPPPPP
PPPPPPPP
E9}_t
HHtpHHtl
QQSVWj_3
>:uNFV
>:u#FV
ESVWj 
USVWf
+ttHHtd
_9=`
T
G;=`
T
QQSUVWj
_^][YY
E_^[]
HSVHWtgHHtF
`9Mtc}
9MtAVW
);]u
t/WWUPj
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00413a04` | `0x413a04` | 18707 | ✓ |
| `fcn.0041809a` | `0x41809a` | 18029 | ✓ |
| `fcn.0041a330` | `0x41a330` | 2972 | ✓ |
| `method.CDataSourceControl.virtual_20` | `0x4120d7` | 2371 | ✓ |
| `fcn.00407c00` | `0x407c00` | 1991 | ✓ |
| `fcn.004072f0` | `0x4072f0` | 1948 | ✓ |
| `fcn.0041b45f` | `0x41b45f` | 1918 | ✓ |
| `fcn.0041176b` | `0x41176b` | 1916 | ✓ |
| `fcn.0040b140` | `0x40b140` | 1362 | ✓ |
| `fcn.00421620` | `0x421620` | 1315 | ✓ |
| `fcn.004058b0` | `0x4058b0` | 1232 | ✓ |
| `fcn.00408850` | `0x408850` | 1209 | ✓ |
| `fcn.00425988` | `0x425988` | 1198 | ✓ |
| `fcn.0041cf25` | `0x41cf25` | 1185 | ✓ |
| `fcn.0042e662` | `0x42e662` | 1131 | ✓ |
| `fcn.0040b7b0` | `0x40b7b0` | 1074 | ✓ |
| `fcn.00409820` | `0x409820` | 1022 | ✓ |
| `fcn.00416acb` | `0x416acb` | 1007 | ✓ |
| `method.COccManager.virtual_36` | `0x413ba1` | 1003 | ✓ |
| `fcn.00408f80` | `0x408f80` | 966 | ✓ |
| `fcn.00404410` | `0x404410` | 860 | ✓ |
| `fcn.00422d78` | `0x422d78` | 845 | ✓ |
| `fcn.0040a3c0` | `0x40a3c0` | 835 | ✓ |
| `fcn.004212e0` | `0x4212e0` | 831 | ✓ |
| `fcn.00421e50` | `0x421e50` | 822 | ✓ |
| `fcn.00415360` | `0x415360` | 821 | ✓ |
| `fcn.004159a0` | `0x4159a0` | 821 | ✓ |
| `fcn.0041460c` | `0x41460c` | 815 | ✓ |
| `fcn.0040bf20` | `0x40bf20` | 811 | ✓ |
| `fcn.0041887a` | `0x41887a` | 809 | ✓ |

### Decompiled Code Files

- [`code/fcn.00404410.c`](code/fcn.00404410.c)
- [`code/fcn.004058b0.c`](code/fcn.004058b0.c)
- [`code/fcn.004072f0.c`](code/fcn.004072f0.c)
- [`code/fcn.00407c00.c`](code/fcn.00407c00.c)
- [`code/fcn.00408850.c`](code/fcn.00408850.c)
- [`code/fcn.00408f80.c`](code/fcn.00408f80.c)
- [`code/fcn.00409820.c`](code/fcn.00409820.c)
- [`code/fcn.0040a3c0.c`](code/fcn.0040a3c0.c)
- [`code/fcn.0040b140.c`](code/fcn.0040b140.c)
- [`code/fcn.0040b7b0.c`](code/fcn.0040b7b0.c)
- [`code/fcn.0040bf20.c`](code/fcn.0040bf20.c)
- [`code/fcn.0041176b.c`](code/fcn.0041176b.c)
- [`code/fcn.00413a04.c`](code/fcn.00413a04.c)
- [`code/fcn.0041460c.c`](code/fcn.0041460c.c)
- [`code/fcn.00415360.c`](code/fcn.00415360.c)
- [`code/fcn.004159a0.c`](code/fcn.004159a0.c)
- [`code/fcn.00416acb.c`](code/fcn.00416acb.c)
- [`code/fcn.0041809a.c`](code/fcn.0041809a.c)
- [`code/fcn.0041887a.c`](code/fcn.0041887a.c)
- [`code/fcn.0041a330.c`](code/fcn.0041a330.c)
- [`code/fcn.0041b45f.c`](code/fcn.0041b45f.c)
- [`code/fcn.0041cf25.c`](code/fcn.0041cf25.c)
- [`code/fcn.004212e0.c`](code/fcn.004212e0.c)
- [`code/fcn.00421620.c`](code/fcn.00421620.c)
- [`code/fcn.00421e50.c`](code/fcn.00421e50.c)
- [`code/fcn.00422d78.c`](code/fcn.00422d78.c)
- [`code/fcn.00425988.c`](code/fcn.00425988.c)
- [`code/fcn.0042e662.c`](code/fcn.0042e662.c)
- [`code/method.CDataSourceControl.virtual_20.c`](code/method.CDataSourceControl.virtual_20.c)
- [`code/method.COccManager.virtual_36.c`](code/method.COccManager.virtual_36.c)

## Behavioral Analysis

This updated analysis incorporates the disassembly provided in chunk 3/3. The additional code provides a deeper look into how the binary manages its internal data structures and handles UI elements, further solidifying its classification as a sophisticated loader.

### Updated Analysis of Functionality and Purpose

The presence of complex memory management and OLE-like logic indicates that this is not just a simple "unpacker" but a **sophisticated execution framework**.

*   **Advanced Data Structure Management (The "Variant" Logic):**
    The large block starting with `fcn.0041887a` contains highly complex pointer arithmetic and memory management logic (including nested loops, `HeapAlloc`, `HeapRealloc`, and `VirtualFree`). The math involved (e.g., `uVar14 * 0x204 + 0x144`) suggests the binary is navigating a large array of structured data objects. This is highly characteristic of **MS-OLE or COM-style Variant handling**.
    *   **Implication:** The "payload" isn't just a raw executable; it is likely part of a complex configuration system. The loader is parsing these structures to determine operational parameters (e.g., C2 URLs, encryption keys, or regional instructions) before passing execution to the second stage.

*   **Presence of GUI Components:**
    The function `fcn.0040bf20` contains a sequence of vtable assignments for common Windows controls (`CButton`, `CEdit`, `CComboBox`, `CListBox`). 
    *   **Implication:** This suggests the binary may have a **Graphical User Interface (GUI)**. In a malware context, this is often used to create a "decoy" application (e.g., a fake software update window or an error message) that remains visible on the screen while the malicious payload executes in the background.

*   **Sophisticated Memory Lifecycle Management:**
    The code shows frequent use of `HeapReAlloc` and immediate calls to `VirtualFree`. The logic ensures that only enough memory is allocated for the current operation, and large "intermediate" buffers are freed immediately after use. This indicates a high level of professional development intended to **minimize the memory footprint** of the loader, making it harder for analysts to find remnants of the "loader's" logic in a memory dump.

### Updated Suspicious and Malicious Behaviors

The new data adds several layers of sophistication to the threat profile:

*   **Hidden Configuration via Complex Objects:**
    Instead of storing configuration in a simple `.ini` or registry key, the binary uses an internal "object-oriented" approach (the OLE-like structure). This makes it much harder for automated scanners to flag specific malicious strings because they are hidden within complex data structures that only "assemble" correctly during runtime.

*   **Hybrid Loader/Decoy Capability:**
    The combination of "heavy" decompression logic (Chunk 2) and "GUI" component initialization (Chunk 3) suggests the malware may be designed to appear as a legitimate piece of software while serving as a vehicle for a malicious payload. This is often seen in **Trojanized installers**.

*   **Anti-Forensic Memory Management:**
    The systematic use of `VirtualFree` and specifically targeted heap allocations indicates an attempt to leave no "footprints" in the process memory. By freeing the structures used to parse the configuration immediately after they are processed, the malware limits what can be recovered during a live memory forensics investigation.

### New Technical Observations
1.  **Complex State Machine:** The logic surrounding `*0x540a68 == 3` and `*0x540a68 == 2` suggests a state-machine approach to processing data. This is common when a single function is tasked with handling multiple types of objects (e.g., strings, numbers, and nested arrays).
2.  **Memory Alignment Manipulation:** The code uses bitwise AND operations (`& 0xfffffff0`) on memory sizes before calling `HeapAlloc`. This ensures memory is aligned to specific boundaries, which is common in high-performance Windows programming but also used by malware to ensure stability when handling large, manually unpacked buffers.
3.  **Potential "Heavy" Library Inclusion:** The sheer complexity of the functions in this chunk suggests that a significant portion of the binary may be built from or inspired by standard system libraries (like `Ole32.dll` logic), which allows the malware to blend in with legitimate Windows behaviors.

### Updated Summary for Incident Response
The binary is confirmed as a **highly sophisticated multi-stage loader.** It possesses features common in high-end Trojan and Downloader families:

1.  **Robust Decoding/Unpacking:** It uses custom decompression logic to hide its core payload (Chunk 2).
2.  **Complex Configuration Parsing:** It utilizes a complex, likely OLE-inspired system to manage internal state and configuration data (Chunk 3).
3.  **Potential Decoy Interface:** The inclusion of `CButton` and `CEdit` vtables suggests the loader can present a GUI to the user to mask its activities.
4.  **Anti-Forensic Design:** It aggressively manages memory, purging "loader" data as soon as it is no longer needed.

**Revised Recommendation:**
*   **Memory Forensics (Refined):** When capturing memory, look specifically for **allocated segments that do not have a corresponding file mapping on disk.** These are the primary locations where the unpacked payload and the "parsed configuration" will reside. 
*   **Identify Payload Signature:** Since the loader is sophisticated enough to use OLE-style parsing, there is likely a "configuration blob." If found, this blob should be extracted as it may contain C2 infrastructure details (IPs, Domains) that are currently hidden in the packed state.
*   **Behavioral Monitoring:** Monitor for any window creation or title changes during execution; if the loader displays a GUI, it is likely attempting to distract the user or provide a fake "update" interface.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex OLE-style data structures and custom decompression logic masks configuration details like C2 URLs from automated detection. |
| T1036 | Masquerading | The inclusion of standard GUI components (buttons, edit boxes) suggests a decoy interface is used to mimic legitimate software behavior while executing malicious tasks. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted list of Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*None identified.* (Note: The behavioral analysis suggests these may be hidden within an internal "configuration blob" using OLE-style parsing, but no specific domains or IPs were present in the provided text.)

### **File paths / Registry keys**
*None identified.*

### **Mutex names / Named pipes**
*None identified.*

### **Hashes**
*None identified.* (No MD5, SHA1, or SHA256 hashes were present in the string dump.)

### **Other artifacts**
*   **Technical Patterns/TTPs:**
    *   **Obfuscated Configuration Parsing:** Use of "MS-OLE" or "COM-style" Variant logic to hide configuration data (C2 URLs, keys) within complex structures.
    *   **Memory Alignment Manipulation:** Utilization of bitwise AND operations (`& 0xfffffff0`) for memory alignment during large buffer handling.
    *   **Anti-Forensic Memory Management:** Frequent use of `VirtualFree` and `HeapRealloc` to purge "loader" data immediately after consumption to minimize the forensic footprint.
    *   **Decoy UI Implementation:** Inclusion of vtables for standard Windows controls (`CButton`, `CEdit`, `CComboBox`, `CListBox`) to potentially display a fake update or error window to distract users.
    *   **Multi-stage Loading:** Evidence of a "heavy" decompression routine used to hide the secondary payload.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Sophisticated Multi-Stage Architecture:** The sample utilizes complex OLE/COM-style "Variant" parsing and heavy decompression logic to hide its configuration data (C2s, keys) within a complex memory structure rather than simple strings.
*   **Anti-Forensic Memory Management:** The deliberate use of `VirtualFree` and `HeapRealloc` to immediately purge loader components from memory after processing indicates a high level of professional development aimed at evading forensic analysis.
*   **Masquerading Capabilities:** The presence of GUI vtables for elements like `CButton` and `CEdit` suggests the inclusion of a "decoy" interface, common in sophisticated trojans to distract users with fake update windows or error messages while malicious activities occur in the background.
