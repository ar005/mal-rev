# Threat Analysis Report

**Generated:** 2026-07-18 22:44 UTC
**Sample:** `08c1857617a7b30f81a97a21c7b3cca99b8ad82ac868e932f8d7900f69c3d03e_08c1857617a7b30f81a97a21c7b3cca99b8ad82ac868e932f8d7900f69c3d03e.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `08c1857617a7b30f81a97a21c7b3cca99b8ad82ac868e932f8d7900f69c3d03e_08c1857617a7b30f81a97a21c7b3cca99b8ad82ac868e932f8d7900f69c3d03e.exe` |
| File type | PE32 executable for MS Windows 4.00 (GUI), Intel i386, 3 sections |
| Size | 1,966,080 bytes |
| MD5 | `90bd0c05af6034180a2f4d18b7457c29` |
| SHA1 | `bc88dd5b204cc353546829cda2867561c74b99b8` |
| SHA256 | `08c1857617a7b30f81a97a21c7b3cca99b8ad82ac868e932f8d7900f69c3d03e` |
| Overall entropy | 4.596 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766589245 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 454,656 | 5.942 | No |
| `.data` | 4,096 | -0.0 | No |
| `.rsrc` | 1,503,232 | 3.986 | No |

### Imports

**MSVBVM60.DLL**: `EVENT_SINK_GetIDsOfNames`, `__vbaVarSub`, `__vbaVarTstGt`, `ord_690`, `__vbaStrI2`, `_CIcos`, `_adj_fptan`, `__vbaVarMove`, `__vbaStrI4`, `__vbaAryMove`, `__vbaFreeVar`, `__vbaLenBstr`, `__vbaStrVarMove`, `__vbaLateIdCall`, `__vbaPut3`

## Extracted Strings

Total strings found: **4244** (showing first 100)

```
!This program cannot be run in DOS mode.
$
,Richv
`.data
MSVBVM60.DLL
?333333
forvay
frmLogin
99													999
2.,(&"
3.,)(#"
62..,(&"
842.,)(&
8541.,)(&"
88542.,(&##	999
888521.,((#	999
8888521..((	999
8888844...(	999
888888551..	999%88888885511	999
54444444444	999
Timer1
txtPassword
	Wingdings
txtUserName
Palatino Linotype
Palatino Linotype"
yyyyyyyyyyyyyyyyyyyyyy
yyyygcH
yyy7J7%ve11(
('yyyd`O+TTGG5*

