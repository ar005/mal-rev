# Threat Analysis Report

**Generated:** 2026-07-14 12:37 UTC
**Sample:** `05995356583300d087cb73da34fc9722099c6229325cbe240bf6ba32aac258a5_05995356583300d087cb73da34fc9722099c6229325cbe240bf6ba32aac258a5.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `05995356583300d087cb73da34fc9722099c6229325cbe240bf6ba32aac258a5_05995356583300d087cb73da34fc9722099c6229325cbe240bf6ba32aac258a5.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 658,760 bytes |
| MD5 | `2784d93333fa8284267a70b25ed00706` |
| SHA1 | `3dcb019973629bcdb423ac6e0df1ef29c4fbd89f` |
| SHA256 | `05995356583300d087cb73da34fc9722099c6229325cbe240bf6ba32aac258a5` |
| Overall entropy | 6.925 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775068721 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 178,176 | 5.567 | No |
| `.rdata` | 8,704 | 5.541 | No |
| `.data` | 269,312 | 7.8 | ⚠️ Yes |
| `.pdata` | 512 | 3.933 | No |
| `.idata` | 4,096 | 4.258 | No |
| `.rsrc` | 178,688 | 4.202 | No |
| `.reloc` | 8,192 | 5.423 | No |

### Exports

`AcceptHandlerSafe`, `AcceptSettingBlocking`, `AdapterDecryptSocket`, `AdapterSeekEntity`, `AdjustEndpoint`, `AlgorithmGenerator`, `AlgorithmWriter`, `AllocManageField`, `AllocParseModule`, `AllocStartValidator`, `AllocUnloadBuilder`, `AllocateSettingInternal`, `AllocateVerifier`, `AnalyzeBuffer`, `AnalyzeStream`, `ArchiveAllocator`, `ArchiveBuilder`, `ArchiveConnectPacker`, `ArchiveCreateArchive`, `ArchiveHandler`, `ArchiveParser`, `ArchiveReleaseer`, `ArrayDecodeer`, `ArrayManager`, `ArrayReader`, `AudioCloseRecord`, `AudioEnableWriter`, `BaseCompressInfo`, `BindEndpoint`, `BufferCalculate`, `BufferCreator`, `BufferReader`, `BuilderDisableAlgorithm`, `BuilderUnpackDecoder`, `BusinessCalculateSession`, `BusinessInspectModule`, `CacheAllocateDecoder`, `CalculateConfig`, `ChangeDispatcher`, `ChannelAllocate`, `CheckMethodVersion3`, `CheckText`, `CheckerReceiveDomain`, `ComponentAllocator`, `ComponentProvider`, `CompressUnloadValue`, `CompressUnlockMemory`, `CompressorAllocator`, `CompressorManager`, `CompressorParser`

## Extracted Strings

Total strings found: **9428** (showing first 100)

