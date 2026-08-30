# Threat Analysis Report

**Generated:** 2026-08-17 19:18 UTC
**Sample:** `0fe2b6c7d0e9b57d2b6f7c3d3ffd05025eb3e4adf3f9c4937be8bd40154e5bd2_0fe2b6c7d0e9b57d2b6f7c3d3ffd05025eb3e4adf3f9c4937be8bd40154e5bd2.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0fe2b6c7d0e9b57d2b6f7c3d3ffd05025eb3e4adf3f9c4937be8bd40154e5bd2_0fe2b6c7d0e9b57d2b6f7c3d3ffd05025eb3e4adf3f9c4937be8bd40154e5bd2.exe` |
| File type | PE32 executable for MS Windows 6.00 (console), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,286,656 bytes |
| MD5 | `206d6cfe254bd677e0591774552d9d6e` |
| SHA1 | `c1d3c73872411d9d724dbc6c16b578123e373c5a` |
| SHA256 | `0fe2b6c7d0e9b57d2b6f7c3d3ffd05025eb3e4adf3f9c4937be8bd40154e5bd2` |
| Overall entropy | 7.917 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2960719396 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,279,488 | 7.926 | ⚠️ Yes |
| `.rsrc` | 6,144 | 4.139 | No |
| `.reloc` | 512 | 0.102 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **3895** (showing first 100)

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

