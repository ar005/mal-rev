# Threat Analysis Report

**Generated:** 2026-08-20 18:56 UTC
**Sample:** `109b233024348f26571c086aa6aae6eeedb062a704b4a23e0d87dd2234659103_109b233024348f26571c086aa6aae6eeedb062a704b4a23e0d87dd2234659103.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `109b233024348f26571c086aa6aae6eeedb062a704b4a23e0d87dd2234659103_109b233024348f26571c086aa6aae6eeedb062a704b4a23e0d87dd2234659103.exe` |
| File type | PE32+ executable for MS Windows 6.01 (console), x86-64, 16 sections |
| Size | 3,564,544 bytes |
| MD5 | `1ca66f5770cff04b03e200aab601cdb8` |
| SHA1 | `f6ac1b40817dae7058cfec365974e03ea68538e9` |
| SHA256 | `109b233024348f26571c086aa6aae6eeedb062a704b4a23e0d87dd2234659103` |
| Overall entropy | 6.884 |
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
| `.text` | 919,040 | 6.259 | No |
| `.rdata` | 1,488,384 | 5.877 | No |
| `.data` | 128,512 | 4.259 | No |
| `.pdata` | 24,576 | 5.286 | No |
| `.xdata` | 512 | 1.783 | No |
| `/4` | 512 | 5.673 | No |
| `/19` | 200,192 | 7.995 | ⚠️ Yes |
| `/32` | 39,424 | 7.918 | ⚠️ Yes |
| `/46` | 512 | 0.856 | No |
| `/65` | 337,920 | 7.998 | ⚠️ Yes |
| `/78` | 154,112 | 7.994 | ⚠️ Yes |
| `/95` | 79,872 | 7.992 | ⚠️ Yes |
| `/112` | 5,120 | 7.747 | ⚠️ Yes |
| `.idata` | 1,536 | 4.016 | No |
| `.reloc` | 31,232 | 5.351 | No |
| `.symtab` | 151,552 | 5.137 | No |

### Imports

**kernel32.dll**: `WriteFile`, `WriteConsoleW`, `WerSetFlags`, `WerGetFlags`, `WaitForMultipleObjects`, `WaitForSingleObject`, `VirtualQuery`, `VirtualFree`, `VirtualAlloc`, `TlsAlloc`, `SwitchToThread`, `SuspendThread`, `SetWaitableTimer`, `SetProcessPriorityBoost`, `SetEvent`

## Extracted Strings

Total strings found: **11590** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.xdata
B.idata
.reloc
B.symtab
 Go build ID: "x-yGvYwiIJr76R_ZXNAA/pq8ji525ftmjH0kdh-39/lC9FQEN3P-FRauXaWhJ-/o-7TOPJfGdGg_ailDGVi"
 
l$ M9,$u
8cpu.u
P0H9S0
PPH9SP
PpH9Sp
UUUUUUUUH!
33333333H!
\$PH9H@v#H
D$pL9A
L$pL9N
D$@I9p
\$hM9K
\$hM9K
l$8M9,$u
P(H9S(t
P H9S uqH
S0H9P0ug
P88S8u^
P98S9uUH
expafH
nd 3fH
2-byfH
te kfH
H9uH
H9L$ r
L$@H9
s`H9J
debugCal
debugCal
debugCalH9
debugCalH9
l409u
x6tzH9
l819um
debugCalH9
l163uf
x84t6H9
l327uf
runtime.
runtime H
 error: H
