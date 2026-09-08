# Threat Analysis Report

**Generated:** 2026-09-02 23:13 UTC
**Sample:** `13b92c9a67524a0ff5098fbb00b53219cb93c8abd23594b36875fe92320f2a13_13b92c9a67524a0ff5098fbb00b53219cb93c8abd23594b36875fe92320f2a13.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13b92c9a67524a0ff5098fbb00b53219cb93c8abd23594b36875fe92320f2a13_13b92c9a67524a0ff5098fbb00b53219cb93c8abd23594b36875fe92320f2a13.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 356,352 bytes |
| MD5 | `016becbef6598c26f79ce112eefe0f5b` |
| SHA1 | `238d84c10078750ad3ac7df945ebc1cbeb282869` |
| SHA256 | `13b92c9a67524a0ff5098fbb00b53219cb93c8abd23594b36875fe92320f2a13` |
| Overall entropy | 6.427 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769591831 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 352,768 | 6.444 | No |
| `.rsrc` | 2,560 | 4.236 | No |
| `.reloc` | 512 | 0.098 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **2540** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

-r0	

-J+Z 

-4	(


+ra#

,&	oJ

+ 	o

,rZ'

,hrl(
0A[i
+

+2	o

+*	o

+*	o

-rW?

-rtE

,r6I

1r4J

,rOK

,rOK

-raL

,rOK

,rOK

,rOK

,rCN
cZjX}v
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
hSystem.Drawing.Bitmap, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3aPADPADi
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Bitmap
tEXtSoftware
Adobe ImageReadyq
IDAT8O]
V:>zp3
f{9D]r
\vZ"ZB!
v4.0.30319
#Strings
K6?c%
KNA#&

 LXS_0Q
 .!5!|!
#$#>#d#
$0$D$o$
+),C,X,q,
.!///:/_/
0*0@0g0
1$2A2c2
5 515]5s5
6757]7s7
78d8w8
9!9J9#:):e:p:
;E<f<x<
>&>T>gD
"L$g$	%!%
-P.`.p.$1
586{6J7
7,898I8=;S;T<
 @
# @
5 @
T @
_ @
e @
k @
s @

Client.exe
Client
mscorlib
System.Core
System.Windows.Forms
System
System.Drawing
System.Runtime.Serialization
System.Xml
System.Management
System.Security
Microsoft.VisualBasic
user32.dll
kernel32.dll
gdi32.dll
msvcrt.dll
advapi32.dll
shlwapi.dll
Kernel32.dll
shell32.dll
iphlpapi.dll
ole32.dll
ntdll.dll
oleaut32.dll
xClient.Properties.Resources.resources
Object
ApplicationContext
Application
EnableVisualStyles
SetCompatibleTextRenderingDefault
AppDomain
get_CurrentDomain
UnhandledExceptionEventHandler
add_UnhandledException
STAThreadAttribute
get_MessageLoop
Environment
UnhandledExceptionEventArgs
get_IsTerminating
String
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **5**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym...cctor__26` | `0x419ab4` | 262144 | ✓ |
| `method...cctor` | `0x419b28` | 65420 | — |
| `sym...ctor__51` | `0x4148b8` | 9904 | ✓ |
| `sym...cctor__17` | `0x413730` | 2616 | ✓ |
| `sym..__103` | `0x407ad0` | 2092 | ✓ |
| `method.xClient.Core.Utilities.UnsafeStreamCodec.CodeImage` | `0x405344` | 1968 | ✓ |
| `method.AForge.Video.DirectShow.VideoCaptureDevice.WorkerThread` | `0x41886c` | 1744 | — |
| `sym..__105` | `0x408448` | 1720 | — |
| `sym..__165` | `0x40da3c` | 1532 | — |
| `sym..__148` | `0x40ae68` | 1460 | — |
| `sym..__147` | `0x40aa2c` | 1076 | — |
| `sym..__178` | `0x40ead0` | 1056 | — |
| `sym..__166` | `0x40e060` | 968 | — |
| `sym..__142` | `0x40a14c` | 940 | — |
| `method..C` | `0x41433c` | 876 | — |
| `sym..__146` | `0x40a750` | 692 | — |
| `method.xClient.Core.NetSerializer.TypeSerializers.ObjectSerializer.GenerateReaderMethod` | `0x4115d0` | 616 | — |
| `method.xClient.Core.NetSerializer.TypeSerializers.ArraySerializer.GenerateReaderMethod` | `0x4106c8` | 584 | — |
| `sym...cctor__25` | `0x419874` | 576 | — |
| `method.xClient.Core.NetSerializer.TypeSerializers.ObjectSerializer.GenerateWriterMethod` | `0x411394` | 572 | — |
| `sym..__125` | `0x409778` | 532 | — |
| `sym..__91` | `0x4072b0` | 512 | — |
| `method.xClient.Core.NetSerializer.TypeSerializers.ArraySerializer.GenerateWriterMethod` | `0x4104c8` | 512 | — |
| `sym..__157` | `0x40d4e8` | 508 | — |
| `sym...cctor__13` | `0x412678` | 500 | — |
| `sym..__159` | `0x40d6fc` | 484 | — |
| `method.xClient.Core.NetSerializer.Serializer.GenerateTypeData` | `0x410058` | 448 | — |
| `sym..__85` | `0x404dc4` | 440 | — |
| `sym...ctor__58` | `0x4173c4` | 432 | — |
| `sym..__144` | `0x40a568` | 424 | — |

### Decompiled Code Files

- [`code/method.xClient.Core.Utilities.UnsafeStreamCodec.CodeImage.c`](code/method.xClient.Core.Utilities.UnsafeStreamCodec.CodeImage.c)
- [`code/sym...cctor__17.c`](code/sym...cctor__17.c)
- [`code/sym...cctor__26.c`](code/sym...cctor__26.c)
- [`code/sym...ctor__51.c`](code/sym...ctor__51.c)
- [`code/sym..__103.c`](code/sym..__103.c)

## Behavioral Analysis

Based on the analysis of the provided strings and decompiled code, this binary appears to be a **malware sample (likely a Trojan or a proxy/backdoor)** that utilizes significant obfuscation techniques to hinder analysis.

### Core Functionality
The code is written in .NET (indicated by `mscorlib` and various `System.*` namespaces). Based on the internal symbols and strings, its primary functions appear to be:
*   **Network Communication:** The presence of `System.Net.Sockets`, `ReverseProxyConnect`, and `Packet` structures suggests it is designed to establish connections, potentially acting as a proxy or participating in a C2 (Command & Control) architecture.
*   **Resource Management:** The inclusion of `System.Drawing` and various image-related strings suggests it may have a GUI component or handles icons/images used for its own display.
*   **File System Manipulation:** References to `FileAttributes`, `SetAttributes`, and `GetDirectoryName` indicate the ability to modify files, potentially for persistence or to hide its presence.

### Suspicious / Malicious Behaviors
The following behaviors are indicative of malicious intent:
*   **Network Proxy/Tunneling:** The specific strings like `ReverseProxyConnect` and `xClient.Core.ReverseProxy` strongly suggest the binary is intended to tunnel traffic or facilitate a proxy connection, a common feature in "Bot" malware used for gray-market proxy services or data exfiltration.
*   **In-Memory Code Execution:** The method `UnsafeStreamCodec.CodeImage` combined with .NET's Reflection capabilities often indicates that the program may execute code directly in memory (JIT compilation). This is a common technique to bypass signature-based antivirus by never writing the actual malicious payload to disk.
*   **Process Interaction:** The inclusion of `System.Diagnostics.Process` and `ProcessStartInfo` suggests it can launch other processes, which could be used for "dropping" additional payloads or executing commands received from a remote server.

### Notable Techniques & Patterns
The disassembly reveals several advanced evasion techniques:
*   **Heavy Obfuscation/Junk Code:** The functions `sym...cctor__26`, `sym...cctor__51`, and especially `sym...cctor__17` contain massive amounts of "junk" arithmetic. These are calculations that result in no meaningful change to the program's logic but are designed to break decompiler tools (like Hex-Rays or Ghidra) and waste an analyst's time.
*   **Control Flow Flattening/Garbage Code:** The `sym...cctor__17` function contains numerous "bad instruction" warnings, overlapping code blocks, and unreachable segments. This is a classic sign of **code virtualization** or complex **control-flow obfuscation**, intended to hide the actual logic of the program behind a wall of nonsensical instructions.
*   **Software Interrupts:** The use of `swi(3)` (a software interrupt) in some functions can be used as an anti-debugging trick; it triggers an exception that, if handled by a debugger, allows the malware to detect and change its behavior or exit.
*   **Resource Masking:** The presence of strings like "Adobe ImageReady" and "xClient" may indicate the use of a custom wrapper or packer intended to make the binary look like a legitimate piece of software (like an Adobe plugin) during initial triaging.

### Summary for Triage
This is a **highly obfuscated .NET-based Trojan.** It likely functions as a proxy/backdoor capable of network communication and in-memory execution. The presence of significant junk code and "broken" disassembly blocks suggests it was compiled with a professional protector (like VMProtect or Themida) or a sophisticated custom packer to evade automated and manual analysis.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1090** | Proxy | The inclusion of `ReverseProxyConnect` and `xClient.Core.ReverseProxy` indicates the malware is designed to route traffic through other systems, likely for C2 or as a gray-market proxy service. |
| **T1637** | Reflection | The use of .NET `Reflection` and `UnsafeStreamCodec.CodeImage` suggests in-memory execution to bypass signature-based antivirus detections by avoiding disk writes. |
| **T1059** | Command and Scripting Interpreter | The implementation of `ProcessStartInfo` indicates the ability to execute commands or "drop" additional payloads received from a remote server. |
| **T1027** | Obfuscated Files/Information | The use of extensive junk code, control-flow flattening, and "broken" disassembly blocks is intended to hinder analysis by automated tools and human researchers. |
| **T1036** | Masquerading | The presence of strings like "Adobe ImageReady" suggests the malware attempts to appear as a legitimate software component during initial triage. |
| **T1564** | Hide Elements | The use of `FileAttributes` and `SetAttributes` indicates an intent to modify file properties, potentially to hide the binary's presence or persistence mechanism from the user. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

### **File paths / Registry keys**
*   **Client.exe** (Note: This is a generic filename; specific file paths were not provided.)

### **Mutex names / Named pipes**
*   *(None identified in the provided text)*

### **Hashes**
*   *(No MD5, SHA1, or SHA256 hashes were present in the strings.)*

### **Other artifacts**
*   **C2/Proxy Indicators:**
    *   `ReverseProxyConnect` (Internal class/method for proxy traffic)
    *   `xClient.Core.ReverseProxy.Packets` (Internal structure used for packet handling)
*   **Deception / Branding Strings:**
    *   `Adobe ImageReadyq` (Potential masquerading string to bypass initial triage)
*   **Technical Artifacts/Behavioral Indicators:**
    *   **Anti-Debugging:** Use of `swi(3)` software interrupts.
    *   **Evasion Techniques:** Control flow flattening, junk code insertion, and "broken" disassembly blocks (suggesting the use of a packer like VMProtect or Themida).
    *   **Malware Type Indicator:** The presence of `.Net` framework calls for `System.Net.Sockets` combined with "ReverseProxy" indicators suggests a **proxy-bot** used for illicit proxy services.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: backdoor (specifically a proxy-bot)
3. **Confidence**: High

4. **Key evidence**:
*   **Proxy/Tunneling Functionality:** The presence of specific internal classes and structures like `ReverseProxyConnect` and `xClient.Core.ReverseProxy` strongly indicates the binary is designed to facilitate unauthorized network tunneling or act as a gray-market proxy service.
*   **Advanced Evasion & Obfuscation:** The use of control-flow flattening, "junk" arithmetic, and "broken" disassembly blocks—likely resulting from high-end protectors like VMProtect—indicates a sophisticated effort to hide the backend logic from both automated tools and manual analysis.
*   **In-Memory Execution/Loader Traits:** The combination of .NET Reflection, `UnsafeStreamCodec.CodeImage`, and `ProcessStartInfo` suggests the malware is designed to execute payloads in memory or drop additional components while masquerading as legitimate software (e.g., "Adobe ImageReady").
