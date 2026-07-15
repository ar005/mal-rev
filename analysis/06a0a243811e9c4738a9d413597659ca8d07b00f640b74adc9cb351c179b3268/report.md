# Threat Analysis Report

**Generated:** 2026-07-15 08:13 UTC
**Sample:** `06a0a243811e9c4738a9d413597659ca8d07b00f640b74adc9cb351c179b3268_06a0a243811e9c4738a9d413597659ca8d07b00f640b74adc9cb351c179b3268.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `06a0a243811e9c4738a9d413597659ca8d07b00f640b74adc9cb351c179b3268_06a0a243811e9c4738a9d413597659ca8d07b00f640b74adc9cb351c179b3268.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 4 sections |
| Size | 120,288 bytes |
| MD5 | `ee75b57b9300aab96530503bfae8a2f2` |
| SHA1 | `98dd757e1c1fa8b5605bda892aa0b82ebefa1f07` |
| SHA256 | `06a0a243811e9c4738a9d413597659ca8d07b00f640b74adc9cb351c179b3268` |
| Overall entropy | 5.258 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1701779761 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 512 | 2.78 | No |
| `.rdata` | 512 | 3.511 | No |
| `.rsrc` | 93,696 | 4.135 | No |
| `.reloc` | 512 | 0.222 | No |

### Imports

**PCICL32.dll**: `_NSMClient32@8`
**KERNEL32.dll**: `GetCommandLineW`, `ExitProcess`, `GetModuleHandleW`, `GetStartupInfoW`

## Extracted Strings

Total strings found: **283** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.rsrc
@.reloc
_NSMClient32@8
PCICL32.dll
ExitProcess
GetModuleHandleW
GetStartupInfoW
GetCommandLineW
KERNEL32.dll
E:\nsmsrc\nsm\1410\1410\client32\release_unicode\client32.pdb
7>=>>>>>>=>>>>>>>>>>E
	
4404000040+0*4040-0>
	
4040-cj6**>kH'0-fh4>
	
4400*t
	
404-*j
h'*x{6;
	
4400*t
C#x}6;
	
