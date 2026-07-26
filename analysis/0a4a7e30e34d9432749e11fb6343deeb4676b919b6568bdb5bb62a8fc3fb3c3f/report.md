# Threat Analysis Report

**Generated:** 2026-07-24 20:40 UTC
**Sample:** `0a4a7e30e34d9432749e11fb6343deeb4676b919b6568bdb5bb62a8fc3fb3c3f_0a4a7e30e34d9432749e11fb6343deeb4676b919b6568bdb5bb62a8fc3fb3c3f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0a4a7e30e34d9432749e11fb6343deeb4676b919b6568bdb5bb62a8fc3fb3c3f_0a4a7e30e34d9432749e11fb6343deeb4676b919b6568bdb5bb62a8fc3fb3c3f.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 106,496 bytes |
| MD5 | `7461d08e73c953ff86fac4d395fd643e` |
| SHA1 | `006e2bac7d9dd245ec7ff71c0a0f11944a5b2f24` |
| SHA256 | `0a4a7e30e34d9432749e11fb6343deeb4676b919b6568bdb5bb62a8fc3fb3c3f` |
| Overall entropy | 5.922 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1769707987 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 55,808 | 6.447 | No |
| `.rdata` | 39,936 | 4.699 | No |
| `.data` | 3,072 | 2.125 | No |
| `.pdata` | 4,096 | 4.747 | No |
| `.fptable` | 512 | -0.0 | No |
| `.reloc` | 2,048 | 4.857 | No |

### Imports

**USER32.dll**: `DispatchMessageA`, `TranslateMessage`, `GetMessageA`
**ADVAPI32.dll**: `RegSetValueExA`, `RegQueryValueExA`, `RegOpenKeyExA`, `RegCloseKey`
**KERNEL32.dll**: `CreateFileW`, `WriteConsoleW`, `GetModuleHandleExW`, `IsDebuggerPresent`, `CheckRemoteDebuggerPresent`, `CloseHandle`, `WaitForSingleObject`, `Sleep`, `GetCurrentProcess`, `CreateThread`, `GetTickCount`, `VirtualAlloc`, `VirtualProtect`, `DisableThreadLibraryCalls`, `GetModuleFileNameA`

### Exports

`get_hostfxr_path`

## Extracted Strings

Total strings found: **405** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.fptable
.reloc
@UATAUH
UVWAVAWH
A_A^_^]
@USAUH
D$xgy~y
D$|~ud>
D$`bin
ugHcA<
|$ AVH
WATAUAVAWH
A_A^A]A\_
t$ WATAUAVAWH
 A_A^A]A\_
