# Threat Analysis Report

**Generated:** 2026-09-03 17:57 UTC
**Sample:** `13da375c854bdd1de35b2e7390416173a96797b14d3d1d90efed1984f1b81e2f_13da375c854bdd1de35b2e7390416173a96797b14d3d1d90efed1984f1b81e2f.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `13da375c854bdd1de35b2e7390416173a96797b14d3d1d90efed1984f1b81e2f_13da375c854bdd1de35b2e7390416173a96797b14d3d1d90efed1984f1b81e2f.exe` |
| File type | PE32 executable for MS Windows 6.00 (GUI), Intel i386, 5 sections |
| Size | 2,967,488 bytes |
| MD5 | `1298e6ebc440a4417665be2845b52114` |
| SHA1 | `8e4b7f7644ee93429293c92652e22d18b11ac001` |
| SHA256 | `13da375c854bdd1de35b2e7390416173a96797b14d3d1d90efed1984f1b81e2f` |
| Overall entropy | 6.522 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1647450385 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 2,472,960 | 6.329 | No |
| `.data` | 109,568 | 2.138 | No |
| `.idata` | 3,584 | 5.298 | No |
| `.rsrc` | 2,048 | 4.836 | No |
| `.reloc` | 368,128 | 7.374 | ⚠️ Yes |

### Imports

**KERNEL32.dll**: `MultiByteToWideChar`, `CloseHandle`, `ExpandEnvironmentStringsW`, `VirtualAlloc`, `VirtualFree`, `DeleteFileW`, `RaiseException`, `GetLastError`, `WriteFile`, `FlushFileBuffers`, `UnmapViewOfFile`, `CreateFileMappingW`, `MapViewOfFile`, `GetModuleHandleExW`, `GetProcAddress`
**RPCRT4.dll**: `UuidCreate`
**ADVAPI32.dll**: `EventActivityIdControl`, `EventRegister`, `EventUnregister`, `EventWriteTransfer`

## Extracted Strings

Total strings found: **6522** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.data
.idata
@.rsrc
@.reloc
.tks%d
m_pNativeThunkStubsSections
.tkd%d
      <Node Type="%s" Name="
" RVA="0x%08X" Length="0x%08X" Alignment="%u"/>

      <Node Type="%s" RVA="0x%08X" Length="0x%08X" Alignment="%u"/>

.drectve
___isa_available
__tls_index
.rdata
_RDATA
.debug
.debug$T
.debug$S
$eip $esp %u + ^ = 
$esp $esp %u + =
RhpFlt2Lng
CreateCommandLine
RhR2RLazyCheckVectorElemAddr
RhR2RLazyCheckCast
RhR2RLazyIsInstanceOf
RhR2RLazyAllocArray
RhR2RLazyAlloc
RhExceptionHandling_FailFast
RhExceptionHandling_ThrowClasslibOverflowException
RhExceptionHandling_ThrowClasslibIndexOutOfRangeException
RhExceptionHandling_ThrowClasslibDivideByZeroException
RhExceptionHandling_ThrowClasslibArithmeticException
RhExceptionHandling_ThrowInter
RhExceptionHandling_ThrowIntra
RhpPInvokeExceptionGuard
RhpRethrow
RhpThrowEx
RhNewArray
RhBoxAndNullCheck
RhArrayStoreCheckAny
RhUnboxAny
RhBoxAny
RhAllocLocal
RhTypeCast_CheckVectorElemAddr
RhGcStress_Initialize
RhTypeCast_CheckArrayStore
RhTypeCast_CheckUnbox
RhTypeCast_CheckCast
RhTypeCast_IsInstanceOf
RhTypeCast_CheckCastInterface
RhTypeCast_IsInstanceOfInterface
RhTypeCast_CheckCastArray
RhTypeCast_IsInstanceOfArray
RhTypeCast_CheckCastClass
RhTypeCast_IsInstanceOfClass
RhpCheckCctor2
RhpCheckedXchg
RhpCheckedLockCmpXchg
RhpLoopHijack
RhpWaitForGC
RhpWaitForSuspend
RhpTrapThreads
RhpResolveInterfaceMethod
RhpGcPollStress
RhpGcPoll
RhpGetThread
RhpEHJumpByrefGCStress
RhpEHJumpObjectGCStress
RhpEHJumpScalarGCStress
RhpEHJumpByref
RhpEHJumpObject
RhpEHJumpScalar
RhpUnsuppressGcStress
RhpSuppressGcStress
RhpHijackForGcStress
RhpShutdown
RhpDblRemRev_SSE2
RhpFltRemRev_SSE2
Flt2LngOvf
RhpDbl2ULng
Flt2IntOvf
Dbl2LngOvf
Dbl2ULngOvf
Dbl2IntOvf
RhpULDivMod
RhpLDivMod
RhpULMod
RhpULDiv
RhpLMod
RhpLDiv
ULMulOvf
LMulOvf
RhpLMul
RhpInitialInterfaceDispatch
RhpRegisterModule
RhpReversePInvokeReturn
RhpReversePInvoke
RhpPInvokeReturn
RhpCheckedAssignRefEBP
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.004c1d34` | `0x4c1d34` | 1400131 | ✓ |
| `fcn.004c1e41` | `0x4c1e41` | 1399924 | ✓ |
| `fcn.004c1fa0` | `0x4c1fa0` | 1399609 | ✓ |
| `fcn.004c2054` | `0x4c2054` | 1399447 | ✓ |
| `fcn.004c21cc` | `0x4c21cc` | 1399125 | ✓ |
| `fcn.004c2394` | `0x4c2394` | 1398710 | ✓ |
| `fcn.004c2446` | `0x4c2446` | 1398630 | ✓ |
| `fcn.004c2413` | `0x4c2413` | 1398601 | ✓ |
| `fcn.004c25b3` | `0x4c25b3` | 1398280 | ✓ |
| `fcn.004c2784` | `0x4c2784` | 1397832 | ✓ |
| `fcn.004c27e5` | `0x4c27e5` | 1397786 | ✓ |
| `fcn.004c2979` | `0x4c2979` | 1397399 | ✓ |
| `fcn.004c2a53` | `0x4c2a53` | 1397249 | ✓ |
| `fcn.004c2c1e` | `0x4c2c1e` | 1396811 | ✓ |
| `fcn.004c2d85` | `0x4c2d85` | 1396503 | ✓ |
| `fcn.004c303f` | `0x4c303f` | 1395888 | ✓ |
| `fcn.004c3255` | `0x4c3255` | 1395373 | ✓ |
| `fcn.004c338a` | `0x4c338a` | 1395147 | ✓ |
| `fcn.004c3584` | `0x4c3584` | 1394660 | ✓ |
| `fcn.004c373b` | `0x4c373b` | 1394263 | ✓ |
| `fcn.004c37c7` | `0x4c37c7` | 1394188 | ✓ |
| `fcn.004c3916` | `0x4c3916` | 1393870 | ✓ |
| `fcn.004c3bff` | `0x4c3bff` | 1393142 | ✓ |
| `fcn.004c3cda` | `0x4c3cda` | 1392974 | ✓ |
| `fcn.004c3e03` | `0x4c3e03` | 1392742 | ✓ |
| `fcn.004c3f59` | `0x4c3f59` | 1392414 | ✓ |
| `fcn.004c413b` | `0x4c413b` | 1392065 | ✓ |
| `fcn.004c3c95` | `0x4c3c95` | 1392049 | ✓ |
| `fcn.004c422a` | `0x4c422a` | 1391845 | ✓ |
| `fcn.004c4402` | `0x4c4402` | 1391425 | ✓ |