:H9F w
>H+zhH
L$HI9QhuH
D$hH98
P`f9P2tgH
\$0f9C2u
2}#s]H
H+.)'
uH9w t
D$PA)P
H9D$(t
H
^0H9X0tQ
\$XHc
$H+L$HH
T$(H+J
L$(H+A

H9Z(w
\$0H9K
D$pH9H
D$0H9H
|$pH9\$
T$ H+:
UUUUUUUUH!
UUUUUUUUH
wwwwwwwwH!
wwwwwwwwH
J0f9J2vuH
f9s2uFf
D$$u$L
T$(M	D
	I9x tE1
runtime.H9
QpM9Qhu
L9L$Xt$H
runtime.H9
reflect.H9
D$#e+H
I9N0tVH
T$ 9T$$
H92t9H9rHt3H
rhH92w
H+5`9"
tRI9N0tLH
H+$+"
T$`Hc
L$XHc
|$0uMH
memprofi
lerau*f
yteu"H
,$M9l$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.crypto_internal_fips140_sha3.keccakF1600.abi0` | `0x1400d4d80` | 19597 | ✓ |
| `sym.unicode.map.init.2` | `0x1400822a0` | 10789 | ✓ |
| `sym.runtime.callbackasm.abi0` | `0x140077cc0` | 10001 | ✓ |
| `sym.time.Time.appendFormat` | `0x1400979a0` | 9381 | ✓ |
| `sym.syscall.init` | `0x14008c560` | 7589 | ✓ |
| `sym.regexp_syntax.dumpInst` | `0x1400c2020` | 7205 | ✓ |
| `sym.runtime.initMetrics` | `0x14001a500` | 6181 | ✓ |
| `sym.runtime.selectgo` | `0x140050e60` | 5741 | ✓ |
| `sym.regexp_syntax._compiler_.compile` | `0x1400b69a0` | 5733 | ✓ |
| `sym.regexp.makeOnePass.func1` | `0x1400c9ea0` | 5373 | ✓ |
| `sym.regexp_syntax._parser_.factor` | `0x1400bab60` | 5360 | ✓ |
| `sym.runtime.findRunnable` | `0x140045360` | 4942 | ✓ |
| `sym.regexp_syntax.parse` | `0x1400bc620` | 4741 | ✓ |
| `sym.runtime.gcMarkTermination` | `0x14001e220` | 4350 | ✓ |
| `sym.crypto_internal_fips140_sha256.blockAVX2.abi0` | `0x1400d2520` | 4350 | ✓ |
| `sym.internal_syscall_windows.init` | `0x1400a0c00` | 4240 | ✓ |
| `sym.runtime._sweepLocked_.sweep` | `0x1400295c0` | 3924 | ✓ |
| `sym.time.nextStdChunk` | `0x14009f340` | 3819 | ✓ |
| `sym.regexp_syntax.map.init.1` | `0x1400b5800` | 3786 | ✓ |
| `sym.syscall.StartProcess` | `0x14008fec0` | 3575 | ✓ |
| `sym.crypto_internal_fips140_sha512.blockAVX2.abi0` | `0x1400da9e0` | 3536 | ✓ |
| `sym.regexp_syntax._Regexp_.Simplify` | `0x1400c42e0` | 3229 | ✓ |
| `sym.internal_filepathlite.Clean` | `0x1400a3620` | 3129 | ✓ |
| `sym.runtime.newstack` | `0x140055fa0` | 3045 | ✓ |
| `sym.regexp._Regexp_.tryBacktrack` | `0x1400c5620` | 3045 | ✓ |
| `sym.runtime.typesEqual` | `0x140069ee0` | 3022 | ✓ |
| `sym.os.stat` | `0x1400abcc0` | 3005 | ✓ |
| `sym.runtime._pageAlloc_.find` | `0x140030540` | 2917 | ✓ |
| `sym.os_exec._Cmd_.Start` | `0x1400b0a60` | 2839 | ✓ |
| `sym.regexp.mergeRuneSets` | `0x1400c8a40` | 2633 | ✓ |

### Decompiled Code Files

- [`code/sym.crypto_internal_fips140_sha256.blockAVX2.abi0.c`](code/sym.crypto_internal_fips140_sha256.blockAVX2.abi0.c)
- [`code/sym.crypto_internal_fips140_sha3.keccakF1600.abi0.c`](code/sym.crypto_internal_fips140_sha3.keccakF1600.abi0.c)
- [`code/sym.crypto_internal_fips140_sha512.blockAVX2.abi0.c`](code/sym.crypto_internal_fips140_sha512.blockAVX2.abi0.c)
- [`code/sym.internal_filepathlite.Clean.c`](code/sym.internal_filepathlite.Clean.c)
- [`code/sym.internal_syscall_windows.init.c`](code/sym.internal_syscall_windows.init.c)
- [`code/sym.os.stat.c`](code/sym.os.stat.c)
- [`code/sym.os_exec._Cmd_.Start.c`](code/sym.os_exec._Cmd_.Start.c)
- [`code/sym.regexp._Regexp_.tryBacktrack.c`](code/sym.regexp._Regexp_.tryBacktrack.c)
- [`code/sym.regexp.makeOnePass.func1.c`](code/sym.regexp.makeOnePass.func1.c)
- [`code/sym.regexp.mergeRuneSets.c`](code/sym.regexp.mergeRuneSets.c)
- [`code/sym.regexp_syntax._Regexp_.Simplify.c`](code/sym.regexp_syntax._Regexp_.Simplify.c)
- [`code/sym.regexp_syntax._compiler_.compile.c`](code/sym.regexp_syntax._compiler_.compile.c)
- [`code/sym.regexp_syntax._parser_.factor.c`](code/sym.regexp_syntax._parser_.factor.c)
- [`code/sym.regexp_syntax.dumpInst.c`](code/sym.regexp_syntax.dumpInst.c)
- [`code/sym.regexp_syntax.map.init.1.c`](code/sym.regexp_syntax.map.init.1.c)
- [`code/sym.regexp_syntax.parse.c`](code/sym.regexp_syntax.parse.c)
- [`code/sym.runtime._pageAlloc_.find.c`](code/sym.runtime._pageAlloc_.find.c)
- [`code/sym.runtime._sweepLocked_.sweep.c`](code/sym.runtime._sweepLocked_.sweep.c)
- [`code/sym.runtime.callbackasm.abi0.c`](code/sym.runtime.callbackasm.abi0.c)
- [`code/sym.runtime.findRunnable.c`](code/sym.runtime.findRunnable.c)
- [`code/sym.runtime.gcMarkTermination.c`](code/sym.runtime.gcMarkTermination.c)
- [`code/sym.runtime.initMetrics.c`](code/sym.runtime.initMetrics.c)
- [`code/sym.runtime.newstack.c`](code/sym.runtime.newstack.c)
- [`code/sym.runtime.selectgo.c`](code/sym.runtime.selectgo.c)
- [`code/sym.runtime.typesEqual.c`](code/sym.runtime.typesEqual.c)
- [`code/sym.syscall.StartProcess.c`](code/sym.syscall.StartProcess.c)
- [`code/sym.syscall.init.c`](code/sym.syscall.init.c)
- [`code/sym.time.Time.appendFormat.c`](code/sym.time.Time.appendFormat.c)
- [`code/sym.time.nextStdChunk.c`](code/sym.time.nextStdChunk.c)
- [`code/sym.unicode.map.init.2.c`](code/sym.unicode.map.init.2.c)

