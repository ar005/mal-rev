# Threat Analysis Report

**Generated:** 2026-07-31 17:47 UTC
**Sample:** `0c9e772d8730204dd850797827745a27bde599983d1ee070d0b61ea5faeaf535_0c9e772d8730204dd850797827745a27bde599983d1ee070d0b61ea5faeaf535.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c9e772d8730204dd850797827745a27bde599983d1ee070d0b61ea5faeaf535_0c9e772d8730204dd850797827745a27bde599983d1ee070d0b61ea5faeaf535.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 647,368 bytes |
| MD5 | `f351df6796ba968e79a8b66e76e3e1a7` |
| SHA1 | `48c301a649e49cc3022cef18f471f74e9fa3237f` |
| SHA256 | `0c9e772d8730204dd850797827745a27bde599983d1ee070d0b61ea5faeaf535` |
| Overall entropy | 6.891 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1778695543 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 190,464 | 5.871 | No |
| `.rdata` | 7,168 | 5.568 | No |
| `.data` | 193,536 | 7.738 | ⚠️ Yes |
| `.pdata` | 512 | 3.817 | No |
| `.idata` | 4,608 | 4.017 | No |
| `.rsrc` | 232,960 | 5.227 | No |
| `.reloc` | 7,168 | 5.43 | No |

### Exports

`AddonMove`, `AgentConnectSignal`, `AgentPath`, `AllocationKey`, `AnalyzeChannel`, `AnalyzeContext`, `ArchiveTransactionPart`, `AssertRegisterInput`, `AssetCellDeserialize`, `AssetPropsBuffer`, `BackupCopyArchive`, `BatchMasterProfile`, `BatchObjectEmit`, `BinaryListenStat`, `BlockInfer`, `BlockingCollect`, `BlockingMethod`, `BodyHelper`, `BrokerTargetConstraint`, `BucketFrameReduce`, `BufferOptimize`, `BufferPrepare`, `Build`, `BuilderPeerRoute`, `BusinessChunk`, `CacheHook`, `CalendarProvider`, `CallbackWarningVertex`, `CapturePrefetchSession`, `CertificateModify`, `ChangePacket`, `ChannelFieldsContent`, `CheckStack`, `Clear`, `ClusterPassword`, `Collect`, `CollectCallback`, `CollectorJobPointer`, `CommitOptions`, `CompiledVerify`, `ConfigBoundStat`, `ConfigBucketDeserialize`, `ConfigContent`, `ConstraintFinalize`, `ContainerGraphSerialize`, `ContentDuplicate`, `ContextVector`, `ConvertAssertTree`, `CoreBound`, `CorrectDigest`

## Extracted Strings

Total strings found: **1027** (showing first 100)

```
`.rdata
@.data
.pdata
@.idata
@.reloc
j!XP[9
j%XjX
P[P[H
-P[j!X
P[j X9
 P[j/X
P[j+XH
j.Xj+XP[H
P[j&X9
P[j-XH
 P[j/X
Xj&XP[
 P[j%X
 j'XjXg
P[j.XH
j(Xj1Xj
 P[j,X
 P[j	X
 j-Xj/X
 P[j"X
 P[j,X
jXP[j
+jXP[9
j(XP[
T,0B2T
:B2T$XB
T402T4XB2T
T<0B2T
<2T$ B
=2T$!B
>2T$"B
D2u?D2u@D2
@SUVWATAUAVAWLcT$xM
Hc\$hM
Lc\$pH
B*:C0)E
$A_A^A]A\_^][
@SUVWATAVAW
A_A^A\_^][
@SUVWATAVAWH
@A_A^A\_^][
@SUVWATAUAVAWH
u_HcA<
(A_A^A]A\_^][
(D#$Mc
@SUVWATAUH
M+]0toD
XA]A\_^][
XA]A\_^][
XA]A\_^][
.text$mn
.rdata
.rdata$voltmd
.rdata$zzzdbg
.xdata
.edata
.pdata
.idata
.rsrc$01
.rsrc$02
App.exe
AddonMove
AgentConnectSignal
AgentPath
AllocationKey
AnalyzeChannel
AnalyzeContext
ArchiveTransactionPart
AssertRegisterInput
AssetCellDeserialize
AssetPropsBuffer
BackupCopyArchive
BatchMasterProfile
BatchObjectEmit
BinaryListenStat
BlockInfer
BlockingCollect
BlockingMethod
BodyHelper
BrokerTargetConstraint
BucketFrameReduce
BufferOptimize
BufferPrepare
BuilderPeerRoute
BusinessChunk
CacheHook
CalendarProvider
CallbackWarningVertex
CapturePrefetchSession
CertificateModify
ChangePacket
ChannelFieldsContent
CheckStack
ClusterPassword
Collect
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.14002c2c0` | `0x14002c2c0` | 4606 | ✓ |
| `fcn.14002da90` | `0x14002da90` | 3253 | ✓ |
| `fcn.14002f1a0` | `0x14002f1a0` | 1441 | ✓ |
| `fcn.14002d4c0` | `0x14002d4c0` | 978 | ✓ |
| `fcn.14002ed60` | `0x14002ed60` | 634 | ✓ |
| `fcn.14002d8a0` | `0x14002d8a0` | 487 | ✓ |
| `fcn.14002e750` | `0x14002e750` | 485 | ✓ |
| `fcn.14002efe0` | `0x14002efe0` | 255 | ✓ |
| `fcn.14002f0e0` | `0x14002f0e0` | 188 | ✓ |
| `fcn.14002ecb0` | `0x14002ecb0` | 175 | ✓ |
| `fcn.14002eac0` | `0x14002eac0` | 139 | ✓ |
| `fcn.14002f750` | `0x14002f750` | 131 | ✓ |
| `fcn.14002ebf0` | `0x14002ebf0` | 94 | ✓ |
| `fcn.14002ec50` | `0x14002ec50` | 94 | ✓ |
| `entry0` | `0x14002e990` | 74 | ✓ |
| `fcn.14002c27c` | `0x14002c27c` | 67 | ✓ |
| `fcn.140001000` | `0x140001000` | 48 | ✓ |
| `fcn.14002eb50` | `0x14002eb50` | 46 | ✓ |
| `fcn.14002eba0` | `0x14002eba0` | 35 | ✓ |
| `fcn.14002ebd0` | `0x14002ebd0` | 28 | ✓ |
| `fcn.14002eb80` | `0x14002eb80` | 28 | ✓ |
| `fcn.140001030` | `0x140001030` | 24 | ✓ |
| `sym.App.exe_AddonMove` | `0x14002e940` | 8 | ✓ |
| `sym.App.exe_AgentConnectSignal` | `0x14002e950` | 8 | ✓ |
| `sym.App.exe_AssetPropsBuffer` | `0x14002e9f0` | 8 | ✓ |
| `sym.App.exe_AgentPath` | `0x14002e960` | 6 | ✓ |
| `sym.App.exe_AnalyzeContext` | `0x14002e980` | 6 | ✓ |
| `sym.App.exe_ArchiveTransactionPart` | `0x14002e9e0` | 6 | ✓ |
| `sym.App.exe_BinaryListenStat` | `0x14002ea20` | 6 | ✓ |
| `sym.App.exe_BusinessChunk` | `0x14002ea50` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.140001000.c`](code/fcn.140001000.c)
- [`code/fcn.140001030.c`](code/fcn.140001030.c)
- [`code/fcn.14002c27c.c`](code/fcn.14002c27c.c)
- [`code/fcn.14002c2c0.c`](code/fcn.14002c2c0.c)
- [`code/fcn.14002d4c0.c`](code/fcn.14002d4c0.c)
- [`code/fcn.14002d8a0.c`](code/fcn.14002d8a0.c)
- [`code/fcn.14002da90.c`](code/fcn.14002da90.c)
- [`code/fcn.14002e750.c`](code/fcn.14002e750.c)
- [`code/fcn.14002eac0.c`](code/fcn.14002eac0.c)
- [`code/fcn.14002eb50.c`](code/fcn.14002eb50.c)
- [`code/fcn.14002eb80.c`](code/fcn.14002eb80.c)
- [`code/fcn.14002eba0.c`](code/fcn.14002eba0.c)
- [`code/fcn.14002ebd0.c`](code/fcn.14002ebd0.c)
- [`code/fcn.14002ebf0.c`](code/fcn.14002ebf0.c)
- [`code/fcn.14002ec50.c`](code/fcn.14002ec50.c)
- [`code/fcn.14002ecb0.c`](code/fcn.14002ecb0.c)
- [`code/fcn.14002ed60.c`](code/fcn.14002ed60.c)
- [`code/fcn.14002efe0.c`](code/fcn.14002efe0.c)
- [`code/fcn.14002f0e0.c`](code/fcn.14002f0e0.c)
- [`code/fcn.14002f1a0.c`](code/fcn.14002f1a0.c)
- [`code/fcn.14002f750.c`](code/fcn.14002f750.c)
- [`code/sym.App.exe_AddonMove.c`](code/sym.App.exe_AddonMove.c)
- [`code/sym.App.exe_AgentConnectSignal.c`](code/sym.App.exe_AgentConnectSignal.c)
- [`code/sym.App.exe_AgentPath.c`](code/sym.App.exe_AgentPath.c)
- [`code/sym.App.exe_AnalyzeContext.c`](code/sym.App.exe_AnalyzeContext.c)
- [`code/sym.App.exe_ArchiveTransactionPart.c`](code/sym.App.exe_ArchiveTransactionPart.c)
- [`code/sym.App.exe_AssetPropsBuffer.c`](code/sym.App.exe_AssetPropsBuffer.c)
- [`code/sym.App.exe_BinaryListenStat.c`](code/sym.App.exe_BinaryListenStat.c)
- [`code/sym.App.exe_BusinessChunk.c`](code/sym.App.exe_BusinessChunk.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly and strings, this binary is a **multistage packer or loader** designed to deobfuscate an embedded payload and execute it in memory. The code exhibits several characteristics typical of sophisticated malware "stubs" used to hide the primary malicious functionality from static analysis.

### Core Functionality and Purpose
The primary purpose of this code is to act as a **loader/wrapper**. Instead of containing the main malicious logic itself, it contains highly complex routines designed to:
1.  **Decrypt data:** Decipher nested layers of configuration data or secondary executable code.
2.  **Resolve APIs dynamically:** Hide its intent by not using standard Windows API names in the Import Address Table (IAT).
3.  **In-memory execution:** Manually map and execute a hidden payload (likely an "Agent" as suggested by the strings `AgentConnectSignal` and `AgentPath`) directly into memory to evade traditional disk-based antivirus scans.

### Suspicious or Malicious Behaviors
*   **Multi-Layered Decryption/Deobfuscation:** Functions like `fcn.14002c2c0` and `fcn.14002da90` contain complex, mathematically intensive loops (bit-shifts, XORs, and modular arithmetic). These are used to decrypt "Stage 2" code or configuration blocks containing C2 (Command & Control) addresses and file paths.
*   **Manual PE Loading/Reflection:** Function `fcn.14002f1a0` specifically checks for the **MZ** (`0x5a4d`) and **PE** (`0x4550`) headers. It then iterates through segments to calculate offsets and lengths, which is a classic signature of a **Reflective Loader**. This allows the malware to load an EXE or DLL into memory without ever writing it to the hard drive.
*   **API Hashing:** The code uses functions like `fcn.14002ecb0` that take large constants (e.g., `0x3f1799e`, `0x560eff7d`). These are used to resolve Windows API functions via hashes rather than by name, making it difficult for analysts to see what the program is doing at a glance.
*   **Evasive String Manipulation:** The extensive amount of "garbage" strings and complex internal names (e.g., `BufferOptimize`, `Decrypt_Loader`) suggest the author is attempting to blend in with legitimate system code or simply hide the underlying mechanics from automated scanners.

### Notable Techniques & Patterns
*   **Custom Cipher Loops:** The repetition of similar, highly-complex arithmetic blocks suggests the use of custom XOR/XOR-Chaining ciphers. This is a common way to bypass simple signature-based detection.
*   **In-Memory Patching:** In `fcn.14002f1a0`, there are sections where the code modifies memory at specific offsets (`piVar16 = *piVar16 + (iVar18 - iVar15)`). This is often used to resolve relocations or fix up an unpacked module in memory before execution.
*   **Execution Guarding:** The `entry0` and `fcn.14002f0e0` functions act as a gateway, ensuring that the environment is "ready" (deobfuscated) before the final jump into the payload is made.

### Summary of Risks
This binary's primary role is **evasion**. By utilizing a heavy packer/loader:
1.  The actual malware remains hidden in an encrypted state on disk.
2.  The presence of an "Agent" in the strings suggests this is likely part of a **backdoor or botnet framework** (e.g., Remote Access Trojan).
3.  The manual loading process indicates it is designed to evade simple "file-on-disk" detection, meaning it can only be analyzed effectively by monitoring memory during runtime.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of multi-layered decryption, custom XOR/arithmetic loops, and "garbage" strings is intended to hide the payload's true nature from static analysis. |
| **T1036** | Dynamic Resolution | The implementation of API hashing with large constants allows the binary to resolve functions at runtime without populating a visible Import Address Table (IAT). |
| **T1055** | Process Injection | The "Reflective Loader" functionality manually maps and executes the payload directly in memory to bypass traditional disk-based antivirus scans. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: Because this binary functions as a **packer/loader**, many high-value IOCs (such as C2 IP addresses and specific file paths) are likely encrypted within the "Stage 2" payloads and do not appear in the static string dump.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis indicates these are obfuscated/encrypted within the binary's payload).

### **File paths / Registry keys**
*   `App.exe` (Potential internal name for the primary executable or a component)
*   `AgentPath` (Internal variable/string used to identify the location of the secondary malicious payload)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   **API Resolution Hashes:** 
    *   `0x3f1799e`
    *   `0x560eff7d`
    *(Note: These are used by the malware to resolve Windows API functions dynamically rather than using plain-text names.)*

### **Other artifacts**
*   **Suspicious Internal Function Names:**
    *   `AgentConnectSignal` (Indicates a signaling mechanism for a remote agent/bot)
    *   `Decrypt_Loader` (Identified in analysis as a module used to decrypt stage data)
    *   `AddonMove` (Potential internal identifier)
*   **Technical Indicators of Behavior:**
    *   **Reflective Loading:** The binary checks for `MZ` (`0x5a4d`) and `PE` (`0x4550`) headers to manually map a payload into memory.
    *   **API Hashing:** Use of large constants to mask the Import Address Table (IAT).
    *   **Memory Manipulation:** Presence of code designed to calculate offsets and patch memory for relocated modules.
    *   **Multi-stage Construction:** The presence of `Agent` related strings suggests a **Botnet or Remote Access Trojan (RAT)** framework.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family:** Unknown
2. **Malware type:** Loader / Dropper
3. **Confidence:** High (regarding the functional type; Low regarding specific campaign attribution)
4. **Key evidence:**
    * **Reflective Loading Techniques:** The binary performs manual checks for MZ/PE headers and executes code directly in memory, a hallmark of loaders designed to bypass disk-based antivirus signatures.
    * **Advanced Evasion Tactics:** The use of API hashing (hiding the Import Address Table) and multi-layered decryption routines indicates it is a sophisticated "wrapper" designed to hide a secondary payload.
    * **Payload Indicators:** The presence of strings like `AgentConnectSignal` and `AgentPath` suggests that the payload delivered by this loader is likely a Remote Access Trojan (RAT) or botnet agent.