### Decompiled Code Files

- [`code/fcn.004c1d34.c`](code/fcn.004c1d34.c)
- [`code/fcn.004c1e41.c`](code/fcn.004c1e41.c)
- [`code/fcn.004c1fa0.c`](code/fcn.004c1fa0.c)
- [`code/fcn.004c2054.c`](code/fcn.004c2054.c)
- [`code/fcn.004c21cc.c`](code/fcn.004c21cc.c)
- [`code/fcn.004c2394.c`](code/fcn.004c2394.c)
- [`code/fcn.004c2413.c`](code/fcn.004c2413.c)
- [`code/fcn.004c2446.c`](code/fcn.004c2446.c)
- [`code/fcn.004c25b3.c`](code/fcn.004c25b3.c)
- [`code/fcn.004c2784.c`](code/fcn.004c2784.c)
- [`code/fcn.004c27e5.c`](code/fcn.004c27e5.c)
- [`code/fcn.004c2979.c`](code/fcn.004c2979.c)
- [`code/fcn.004c2a53.c`](code/fcn.004c2a53.c)
- [`code/fcn.004c2c1e.c`](code/fcn.004c2c1e.c)
- [`code/fcn.004c2d85.c`](code/fcn.004c2d85.c)
- [`code/fcn.004c303f.c`](code/fcn.004c303f.c)
- [`code/fcn.004c3255.c`](code/fcn.004c3255.c)
- [`code/fcn.004c338a.c`](code/fcn.004c338a.c)
- [`code/fcn.004c3584.c`](code/fcn.004c3584.c)
- [`code/fcn.004c373b.c`](code/fcn.004c373b.c)
- [`code/fcn.004c37c7.c`](code/fcn.004c37c7.c)
- [`code/fcn.004c3916.c`](code/fcn.004c3916.c)
- [`code/fcn.004c3bff.c`](code/fcn.004c3bff.c)
- [`code/fcn.004c3c95.c`](code/fcn.004c3c95.c)
- [`code/fcn.004c3cda.c`](code/fcn.004c3cda.c)
- [`code/fcn.004c3e03.c`](code/fcn.004c3e03.c)
- [`code/fcn.004c3f59.c`](code/fcn.004c3f59.c)
- [`code/fcn.004c413b.c`](code/fcn.004c413b.c)
- [`code/fcn.004c422a.c`](code/fcn.004c422a.c)
- [`code/fcn.004c4402.c`](code/fcn.004c4402.c)

