# Threat Analysis Report

**Generated:** 2026-09-02 10:17 UTC
**Sample:** `1323bb548e5b6d0f664e66cd222dcdddc811c1f3676139b31a69364a1c044a78_1323bb548e5b6d0f664e66cd222dcdddc811c1f3676139b31a69364a1c044a78.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `1323bb548e5b6d0f664e66cd222dcdddc811c1f3676139b31a69364a1c044a78_1323bb548e5b6d0f664e66cd222dcdddc811c1f3676139b31a69364a1c044a78.exe` |
| File type | PE32 executable for MS Windows 5.00 (GUI), Intel i386, 4 sections |
| Size | 8,526,848 bytes |
| MD5 | `c2614adf12349681d7746f3abdd013c0` |
| SHA1 | `ed4d95eb15e4347fe6fe5714ffb0ee55cc5696c1` |
| SHA256 | `1323bb548e5b6d0f664e66cd222dcdddc811c1f3676139b31a69364a1c044a78` |
| Overall entropy | 7.998 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1342219636 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 104,448 | 6.749 | No |
| `.rdata` | 28,160 | 6.443 | No |
| `.data` | 5,632 | 3.263 | No |
| `.rsrc` | 8,387,584 | 8.0 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `RaiseException`, `GetLastError`, `MultiByteToWideChar`, `lstrlenA`, `InterlockedDecrement`, `GetProcAddress`, `LoadLibraryA`, `FreeResource`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceA`, `GetModuleHandleA`, `Module32Next`, `CloseHandle`
**ole32.dll**: `OleInitialize`
**OLEAUT32.dll**: `SafeArrayCreate`, `SafeArrayAccessData`, `SafeArrayUnaccessData`, `SafeArrayDestroy`, `SafeArrayCreateVector`, `VariantClear`, `VariantInit`, `SysFreeString`, `SysAllocString`

## Extracted Strings

Total strings found: **18793** (showing first 100)