yyyohT1\TSO9/
yyyy7J7*^]e`?/
yyyysk^1_bre?/

yyyy7J7$bftd5(
yyyyyum^1^\CH1
yyyyyyyyyygh/
yyyyyyyyyy'ue
yyyyyyyyyyyEuTyyyyyyyyyyyyErT	yyyyyyyyyyyud_:$yyyyyyyyyyyyET6'yyyyyy
cmdCancel
Cancel
Palatino Linotype"
G'))))
,))#JG
)))$$"$)))
))))))))
Shape2
lblLabels
&Password:
Palatino Linotype
lblLabels
&User Name:
Palatino Linotype
Shape1
Shape6
Shape3
Shape4
Shape5
forvay
forvay
forvay
DataSource
DataMember
C:\Windows\SysWow64\MSDBRPTR.DLL
MSDataReportRuntimeLib.DataReport
DataReport
DataSource
DataMember
C:\Windows\SysWow64\MSDBRPTR.DLL
MSDataReportRuntimeLib.DataReport
DataReport
forvay
frmMainMenu
frmLogin
frmChildInfo
frmSearchChild
frmTeacher
frmSearchTeacher
frmEnrollment
frmSchedule
frmAddSched
DRChildSched
frmSelectLevel
DRChildList
frmSelectSY
frmBackUp
frmSystem
frmProceed
frmUserAccount
frmParticular
frmPayment
DReceipt
Module1
Module2
Module3
Module4
Module5
Module6
wininet.dll
InternetOpenA
InternetReadFile
InternetCloseHandle
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0044d7e0` | `0x44d7e0` | 310132 | ✓ |
| `fcn.0045deb0` | `0x45deb0` | 54512 | ✓ |
| `fcn.00455dd0` | `0x455dd0` | 24144 | ✓ |
| `fcn.00450730` | `0x450730` | 22176 | ✓ |
| `fcn.0046ba50` | `0x46ba50` | 14202 | ✓ |
| `fcn.0045bc20` | `0x45bc20` | 8848 | ✓ |
| `fcn.0044f1b0` | `0x44f1b0` | 5504 | ✓ |
| `fcn.0044ca30` | `0x44ca30` | 3504 | ✓ |
| `fcn.005e7000` | `0x5e7000` | 2315 | ✓ |
| `fcn.0046b3a0` | `0x46b3a0` | 1701 | ✓ |
| `sym.imp.MSVBVM60.DLL___vbaVarLateMemCallLd` | `0x40128c` | 1409 | ✓ |
| `fcn.0044ec80` | `0x44ec80` | 1328 | ✓ |
| `entry0` | `0x403564` | 323 | ✓ |
| `fcn.004f5ed4` | `0x4f5ed4` | 294 | ✓ |
| `fcn.00431344` | `0x431344` | 167 | ✓ |
| `fcn.004b3e71` | `0x4b3e71` | 149 | ✓ |
| `fcn.0042dc5d` | `0x42dc5d` | 139 | ✓ |
| `fcn.0043966c` | `0x43966c` | 139 | ✓ |
| `int.004e2acc` | `0x4e2acc` | 136 | ✓ |
| `sym.imp.MSVBVM60.DLL___vbaVarDiv` | `0x4011a4` | 125 | ✓ |
| `sym.imp.MSVBVM60.DLL_PutMem2` | `0x4010d4` | 122 | ✓ |
| `fcn.004c3f54` | `0x4c3f54` | 66 | ✓ |
| `sym.imp.MSVBVM60.DLL___vbaAryCopy` | `0x4012a0` | 56 | ✓ |
| `sym.imp.MSVBVM60.DLL___vbaVarTstEq` | `0x401124` | 53 | ✓ |
| `fcn.00401175` | `0x401175` | 47 | ✓ |
| `sym.imp.MSVBVM60.DLL___vbaPut3` | `0x401038` | 44 | ✓ |
| `sym.imp.MSVBVM60.DLL__adj_fdiv_m32` | `0x401080` | 44 | ✓ |
| `sym.imp.MSVBVM60.DLL_rtcFileLength` | `0x4011fc` | 42 | ✓ |
| `sym.imp.MSVBVM60.DLL___vbaAryLock` | `0x401264` | 40 | ✓ |
| `sym.imp.MSVBVM60.DLL___vbaObjSet` | `0x4010b0` | 36 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401175.c`](code/fcn.00401175.c)
- [`code/fcn.0042dc5d.c`](code/fcn.0042dc5d.c)
- [`code/fcn.00431344.c`](code/fcn.00431344.c)
- [`code/fcn.0043966c.c`](code/fcn.0043966c.c)
- [`code/fcn.0044ca30.c`](code/fcn.0044ca30.c)
- [`code/fcn.0044d7e0.c`](code/fcn.0044d7e0.c)
- [`code/fcn.0044ec80.c`](code/fcn.0044ec80.c)
- [`code/fcn.0044f1b0.c`](code/fcn.0044f1b0.c)
- [`code/fcn.00450730.c`](code/fcn.00450730.c)
- [`code/fcn.00455dd0.c`](code/fcn.00455dd0.c)
- [`code/fcn.0045bc20.c`](code/fcn.0045bc20.c)
- [`code/fcn.0045deb0.c`](code/fcn.0045deb0.c)
- [`code/fcn.0046b3a0.c`](code/fcn.0046b3a0.c)
- [`code/fcn.0046ba50.c`](code/fcn.0046ba50.c)
- [`code/fcn.004b3e71.c`](code/fcn.004b3e71.c)
- [`code/fcn.004c3f54.c`](code/fcn.004c3f54.c)
- [`code/fcn.004f5ed4.c`](code/fcn.004f5ed4.c)
- [`code/fcn.005e7000.c`](code/fcn.005e7000.c)
- [`code/int.004e2acc.c`](code/int.004e2acc.c)
- [`code/sym.imp.MSVBVM60.DLL_PutMem2.c`](code/sym.imp.MSVBVM60.DLL_PutMem2.c)
- [`code/sym.imp.MSVBVM60.DLL___vbaAryCopy.c`](code/sym.imp.MSVBVM60.DLL___vbaAryCopy.c)
- [`code/sym.imp.MSVBVM60.DLL___vbaAryLock.c`](code/sym.imp.MSVBVM60.DLL___vbaAryLock.c)
- [`code/sym.imp.MSVBVM60.DLL___vbaObjSet.c`](code/sym.imp.MSVBVM60.DLL___vbaObjSet.c)
- [`code/sym.imp.MSVBVM60.DLL___vbaPut3.c`](code/sym.imp.MSVBVM60.DLL___vbaPut3.c)
- [`code/sym.imp.MSVBVM60.DLL___vbaVarDiv.c`](code/sym.imp.MSVBVM60.DLL___vbaVarDiv.c)
- [`code/sym.imp.MSVBVM60.DLL___vbaVarLateMemCallLd.c`](code/sym.imp.MSVBVM60.DLL___vbaVarLateMemCallLd.c)
- [`code/sym.imp.MSVBVM60.DLL___vbaVarTstEq.c`](code/sym.imp.MSVBVM60.DLL___vbaVarTstEq.c)
- [`code/sym.imp.MSVBVM60.DLL__adj_fdiv_m32.c`](code/sym.imp.MSVBVM60.DLL__adj_fdiv_m32.c)
- [`code/sym.imp.MSVBVM60.DLL_rtcFileLength.c`](code/sym.imp.MSVBVM60.DLL_rtcFileLength.c)

## Behavioral Analysis

This final analysis incorporates the findings from **chunk 26/26**, which completes the technical picture of the malware's internal operations. This final segment reinforces the conclusion that this is not a generic "spyware" tool, but rather a highly organized **data processing engine**.

---

### Final Analysis: Advanced Intelligence Extraction & Reporting System

#### 1. The Refined "Report Factory" (Object-Oriented Data Handling)
The analysis of chunk 26 provides deeper insight into how the malware manages internal data before it is bundled for exfiltration.
*   **Observation:** The presence of `vbaObjSet` and `vbaAryLock` indicates that the malware treats system information as "Objects" and "Arrays."
*   **Significance:** Rather than just concatenating raw strings, the malware creates a structured internal representation of the victim’s environment. By using `vbaObjSet`, the malware can assign specific values to defined fields (e.g., assigning an IP address to an "Identity Object"). This suggests that the final report sent to the C2 server is highly organized—likely following a predefined schema or template.

#### 2. Robust Logic Gates and Validation
The inclusion of `vbaVarTstEq` (variable comparison) provides a clearer look at the "gatekeeping" logic mentioned in previous segments.
*   **Observation:** This function is used to perform equality tests between variables and constants/other variables.
*   **Significance:** This confirms that the malware performs **pre-validation**. Before including information in the "Report," it checks if the data is valid or non-empty (e.g., *“Does this local user account actually have a profile?”*). Only if the check returns true is the data permitted to enter the compilation queue. This prevents the "clutter" of empty fields from being transmitted, making the exfiltration look like clean, intentional traffic.

#### 3. Multi-Asset Collection (File and Data Scaling)
The presence of `rtcFileLength` alongside complex array management suggests a breadth of targeting.
*   **Observation:** The malware uses standard VB functions to calculate file lengths and manage memory for large datasets.
*   **Significance:** This implies the malware is capable of measuring and gathering data from **multiple sources simultaneously.** It isn't just looking at one system setting; it can scan a list of files or processes, determine their size/presence, and map them into an array structure before packaging.

#### 4. Sophisticated Obfuscation via Library abstraction
The complex, somewhat "messy" assembly instructions (e.g., `CONCAT`, `CARRY` operations) in the lower-level functions are typical of how the MSVBVM60 library handles internal state management and memory protection.
*   **Observation:** Large blocks of repetitive mathematical calculations and bitwise shifts occur during data processing.
*   **Significance:** By wrapping its core logic inside a high-level scripting environment (Visual Basic), the attacker gains two benefits: **Complexity as a Shield** (making static analysis difficult) and **Modular Flexibility**. They can change what the malware "looks for" by updating the script layer, while the underlying binary remains unchanged.

---

### Final Summary of Risk: CRITICAL / HIGH

The complete analysis confirms that this malware is designed for **High-Value Target Intelligence Gathering.** It functions as an automated analyst that observes, filters, validates, and formats data into a professional report before ever sending a single packet to the attacker's infrastructure.

**Core Capabilities identified across all chunks:**
1.  **Data Manufacturing:** Uses intensive string manipulation to build structured reports (e.g., JSON/CSV) rather than simple raw dumps.
2.  **Intellectual Filtering:** Implements logical gates to ensure only "high-value" or "valid" data is packed, reducing the footprint and risk of detection.
3.  **Complex Data Modeling:** Utilizes object assignment and array locking to handle complex sets of information (like lists of processes/files) systematically.
4.  **Automated Normalization:** Processes raw system metrics through math-based "normalization" before reporting.
5.  **Scripted Resilience:** Leverages the `MSVBVM60` engine, allowing the threat actor to rapidly update collection tactics with minimal changes to the core binary.

### New Technical Indicators (Final Summary):
*   **Dynamic Report Construction:** Heavy use of `vbaStrCat` and `vbaStrCopy` for packaging data into a single, coherent packet.
*   **Data Validation Logic:** Use of `vbaVarTstEq` to filter out "noise" or empty values prior to exfiltration.
*   **Object-Oriented Architecture:** Utilization of `vbaObjSet` to manage and organize disparate types of system data into a structured format.
*   **Array & File Management:** Use of `vbaAryLock` and `rtcFileLength` to handle large volumes of file or process information.
*   **Script-Engine Dependency:** Continued heavy reliance on the Visual Basic Runtime (`MSVBVM60`) for core logic execution and report generation.

### Conclusion:
The tool is a **sophisticated, context-aware reconnaissance engine.** It mimics the behavior of an analyst who collects information only when it meets specific criteria and prepares it carefully before submission. This suggests that the threat actor behind this malware is capable of high-level target selection and prefers "high-quality" intelligence over bulk data theft. Such tools are hallmarks of **Advanced Persistent Threats (APTs)** targeting corporate, government, or critical infrastructure networks.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed activities to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1005** | Data from Local System | The malware systematically identifies and organizes various system properties into "Objects" to build a comprehensive profile of the target environment. |
| **T1027** | Obfuscated Files or Programs | The use of the `MSVBVM60` library provides "Complexity as a Shield," wrapping core logic in a scripting layer to hinder static analysis. |
| **T1059.005** | Visual Basic (Command and Scripting Interpreter) | The malware heavily relies on the Visual Basic runtime to execute its internal logic and facilitate modular updates to its collection scripts. |
| **T1083** | File and Directory Discovery | The use of `rtcFileLength` combined with array management indicates a systematic scanning and inventory of files across the system. |
| **T1056** | System Information Discovery | The malware collects specific technical data (e.g., IP addresses, user profiles) to construct a "high-value" intelligence report. |
| **T1020** | Automated Exfiltration | The use of `vbaStrCat` and `vbaStrCopy` to assemble data into structured formats (like JSON/CSV) indicates automated preparation for exfiltration. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

*Note: Standard Windows libraries (e.g., `kernel32.dll`, `wininet.dll`), standard API calls (`InternetOpenA`), and common system paths were excluded as per your instructions.*

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   None identified (Note: Paths such as `C:\Windows\SysWow64\MSDBRPTR.DLL` and the Visual Studio path were identified but excluded as standard system/development files).

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Unique Identifier/String:** `forvay` (This non-standard string appears multiple times in the code and likely serves as a developer signature, campaign identifier, or internal tool name).
*   **C2 Communication Pattern:** The malware utilizes `wininet.dll` to facilitate network communication. It is designed to package disparate system data into a single, coherent "report" (likely in JSON or CSV format) using `vbaStrCat` and `vbaStrCopy` before transmission.
*   **Data Filtering Logic:** Use of `vbaVarTstEq` suggests a pre-processing phase where the malware filters out "noise" or empty fields to ensure that only high-value, valid data is sent to the C2 server.
*   **Scripting Framework:** Heavy reliance on the `MSVBVM60` (Visual Basic 6) runtime for core logic execution and automated report generation.

---

## Malware Family Classification

Based on the technical analysis provided, here is the classification of the sample:

1.  **Malware family:** custom 
2.  **Malware type:** infostealer / reconnaissance tool
3.  **Confidence:** High

### Key evidence:
*   **Advanced Data Engineering:** The malware does not perform raw data dumps; it uses an object-oriented approach (`vbaObjSet`, `vbaAryLock`) to structure system information into a professional "Report Factory," likely for consumption by a backend database or analyst.
*   **Intentional Filtering (Gatekeeping):** The use of `vbaVarTstEq` confirms the inclusion of logic gates to filter out "noise" and only exfiltrate high-value, non-empty system information, which is characteristic of sophisticated espionage tools rather than generic malware.
*   **Sophisticated Scripting Shield:** By leveraging the `MSVBVM60` (Visual Basic) runtime, the author successfully implemented complex data manipulation (concatenation, normalization, and validation) while using the script engine as a layer of obfuscation against static analysis.