## Behavioral Analysis

Based on the provided disassembly and strings, here is an analysis of the binary sample:

### Core Functionality and Purpose
The sample is a **managed .NET assembly** (or a wrapper for one). The presence of strings such as `System::String`, `RhPInvoke`, `Rh_LAdvCheck`, and various `Rh` prefixed functions indicates that this code is part of the .NET Common Language Runtime (CLR) or, more likely, a **highly obfuscated .NET executable** (using tools like ConfuserEx or similar).

The primary purpose of the logic shown in these specific functions appears to be **method resolution and state management** within an obfuscated environment. Rather than direct execution of malicious commands, this code handles the internal "plumbing" required to navigate a complex, protected code structure.

### Suspicious or Malicious Behaviors
While this specific snippet does not contain immediate "smoking gun" indicators like hardcoded IP addresses or raw shellcode injection instructions, it exhibits several behaviors characteristic of **malware loaders and packers**:

*   **Heavy Obfuscation (Control Flow Flattening/Abstraction):** The functions `fcn.004c1d34`, `fcn.004c21cc`, `fcn.004c303f`, and `fcn.004c373b` are structurally almost identical despite having different addresses. This is a hallmark of **packer logic**, where many different pieces of code are wrapped in identical "dispatcher" functions to hinder static analysis and make it difficult for an analyst to follow the execution flow.
*   **Indirect Mapping/Dispatching:** The frequent use of modular arithmetic (e.g., `uVar1 % arg_ch`, `arg_ch * 0x14`) and loop-based table lookups suggests that the code is resolving "real" functions from a protected table at runtime. This is often used to hide API imports (like `CreateRemoteThread` or `URLDownloadToFile`).
*   **Anti-Analysis via Complexity:** The complexity of the logic required just to perform simple assignments or checks indicates an effort to overwhelm automated analysis tools and human analysts by introducing "junk" calculations into the code flow.

