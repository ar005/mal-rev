# Threat Analysis Report

**Generated:** 2026-07-15 08:11 UTC
**Sample:** `06a084722d72aa9e7e49a72e2c2584b9c8f4566c55e8db6521da8cf367a2b8c7_06a084722d72aa9e7e49a72e2c2584b9c8f4566c55e8db6521da8cf367a2b8c7.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `06a084722d72aa9e7e49a72e2c2584b9c8f4566c55e8db6521da8cf367a2b8c7_06a084722d72aa9e7e49a72e2c2584b9c8f4566c55e8db6521da8cf367a2b8c7.exe` |
| File type | PE32 executable for MS Windows 6.00 (console), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,308,672 bytes |
| MD5 | `99bfdc2576148bfe62b9534be5bf4d70` |
| SHA1 | `9e3546270d9dcb3ddef441e73e795a427ced4a22` |
| SHA256 | `06a084722d72aa9e7e49a72e2c2584b9c8f4566c55e8db6521da8cf367a2b8c7` |
| Overall entropy | 7.917 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 3316276488 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,301,504 | 7.926 | ⚠️ Yes |
| `.rsrc` | 6,144 | 4.136 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **4009** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc

-7	{%
	,?	o1

-4	{%
0}~YYYt
D1ogNy
Q9xEd^@
HO{;Gz
4$]sHC+ix
"=/<Dz^d
~^i|Qi|Ii|
v	.5iK
w	~hCYn
4'/17 k
\_ioBY
TX<@)*
Tti:m{
5M#0Pk
*$~HaQ
'VNc4h 
?(t)J{
R/v*t!
-3~!V,
9J\9Zl
G,==9>
C4{z`ms
?NT=+Y
9]8'ob&
}K\Lomj
b~be\f
Zck(0)
[MN';H"D
iM[kK[k:=
kF{\f<=
))yc&6
T*:zq3
|Zcr%mb
sfl=v \g
HK1CK1
c}"-E"-EBK
h-RRm'y
ZHZIX\g4
P\ZeH/
2{>Qs9Je{A
 Kh=+{

c-N5K
OXp@)

L7P/&C
)Gx|1=
WgUF'
jH
b.\N@P 
[3lp6'SK
cMeLyl"1
e64=S8
g#{ufKiV
/[k3V]
#{^nM8
JK>E_p
<OP'-(u;
t~|R6K
vUtB~Y
ogjj4X
445u62
m[)MU6
\WG,G
b#Pmn<GNk6
IUK7C?
LK[!C2
hI7_g
N)J;flzzJ>
'L-3*e
5$G(23
oeHvT
X b	zX
+ic]j&
t,<
VZ
Ee-hzA
KGbGh-
Pbd)L
^_
4MYA},
VqA|0<BQJ
z 4&@3
a#1bDa
$|Wo09.
PI'EMla<
):Z`M

Y 6 :1?
-<0z'
h:B\Z{i
X.2l'
46+K.BMx#R
<SFODN
\O@"L*f<
m<	NHMx*
80/<S@
%LD$&"
%:;f4t
(>5x[8$
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **28**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method._ReadAllAsync_d__7_1.System.Collections.Generic.IAsyncEnumerator_T_.get_Current` | `0x402ff3` | 1302838 | ✓ |
| `sym.Costura.AssemblyLoader.LoadStream` | `0x4127a4` | 1239428 | ✓ |
| `method.Sharphound.Producers.LdapProducer.GetPartitionedFilter` | `0x40ff67` | 143500 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x412bbc` | 64488 | ✓ |
| `method.Sharphound.Writers.JsonDataWriter_1.GetFilename` | `0x4063bf` | 8291 | ✓ |
| `method._ProcessComputerObject_d__25.MoveNext` | `0x4098ac` | 4824 | ✓ |
| `method.Sharphound.Producers.StealthContext.GetSearchResultEntries` | `0x4111a9` | 3177 | ✓ |
| `method.__c._BuildRecursiveDomainList_b__5_1` | `0x404c0d` | 3070 | ✓ |
| `method._ProcessEnterpriseCA_d__34.MoveNext` | `0x40ccbc` | 2884 | ✓ |
| `method._BuildRecursiveDomainList_d__5.System.Threading.Tasks.Sources.IValueTaskSource.GetResult` | `0x405841` | 2628 | ✓ |
| `method._GetPartitionedFilter_d__2.System.Collections.IEnumerable.GetEnumerator` | `0x410803` | 2470 | — |
| `method.Sharphound.Options.set_StatusInterval` | `0x403465` | 2393 | ✓ |
| `method._ProduceConfigNC_d__3.MoveNext` | `0x41080c` | 2320 | — |
| `method._StartWriter_d__23.MoveNext` | `0x40e9ec` | 2024 | ✓ |
| `method._ProcessDomainObject_d__28.MoveNext` | `0x40b33c` | 1764 | ✓ |
| `method._Produce_d__1.MoveNext` | `0x40ffc4` | 1756 | ✓ |
| `method._ProcessObject_d__22.MoveNext` | `0x408b30` | 1728 | ✓ |
| `method._FindPathTargetSids_d__10.MoveNext` | `0x411e24` | 1700 | ✓ |
| `method._ProcessUserObject_d__24.MoveNext` | `0x409228` | 1652 | ✓ |
| `sym._Produce_d__1.MoveNext` | `0x40f8cc` | 1516 | ✓ |
| `method._StartCollection_d__11.MoveNext` | `0x406c20` | 1508 | ✓ |
| `method._ConsumeSearchResults_d__12.MoveNext` | `0x407214` | 1424 | ✓ |
| `method._FlushWriters_d__24.MoveNext` | `0x40f1e4` | 1424 | ✓ |
| `method._ConsumeSearchResults_d__0.MoveNext` | `0x407810` | 1416 | ✓ |
| `method._ProcessOUObject_d__30.MoveNext` | `0x40bce4` | 1268 | ✓ |
| `method._BuildRecursiveDomainList_d__5.MoveNext` | `0x405260` | 1252 | ✓ |
| `method._ProcessGroupObject_d__27.MoveNext` | `0x40ae48` | 1252 | ✓ |
| `method._GetDomainsForEnumeration_d__4.MoveNext` | `0x404dc8` | 1124 | ✓ |
| `method._StartCollection_d__1.MoveNext` | `0x403fec` | 1084 | ✓ |
| `method.__Main_b__1_d.MoveNext` | `0x4039a4` | 1036 | ✓ |

### Decompiled Code Files

- [`code/method.Costura.AssemblyLoader.Attach.c`](code/method.Costura.AssemblyLoader.Attach.c)
- [`code/method.Sharphound.Options.set_StatusInterval.c`](code/method.Sharphound.Options.set_StatusInterval.c)
- [`code/method.Sharphound.Producers.LdapProducer.GetPartitionedFilter.c`](code/method.Sharphound.Producers.LdapProducer.GetPartitionedFilter.c)
- [`code/method.Sharphound.Producers.StealthContext.GetSearchResultEntries.c`](code/method.Sharphound.Producers.StealthContext.GetSearchResultEntries.c)
- [`code/method.Sharphound.Writers.JsonDataWriter_1.GetFilename.c`](code/method.Sharphound.Writers.JsonDataWriter_1.GetFilename.c)
- [`code/method._BuildRecursiveDomainList_d__5.MoveNext.c`](code/method._BuildRecursiveDomainList_d__5.MoveNext.c)
- [`code/method._BuildRecursiveDomainList_d__5.System.Threading.Tasks.Sources.IValueTaskSource.GetResult.c`](code/method._BuildRecursiveDomainList_d__5.System.Threading.Tasks.Sources.IValueTaskSource.GetResult.c)
- [`code/method._ConsumeSearchResults_d__0.MoveNext.c`](code/method._ConsumeSearchResults_d__0.MoveNext.c)
- [`code/method._ConsumeSearchResults_d__12.MoveNext.c`](code/method._ConsumeSearchResults_d__12.MoveNext.c)
- [`code/method._FindPathTargetSids_d__10.MoveNext.c`](code/method._FindPathTargetSids_d__10.MoveNext.c)
- [`code/method._FlushWriters_d__24.MoveNext.c`](code/method._FlushWriters_d__24.MoveNext.c)
- [`code/method._GetDomainsForEnumeration_d__4.MoveNext.c`](code/method._GetDomainsForEnumeration_d__4.MoveNext.c)
- [`code/method._ProcessComputerObject_d__25.MoveNext.c`](code/method._ProcessComputerObject_d__25.MoveNext.c)
- [`code/method._ProcessDomainObject_d__28.MoveNext.c`](code/method._ProcessDomainObject_d__28.MoveNext.c)
- [`code/method._ProcessEnterpriseCA_d__34.MoveNext.c`](code/method._ProcessEnterpriseCA_d__34.MoveNext.c)
- [`code/method._ProcessGroupObject_d__27.MoveNext.c`](code/method._ProcessGroupObject_d__27.MoveNext.c)
- [`code/method._ProcessOUObject_d__30.MoveNext.c`](code/method._ProcessOUObject_d__30.MoveNext.c)
- [`code/method._ProcessObject_d__22.MoveNext.c`](code/method._ProcessObject_d__22.MoveNext.c)
- [`code/method._ProcessUserObject_d__24.MoveNext.c`](code/method._ProcessUserObject_d__24.MoveNext.c)
- [`code/method._Produce_d__1.MoveNext.c`](code/method._Produce_d__1.MoveNext.c)
- [`code/method._ReadAllAsync_d__7_1.System.Collections.Generic.IAsyncEnumerator_T_.get_Current.c`](code/method._ReadAllAsync_d__7_1.System.Collections.Generic.IAsyncEnumerator_T_.get_Current.c)
- [`code/method._StartCollection_d__1.MoveNext.c`](code/method._StartCollection_d__1.MoveNext.c)
- [`code/method._StartCollection_d__11.MoveNext.c`](code/method._StartCollection_d__11.MoveNext.c)
- [`code/method._StartWriter_d__23.MoveNext.c`](code/method._StartWriter_d__23.MoveNext.c)
- [`code/method.__Main_b__1_d.MoveNext.c`](code/method.__Main_b__1_d.MoveNext.c)
- [`code/method.__c._BuildRecursiveDomainList_b__5_1.c`](code/method.__c._BuildRecursiveDomainList_b__5_1.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)
- [`code/sym._Produce_d__1.MoveNext.c`](code/sym._Produce_d__1.MoveNext.c)

## Behavioral Analysis

This final chunk of disassembly provides the concluding technical evidence regarding the tool's scope, its architectural complexity, and its specific focus on deep organizational mapping within Active Directory (AD).

### Updated Analysis: Analysis Report (Chunk 5/5)

#### 1. New Technical Capabilities Identified
*   **Recursive Domain Mapping:** The functions `_BuildRecursiveDomainList` and `_GetDomains` (found in the context of the construction logic) indicate that the tool is designed to map not just local objects, but the entire scope of the Active Directory forest.
    *   *Significance:* This confirms the tool is intended for **large-scale reconnaissance**. It seeks to identify every domain, sub-domain, and cross-forest trust relationship. For an attacker, this maps out the "geography" of the network, identifying potential paths for lateral movement across different corporate divisions or trust boundaries.
*   **Granular Group Object Processing:** The function `_ProcessGroupObject` specifically targets group memberships and structures.
    *   *Significance:* By programmatically parsing complex group nesting (e.g., a user in "Group A" which is nested inside "Group B" with admin rights), the tool automates the identification of **privilege escalation paths**. It doesn't just find groups; it evaluates their role in the security architecture.
*   **Standardized Data Pipeline:** The reference to `sym.Sharphound.Writers.BaseWriter_1.WriteData` confirms a modular, "plug-and-play" design for data handling.
    *   *Significance:* This indicates high-quality software engineering. By using a base writer class, the developers can easily add new types of objects (e.g., GPOs, Exchange information) to the tool without rewriting the core logic, allowing it to evolve into a multi-purpose collection suite.

#### 2. Sophisticated Code Construction
*   **Complex State Machines:** The extremely large and complex `_FlushWriters` function suggests a sophisticated management of the data buffer.
    *   *Significance:* This is designed to handle thousands of results without crashing or timing out. It allows the tool to stay "silent" on the network for longer periods while it processes massive amounts of data in memory before finally writing it to the JSON file, reducing the chance of being flagged by real-time traffic analysis.
*   **Advanced Logic for Nested Objects:** The code shows logic designed to handle nested and recursive elements (evidenced by the "Recursive" naming conventions).
    *   *Significance:* This is a hallmark of tools meant to bypass simple monitoring. Many basic scanners only look at direct memberships; this tool goes deep into nested objects, which are often used for sophisticated administrative roles.

#### 3. Updated Security Risk Profile
The evidence from Chunk 5/5 solidifies the tool's classification as a **Strategic Reconnaissance and Mapping Engine.**

*   **Scope Expansion:** The tool is not just "scouting" the immediate area; it is "mapping the continent." By building recursive domain lists, the attacker prepares for long-term persistence and movement across complex enterprise environments.
*   **Automated Infrastructure Analysis:** By automatically processing Group objects and their attributes, the tool automates the hardest part of manual reconnaissance: figuring out which accounts have power over other systems.
*   **Professionalism/Sophistication:** The use of consistent naming conventions (e.g., `_ProcessUserObject`, `_ProcessGroupObject`, `_FlushWriters`) and high-level abstractions (`BaseWriter`) confirms this is a professional-grade tool capable of providing an attacker with a complete "blueprint" of the target's security infrastructure in a single execution.

#### 4. Technical Indicators & Mapping (Final Update)
*   **Tool Association:** **Confirmed.** High degree of overlap with **Sharphound** functionality and code structure.
*   **MITRE ATT&CK Mapping Updates:**
    *   **Discovery (T1087.005):** Enhanced. The tool specifically identifies Domain trust relationships and nested group memberships to map out the entire infrastructure.
    *   **Credential Access/Privilege Escalation (Preparation):** The specialized processing of Group Objects directly facilitates the identification of high-privilege targets for later exploitation.
    *   **Defense Evasion:** The modular "Writer" system and state-machine processing allow it to collect massive amounts of data efficiently, minimizing its footprint on the network during the reconnaissance phase.

---

### Summary of Final Findings (Chunk 5/5)
| Feature | Technical Significance | Impact on Defense |
| :--- | :--- | :--- |
| **Recursive Domain Mapping** | Automatically maps all domains and trust relationships in an AD forest. | Allows attackers to plan large-scale lateral movement across different network zones. |
| **Group Object Parsing** | Specifically isolates and analyzes nested group memberships. | Directly identifies targets for privilege escalation (e.g., finding "Shadow Admins"). |
| **BaseWriter Architecture** | Uses a common backend for all types of data being collected. | Indicates a professional, scalable framework designed for high-volume data collection. |
| **Flush/Buffer Logic** | Advanced handling of large amounts of data before outputting to disk. | Minimizes the duration and "noise" generated during the data extraction phase. |

### Final Conclusion
The final analysis of all five chunks confirms that this is a highly sophisticated, professional-grade reconnaissance tool—consistent with **Sharphound**. It is designed to automate the collection of deep technical data regarding Active Directory architecture, including user accounts, group memberships, and complex trust relationships. 

Its primary purpose is not immediate execution, but the creation of a **comprehensive infrastructure blueprint.** By exporting this information into structured JSON files, it allows an attacker to move their analysis offline, where they can plan sophisticated movements for privilege escalation and long-term persistence without being detected by internal security teams during the planning phase.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1087 | System Information Discovery | The "Recursive Domain Mapping" identifies the overall geography of the Active Directory forest, including sub-domains and cross-forest trust relationships. |
| T1069 | Permission Group Membership Discovery | The "Granular Group Object Processing" specifically analyzes nested memberships to identify privilege escalation paths and "shadow" administrative accounts. |
| T1083 | File and Directory Discovery | The "Standardized Data Pipeline" enables the collection of a wide range of objects, including GPOs and Exchange information beyond standard user accounts. |
| T1566 | (Defense Evasion) | The use of complex state machines and buffer logic is designed to minimize network noise and avoid detection by real-time traffic analysis during the discovery phase. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section contains heavily obfuscated or non-human-readable data; however, the "BEHAVIORAL ANALYSIS" provides specific technical artifacts and functional indicators.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The strings provided are low-level assembly/code fragments without specific file system paths).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Tool Association:** **Sharphound** (The analysis explicitly links the behavior and code structure to this specific tool used for Active Directory enumeration).
*   **Internal Function Names (Signature Detection):**
    *   `_BuildRecursiveDomainList`
    *   `_GetDomains`
    *   `_ProcessGroupObject`
    *   `sym.Sharphound.Writers.BaseWriter_1.WriteData`
    *   `_FlushWriters`
*   **Behavioral Patterns:**
    *   **Recursive Domain Mapping:** Identification of cross-forest trust relationships and sub-domains.
    *   **Group Membership Parsing:** Programmatic analysis of nested group memberships to identify privilege escalation paths.
    *   **Data Buffering (Stealth Technique):** Use of a state machine (`_FlushWriters`) to buffer large amounts of data in memory before writing to disk, intended to minimize network "noise."
    *   **Output Format:** Data exported specifically into **JSON** format for offline analysis.
    *   **MITRE ATT&CK Mapping:** T1087.005 (Domain trust relationships).

---

## Malware Family Classification

Based on the provided analysis, here is the classification of the sample:

1. **Malware family:** SharpHound
2. **Malware type:** Reconnaissance / Discovery Tool
3. **Confidence:** High
4. **Key evidence:**
    *   **Direct Code Correlation:** The analysis identifies specific internal function names and naming conventions (e.g., `_BuildRecursiveDomainList`, `_ProcessGroupObject`, and specifically `sym.Sharphound.Writers.BaseWriter_1.WriteData`) that directly map to the SharpHound tool.
    *   **Advanced AD Mapping:** The tool features specialized logic for "Recursive Domain Mapping" and "Granular Group Object Processing," designed specifically to identify cross-forest trust relationships and nested group memberships to facilitate privilege escalation.
    *   **Stealthy Data Collection:** The use of complex state machines (`_FlushWriters`) and buffering techniques is intended to minimize network noise while collecting large volumes of infrastructure data for offline analysis, a hallmark of professional-grade offensive security tools.