Functions analyzed: **30** | Decompiled to C: **29**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `method._ReadAllAsync_d__7_1.System.Collections.Generic.IAsyncEnumerator_T_.get_Current` | `0x402ff3` | 1286454 | ✓ |
| `sym.Costura.AssemblyLoader.LoadStream` | `0x412144` | 1224676 | ✓ |
| `method.Sharphound.Producers.LdapProducer.GetPartitionedFilter` | `0x40f9c3` | 144944 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x41255c` | 64488 | ✓ |
| `method.Sharphound.Writers.JsonDataWriter_1.GetFilename` | `0x4063bf` | 8271 | ✓ |
| `method._ProcessComputerObject_d__25.MoveNext` | `0x409824` | 4812 | ✓ |
| `method.Sharphound.Producers.StealthContext.GetSearchResultEntries` | `0x410c05` | 3173 | ✓ |
| `method.__c._BuildRecursiveDomainList_b__5_1` | `0x404c0d` | 3070 | ✓ |
| `method._BuildRecursiveDomainList_d__5.System.Threading.Tasks.Sources.IValueTaskSource.GetResult` | `0x405841` | 2628 | ✓ |
| `method._GetPartitionedFilter_d__2.System.Collections.IEnumerable.GetEnumerator` | `0x41025f` | 2470 | ✓ |
| `method._ProcessEnterpriseCA_d__34.MoveNext` | `0x40ca14` | 2468 | ✓ |
| `method.Sharphound.Options.set_StatusInterval` | `0x403465` | 2393 | ✓ |
| `method._ProduceConfigNC_d__3.MoveNext` | `0x410268` | 2320 | ✓ |
| `method._StartWriter_d__23.MoveNext` | `0x40e508` | 2024 | ✓ |
| `method._Produce_d__1.MoveNext` | `0x40fa20` | 1756 | — |
| `method._ProcessObject_d__22.MoveNext` | `0x408b14` | 1720 | ✓ |
| `method._ProcessDomainObject_d__28.MoveNext` | `0x40b1f4` | 1716 | ✓ |
| `method._ProcessUserObject_d__24.MoveNext` | `0x4091dc` | 1592 | ✓ |
| `method._FindPathTargetSids_d__10.MoveNext` | `0x41187c` | 1516 | ✓ |
| `method._StartCollection_d__11.MoveNext` | `0x406c0c` | 1508 | ✓ |
| `method._ConsumeSearchResults_d__12.MoveNext` | `0x407200` | 1424 | ✓ |
| `method._FlushWriters_d__24.MoveNext` | `0x40ed00` | 1424 | ✓ |
| `method._ConsumeSearchResults_d__0.MoveNext` | `0x4077fc` | 1416 | ✓ |
| `sym._Produce_d__1.MoveNext` | `0x40f3dc` | 1336 | ✓ |
| `method._BuildRecursiveDomainList_d__5.MoveNext` | `0x405260` | 1252 | ✓ |
| `method._ProcessOUObject_d__30.MoveNext` | `0x40bb30` | 1208 | ✓ |
| `method._GetDomainsForEnumeration_d__4.MoveNext` | `0x404dc8` | 1124 | ✓ |
| `method._StartCollection_d__1.MoveNext` | `0x403fec` | 1084 | ✓ |
| `method._ProcessGroupObject_d__27.MoveNext` | `0x40adbc` | 1064 | ✓ |
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
- [`code/method._GetPartitionedFilter_d__2.System.Collections.IEnumerable.GetEnumerator.c`](code/method._GetPartitionedFilter_d__2.System.Collections.IEnumerable.GetEnumerator.c)
- [`code/method._ProcessComputerObject_d__25.MoveNext.c`](code/method._ProcessComputerObject_d__25.MoveNext.c)
- [`code/method._ProcessDomainObject_d__28.MoveNext.c`](code/method._ProcessDomainObject_d__28.MoveNext.c)
- [`code/method._ProcessEnterpriseCA_d__34.MoveNext.c`](code/method._ProcessEnterpriseCA_d__34.MoveNext.c)
- [`code/method._ProcessGroupObject_d__27.MoveNext.c`](code/method._ProcessGroupObject_d__27.MoveNext.c)
- [`code/method._ProcessOUObject_d__30.MoveNext.c`](code/method._ProcessOUObject_d__30.MoveNext.c)
- [`code/method._ProcessObject_d__22.MoveNext.c`](code/method._ProcessObject_d__22.MoveNext.c)
- [`code/method._ProcessUserObject_d__24.MoveNext.c`](code/method._ProcessUserObject_d__24.MoveNext.c)
- [`code/method._ProduceConfigNC_d__3.MoveNext.c`](code/method._ProduceConfigNC_d__3.MoveNext.c)
- [`code/method._ReadAllAsync_d__7_1.System.Collections.Generic.IAsyncEnumerator_T_.get_Current.c`](code/method._ReadAllAsync_d__7_1.System.Collections.Generic.IAsyncEnumerator_T_.get_Current.c)
- [`code/method._StartCollection_d__1.MoveNext.c`](code/method._StartCollection_d__1.MoveNext.c)
- [`code/method._StartCollection_d__11.MoveNext.c`](code/method._StartCollection_d__11.MoveNext.c)
- [`code/method._StartWriter_d__23.MoveNext.c`](code/method._StartWriter_d__23.MoveNext.c)
- [`code/method.__Main_b__1_d.MoveNext.c`](code/method.__Main_b__1_d.MoveNext.c)
- [`code/method.__c._BuildRecursiveDomainList_b__5_1.c`](code/method.__c._BuildRecursiveDomainList_b__5_1.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)
- [`code/sym._Produce_d__1.MoveNext.c`](code/sym._Produce_d__1.MoveNext.c)

## Behavioral Analysis

This updated analysis incorporates the findings from **chunk 6/6**, which provides the final pieces of evidence regarding specific target objects, the internal naming conventions of the code, and the sheer scale of the tool's operations.

### Analysis of New Findings (Chunk 6/6)

#### 1. Explicit Tool Identification (The "Smoking Gun")
The most significant discovery in this final chunk is the function name: `method.Sharphound.Options.set_StatusInterval`.
*   **Analysis:** The inclusion of the word **"Sharphound"** within the internal method names is a definitive indicator. This strongly suggests that the binary is not just "inspired by" or "similar to" professional tools; it likely contains direct, unmodified (or minimally modified) source code from the **Sharphound** framework.
*   **Attacker Intent:** Sharphound is a well-known, high-tier reconnaissance tool used by sophisticated actors to map Active Directory. Its presence confirms that the threat actor is using a "pro-grade" toolkit designed for large-scale enterprise penetration and credential harvesting.

#### 2. Granular Target Mapping (OU & Group Objects)
The discovery of `_ProcessOUObject` and `_ProcessGroupObject` functions reinforces the "Recursive Discovery" logic found earlier.
*   **Analysis:** The tool doesn't just look for users; it specifically targets **Organizational Units (OUs)** and **Security Groups**. 
    *   **OUs** are used to define the structure of the network and where permissions are delegated.
    *   **Groups** are primary vehicles for privilege escalation (e.g., identifying who belongs in "Domain Admins" or "Schema Admins").
*   **Attacker Intent:** By systematically processing OUs and Groups, the attacker is building a comprehensive map of the organization's hierarchy to find high-value targets and administrative shortcuts.

#### 3. Automated Collection Logic
The function `_StartCollection` indicates a transition point in the tool's execution.
*   **Analysis:** This represents the phase where the tool moves from *mapping* the environment to *extracting* data (such as attributes, permissions, or hashes) from the objects it just mapped in the previous steps.
*   **Attacker Intent:** The logic is designed for automation. Once the "map" is built via recursive discovery, the "collection" phase harvests the necessary intelligence to facilitate lateral movement and privilege escalation.

#### 4. Continued Execution of Anti-Analysis Techniques
Even in these specific functional areas, the disassembler continues to flag **"overlapping instruction data"** and **"bad instructions."**
*   **Analysis:** The fact that even "boring" tasks like iterating through groups or updating status intervals are wrapped in complex, broken code confirms a high level of effort to defeat automated analysis (like Ghidhra/IDA) and manual review.
*   **Attacker Intent:** Every single component of the tool is designed to be difficult for a human analyst to read quickly. This buys the attacker time during an active incident response.

---

### Updated Summary Table (Cumulative)

| Feature | Evidence Found | Risk/Impact |
| :--- | :--- | :--- |
| **Direct Tool Link** | `method.Sharphound.Options...` | **Critical:** Direct link to the **Sharphound** framework confirms use of a professional-grade, high-sophistication toolset. |
| **Recursive Mapping** | `_BuildRecursiveDomainList` | **High:** Ensures no "hidden" OUs or groups are missed during the reconnaissance phase. |
| **Targeted Collection** | `_ProcessOUObject`, `_ProcessGroupObject`, `_StartCollection`. | **High:** Specific focus on infrastructure hierarchy and group memberships to facilitate privilege escalation. |
| **Data Persistence** | `_FlushWriters` & `JsonDataWriter`. | **High:** Ensures large-scale, multi-stage data harvesting is successful across the entire domain. |
| **Extreme Obfuscation** | "Overlapping instructions" and "Bad instruction" flags in all core functions. | **Critical:** High effort to stall incident responders and bypass automated security scanners. |

---

### Final Assessment (Final Version)

The analysis of chunks 1 through 6 confirms that this binary is a **highly sophisticated, enterprise-grade Active Directory reconnaissance engine**, almost certainly a derivative of the **Sharphound** toolset.

**Key Takeaways:**
1.  **High Sophistication & Proven Pedigree:** The explicit naming in the code (Sharphound) identifies this as an elite toolkit used by professional cybercrime groups or state-sponsored actors to map and compromise large corporate networks.
2.  **Comprehensive Scope:** Through recursive logic and specific processing of OUs and Groups, the tool is designed to leave no stone unturned. It maps out every potential path for a user to escalate privileges from a standard account to a Domain Administrator.
3.  **Advanced Anti-Analysis:** The consistent use of overlapping code and "bad instructions" across even basic functions demonstrates an intent to frustrate security professionals during the critical minutes/hours of a breach investigation.
4.  **Strategic Intent:** This is not a "spray and pray" tool; it is a surgical, methodical reconnaissance engine. It is designed to be deployed once an initial foothold is gained to provide the attacker with a complete map of the internal network's identity infrastructure.

**Conclusion:** The presence of this binary indicates a **high-level threat**. It confirms that the adversary has moved beyond simple infection and is actively engaged in systematic mapping for large-scale exploitation. Any system where this code is detected should be considered compromised at a high level, and the Active Directory environment must be audited for lateral movement and unauthorized privilege escalations.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1087** | Account Discovery | The tool specifically targets Organizational Units (OUs) and Security Groups to map out high-privilege accounts and identify paths for lateral movement. |
| **T1027** | Obfuscated Files or Information | The use of "overlapping instructions" and "bad instructions" is a deliberate tactic to hinder manual analysis and evade automated detection tools like Ghidhra/IDA. |
| **T1594** | System Proxy Configuration Discovery | *Note: While not explicitly detailed as a proxy, the tool's "mapping" phase of infrastructure logic often aligns with identifying system configuration for further connectivity.* (Optional/Implicit) |

**Analyst Note:** 
The identification of **SharpHound** functions confirms that the actor is specifically engaged in the **Discovery** phase of an operation. The focus on OUs and Groups indicates a primary objective of mapping out the Active Directory hierarchy to facilitate **Privilege Escalation**. The consistent use of anti-analysis techniques (overlapping instructions) confirms a high level of sophistication, typical of advanced persistent threats (APTs) or professional cybercrime groups aiming to maintain persistence while conducting internal reconnaissance.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.* (The text contains high-entropy, obfuscated strings, but no clear IP addresses or active C2 domains were present in the provided sample.)

### **File paths / Registry keys**
*   *None identified.* (Standard Windows system paths were omitted as per instructions.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Tool Identification:** `Sharphound` (Internal method naming: `method.Sharphound.Options.set_StatusInterval`). This identifies the binary as a known professional-grade Active Directory reconnaissance tool.
*   **Functional Logic Indicators:** 
    *   `_BuildRecursiveDomainList` (Indicates automated network mapping)
    *   `_ProcessOUObject` (Targeting Organizational Units)
    *   `_ProcessGroupObject` (Targeting Security Groups for privilege escalation)
    *   `_StartCollection` (Automated data extraction logic)
    *   `_FlushWriters` / `JsonDataWriter` (Persistence of gathered intelligence)
*   **Anti-Analysis Techniques:** 
    *   "Overlapping instruction data" 
    *   "Bad instructions" (Used to evade automated disassembly and static analysis tools like Ghidhra or IDA Pro).

---

### **Analyst Notes**
While the "Extracted Strings" section consists largely of high-entropy garbage data designed to hinder manual analysis, the **Behavioral Analysis** provides high-confidence indicators of capability. The presence of the **Sharphound** framework indicates a sophisticated threat actor capable of performing large-scale mapping and privilege escalation within an Active Directory environment.

---

## Malware Family Classification

1. **Malware family**: SharpHound
2. **Malware type**: Reconnaissance / Discovery
3. **Confidence**: High
4. **Key evidence**:
    *   **Explicit Tool Identification:** The inclusion of `method.Sharphound.Options.set_StatusInterval` serves as a "smoking gun," confirming the binary is a derivative of the SharpHound framework used for Active Directory mapping.
    *   **Targeted Infrastructure Mapping:** The presence of specialized functions like `_ProcessOUObject` and `_ProcessGroupObject` indicates a specific intent to map organizational hierarchies and identify paths for privilege escalation.
    *   **Advanced Anti-Analysis:** The deliberate use of "overlapping instructions" and "bad instructions" across all modules confirms the tool is designed by sophisticated actors to evade automated detection and stall manual analysis during the discovery phase.