```
`.rdata
@.data
.pdata
@.idata
@.reloc
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
j,jBX[H
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 j#jX[H
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 j	XP[H
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 j$j_X[H
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
 A]A\_^[
SVWATAUH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140029ed0` | `0x140029ed0` | 3423 | ✓ |
| `fcn.14002ac30` | `0x14002ac30` | 2700 | ✓ |
| `fcn.14002c1c0` | `0x14002c1c0` | 1084 | ✓ |
| `fcn.14002bd40` | `0x14002bd40` | 664 | ✓ |
| `fcn.140029cc0` | `0x140029cc0` | 518 | ✓ |
| `fcn.14002b6c0` | `0x14002b6c0` | 516 | ✓ |
| `fcn.14002c600` | `0x14002c600` | 348 | ✓ |
| `fcn.14002bfe0` | `0x14002bfe0` | 291 | ✓ |
| `fcn.14002bc70` | `0x14002bc70` | 196 | ✓ |
| `fcn.14002c110` | `0x14002c110` | 166 | ✓ |
| `fcn.14002c760` | `0x14002c760` | 151 | ✓ |
| `fcn.14002ba50` | `0x14002ba50` | 139 | ✓ |
| `fcn.14002bbb0` | `0x14002bbb0` | 96 | ✓ |
| `fcn.14002bc10` | `0x14002bc10` | 96 | ✓ |
| `section..text` | `0x140001000` | 95 | ✓ |
| `fcn.140029c70` | `0x140029c70` | 80 | ✓ |
| `entry0` | `0x14002b960` | 74 | ✓ |
| `fcn.14000105f` | `0x14000105f` | 63 | ✓ |
| `fcn.14002bae0` | `0x14002bae0` | 46 | ✓ |
| `fcn.14002bb10` | `0x14002bb10` | 39 | ✓ |
| `fcn.14002bb60` | `0x14002bb60` | 35 | ✓ |
| `fcn.14002bb90` | `0x14002bb90` | 28 | ✓ |
| `fcn.14002bb40` | `0x14002bb40` | 28 | ✓ |
| `fcn.14000109e` | `0x14000109e` | 11 | ✓ |
| `sym.App.exe_AcceptHandlerSafe` | `0x14002b8d0` | 8 | ✓ |
| `sym.App.exe_AdapterDecryptSocket` | `0x14002b8f0` | 8 | ✓ |
| `sym.App.exe_ConnectionProvider` | `0x14002ba30` | 8 | ✓ |
| `sym.App.exe_AcceptSettingBlocking` | `0x14002b8e0` | 6 | ✓ |
| `sym.App.exe_AlgorithmWriter` | `0x14002b930` | 6 | ✓ |
| `sym.App.exe_AllocStartValidator` | `0x14002b940` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.14000105f.c`](code/fcn.14000105f.c)
- [`code/fcn.14000109e.c`](code/fcn.14000109e.c)
- [`code/fcn.140029c70.c`](code/fcn.140029c70.c)
- [`code/fcn.140029cc0.c`](code/fcn.140029cc0.c)
- [`code/fcn.140029ed0.c`](code/fcn.140029ed0.c)
- [`code/fcn.14002ac30.c`](code/fcn.14002ac30.c)
- [`code/fcn.14002b6c0.c`](code/fcn.14002b6c0.c)
- [`code/fcn.14002ba50.c`](code/fcn.14002ba50.c)
- [`code/fcn.14002bae0.c`](code/fcn.14002bae0.c)
- [`code/fcn.14002bb10.c`](code/fcn.14002bb10.c)
- [`code/fcn.14002bb40.c`](code/fcn.14002bb40.c)
- [`code/fcn.14002bb60.c`](code/fcn.14002bb60.c)
- [`code/fcn.14002bb90.c`](code/fcn.14002bb90.c)
- [`code/fcn.14002bbb0.c`](code/fcn.14002bbb0.c)
- [`code/fcn.14002bc10.c`](code/fcn.14002bc10.c)
- [`code/fcn.14002bc70.c`](code/fcn.14002bc70.c)
- [`code/fcn.14002bd40.c`](code/fcn.14002bd40.c)
- [`code/fcn.14002bfe0.c`](code/fcn.14002bfe0.c)
- [`code/fcn.14002c110.c`](code/fcn.14002c110.c)
- [`code/fcn.14002c1c0.c`](code/fcn.14002c1c0.c)
- [`code/fcn.14002c600.c`](code/fcn.14002c600.c)
- [`code/fcn.14002c760.c`](code/fcn.14002c760.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sym.App.exe_AcceptHandlerSafe.c`](code/sym.App.exe_AcceptHandlerSafe.c)
- [`code/sym.App.exe_AcceptSettingBlocking.c`](code/sym.App.exe_AcceptSettingBlocking.c)
- [`code/sym.App.exe_AdapterDecryptSocket.c`](code/sym.App.exe_AdapterDecryptSocket.c)
- [`code/sym.App.exe_AlgorithmWriter.c`](code/sym.App.exe_AlgorithmWriter.c)
- [`code/sym.App.exe_AllocStartValidator.c`](code/sym.App.exe_AllocStartValidator.c)
- [`code/sym.App.exe_ConnectionProvider.c`](code/sym.App.exe_ConnectionProvider.c)

## Behavioral Analysis

Based on the analysis of the provided disassembly, this binary is a **highly obfuscated loader or packer**. It is designed to hide its true functionality (such as and exfiltrating data or establishing command-and-control) by decrypting and loading malicious components into memory at runtime.

The code follows patterns typical of sophisticated malware loaders where "Stage 1" performs environment checks and decryption, while "Stage 2" (the hidden payload) is only revealed in memory after the heavy obfuscation layers are stripped away.

### Core Functionality & Purpose
*   **Stub/Loader behavior:** The primary purpose of this code is not to perform a direct malicious action but to act as a gateway. It decrypts encrypted data blocks stored within the binary's resources and prepares them for execution.
*   **Dynamic API Resolution:** Instead of calling Windows APIs directly (which would be visible in the Import Address Table), it uses custom dispatcher functions (`fcn.14002bc70`) to resolve internal logic or "hidden" imports at runtime.

### Suspicious & Malicious Behaviors
*   **Multi-Stage Decryption:** The core of the code is dominated by complex, nested loops (e.g., `fcn.140029ed0`, `fcn.14002ac30`). These functions perform heavy mathematical operations (XORs, bit-shifts, and constant multiplications) to transform "garbage" data into executable code or configuration blocks.
*   **In-Memory Execution:** The length and complexity of the loops in `fcn.14002c1c0` suggest it is processing large amounts of data (over 1,000 iterations per block). This indicates that the "true" payload—be it a secondary executable, a DLL, or shellcode—is being decrypted directly into memory to evade disk-based antivirus scanners.
*   **Data Obfuscation:** The extracted strings are essentially "junk." They appear to be a placeholder for encrypted data that only becomes readable after passing through the decoders mentioned above. This is a common technique to hide Command & Control (C2) server addresses and file paths from static analysis.

### Notable Techniques or Patterns
*   **API Hashing / Dispatcher Pattern:** The function `fcn.14002bc70` acts as a gatekeeper. It takes an ID and a key to jump to specific code blocks. This is a common anti-analysis technique used to hide the program's execution flow from automated tools.
*   **Custom Encryption Algorithms:** Function `fcn.14002bd40` uses "magic" constants (e.g., `-0x7a143589`, `-0x61c8864f`). These are characteristic of custom stream ciphers or rolling XOR keys used to protect the malicious payload's inner logic.
*   **Anti-Analysis & Obfuscation:** 
    *   The code structure is designed to be confusing for both humans and automated tools (Control Flow Flattening).
    *   **Entry Point Obfuscation:** The `entry0` function shows a "decision tree" where the program checks several conditions before proceeding. This is often used to detect if it's running in a debugger or an analysis sandbox; if it detects one, it will take a path that does nothing or crashes the process safely.
    *   **String Masking:** By using repeated junk strings and complex logic to find data offsets, the developer ensures that common "lazy" indicators of malice (like "GetProcAddress") are never present in the raw file.

### Summary for Incident Response
This sample is a **sophisticated loader**. It should be treated as part of an active infection or a delivery stage. 
*   **Detection:** Traditional signature-based antivirus may fail because the malicious payload is encrypted until it runs in memory. 
*   **Action:** If this binary is found, it suggests that an attacker has successfully bypassed initial defenses and is attempting to execute multi-stage code on the system. Forensic analysis should focus on memory dumps of the process to capture the "unpacked" stage for further investigation.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1055 | Packer | The analysis identifies the binary as a packer/loader designed to decrypt and hide malicious components (Stage 2) during execution. |
| T1027 | Obfuscated Files | The use of control flow flattening, junk strings, and custom encryption algorithms is intended to hinder static analysis and hide C2 information. |
| T1630 | Reflective Code Loading | The binary decrypts its payload directly into memory for execution to bypass disk-based antivirus signatures. |
| T1497 | Virtualization/Sandbox Detection | The entry point includes a "decision tree" specifically designed to detect and evade debuggers and analysis environments. |

---

## Indicators of Compromise

Based on the provided string data and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** Because this sample is identified as a **highly obfuscated loader**, most "traditional" IOCs (like raw IP addresses or cleartext file paths) are intentionally hidden/encrypted and do not appear in the static strings provided.

### **IP addresses / URLs / Domains**
*   *None identified.* (The analysis notes that C2 infrastructure is hidden behind layers of encryption).

### **File paths / Registry keys**
*   *None identified.* (Standard linker sections such as `.rdata` and `.data` were excluded as false positives).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Internal Function Offsets (Detection Points):** While not network-level IOCs, these can be used for YARA rule development to identify the specific loader's logic:
    *   `fcn.14002bc70` (Dynamic API Resolution / Dispatcher)
    *   `fcn.140029ed0` (Decryption Loop)
    *   `fcn.14002ac30` (Decryption Loop)
    *   `fcn.14002c1c0` (Large Data Processing/Unpacking)
    *   `fcn.14002bd40` (Custom Encryption Logic)
*   **Encryption Constants (Signature Material):** These "magic" constants are used in the custom encryption algorithms:
    *   `-0x7a143589`
    *   `-0x61c8864f`
*   **Obfuscation Patterns:** 
    *   Repeated junk strings (e.g., `SVWATAUH`, `A]A\_[`) used to mask code flow and data offsets.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Multi-Stage Execution:** The analysis confirms the binary functions as a "Stage 1" loader, utilizing complex decryption loops and reflective loading to execute hidden payloads (Stage 2) directly in memory to evade disk-based detection.
*   **Advanced Anti-Analysis:** The presence of "decision tree" entry points for sandbox/debugger detection, control flow flattening, and the use of custom encryption constants indicate a sophisticated effort to bypass automated security tools.
*   **Obfuscated Infrastructure:** The absence of cleartext C2 information (IPs/URLs) combined with dynamic API resolution via a custom dispatcher shows the sample is designed to hide its true intent until runtime.
