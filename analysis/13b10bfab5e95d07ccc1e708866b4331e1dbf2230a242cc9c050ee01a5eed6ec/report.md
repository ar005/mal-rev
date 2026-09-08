# Threat Analysis Report

**Generated:** 2026-09-02 21:24 UTC
**Sample:** `13b10bfab5e95d07ccc1e708866b4331e1dbf2230a242cc9c050ee01a5eed6ec_13b10bfab5e95d07ccc1e708866b4331e1dbf2230a242cc9c050ee01a5eed6ec.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13b10bfab5e95d07ccc1e708866b4331e1dbf2230a242cc9c050ee01a5eed6ec_13b10bfab5e95d07ccc1e708866b4331e1dbf2230a242cc9c050ee01a5eed6ec.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 9 sections |
| Size | 2,623,488 bytes |
| MD5 | `08bea2d932f81bd98c5213dfaf546b07` |
| SHA1 | `26d86787f10ef879f33fbf7dcbd29645b682689f` |
| SHA256 | `13b10bfab5e95d07ccc1e708866b4331e1dbf2230a242cc9c050ee01a5eed6ec` |
| Overall entropy | 7.062 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1776512764 |
| Machine | 34404 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 414,208 | 7.778 | ⚠️ Yes |
| `.managed` | 676,352 | 7.733 | ⚠️ Yes |
| `hydrated` | 0 | 0.0 | No |
| `.rdata` | 492,032 | 6.691 | No |
| `.data` | 6,656 | 3.335 | No |
| `.pdata` | 62,464 | 6.063 | No |
| `.rsrc` | 512 | 2.875 | No |
| `.reloc` | 965,632 | 4.021 | No |
| `.mrdata` | 4,608 | 7.955 | ⚠️ Yes |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegEnumKeyExW`, `RegOpenKeyExW`, `RegQueryValueExW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `TlsFree`, `TlsSetValue`, `LocalFree`, `GetTickCount64`, `CloseThreadpoolIo`, `GetCurrentProcessId`, `MultiByteToWideChar`, `GetStdHandle`, `RaiseFailFastException`, `TzSpecificLocalTimeToSystemTime`, `SystemTimeToFileTime`, `FileTimeToSystemTime`, `GetSystemTime`, `GetCurrentProcess`, `GetCurrentThread`
**ole32.dll**: `CoGetApartmentType`, `CoUninitialize`, `CoCreateGuid`, `CoWaitForMultipleHandles`, `CoInitializeEx`
**api-ms-win-crt-math-l1-1-0.dll**: `modf`, `pow`, `ceil`
**api-ms-win-crt-heap-l1-1-0.dll**: `malloc`, `calloc`, `free`, `_callnewh`
**api-ms-win-crt-string-l1-1-0.dll**: `wcsncmp`, `_stricmp`, `strcpy_s`, `strcmp`
**api-ms-win-crt-convert-l1-1-0.dll**: `strtoull`
**api-ms-win-crt-runtime-l1-1-0.dll**: `abort`, `_execute_onexit_table`, `_initterm`, `terminate`, `_register_onexit_function`, `_initialize_onexit_table`, `_cexit`, `_crt_atexit`, `_initterm_e`, `_seh_filter_dll`, `_configure_narrow_argv`, `_initialize_narrow_environment`

### Exports

`0L2xg8cH4WtqdLVPaRSC30vT8`, `0hcanLbwr8NdhEWArD4zf`, `1Xi4b8INkC`, `2JWY1TCi0Xq`, `2K2ShdKPZFDySJrIREPLqr2b0wmDn`, `2Pv0dBpt3jPds9fk`, `4Uv7aDEseGkXlo`, `5N2G8VqdBPdRAtqdGyqYM1WE1A6bLPNM`, `5ahCwqLFXKIi1THXknl4pQs`, `5nmSGV8MXGVfHCxVdW`, `6avhkLWcKYIqIj`, `7bQWH7rkne8iwpbTZiR9gWY1`, `7oNTCVYiBvjFdc4JWNBksRppU83mMgZl`, `830v0mvBMtSYpkZhzBzbMorXP2YkMR`, `9EKOea4RbECJUbF9Kj767r9IPHYWt`, `9Z61qCp5`, `AHh3fpHzyrs0uUFPFfmjyEWUUDn5PIx5`, `ASxIdaU`, `B8oaDUDvwAc9SveOCo3uRAvBFsP2X`, `BCKkTHyYXZa6wa68ftQm96j2j`, `BIWRrmNTN7P084fE`, `BPhkD5i`, `CGnlNSVqv8DAGNBHrWRJZ`, `CKHzBBHxBjcBUOmOVFHtHJ`, `Ce0CBtVcZLEAYal`, `CeqHRlp9QmDOoJAqTub9Jc`, `CpUZGPS`, `CqcfJBEW85p6ZlXz`, `EyBLGn6VOl1Im7x6xBeKVjzBPh0FLa2Q`, `F3lu4XSsbgNh6`, `FEEqZ34OVRjJHIB9UoZIL4y4rOtHC3qT`, `Fu3iJTLcVqJg5lyZqilXArILQHbDXrsY`, `GetUtfMode`, `JmPflKvtGTIaKEedhYpobJqxu7TTddsK`, `JzxddMn8HzV7QWO8pmtSY7tsKbkLt`, `LookupStringInFixedSet`, `MhBs7fn83zxaWeAeCv`, `PudiwI5H8YbZtoc`, `S4t86PqEJpyJGOwxM46gFEFwVWheM`, `TnzdwVedO`, `VvRc7QUvWDqXE`, `WhnCqiosp7`, `YN9BlFqrJ3fA6Xgq4IcW`, `Z1979pR6bdFp9YTn2lu9QV9kbzo7b9R9`, `aJSnqiVX1pncbLc7m08uBuEo9u`, `as1csjFVNNExSR8qf`, `diM9Rm88za`, `dmMQPadQVZUEvm`, `e3e5osjBGttGZFXWM`, `eOW3RZkmIMuzvaxeTVKUgOHV8FR`

## Extracted Strings

Total strings found: **4946** (showing first 100)

```
!This program cannot be run in DOS mode.
$
.managed
hydrated
.rdata
@.data
.pdata
@.rsrc
@.reloc
B.mrdata
"6-e@*
ueR;;
"6eDA^n-
"6eeA&
"6-e@*
S<A&U,I
_	c"+
#^ uv/
|A&U4*
l6+"'
}	|bTR
"+6/pL
"+jNGX
J{
}|b
X&XeSP
bA^L+=
&XvSNA
SeA&U4Ib
V|u_N!
nA&J4=4n
J"6_	i
(g}"6FR
SDA&U4IR!
nA&J4Z
_	c"+6O
tbNYKx
s#^!zZ
SDA&U4IR
nmgSzZ
_	c"+6#
X&XvS<$
i6&F0
+j GtzZ
Ol6<5`c
&OO;/A^
6
&Or;/A^
)OD^n|{
_,x\ew
A"+6IJ
bNC6

|'"6)

}6&XvSsA
+A&U4I
|bT^Ul
}(ei*V|;&
A"+jNG}zZ@
='Jn-S9A^l
AqXJ,H
H<ZX4F
kD^gzZx
"6he@>
"6hewDN
sS+6E`
X&^/xewD=
|b8>u^
3%i\|Q
}"Kb9A&
qYsV|9S
kD^gzZx
|bG}]v.
%E"M*+A&U4
aW#}|b*A
aW#}|b*A
aWL}|b*A
aWX}|b*A
aWo}|b*A
aW.}|b*A
aW@}|b*A
aW2}|b*A
aW#]|b*A
WzZ.l6
L_=O
*,XE~%
||6-j?

