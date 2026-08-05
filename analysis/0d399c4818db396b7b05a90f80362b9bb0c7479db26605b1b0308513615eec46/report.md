# Threat Analysis Report

**Generated:** 2026-08-04 22:49 UTC
**Sample:** `0d399c4818db396b7b05a90f80362b9bb0c7479db26605b1b0308513615eec46_0d399c4818db396b7b05a90f80362b9bb0c7479db26605b1b0308513615eec46.dll`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0d399c4818db396b7b05a90f80362b9bb0c7479db26605b1b0308513615eec46_0d399c4818db396b7b05a90f80362b9bb0c7479db26605b1b0308513615eec46.dll` |
| File type | PE32 executable for MS Windows 4.00 (DLL), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 8,192 bytes |
| MD5 | `6f31eb40eacfe7d0a647f179e576b503` |
| SHA1 | `062967dc1d38e6f8e4f28d69186a62775fdc8911` |
| SHA256 | `0d399c4818db396b7b05a90f80362b9bb0c7479db26605b1b0308513615eec46` |
| Overall entropy | 4.664 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1774967765 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 6,144 | 5.339 | No |
| `.rsrc` | 1,024 | 2.235 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorDllMain`

## Extracted Strings

Total strings found: **132** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
v4.0.30319
#Strings
<.cctor>b__0_0
<>9__31_0
<StartCursorHideThread>b__31_0
ToInt32
<Module>
WS_VISIBLE
WDA_EXCLUDEFROMCAPTURE
WS_EX_NOACTIVATE
System.IO
WS_POPUP
WNDCLASS
WS_EX_TRANSPARENT
WS_EX_TOOLWINDOW
SW_SHOW
cbWndExtra
cbClsExtra
mscorlib
lpfnWndProc
_wndProc
DefWindowProc
StopCursorHideThread
StartCursorHideThread
_cursorHideThread
NewGuid
_ghostWnd
hbrBackground
set_IsBackground
method
hInstance
PipeTransmissionMode
GhostMode
get_Message
EndInvoke
BeginInvoke
IDisposable
GetModuleHandle
Rectangle
dwStyle
dwExStyle
lpModuleName
pipeName
lpClassName
lpszClassName
lpszMenuName
lpWindowName
ValueType
System.Core
Dispose
WndProcDelegate
GetFunctionPointerForDelegate
MulticastDelegate
CompilerGeneratedAttribute
DebuggableAttribute
CompilationRelaxationsAttribute
RuntimeCompatibilityAttribute
get_IsAlive
_ghostActive
System.Threading
OutputDebugString
ToString
lpOutputString
System.Drawing
get_Width
nWidth
AsyncCallback
callback
Marshal
kernel32.dll
user32.dll
GhostInjector.dll
win32u.dll
NamedPipeServerStream
lParam
lpParam
wParam
System
get_PrimaryScreen
WaitForConnection
PipeDirection
Exception
BitConverter
PipeServer
hCursor
ShowCursor
.cctor
GhostInjector
IntPtr
System.Diagnostics
get_Bounds
System.Runtime.InteropServices
System.Runtime.CompilerServices
DebuggingModes
System.IO.Pipes
System.Windows.Forms
get_AllScreens
```

## Disassembly Overview

Functions analyzed: **14** | Decompiled to C: **14**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method.__c._StartCursorHideThread_b__31_0` | `0x10002508` | 4754 | ✓ |
| `method.GhostInjector.GhostMode.CreateGhostWindow` | `0x100022a8` | 328 | ✓ |
| `method.GhostInjector.GhostMode.PipeServer` | `0x100020a4` | 200 | ✓ |
| `method.GhostInjector.GhostMode.EnableGhost` | `0x1000216c` | 196 | ✓ |
| `method.GhostInjector.GhostMode.DisableGhost` | `0x10002230` | 120 | ✓ |
| `method.GhostInjector.GhostMode..cctor` | `0x10002050` | 84 | ✓ |
| `method.GhostInjector.GhostMode.StartCursorHideThread` | `0x10002458` | 80 | ✓ |
| `method.GhostInjector.GhostMode.StopCursorHideThread` | `0x100024a8` | 62 | ✓ |
| `method.GhostInjector.GhostMode.DestroyGhostWindow` | `0x100023f0` | 56 | ✓ |
| `method.GhostInjector.GhostMode.WndProc` | `0x10002428` | 48 | ✓ |
| `method.__c._.cctor_b__0_0` | `0x100024fb` | 13 | ✓ |
| `method.__c..cctor` | `0x100024ef` | 12 | ✓ |
| `method.GhostInjector.GhostMode..ctor` | `0x100024e6` | 9 | ✓ |
| `entry0` | `0x1000379a` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.GhostInjector.GhostMode..cctor.c`](code/method.GhostInjector.GhostMode..cctor.c)
- [`code/method.GhostInjector.GhostMode..ctor.c`](code/method.GhostInjector.GhostMode..ctor.c)
- [`code/method.GhostInjector.GhostMode.CreateGhostWindow.c`](code/method.GhostInjector.GhostMode.CreateGhostWindow.c)
- [`code/method.GhostInjector.GhostMode.DestroyGhostWindow.c`](code/method.GhostInjector.GhostMode.DestroyGhostWindow.c)
- [`code/method.GhostInjector.GhostMode.DisableGhost.c`](code/method.GhostInjector.GhostMode.DisableGhost.c)
- [`code/method.GhostInjector.GhostMode.EnableGhost.c`](code/method.GhostInjector.GhostMode.EnableGhost.c)
- [`code/method.GhostInjector.GhostMode.PipeServer.c`](code/method.GhostInjector.GhostMode.PipeServer.c)
- [`code/method.GhostInjector.GhostMode.StartCursorHideThread.c`](code/method.GhostInjector.GhostMode.StartCursorHideThread.c)
- [`code/method.GhostInjector.GhostMode.StopCursorHideThread.c`](code/method.GhostInjector.GhostMode.StopCursorHideThread.c)
- [`code/method.GhostInjector.GhostMode.WndProc.c`](code/method.GhostInjector.GhostMode.WndProc.c)
- [`code/method.__c..cctor.c`](code/method.__c..cctor.c)
- [`code/method.__c._.cctor_b__0_0.c`](code/method.__c._.cctor_b__0_0.c)
- [`code/method.__c._StartCursorHideThread_b__31_0.c`](code/method.__c._StartCursorHideThread_b__31_0.c)

## Behavioral Analysis

Based on the provided disassembly and string analysis, here is a technical summary of the binary's behavior:

### Core Functionality and Purpose
The sample appears to be a component of a **stealth-oriented malware framework** (likely a Remote Access Trojan (RAT) or an information stealer). Its primary purpose is to create "Ghost" windows—windows that exist in the operating system but are hidden from standard viewing, screen-capture software, and potential user detection.

### Suspicious or Malicious Behaviors
*   **Anti-Analysis / Anti-Screen Capture:** 
    *   The inclusion of `SetWindowDisplayAffinity` is a significant indicator. This Windows API is frequently used by malware to hide a window from being captured by screen recording software (like OBS) or screen-sharing tools (like Discord or Zoom).
    *   The use of the `WDA_EXCLUDEFROMCAPTURE` flag suggests the application intentionally wants to operate "in the shadows" while still performing actions on the desktop.
*   **Interactive Stealth (Mouse Manipulation):** 
    *   The functions `StartCursorHideThread`, `StopCursorHideThread`, and the string `hCursor` indicate a mechanism to hide the mouse cursor. This is common in malicious overlays or "stealth" interfaces where the attacker wants to interact with the system without the user noticing standard GUI elements like a moving cursor.
*   **Inter-Process Communication (IPC):** 
    *   The use of `NamedPipeServerStream` and `PipeServer` indicates that the application communicates with other processes on the local machine via named pipes. This is often used to coordinate between a "loader" (the initial file executed by the user) and a hidden "agent" or service that remains resident in memory.
*   **"Ghosting" Logic:** 
    *   The functions `CreateGhostWindow`, `EnableGhost`, and `DisableGhost` suggest the creation of windows with specific flags (`WS_EX_NOACTIVATE`, `WS_EX_TRANSPARENT`) designed to make them "invisible" to standard user interaction while remaining active.

### Notable Techniques or Patterns
*   **High-Level Obfuscation:** 
    *   The decompiler (r2ghidra) produced significant amounts of junk code and "bad instruction" warnings in the decompiled functions (e.g., `method.__c._StartCursorHideThread_b__31_0`). This indicates the binary was likely processed with an obfuscator designed to confuse automated analysis tools and human researchers.
*   **Managed Code Wrapper:** 
    *   The presence of `.NET` artifacts (`mscoree.dll`, `System.IO`, `System.Threading`) reveals that this is a .NET-based application. This allows the attacker to use high-level libraries for complex tasks like networking and multi-threading while using lower-level Win32 API calls (via PInvoke) for stealth behaviors.
*   **Persistence/Evasion Context:** 
    *   The naming convention `GhostInjector` and `GhostMode` strongly suggests the tool is designed to inject or host code in a way that avoids detection by standard security software that monitors common "visible" windows and interactions.

### Summary of Findings
This binary acts as a **stealth infrastructure component**. It provides the technical capabilities needed for an attacker to maintain a presence on a system while hiding their activities (such as remote control or data exfiltration) from both the user and automated monitoring tools through "ghosting" techniques and screen-capture evasion.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The use of `SetWindowDisplayAffinity` and "Ghost" logic (e.g., `WS_EX_NOACTIVATE`) is intended to hide the application's presence from users and monitoring software. |
| T1027 | Obfuscated Files or Information | The inclusion of junk code and "bad instruction" warnings indicates an intentional attempt to hinder automated analysis and manual reverse engineering. |
| T1055 | Process Injection | The use of a "loader" and "agent" architecture, coupled with named pipes for coordination, suggests the injection of malicious components into separate processes to evade detection. |
| T1631 | Manipulation of System Properties | The intentional manipulation of window flags and cursor visibility are used to bypass standard UI monitoring and user interaction detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None identified)*

**File paths / Registry keys**
*   `GhostInjector.dll` (Note: This is a module/library name associated with the malicious functionality)

**Mutex names / Named pipes**
*   `NamedPipeServerStream` (Mechanism for Inter-Process Communication)
*   `PipeServer` (Associated infrastructure for IPC communication)
*   *Note: Specific pipe names (e.g., \.\pipe\...) were not explicitly listed in the strings, but the presence of `pipeName`, `PipeTransmissionMode`, and `PipeDirection` confirms the use of Named Pipes.*

**Hashes**
*   *(None identified)*

**Other artifacts**
*   **Evasion Techniques:** Use of `SetWindowDisplayAffinity` with `WDA_EXCLUDEFROMCAPTURE` to hide windows from screen-capture software.
*   **Stealth Logic:** `CreateGhostWindow`, `EnableGhost`, `DisableGhost`, and `_ghostWnd`.
*   **User Interface Manipulation:** `StartCursorHideThread`, `StopCursorHideThread`, and `hCursor` (used to hide the mouse cursor during malicious operations).
*   **Development Artifacts:** The presence of `.NET` framework identifiers (`mscoree.dll`, `System.IO`, `System.Threading`) combined with non-standard naming conventions like "Ghost" indicates a custom .NET wrapper for malicious activities.

---

## Malware Family Classification

1. **Malware family**: Custom 
2. **Malware type**: RAT / Loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Evasion-Centric Architecture:** The use of `SetWindowDisplayAffinity` (specifically the `WDA_EXCLUDEFROMCAPTURE` flag) and "Ghost" window logic is a hallmark of Remote Access Trojans (RATs) designed to hide malicious activity from screen-sharing software and users.
    *   **Multi-Stage Infrastructure:** The presence of `NamedPipeServerStream`, a loader/agent architecture, and the term "GhostInjector" indicates this is part of a sophisticated framework used to coordinate between various processes to maintain stealth.
    *   **Intentional Obfuscation:** The use of .NET wrapping combined with high levels of junk code/instruction errors confirms it was designed specifically to hinder automated analysis and manual reverse engineering during a persistence phase.
