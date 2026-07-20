# Threat Analysis Report

**Generated:** 2026-07-18 02:50 UTC
**Sample:** `082cefa4daf662f5e1358779c49347c997938675ba134b939a81a9557ce0b38d_082cefa4daf662f5e1358779c49347c997938675ba134b939a81a9557ce0b38d.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `082cefa4daf662f5e1358779c49347c997938675ba134b939a81a9557ce0b38d_082cefa4daf662f5e1358779c49347c997938675ba134b939a81a9557ce0b38d.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 6 sections |
| Size | 11,237,376 bytes |
| MD5 | `2dead59422250009e89e5df5d8ee4b4a` |
| SHA1 | `174e8f4d2bebf0a11eb8db5db91e16dac5cc86dc` |
| SHA256 | `082cefa4daf662f5e1358779c49347c997938675ba134b939a81a9557ce0b38d` |
| Overall entropy | 7.944 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1767800243 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 123,904 | 5.224 | No |
| `.rdata` | 7,168 | 5.77 | No |
| `.data` | 386,560 | 7.952 | ⚠️ Yes |
| `.idata` | 4,608 | 4.91 | No |
| `.rsrc` | 10,699,776 | 7.948 | ⚠️ Yes |
| `.reloc` | 14,336 | 5.912 | No |

### Exports

`@AiFreeScannerV5A@0`, `@AiMatchHandle@20`, `@AttachBufferV4@8`, `@AuthConnectWriter@24`, `@AuthScaleAgentA@16`, `@AuthSplitLexerV4@24`, `@Callback_348@0`, `@CharDeleteBuilder@8`, `@CharUpperToken@0`, `@ClearLexer@12`, `@CommitCatalog@12`, `@ConvertScope@20`, `@ConvertWorkerEx@8`, `@CoreDecompressReader@24`, `@CoreSaveTask@20`, `@DecompressBuffer@4`, `@DeserializeNode@24`, `@EncryptModelA@28`, `@ExportFunc_278@24`, `@ExportFunc_760@8`, `@Export_2267@24`, `@Export_5164@0`, `@Export_7563@4`, `@Export_9234@0`, `@Export_9570@24`, `@FlushBufferV3@8`, `@Function_814@12`, `@Handler_366@4`, `@Handler_870@16`, `@InitChunk@0`, `@JoinPacket@24`, `@JoinSignal@0`, `@LocaleBindValidator@8`, `@LocaleNormalizeEvent@24`, `@LocaleSignRegistryV2@16`, `@MatchValidator@0`, `@MergeParser@24`, `@Method_260@20`, `@MlLowerKey@20`, `@MoveReader@16`, `@MultiInitDomain@4`, `@NetDecompressFrame@12`, `@NetEncodeIndex@8`, `@NetReceiveStream@4`, `@NetReserveRouterEx@4`, `@NormalizeZoneA@20`, `@NotifyDomain@12`, `@Operation_684@16`, `@PadJob@4`, `@PadStream@4`

## Extracted Strings

Total strings found: **36448** (showing first 100)