<h+Fpb
[Oaj8J
")0A&W
E-aL 
7UHn
a
V|&,6)

I^Mjev
l6Hxni
!#luZe
\zbzH6-r
_?_&^P
b&X-Ss
i^UuZll
-SeA3 zZ
sKc6[K
+A&U4I
"6o9A3	
```

## Disassembly Overview

Functions analyzed: **4** | Decompiled to C: **4**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry1` | `0x1802e0000` | 474 | ✓ |
| `sym.YGw1RvZJ1RFrU9dJiSVKq9f78a.dll_0L2xg8cH4WtqdLVPaRSC30vT8` | `0x180076640` | 13 | ✓ |
| `sym.YGw1RvZJ1RFrU9dJiSVKq9f78a.dll_GetUtfMode` | `0x180076600` | 13 | ✓ |
| `entry0` | `0x1800607a0` | 3 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/entry1.c`](code/entry1.c)
- [`code/sym.YGw1RvZJ1RFrU9dJiSVKq9f78a.dll_0L2xg8cH4WtqdLVPaRSC30vT8.c`](code/sym.YGw1RvZJ1RFrU9dJiSVKq9f78a.dll_0L2xg8cH4WtqdLVPaRSC30vT8.c)
- [`code/sym.YGw1RvZJ1RFrU9dJiSVKq9f78a.dll_GetUtfMode.c`](code/sym.YGw1RvZJ1RFrU9dJiSVKq9f78a.dll_GetUtfMode.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled code, here is a summary of the behavior observed in this binary.

### Core Functionality
The code functions as a **malicious loader or "packer" stub**. Its primary purpose is to decrypt and transition execution into a secondary, hidden payload (the actual malware). It performs heavy lifting to hide its true intent from static analysis by ensuring that no malicious strings or APIs are visible until the moment of execution.

### Suspicious & Malicious Behaviors
*   **Complex Decryption/De-obfuscation:** The initial loop in `entry1` uses complex arithmetic (a variation of a Linear Congruential Generator) and XOR operations to "unlock" data stored in the `.mrdata` section. This is typical for unpacking code where the actual malicious logic is encrypted on disk.
*   **Manual API Resolution (Import Obfuscation):** Instead of using a standard Import Address Table (IAT), the code manually parses system library Export Tables to find the addresses of necessary functions. 
    *   The loop checking `0x7250744e`, `0x6365746f`, and `0x72695674` is scanning for specific function names in memory. This allows the malware to call Windows APIs without those calls being visible to static analysis tools like `Strings` or standard disassemblers.
*   **Execution Flow Hijacking (Jump Patching):** The final block of `entry1` contains a classic **JMP patch**. It calculates an offset and writes the opcode `0xE9` followed by a relative address into memory: 
    `*puVar5 = 0xe9; *(puVar5 + 1) = iVar13 - (puVar5 + 5);`
    This is used to "jump" from the loader stub directly into the decrypted payload in memory.
*   **Anti-Analysis/Obfuscation:** The presence of several functions labeled `halt_baddata()` and junk strings like `YGw1RvZJ1RFrU9dJiSVKq9f78a` suggests that the binary was processed by a "crypter" or "packer." These techniques are designed to break decompilers and confuse human analysts.

### Notable Techniques & Patterns
*   **"Staged" Loading:** The code is not doing anything "malicious" (like stealing files or contacting IPs) in this specific snippet; rather, it is building the environment for a payload to do those things.
*   **Memory-Only Execution:** By resolving APIs at runtime and using jump patches, the malware ensures that its primary malicious logic never exists as an unencrypted file on the disk.
*   **Complex Indexing:** The calculation `((uVar8 & 0xf) << 8)` during the decryption phase suggests it is decrypting a table of strings or internal structures to be used later by the payload.

### Summary Conclusion
This is a **malicious packer/stub**. It uses **dynamic API resolution**, **multi-layered encryption**, and **code injection techniques (Jump Patching)** to hide its primary malicious payload from security software and analysts.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of complex decryption (LCG/XOR), junk strings, and dummy functions (`halt_baddata`) is designed to hide the binary's true purpose from static analysis. |
| T1027 | Obfuscated Files or Information | Manual API resolution skips the standard Import Address Table (IAT) to prevent automated tools from identifying the specific Windows APIs used by the malware. |
| T1055 | Process Injection | The "Jump Patch" technique and memory-only execution ensure that the primary malicious payload only exists in volatile memory, evading detection by disk-based security scanners. |

---

## Indicators of Compromise

As a threat intelligence analyst, I have reviewed the provided strings and behavioral analysis. Based on your specific criteria to exclude false positives (like standard system paths) and only include genuine IOCs:

**IP addresses / URLs / Domains**
*   None detected.

**File paths / Registry keys**
*   None detected. (Note: The references to `.mrdata`, `.rdata`, etc., are internal PE section headers, not specific file paths or registry keys).

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None detected.

**Other artifacts**
*   **Malware Type:** Identified as a **Malicious Packer/Loader Stub**.
*   **Obfuscation Technique:** Manual API Resolution (searching for `0x7250744e`, `0x6365746f`, and `0x72695674` in memory to resolve functions like `GetProcAddress` and `GetModuleHandle`).
*   **Execution Mechanism:** **Jump Patching** (utilizing the `0xE9` opcode to transition from the stub to the decrypted payload).
*   **Encryption Method:** Custom decryption loop utilizing a **Linear Congruential Generator (LCG)** variant for de-obfuscating data within the `.mrdata` section.

***

**Analyst Note:** 
The provided "Strings" segment consists primarily of high-entropy, obfuscated data typical of a packed binary. No plain-text network indicators or file system artifacts were visible because they are currently encrypted/hidden within the payload layer. The current sample serves as a **delivery vehicle** (loader) rather than the primary malware agent.

---

## Malware Family Classification

1. **Malware family**: custom (Loader/Packer Stub)
2. **Malware type**: loader
3. **Confidence**: High
4. **Key evidence**:
    *   **Manual API Resolution & Obfuscation:** The binary avoids the standard Import Address Table (IAT) by manually scanning memory for function names, a classic technique used to hide its capabilities from static analysis tools.
    *   **Execution Flow Hijacking (Jump Patching):** The use of the `0xE9` opcode to jump into decrypted code indicates the file is designed to act as a "wrapper" or stub that unpacks a primary payload in memory.
    *   **Multi-layered Encryption:** The presence of a custom Linear Congruential Generator (LCG) for decryption and junk data strings confirms it is designed specifically to evade signature-based detection by acting as a delivery vehicle.
