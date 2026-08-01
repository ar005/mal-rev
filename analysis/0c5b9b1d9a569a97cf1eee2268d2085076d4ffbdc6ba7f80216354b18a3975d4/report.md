# Threat Analysis Report

**Generated:** 2026-07-30 05:19 UTC
**Sample:** `0c5b9b1d9a569a97cf1eee2268d2085076d4ffbdc6ba7f80216354b18a3975d4_0c5b9b1d9a569a97cf1eee2268d2085076d4ffbdc6ba7f80216354b18a3975d4.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c5b9b1d9a569a97cf1eee2268d2085076d4ffbdc6ba7f80216354b18a3975d4_0c5b9b1d9a569a97cf1eee2268d2085076d4ffbdc6ba7f80216354b18a3975d4.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 4 sections |
| Size | 2,028,032 bytes |
| MD5 | `18c02b45aac69d88b3e17f119cecfa84` |
| SHA1 | `8c5addcf477a5f0426f6e1d01c802fe899fa015f` |
| SHA256 | `0c5b9b1d9a569a97cf1eee2268d2085076d4ffbdc6ba7f80216354b18a3975d4` |
| Overall entropy | 7.224 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2342666174 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,037,824 | 7.861 | ⚠️ Yes |
| `.rsrc` | 6,144 | 3.586 | No |
| `.enigma1` | 229,376 | 7.898 | ⚠️ Yes |
| `.enigma2` | 753,664 | 5.362 | No |

### Imports

**kernel32.dll**: `GetStdHandle`, `GetConsoleMode`, `TlsGetValue`, `GetLastError`, `SetLastError`, `RaiseException`, `GetTickCount`, `ExitProcess`, `GetStartupInfoA`, `GetCommandLineA`, `GetCurrentProcessId`, `GetCurrentThreadId`, `GetCurrentProcess`, `ReadProcessMemory`, `GetModuleFileNameA`
**oleaut32.dll**: `SysAllocStringLen`, `SysFreeString`, `SysReAllocStringLen`, `SafeArrayCreate`, `SafeArrayRedim`, `SafeArrayGetUBound`, `SafeArrayGetLBound`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `SafeArrayGetElement`, `SafeArrayPutElement`, `SafeArrayPtrOfIndex`, `VariantChangeTypeEx`, `VariantClear`, `VariantCopy`
**user32.dll**: `MessageBoxA`, `CharUpperBuffW`, `CharLowerBuffW`, `CharUpperA`, `CharUpperBuffA`, `CharLowerA`, `CharLowerBuffA`, `GetSystemMetrics`, `MessageBeep`
**advapi32.dll**: `RegOpenKeyA`
**ole32.dll**: `CoUninitialize`, `CoInitialize`
**ntdll.dll**: `ZwProtectVirtualMemory`, `RtlFormatCurrentUserKeyPath`, `RtlDosPathNameToNtPathName_U`, `RtlFreeUnicodeString`, `RtlInitUnicodeString`, `NtQuerySystemInformation`
**shlwapi.dll**: `PathMatchSpecW`

## Extracted Strings

Total strings found: **4529** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.enigma1
.enigma2

&*2r),

&		( 
#333333
#333333
#333333
#333333
#333333
#333333
 .r*4
lSystem.Resources.ResourceReader, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089#System.Resources.RuntimeResourceSet
fSystem.Drawing.Icon, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3ahSystem.Drawing.Bitmap, System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3aPADPADPBj
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Icon
IconData
IconSize
System.Drawing.Size
System.Drawing.Size
height
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Bitmap
IDATx^
9rdKteQ
EaxW=k
~90J=s
\[]
We>`]u
vV}28A
QSystem.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
System.Drawing.Bitmap
CIDATx^
"i{Uq/
4RTn5%
-<-K;nY
2JcQIcqIvm
<oZ]E1
E^9wW
@FB9{
LOA7{
+s~'
BC!~pM72k
N3'7iI
ylO!G0
cDTC$
xl!,l^p
unxW]
^oa"M
2JCg9&
X@t*7;
{Q
v_Bnp
vg'%9;T
Gu?Tb;G
l&K~%
dv5(7<
TRraE
QBA'%z[Tn8
J~Bx?

`#}u4
d[;r+
O	TlLu
g|~xA>`
3r]%qS&
;ce1%wG1
<i};M_
6P8_gR
vTQlA+[
A76,dQ
bQgAG&
2(22}^
;*gM=D
F-,F
5w{.x>0/~
R
;U-|
uWQL>
~iYwMy
Q*'y/AW
kifQEW
y4cA.}
1yl);Y
t4tK+f
tD^)e8
4w'/(X
\ogqoQ%gc
VC#r7tic&
>~4/(P/
8h]	:
}_4QIbA7
2[hXn
Nge!7;
AqC|54
FO:i~Q%%
XEiXW-
<	HaCou
n+E;*T
z_-tCDz
1yu[W2
*J
6S\
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.005773c0` | `0x5773c0` | 465733 | ✓ |
| `fcn.005773d0` | `0x5773d0` | 465685 | ✓ |
| `fcn.00577390` | `0x577390` | 465669 | ✓ |
| `fcn.00577360` | `0x577360` | 465653 | ✓ |
| `fcn.00577380` | `0x577380` | 465637 | ✓ |
| `fcn.005773b0` | `0x5773b0` | 465621 | ✓ |
| `fcn.005773a0` | `0x5773a0` | 465589 | ✓ |
| `fcn.00577350` | `0x577350` | 465573 | ✓ |
| `fcn.00577370` | `0x577370` | 465573 | ✓ |
| `fcn.00577340` | `0x577340` | 465429 | ✓ |
| `fcn.00577320` | `0x577320` | 465429 | ✓ |
| `fcn.00577330` | `0x577330` | 465429 | ✓ |
| `fcn.00577310` | `0x577310` | 465429 | ✓ |
| `fcn.0051b120` | `0x51b120` | 88501 | ✓ |
| `fcn.0051b130` | `0x51b130` | 88501 | ✓ |
| `fcn.00562ef0` | `0x562ef0` | 12117 | ✓ |
| `fcn.0051e960` | `0x51e960` | 6072 | ✓ |
| `fcn.00538530` | `0x538530` | 6018 | ✓ |
| `fcn.0054bc90` | `0x54bc90` | 4869 | ✓ |
| `fcn.00552870` | `0x552870` | 4793 | ✓ |
| `fcn.005063d0` | `0x5063d0` | 4409 | ✓ |
| `fcn.00553d70` | `0x553d70` | 4073 | ✓ |
| `fcn.00541b30` | `0x541b30` | 3970 | ✓ |
| `fcn.00556620` | `0x556620` | 3712 | ✓ |
| `fcn.00547700` | `0x547700` | 3461 | ✓ |
| `fcn.0051d390` | `0x51d390` | 3418 | ✓ |
| `fcn.00522070` | `0x522070` | 3305 | ✓ |
| `fcn.005577e0` | `0x5577e0` | 3138 | ✓ |
| `fcn.00544630` | `0x544630` | 2713 | ✓ |
| `fcn.00539ff0` | `0x539ff0` | 2690 | ✓ |

### Decompiled Code Files

- [`code/fcn.005063d0.c`](code/fcn.005063d0.c)
- [`code/fcn.0051b120.c`](code/fcn.0051b120.c)
- [`code/fcn.0051b130.c`](code/fcn.0051b130.c)
- [`code/fcn.0051d390.c`](code/fcn.0051d390.c)
- [`code/fcn.0051e960.c`](code/fcn.0051e960.c)
- [`code/fcn.00522070.c`](code/fcn.00522070.c)
- [`code/fcn.00538530.c`](code/fcn.00538530.c)
- [`code/fcn.00539ff0.c`](code/fcn.00539ff0.c)
- [`code/fcn.00541b30.c`](code/fcn.00541b30.c)
- [`code/fcn.00544630.c`](code/fcn.00544630.c)
- [`code/fcn.00547700.c`](code/fcn.00547700.c)
- [`code/fcn.0054bc90.c`](code/fcn.0054bc90.c)
- [`code/fcn.00552870.c`](code/fcn.00552870.c)
- [`code/fcn.00553d70.c`](code/fcn.00553d70.c)
- [`code/fcn.00556620.c`](code/fcn.00556620.c)
- [`code/fcn.005577e0.c`](code/fcn.005577e0.c)
- [`code/fcn.00562ef0.c`](code/fcn.00562ef0.c)
- [`code/fcn.00577310.c`](code/fcn.00577310.c)
- [`code/fcn.00577320.c`](code/fcn.00577320.c)
- [`code/fcn.00577330.c`](code/fcn.00577330.c)
- [`code/fcn.00577340.c`](code/fcn.00577340.c)
- [`code/fcn.00577350.c`](code/fcn.00577350.c)
- [`code/fcn.00577360.c`](code/fcn.00577360.c)
- [`code/fcn.00577370.c`](code/fcn.00577370.c)
- [`code/fcn.00577380.c`](code/fcn.00577380.c)
- [`code/fcn.00577390.c`](code/fcn.00577390.c)
- [`code/fcn.005773a0.c`](code/fcn.005773a0.c)
- [`code/fcn.005773b0.c`](code/fcn.005773b0.c)
- [`code/fcn.005773c0.c`](code/fcn.005773c0.c)
- [`code/fcn.005773d0.c`](code/fcn.005773d0.c)

## Behavioral Analysis

This updated analysis incorporates the findings from the second disassembly chunk. The additional code reinforces the conclusion that this is a highly sophisticated, professional-grade packer/loader, likely designed to host complex malware or high-value stolen intellectual property.

### Updated Analysis: Continued Evidence of Sophisticed Loader Behavior

The second chunk of disassembly provides deep insight into how the loader processes its internal "Resource" data and prepares it for injection. It reveals that the loader doesn't just move bytes; it actively **translates, maps, and reconstructs** data structures to bypass security checks.

#### 1. Advanced Manual Mapping & Structure Reconstruction
The logic surrounding `dwSize` and the subsequent `fcn.0051b140` calls shows a high degree of sophistication in how the payload is prepared for the target process:
*   **Metadata Assembly:** The code doesn't just copy one buffer; it builds a complex structure (calculated via `dwSize`) that includes multiple offsets (`0x10`, `0x20`, `0x58`, etc.) and values pulled from the source of the payload. This is characteristic of **Manual Mapping**, where the loader mimics the Windows PE Loader's behavior to map a "hidden" EXE or DLL into memory without using standard (and easily monitored) functions like `LoadLibrary`.
*   **Dynamic Relocation Table:** The loops calculating offsets for `var_5c0h` and other variables suggest that the loader is building a custom relocation table. This allows it to fix up addresses of the injected payload based on its location in memory, ensuring it can execute even if not loaded at its original base address.

#### 2. Complex Data Translation & Transformation (`fcn.00522070`)
The large function `fcn.00522070` is particularly notable for reverse engineers:
*   **Decoding/Translation Engine:** This function appears to be a "translation" loop. It iterates through data and checks for specific byte triggers (like `0x41`, `0x43`, `0x46`). 
*   **State Management:** The complex nested logic suggests it is converting the obfuscated "inner" code of the payload into a format that can be executed by the CPU. This indicates that even after unpacking, the payload remains heavily "mangled" until this specific transition occurs.

#### 3. Deep Resource Parsing (`fcn.00547700`)
This function is a massive switch-case/branching structure used for processing the internal resources:
*   **Complex State Machine:** The length and complexity suggest it handles diverse data types within the "Resource" section. It likely interprets different command codes to determine how to unpack various components (e.g., different modules, configuration files, or nested scripts).
*   **Validation & Safety:** The repeated checks for `arg_38h == 0` and the use of `IsBadWritePtr` suggest it is hardened against crashes during the unpacking process, a common trait in high-end commercial packers like Enigma.

#### 4. Orchestration of Payload Components (`fcn.00539ff0`)
This function serves as a central coordinator for the "Resource" manager:
*   **Component Linking:** It builds and links various segments of the payload together. The frequent use of `fcn.005602c0` suggests it is establishing the connections between different functions or modules within the decoded content, essentially rebuilding a functional program in memory piece-by-piece.

---

### Updated Summary Table of Suspicious Findings

| Feature | Location / Evidence | Significance |
| :--- | :--- | :--- |
| **Process Injection** | `fcn.00541b30`, `fcn.00544630` | Uses `VirtualAllocEx` and `WriteProcessMemory` to inject and potentially manually map a payload into remote memory space. |
| **Manual Mapping** | Memory calculation blocks (`dwSize`) | Shows the loader "reconstructing" the PE header/relocations for the payload, bypassing standard OS monitoring of DLL loading. |
| **Complex Translation** | `fcn.00522070` | A large translation engine that decodes or transforms internal instructions just before execution. |
| **Sophisticated Parsing** | `fcn.00547700`, `fcn.00539ff0` | Extensive, complex logic to parse a multi-layered "Resource" section containing multiple components. |
| **Obfuscation/Packing** | `@.enigma1`/`@.enigma2` | Confirmed use of Enigma Protector to hide the malicious payload from static analysis and signature detection. |

### Conclusion for Defense / Incident Response
The complexity found in Chunk 2 confirms that this is not a "script-kiddie" tool but a **professionally engineered packer**. 

*   **Detection Difficulty:** Because it uses manual mapping techniques rather than standard Windows API calls to load the final stage, signature-based detection on `LoadLibrary` or common and simple unpacking strings will likely fail.
*   **Behavioral Profile:** Monitoring for high-frequency memory allocations (`VirtualAllocEx`) followed by a "silent" jump into those regions, combined with the presence of Enigma-related artifacts, is the most reliable way to flag this specific loader. 
*   **Payload Nature:** The sheer amount of logic dedicated to translating and re-linking internal segments suggests that the final payload may be quite complex—potentially involving multiple modules or a sophisticated "plug-in" architecture for malicious functionality.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the behaviors identified in your analysis to the corresponding MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Process Injection | The loader utilizes `VirtualAllocEx` and `WriteProcessMemory` to inject and execute payload components in the memory space of a target process. |
| **T1620** | Reflective Loading Code | The use of "Manual Mapping" (reconstructing PE headers and relocation tables) allows the loader to map code without using standard Windows API calls like `LoadLibrary`. |
| **T1560** | Data Encrypted/Encoded | The transformation loop (`fcn.00522070`) indicates that the payload's "inner" instructions are kept in an encoded or mangled state until just before execution. |
| **T1027** | Obfuscated Files or System Tools | The use of the Enigma Protector and complex, multi-layered resource parsing is designed to hide the malicious functionality from static analysis and signature detection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Several strings in the "Extracted Strings" section were identified as standard .NET framework components or junk data/obfuscated blocks and have been excluded as false positives.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (Note: While "Resource" sections were mentioned, no specific filesystem paths or registry keys were provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (Note: The long strings involving `System.Drawing` and `mscorlib` are standard .NET assembly identifiers and do not constitute unique malware hashes.)

### **Other artifacts**
*   **Packer/Protector Identifiers:** 
    *   `@.enigma1`
    *   `@.enigma2`
    *   *(Signifies the use of Enigma Protector to obfuscate the payload).*
*   **Behavioral Indicators (TTPs):**
    *   **Manual Mapping:** The loader utilizes `VirtualAllocEx` and `WriteProcessMemory` to map a "hidden" executable into memory, intentionally bypassing standard Windows API monitoring like `LoadLibrary`.
    *   **Dynamic Translation Engine:** A significant translation loop (`fcn.00522070`) is used to decode and transform "mangled" instructions just before execution.
    *   **Resource Parsing State Machine:** Complex logic (`fcn.00547700` and `fcn.00539ff0`) is used to manage multi-layered resources, suggesting a modular payload structure.
*   **Suspicious Functions (Internal Offsets):** 
    *   `fcn.0051b140` (Mapping/Size calculation)
    *   `fcn.00522070` (Decoding/Translation loop)
    *   `fcn.00539ff0` (Resource management)
    *   `fcn.00541b30` / `fcn.00544630` (Injection routines)

---

## Malware Family Classification

Based on the provided analysis, here is the classification:

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**: 
    *   **Advanced Manual Mapping:** The sample employs sophisticated techniques to reconstruct PE headers and relocation tables in memory (T1620), bypassing standard Windows APIs like `LoadLibrary` to hide the final payload.
    *   **Complex Translation & Parsing:** The presence of a dedicated "translation" loop (`fcn.00522070`) and a complex state machine for resource management indicates a high-end loader designed to decode multiple layers of functionality.
    *   **Professional Obfuscation:** Use of the Enigma Protector combined with advanced process injection (T1055) confirms its role as a professional-grade delivery vehicle rather than a simple script or basic malware.
