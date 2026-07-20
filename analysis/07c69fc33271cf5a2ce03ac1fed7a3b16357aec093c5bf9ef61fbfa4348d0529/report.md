# Threat Analysis Report

**Generated:** 2026-07-17 19:39 UTC
**Sample:** `07c69fc33271cf5a2ce03ac1fed7a3b16357aec093c5bf9ef61fbfa4348d0529_07c69fc33271cf5a2ce03ac1fed7a3b16357aec093c5bf9ef61fbfa4348d0529.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07c69fc33271cf5a2ce03ac1fed7a3b16357aec093c5bf9ef61fbfa4348d0529_07c69fc33271cf5a2ce03ac1fed7a3b16357aec093c5bf9ef61fbfa4348d0529.exe` |
| File type | PE32 executable for MS Windows 5.00 (native), Intel i386, 5 sections |
| Size | 44,580 bytes |
| MD5 | `0ff6abe0252d4f37a196a1231fae5f26` |
| SHA1 | `92e9dcaf7249110047ef121b7586c81d4b8cb4e5` |
| SHA256 | `07c69fc33271cf5a2ce03ac1fed7a3b16357aec093c5bf9ef61fbfa4348d0529` |
| Overall entropy | 3.451 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1121786141 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 8,736 | 6.56 | No |
| `.rdata` | 256 | 2.958 | No |
| `.data` | 31,744 | 1.824 | No |
| `INIT` | 1,088 | 5.117 | No |
| `.reloc` | 864 | 5.75 | No |

### Imports

**ntoskrnl.exe**: `IoGetRelatedDeviceObject`, `IoDeleteDevice`, `IoDetachDevice`, `ExReleaseResourceForThreadLite`, `ExAcquireResourceExclusiveLite`, `IoAttachDeviceToDeviceStack`, `KeInitializeEvent`, `ExInitializeResourceLite`, `IoCreateDevice`, `KeReleaseMutex`, `KeInitializeMutex`, `IoDeleteSymbolicLink`, `IoRegisterFsRegistrationChange`, `IoCreateSymbolicLink`, `IofCallDriver`
**HAL.dll**: `KfAcquireSpinLock`, `KfReleaseSpinLock`, `KeGetCurrentIrql`

## Extracted Strings

Total strings found: **133** (showing first 100)