### Notable Techniques and Patterns
*   **Intermediate Language (IL) Wrapping:** The `Rh` prefix on many functions suggests a transformation layer between the original .NET IL and the final machine code, used to hide the underlying logic of the original source.
*   **Stack-Based State Machine:** Many of these functions appear to be part of a state machine. Instead of a linear progression of code (Standard: A $\rightarrow$ B $\rightarrow$ C), the code jumps back and forth through the dispatcher loops, making it very difficult for automated tools to map out the logic.
*   **Memory-Resident Execution Preparation:** The repetitive structure of these functions is common in **"Staged Loaders."** These loaders are designed to unpack a second, malicious payload into memory. By using complex lookups for internal jumps, the loader makes it harder for security software to identify what the "next" piece of code will do until it is actually executed.

### Summary
This appears to be a **sophisticated packer or protector** used by malware (such as a Trojan or Downloader). The specific functions shown are not the "payload" itself, but rather the **obfuscation layer** designed to shield the actual malicious behavior from detection during the static analysis phase.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping of the observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The use of .NET packers (like ConfuserEx), control flow flattening, and "junk" calculations are primary methods to hinder static analysis and evade detection. |
| **T1027.005** | Packing | The analyst specifically identifies the core logic as a "packer," which wraps malicious code in an obfuscated layer to hide its true functionality from security tools. |
| **T1036** | Masquerading | While not explicitly stated, the use of a sophisticated "loader" for memory-resident execution is a common way to masquerade as legitimate system or application logic during analysis. |
| **T1105** | Ingress Tool Transfer (Related Logic) | The description of a "Staged Loader" suggests a multi-stage execution process where the current code's role is to prepare the environment for a secondary payload. |

### Analyst Notes:
*   **Control Flow Flattening:** While not its own unique MITRE ID, this specific behavior is a sub-method of **T1027**. It is used to transform the linear logic into a complex "switch" or "dispatcher" structure (the `fcn.xxxx` calls in your report), making it difficult for analysts to trace execution paths.
*   **API Obfuscation:** The use of modular arithmetic and table lookups to resolve "real" functions at runtime is a common tactic used to bypass static analysis of the Import Address Table (IAT). This behavior is also functionally grouped under **T1027**.
*   **Staged Loader Logic:** The report notes that the current binary is not the "payload" but an "obfuscation layer." In a full investigation, this suggests potential subsequent behaviors such as **T1055 (Process Injection)** or **T1056 (Example DLL Loading)** once the payload is unpacked into memory.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the extracted threat intelligence report:

### **IP addresses / URLs / Domains**
*   None identified.

### **File paths / Registry keys**
*   None identified (Note: `mrt100.dll` was identified in the strings but is a common library name and lacks a specific file path or malicious context to be considered a high-fidelity IOC).

### **Mutex names / Named pipes**
*   None identified.

### **Hashes**
*   None identified (Note: Hexadecimal addresses such as `0x1d34` are internal memory/segment offsets and do not constitute file hashes).

### **Other artifacts**
*   **Obfuscation Technique:** Use of **Control Flow Flattening** and **Operand Substitution**. 
*   **Protection Layer:** Evidence of **ConfuserEx** or similar .NET protection tools (indicated by the "Rh" prefixed functions and standard `.NET` internal symbols).
*   **Execution Style:** Identification of a **Staged Loader** architecture designed to hide final payload functionality.

---
**Analyst Note:** The provided data describes the mechanics of a sophisticated packer/protector rather than a specific malware campaign's infrastructure. While no immediate network indicators (IPs/URLs) are present, the behavioral analysis confirms that the sample is designed for anti-analysis and evasion.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Loader / Dropper
3. **Confidence**: Medium

**Key evidence**:
*   **Staged Loading Architecture:** The analysis identifies the sample as a "Staged Loader," meaning its primary function is not to execute a final payload but to act as an obfuscated delivery vehicle for secondary, potentially more malicious components.
*   **Advanced Obfuscation Techniques:** The use of control flow flattening, operand substitution, and dispatcher-based execution (common in tools like ConfuserEx) indicates a high level of effort to hide API imports and bypass static analysis.
*   **Defensive Shielding:** The "Rh" prefix functions and complex mathematical lookups for internal jumps are characteristic of specialized protectors designed to shield the true functionality of malware from security products during the initial infection phase.