4-4-*j
z-t{6;
	
4440*r{G
	
44-0*j
	
4-4-*j
c'006"I
	
4440*j
}6*4000*r
	
44-0*h
E'40404'>
	
4-44->@-+040401*@>0>
	
44404*(060040406)*4>
	
44-4044004004000040=
	
4-40404040400404004>
	
4440040404040040400>
	
44-4004040404004040>
	
4-40400404040400404>
	
4440040040404040040>
	
44-4004004040404004>
4-40400400404040400>
4440040040040404040>
44-4004004004040404>
omXY^]
4040400400400404040>
44-4040040040040404>
4040404004004004040=
44-4040400400400404>
4-40404040040040040=
mq\^^^^\
4440040404004004004>
SLLQLOSL
44-4004040400400400>J
7===>==>=>=>==>==>=>C
1,+///*//
G8
!CJ(
P6TLDW*3S.*
P7:Y/(WB;O,*
G:!%&&
./,/,////
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3">
<assemblyIdentity
    version="10.0.0.0"
    processorArchitecture="X86"
    name="NetSupport Client"
    type="win32"
/>
<description>NetSupport Manager Remote Control.</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel level="asInvoker" />
      </requestedPrivileges>
    </security>
  </trustInfo>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>

<asmv3:application>
  <asmv3:windowsSettings>
    <dpiAware xmlns="http://schemas.microsoft.com/SMI/2005/WindowsSettings">true</dpiAware>
    <dpiAwareness xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings">PerMonitorV2</dpiAwareness>
  </asmv3:windowsSettings>
</asmv3:application>

</assembly>

PADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGXXPADDINGPADDINGX
GlobalSign Root CA - R31

GlobalSign1

GlobalSign0
200728000000Z
290318000000Z0S10	
GlobalSign nv-sa1)0'
 GlobalSign Code Signing Root R450
p\$x %
!http://ocsp.globalsign.com/rootr30;
/http://secure.globalsign.com/cacert/root-r3.crt06
%http://crl.globalsign.com/root-r3.crl0G
&https://www.globalsign.com/repository/0
{Z3ng
0S10	
GlobalSign nv-sa1)0'
 GlobalSign Code Signing Root R450
200728000000Z
300728000000Z0\10	
GlobalSign nv-sa1200
)GlobalSign GCC R45 EV CodeSigning CA 20200
```

## Disassembly Overview

Functions analyzed: **3** | Decompiled to C: **3**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x401020` | 155 | ✓ |
| `main` | `0x401000` | 20 | ✓ |
| `sub.PCICL32.dll__NSMClient32_8` | `0x4010bc` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/main.c`](code/main.c)
- [`code/sub.PCICL32.dll__NSMClient32_8.c`](code/sub.PCICL32.dll__NSMClient32_8.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is the analysis of the binary sample:

### Core Functionality and Purpose
The binary appears to be a legitimate component of **NetSupport Manager**, a commercial remote desktop and computer management software. 

*   **Application Identity:** The presence of strings like `NetSupport Client`, `NetSupport Manager Remote Control`, and the certificate information for `NETSUPPORT LTD.` confirms its identity as a professional remote management tool.
*   **Standard Entry Point:** The `entry0` function follows standard Windows procedure logic: it parses the command line, retrieves startup information, and initializes the environment before handing off execution to the main application logic (the `main` function).
*   **Library Integration:** The primary functionality is delegated to an external library/module (`PCICL32.dll`).

### Suspicious or Malicious Behaviors
No inherently malicious behaviors (such as process injection, obfuscation, or anti-analysis techniques) were detected in the provided code snippet. However, it is important to note:

*   **Dual-Use Nature:** While the code itself is standard for its intended purpose, NetSupport Manager is a "dual-use" tool. Because it provides legitimate remote control capabilities, it is frequently used by threat actors as a backdoor or Remote Access Trojan (RAT) component because of its ability to manage systems remotely.
*   **Standard API Usage:** The use of `GetCommandLineW`, `GetStartupInfoW`, and `GetModuleHandleW` are standard requirements for any Win32 application and do not indicate malicious intent on their own.

### Notable Techniques or Patterns
*   **Standard Boilerplate:** The `entry0` function is a typical "wrapper" generated by compilers/linkers to handle the transition from the OS entry point to the program's main logic.
*   **Linker Artifacts:** The inclusion of `.pdb` paths (e.g., `E:\nsmsrc\nsm\...`) and extensive certificate chains in the string table indicate a professionally developed, signed production binary rather than a hastily crafted piece of malware. 

### Summary for Incident Response
This specific sample appears to be **non-malicious** code belonging to a known remote management suite. If this file was found on a system where it was not intentionally installed by an administrator, it could indicate that a threat actor is using legitimate administrative tools to maintain persistence or move laterally within the network.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1133 | External Remote Services | The analysis identifies the software as a tool for remote control and management, which can be used by threat actors to establish unauthorized access or as part of a Remote Access Trojan (RAT). |

---

## Indicators of Compromise

As a threat intelligence analyst, I have analyzed the provided strings and behavioral reports. Because the sample is identified as a **dual-use** tool (NetSupport Manager), there are no immediate indicators of malicious infrastructure (such as C2 domains or malicious IPs). However, several artifacts identify the specific software and its development environment.

### **IOCs Identified**

**IP addresses / URLs / Domains**
*   *None* (All identified URLs in the strings—e.g., `globalsign.com`—are standard Certificate Authority verification points and are not malicious.)

**File paths / Registry keys**
*   `E:\nsmsrc\nsm\1410\1410\client32\release_unicode\client32.pdb` (Note: This is a developer path; while not an active infection indicator, it identifies the build environment for the NetSupport software.)

**Mutex names / Named pipes**
*   None detected.

**Hashes**
*   None provided in the source text.

**Other artifacts**
*   **Application Names:** `NetSupport Client`, `NetSupport Manager Remote Control`
*   **Organization Identity:** `NETSUPPORT LTD.`
*   **Email Contact:** `is@netsupportsoftware.com` 
*   **Module Name:** `PCICL32.dll`

---
### **Analyst Notes**
The analysis confirms that this sample is a legitimate, signed binary of the NetSupport remote management suite. While no "malicious" IOCs (like command-and-control IPs) were found, the presence of this specific software on an endpoint should be flagged for investigation if it was not authorized by IT administration, as it can be used by threat actors to facilitate remote access and lateral movement.

---
**Regex-extracted plaintext IOCs** *(from static strings + decompiled C)*

**URLs:**
- `http://crl.globalsign.com/ca/gstsacasha384g4.crl0`
- `http://crl.globalsign.com/codesigningrootr45.crl0U`
- `http://crl.globalsign.com/gsgccr45evcodesignca2020.crl0$`
- `http://crl.globalsign.com/root-r3.crl0G`
- `http://crl.globalsign.com/root-r6.crl0G`
- `http://ocsp.globalsign.com/ca/gstsacasha384g40C`
- `http://ocsp.globalsign.com/codesigningrootr450F`
- `http://ocsp.globalsign.com/gsgccr45evcodesignca20200U`
- `http://ocsp.globalsign.com/rootr30`
- `http://ocsp2.globalsign.com/rootr606`
- `http://schemas.microsoft.com/SMI/2005/WindowsSettings`
- `http://schemas.microsoft.com/SMI/2016/WindowsSettings`
- `http://secure.globalsign.com/cacert/codesigningrootr45.crt0A`
- `http://secure.globalsign.com/cacert/gsgccr45evcodesignca2020.crt0?`
- `http://secure.globalsign.com/cacert/gstsacasha384g4.crt0`
- `http://secure.globalsign.com/cacert/root-r3.crt06`
- `https://www.globalsign.com/repository/0`

---

## Malware Family Classification

1. **Malware family**: Unknown (Identified as NetSupport Manager)
2. **Malware type**: Non-malicious / Dual-use Tool
3. **Confidence**: High
4. **Key evidence**:
*   **Authentic Corporate Signature:** The presence of clear certificate information for "NETSUPPORT LTD." and standardized `.pdb` paths indicates a professional, signed commercial product rather than custom-built malware.
*   **Lack of Malicious Indicators:** The analysis found no evidence of common malware techniques such as process injection, code obfuscation, anti-debugging measures, or hardcoded malicious C2 infrastructure.
*   **Dual-Use Functionality:** While the software is a legitimate remote management tool and not inherently "malware," it possesses capabilities (remote access/control) that can be exploited by threat actors to maintain persistence or move laterally within a network.