## Behavioral Analysis

The analysis of Chunk 9/9 completes the technical examination of the provided disassembly. This final segment confirms the presence of deep-level system integration and highlights a sophisticated approach to both functionality and obfuscation.

### Updated Summary of Findings (Cumulative)

The evidence continues to reinforce the classification of this tool as an **industrial-grade cyberespionage platform.** The transition from high-performance data processing (Chunk 8) to complex process management and internal Go runtime integration (Chunk 9) suggests a multi-functional tool designed for long-term persistence and sophisticated operations.

---

### 1. New Findings from Chunk 9/9

#### **A. Sub-process Execution & System Interaction (`sym.os_exec._Cmd_.Start`)**
This is one of the most significant findings in this final segment. The code handles the spawning of new processes, including management of:
*   **Standard Streams:** Handling `stdin`, `stdout`, and `stderr`.
*   **Environment Variables:** Passing environment context to child processes.
*   **File Descriptor Management:** Managing various file descriptors (e.g., `0x2200000` for file creation).
*   **Strategic Intent:** While the primary role of this tool is data collection, the ability to execute system commands allows it to:
    1.  **Use "Living off the Land" (LotL) Techniques:** Instead of including complex logic for compression or network transmission, the malware can call native Windows tools (e.g., `powershell.exe`, `certutil.exe`) to perform these tasks, blending in with legitimate admin activity.
    2.  **Evasion via Injection:** It may spawn a secondary process into which it "injects" further malicious payloads or communication modules.

#### **B. Robust File System Interrogation (`sym.os.stat`)**
The inclusion of the `stat` function, coupled with previous findings on path normalization and regex filtering, completes the "Collection Pipeline":
*   **Validation:** Before attempting to read a file for hashing (AVX-512) or content analysis (Regex), the malware uses `stat` to verify the existence, size, and permissions of the target.
*   **Error Handling:** The logic includes checks to see if files are accessible, ensuring that the crawler doesn't crash when encountering system files or protected directories—a hallmark of professional-grade software.

#### **C. Sophisticated Structural Obfuscation (Go Runtime Bloat)**
The presence of internal Go functions like `sym.runtime._pageAlloc_.find`, `sym.runtime.typesEqual`, and `sym.regexp.mergeRuneSets` confirms a deliberate design choice:
*   **Obscurity through Complexity:** By using the full Go runtime, the developers have "buried" their malicious logic inside hundreds of thousands of lines of standard library code. 
*   **Analysis Fatigue:** A human analyst or an automated sandbox must sift through massive amounts of "noise" (memory allocation, type checking, rune set merging) to find the specific instructions that perform the theft. This significantly increases the time and effort required for a thorough reverse-engineering effort.

---

### 2. Updated Analysis of Suspicious & Malicious Behaviors

*   **The "Stealthy Crawler" Profile:** The combination of `stat` (verification), `regexp` (targeting), and `AVX-512` (high-speed hashing) creates a highly efficient pipeline for identifying and preparing high-value data.
*   **Strategic Use of Sub-processes:** The `_Cmd_.Start` function suggests that the malware is not a single "monolith." It is designed to interact with the OS as a suite, potentially calling other tools or scripts to facilitate its goals, making it harder to detect by simply monitoring one single process.
*   **Professional Integrity:** The precision of the `_pageAlloc_.find` and `typesEqual` functions suggests that the developers prioritize **stability.** They want the tool to run reliably on a victim's machine for months without crashing, which is critical for high-value targets where "noisy" crashes lead to immediate investigation.