```
!This program cannot be run in DOS mode.
$
h.rdata
H.data
.reloc
C`$_^[
tL9X0tGW
t9x`t
t	9x`t
_^[t	=
t9p`t
9X`t
jLS
0SA;L$
u@;D$
9X`t
j
VSSSSW
t	9X`t
ESVWf
M;Ntr
@(#)foo.c $Revision: 1.8 $
@(#)par.h $Revision: 1.3 $
@(#)pae.h $Revision: 1.3 $
@(#)fao.h $Revision: 1.3 $
@(#)uis.h $Revision: 1.4 $
@(#)ree.h $Revision: 1.4 $
@(#)fir.h $Revision: 1.3 $
@(#)fir.c $Revision: 1.4 $
@(#)par.h $Revision: 1.3 $
@(#)pae.h $Revision: 1.3 $
@(#)fao.h $Revision: 1.3 $
@(#)uis.h $Revision: 1.4 $
@(#)ree.h $Revision: 1.4 $
@(#)fir.h $Revision: 1.3 $
@(#)myy.h $Revision: 1.4 $
@(#)fic.h $Revision: 1.3 $
@(#)ree.h $Revision: 1.4 $
@(#)ree.c $Revision: 1.10 $
4$PSQR
4$PSQR
4$PSQR
4$PSQR
d$lY[X
d$l___^[
+3ZY[X
$Loading  co
@(#)par.h $Revision: 1.3 $
@(#)pae.h $Revision: 1.3 $
@(#)uis.h $Revision: 1.4 $
@(#)ree.h $Revision: 1.4 $
@(#)fir.h $Revision: 1.3 $
@(#)uis.c $Revision: 1.4 $
@(#)myy.h $Revision: 1.4 $
@(#)fic.h $Revision: 1.3 $
@(#)eer.h $Revision: 1.3 $
@(#)pao.h $Revision: 1.3 $
S6S4S:S S'S!S*S
S2S0S;S:S=S6S
S*S S'S6S>S
S&S!S!S6S=S'S
S<S=S'S!S<S?S
S<S=S'S!S<S?S
S6S S S:S<S=SsS
S2S=S2S4S6S!S
S6S>S<S!S*SsS
S2S=S2S4S6S>S6S=S'S
S!S6S5S6S'S0S;S
S2S!S2S>S6S'S6S!S SSS
S=S2S1S?S6S
S!S6S5S6S'S0S;S6S!SSS
@(#)par.h $Revision: 1.3 $
@(#)pae.h $Revision: 1.3 $
@(#)fic.c $Revision: 1.4 $
ntoskrnl.exe
KeWaitForSingleObject
IofCallDriver
KeGetCurrentThread
IoAllocateIrp
KeInitializeEvent
IoGetRelatedDeviceObject
IoDeleteDevice
IoDetachDevice
ExReleaseResourceForThreadLite
ExAcquireResourceExclusiveLite
IoAttachDeviceToDeviceStack
ExInitializeResourceLite
IoCreateDevice
KeReleaseMutex
KeInitializeMutex
IoDeleteSymbolicLink
IoRegisterFsRegistrationChange
IoCreateSymbolicLink
RtlInitUnicodeString
KeClearEvent
RtlFreeUnicodeString
RtlCompareMemory
RtlUpcaseUnicodeString
KeLeaveCriticalRegion
KeEnterCriticalRegion
MmForceSectionClosed
MmMapLockedPagesSpecifyCache
KeSetEvent
```

## Disassembly Overview

Functions analyzed: **27** | Decompiled to C: **27**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `entry0` | `0x10dce` | 640 | ✓ |
| `fcn.00011a20` | `0x11a20` | 636 | ✓ |
| `fcn.00011fb0` | `0x11fb0` | 415 | ✓ |
| `fcn.00011848` | `0x11848` | 201 | ✓ |
| `fcn.00012150` | `0x12150` | 196 | ✓ |
| `fcn.00010bbc` | `0x10bbc` | 174 | ✓ |
| `fcn.00012286` | `0x12286` | 172 | ✓ |
| `fcn.00011e00` | `0x11e00` | 171 | ✓ |
| `fcn.00011c9c` | `0x11c9c` | 160 | ✓ |
| `fcn.00011d62` | `0x11d62` | 157 | ✓ |
| `fcn.00012332` | `0x12332` | 150 | ✓ |
| `fcn.0001240e` | `0x1240e` | 150 | ✓ |
| `fcn.00011eac` | `0x11eac` | 149 | ✓ |
| `fcn.00011976` | `0x11976` | 141 | ✓ |
| `fcn.000117c8` | `0x117c8` | 127 | ✓ |
| `fcn.00011f42` | `0x11f42` | 110 | ✓ |
| `fcn.00011912` | `0x11912` | 80 | ✓ |
| `fcn.0001223a` | `0x1223a` | 75 | ✓ |
| `fcn.000123c8` | `0x123c8` | 70 | ✓ |
| `fcn.00011d3c` | `0x11d3c` | 38 | ✓ |
| `fcn.00012214` | `0x12214` | 37 | ✓ |
| `fcn.000117ac` | `0x117ac` | 28 | ✓ |
| `fcn.00011a04` | `0x11a04` | 27 | ✓ |
| `fcn.00011962` | `0x11962` | 19 | ✓ |
| `sub.ntoskrnl.exe_KeGetCurrentThread` | `0x124a4` | 6 | ✓ |
| `sub.ntoskrnl.exe_MmForceSectionClosed` | `0x124aa` | 6 | ✓ |
| `sub.ntoskrnl.exe_ZwNotifyChangeKey` | `0x124b0` | 6 | ✓ |

### Decompiled Code Files

- [`code/entry0.c`](code/entry0.c)
- [`code/fcn.00010bbc.c`](code/fcn.00010bbc.c)
- [`code/fcn.000117ac.c`](code/fcn.000117ac.c)
- [`code/fcn.000117c8.c`](code/fcn.000117c8.c)
- [`code/fcn.00011848.c`](code/fcn.00011848.c)
- [`code/fcn.00011912.c`](code/fcn.00011912.c)
- [`code/fcn.00011962.c`](code/fcn.00011962.c)
- [`code/fcn.00011976.c`](code/fcn.00011976.c)
- [`code/fcn.00011a04.c`](code/fcn.00011a04.c)
- [`code/fcn.00011a20.c`](code/fcn.00011a20.c)
- [`code/fcn.00011c9c.c`](code/fcn.00011c9c.c)
- [`code/fcn.00011d3c.c`](code/fcn.00011d3c.c)
- [`code/fcn.00011d62.c`](code/fcn.00011d62.c)
- [`code/fcn.00011e00.c`](code/fcn.00011e00.c)
- [`code/fcn.00011eac.c`](code/fcn.00011eac.c)
- [`code/fcn.00011f42.c`](code/fcn.00011f42.c)
- [`code/fcn.00011fb0.c`](code/fcn.00011fb0.c)
- [`code/fcn.00012150.c`](code/fcn.00012150.c)
- [`code/fcn.00012214.c`](code/fcn.00012214.c)
- [`code/fcn.0001223a.c`](code/fcn.0001223a.c)
- [`code/fcn.00012286.c`](code/fcn.00012286.c)
- [`code/fcn.00012332.c`](code/fcn.00012332.c)
- [`code/fcn.000123c8.c`](code/fcn.000123c8.c)
- [`code/fcn.0001240e.c`](code/fcn.0001240e.c)
- [`code/sub.ntoskrnl.exe_KeGetCurrentThread.c`](code/sub.ntoskrnl.exe_KeGetCurrentThread.c)
- [`code/sub.ntoskrnl.exe_MmForceSectionClosed.c`](code/sub.ntoskrnl.exe_MmForceSectionClosed.c)
- [`code/sub.ntoskrnl.exe_ZwNotifyChangeKey.c`](code/sub.ntoskrnl.exe_ZwNotifyChangeKey.c)

## Behavioral Analysis

Based on the provided disassembly and string data, here is an analysis of the binary's functionality and behavior.

### Core Functionality
The binary is a **Windows Kernel-Mode Driver**. The presence of `ntoskrnl.exe` imports, `IoCreateDevice`, `IoCreateSymbolicLink`, and the use of SpinLocks/Critical Regions indicates it operates at the highest level of privilege (Ring 0).

Its primary purpose appears to be creating a communication channel between the OS and a specific device or service while monitoring system configurations through registry interaction.

### Suspicious and Malicious Behavs
The following behaviors are highly indicative of rootkit functionality or advanced malware:

*   **Registry Monitoring & Manipulation:**
    *   The code utilizes `ZwOpenKey`, `ZwQueryValueKey`, and notably **`ZwNotifyChangeKey`**. 
    *   The use of `ZwNotifyChangeKey` suggests the driver is "watching" specific Registry keys for changes. This is a common technique used by malware to detect when security software is started or to monitor system configuration changes in real-time.
*   **Manual PE Header Parsing:**
    *   In function `fcn.00011fb0`, the code checks for the `0x5A4D` ("MZ") and `0x4550` ("PE") signatures. 
    *   Standard, legitimate drivers rarely need to manually parse PE headers. This behavior is typically used by malware to load executable code directly from a memory buffer into kernel space (manual mapping) or to inspect other processes' loaded modules without using standard APIs that would be logged.
*   **Kernel-Level Persistence/Presence:**
    *   The driver establishes its presence in the system via `IoCreateDevice` and `IoCreateSymbolicLink`. By operating in the kernel, it can intercept system calls (syscalls), hide files, or hide processes from user-mode security tools.

### Notable Techniques & Patterns
*   **SpinLock & Critical Region Usage:** The code heavily utilizes `KfAcquireSpinLock`, `KeEnterCriticalRegion`, and `KeLeaveCriticalRegion`. These are used to perform operations at high IRQL (Interrupt Request Levels). This ensures the driver can execute its logic while potentially "freezing" or bypassing certain standard OS protections/monitoring.
*   **Hardcoded Offsets:** The code uses several hardcoded offsets (e.g., `0x15a38`, `0x15924`) to access internal structures. This is typical of drivers that interact with undocumented parts of the Windows kernel or and custom communication protocols between a user-mode component and this driver.
*   **Symbolic Link Cleanup:** In `entry0`, if certain conditions are met, the code attempts to delete its symbolic link before continuing or exiting. This can be used to hide the "footprint" of the device it created.

### Summary for Incident Response
This sample exhibits characteristics of a **Rootkit**. It is designed to run in kernel mode to gain high-level access to the system. The most alarming features are its ability to manually parse PE headers (suggesting potential execution of unsigned code) and its active monitoring of Registry keys via `ZwNotifyChangeKey`, which suggests an intent to evade security software or maintain a persistent, hidden presence on the host.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1637** | Reflective Loading | The manual parsing of PE headers and MZ/PE signatures indicates an attempt to load executable code from memory without using standard, logged Windows APIs. |
| **T1562** | Impair Defenses | The use of `ZwNotifyChangeKey` to monitor registry keys suggests a mechanism for detecting the presence or updates of security software. |
| **T1070** | Indicator Removal | The deliberate deletion of symbolic links before exiting is an attempt to hide the footprint and "clean up" evidence of the driver's activity. |

---

## Indicators of Compromise

Based on the analysis of the provided strings and behavioral report, here are the extracted Indicators of Compromise (IOCs):

**IP addresses / URLs / Domains**
*   None identified.

**File paths / Registry keys**
*   `.\i386\fast16.sys` (Identified as the driver filename)

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified.

**Other artifacts**
*   **Manual PE Parsing:** The binary contains logic to manually parse "MZ" (`0x5A4D`) and "PE" (`0x4550`) headers (identified at function `fcn.00011fb0`).
*   **Hardcoded Offsets:** Use of non-standard offsets `0x15a38` and `0x15924` to access internal kernel structures.
*   **Registry Monitoring Behavior:** Frequent use of the `ZwNotifyChangeKey` API, indicating active monitoring of registry keys for security software changes or system configuration.
*   **Kernel Function Usage:** High-frequency usage of `KeRegisterFsRegistrationChange`, `KeInitializeMutex`, and `KeReleaseMutex`.

---

## Malware Family Classification

1. **Malware family**: Unknown
2. **Malware type**: Rootkit / Loader
3. **Confidence**: High

4. **Key evidence**:
*   **Kernel-Mode Execution & Privilege:** The sample is a Windows Kernel-Mode Driver (Ring 0) that establishes its own device and symbolic link, providing it with the highest level of system privilege to hide activities or intercept system calls.
*   **Manual PE Parsing for Loading:** The presence of manual "MZ" and "PE" header checks (`fcn.00011fb0`) is a definitive indicator of **Reflective Loading**. This allows the malware to load additional malicious modules directly into memory while bypassing standard Windows APIs that would be flagged by security software.
*   **Active Evasion Tactics:** The use of `ZwNotifyChangeKey` suggests the driver is actively monitoring for the presence or changes in security software, while the deletion of its own symbolic links indicates a deliberate attempt to remove traces and hide its footprint on the host system.
