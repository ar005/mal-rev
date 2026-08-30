# Threat Analysis Report

**Generated:** 2026-08-23 05:52 UTC
**Sample:** `113a05106b85844a4fcc943e5b06af75bb45c22cec1e6aa30400a13e00dcfc22_113a05106b85844a4fcc943e5b06af75bb45c22cec1e6aa30400a13e00dcfc22.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `113a05106b85844a4fcc943e5b06af75bb45c22cec1e6aa30400a13e00dcfc22_113a05106b85844a4fcc943e5b06af75bb45c22cec1e6aa30400a13e00dcfc22.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 628,472 bytes |
| MD5 | `b7e31b72a11298cc1a2da18ad6ee17bc` |
| SHA1 | `6a8dfb68735ef059845a4925a46626876c0863d0` |
| SHA256 | `113a05106b85844a4fcc943e5b06af75bb45c22cec1e6aa30400a13e00dcfc22` |
| Overall entropy | 6.8 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1775121153 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 153,088 | 5.617 | No |
| `.rdata` | 14,336 | 5.451 | No |
| `.data` | 264,192 | 7.837 | ⚠️ Yes |
| `.pdata` | 1,024 | 2.811 | No |
| `.idata` | 5,120 | 4.132 | No |
| `.rsrc` | 172,544 | 3.347 | No |
| `.reloc` | 7,168 | 5.37 | No |

### Exports

`AccessAllocateEncoder`, `AccessDecryptEncoder`, `AccessInspectChannel`, `AcquireDispatcher`, `AcquireEndpoint`, `AcquireObjectNew`, `AcquireOption`, `AdapterSendToken`, `AdjustParameter`, `AdjustPropertyV4`, `AlgorithmHandleer`, `AlgorithmManager`, `AlgorithmUpdateer`, `AllocCorrectDomain`, `AllocDisconnectDispatcher`, `AllocReleaseEntity`, `AllocTestObject`, `AllocUnlockInstance`, `AllocateDispatcherPublic`, `AllocateOption`, `AllocateStack`, `AnalyzeVerifierOld`, `ArchiveCheckSession`, `ArchiveCorrecter`, `ArchiveEnable`, `ArchiveManager`, `ArchiveParseer`, `ArchiveReader`, `ArchiveService`, `ArrayBuilder`, `ArrayHandler`, `ArrayManager`, `ArrayReceiveer`, `AudioParseProvider`, `AuthLockValidator`, `AuthModifyDecompressor`, `AuthSignalController`, `BaseAcquireComponent`, `BindEndpoint`, `BindEntity`, `BindFormatter`, `BufferBuildEncryptor`, `BufferEncryptFormatter`, `BufferHandleRule`, `BufferManager`, `BufferParser`, `BuilderManager`, `BuilderProcessString`, `BuilderReadValidator`, `CacheDecryptProvider`

## Extracted Strings