```
`.rdata
@.data
.idata
@.reloc
ttf9.uo
D$8M#!
1D$P1l$L
D$ G;{
D$,F;s
D$,F;s
2E@2E*2E
2472t$
D$82>2
l$,20
282*
tqf9/ul
D$HF;s
D$HF;s
D$H3L$T
D$02(
t$T2(2
2
D$LF;s
D$ F;s
D$ G;{
t3;HPs.
Ot[F;s
App.exe
@AiFreeScannerV5A@0
@AiMatchHandle@20
@AttachBufferV4@8
@AuthConnectWriter@24
@AuthScaleAgentA@16
@AuthSplitLexerV4@24
@Callback_348@0
@CharDeleteBuilder@8
@CharUpperToken@0
@ClearLexer@12
@CommitCatalog@12
@ConvertScope@20
@ConvertWorkerEx@8
@CoreDecompressReader@24
@CoreSaveTask@20
@DecompressBuffer@4
@DeserializeNode@24
@EncryptModelA@28
@ExportFunc_278@24
@ExportFunc_760@8
@Export_2267@24
@Export_5164@0
@Export_7563@4
@Export_9234@0
@Export_9570@24
@FlushBufferV3@8
@Function_814@12
@Handler_366@4
@Handler_870@16
@InitChunk@0
@JoinPacket@24
@JoinSignal@0
@LocaleBindValidator@8
@LocaleNormalizeEvent@24
@LocaleSignRegistryV2@16
@MatchValidator@0
@MergeParser@24
@Method_260@20
@MlLowerKey@20
@MoveReader@16
@MultiInitDomain@4
@NetDecompressFrame@12
@NetEncodeIndex@8
@NetReceiveStream@4
@NetReserveRouterEx@4
@NormalizeZoneA@20
@NotifyDomain@12
@Operation_684@16
@PadJob@4
@PadStream@4
@ProcSubstrBlockEx@16
@PublishParser@24
@ReceiveResourceA@16
@ResetResource@4
@ReverseConverter@0
@ScaleConverterV4@12
@SearchBufferV3@12
@SecUpdateBufferA@8
@SetToken@20
@SignalPolicy@16
@StartParser@24
@StoreResumeCred@24
@SyncAttachWorker@0
@SyncPutBuffer@12
@SyncStartRealm@16
@TaskFetchIndex@12
@TaskUnlockScope@12
@TextCopySignal@4
@TextDecryptValidator@8
@TranslateRealm@0
@UnbindFilterA@4
@UnbindStream@24
@UpdateIndex@20
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0041d410` | `0x41d410` | 3863 | ✓ |
| `fcn.0041c490` | `0x41c490` | 3088 | ✓ |
| `fcn.0041be10` | `0x41be10` | 1661 | ✓ |
| `fcn.0041eda0` | `0x41eda0` | 1094 | ✓ |
| `fcn.0041e9d0` | `0x41e9d0` | 971 | ✓ |
| `fcn.0041ba70` | `0x41ba70` | 915 | ✓ |
| `fcn.0041e5e0` | `0x41e5e0` | 588 | ✓ |
| `entry0` | `0x41b6d0` | 517 | ✓ |
| `fcn.0041d0a0` | `0x41d0a0` | 433 | ✓ |
| `fcn.0041f1f0` | `0x41f1f0` | 423 | ✓ |
| `fcn.0041d260` | `0x41d260` | 422 | ✓ |
| `fcn.0041e830` | `0x41e830` | 412 | ✓ |
| `fcn.0041e330` | `0x41e330` | 349 | ✓ |
| `fcn.0041e490` | `0x41e490` | 329 | ✓ |
| `fcn.0041b8e0` | `0x41b8e0` | 297 | ✓ |
| `fcn.0041ba10` | `0x41ba10` | 88 | ✓ |
| `fcn.0041ae10` | `0x41ae10` | 43 | ✓ |
| `fcn.0040100f` | `0x40100f` | 40 | ✓ |
| `sym.App.exe__IotMatchScope_20` | `0x41af40` | 32 | ✓ |
| `sym.App.exe_TextDisconnectConverterA` | `0x41b350` | 23 | ✓ |
| `sym.App.exe__DeserializeNode_24` | `0x41b650` | 21 | ✓ |
| `sym.App.exe__LocaleSignRegistryV2_16` | `0x41b610` | 21 | ✓ |
| `sym.App.exe__ProcSubstrBlockEx_16` | `0x41b5f0` | 21 | ✓ |
| `sym.App.exe__DisconnectServiceV5_20` | `0x41b0c0` | 21 | ✓ |
| `sym.App.exe__EdgeJoinResource_12` | `0x41afc0` | 21 | ✓ |
| `sym.App.exe__RemoveRealm_12` | `0x41b030` | 21 | ✓ |
| `sym.App.exe__MultiFlushConverterEx_24` | `0x41afe0` | 20 | ✓ |
| `sym.App.exe__CoreResumeDomainA_12` | `0x41b190` | 19 | ✓ |
| `sym.App.exe_LocaleLockOrchestrator` | `0x41b390` | 19 | ✓ |
| `sym.App.exe_MatchValidatorV3` | `0x41b2c0` | 19 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.0040100f.c`](code/fcn.0040100f.c)
- [`code/fcn.0041ae10.c`](code/fcn.0041ae10.c)
- [`code/fcn.0041b8e0.c`](code/fcn.0041b8e0.c)
- [`code/fcn.0041ba10.c`](code/fcn.0041ba10.c)
- [`code/fcn.0041ba70.c`](code/fcn.0041ba70.c)
- [`code/fcn.0041be10.c`](code/fcn.0041be10.c)
- [`code/fcn.0041c490.c`](code/fcn.0041c490.c)
- [`code/fcn.0041d0a0.c`](code/fcn.0041d0a0.c)
- [`code/fcn.0041d260.c`](code/fcn.0041d260.c)
- [`code/fcn.0041d410.c`](code/fcn.0041d410.c)
- [`code/fcn.0041e330.c`](code/fcn.0041e330.c)
- [`code/fcn.0041e490.c`](code/fcn.0041e490.c)
- [`code/fcn.0041e5e0.c`](code/fcn.0041e5e0.c)
- [`code/fcn.0041e830.c`](code/fcn.0041e830.c)
- [`code/fcn.0041e9d0.c`](code/fcn.0041e9d0.c)
- [`code/fcn.0041eda0.c`](code/fcn.0041eda0.c)
- [`code/fcn.0041f1f0.c`](code/fcn.0041f1f0.c)
- [`code/sym.App.exe_LocaleLockOrchestrator.c`](code/sym.App.exe_LocaleLockOrchestrator.c)
- [`code/sym.App.exe_MatchValidatorV3.c`](code/sym.App.exe_MatchValidatorV3.c)
- [`code/sym.App.exe_TextDisconnectConverterA.c`](code/sym.App.exe_TextDisconnectConverterA.c)
- [`code/sym.App.exe__CoreResumeDomainA_12.c`](code/sym.App.exe__CoreResumeDomainA_12.c)
- [`code/sym.App.exe__DeserializeNode_24.c`](code/sym.App.exe__DeserializeNode_24.c)
- [`code/sym.App.exe__DisconnectServiceV5_20.c`](code/sym.App.exe__DisconnectServiceV5_20.c)
- [`code/sym.App.exe__EdgeJoinResource_12.c`](code/sym.App.exe__EdgeJoinResource_12.c)
- [`code/sym.App.exe__IotMatchScope_20.c`](code/sym.App.exe__IotMatchScope_20.c)
- [`code/sym.App.exe__LocaleSignRegistryV2_16.c`](code/sym.App.exe__LocaleSignRegistryV2_16.c)
- [`code/sym.App.exe__MultiFlushConverterEx_24.c`](code/sym.App.exe__MultiFlushConverterEx_24.c)
- [`code/sym.App.exe__ProcSubstrBlockEx_16.c`](code/sym.App.exe__ProcSubstrBlockEx_16.c)
- [`code/sym.App.exe__RemoveRealm_12.c`](code/sym.App.exe__RemoveRealm_12.c)

## Behavioral Analysis

Based on the provided disassembly and string analysis, here is the technical analysis of the binary:

### Core Functionality and Purpose
The code appears to be a highly sophisticated piece of software featuring **multi-layered encryption, obfuscation, and complex data processing**. While the presence of strings like "AiFreeScanner," "AuthConnectWriter," and "NetReceiveStream" suggests it may belong to a professional application (possibly related to AI or network analysis), in a malware context, these types of names are often used as **decoy identifiers** for internal routines that handle encrypted communications.

The primary purpose of the functions shown is not simple execution but rather the **transformation of data**. The code spends significant resources on complex mathematical operations to decode or "unpack" information before use.

### Suspicious and Malicious Behaviors
*   **Heavy Obfuscation / Custom Cryptography:** 
    Functions such as `fcn.0041d410`, `fcn.0041c490`, and particularly `fcn.0041ba70` contain dense, non-standard loops involving bitwise XORs, shifts, and multi-step arithmetic logic. This is a hallmark of **custom encryption algorithms** used to bypass signature-based detection by avoiding standard library calls (like Windows CryptoAPI).
*   **Complex Decoding Loop:** 
    The structure of `fcn.0041d410` suggests it is decoding a large block of data (potentially an encrypted configuration or a secondary payload) in memory. The high level of complexity implies that the "real" functionality of the code is hidden behind these decryption layers.
*   **Multi-Stage Initialization:** 
    The entry point (`entry0`) calls `fcn.0041ae10` multiple times before proceeding to core logic. This pattern is commonly used in **malware loaders** or "stagers" to initialize environment checks, decrypt anti-analysis checks, or prepare the memory space for a secondary payload.
*   **Decoy Strings:** 
    The extensive list of "professional-sounding" strings (e.g., `_IntellectQueryAlgorithm`, `_NetDecompressFrame`) suggests an attempt to blend in with legitimate complex software while masking specific malicious functionalities (like C2 communication or data exfiltration).

### Notable Techniques and Patterns
*   **Custom Logic Gates:** The use of magic numbers (e.g., `0x1eba950c`, `0x6c92ea91`) in `fcn.0041ba70` indicates a custom-tailored hashing or encryption routine, making it harder for automated tools to identify the algorithm as standard AES or RSA.
*   **Memory Management/Manipulation:** Several functions involve large buffer allocations and manual loop processing of these buffers (e.g., `fcn.0041d260` and `fcn.0041e5e0`). This suggests the program may be decompressing or "unpacking" data in-memory to avoid writing suspicious files to disk.
*   **Nested Offsets:** The code frequently uses complex pointer arithmetic (e.g., `piVar2 = *(***(*(*(unaff_FS_OFFSET + 0x30) + 0xc) + 0xc) + 0x18)`). This is often a sign of **anti-debugging** or techniques to access internal structures while bypassing standard security monitoring.
*   **High Complexity Overhead:** The sheer amount of code required just to perform what appears to be simple data manipulation (as seen in the 300+ line `fcn.0041d410`) is a common tactic used by advanced persistent threats (APTs) to slow down manual analysis and exhaust the analyst's resources.

### Summary for Incident Response
This sample is **highly suspicious** and exhibits characteristics of an advanced piece of malware or a sophisticated crypter/loader. The primary risk is that the core functionality is hidden behind several layers of custom encryption. If this is a malicious sample, it likely acts as a **downloader or protector** for subsequent stages of an attack.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files/Information | The use of custom cryptography, dense bitwise logic, and complex decoding loops is designed to hide the program's true functionality from signature-based detection and manual analysis. |
| **T1036** | Masquerading | The inclusion of professional-sounding "decoy" strings (e.g., `AiFreeScanner`) is intended to blend the malicious process with legitimate system software. |
| **T1497** | Virtualized Environment | The use of complex pointer arithmetic and nested offsets (like `unaff_FS_OFFSET`) indicates anti-debugging/anti-analysis techniques used to detect or bypass security monitoring tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** While the analysis confirms the binary is highly suspicious and likely a malicious loader/crypter, it does not contain "high-fidelity" network indicators (like specific IP addresses or URLs) or file system paths. The available data consists primarily of internal function names and memory offsets.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   **App.exe** (Note: This is a generic filename; no specific path was provided).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *No MD5, SHA1, or SHA256 hashes were present in the strings.*

### **Other artifacts**
*   **Custom Encryption Constants (Magic Numbers):** 
    *   `0x1eba950c`
    *   `0x6c92ea91`
*   **Suspicious Function Offsets (Internal Tracking):** 
    *   `fcn.0041d410` (Complex decoding loop)
    *   `fcn.0041c490` (Encryption/Obfuscation logic)
    *   `fcn.0041ba70` (Custom hashing/encryption routine)
*   **Behavioral Patterns:** 
    *   Multi-layered encryption/obfuscation.
    *   Use of "decoy" strings to mask C2 communication and data exfiltration logic.
    *   In-memory unpacking of payloads to bypass disk-based detection.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: Medium

4. **Key evidence**:
*   **Multi-layered Obfuscation & Custom Encryption:** The analysis highlights several complex, non-standard loops (e.g., `fcn.0041ba70`) using bitwise operations and "magic numbers" to bypass signature-based detection rather than using standard system libraries.
*   **In-Memory Payload Delivery:** The presence of large buffer allocations and decoding loops suggests the binary is designed to unpack or decompress a secondary payload directly into memory to evade disk-based security scanners.
*   **Anti-Analysis Tactics:** The use of "decoy" strings (like `AiFreeScanner`) to mask malicious intent, combined with complex pointer arithmetic (`unaff_FS_OFFSET`) to bypass debuggers/security monitoring, is characteristic of a sophisticated loader or stager.