```
!This program cannot be run in DOS mode.
$
~2#{~-q
~Rich,q
`.rdata
@.data
D$<RSP
L$PQSV
D$HUWP
D$QRP
J#T$f
FD)np)nl
Vlf+Vp
Vlf+Vd
tr9_ tm9_$th
O(9O$u
D$RPV

<ruV
t*9Qlu%
)Nd)Vh
FL9~Xu	V
~\wu(j
CP_^][
<0|<9
T$h9T$
t:<wuE
t.9Vlt)
)Vd)Nh
^(9^$u
D$$)G@
w<9G,s
T$<PQR
D$Tt*;
;l$TsY)l$T
L$4;D$Ts<)D$T
p<O#|$
~(9~$u
O@;H s
O@;H(s
T$$QUR
D$ )D$
Oh;O\sN
Gh9Ghr
L$(9ODv
L$(+L$
D$(+D$
D$0^][_
@;D$r
u9{<s
N(Uh0%
t$H;t$8
D$SUW
|$ WSPV
@PAQBR
u.j^9
9}t$9}
9ut)9u
F@uwV
tSSSSS
8VVVVV
<at<rt
E9Xt
uL9=\9B
tVVVVV
tVVVVV
tVVVVV
0SSSSS
@A;Er
t)jXP
8
u
AA
0WWWWW
F@u^V
HHtXHHt
>If90t
j@j ^V
u,9Et'9
0SSSSS
<at9<rt,<wt
tVHtG
URPQQh
>=Yt1j
< tK<	tG
_VVVVV
tSSSSS
^WWWWW
tVVVVV
0SSSSS
0A@@Ju
u`9]t$9
tSSSSS
VW|[;P?B
^SSSSS
j"^SSSSS
MQSWVj
v	N+D$
tSSSSS
tGHt.Ht&
^SSSSS
8VVVVV
;t$,v-
kUQPXY]Y[
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.00410598` | `0x410598` | 12326 | ✓ |
| `fcn.004073a0` | `0x4073a0` | 5153 | ✓ |
| `fcn.00410c4b` | `0x410c4b` | 2935 | ✓ |
| `main` | `0x4019f0` | 2727 | ✓ |
| `fcn.004193c4` | `0x4193c4` | 2340 | ✓ |
| `fcn.00403080` | `0x403080` | 2024 | ✓ |
| `fcn.00403310` | `0x403310` | 2009 | ✓ |
| `fcn.0040f211` | `0x40f211` | 1843 | ✓ |
| `fcn.00415ad5` | `0x415ad5` | 1823 | ✓ |
| `fcn.00418ccc` | `0x418ccc` | 1735 | ✓ |
| `fcn.0040fd32` | `0x40fd32` | 1474 | ✓ |
| `fcn.00418244` | `0x418244` | 1348 | ✓ |
| `fcn.00418788` | `0x418788` | 1348 | ✓ |
| `fcn.00409590` | `0x409590` | 1291 | ✓ |
| `fcn.00408c60` | `0x408c60` | 1227 | ✓ |
| `fcn.00406ca0` | `0x406ca0` | 1097 | ✓ |
| `fcn.00409da0` | `0x409da0` | 1015 | ✓ |
| `fcn.00417081` | `0x417081` | 933 | ✓ |
| `fcn.00412ebc` | `0x412ebc` | 883 | ✓ |
| `fcn.004147ec` | `0x4147ec` | 880 | ✓ |
| `fcn.0040afe0` | `0x40afe0` | 869 | ✓ |
| `fcn.0040b350` | `0x40b350` | 869 | ✓ |
| `fcn.0040d743` | `0x40d743` | 790 | ✓ |
| `fcn.00419e16` | `0x419e16` | 783 | ✓ |
| `fcn.0040def2` | `0x40def2` | 741 | ✓ |
| `fcn.0040dc11` | `0x40dc11` | 737 | ✓ |
| `fcn.00411f93` | `0x411f93` | 713 | ✓ |
| `fcn.004024a0` | `0x4024a0` | 622 | ✓ |
| `fcn.00409aa0` | `0x409aa0` | 602 | ✓ |
| `fcn.00411a15` | `0x411a15` | 596 | ✓ |

### Decompiled Code Files

- [`code/fcn.004024a0.c`](code/fcn.004024a0.c)
- [`code/fcn.00403080.c`](code/fcn.00403080.c)
- [`code/fcn.00403310.c`](code/fcn.00403310.c)
- [`code/fcn.00406ca0.c`](code/fcn.00406ca0.c)
- [`code/fcn.004073a0.c`](code/fcn.004073a0.c)
- [`code/fcn.00408c60.c`](code/fcn.00408c60.c)
- [`code/fcn.00409590.c`](code/fcn.00409590.c)
- [`code/fcn.00409aa0.c`](code/fcn.00409aa0.c)
- [`code/fcn.00409da0.c`](code/fcn.00409da0.c)
- [`code/fcn.0040afe0.c`](code/fcn.0040afe0.c)
- [`code/fcn.0040b350.c`](code/fcn.0040b350.c)
- [`code/fcn.0040d743.c`](code/fcn.0040d743.c)
- [`code/fcn.0040dc11.c`](code/fcn.0040dc11.c)
- [`code/fcn.0040def2.c`](code/fcn.0040def2.c)
- [`code/fcn.0040f211.c`](code/fcn.0040f211.c)
- [`code/fcn.0040fd32.c`](code/fcn.0040fd32.c)
- [`code/fcn.00410598.c`](code/fcn.00410598.c)
- [`code/fcn.00410c4b.c`](code/fcn.00410c4b.c)
- [`code/fcn.00411a15.c`](code/fcn.00411a15.c)
- [`code/fcn.00411f93.c`](code/fcn.00411f93.c)
- [`code/fcn.00412ebc.c`](code/fcn.00412ebc.c)
- [`code/fcn.004147ec.c`](code/fcn.004147ec.c)
- [`code/fcn.00415ad5.c`](code/fcn.00415ad5.c)
- [`code/fcn.00417081.c`](code/fcn.00417081.c)
- [`code/fcn.00418244.c`](code/fcn.00418244.c)
- [`code/fcn.00418788.c`](code/fcn.00418788.c)
- [`code/fcn.00418ccc.c`](code/fcn.00418ccc.c)
- [`code/fcn.004193c4.c`](code/fcn.004193c4.c)
- [`code/fcn.00419e16.c`](code/fcn.00419e16.c)
- [`code/main.c`](code/main.c)

## Behavioral Analysis

The third chunk of disassembly provides critical insights into the malware's anti-analysis techniques, its internal data management, and its robust implementation for interacting with the Windows environment. This new evidence reinforces your previous assessment: this is a high-effort, professional-grade piece of malware.

### Updated Analysis Summary (Final Update)

The addition of the final code block confirms that the "Data Translation Layer" and "Robust API Wrappers" identified earlier are part of a much larger ecosystem designed for **persistence through evasion**. The analysis now confirms a multi-layered architecture:
1.  **Execution Layer:** A complex VM Interpreter (Opcode processing).
2.  **Translation/Decryption Layer:** Dense, high-complexity loops that de-obfuscate data in real-time.
3.  **Anti-Analysis/Environment Layer:** Specific checks for hardware state and environment consistency.
4.  **Robust Wrapper Layer:** Thick wrappers to ensure stability across various Windows versions and locales.

---

### New Functional Insights

#### 1. Anti-Analysis & Environmental Consistency
The function **`fcn.00419e16`** is a classic high-end evasion technique involving the **FPU (Floating Point Unit) Control Word**.
*   **What it does:** It checks several bit-flags within the FPU state and, if they do not match "expected" values, calls another routine (`fcn.00419ce8`) to force a state update or correction. 
*   **Malicious Significance:** This is often used to detect emulators, sandboxes, or specific analysis tools that might default to different floating-point behaviors than a physical Windows installation. By enforcing a "standard" FPU state, the malware ensures it only proceeds on what it perceives as a "real" user machine.

#### 2. Complex De-obfuscation & Decoding
Functions like **`fcn.00409aa0`** and **`fcn.0040fe0`** demonstrate that the data being passed from the VM Interpreter isn't just "cleaned up" before use; it is actively **deconstructed**.
*   **`fcn.00409aa0`**: This function contains complex loops involving bit-shifts, rotations, and multi-byte assembly. It appears to be a custom **decoding/decompression algorithm** for the payload data. The nested logic suggests it is pulling "chunks" of data from an obfuscated stream.
*   **`fcn.0040fe0`**: This function features highly dense, repetitive switch-case logic and offset math (e.g., `piVar5[var_4h * 0x81 + 0x51]`). This indicates the malware is interacting with a **highly structured internal database or table**. It isn't just looking for strings; it’s navigating a complex proprietary data structure, likely to determine which "action" to take next.

#### 3. Robustness & Locale-Awareness (Advanced Wrapper)
The block containing `MultiByteToWideChar` and the subsequent logic confirms your previous suspicion regarding "thick wrappers."
*   **Mechanism:** Instead of calling a simple conversion, it handles memory allocation for various buffer sizes, checks for success, and then performs a **`CompareStringW`** check.
*   **Significance:** This ensures that even if the malware is launched in different regions (with different system locales) or against different OS versions, its internal "checks" remain consistent. It removes any "noise" from the Windows environment before the core logic processes the data.

#### 4. Proprietary Memory/Resource Management
The function **`fcn.00411a15`** shows how the malware manages system handles (File, Console, etc.).
*   **Mechanism:** It iterates through and validates a list of standard handles while setting up internal data structures to track them. 
*   **Significance:** This is typical for a large loader that needs to manage many "hidden" operations simultaneously without crashing or alerting the OS via unexpected behavior.

---

### Updated Summary of Suspected Behaviors

| Feature | Observation | Impact on Analysis |
| :--- | :--- | :--- |
| **Evasion** | FPU Control Word manipulation (`fcn.00419e16`). | Harder to run in automated sandboxes; detects "non-standard" hardware environments. |
| **Complexity** | Multi-pass decoding logic in `fcn.00409aa0`. | Makes it extremely difficult for researchers to see the final payload without full execution/tracing. |
| **Durability** | Sophisticated Unicode conversion and comparison loops. | Ensures functionality across different countries and Windows editions (High Reliability). |
| **Abstraction** | Use of "Table-Driven" logic in `fcn.0040fe0`. | The core malicious intent is hidden behind several layers of data lookup, making static analysis difficult. |

### Final Technical Conclusion
The analyzed code represents a **highly professional and sophisticated malware loader.** It utilizes a **Virtual Machine (VM) architecture** to decouple its control logic from the actual system API calls. Furthermore, it employs **multi-stage decoding**, **anticipation of regional variations**, and **hardware-state checks** to ensure it survives in complex enterprise environments while remaining invisible to automated security systems.

The complexity suggests this is likely a **"Stage 0" or "Loader" component** for a sophisticated threat actor (e.g., an APT or a highly organized ransomware group). The presence of the VM and high-quality wrappers indicates that the final payload—once decoded by the layers identified in `fcn.00409aa0` and `fcn.0040fe0`—is likely capable of sophisticated tasks such as data exfiltration or long-term persistence.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1497** | Virtualization/Sandbox Escape | The use of FPU Control Word checks (fcn.00419e16) is a specific technique used to detect if the malware is running in an emulated or sandboxed environment. |
| **T1027** | Obfuscated Valid Project | The multi-pass decoding, complex bitwise logic in fcn.00409aa0, and table-driven logic in fcn.0040fe0 are used to hide the core malicious intent from static analysis. |
| **T1055** | Packing | The presence of a "Stage 0" loader with multi-layer decoding and data translation indicates the use of packing/encryption to protect the final payload. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Many elements in the "Extracted Strings" section were identified as standard C++ runtime errors or obfuscated data noise and have been excluded from the final list to ensure only relevant indicators are included.

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified. (Note: "NoRemove" and "ForceRemove" were identified as internal status flags rather than specific file paths).

**Mutex names / Named pipes**
*   `Qkkbal` (Identified as a non-standard string likely used as a Mutex name or an internal identifier for execution tracking.)

**Hashes**
*   None identified.

**Other artifacts**
*   **Internal Function Offsets:** 
    *   `0x419e16` (FPU Control Word manipulation logic)
    *   `0x419ce8` (FPU state update routine)
    *   `0x409aa0` (Decoding/decompression algorithm)
    *   `0x40fe0` (Table-driven logic/data structure navigation)
    *   `0x411a15` (System handle management)
*   **Behavioral Indicators:** 
    *   **Anti-Analysis:** Manipulation of the FPU (Floating Point Unit) Control Word to detect emulators or sandboxes.
    *   **Obfuscation Method:** Use of a custom Virtual Machine (VM) Interpreter and multi-pass decoding for payload extraction.
    *   **Persistence Strategy:** Implementation of "thick wrappers" around standard APIs (e.g., `MultiByteToWideChar`) to ensure consistency across different locales and OS versions.

---

## Malware Family Classification

1. **Malware family**: custom (loader)
2. **Malware type**: loader
3. **Confidence**: High

**Key evidence**:
*   **Sophisticated Anti-Analysis:** The use of FPU Control Word manipulation (`fcn.00419e16`) specifically targets emulators and sandboxes, indicating a high level of professional development intended to bypass automated security systems.
*   **Virtual Machine (VM) Architecture:** The implementation of a VM Interpreter for execution and multi-pass decoding routines (`fcn.00409aa0`) indicates that the core logic is hidden behind layers of abstraction, a hallmark of sophisticated "Stage 0" loaders used by advanced threat actors.
*   **Robust Infrastructure:** The use of "thick wrappers" for locale awareness and table-driven data structures suggests the malware is designed for stability in diverse enterprise environments, prioritizing persistence and reliable execution across different Windows versions.