WATAUAVAWH
0A_A^A]A\_
H;XXs
H;xXu5
AUAVAWH
9;|
HcC
u4I9}(
9I9}(tgH
0A_A^A]
UVWATAUAVAWH
`A_A^A]A\_^]
@USVWATAUAVAWH
G0HcX
G0HcX
A_A^A]A\_^[]
UVWATAUAVAWH
A_A^A]A\_^]
WAVAWH
 A_A^_
WAVAWH
@SVWATAUAVAWH
A_A^A]A\_^[
A9	uaA
B(I9A(u
A9	u3A
SVWATAUAVAWH
|$$Hc^
@A_A^A]A\_^[
UVWATAUAVAWH
G0Lch
G0HcX
D$hIcu
 A_A^A]A\_^]
99~YHc^
t98t H
u3HcH<H
x ATAVAWH
< t;<	t7
 A_A^A\
UVWAVAWH
H9:tH
0A_A^_^]
	H;vA
	H;RA
WAVAWH
L3
H3B
 A_A^_
D$0u3
\$8t	H
D$0@8{
u$D8r(tH
D81u`L9r
uPD8r(tH
vWD8s(tH
u$D8r(tH
fD91u_L9r
uPD8r(tH
vVD8s(tH
UVWATAUAVAWH
PA_A^A]A\_^]
WATAUAVAWH
0A_A^A]A\_
H9>u+A
@USVWATAUAVH
,/<-w
H
D8t$ht
H
D8t$ht
H
A^A]A\_^[]
f9)u4H9j
u%@8j(t
v@8k(t
8D$@tH
l$ VWATAVAWH
L$&8\$&t,8Y
A_A^A\_^
t$ WATAUAVAWH
 A_A^A]A\_
fD9t$b
t$ WATAUAVAWH
D!|$xA
A_A^A]A\_
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.180005fe8` | `0x180005fe8` | 13503 | ✓ |
| `fcn.180005fb0` | `0x180005fb0` | 13498 | ✓ |
| `fcn.1800027b4` | `0x1800027b4` | 11391 | ✓ |
| `fcn.1800026b4` | `0x1800026b4` | 2294 | ✓ |
| `fcn.180002844` | `0x180002844` | 2016 | ✓ |
| `fcn.180007ae4` | `0x180007ae4` | 1985 | ✓ |
| `section..text` | `0x180001000` | 1856 | ✓ |
| `fcn.18000d990` | `0x18000d990` | 1677 | ✓ |
| `fcn.180003e98` | `0x180003e98` | 1213 | ✓ |
| `fcn.18000be90` | `0x18000be90` | 1171 | ✓ |
| `fcn.180001a00` | `0x180001a00` | 1057 | ✓ |
| `fcn.18000aed0` | `0x18000aed0` | 922 | ✓ |
| `fcn.18000e040` | `0x18000e040` | 920 | ✓ |
| `fcn.18000a960` | `0x18000a960` | 920 | ✓ |
| `fcn.1800076e8` | `0x1800076e8` | 862 | ✓ |
| `fcn.18000b4b4` | `0x18000b4b4` | 817 | ✓ |
| `fcn.18000c7dc` | `0x18000c7dc` | 815 | ✓ |
| `fcn.1800085b0` | `0x1800085b0` | 712 | ✓ |
| `fcn.180001740` | `0x180001740` | 689 | ✓ |
| `fcn.180002aa0` | `0x180002aa0` | 667 | ✓ |
| `fcn.18000820c` | `0x18000820c` | 623 | ✓ |
| `fcn.180001e30` | `0x180001e30` | 621 | ✓ |
| `fcn.180009644` | `0x180009644` | 604 | ✓ |
| `fcn.180005cb8` | `0x180005cb8` | 589 | ✓ |
| `fcn.180004358` | `0x180004358` | 584 | ✓ |
| `fcn.1800048f8` | `0x1800048f8` | 557 | ✓ |
| `fcn.18000a50c` | `0x18000a50c` | 555 | ✓ |
| `fcn.180002d50` | `0x180002d50` | 517 | ✓ |
| `fcn.180008014` | `0x180008014` | 501 | ✓ |
| `fcn.180003b0c` | `0x180003b0c` | 499 | ✓ |

### Decompiled Code Files

- [`code/fcn.180001740.c`](code/fcn.180001740.c)
- [`code/fcn.180001a00.c`](code/fcn.180001a00.c)
- [`code/fcn.180001e30.c`](code/fcn.180001e30.c)
- [`code/fcn.1800026b4.c`](code/fcn.1800026b4.c)
- [`code/fcn.1800027b4.c`](code/fcn.1800027b4.c)
- [`code/fcn.180002844.c`](code/fcn.180002844.c)
- [`code/fcn.180002aa0.c`](code/fcn.180002aa0.c)
- [`code/fcn.180002d50.c`](code/fcn.180002d50.c)
- [`code/fcn.180003b0c.c`](code/fcn.180003b0c.c)
- [`code/fcn.180003e98.c`](code/fcn.180003e98.c)
- [`code/fcn.180004358.c`](code/fcn.180004358.c)
- [`code/fcn.1800048f8.c`](code/fcn.1800048f8.c)
- [`code/fcn.180005cb8.c`](code/fcn.180005cb8.c)
- [`code/fcn.180005fb0.c`](code/fcn.180005fb0.c)
- [`code/fcn.180005fe8.c`](code/fcn.180005fe8.c)
- [`code/fcn.1800076e8.c`](code/fcn.1800076e8.c)
- [`code/fcn.180007ae4.c`](code/fcn.180007ae4.c)
- [`code/fcn.180008014.c`](code/fcn.180008014.c)
- [`code/fcn.18000820c.c`](code/fcn.18000820c.c)
- [`code/fcn.1800085b0.c`](code/fcn.1800085b0.c)
- [`code/fcn.180009644.c`](code/fcn.180009644.c)
- [`code/fcn.18000a50c.c`](code/fcn.18000a50c.c)
- [`code/fcn.18000a960.c`](code/fcn.18000a960.c)
- [`code/fcn.18000aed0.c`](code/fcn.18000aed0.c)
- [`code/fcn.18000b4b4.c`](code/fcn.18000b4b4.c)
- [`code/fcn.18000be90.c`](code/fcn.18000be90.c)
- [`code/fcn.18000c7dc.c`](code/fcn.18000c7dc.c)
- [`code/fcn.18000d990.c`](code/fcn.18000d990.c)
- [`code/fcn.18000e040.c`](code/fcn.18000e040.c)
- [`code/section..text.c`](code/section..text.c)

## Behavioral Analysis

This additional analysis confirms the high level of sophistication previously identified and provides specific evidence of how the malware attempts to achieve persistence, evade detection, and de-obfuscate its payload in memory.

The updated analysis of the binary's behavior is as follows:

### 1. Confirmed Persistence Mechanism (High Significance)
The disassembly confirms that the string `EdgeUpdate` isn't just a "passive" identifier; it is actively used in an attempt to achieve persistence.
*   **Registry Manipulation:** In function `fcn.180001740`, the code specifically targets: 
    `Software\Microsoft\Windows\CurrentVersion\Run`.
*   **Automatic Execution:** It attempts to find a value named `"EdgeUpdate"`. If it does not exist (or if the program is newly installed), it uses `RegSetValueExA` to create/update that key. This ensures that the malware will automatically start every time the Windows user logs in, masquerading as a legitimate Microsoft Edge update process.

### 2. Anti-Analysis and Anti-Debugging Techniques
The code contains several "environmental checks" designed to detect if it is being analyzed by a human researcher or an automated sandbox:
*   **Debugger Detection:** Function `fcn.180001740` explicitly calls `IsDebuggerPresent()` and `CheckRemoteDebuggerPresent()`. If these return true, the malware can change its behavior (e.g., stop running malicious functions) to hide from a researcher.
*   **Timing/Delay Tactics:** The use of `GetTickCount` combined with `Sleep` in `fcn.180001740` is a common technique used to "stall" the malware, causing automated sandboxes (which usually only run samples for 2-5 minutes) to time out before the malicious payload is even activated.
*   **Hardware/CPU Check:** Function `fcn.180002aa0` performs heavy usage of `CPUID` instructions and checks for specific processor features. This is often used to identify virtualized environments (like those used in malware analysis labs).

### 3. Advanced Memory De-obfuscation
The most critical finding in this chunk relates to how the "payload" is handled once it is loaded into memory:
*   **In-Memory Decryption:** Function `fcn.180001740` contains a loop that performs bitwise XOR operations (`^`) on an allocated block of memory. This confirms that even after the loader finds and loads a component, that component is kept "encrypted" in memory until just before it is needed.
*   **Buffer Manipulation:** The code frequently manipulates buffers with calculated offsets (e.g., `puVar10 = arg2 + 0x18` or `iVar4 = iVar3 + 0x10`). This avoids using standard, traceable memory structures and instead uses "raw" pointers to navigate the data.

### 4. Complex Scripting/Interpreter Engine
The logic in `fcn.180009644` and `fcn.180003b0c` indicates a high degree of internal complexity:
*   **State Machine/Dispatcher:** The heavy use of nested "if" checks for specific hex values (like `0x15`, `0xf`, `0xd`) suggests the presence of a **Virtual Machine (VM) or Interpreter**. 
*   **Why this matters:** This means the "malicious" part of the code isn't actually written in standard x86 assembly that an antivirus can easily signature. Instead, it is likely a custom bytecode format. The loader acts as the "CPU," and the malware's actual logic is "scrambled" into instructions that only this specific loader knows how to interpret.

### 5. Obfuscated API Resolution
The code frequently uses indirection for function calls. Rather than calling standard Windows APIs directly (which would show up in a static analysis of the Import Table), it calculates offsets to find them. This makes it significantly harder to see what "capabilities" the malware has until the moment it actually executes them.

---

### Updated Conclusion
This binary is a **highly sophisticated, multi-stage malicious loader.** 

It is designed for maximum stealth by employing a "layered" defense:
1.  **Outer Layer (Persistence):** It hides in the system's startup list using a fake name (`EdgeUpdate`).
2.  **Middle Layer (Evasion):** It checks for debuggers and virtual machines to stay hidden from security researchers.
3.  **Inner Layer (Obfuscation):** It uses a custom bytecode interpreter and XOR-based memory encryption to ensure that the "real" malicious payload never exists in a readable form on the disk or in memory until it is needed at the very last moment.

**Threat Level:** **High.** This is characteristic of modern, high-end malware (such as RATs, info-stealers, or modular trojans) where the loader's only job is to "clean" and "prepare" the environment for a more dangerous hidden component.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1547.001 | Registry Run Keys/Execute | The malware modifies the `Software\Microsoft\Windows\CurrentVersion\Run` key to ensure it automatically executes upon user login. |
| T1435 | Anti-Debugging | The use of `IsDebuggerPresent` and `CheckRemoteDebuggerPresent` functions indicates an attempt to detect and evade analysis tools. |
| T1497 | Virtualization/Sandbox Evasion | The combination of time delays (`Sleep`/`GetTickCount`) and hardware checks (`CPUID`) is designed to bypass automated sandbox environments. |
| T1027 | Obfuscated Files or Information | XOR-based in-memory decryption is used to hide the payload's content from static analysis until it is ready for execution. |
| T1027 | Obfuscated Files or Information | The implementation of a custom bytecode interpreter (Virtual Machine) hides the true malicious logic by converting it into a non-standard format. |
| T1027 | Obfuscated Files or Information | Calculating offsets to resolve APIs rather than using a standard Import Table masks the malware's capabilities from static analysis tools. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have analyzed the provided strings and behavioral reports. Below are the extracted Indicators of Compromise (IOCs) categorized by type:

### **IP addresses / URLs / Domains**
*   **tbox.moe** (Extracted from string `+tbox.moe/rua2qr.https://files.ca`)
*   **files.ca** (Potential hosting site or C2 redirect)
*   **Note:** The combined string `+tbox.moe/rua2qr.https://files.ca` suggests a multi-stage URL or an obfuscated connection string to a file server.