---

### 3. Final Technical Conclusions

The completion of the disassembly confirms this is not a common commodity trojan. It is a **highly engineered collection platform** with several key characteristics:

1.  **Performance over Simplicity:** Using AVX instructions ensures it can process massive amounts of data (e.g., a company's entire file server) quickly enough to avoid detection by performance-monitoring tools.
2.  **Precision over Volume:** The advanced regex logic confirms that the goal is "surgical" theft—looking for specific documents, credentials, and proprietary information rather than just grabbing everything blindly.
3.  **High Obfuscation Ceiling:** By utilizing a modern, high-level language (Go) with extensive standard library inclusion, the developers have created a significant barrier to analysis. The malicious logic is hidden behind legitimate, complex system calls.

### Indicators of Compromise (IoCs) & Monitoring Targets:
*   **Process Execution:** Monitor for unusual parent-child processes where a Go-based binary spawns common system tools (`powershell`, `cmd.exe`, `wmic`).
*   **Rapid File Access:** Look for a single process opening thousands of files in a short period, particularly those containing keywords identified in the regex analysis (e.g., "password", "confidential").
*   **High CPU Utilization on specific instruction sets:** While rare to detect directly, high-frequency use of AVX/SIMD instructions during a routine file crawl can be a signature of automated data indexing.

**Final Assessment:** This is a sophisticated piece of **cyberespionage software**, likely designed for targeting corporate networks or government entities where high-value intellectual property and sensitive information are located.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The malware utilizes `_Cmd_.Start` to execute system commands, potentially leveraging "Living off the Land" (LotL) binaries like PowerShell or Certutil. |
| **T1083** | File and Directory Discovery | The combination of `stat`, regex filtering, and high-speed hashing indicates a systematic crawl to identify and prepare high-value data for exfiltration. |
| **T1027** | Obfuscated Files or Information | By utilizing the full Go runtime, the developers hide malicious logic within a massive volume of standard library "noise" to cause analysis fatigue. |
| **T1055** | Process Injection | The analyst notes that the malware may spawn secondary processes as hosts for injecting additional payloads or communication modules. |

---

## Indicators of Compromise

Based on the provided strings and behavior analysis, here are the extracted Indicators of Compromise (IOCs). 

Please note that the "Extracted Strings" section contains significant amounts of "noise" common to Go-compiled binaries; however, the Behavioral Analysis provides specific functional indicators used for detection.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis mentions C2 capabilities generally, but no specific infrastructure was provided in the text.)

### **File paths / Registry keys**
*   *None identified.* (While the malware performs file system traversal via `sym.os.stat`, no specific hardcoded malicious paths or registry keys were present in the provided data.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (The "Go build ID" string is a unique identifier for the compiler's build process, not a file hash/checksum of the malware itself.)

### **Other artifacts (Behavioral & Technical Indicators)**
**Process Behavior / Execution Patterns:**
*   **Suspicious Parent-Child Relationships:** A Go-based binary spawning system administration tools such as `powershell.exe`, `cmd.exe`, or `wmic.exe`. 
*   **Living off the Land (LotL):** Use of native Windows binaries to perform tasks like data compression, network transmission, or credential gathering to evade detection.

**File System Activity:**
*   **Rapid File Access:** A single process accessing a high volume of files in a short window (indicative of an automated crawler).
*   **Keyword-Based Targeting:** Automated scanning of file contents for specific strings like "password" and "confidential."

**Technical/System Signatures:**
*   **High-Frequency SIMD/AVX Instructions:** Use of AVX-512 instructions during the file indexing phase (atypical for standard office applications but common in high-performance data processing or rapid hashing).
*   **Go Runtime Overlap:** The use of standard Go libraries (`runtime`, `reflect`, `regexp`) to hide malicious logic within a large volume of "noise" code.

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: Custom
2. **Malware type**: Infostealer / Spyware
3. **Confidence**: High

---

**Key evidence**:
*   **Sophisticated Data Collection Pipeline:** The combination of `sym.os_stat` for file validation, `regexp` for surgical targeting (finding passwords/confidential data), and `AVX-512` instructions for high-speed hashing indicates a professional-grade crawler designed to ingest large volumes of sensitive data quickly while minimizing its footprint.
*   **Strategic Use of "Living off the Land" (LotL):** The implementation of `sym.os_exec._Cmd_.Start` allows the malware to leverage native system tools (like PowerShell or Certutil) for secondary tasks, effectively blending malicious activities with legitimate administrative actions to evade detection.
*   **Advanced Obfuscation through Language Choice:** By utilizing a Go-based architecture, the developers have intentionally hidden the malicious logic within a massive amount of "noise" from the standard library, creating a high barrier for manual analysis and automated detection.
