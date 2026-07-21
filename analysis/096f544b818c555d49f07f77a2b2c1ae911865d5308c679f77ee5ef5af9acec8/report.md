# Threat Analysis Report

**Generated:** 2026-07-20 14:22 UTC
**Sample:** `096f544b818c555d49f07f77a2b2c1ae911865d5308c679f77ee5ef5af9acec8_096f544b818c555d49f07f77a2b2c1ae911865d5308c679f77ee5ef5af9acec8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `096f544b818c555d49f07f77a2b2c1ae911865d5308c679f77ee5ef5af9acec8_096f544b818c555d49f07f77a2b2c1ae911865d5308c679f77ee5ef5af9acec8.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 747,520 bytes |
| MD5 | `9e137668ec9678089ae811c375aeb8dc` |
| SHA1 | `f3c03033040ead91ec0de1a85e5475739171c9f1` |
| SHA256 | `096f544b818c555d49f07f77a2b2c1ae911865d5308c679f77ee5ef5af9acec8` |
| Overall entropy | 7.992 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2273727451 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 744,960 | 7.995 | ⚠️ Yes |
| `.rsrc` | 1,536 | 3.906 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **1895** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
 	J0 
:Jfa}L
a QTvRa}E
 Y>uxe 
b b&1nY 
 Y>uxe 
a q\
Va 
9g"f g
 t_Yuf 
:Jfa}}
a q\
Va 
9g"f g
 	J0 
cX |DNga}D
 	J0 
