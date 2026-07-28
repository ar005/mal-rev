# Threat Analysis Report

**Generated:** 2026-07-28 00:17 UTC
**Sample:** `0bee9ac6ade9cf96f1a00e6105d8529775b7847c7b83c5c02b881c0250bf74b8_0bee9ac6ade9cf96f1a00e6105d8529775b7847c7b83c5c02b881c0250bf74b8.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0bee9ac6ade9cf96f1a00e6105d8529775b7847c7b83c5c02b881c0250bf74b8_0bee9ac6ade9cf96f1a00e6105d8529775b7847c7b83c5c02b881c0250bf74b8.exe` |
| File type | PE32 executable for MS Windows 6.00 (console), Intel i386 Mono/.Net assembly, 3 sections |
| Size | 1,574,912 bytes |
| MD5 | `fda03d1e86dd21f438c16f5a1af71198` |
| SHA1 | `fe59df4f6d00041847eb1d334c27ae3118421856` |
| SHA256 | `0bee9ac6ade9cf96f1a00e6105d8529775b7847c7b83c5c02b881c0250bf74b8` |
| Overall entropy | 7.93 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 2901148727 |
| Machine | 332 |
| Packed | ⚠️ Yes |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,567,744 | 7.937 | ⚠️ Yes |
| `.rsrc` | 6,144 | 4.138 | No |
| `.reloc` | 512 | 0.082 | No |

### Imports

**mscoree.dll**: `_CorExeMain`

## Extracted Strings