Total strings found: **8016** (showing first 100)

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
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140023680` | `0x140023680` | 3423 | ✓ |
| `fcn.1400243e0` | `0x1400243e0` | 2700 | ✓ |
| `fcn.1400250d0` | `0x1400250d0` | 1284 | ✓ |
| `fcn.140025f90` | `0x140025f90` | 1084 | ✓ |
| `fcn.140025b10` | `0x140025b10` | 664 | ✓ |
| `fcn.140023470` | `0x140023470` | 518 | ✓ |
| `fcn.140024e70` | `0x140024e70` | 516 | ✓ |
| `fcn.1400263d0` | `0x1400263d0` | 348 | ✓ |
| `fcn.140025db0` | `0x140025db0` | 291 | ✓ |
| `fcn.140025a40` | `0x140025a40` | 196 | ✓ |
| `fcn.140025ee0` | `0x140025ee0` | 166 | ✓ |
| `fcn.140026530` | `0x140026530` | 151 | ✓ |
| `fcn.140025740` | `0x140025740` | 139 | ✓ |
| `fcn.140025830` | `0x140025830` | 134 | ✓ |
| `fcn.140025980` | `0x140025980` | 96 | ✓ |
| `fcn.1400259e0` | `0x1400259e0` | 96 | ✓ |
| `section..text` | `0x140001000` | 95 | ✓ |
| `fcn.140023420` | `0x140023420` | 80 | ✓ |
| `entry0` | `0x140025620` | 79 | ✓ |
| `fcn.1400258c0` | `0x1400258c0` | 78 | ✓ |
| `fcn.14000105f` | `0x14000105f` | 63 | ✓ |
| `fcn.1400257d0` | `0x1400257d0` | 46 | ✓ |
| `fcn.140025800` | `0x140025800` | 39 | ✓ |
| `fcn.140025930` | `0x140025930` | 35 | ✓ |
| `fcn.140025710` | `0x140025710` | 33 | ✓ |
| `fcn.140025960` | `0x140025960` | 28 | ✓ |
| `fcn.140025910` | `0x140025910` | 28 | ✓ |
| `fcn.14000109e` | `0x14000109e` | 11 | ✓ |
| `sym.App.exe_AcquireEndpoint` | `0x1400250c0` | 8 | ✓ |
| `sym.App.exe_AllocTestObject` | `0x140025600` | 8 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.14000105f.c`](code/fcn.14000105f.c)
- [`code/fcn.14000109e.c`](code/fcn.14000109e.c)
- [`code/fcn.140023420.c`](code/fcn.140023420.c)
- [`code/fcn.140023470.c`](code/fcn.140023470.c)
- [`code/fcn.140023680.c`](code/fcn.140023680.c)
- [`code/fcn.1400243e0.c`](code/fcn.1400243e0.c)
- [`code/fcn.140024e70.c`](code/fcn.140024e70.c)
- [`code/fcn.1400250d0.c`](code/fcn.1400250d0.c)
- [`code/fcn.140025710.c`](code/fcn.140025710.c)
- [`code/fcn.140025740.c`](code/fcn.140025740.c)
- [`code/fcn.1400257d0.c`](code/fcn.1400257d0.c)
- [`code/fcn.140025800.c`](code/fcn.140025800.c)
- [`code/fcn.140025830.c`](code/fcn.140025830.c)
- [`code/fcn.1400258c0.c`](code/fcn.1400258c0.c)
- [`code/fcn.140025910.c`](code/fcn.140025910.c)
- [`code/fcn.140025930.c`](code/fcn.140025930.c)
- [`code/fcn.140025960.c`](code/fcn.140025960.c)
- [`code/fcn.140025980.c`](code/fcn.140025980.c)
- [`code/fcn.1400259e0.c`](code/fcn.1400259e0.c)
- [`code/fcn.140025a40.c`](code/fcn.140025a40.c)
- [`code/fcn.140025b10.c`](code/fcn.140025b10.c)
- [`code/fcn.140025db0.c`](code/fcn.140025db0.c)
- [`code/fcn.140025ee0.c`](code/fcn.140025ee0.c)
- [`code/fcn.140025f90.c`](code/fcn.140025f90.c)
- [`code/fcn.1400263d0.c`](code/fcn.1400263d0.c)
- [`code/fcn.140026530.c`](code/fcn.140026530.c)
- [`code/section..text.c`](code/section..text.c)
- [`code/sym.App.exe_AcquireEndpoint.c`](code/sym.App.exe_AcquireEndpoint.c)
- [`code/sym.App.exe_AllocTestObject.c`](code/sym.App.exe_AllocTestObject.c)

## Behavioral Analysis

Based on the provided disassembly and decompiled C pseudocode, the binary is a **multi-stage packer/loader** designed to hide malicious functionality through heavy obfuscation and anti-analysis techniques.

### Core Functionality and Purpose
The primary purpose of this code is to act as a "stub" or "loader." It does not perform any obvious useful actions; instead, it decrypts an embedded payload in memory and executes it, while ensuring the core malicious logic remains hidden from static analysis.

### Suspicious and Malicious Behaviors

*   **Persistence Mechanism:**
    *   The function `fcn.1400250d0` specifically interacts with the Windows Registry to achieve persistence. It targets the key: `Software\Microsoft\Windows\CurrentVersion\Run`.
    *   It attempts to register a program name (appears as `"EojeWocC"`, likely a dynamically generated or obfuscated name) into this key, ensuring the malware automatically starts every time the user logs in.

*   **Anti-Analysis & Anti-Debugging:**
    *   The `section..text` function contains common anti-analysis checks: `rdtsc` (used to detect timing discrepancies caused by debuggers), `cpuid_basic_0`, and `rdrand`. These are frequently used to detect virtual machines or specialized analysis environments.
    *   The code uses a "jump" logic in `entry0` that only proceeds if certain conditions are met, likely skipping out of execution if it detects a debugger.