v4.0.30319
#Strings
Xsecb.exe
<Module>
EmbeddedAttribute
Microsoft.CodeAnalysis
Attribute
System
mscorlib
RefSafetyRulesAttribute
System.Runtime.CompilerServices
Vdasjjgfolh
Object
OKUACZTpGK99YFIsrO
mKbManRvSjKgXtW20M
Apapeseaa
Xsecb.Properties
<Module>{8c8944b9-ddf6-4b1e-b200-0c44bbf22818}
m8DE345011EB38AF
.cctor
Version
iUVnoI5oJPdM2tKcCS
XhV9aUydVgguLgG854
Boolean
UGYjp1hvTSoe7ZVJDT
DZwp5hgWEfPRuWwY2Z
Assembly
System.Reflection
GetExportedTypes
InvokeMember
String
BindingFlags
Binder
CP5WXLFY5
N6dQlM0xU
TripleDESCryptoServiceProvider
System.Security.Cryptography
MemoryStream
System.IO
GZipStream
System.IO.Compression
CryptoStream
ArgumentException
SymmetricAlgorithm
set_Mode
CipherMode
set_Key
set_IV
set_Padding
PaddingMode
CreateDecryptor
ICryptoTransform
Stream
CryptoStreamMode
ToArray
FlushFinalBlock
CompressionMode
BitConverter
ToInt32
IDisposable
Dispose
S94bFJLlqMMKv35FCI
UmqBels48dYOWsWD1u
YJN0W0nm4
LF7n955om
HDEPWM3iZJIhO0tH87
Convert
FromBase64String
LvMuIRj2dFwLmV3KIs
qKN6DiwPvQiaXDKvaT
VTlbGiI2t
ResourceManager
System.Resources
ef1itWW5Z
CultureInfo
System.Globalization
t06lGHFc91pHh2grWV
get_ResourceManager
GetTypeFromHandle
RuntimeTypeHandle
get_Assembly
get_Culture
```

## Disassembly Overview

Functions analyzed: **26** | Decompiled to C: **26**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x4020e4` | 761628 | ✓ |
| `method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.trONo971WhUcYgO94R` | `0x403de0` | 58116 | ✓ |
| `method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.fc181e715feaf46cd9a76a43e3d433331` | `0x4029cc` | 5128 | ✓ |
| `method.Xsecb.Vdasjjgfolh.N6dQlM0xU` | `0x40225c` | 1512 | ✓ |
| `method.Xsecb.Properties.Apapeseaa.get_ResourceManager` | `0x4028f0` | 140 | ✓ |
| `method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO..cctor` | `0x402858` | 124 | ✓ |
| `method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor` | `0x402064` | 108 | ✓ |
| `method.Xsecb.Properties.Apapeseaa.get_Nwrsrpmok` | `0x40298c` | 28 | ✓ |
| `method.Xsecb.Vdasjjgfolh.CP5WXLFY5` | `0x402244` | 24 | ✓ |
| `method.System.Runtime.CompilerServices.RefSafetyRulesAttribute.XhV9aUydVgguLgG854` | `0x4020d0` | 12 | ✓ |
| `method.Xsecb.Vdasjjgfolh.S94bFJLlqMMKv35FCI` | `0x402844` | 12 | ✓ |
| `method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO.LvMuIRj2dFwLmV3KIs` | `0x4028d4` | 12 | ✓ |
| `method.Xsecb.Properties.Apapeseaa.wLQZhQBavRGVYbhBbR` | `0x4029a8` | 12 | ✓ |
| `method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.KwydRrty2VUIjs04tc` | `0x403dd4` | 12 | ✓ |
| `method._Module_..cctor` | `0x402054` | 8 | ✓ |
| `method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor` | `0x40205c` | 8 | ✓ |
| `method.System.Runtime.CompilerServices.RefSafetyRulesAttribute.UGYjp1hvTSoe7ZVJDT` | `0x4020dc` | 8 | ✓ |
| `method.Xsecb.Vdasjjgfolh.UmqBels48dYOWsWD1u` | `0x402850` | 8 | ✓ |
| `method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO.qKN6DiwPvQiaXDKvaT` | `0x4028e0` | 8 | ✓ |
| `method.Xsecb.Properties.Apapeseaa..ctor` | `0x4028e8` | 8 | ✓ |
| `method.Xsecb.Properties.Apapeseaa.get_Culture` | `0x40297c` | 8 | ✓ |
| `method.Xsecb.Properties.Apapeseaa.set_Culture` | `0x402984` | 8 | ✓ |
| `method.Xsecb.Properties.Apapeseaa.D5ef9VUHeovS3gDkoh` | `0x4029b4` | 8 | ✓ |
| `method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818..ctor` | `0x4029bc` | 8 | ✓ |
| `method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818..cctor` | `0x4029c4` | 8 | ✓ |
| `method._Module_.m8DE345011EB38AF` | `0x402050` | 4 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c`](code/method.Microsoft.CodeAnalysis.EmbeddedAttribute..ctor.c)
- [`code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c`](code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute..ctor.c)
- [`code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute.UGYjp1hvTSoe7ZVJDT.c`](code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute.UGYjp1hvTSoe7ZVJDT.c)
- [`code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute.XhV9aUydVgguLgG854.c`](code/method.System.Runtime.CompilerServices.RefSafetyRulesAttribute.XhV9aUydVgguLgG854.c)
- [`code/method.Xsecb.Properties.Apapeseaa..ctor.c`](code/method.Xsecb.Properties.Apapeseaa..ctor.c)
- [`code/method.Xsecb.Properties.Apapeseaa.D5ef9VUHeovS3gDkoh.c`](code/method.Xsecb.Properties.Apapeseaa.D5ef9VUHeovS3gDkoh.c)
- [`code/method.Xsecb.Properties.Apapeseaa.get_Culture.c`](code/method.Xsecb.Properties.Apapeseaa.get_Culture.c)
- [`code/method.Xsecb.Properties.Apapeseaa.get_Nwrsrpmok.c`](code/method.Xsecb.Properties.Apapeseaa.get_Nwrsrpmok.c)
- [`code/method.Xsecb.Properties.Apapeseaa.get_ResourceManager.c`](code/method.Xsecb.Properties.Apapeseaa.get_ResourceManager.c)
- [`code/method.Xsecb.Properties.Apapeseaa.set_Culture.c`](code/method.Xsecb.Properties.Apapeseaa.set_Culture.c)
- [`code/method.Xsecb.Properties.Apapeseaa.wLQZhQBavRGVYbhBbR.c`](code/method.Xsecb.Properties.Apapeseaa.wLQZhQBavRGVYbhBbR.c)
- [`code/method.Xsecb.Vdasjjgfolh.CP5WXLFY5.c`](code/method.Xsecb.Vdasjjgfolh.CP5WXLFY5.c)
- [`code/method.Xsecb.Vdasjjgfolh.N6dQlM0xU.c`](code/method.Xsecb.Vdasjjgfolh.N6dQlM0xU.c)
- [`code/method.Xsecb.Vdasjjgfolh.S94bFJLlqMMKv35FCI.c`](code/method.Xsecb.Vdasjjgfolh.S94bFJLlqMMKv35FCI.c)
- [`code/method.Xsecb.Vdasjjgfolh.UmqBels48dYOWsWD1u.c`](code/method.Xsecb.Vdasjjgfolh.UmqBels48dYOWsWD1u.c)
- [`code/method._Module_..cctor.c`](code/method._Module_..cctor.c)
- [`code/method._Module_.m8DE345011EB38AF.c`](code/method._Module_.m8DE345011EB38AF.c)
- [`code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818..cctor.c`](code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818..cctor.c)
- [`code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818..ctor.c`](code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818..ctor.c)
- [`code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.KwydRrty2VUIjs04tc.c`](code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.KwydRrty2VUIjs04tc.c)
- [`code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.fc181e715feaf46cd9a76a43e3d433331.c`](code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.fc181e715feaf46cd9a76a43e3d433331.c)
- [`code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.trONo971WhUcYgO94R.c`](code/method._Module_8c8944b9_ddf6_4b1e_b200_0c44bbf22818.trONo971WhUcYgO94R.c)
- [`code/method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO..cctor.c`](code/method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO..cctor.c)
- [`code/method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO.LvMuIRj2dFwLmV3KIs.c`](code/method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO.LvMuIRj2dFwLmV3KIs.c)
- [`code/method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO.qKN6DiwPvQiaXDKvaT.c`](code/method.mKbManRvSjKgXtW20M.OKUACZTpGK99YFIsrO.qKN6DiwPvQiaXDKvaT.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary's functionality and characteristics.

### Core Functionality and Purpose
The binary appears to be a **loader or packer (dropper)** designed to host and execute a second-stage payload. It is heavily obfuscated, likely using a .NET-based protection layer that has been compiled into native code.

The presence of `TripleDESCryptoServiceProvider`, `GZipStream`, and `MemoryStream` in the string table indicates that the primary role of this specific executable is to:
1.  **Decrypt** an embedded resource or file (using 3DES).
2.  **Decompress** that data (using GZip).
3.  **Inject/Execute** the resulting code into memory or onto the disk.

### Suspicious and Malicious Behaviors
*   **Multi-Stage Execution:** The heavy reliance on decryption and decompression routines suggests this is not a standalone application but a "wrapper." The actual malicious logic (e.g., stealing data, installing backdoors) is likely hidden inside the encrypted payload to evade signature-based detection.
*   **Anti-Analysis / Anti-Disassembly:**
    *   **Junk Code/Obfuscation:** The decompiler output shows a massive amount of "garbage" arithmetic (e.g., `CONCAT31`, repeated additions/subtractions that result in no net change to the variable). This is used to confuse automated analysis tools and human researchers.
    *   **Overlapping Instructions:** Multiple warnings (e.g., `Instruction at (...0x40214e) overlaps instruction at (...0x40214d)`) indicate the use of **self-modifying code** or "jump" tricks designed to break disassemblers like Ghidra/IDA by creating areas where multiple instructions share the same memory space.
    *   **Opaque Predicates:** The complex nested logic in functions like `method._Module_...` are likely used to create branches that always evaluate one way but are mathematically difficult for an analyst to trace quickly.

### Notable Techniques and Patterns
*   **Encryption/Compression Stack:** The use of **Triple DES (3DES)** combined with **GZip** is a classic signature of "packer" technology (similar to those used by Crypters or common malware families like Emotet/TrickBot) to hide the final stage of an infection.
*   **Obfuscated Symbol Names:** The use of meaningless strings for internal functions (e.g., `Vdasjjgfolh`, `mKbManRvSjKgXtW20M`) is a standard technique to prevent analysts from understanding the program's logic by simply reading the function names.
*   **Runtime Decryption:** Because there are no clear "malicious" strings (like URLs or file paths) visible in the plain text, it confirms that the payload is likely decrypted only at runtime into memory, making static analysis difficult.

### Summary for Incident Response
This binary is a **high-confidence loader**. While this specific executable may not perform the final malicious act (like stealing credentials), it serves as the primary vehicle to get a hidden payload past security filters. 

**Recommended Action:** Treat any system where this binary was found as potentially compromised. The "true" malware is likely currently residing in memory or hidden within a file that was decompressed by this loader during execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1564.001** | **Packer** | The binary acts as a "wrapper" using 3DES and GZip to hide a second-stage payload, which is characteristic of packer technology. |
| **T1027** | **Obfuscated Files or Information** | The use of junk code, overlapping instructions, opaque predicates, and meaningless symbol names are all methods to hinder analysis tools and human researchers. |
| **T1055** | **Process Injection** | The analyst notes that the decrypted payload is designed to be injected into memory for execution to evade detection by security controls. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *(None found)*

**File paths / Registry keys**
*   `Xsecb.exe` (Identified as the primary executable/loader)

**Mutex names / Named pipes**
*   *(None found)*

**Hashes**
*   *(None identified. Note: The "m_..." strings appear to be internal obfuscated constants or data chunks used by the packer's logic rather than standard file hashes like MD5 or SHA-256.)*

**Other artifacts**
*   **Encryption/Compression Profile:** Triple DES (3DES) + GZip (This specific combination is a signature of multi-stage packer/crypter behavior).
*   **Antianalysis Techniques:** 
    *   Junk code (e.g., `CONCAT31` operations)
    *   Overlapping instructions
    *   Opaque predicates
*   **Loader Characteristics:** Multi-stage execution; the binary functions as a "wrapper" or "dropper" designed to decrypt and execute an embedded payload in memory.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Execution Architecture:** The use of a TripleDES encryption and GZip decompression stack indicates the binary acts as a "wrapper" designed to hide its primary payload from static analysis until runtime.
*   **Advanced Anti-Analysis Techniques:** The presence of junk code, overlapping instructions, and opaque predicates are classic hallmarks of professional malware loaders intended to frustrate automated sandboxes and human reverse engineers.
*   **Lack of Direct Malicious Activity:** The absence of clear malicious strings (URLs, IPs) in the primary binary confirms its role as a delivery vehicle; it functions by decrypting and injecting the "true" payload into memory or onto disk.
