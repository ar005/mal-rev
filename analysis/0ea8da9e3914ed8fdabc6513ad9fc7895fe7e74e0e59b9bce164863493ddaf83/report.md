# Threat Analysis Report

**Generated:** 2026-08-13 19:18 UTC
**Sample:** `0ea8da9e3914ed8fdabc6513ad9fc7895fe7e74e0e59b9bce164863493ddaf83_0ea8da9e3914ed8fdabc6513ad9fc7895fe7e74e0e59b9bce164863493ddaf83.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0ea8da9e3914ed8fdabc6513ad9fc7895fe7e74e0e59b9bce164863493ddaf83_0ea8da9e3914ed8fdabc6513ad9fc7895fe7e74e0e59b9bce164863493ddaf83.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 6 sections |
| Size | 296,960 bytes |
| MD5 | `f92a58cdd2a53e3f62363544a9f6cfc0` |
| SHA1 | `13c09be1d5b9d77ea0cf8320e4620dd4d145f61c` |
| SHA256 | `0ea8da9e3914ed8fdabc6513ad9fc7895fe7e74e0e59b9bce164863493ddaf83` |
| Overall entropy | 7.849 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1765892281 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 20,480 | 6.009 | No |
| `.rdata` | 14,336 | 5.659 | No |
| `.data` | 246,272 | 7.999 | ⚠️ Yes |
| `.CRT` | 512 | 0.098 | No |
| `.rsrc` | 13,312 | 3.69 | No |
| `.reloc` | 1,024 | 6.378 | No |

### Imports

**KERNEL32.dll**: `GetConsoleOutputCP`, `lstrlenW`, `GetStdHandle`, `WriteFile`, `lstrcpynW`, `GetModuleHandleExW`, `ExpandEnvironmentStringsW`, `SetConsoleMode`, `VirtualAlloc`, `RemoveDirectoryW`, `GetModuleFileNameW`, `WaitForMultipleObjects`, `SetEnvironmentVariableW`, `SetThreadPriority`, `LeaveCriticalSection`
**USER32.dll**: `DrawTextW`, `GetSystemMetrics`
**GDI32.dll**: `GetTextMetricsW`, `DeleteDC`, `TextOutW`, `SetTextColor`, `SetBkMode`, `CreatePen`, `Rectangle`, `SetBkColor`, `Ellipse`, `DeleteObject`, `CreateSolidBrush`, `CreateFontIndirectW`, `GetDeviceCaps`, `StretchBlt`, `SelectObject`

### Exports

`@AgentNovaUnbind@0`, `@AgentWait@12`, `@BlockCacheCompressPlus@32`, `@BlockIoTSet@24`, `@BlockIoTSummon@32`, `@BlockMeshEnd@20`, `@BlockSecAscend@24`, `@BufferResume@4`, `@CachePushSync@28`, `@CacheTaskStop@32`, `@ChunkReceive@0`, `@ChunkStoreReset@4`, `@ConfigPull@0`, `@ConfigScan@24`, `@ContextAttach@20`, `@CrystalReceive@20`, `@CrystalScanFast@28`, `@DomainCoreEnd@4`, `@DomainEncryptFast@24`, `@EchoCloudAttach@32`, `@EchoSyncDeserialize@28`, `@EndpointExecute@24`, `@EndpointProcStop@8`, `@FrameVerify@32`, `@GraphEdgeSummon@8`, `@HandleAuthRelease@8`, `@HandleDecode@32`, `@IdentityAuthShatterSync@4`, `@IdentityDeserialize@8`, `@IndexCloudResume@12`, `@IndexParse@40`, `@KeyFetch@12`, `@KeySave@16`, `@LayerAIDecompress@20`, `@LayerEncryptPlus@8`, `@LayerSecReset@32`, `@ModelFluxExecute@8`, `@OrchestratorCoreRollback@24`, `@OrchestratorMLAnalyze@0`, `@OrchestratorProcValidate@20`, `@PhoenixJobCompress@20`, `@PipelineFluxSend@36`, `@PolicyLockSecure@36`, `@PolicySecNotify@24`, `@PortalCoreEncode@36`, `@PortalDataBegin@8`, `@PortalFree@12`, `@ProxyQuantumAttachSecure@16`, `@RadianceNodeStopFast@16`, `@RadianceStoreWrite@20`

## Extracted Strings

Total strings found: **1042** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
@.rsrc
@.reloc
T$0_^][
3t$03t$,
D$,3T$,
L$,2|$%2
2D$)2D$*0
?222L$
L$82D$
T$T2\$
t$<2(
D$<3D$L
D$ 2L$
|$$28
D$$_^]
D$x3T$ 
T$@2\$
\$<2L$
D$82(
3\$0
l$,1D$
D$(383H
D$(;D$
3|$$3
3|$(
3\$(3|$$3
\$<;\$H
Build.exe
@AgentNovaUnbind@0
@AgentWait@12
@BlockCacheCompressPlus@32
@BlockIoTSet@24
@BlockIoTSummon@32
@BlockMeshEnd@20
@BlockSecAscend@24
@BufferResume@4
@CachePushSync@28
@CacheTaskStop@32
@ChunkReceive@0
@ChunkStoreReset@4
@ConfigPull@0
@ConfigScan@24
@ContextAttach@20
@CrystalReceive@20
@CrystalScanFast@28
@DomainCoreEnd@4
@DomainEncryptFast@24
@EchoCloudAttach@32
@EchoSyncDeserialize@28
@EndpointExecute@24
@EndpointProcStop@8
@FrameVerify@32
@GraphEdgeSummon@8
@HandleAuthRelease@8
@HandleDecode@32
@IdentityAuthShatterSync@4
@IdentityDeserialize@8
@IndexCloudResume@12
@IndexParse@40
@KeyFetch@12
@KeySave@16
@LayerAIDecompress@20
@LayerEncryptPlus@8
@LayerSecReset@32
@ModelFluxExecute@8
@OrchestratorCoreRollback@24
@OrchestratorMLAnalyze@0
@OrchestratorProcValidate@20
@PhoenixJobCompress@20
@PipelineFluxSend@36
@PolicyLockSecure@36
@PolicySecNotify@24
@PortalCoreEncode@36
@PortalDataBegin@8
@PortalFree@12
@ProxyQuantumAttachSecure@16
@RadianceNodeStopFast@16
@RadianceStoreWrite@20
@RealmMLSignAdv@36
@RegistryMeshPull@24
@RiftAuthActivate@20
@RiftFlushPro@32
@RiftSignalAsync@28
@RouterLoad@8
@SchemaEdgeAdd@12
@ScopeBindPlus@20
@ServiceCoreSignalFast@16
@ServiceJobSet@8
@SessionEdgeCopyPrime@12
@SessionMLDecrypt@36
@SignalDataReserve@20
@StreamNotifySecure@4
@StreamRun@4
@TaskAuthLoadPrime@16
@TaskProcAwakenSync@4
@TokenNetAnalyze@20
@VaultAlloc@32
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004052a0` | `0x4052a0` | 3104 | ✓ |
| `fcn.00404910` | `0x404910` | 2440 | ✓ |
| `fcn.00403870` | `0x403870` | 2035 | ✓ |
| `fcn.00404070` | `0x404070` | 1162 | ✓ |
| `fcn.00404500` | `0x404500` | 1029 | ✓ |
| `fcn.00401580` | `0x401580` | 804 | ✓ |
| `fcn.00403410` | `0x403410` | 638 | ✓ |
| `entry0` | `0x401490` | 226 | ✓ |
| `fcn.00401b70` | `0x401b70` | 119 | ✓ |
| `fcn.00405f40` | `0x405f40` | 65 | ✓ |
| `fcn.00405f10` | `0x405f10` | 38 | ✓ |
| `sym.Build.exe__ZoneJobStart_20` | `0x401e10` | 33 | ✓ |
| `sym.Build.exe__CrystalScanFast_28` | `0x401ea0` | 31 | ✓ |
| `sym.Build.exe__DragonQuery_28` | `0x402ac0` | 28 | ✓ |
| `sym.Build.exe__PacketIoTCopyEx_20` | `0x402990` | 28 | ✓ |
| `sym.Build.exe__SignalQuantumRollback_28` | `0x402cf0` | 28 | ✓ |
| `sym.Build.exe_ForgeNetPublish` | `0x4026e0` | 24 | ✓ |
| `sym.Build.exe__WorkerValidate_16` | `0x402880` | 21 | ✓ |
| `sym.Build.exe__BlockProcSet_16` | `0x402de0` | 19 | ✓ |
| `sym.Build.exe__DomainVerify_8` | `0x4030c0` | 19 | ✓ |
| `sym.Build.exe_SchemaDataShatter` | `0x402690` | 19 | ✓ |
| `sym.Build.exe_ServiceEdgeDecrypt` | `0x402410` | 19 | ✓ |
| `sym.Build.exe__SchemaEdgeAdd_12` | `0x401f40` | 17 | ✓ |
| `sym.Build.exe__AgentProcMove_28` | `0x402ae0` | 17 | ✓ |
| `sym.Build.exe__DomainAuthAttach_12` | `0x402d10` | 17 | ✓ |
| `sym.Build.exe_RealmFlowDeserializeEx` | `0x402810` | 17 | ✓ |
| `sym.Build.exe__SessionJobSign_28` | `0x403330` | 17 | ✓ |
| `sym.Build.exe_VoidNodeAnalyze` | `0x402310` | 17 | ✓ |
| `sym.Build.exe__BlockCacheCompressPlus_32` | `0x401ca0` | 16 | ✓ |
| `sym.Build.exe__BlockIoTSet_24` | `0x401c00` | 16 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00401580.c`](code/fcn.00401580.c)
- [`code/fcn.00401b70.c`](code/fcn.00401b70.c)
- [`code/fcn.00403410.c`](code/fcn.00403410.c)
- [`code/fcn.00403870.c`](code/fcn.00403870.c)
- [`code/fcn.00404070.c`](code/fcn.00404070.c)
- [`code/fcn.00404500.c`](code/fcn.00404500.c)
- [`code/fcn.00404910.c`](code/fcn.00404910.c)
- [`code/fcn.004052a0.c`](code/fcn.004052a0.c)
- [`code/fcn.00405f10.c`](code/fcn.00405f10.c)
- [`code/fcn.00405f40.c`](code/fcn.00405f40.c)
- [`code/sym.Build.exe_ForgeNetPublish.c`](code/sym.Build.exe_ForgeNetPublish.c)
- [`code/sym.Build.exe_RealmFlowDeserializeEx.c`](code/sym.Build.exe_RealmFlowDeserializeEx.c)
- [`code/sym.Build.exe_SchemaDataShatter.c`](code/sym.Build.exe_SchemaDataShatter.c)
- [`code/sym.Build.exe_ServiceEdgeDecrypt.c`](code/sym.Build.exe_ServiceEdgeDecrypt.c)
- [`code/sym.Build.exe_VoidNodeAnalyze.c`](code/sym.Build.exe_VoidNodeAnalyze.c)
- [`code/sym.Build.exe__AgentProcMove_28.c`](code/sym.Build.exe__AgentProcMove_28.c)
- [`code/sym.Build.exe__BlockCacheCompressPlus_32.c`](code/sym.Build.exe__BlockCacheCompressPlus_32.c)
- [`code/sym.Build.exe__BlockIoTSet_24.c`](code/sym.Build.exe__BlockIoTSet_24.c)
- [`code/sym.Build.exe__BlockProcSet_16.c`](code/sym.Build.exe__BlockProcSet_16.c)
- [`code/sym.Build.exe__CrystalScanFast_28.c`](code/sym.Build.exe__CrystalScanFast_28.c)
- [`code/sym.Build.exe__DomainAuthAttach_12.c`](code/sym.Build.exe__DomainAuthAttach_12.c)
- [`code/sym.Build.exe__DomainVerify_8.c`](code/sym.Build.exe__DomainVerify_8.c)
- [`code/sym.Build.exe__DragonQuery_28.c`](code/sym.Build.exe__DragonQuery_28.c)
- [`code/sym.Build.exe__PacketIoTCopyEx_20.c`](code/sym.Build.exe__PacketIoTCopyEx_20.c)
- [`code/sym.Build.exe__SchemaEdgeAdd_12.c`](code/sym.Build.exe__SchemaEdgeAdd_12.c)
- [`code/sym.Build.exe__SessionJobSign_28.c`](code/sym.Build.exe__SessionJobSign_28.c)
- [`code/sym.Build.exe__SignalQuantumRollback_28.c`](code/sym.Build.exe__SignalQuantumRollback_28.c)
- [`code/sym.Build.exe__WorkerValidate_16.c`](code/sym.Build.exe__WorkerValidate_16.c)
- [`code/sym.Build.exe__ZoneJobStart_20.c`](code/sym.Build.exe__ZoneJobStart_20.c)

## Behavioral Analysis

Based on the disassembly provided, here is an analysis of the binary sample.

### Core Functionality and Purpose
The primary purpose of this code is as a **packer/loader (stub)**. The binary does not contain its actual malicious payload in its initial state; instead, it contains highly complex decryption routines designed to "unpack" or "decrypt" the actual executable code into memory at runtime.

### Suspicious and Malicious Behaviors
The following behaviors are indicative of a sophisticated piece of malware or a high-end packer:

*   **Heavy Obfuscation and Layered Decryption:** 
    *   `fcn.00404910` is a large, complex decryption routine. It uses multiple loops and intricate bitwise arithmetic (XORs, shifts, and additions) to transform data in memory. This is typical of **Stage-2 payload unpacking**.
    *   The code frequently accesses specific memory addresses (e.g., `0x4061e0`, `0x406220`) which act as "S-boxes" or hardcoded keys to decrypt different parts of the binary's internal state.
*   **Self-Modifying Code / In-Memory Execution:** 
    *   The function `fcn.00403870` performs memory allocations (`LocalAlloc`) and then passes those buffers into various transformation loops. This indicates that a payload is being decrypted directly into allocated memory, likely to be executed immediately after the stub completes its work.
*   **Anti-Analysis/Deobfuscation Resistance:** 
    *   The sheer complexity of `fcn.004052a0` and `fcn.00401580` suggests a "junk code" or "complex logic" approach to thwart static analysis. By making the decryption math nearly impossible to follow by hand, the author forces researchers to use dynamic analysis (debugging) to see what is actually being decrypted.
*   **Payload Hiding:** 
    *   The `entry0` function serves as the loader's entry point. It manages the progression through various "stages" of decryption before handing over execution to the final, unpacked payload.

### Notable Techniques and Patterns
*   **Signature Evasion via Junk Data:** The extensive list of "Extracted Strings" (e.g., `@AgentNovaUnbind`, `@CrystalScanFast`, `@QuantumReach`) appears to be a **distraction technique**. These names are programmatically generated or pulled from a large table to bloat the binary and clutter the string table, making it harder for analysts to quickly identify keywords or malicious functionality.
*   **Cyclic/Complex Arithmetic (Custom Ciphers):** Instead of using standard libraries like AES, the code uses custom-built rolling XOR loops and "bit-shuffling" logic. This is a common way to hide the nature of the payload from automated scanners that look for standard cryptographic constants.
*   **Memory Manipulation:** The use of `LocalAlloc` followed by immediate decryption of those segments suggests the malware intends to run its primary logic entirely in memory (fileless execution) or within a hijacked process, minimizing its footprint on the disk.
*   **Tail Jump/OEP Transition:** In `entry0`, after several calls to unpacking functions (`fcn.00403870` and `fcn.00403410`), there is likely a jump to an "Original Entry Point" (OEP), where the decrypted code begins its execution.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1027 | Obfuscated Files or Information | The use of "junk code," complex bitwise arithmetic, and custom ciphers is intended to hinder static analysis and hide the payload's true functionality. |
| T1055 | Packing | The binary functions as a packer/loader stub that decrypts and unpacks an executable payload into memory at runtime. |
| T1027.001 | (Sub-technique of T1027) Junk Code | The inclusion of "distraction" strings and complex logic is specifically designed to waste the time of analysts and complicate manual deobfuscation. |
| T1036 | Masquerading | While not strictly masquerading as a system process, the use of decoy strings (e.g., @AgentNovaUnbind) serves as a distraction technique to hide malicious intent. |

***Note on mapping:** While "Tail Jump" and "In-Memory Execution" are specific behaviors observed in your analysis, they fall under the broader MITRE ATT&CK categories of **T1055 (Packing)** and **T1027 (Obfuscated Files or Information)**.*

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `Build.exe` (Potential internal component or unpacked payload name)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Malware Type:** Sophisticated Packer/Loader (Stub).
*   **Obfuscation Technique:** Junk Code Injection. The high volume of `@` prefixed strings (e.g., `@AgentNovaUnbind`, `@CrystalScanFast`, `@QuantumReach`) is identified as a distraction tactic to complicate static analysis and inflate the string table.
*   **Decoding Mechanism:** Custom-built rolling XOR loops and "bit-shuffling" logic instead of standard cryptographic libraries.
*   **Memory Manipulation:** Use of `LocalAlloc` for in-memory execution (fileless behavior) before reaching a Tail Jump to the Original Entry Point (OEP).
*   **Hardcoded Offsets:** Use of specific memory offsets (`0x4061e0`, `0x406220`) as "S-boxes" or keys for decryption.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: loader
3. **Confidence**: High

4. **Key evidence**:
*   **Loader/Packer Architecture:** The analysis explicitly identifies the sample as a "packer/loader (stub)" that utilizes complex, multi-layer decryption routines and S-boxes to unpack an actual payload into memory at runtime.
*   **Evasive Execution Techniques:** The use of `LocalAlloc` for in-memory execution and the presence of a "Tail Jump" to an Original Entry Point (OEP) are signature behaviors of loaders designed to execute code while minimizing its footprint on the disk.
*   **Advanced Obfuscation:** The presence of intentionally misleading junk strings (e.g., `@AgentNovaUnbind`) and custom-built rolling XOR loops indicates a high level of effort to bypass static analysis and automated detection systems.