### **File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\Run`
*   **Registry Value Name:** `EdgeUpdate`
    *   *Context:* The malware utilizes this specific key and value to establish persistence, masquerading as a legitimate Microsoft Edge update process.

### **Mutex names / Named pipes**
*   *None identified in the provided data.*

### **Hashes**
*   *No cryptographic hashes (MD5, SHA-1, or SHA-256) were found in the provided strings.*

### **Other artifacts**
*   **User Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64)`
    *   *Note:* While common, this indicates the malware is configured to mimic a standard Windows 10 browser environment when making web requests.
*   **Persistence Tactic:** Use of the string `EdgeUpdate` as a deceptive name for unauthorized auto-run persistence.
*   **Anti-Analysis Techniques:** 
    *   Calls to `IsDebuggerPresent()` and `CheckRemoteDebuggerPresent()`.
    *   Use of `GetTickCount` and `Sleep` for sandbox "stalling."
    *   `CPUID` instruction usage to detect virtualized environments.
*   **Obfuscation Method:** XOR-based in-memory decryption and the use of a custom bytecode interpreter/virtual machine (VM) to hide the primary payload logic.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `https://files.ca`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Advanced Evasion & Obfuscation:** The presence of a custom bytecode interpreter (Virtual Machine), XOR-based in-memory decryption, and indirect API resolution indicates the sample is a sophisticated loader designed to shield its primary payload from static analysis.
*   **Anti-Analysis Techniques:** The malware actively employs multiple layers of defense, including debugger/VM checks (`IsDebuggerPresent`, `CPUID`) and time-delay tactics (`Sleep` / `GetTickCount`) specifically intended to bypass automated sandbox environments.
*   **Persistence & Masquerading:** The use of the "EdgeUpdate" string in the `Windows\CurrentVersion\Run` registry key demonstrates a clear intent to maintain long-term access on the host while masquerading as a legitimate system update process.
