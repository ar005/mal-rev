# Threat Analysis Report

**Generated:** 2026-08-15 18:16 UTC
**Sample:** `0f0f59593cfae8f5fb3d1ab9af840348c2866a8bddf95be8f98cb7e8874b1138_0f0f59593cfae8f5fb3d1ab9af840348c2866a8bddf95be8f98cb7e8874b1138.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0f0f59593cfae8f5fb3d1ab9af840348c2866a8bddf95be8f98cb7e8874b1138_0f0f59593cfae8f5fb3d1ab9af840348c2866a8bddf95be8f98cb7e8874b1138.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 3 sections |
| Size | 380,928 bytes |
| MD5 | `26d95adcf918117801020378bf6dbbfe` |
| SHA1 | `4ede98e788e7cd89eaa2c52ee9de75cc42036598` |
| SHA256 | `0f0f59593cfae8f5fb3d1ab9af840348c2866a8bddf95be8f98cb7e8874b1138` |
| Overall entropy | 7.687 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1522911479 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 368,640 | 7.795 | ⚠️ Yes |
| `.data` | 4,096 | -0.0 | No |
| `.rsrc` | 4,096 | 4.528 | No |

### Imports

**MSVBVM60.DLL**: `_CIcos`, `_adj_fptan`, `__vbaFreeVarList`, `_adj_fdiv_m64`, `_adj_fprem1`, `__vbaHresultCheckObj`, `_adj_fdiv_m32`, `__vbaObjSet`, `ord_595`, `_adj_fdiv_m16i`, `_adj_fdivr_m16i`, `_CIsin`, `__vbaChkstk`, `EVENT_SINK_AddRef`, `ord_671`

## Extracted Strings

Total strings found: **868** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
MSVBVM60.DLL
Sumpedes
Overflyvningers
checksvindler
33333333+M8
qIII33333M8v-
_"?OSJ'
H};IIW
x(
{`Fn
*nnu@I5K>
#\rz,`%
?|933~s!/jR	
M333~GL4
033333
33333333EPTT5
checksvindler
Command2
Command2
VB5!6&*
Smrrebrdenes1
Lkasserne1
Sumpedes
Sumpedes
Overflyvningers
herpetologists
Overglazing
Unbookishness
deteriorated
Congruency
skoledirektionen
forkludret
Cornets
Mikadoer5
C:\Program Files (x86)\Microsoft Visual Studio\VB98\VB6.OLB
Command2
VBA6.DLL
__vbaFreeVarList
__vbaVarDup
__vbaObjSet
__vbaFreeObj
__vbaHresultCheckObj
__vbaNew2
l2k}9
>:OfH
Cornets
Mntedes1
Mntedes1
Congruency
Remburserede
Remburserede
H?4L:O
Unbookishness
Idealisere2
Idealisere2
deteriorated
Velanskrevnes1
Velanskrevnes1
Overglazing
stormagtstider
stormagtstider
skoledirektionen
Umenneskeliggre0
Umenneskeliggre0
forkludret
hollywoodskuespiller
hollywoodskuespiller
herpetologists
Oluffa7
R^qTZ4
Dx:<n_
n.0[Dj9?hX
*Df
_Gf
$ylT.f:I
8Wc[5F
8:q?S0
fJqG	
#m47Bb
p{`!
9
;q|Umu
^?:7Ey@
GnG9a%
k]8$:vu$!
zB_pGi
&3@w@4
]'&fpmN1C
W?v~71
|7`U[Y
jW>'h]
M/=u501
a%{EFf
/\]P1<
'WYHu-
%G	9IQL
9+]yxA
;xwrm5,
IeNIm6
xl$}\GM[
CccI+[
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00457056` | `0x457056` | 12914 | ✓ |
| `fcn.00454772` | `0x454772` | 2566 | ✓ |
| `fcn.00452126` | `0x452126` | 1471 | ✓ |
| `fcn.0043b4e9` | `0x43b4e9` | 493 | ✓ |
| `entry0` | `0x4011b4` | 370 | ✓ |
| `fcn.00452197` | `0x452197` | 309 | ✓ |
| `fcn.004524d5` | `0x4524d5` | 203 | — |
| `int.0044d718` | `0x44d718` | 191 | ✓ |
| `sym.imp.MSVBVM60.DLL__adj_fpatan` | `0x40103c` | 148 | ✓ |
| `fcn.00452123` | `0x452123` | 124 | ✓ |
| `int.00420382` | `0x420382` | 123 | ✓ |
| `fcn.0041ea77` | `0x41ea77` | 66 | ✓ |
| `sym.imp.MSVBVM60.DLL__CIcos` | `0x401000` | 56 | ✓ |
| `fcn.0040606f` | `0x40606f` | 26 | ✓ |
| `fcn.0045a2e7` | `0x45a2e7` | 24 | ✓ |
| `fcn.0041f1a5` | `0x41f1a5` | 18 | ✓ |
| `fcn.00406ef7` | `0x406ef7` | 14 | ✓ |
| `sub.MSVBVM60.DLL_ThunRTMain` | `0x4011ae` | 6 | ✓ |
| `fcn.0044bcf4` | `0x44bcf4` | 6 | ✓ |
| `sub.MSVBVM60.DLL___vbaChkstk` | `0x4010d0` | 6 | ✓ |
| `sub.MSVBVM60.DLL___vbaNew2` | `0x401196` | 6 | ✓ |
| `sub.MSVBVM60.DLL___vbaHresultCheckObj` | `0x401190` | 6 | ✓ |
| `sub.MSVBVM60.DLL___vbaFreeObj` | `0x40118a` | 6 | ✓ |
| `sub.MSVBVM60.DLL_rtcErrObj` | `0x40117e` | 6 | ✓ |
| `sub.MSVBVM60.DLL___vbaObjSet` | `0x401184` | 6 | ✓ |
| `sub.MSVBVM60.DLL___vbaVarDup` | `0x401172` | 6 | ✓ |
| `sub.MSVBVM60.DLL_rtcMsgBox` | `0x401178` | 6 | ✓ |
| `sub.MSVBVM60.DLL___vbaFreeVarList` | `0x40116c` | 6 | ✓ |
| `sub.MSVBVM60.DLL_rtcBeep` | `0x401166` | 6 | ✓ |
| `sub.MSVBVM60.DLL_rtcSLN` | `0x401160` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040606f.c`](code/fcn.0040606f.c)
- [`code/fcn.00406ef7.c`](code/fcn.00406ef7.c)
- [`code/fcn.0041ea77.c`](code/fcn.0041ea77.c)
- [`code/fcn.0041f1a5.c`](code/fcn.0041f1a5.c)
- [`code/fcn.0043b4e9.c`](code/fcn.0043b4e9.c)
- [`code/fcn.0044bcf4.c`](code/fcn.0044bcf4.c)
- [`code/fcn.00452123.c`](code/fcn.00452123.c)
- [`code/fcn.00452126.c`](code/fcn.00452126.c)
- [`code/fcn.00452197.c`](code/fcn.00452197.c)
- [`code/fcn.00454772.c`](code/fcn.00454772.c)
- [`code/fcn.00457056.c`](code/fcn.00457056.c)
- [`code/fcn.0045a2e7.c`](code/fcn.0045a2e7.c)
- [`code/int.00420382.c`](code/int.00420382.c)
- [`code/int.0044d718.c`](code/int.0044d718.c)
- [`code/sub.MSVBVM60.DLL_ThunRTMain.c`](code/sub.MSVBVM60.DLL_ThunRTMain.c)
- [`code/sub.MSVBVM60.DLL___vbaChkstk.c`](code/sub.MSVBVM60.DLL___vbaChkstk.c)
- [`code/sub.MSVBVM60.DLL___vbaFreeObj.c`](code/sub.MSVBVM60.DLL___vbaFreeObj.c)
- [`code/sub.MSVBVM60.DLL___vbaFreeVarList.c`](code/sub.MSVBVM60.DLL___vbaFreeVarList.c)
- [`code/sub.MSVBVM60.DLL___vbaHresultCheckObj.c`](code/sub.MSVBVM60.DLL___vbaHresultCheckObj.c)
- [`code/sub.MSVBVM60.DLL___vbaNew2.c`](code/sub.MSVBVM60.DLL___vbaNew2.c)
- [`code/sub.MSVBVM60.DLL___vbaObjSet.c`](code/sub.MSVBVM60.DLL___vbaObjSet.c)
- [`code/sub.MSVBVM60.DLL___vbaVarDup.c`](code/sub.MSVBVM60.DLL___vbaVarDup.c)
- [`code/sub.MSVBVM60.DLL_rtcBeep.c`](code/sub.MSVBVM60.DLL_rtcBeep.c)
- [`code/sub.MSVBVM60.DLL_rtcErrObj.c`](code/sub.MSVBVM60.DLL_rtcErrObj.c)
- [`code/sub.MSVBVM60.DLL_rtcMsgBox.c`](code/sub.MSVBVM60.DLL_rtcMsgBox.c)
- [`code/sub.MSVBVM60.DLL_rtcSLN.c`](code/sub.MSVBVM60.DLL_rtcSLN.c)
- [`code/sym.imp.MSVBVM60.DLL__CIcos.c`](code/sym.imp.MSVBVM60.DLL__CIcos.c)
- [`code/sym.imp.MSVBVM60.DLL__adj_fpatan.c`](code/sym.imp.MSVBVM60.DLL__adj_fpatan.c)

## Behavioral Analysis

This second portion of disassembly confirms and significantly deepens the initial analysis. The additional code reinforces the conclusion that this binary is a sophisticated **staged loader** designed to evade detection through technical obfuscation, environmental checks, and "junk" instruction insertion.

Below is the updated and extended analysis incorporating the new data.

---

### Updated Analysis of Binary Sample

#### 1. Core Functionality: Advanced Stub Logic
The sample remains a **stub/loader** for an embedded script-based payload (likely VBScript or VB6). However, the second chunk reveals that the "translation" from the loader to the payload is heavily shielded by layers of anti-analysis logic.

*   **Signature Scanning & Resolution:** Function `fcn.00452197` appears to be a **resolver**. It iterates through memory looking for specific byte signatures (e.g., `0x53004d` and `0x420056`). This is a common technique used by malware to find the correct offsets for decrypted code or to locate necessary system resources that are not statically linked, thereby hiding its true intent from static scanners.
*   **Multi-Stage Construction:** The functions `fcn.00452126` and `fcn.00452123` exhibit high levels of repetition. This structure suggests a "builder" pattern where the loader is constructing the execution environment for the payload bit-by-bit in memory before jumping to it.

#### 2. Advanced Evasion & Anti-Analysis (New Findings)
The additional disassembly reveals specific techniques used to thwart automated sandboxes and manual reverse engineering:

*   **Timing Attacks (Anti-Debugging):** The use of `rdtsc()` (Read Time-Stamp Counter) in several loops indicates **time-based evasion**. By measuring the time taken between instructions, the malware can detect if it is being executed within a debugger or an emulated environment (where execution "jitters" or slows down). If a delay is detected, the malware may change its behavior or refuse to decrypt the payload.
*   **Instruction Bloating/Metamorphism:** The code in `fcn.00454772` and others shows extreme arithmetic complexity for very simple operations (e.g., bitwise shifts combined with modular arithmetic like `% 0x43`). This is a **metamorphic technique**: the logic remains functionally the same, but the instruction sequence is "mangled" to frustrate decompilers and prevent signature-based detection.
*   **Control Flow Flattening/Obfuscation:** The presence of many `halt_baddata()` warnings and "bad instruction" flags in the decompiler indicates that the original assembly was designed with overlapping instructions or jumps into "invalid" data areas. This is a tactic used to break automated disassembly tools, forcing human analysts to manually fix the code flow just to see what it does.

#### 3. Triage of Key Code Sections
*   **`fcn.00454772`:** Confirmed as the primary **de-obfuscation engine**. The repeated use of `uVar16 & 3` and complex modular arithmetic is a signature of an automated obfuscator (like a custom packer or "crypter") used to hide the transition from loader code to script data.
*   **`fcn.00452197`:** Identified as a **scanning/lookup loop**. It likely locates specific headers or markers within the encrypted payload buffer.
*   **`entry0`:** The entry point confirms the integration with the `MSVBVM60.DLL`. However, it also contains "junk" loops (e.g., repeated additions and XORs) that serve no purpose other than to increase the file's entropy and change its signature.

#### 4. Summary of Technical Indicators (IOCs/Patterns)
*   **Technique - Junk Code Insertion:** High density of NOP-equivalent math logic used to hide actual logic.
*   **Technique - Anti-Debugging:** Usage of `rdtsc()` for timing checks.
*   **Technique - Dynamic Resolution:** Using loops to find specific byte sequences in memory instead of using standard import tables.
*   **Tooling/Framework:** **VB6 Wrapper.** The reliance on the Visual Basic runtime allows the attacker to store the "malicious" logic in a script format, making it much harder to detect via traditional string searching or API monitoring.

---

### Updated Incident Response Summary

**Risk Assessment: High**
This binary is confirmed as a **sophisticated malicious loader**. It is not "benign" simply because the heavy lifting (the actual payload) is hidden inside an encrypted/obfuscated script.

**Actionable Intelligence for IR:**
1.  **Execution Behavior:** If executed, this process will likely stay in memory for some time while it performs its de-obfuscation loops. **Memory forensics (e.g., Volatility)** should be performed to dump the memory space of this process after execution, as the "true" malicious script will only exist in an unencrypted state in RAM during this stage.
2.  **Detection Logic:** Detection based on static signatures is likely to fail due to the high amount of metamorphic code. Focus should instead be on **behavioral indicators**:
    *   Process spawning/memory allocation for `MSVBVM60.dll` activities.
    *   High-frequency loops and use of `rdtsc` in known suspicious memory regions.
3.  **Payload Identification:** The core malicious activity (e.g., keylogging, C2 communication) is likely wrapped inside the script decoded by `fcn.00454772`. Once the script is dumped from memory, it can be analyzed separately to determine the specific intent of the attack.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Software Packing | The use of junk code, metamorphic instruction sequences (metamorphism), and control flow flattening are primary methods to obfuscate the binary's true logic from static analysis. |
| T1498 | Virtualization | The implementation of `rdtsc` timing checks is a specific evasion technique used to detect if the sample is running in an automated sandbox or a virtualized environment. |
| T1059.003 | Command and Scripting Interpreter: JavaScript or VBScript | The use of the `MSVBVM60.dll` wrapper indicates that the primary malicious payload is executed as a script to evade detection by standard signature-based scanners. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Standard system files (e.g., `MSVBVM60.DLL`, `VBA6.DLL`) and standard installation paths have been excluded as per instructions.

### **IP addresses / URLs / Domains**
*None detected.*

### **File paths / Registry keys**
*None identified as unique malicious artifacts (System paths were omitted).*

### **Mutex names / Named pipes**
*None detected.*

### **Hashes**
*None detected.*

### **Other artifacts**
*   **Memory Scanning Signatures:** 
    *   `0x53004d` (Used for finding specific byte signatures in memory)
    *   `0x420056` (Used for finding specific byte signatures in memory)
*   **Anti-Analysis Techniques:**
    *   **Timing Checks:** Use of `rdtsc()` instructions to detect debuggers or emulated environments.
    *   **Dynamic Resolution:** Scanning logic designed to bypass the Import Address Table (IAT) by locating functions via signature matching rather than standard linking.
*   **Obfuscation Indicators:** 
    *   **Instruction Bloating/Metamorphism:** Implementation of complex modular arithmetic (e.g., `uVar16 & 3` and `% 0x43`) to mask simple operations from automated de-compilers.
    *   **Control Flow Flattening:** Intentional inclusion of "bad instructions" and overlapping code fragments to break automated analysis tools.
*   **Execution Environment:** 
    *   **VB6 Wrapper Usage:** The binary utilizes a Visual Basic 6 runtime as an execution container for script-based payloads (VBScript/VB6), likely intended to hide the final payload from static string analysis.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Staged Loading Architecture:** The binary functions as a sophisticated "stub" or loader designed to de-obfuscate and execute an embedded script-based payload (VBScript/VB6) in memory, hiding the primary malicious logic from static analysis.
*   **Advanced Evasion Techniques:** The sample utilizes high-level anti-analysis tactics, including `rdtsc` timing checks to detect debuggers/VMs, control flow flattening to break decompilers, and metamorphic instruction bloat to frustrate signature-based detection.
*   **Dynamic Resolution & Obfuscation:** It employs manual memory scanning for specific byte signatures (e.g., `0x53004d`) to bypass the Import Address Table (IAT) and utilizes complex modular arithmetic to mask its internal operations from automated tools.
