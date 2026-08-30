# Threat Analysis Report

**Generated:** 2026-08-24 23:02 UTC
**Sample:** `12049c977e193972b665995720243571cf775f6f0428460192536d92c8528dbb_12049c977e193972b665995720243571cf775f6f0428460192536d92c8528dbb.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `12049c977e193972b665995720243571cf775f6f0428460192536d92c8528dbb_12049c977e193972b665995720243571cf775f6f0428460192536d92c8528dbb.exe` |
| File type | PE32+ executable for MS Windows 10.00 (GUI), x86-64, 9 sections |
| Size | 461,528 bytes |
| MD5 | `b039cd6770b1bc655e2935f1f34dce2c` |
| SHA1 | `f7dc4f63e212fdc69d70dd4f1527486586c4fd9f` |
| SHA256 | `12049c977e193972b665995720243571cf775f6f0428460192536d92c8528dbb` |
| Overall entropy | 6.456 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 300518272 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 65,536 | 6.104 | No |
| `fothk` | 4,096 | 0.016 | No |
| `.rdata` | 20,480 | 4.193 | No |
| `.data` | 4,096 | 0.105 | No |
| `.pdata` | 4,096 | 3.879 | No |
| `.detourc` | 12,288 | 2.086 | No |
| `.detourd` | 4,096 | 0.02 | No |
| `.rsrc` | 323,584 | 6.642 | No |
| `.reloc` | 4,096 | 2.427 | No |

### Imports

**ADVAPI32.dll**: `RegDeleteValueW`, `CheckTokenMembership`, `FreeSid`, `RegSetValueExW`, `RegCreateKeyExW`, `AllocateAndInitializeSid`, `RegCloseKey`, `RegQueryValueExW`, `RegEnumValueW`, `RegCreateKeyW`, `RegOpenKeyExW`, `RegOpenKeyExA`, `RegSetValueExA`, `RegDeleteKeyW`, `RegQueryValueExA`
**KERNEL32.dll**: `CloseHandle`, `CreateThread`, `SetFileAttributesA`, `GetProcAddress`, `DeleteCriticalSection`, `CreateProcessW`, `FreeLibrary`, `lstrcmpiA`, `lstrcmpiW`, `LoadLibraryExW`, `GetModuleFileNameA`, `FindFirstFileA`, `SetLastError`, `GetFullPathNameW`, `CreateDirectoryExA`
**USER32.dll**: `CharNextW`, `LoadStringW`, `PostQuitMessage`
**msvcrt.dll**: `_onexit`, `__dllonexit`, `_unlock`, `_lock`, `_commode`, `_fmode`, `_wcmdln`, `memset`, `_initterm`, `__setusermatherr`, `_cexit`, `_exit`, `exit`, `__set_app_type`, `__wgetmainargs`
**ntdll.dll**: `RtlLookupFunctionEntry`, `RtlVirtualUnwind`, `RtlCaptureContext`
**ole32.dll**: `CoRegisterClassObject`, `CoRevokeClassObject`, `CoInitialize`, `CoTaskMemAlloc`, `CoUninitialize`, `CoCreateInstance`, `CoTaskMemFree`, `CoImpersonateClient`, `CoRevertToSelf`, `CoGetCallContext`, `StringFromGUID2`, `CoInitializeSecurity`, `CLSIDFromString`, `CoInitializeEx`
**OLEAUT32.dll**: `UnRegisterTypeLib`, `UnRegisterTypeLibForUser`, `RegisterTypeLibForUser`, `RegisterTypeLib`, `SysStringLen`, `SysAllocString`, `SysFreeString`
**RPCRT4.dll**: `RpcStringFreeW`, `UuidCreate`, `UuidToStringW`
**urlmon.dll**: `CompatFlagsFromClsid`, `Extract`, `CoInternetCreateSecurityManager`, `ord_519`, `ord_107`, `CoInternetSetFeatureEnabled`
**WINTRUST.dll**: `CryptCATAdminReleaseContext`, `CryptCATAdminAddCatalog`, `CryptCATAdminAcquireContext`, `CryptCATAdminReleaseCatalogContext`
**AUTHZ.dll**: `AuthzFreeResourceManager`, `AuthzFreeContext`, `AuthzInitializeContextFromSid`, `AuthzInitializeResourceManager`, `AuthzAccessCheck`
**iertutil.dll**: `ord_172`, `ord_34`, `ord_134`, `ord_39`, `ord_57`, `ord_201`, `ord_200`, `ord_35`, `ord_650`, `ord_658`

## Extracted Strings

Total strings found: **884** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`fothk
`.rdata
@.data
.pdata
@.detourc
@.detourd
@.reloc
u L97tH
u*9Q<|%
LcA<E3
L$8u1H
%uNHcI
SUVWATAUAWH
PA_A]A\_^][
PA_A]A\_^][
PA_A]A\_^][
PA_A]A\_^][
PA_A]A\_^][
%u9Hc{
wnH9CPuhL
9dtrRt
WATAUAVAWH
 A_A^A]A\_
UWATAVAWH
fD9<Au
fD9<xu
A_A^A\_]
f98t
H
VWAUAVAWH
H!\$H3
H!\$@H
A_A^A]_^
UVWATAUAVAWH
 A_A^A]A\_^]
t$ UWAVH
UVWAUAVH
PA^A]_^]
x UATAUAVAWH
l$XD9)
fD9,Au
A_A^A]A\]
UWATAVAWH
D$`D9'
A_A^A\_]
VWATAVAWH
A_A^A\_^
L$ SVWAVH
8A^_^[
VWATAVAWH
0A_A^A\_^
UVWATAUAVAWH
fE94Du
fE94Gu
fD94Au
fD94Au
fD94yu
L$hD91t
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
L$ UWAVH
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
L!|$0E3
L!|$xH
A_A^A]A\_^]
9Y(t9Y,u
t"9_(t
H;BXu2I
H;B`u(I
\$ UVWH
x ATAVAWH
 A_A^A\
<\t<:t
UVWATAUAVAWH
 A_A^A]A\_^]
SUVWATAVAWH
fD9$Yu
fD9$Wu
fD9$Wu
@A_A^A\_^][
@SUVWATAVAWH
A_A^A\_^][
l$ VWAVH
H!\$`H
tsH!\$XH
l$ VWAVH
t$ WATAUAVAWH
f98t
H
 A_A^A]A\_