*   **Dynamic String Construction:**
    *   Instead of storing sensitive strings (like registry paths) in the `.data` section where they could be easily read by security tools, the code constructs them at runtime using a hardcoded alphabet (`str.abcdefghijklmnopqrstuvwxyz0123456789`) and an index-based selection process within `fcn.1400250d0`.

### Notable Techniques & Patterns

*   **API Hashing:**
    *   The function `fcn.140025a40` is a classic **API Hash resolution routine**. Instead of calling functions like `RegOpenKeyEx` directly (which would appear in the Import Address Table), it takes a hardcoded hash (e.g., `0x622d0185`, `0x9129b2a8`) and searches for the corresponding function address in memory. This is a standard technique used to hide the malware's capabilities from static analysis.

*   **Multi-Layered Decryption:**
    *   Functions `fcn.140023680` and `fcn.1400243e0` contain highly complex, nested loops involving heavy arithmetic (XORing, bit-shifting, and modular multiplication). This indicates that the payload is encrypted multiple times before it is ever executed in memory.

*   **Custom Loader Logic:**
    *   The function `fcn.140025ee0` acts as a transition point, jumping from the "loader" logic into the actual unpacked "payload." The use of `UNRECOVERED_JUMPTABLE` and heavy obfuscation suggests this is where the packer finishes its job and hands control over to the malicious payload.

### Summary Table for Analysts
| Feature | Observation | Significance |
| :--- | :--- | :--- |
| **Persistence** | Registry `Run` key modification | Ensures malware survives a reboot. |
| **Obfuscation** | API Hashing (`fcn.140025a40`) | Hides the imports (e.g., Networking, File I/O). |
| **Evasion** | `rdtsc`, `cpuid` usage | Detects virtual machines and debuggers. |
| **Payload Masking** | Complex XOR/Arithmetic loops | Protects the final malicious payload from scanners. |

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder | The malware modifies the `Software\Microsoft\Windows\CurrentVersion\Run` registry key to ensure it executes automatically upon user login. |
| **T1497** | Virtualization/Sandbox Evasion | The use of `rdtsc`, `cpuid`, and `rdrand` instructions is a common method for detecting virtualized environments or debugger presence. |
| **T1027** | Obfuscated Files/Information | The implementation of API hashing, dynamic string construction, and multi-layered decryption (XOR/bit-shifting) serves to hide the payload's true functionality from static analysis. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   *None identified.*

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\Run`
*   **Registry Value Name:** `EojeWocC` (Note: Identified as a likely obfuscated/dynamic name for the persistence mechanism).

**Mutex names / Named pipes**
*   *None identified.*

**Hashes**
*   *No file hashes (MD5/SHA1/SHA256) were present in the provided strings.* 
*   *(Note: The values `0x622d0185` and `0x9129b2a8` are identified as **API Hashes** used for internal function resolution, not file hashes.)*

**Other artifacts**
*   **API Hashes (Function Resolution):** `0x622d0185`, `0x9129b2a8`
*   **Anti-Analysis Techniques:** Use of `rdtsc`, `cpuid_basic_0`, and `rdrand` to detect debuggers/VMs.
*   **Internal Function Offsets (Potential for YARA rule development):** 
    *   `fcn.1400250d0` (Persistence logic)
    *   `fcn.140025a40` (API Hash resolution)
    *   `fcn.140023680` & `fcn.1400243e0` (Decryption loops)
    *   `fcn.140025ee0` (Payload transition point)

---

## Malware Family Classification

1. **Malware family**: Unknown (The analysis describes a generic loader/packer; without the decrypted payload, it cannot be linked to a specific campaign like Cobalt Strike or Emotet.)
2. **Malware type**: Loader / Packer
3. **Confidence**: High (Regarding its role as a loader)
4. **Key evidence**: 
    *   **Stub Architecture:** The analysis identifies the binary as a "multi-stage packer/loader" that uses complex, nested decryption loops (XOR, bit-shifting) to hide an embedded payload from static scanners.
    *   **Evasion & Obfuscation:** The use of API hashing (`fcn.140025a40`), dynamic string construction, and anti-analysis instructions (`rdtsc`, `cpuid`) are hallmark characteristics of a loader designed to protect the subsequent malicious payload.
    *   **Persistence Mechanism:** The inclusion of logic to modify the Windows Registry `Run` key ensures that once the loader successfully executes, it maintains persistence on the host system.