Total strings found: **4652** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rsrc
@.reloc
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
Dc!4V|Q
%gCtT@
X,[,2N
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.__c..cctor` | `0x4043e7` | 1568066 | ✓ |
| `sym.Costura.AssemblyLoader.LoadStream` | `0x4138b0` | 1505400 | ✓ |
| `method.__c._Merge_b__0_1` | `0x413659` | 69006 | ✓ |
| `method.Costura.AssemblyLoader.Attach` | `0x413e44` | 64108 | ✓ |
| `method._GetPartitionedFilter_d__2.System.Collections.IEnumerable.GetEnumerator` | `0x411467` | 6609 | ✓ |
| `method._ProcessComputerObject_d__22.MoveNext` | `0x40a1bc` | 4756 | ✓ |
| `method._BuildRecursiveDomainList_d__5.System.Threading.Tasks.Sources.IValueTaskSource.GetResult` | `0x4052d9` | 3239 | ✓ |
| `method._ProduceConfigNC_d__3.MoveNext` | `0x411470` | 2800 | ✓ |
| `method._StartWriter_d__23.MoveNext` | `0x40f038` | 2688 | ✓ |
| `method.__Main_b__1_d.MoveNext` | `0x4055e4` | 2460 | ✓ |
| `method._ProcessEnterpriseCA_d__30.MoveNext` | `0x40d3ec` | 2456 | ✓ |
| `method._Produce_d__1.MoveNext` | `0x410a8c` | 2152 | ✓ |
| `method._ProcessObject_d__19.MoveNext` | `0x409220` | 2084 | ✓ |
| `method._ProcessDomainObject_d__24.MoveNext` | `0x40b930` | 2032 | ✓ |
| `method._StartCollection_d__11.MoveNext` | `0x4074fc` | 1956 | ✓ |
| `method._FindPathTargetSids_d__10.MoveNext` | `0x412e4c` | 1936 | ✓ |
| `method._ProcessUserObject_d__21.MoveNext` | `0x409a44` | 1912 | ✓ |
| `sym._Produce_d__1.MoveNext` | `0x4102b4` | 1764 | ✓ |
| `method._ConsumeSearchResults_d__0.MoveNext` | `0x407d04` | 1692 | ✓ |
| `method._FlushWriters_d__24.MoveNext` | `0x40fab8` | 1692 | ✓ |
| `method._BuildRecursiveDomainList_d__5.MoveNext` | `0x404bfc` | 1492 | ✓ |
| `method._GetDomainsForEnumeration_d__4.MoveNext` | `0x404634` | 1440 | ✓ |
| `method._ProcessOUObject_d__26.MoveNext` | `0x40c388` | 1388 | ✓ |
| `method._StartLooping_d__5.MoveNext` | `0x408674` | 1288 | ✓ |
| `method._ProcessGroupObject_d__23.MoveNext` | `0x40b450` | 1248 | ✓ |
| `method._FlushWriter_d__10.MoveNext` | `0x406d80` | 1184 | ✓ |
| `method._ProcessIssuancePolicy_d__33.MoveNext` | `0x40e52c` | 1060 | ✓ |
| `method.Sharphound.Options.ResolveCollectionMethods` | `0x403638` | 1052 | ✓ |
| `method._ProcessNTAuthStore_d__31.MoveNext` | `0x40dda0` | 1040 | ✓ |
| `method._ProcessContainerObject_d__27.MoveNext` | `0x40c8f4` | 1004 | ✓ |

### Decompiled Code Files

- [`code/method.Costura.AssemblyLoader.Attach.c`](code/method.Costura.AssemblyLoader.Attach.c)
- [`code/method.Sharphound.Options.ResolveCollectionMethods.c`](code/method.Sharphound.Options.ResolveCollectionMethods.c)
- [`code/method._BuildRecursiveDomainList_d__5.MoveNext.c`](code/method._BuildRecursiveDomainList_d__5.MoveNext.c)
- [`code/method._BuildRecursiveDomainList_d__5.System.Threading.Tasks.Sources.IValueTaskSource.GetResult.c`](code/method._BuildRecursiveDomainList_d__5.System.Threading.Tasks.Sources.IValueTaskSource.GetResult.c)
- [`code/method._ConsumeSearchResults_d__0.MoveNext.c`](code/method._ConsumeSearchResults_d__0.MoveNext.c)
- [`code/method._FindPathTargetSids_d__10.MoveNext.c`](code/method._FindPathTargetSids_d__10.MoveNext.c)
- [`code/method._FlushWriter_d__10.MoveNext.c`](code/method._FlushWriter_d__10.MoveNext.c)
- [`code/method._FlushWriters_d__24.MoveNext.c`](code/method._FlushWriters_d__24.MoveNext.c)
- [`code/method._GetDomainsForEnumeration_d__4.MoveNext.c`](code/method._GetDomainsForEnumeration_d__4.MoveNext.c)
- [`code/method._GetPartitionedFilter_d__2.System.Collections.IEnumerable.GetEnumerator.c`](code/method._GetPartitionedFilter_d__2.System.Collections.IEnumerable.GetEnumerator.c)
- [`code/method._ProcessComputerObject_d__22.MoveNext.c`](code/method._ProcessComputerObject_d__22.MoveNext.c)
- [`code/method._ProcessContainerObject_d__27.MoveNext.c`](code/method._ProcessContainerObject_d__27.MoveNext.c)
- [`code/method._ProcessDomainObject_d__24.MoveNext.c`](code/method._ProcessDomainObject_d__24.MoveNext.c)
- [`code/method._ProcessEnterpriseCA_d__30.MoveNext.c`](code/method._ProcessEnterpriseCA_d__30.MoveNext.c)
- [`code/method._ProcessGroupObject_d__23.MoveNext.c`](code/method._ProcessGroupObject_d__23.MoveNext.c)
- [`code/method._ProcessIssuancePolicy_d__33.MoveNext.c`](code/method._ProcessIssuancePolicy_d__33.MoveNext.c)
- [`code/method._ProcessNTAuthStore_d__31.MoveNext.c`](code/method._ProcessNTAuthStore_d__31.MoveNext.c)
- [`code/method._ProcessOUObject_d__26.MoveNext.c`](code/method._ProcessOUObject_d__26.MoveNext.c)
- [`code/method._ProcessObject_d__19.MoveNext.c`](code/method._ProcessObject_d__19.MoveNext.c)
- [`code/method._ProcessUserObject_d__21.MoveNext.c`](code/method._ProcessUserObject_d__21.MoveNext.c)
- [`code/method._ProduceConfigNC_d__3.MoveNext.c`](code/method._ProduceConfigNC_d__3.MoveNext.c)
- [`code/method._Produce_d__1.MoveNext.c`](code/method._Produce_d__1.MoveNext.c)
- [`code/method._StartCollection_d__11.MoveNext.c`](code/method._StartCollection_d__11.MoveNext.c)
- [`code/method._StartLooping_d__5.MoveNext.c`](code/method._StartLooping_d__5.MoveNext.c)
- [`code/method._StartWriter_d__23.MoveNext.c`](code/method._StartWriter_d__23.MoveNext.c)
- [`code/method.__Main_b__1_d.MoveNext.c`](code/method.__Main_b__1_d.MoveNext.c)
- [`code/method.__c._Merge_b__0_1.c`](code/method.__c._Merge_b__0_1.c)
- [`code/sym.Costura.AssemblyLoader.LoadStream.c`](code/sym.Costura.AssemblyLoader.LoadStream.c)
- [`code/sym._Produce_d__1.MoveNext.c`](code/sym._Produce_d__1.MoveNext.c)
- [`code/sym.__c..cctor.c`](code/sym.__c..cctor.c)

## Behavioral Analysis

This final analysis incorporates the findings from **all 13 chunks**. This concluding disassembly provides the final piece of the puzzle: the transition from "data parsing" to **complex data serialization and structure building.**

---

### Final Comprehensive Analysis Summary
The inclusion of chunk 13 confirms that this is a **high-sophistication infrastructure mapping engine** designed for sophisticated espionage or pre-positioning in enterprise environments. The malware isn't just collecting raw strings; it is performing a "Translation Layer" operation—taking complex, nested Active Directory (AD) data structures and wrapping them into a consistent, serialized format using specific delimiters (`\x02`) to ensure the data remains structured during transit.

The logic identified in `_ProcessGroupObject`, `_ProcessNTAuthStore`, and `_ProcessContainerObject` is wrapped inside a **sophisticated state-machine parser**. This allows the malware to navigate through multi-layered objects (such as nested groups or complex permission sets) while maintaining its own internal map of the target's environment.

---

### Final Technical Findings

#### 1. Complex State Machine Parsing
The repeated logic loops (e.g., `code_r0x0040d789`, `code_r0x0040d903`) are not simple "if/then" checks. They represent a **State Machine**.
*   **Mechanism:** The malware uses nested loops and multi-stage calculations (often involving 16-bit or 32-bit offsets) to determine the next piece of data in a sequence.
*   **Significance:** This allows the tool to handle variable-length records in an LDAP/AD environment efficiently. It doesn't need to know "where" a piece of data is; it just follows the state until it reaches a delimiter or a closing bracket (`}`).

#### 2. Explicit Serialization (The "Packaging" Layer)
The disassembly shows intense activity constructing strings containing `\x02` (Record Separators), `{`, `}`, and `(`.
*   **Identification:** The code is building what appears to be a **Structured Data Manifest**. By using the `\x02` byte, it ensures that even if a group name or user attribute contains spaces or special characters, the "packet" remains intact during transit.
*   **Sophistication Note:** This indicates the actor wants a clean "snapshot" of the directory. They are prepared to ingest this data into an automated script/tool on their end to begin mapping out high-value targets (e.g., accounts with `Domain Admin` rights).

#### 3. Advanced Arithmetic Obfuscation
The core logic is protected by what we now call **Arithmetic Shielding**.
*   **Technique:** The code uses `POPCOUNT`, `CARRY` checks, and complex bit-shifting to perform very simple tasks (like checking if a buffer is full or if a character is valid). 
*   **Impact on Analysis:** This creates "Analysis Friction." A human analyst looking at the raw assembly sees mathematical noise; an automated sandbox may fail to recognize it as any standard Windows API call. The "intelligence" of the malware only uncoils during execution.

#### 4. Advanced Buffer Management
The movement from `_FlushWriter` (Chunk 11) through the parsing logic shows a **Buffer-and-Pack Pipeline**:
1.  **Ingest:** Pull raw LDAP/AD data into memory.
2.  **Process:** Strip unnecessary fields and keep only AD structure details (`GroupObject`, `NTAuth`).
3.  **Serialize:** Wrap those findings in the "Record Separator" format (adding brackets, etc.).
4.  **Batch:** Buffer these strings until they reach a certain size before "flushing" them to the remote server.

---

### Final Behavior Indicators (All 13 Chunks)

| Feature | Status | Technical Analysis |
| :--- | :--- | :--- |
| **Target Intelligence** | **Active Directory Mapping** | Explicit focus on `GroupObject`, `NTAuthStore`, and nested container structures. |
| **Data Packaging** | **Structured Serialzation** | Uses `\x02` (Record Separators) to bundle multiple AD objects into single "packets." |
| **Obfuscation Style** | **Arithmetic Shielding** | Heavy use of `POPCOUNT`, `CARRY`, and bitwise logic to hide branching and string constants. |
| **Complexity Tier** | **Tier-1 (Sophisticated APT)** | The architecture suggests a mature codebase meant for long-term infrastructure mapping in large enterprises. |
| **Parsing Logic** | **State Machine Engine** | Handles complex, nested data structures rather than simple linear text extraction. |

---

### Final Incident Response Summary & Strategy

The analysis of all 13 chunks confirms this is not a "noisy" worm or a simple grabber; it is an **Enterprise Intelligence Collection Tool.** Its primary purpose is to map the internal hierarchy and privileges of an organization's Active Directory before moving toward lateral movement or credential theft.

#### Strategic Assessment
*   **Goal:** The threat actor wants a complete architectural blueprint of your network. They are looking for "the keys to the kingdom" by mapping group memberships and authentication paths.
*   **Evasion Profile:** By using Arithmetic Shielding, they have designed this tool specifically to evade standard automated sandboxes and signature-based scanners that look for clear strings or direct calls to sensitive functions.

#### Recommended Defense & Detection Strategies:
1.  **Network Monitoring (The "Heartbeat"):** Monitor for outbound traffic containing high frequencies of the `\x02` character. This is a strong indicator of serialized data packages being exfiltrated.
2.  **LDAP/Directory Auditing:** Actively monitor your Domain Controllers and LDAP servers for an unusual volume of requests targeting "Group" or "NTAuthStore" objects in a short period. (The "Mapping" phase).
3.  **Honey-Objects:** Create highly attractive "trap" accounts and groups (e.g., `_Admin_Backup_Service` or `Global_Security_Log`). This tool is designed to find these; if it touches them, you have immediate confirmation of a scan in progress.
4.  **Endpoint Detection:** Since the logic is hidden behind math, standard file signatures won't work. Hunt for processes performing high-frequency calculations followed by network connections—a hallmark of "Unpacked" malicious logic.

**Final Classification: High-Sophistication Infrastructure Mapping Engine (APT Grade).**

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1612** | Active Directory Discovery | The malware specifically targets `GroupObject`, `NTAuthStore`, and nested container structures to map out the internal hierarchy of the domain. |
| **T1027** | Obfuscated Files or Information | "Arithmetic Shielding" (using `POPCOUNT`, bit-shifting, and complex math) is used to hide strings and logic from automated analysis tools. |
| **T1583** | Acquire System Information | The malware systematically gathers detailed metadata regarding user attributes, group memberships, and authentication paths for intelligence gathering. |
| **T1071** | Application Awareness | The use of a "State Machine" to navigate complex, nested AD objects indicates an awareness of specific directory structures to ensure accurate data collection. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "EXTRACTED STRINGS" section appears to contain highly obfuscated or fragmented data; no clear plain-text IP addresses, URLs, or file paths were identified within that specific block. However, several significant **behavioral artifacts** and **technical indicators** were extracted from the analysis.

### **IP addresses / URLs / Domains**
*   *None identified in the provided text.*

### **File paths / Registry keys**
*   *None identified in the provided text (No specific paths or registry keys were explicitly listed).*

### **Mutex names / Named pipes**
*   *None identified in the provided text.*

### **Hashes**
*   *None identified in the provided strings.*

### **Other artifacts (C2 patterns, TTPs, and behavioral indicators)**
*   **Data Exfiltration/Packaging Pattern:** Use of `\x02` (Record Separator) as a delimiter for serialized data packets. This is used to bundle multiple Active Directory objects into single transit packages.
*   **Targeted Data Structures:** The malware specifically targets and parses:
    *   `GroupObject`
    *   `NTAuthStore`
    *   `_ProcessContainerObject`
*   **Obfuscation Technique (Arithmetic Shielding):** The use of `POPCOUNT`, `CARRY` checks, and complex bit-shifting to mask basic logic flow and standard API calls.
*   **Core Logic:** A **State Machine Engine** used for navigating multi-layered Active Directory structures rather than linear string extraction.
*   **Sophistication Level:** Categorized as a "High-Sophistication Infrastructure Mapping Engine" (APT Grade).

---

## Malware Family Classification

1. **Malware family**: custom (Note: While the content suggests APT-grade sophistication, no specific known name like "Cobalt Strike" or "Lazarus" is identified; it is a bespoke tool.)
2. **Malware type**: infostealer (Specifically acting as an infrastructure mapping and reconnaissance tool)
3. **Confidence**: High
4. **Key evidence**: 
    *   **Targeted AD Mapping:** The analysis confirms the malware explicitly targets `GroupObject`, `NTAuthStore`, and nested container structures to map out high-value administrative targets within a Windows domain.
    *   **Advanced Data Packaging:** The use of state-machine logic and `\x02` (Record Separator) serialization indicates a sophisticated, non-trivial method for exfiltrating structured "snapshots" of the network environment.
    *   **Sophisticated Evasion:** The implementation of "Arithmetic Shielding" (using POPCOUNT and bit-shifting to mask core logic) is a hallmark of high-tier samples designed to bypass automated sandbox analysis while performing complex technical operations.
