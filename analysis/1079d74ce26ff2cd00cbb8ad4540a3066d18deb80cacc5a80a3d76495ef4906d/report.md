# Threat Analysis Report

**Generated:** 2026-08-19 00:09 UTC
**Sample:** `1079d74ce26ff2cd00cbb8ad4540a3066d18deb80cacc5a80a3d76495ef4906d_1079d74ce26ff2cd00cbb8ad4540a3066d18deb80cacc5a80a3d76495ef4906d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1079d74ce26ff2cd00cbb8ad4540a3066d18deb80cacc5a80a3d76495ef4906d_1079d74ce26ff2cd00cbb8ad4540a3066d18deb80cacc5a80a3d76495ef4906d.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 6 sections |
| Size | 5,354,496 bytes |
| MD5 | `3764c18d9e45cd159a321f7bcce2372a` |
| SHA1 | `d515c53ec5da365ce845ef75ffaaebccb5452fcd` |
| SHA256 | `1079d74ce26ff2cd00cbb8ad4540a3066d18deb80cacc5a80a3d76495ef4906d` |
| Overall entropy | 7.342 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1771349047 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 234,496 | 6.565 | No |
| `.rdata` | 5,102,080 | 7.341 | ⚠️ Yes |
| `.data` | 2,560 | 2.185 | No |
| `.fptable` | 512 | -0.0 | No |
| `.rsrc` | 1,536 | 3.34 | No |
| `.reloc` | 12,288 | 6.632 | No |

### Imports

**api-ms-win-core-synch-l1-2-0.dll**: `WakeByAddressAll`, `WaitOnAddress`, `WakeByAddressSingle`
**ADVAPI32.dll**: `GetTokenInformation`, `OpenProcessToken`
**KERNEL32.dll**: `SetFilePointerEx`, `DecodePointer`, `GetProcessHeap`, `HeapFree`, `HeapReAlloc`, `LoadLibraryA`, `GetProcAddress`, `GetSystemTimePreciseAsFileTime`, `CloseHandle`, `GetCurrentProcessId`, `GetLastError`, `SetLastError`, `GetTempPathW`, `GetACP`, `GetSystemInfo`
**USER32.dll**: `GetSystemMetrics`, `GetDesktopWindow`
**ntdll.dll**: `NtWriteFile`, `RtlNtStatusToDosError`

## Extracted Strings

Total strings found: **14195** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.fptable
@.reloc
D@;F<
D$8RQWVP
#D$,#t$
;|$,t)
L$,uf
D$;T$
T$;T$
#D$$#t$(	
#D$$#|$(	
yr#;}
t$<PQV
|3	\t
>\t1NAu
\t	NAu
tl<
tl
>fulltJ1
t34$3T$
|$8RQVPW
#D$ #t$$	
#D$ #t$$	
#D$ #t$$	
J9Mr

5ntel
5Genu
F;Btt
QQSVWd
38_^]
E9xt
&9Gv!8E
Yt
jV
9~v@k
URPQQh
kUQPXY]Y[
< t1<	t-
9>tWV
t	iud
;1t+;u
u9~uj
};GvP
u9^uj
};GvP
</t
<\t
SSSPSQ
u9^u
uSSSSj
};GvP
];3t'
f9:t!V
u|9]t,9
QQSVj8j@
;ut.;
9Eu$_[
PPPPPPPP
PPPPPWV
PP9E u

u<jXSf

u	jZf
PVVVVV
D$+d$SVW
D$+d$SVW
C:\ProgramData\svc_3f3fe
 !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
lmnohijkdefg`abc|}~
xyz{tuvwpqrsLMNOHIJKDEFG@ABC\]^_XYZ[TUVWPQRS,-./()*+$%&' !"#<=>?89:;45670123
~yd4;_
[!r\_$
 $(,048<@DHLPTX\`dhlptx|
                
shell32.
!,7BMXcny
)4?JU`kv
&1<GR]hs~
#.9DOZep{
src\main.rs
62SystemManufacturer
SystemProductName
BIOSVendor
AppDataRoamingMicrosoftWindowsRecent
USERNAME4
EG[DBG] [] 

loader.startloader.va.nullloader.vp.nullloader.lla.nullloader.gpa.nullloader.apis.ok
loader.x64
loader.x86loader.allocloader.alloc.retloader.alloc.retryloader.allocfailloader.sections
loader.relocloader.iatloader.perm
loader.tls
loader.doneloader.badmagicloader.badpeloader.oobloader.badmzloader.small
state.payloadstate.payload.encryptedstate.payload.decryptedstate.junkstate.load.startstate.load.donestate.load.failstate.exec.startexec.decoy.startexec.decoy.doneexec.ep.computeexec.ep.addr:handle=0x ep=0x
exec.peb.preexec.peb.postexec.transmuteexec.call.preexec.thread.startexec.thread.joinexec.thread.failexec.call.post                                                                                        
															0
gii|h"
{Kj;`)
[{6bO'
oXJZG-):W)B)-txf)!KtpHxiiqzzRE6N]t_Oax4T	daGf[39svC-rk;hEX,F6mo)ejE/tp}wLoOU7IRjK\[mNSBd\uvtlb(.
4Onh]N.eQfcRNArXf:OQgkzMqbnx61Z_!Q(Ynzp}W[GpdO6h8)ldQUWsHcx.h[OM)S09tzKS!kIpzH2 S
u0"9\
]
4\(pR
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00401e56` | `0x401e56` | 19373 | ✓ |
| `fcn.00407bb6` | `0x407bb6` | 13235 | ✓ |
| `fcn.0042b6ca` | `0x42b6ca` | 4929 | ✓ |
| `fcn.00411be0` | `0x411be0` | 3333 | ✓ |
| `fcn.0041a426` | `0x41a426` | 2761 | ✓ |
| `fcn.0041b889` | `0x41b889` | 2517 | ✓ |
| `fcn.00437408` | `0x437408` | 2461 | ✓ |
| `fcn.004221a0` | `0x4221a0` | 2031 | ✓ |
| `fcn.00417960` | `0x417960` | 1837 | ✓ |
| `fcn.00415490` | `0x415490` | 1666 | ✓ |
| `fcn.0040bb00` | `0x40bb00` | 1459 | ✓ |
| `fcn.0040ec80` | `0x40ec80` | 1426 | ✓ |
| `fcn.00422c97` | `0x422c97` | 1416 | ✓ |
| `fcn.0042aff0` | `0x42aff0` | 1396 | ✓ |
| `fcn.004273f0` | `0x4273f0` | 1372 | ✓ |
| `fcn.00420fa0` | `0x420fa0` | 1363 | ✓ |
| `fcn.00418944` | `0x418944` | 1300 | ✓ |
| `fcn.00428c70` | `0x428c70` | 1264 | ✓ |
| `fcn.00418090` | `0x418090` | 1242 | ✓ |
| `fcn.00425500` | `0x425500` | 1170 | ✓ |
| `fcn.00420b10` | `0x420b10` | 1168 | ✓ |
| `fcn.00412920` | `0x412920` | 1109 | ✓ |
| `fcn.0041d080` | `0x41d080` | 1108 | ✓ |
| `fcn.00434560` | `0x434560` | 1084 | ✓ |
| `fcn.004150a0` | `0x4150a0` | 1000 | ✓ |
| `fcn.004352a8` | `0x4352a8` | 966 | ✓ |
| `fcn.0041b46a` | `0x41b46a` | 959 | ✓ |
| `fcn.0041cab0` | `0x41cab0` | 952 | ✓ |
| `fcn.0042d5fd` | `0x42d5fd` | 931 | ✓ |
| `fcn.00433b40` | `0x433b40` | 906 | ✓ |

### Decompiled Code Files

- [`code/fcn.00401e56.c`](code/fcn.00401e56.c)
- [`code/fcn.00407bb6.c`](code/fcn.00407bb6.c)
- [`code/fcn.0040bb00.c`](code/fcn.0040bb00.c)
- [`code/fcn.0040ec80.c`](code/fcn.0040ec80.c)
- [`code/fcn.00411be0.c`](code/fcn.00411be0.c)
- [`code/fcn.00412920.c`](code/fcn.00412920.c)
- [`code/fcn.004150a0.c`](code/fcn.004150a0.c)
- [`code/fcn.00415490.c`](code/fcn.00415490.c)
- [`code/fcn.00417960.c`](code/fcn.00417960.c)
- [`code/fcn.00418090.c`](code/fcn.00418090.c)
- [`code/fcn.00418944.c`](code/fcn.00418944.c)
- [`code/fcn.0041a426.c`](code/fcn.0041a426.c)
- [`code/fcn.0041b46a.c`](code/fcn.0041b46a.c)
- [`code/fcn.0041b889.c`](code/fcn.0041b889.c)
- [`code/fcn.0041cab0.c`](code/fcn.0041cab0.c)
- [`code/fcn.0041d080.c`](code/fcn.0041d080.c)
- [`code/fcn.00420b10.c`](code/fcn.00420b10.c)
- [`code/fcn.00420fa0.c`](code/fcn.00420fa0.c)
- [`code/fcn.004221a0.c`](code/fcn.004221a0.c)
- [`code/fcn.00422c97.c`](code/fcn.00422c97.c)
- [`code/fcn.00425500.c`](code/fcn.00425500.c)
- [`code/fcn.004273f0.c`](code/fcn.004273f0.c)
- [`code/fcn.00428c70.c`](code/fcn.00428c70.c)
- [`code/fcn.0042aff0.c`](code/fcn.0042aff0.c)
- [`code/fcn.0042b6ca.c`](code/fcn.0042b6ca.c)
- [`code/fcn.0042d5fd.c`](code/fcn.0042d5fd.c)
- [`code/fcn.00433b40.c`](code/fcn.00433b40.c)
- [`code/fcn.00434560.c`](code/fcn.00434560.c)
- [`code/fcn.004352a8.c`](code/fcn.004352a8.c)
- [`code/fcn.00437408.c`](code/fcn.00437408.c)

## Behavioral Analysis

This final analysis incorporates the additional disassembly from chunk 4, which provides significant evidence regarding the malware's data processing capabilities, its methods for resolving internal resources, and the specific libraries/frameworks likely used during development.

### Updated Technical Analysis (Chunk 4 Integration)

The latest code snippets provide clear evidence of high-level abstraction and robust system interaction, further cementing the classification of this sample as a sophisticated piece of malware.

#### 1. Complex Data Extraction & String Resolution
The function `fcn.0041b46a` reveals highly complex logic for searching and parsing data structures. Key observations include:
*   **Sophisticated Decoding Loops:** The code utilizes intricate bitwise operations, shifts, and multi-step calculations (e.g., the `uVar18_h / uVar11` logic) to navigate through memory blocks. This is characteristic of **UTF-16 string processing** or searching for specific "tags" within a proprietary data format.
*   **Indirect Reference Resolution:** Instead of using hardcoded strings, this function appears to dynamically resolve offsets and identify internal components. This suggests the malware avoids common signature-based detection by ensuring that sensitive indicators (like C2 URLs or file paths) are never stored as plain text in a recognizable format until they are needed at runtime.

#### 2. Direct File System Manipulation
The function `fcn.004352a8` provides evidence of the loader's ability to perform "heavy lifting" regarding local system interaction:
*   **Robust File I/O:** This function is a dedicated routine for writing data to disk (evidenced by the calls to `WriteFile`). It handles complex calculations for buffer sizes and offsets, ensuring that data chunks are correctly positioned within a file.
*   **Multi-Stage Deployment:** The presence of such a robust "drop" mechanism suggests the loader is designed to unpack, deobfuscate, and write subsequent stages onto the disk in parts (chunked writing). This allows the malware to bypass security scanners that only inspect single large files, as it can construct a malicious file incrementally in memory before committing it to disk.

#### 3. Advanced Infrastructure & Environment Integrity
The function `fcn.00433b40` is particularly revealing regarding the development environment:
*   **FPU/Control Word Management:** This code manages the Floating Point Unit (FPU) state and control words. This type of logic is commonly found in advanced compiler-generated code (such as **Rust's standard library** or specialized C++ libraries).
*   **Significance for Analysts:** While this often indicates a high-level language was used, it also functions as a "technological fingerprint." The presence of such standardized, complex state management implies the author is utilizing professional-grade development tools to ensure stability across different Windows environments, which in turn makes the malware more reliable and harder to distinguish from legitimate software.

---

### Final Comprehensive Analysis & Summary

The analysis of all four chunks confirms that this binary is a **highly sophisticated, tiered downloader/loader** built upon a custom **Virtual Machine (VM) / Interpreter architecture**. It is not merely a "wrapper" but a full-featured execution environment designed to host and run malicious logic while shielding it from automated detection.

#### Key Indicators of Sophistication:
*   **Interpreter/VM Dispatcher:** The core functionality is abstracted through complex switch-case blocks (e.g., `fcn.00418944`). This means the actual "malicious" actions are only visible when the interpreter decodes and executes its custom bytecode at runtime.
*   **Robust File System Handling:** The loader includes advanced logic for handling long paths, UNC shares (`\\?\` prefix), and multi-chunk file writes, making it suitable for operation in large enterprise networks.
*   **Sophisticated String Obfuscation:** The malware utilizes complex searching algorithms to resolve internal identifiers. This hides the "true" intent of the code (IPs, commands, paths) from simple string analysis tools.
*   **High-Level Language Footprints:** Evidence suggesting the use of Rust or sophisticated C++ libraries indicates a professional development cycle focused on stability and evasion.

#### Incident Response & Defense Guidance:

1.  **Behavioral Analysis is Primary:** Because the core malicious payload resides in "bytecode" interpreted by the loader, static analysis will likely fail to find common "malware strings." Focus detection efforts on **runtime behaviors**:
    *   Unexpected network connections from a single process.
    *   Decrypted payloads being written to temporary directories or system folders.
    *   Process hollowing or injection attempts following the execution of this loader.

2.  **Memory Forensics:** Since the payload is only "visible" when interpreted, perform memory dumps of active processes. Search for high-entropy buffers which may contain the decoded bytecode or subsequent stages of the infection.

3.  **Alert on Advanced Pathing:** Configure monitoring to alert on scripts or executables accessing paths using non-standard prefixes (like `\\?\`) or complex network share traversals, as these are characteristic behaviors found in this specific loader's infrastructure.

4.  **Identify by Infrastructure:** The presence of the FPU state management and specific "Switch Case" dispatcher patterns can be used to identify other variants within a campaign that use the same development kit.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your provided analysis to the relevant MITRE ATT&CK techniques.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The malware uses complex decoding loops, a custom VM/interpreter architecture, and multi-chunk file writing to hide malicious logic and evade signature-based detection. |
| **T1568** | Dynamic Resolution | Instead of using hardcoded strings, the malware resolves internal offsets at runtime to identify sensitive components like C2 URLs or local paths. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized as requested:

**IP addresses / URLs / Domains**
*   *None identified.* (The report notes that C2 infrastructures are currently obfuscated/hidden from static analysis).

**File paths / Registry keys**
*   `C:\ProgramData\svc_3f3fe`

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *None identified.*

**Other artifacts**
*   **Function Offsets (Internal):** 
    *   `0041b46a` (Decoding/String Resolution)
    *   `004352a8` (File I/O / WriteFile routine)
    *   `00433b40` (FPU/Control Word management)
*   **Internal Module/State Identifiers:** 
    *   `loader.x64`
    *   `loader.x86`
    *   `loader.alloc`
    *   `loader.iat`
    *   `loader.perm`
*   **Development Artifacts (Leaked Strings):**
    *   `src\main.rs` (Indicates the source code was likely written in Rust).
*   **Observed Behaviors/TTPs:**
    *   **VM/Interpreter Execution:** Use of a custom bytecode interpreter to hide malicious logic from static analysis.
    *   **UNC Path Usage:** Specifically the `\\?\` prefix, used to bypass standard file path limitations and interact with long paths or complex network shares.
    *   **Chunked File Writing:** Ability to construct files in memory/disk incrementally to evade basic scanners.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**Domains:**
- `dg9gx.co`

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **VM/Interpreter Architecture:** The sample utilizes a sophisticated custom bytecode interpreter (switch-case dispatchers) to execute malicious logic, ensuring that the primary payload remains hidden from static analysis.
*   **Multi-Stage Deployment Logic:** The presence of chunked file writing routines and advanced path handling (`\\?\` prefix) confirms its role as a loader designed to deploy additional payloads while evading standard security scanners.
*   **Sophisticated Evasion Techniques:** Extensive use of indirect resolution, complex bitwise string decoding, and modern development signatures (Rust-related artifacts) indicates a professional, custom-engineered tool rather than an "off-the-shelf" malware framework.