\$ VWAVH
t$ UWAVH
MPH!D$@L
H!D$HH
UVWATAUAVAWH
PA_A^A]A\_^]
fD94Gu
UATAUAVAWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.140010d40` | `0x140010d40` | 63422 | ✓ |
| `fcn.1400062c0` | `0x1400062c0` | 2185 | ✓ |
| `fcn.14000dcc0` | `0x14000dcc0` | 2011 | ✓ |
| `fcn.140007524` | `0x140007524` | 1905 | ✓ |
| `fcn.1400029e0` | `0x1400029e0` | 1527 | ✓ |
| `fcn.14000cb84` | `0x14000cb84` | 1372 | ✓ |
| `fcn.14000c614` | `0x14000c614` | 1210 | ✓ |
| `fcn.140005214` | `0x140005214` | 1089 | ✓ |
| `fcn.1400022e0` | `0x1400022e0` | 1019 | ✓ |
| `fcn.140005be0` | `0x140005be0` | 894 | ✓ |
| `fcn.140007070` | `0x140007070` | 890 | ✓ |
| `fcn.140006b50` | `0x140006b50` | 796 | ✓ |
| `fcn.140008d34` | `0x140008d34` | 792 | ✓ |
| `fcn.14000e7e8` | `0x14000e7e8` | 776 | ✓ |
| `fcn.14000f554` | `0x14000f554` | 775 | ✓ |
| `fcn.1400056d0` | `0x1400056d0` | 756 | ✓ |
| `fcn.140004ea4` | `0x140004ea4` | 730 | ✓ |
| `fcn.14001041c` | `0x14001041c` | 706 | ✓ |
| `fcn.14000eca4` | `0x14000eca4` | 704 | ✓ |
| `fcn.14000f8e8` | `0x14000f8e8` | 695 | ✓ |
| `fcn.140009054` | `0x140009054` | 685 | ✓ |
| `fcn.14000acd4` | `0x14000acd4` | 683 | ✓ |
| `fcn.140009308` | `0x140009308` | 674 | ✓ |
| `fcn.14000b4f8` | `0x14000b4f8` | 655 | ✓ |
| `fcn.14000df74` | `0x14000df74` | 633 | ✓ |
| `fcn.140001d60` | `0x140001d60` | 632 | ✓ |
| `fcn.14000c27c` | `0x14000c27c` | 629 | ✓ |
| `fcn.140003090` | `0x140003090` | 623 | ✓ |
| `fcn.14000af88` | `0x14000af88` | 613 | ✓ |
| `fcn.14000ff80` | `0x14000ff80` | 611 | ✓ |

### Decompiled Code Files

- [`code/fcn.140001d60.c`](code/fcn.140001d60.c)
- [`code/fcn.1400022e0.c`](code/fcn.1400022e0.c)
- [`code/fcn.1400029e0.c`](code/fcn.1400029e0.c)
- [`code/fcn.140003090.c`](code/fcn.140003090.c)
- [`code/fcn.140004ea4.c`](code/fcn.140004ea4.c)
- [`code/fcn.140005214.c`](code/fcn.140005214.c)
- [`code/fcn.1400056d0.c`](code/fcn.1400056d0.c)
- [`code/fcn.140005be0.c`](code/fcn.140005be0.c)
- [`code/fcn.1400062c0.c`](code/fcn.1400062c0.c)
- [`code/fcn.140006b50.c`](code/fcn.140006b50.c)
- [`code/fcn.140007070.c`](code/fcn.140007070.c)
- [`code/fcn.140007524.c`](code/fcn.140007524.c)
- [`code/fcn.140008d34.c`](code/fcn.140008d34.c)
- [`code/fcn.140009054.c`](code/fcn.140009054.c)
- [`code/fcn.140009308.c`](code/fcn.140009308.c)
- [`code/fcn.14000acd4.c`](code/fcn.14000acd4.c)
- [`code/fcn.14000af88.c`](code/fcn.14000af88.c)
- [`code/fcn.14000b4f8.c`](code/fcn.14000b4f8.c)
- [`code/fcn.14000c27c.c`](code/fcn.14000c27c.c)
- [`code/fcn.14000c614.c`](code/fcn.14000c614.c)
- [`code/fcn.14000cb84.c`](code/fcn.14000cb84.c)
- [`code/fcn.14000dcc0.c`](code/fcn.14000dcc0.c)
- [`code/fcn.14000df74.c`](code/fcn.14000df74.c)
- [`code/fcn.14000e7e8.c`](code/fcn.14000e7e8.c)
- [`code/fcn.14000eca4.c`](code/fcn.14000eca4.c)
- [`code/fcn.14000f554.c`](code/fcn.14000f554.c)
- [`code/fcn.14000f8e8.c`](code/fcn.14000f8e8.c)
- [`code/fcn.14000ff80.c`](code/fcn.14000ff80.c)
- [`code/fcn.14001041c.c`](code/fcn.14001041c.c)
- [`code/fcn.140010d40.c`](code/fcn.140010d40.c)

## Behavioral Analysis

This updated analysis incorporates the findings from both code chunks. The addition of the second chunk reinforces the initial assessment that this is a sophisticated piece of malware, likely an advanced **downloader/dropper** with significant capabilities for environment preparation and evasion.

### Executive Summary
The provided code belongs to a **highly sophisticated downloader/dropper**. It utilizes a wide range of Windows API calls to establish persistence, manipulate file system permissions, ensure stealth through automated cleanup, and prepare the host for subsequent stages of an infection. The binary deliberately mimics legitimate installer behaviors (like those used by Internet Explorer components) to blend into standard system processes while performing high-level administrative tasks such as **Security Descriptor manipulation** and **recursive directory cleaning**.

---

### Core Functionality and Purpose
The code's primary role is to "pave the way" for a final payload. It achieves this through:

1.  **Persistence & Masking:** Using `RunOnce` keys and hijacking COM objects (via `CLSID/AppID`) to ensure it—or its dropped components—run consistently under various system contexts.
2.  **Security & Privilege Manipulation:** The code contains routines to interact with **Security Descriptors** and **SACLs (System Access Control Lists)**. This is used to modify the permissions of files or folders, potentially ensuring that the malicious payload has sufficient privileges to execute or hide from security software.
3.  **Payload Staging & Management:** It utilizes complex string manipulation and file handling routines (`GetFinalPathNameByHandleW`, `CopyFileW`) to manage "staged" components (often using extensions like `.dat`) before they are executed as final payloads.
4.  **Environment Preparation:** By leveraging `IEAdvpack.dll` and similar system-trusted binaries, it masks its active communication or file-writing activities as standard installation updates.

---

### Suspicious and Malicious Behaviors

*   **Privilege Escalation/Permission Manipulation (New Finding):**
    *   In `fcn.14000af88`, the code uses `GetKernelObjectSecurity` and `GetSecurityDescriptorSacl`. This is a high-level operation used to modify how the OS handles security for specific objects. In a malware context, this is often used to grant the malware's processes elevated rights or to "unlock" files so that they can be modified by other malicious processes.
*   **Recursive File & Directory Cleanup:**
    *   `fcn.14000acd4` implements logic for **recursive directory removal**. It doesn't just delete a single file; it scans and clears entire directory trees. This is used to "mop up" evidence of the staging process, deleting temporary files, installers, or logs that would alert an analyst to its presence.
*   **Sophisticated File System Interaction:**
    *   The code uses `GetFinalPathNameByHandleW` (in `fcn.140009054`) and `CopyFileW`. These are used to resolve and move files across the filesystem, likely to hide a payload's original location or rename it to something less suspicious before execution.
*   **Advanced Persistence & Hijacking:**
    *   The code manipulates **CLSID** and **AppID** (from previous chunks). By masquerading as an "Installer" or "System Component," the malware ensures that its actions are performed in a context where security tools might be less likely to trigger alerts.
*   **Anti-Analysis & Robustness:**
    *   The code includes `IsDebuggerPresent` checks and extensive error handling (`fcn.14000eca4`). The inclusion of robust error-handling routines ensures that the malware remains stable even if it encounters unexpected system states, making it more "reliable" in a production infection environment.

---

### Notable Techniques and Patterns

*   **Living off the Land (LotL):**
    *   The code heavily utilizes `advapi32.dll` and `kernel32.dll` for advanced tasks like **Semaphore management** (`CreateSemaphoreExW`) and **Security Descriptor manipulation**. This avoids using "noisy" third-party libraries that might be flagged by signature-based scanners.
*   **Payload Hiding & Staging:**
    *   The use of `.dat` extensions in construction (seen in `fcn.140009308`) suggests the malware hides its secondary payloads under generic filenames until they are ready to be executed via a "launcher" script or a hijacked system component.
*   **Obfuscated Execution Paths:**
    *   The presence of complex internal string building (`fcn.14000ff80`) and manual memory copying indicates the binary builds its commands at runtime, making it harder for static analysis tools to identify hardcoded malicious URLs or file paths.

---

### Summary of Indicator Logic (IOC) Potential
*   **File System:** Watch for the creation/deletion of folders in `%TEMP%` or `%APPDATA%` involving "Installer" keywords. Look for files with `.dat` extensions being renamed to `.dll` or `.exe`.
*   **Registry:** Monitor for modifications to `Software\Microsoft\Windows\CurrentVersion\RunOnce` and the creation/modification of keys related to `AppID` or `CLSID`.
*   **Behavioral:** Alert on any process (especially those mimicking "Installer" components) attempting to modify **System Access Control Lists (SACL)** or performing recursive deletions in temporary directories.
*   **Process Interaction:** Identify calls that utilize `IEAdvpack.dll` or other system-related DLLs to execute commands via `rundll32.exe`.

### Conclusion
The binary is a sophisticated, multi-stage component of a malware infection chain. It is designed for **longevity and stealth**. Instead of being a "noisy" and immediate threat, it focuses on establishing a persistent and authorized foothold within the OS by masquerading as a legitimate system installer while actively cleaning up its tracks through automated folder purging and permission manipulation.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have mapped the observed behaviors from your report to the relevant MITRE ATT&CK techniques and sub-techniques below:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1547.001** | Registry Run Keys / Startup Folder | The malware utilizes `RunOnce` keys to ensure persistence by executing itself or its components upon system restart. |
| **T1036** | Masquerading | The binary masquerades as a "System Component" via COM/AppID hijacking and uses `.dat` extensions to blend in with legitimate processes. |
| **T1562** | Impair Defenses | Manipulation of Security Descriptors and SACLs is used to modify file permissions, potentially allowing the malware to bypass security software or gain elevated rights. |
| **T1070** | Indicator Removal on Host | The implementation of recursive directory removal is specifically intended to "mop up" evidence, such as logs and staging files, after a successful infection. |
| **T1027** | Obfuscated Files (Execution Path) | The use of complex internal string construction at runtime hides hardcoded malicious URLs and file paths from static analysis tools. |
| **T1218** | System Binary Proxy Execution | The utilization of `rundll32.exe` to execute commands via system-trusted DLLs like `IEAdvpack.dll` helps the malware bypass detection by hiding within legitimate processes. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   *(None identified in the provided text)*

**File paths / Registry keys**
*   **Registry Key:** `Software\Microsoft\Windows\CurrentVersion\RunOnce` (Used for persistence)
*   **Registry Keys:** `CLSID` and `AppID` (Targeted for hijacking and masquerading as system components)
*   **File Patterns:** Files ending in `.dat` (Used for staging payloads before renaming to `.exe` or `.dll`)
*   **Directory Activity:** Recursive deletions/creations within `%TEMP%` and `%APPDATA%` directories.

**Mutex names / Named pipes**
*   *(None explicitly named, though the use of "Semaphores" via `CreateSemaphoreExW` was noted as a technique)*

**Hashes**
*   *(None provided in the text)*

**Other artifacts**
*   **System Manipulation:** Modification of **Security Descriptors** and **SACLs (System Access Control Lists)** to alter file/folder permissions.
*   **Masquerading Tactics:** Use of `IEAdvpack.dll` and "Installer" related keywords to blend with legitimate Internet Explorer components.
*   **File System Operations:** Usage of `GetFinalPathNameByHandleW` and `CopyFileW` for moving/renaming staged payloads.
*   **Execution Path:** Execution via `rundll32.exe` calling modules like `advapi32.dll` and `kernel32.dll`.
*   **Cleanup Behavior:** Automated recursive directory removal to delete evidence of staging files or installer logs.

---

## Malware Family Classification

Based on the analysis provided, here is the classification:

1. **Malware family:** Unknown (The report describes sophisticated behavior but does not link it to a specific known threat actor or campaign name like Emotet or Cobalt Strike.)
2. **Malware type:** Dropper / Loader
3. **Confidence:** High
4. **Key evidence:** 
    *   **Advanced Evasion & Masquerading:** The sample uses sophisticated techniques to blend into the OS, such as hijacking `CLSID/AppID` values, utilizing system-trusted DLLs (`IEAdvpack.dll`), and employing `.dat` extensions to hide secondary payloads from basic scanners.
    *   **Environment Preparation & Privilege Manipulation:** The use of Security Descriptor and SACL manipulation indicates a high level of sophistication intended to grant the malware elevated permissions while "unlocking" files for further infection stages.
    *   **Persistence & Cleanup Tactics:** It establishes persistence through `RunOnce` registry keys and implements recursive directory deletion to "mop up" evidence of its staging process, specifically designed to hinder forensic analysis.
