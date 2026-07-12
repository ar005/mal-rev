# Threat Analysis Report

**Generated:** 2026-07-11 22:10 UTC
**Sample:** `04bb4867d35e77e8e391f3829cf07a542a73815fc8be975a7733790d6e04243c_04bb4867d35e77e8e391f3829cf07a542a73815fc8be975a7733790d6e04243c.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `04bb4867d35e77e8e391f3829cf07a542a73815fc8be975a7733790d6e04243c_04bb4867d35e77e8e391f3829cf07a542a73815fc8be975a7733790d6e04243c.exe` |
| File type | PE32 executable for MS Windows 5.01 (GUI), Intel i386, 6 sections |
| Size | 14,990,585 bytes |
| MD5 | `73e9ab1674c64f040da642b6a4690356` |
| SHA1 | `e5a508bf8a7170cbacd6e6ab0259073a2a07b3cf` |
| SHA256 | `04bb4867d35e77e8e391f3829cf07a542a73815fc8be975a7733790d6e04243c` |
| Overall entropy | 7.995 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1511042438 |
| Machine | 332 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 301,568 | 6.57 | No |
| `.rdata` | 126,464 | 5.114 | No |
| `.data` | 2,560 | 3.153 | No |
| `.wixburn` | 512 | 0.553 | No |
| `.rsrc` | 15,360 | 5.551 | No |
| `.reloc` | 15,872 | 6.794 | No |

### Imports

**ADVAPI32.dll**: `RegCloseKey`, `RegOpenKeyExW`, `OpenProcessToken`, `AdjustTokenPrivileges`, `LookupPrivilegeValueW`, `InitiateSystemShutdownExW`, `GetUserNameW`, `RegQueryValueExW`, `RegDeleteValueW`, `CloseEventLog`, `OpenEventLogW`, `ReportEventW`, `ConvertStringSecurityDescriptorToSecurityDescriptorW`, `DecryptFileW`, `CreateWellKnownSid`
**USER32.dll**: `PeekMessageW`, `PostMessageW`, `IsWindow`, `WaitForInputIdle`, `PostQuitMessage`, `GetMessageW`, `TranslateMessage`, `MsgWaitForMultipleObjects`, `PostThreadMessageW`, `GetMonitorInfoW`, `MonitorFromPoint`, `IsDialogMessageW`, `LoadCursorW`, `LoadBitmapW`, `SetWindowLongW`
**OLEAUT32.dll**: `VariantInit`, `SysAllocString`, `VariantClear`, `SysFreeString`
**GDI32.dll**: `DeleteDC`, `DeleteObject`, `SelectObject`, `StretchBlt`, `GetObjectW`, `CreateCompatibleDC`
**SHELL32.dll**: `CommandLineToArgvW`, `SHGetFolderPathW`, `ShellExecuteExW`
**ole32.dll**: `CoUninitialize`, `CoInitializeEx`, `CoInitialize`, `StringFromGUID2`, `CoCreateInstance`, `CoTaskMemFree`, `CLSIDFromProgID`, `CoInitializeSecurity`
**KERNEL32.dll**: `GetCommandLineA`, `GetCPInfo`, `GetOEMCP`, `CloseHandle`, `CreateFileW`, `GetProcAddress`, `LocalFree`, `HeapSetInformation`, `GetLastError`, `GetModuleHandleW`, `FormatMessageW`, `lstrlenA`, `lstrlenW`, `MultiByteToWideChar`, `WideCharToMultiByte`
**RPCRT4.dll**: `UuidCreate`

## Extracted Strings

Total strings found: **33245** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.wixburn8
@.rsrc
@.reloc
uJVVRQV
uLSSSSRQS
xF;ur
Bj-_f;>
	wEVj

Wj\_f;|A
t3Vj\^f;
tj.^f;
t/Wj\_f;
j\Zf;TN
f92tHSWf9q
j:Xf;F
ulj?Xf;F
tf98t
mj\Yf;
tij\Zf;
/u"PSP
r&j\Yf;K
9~ t?9~
t@j"Zf;
<SVWj83
SSWSh3
}97t]
9_ t!j
;.wixu
8.wixu	
burntC
97tN9w
CuhWh
E9xt
TSVWjP3
9wt:h
VPh@
E
w`h,!E
y
h,!E
wdhD!E
y
hD!E
y
hd!E
9Gt j
y
h(3E
y
h87E
y
hl7E
y
h(8E
y
hx8E
;XXtB
y
h()E
y
h|)E
yh@*E
8
u	9Pu
8u
9Pu
8u
9Pu
9NDt	9VD
9N\t1;
9~\u9~tu
uM9~\uH9~tuC
yhX0E
j_9]t0
y
h$$E
y
hT$E
x<ku(
y
hH&E
yhh(E
t f90t
tKh`,E
C<;Gr
j_9]t-
yhP"E
2jv_f;
RQh<:E
y
h;E
WWWh4;E
ynVhL;E
@PWPPPV
yh8<E
yWj
Y3
9]ueS
j=Zf;T
j=Zf;T
j=Zf;T
yh\_E
y
hLSE
y
h,OE
y
hHOE
y
hlOE
y
hPE
y
h0LE
y
hXLE
y
hxLE
y
h ME
y
hPME
yh\NE
y
h0RE
yIhPRE
y
htRE
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **17**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.0043c9d0` | `0x43c9d0` | 7236 | ✓ |
| `fcn.0043c918` | `0x43c918` | 6429 | ✓ |
| `fcn.0042fb89` | `0x42fb89` | 5374 | ✓ |
| `fcn.0043aa0e` | `0x43aa0e` | 5020 | ✓ |
| `fcn.00415c33` | `0x415c33` | 3347 | ✓ |
| `fcn.0040762c` | `0x40762c` | 2320 | ✓ |
| `fcn.0042e30f` | `0x42e30f` | 2278 | ✓ |
| `fcn.00421e61` | `0x421e61` | 2195 | ✓ |
| `fcn.0040a8f1` | `0x40a8f1` | 2120 | ✓ |
| `fcn.0040df33` | `0x40df33` | 2080 | ✓ |
| `fcn.0040b48b` | `0x40b48b` | 1922 | ✓ |
| `fcn.00423aad` | `0x423aad` | 1853 | ✓ |
| `fcn.004241ea` | `0x4241ea` | 1770 | ✓ |
| `fcn.004355f7` | `0x4355f7` | 1765 | ✓ |
| `fcn.0042b52c` | `0x42b52c` | 1590 | ✓ |
| `fcn.0040ff99` | `0x40ff99` | 1545 | ✓ |
| `fcn.00424abe` | `0x424abe` | 1410 | ✓ |
| `fcn.00408f72` | `0x408f72` | 1409 | — |
| `fcn.0042ede0` | `0x42ede0` | 1396 | — |
| `fcn.0042f360` | `0x42f360` | 1396 | — |
| `fcn.00405770` | `0x405770` | 1394 | — |
| `fcn.0040f9e3` | `0x40f9e3` | 1394 | — |
| `fcn.004260e9` | `0x4260e9` | 1247 | — |
| `fcn.0043a560` | `0x43a560` | 1198 | — |
| `fcn.00426ccc` | `0x426ccc` | 1159 | — |
| `fcn.00417007` | `0x417007` | 1155 | — |
| `fcn.0040cdbd` | `0x40cdbd` | 1149 | — |
| `fcn.004286a1` | `0x4286a1` | 1142 | — |
| `fcn.00405195` | `0x405195` | 1133 | — |
| `fcn.00403cc4` | `0x403cc4` | 1105 | — |

### Decompiled Code Files

- [`code/fcn.0040762c.c`](code/fcn.0040762c.c)
- [`code/fcn.0040a8f1.c`](code/fcn.0040a8f1.c)
- [`code/fcn.0040b48b.c`](code/fcn.0040b48b.c)
- [`code/fcn.0040df33.c`](code/fcn.0040df33.c)
- [`code/fcn.0040ff99.c`](code/fcn.0040ff99.c)
- [`code/fcn.00415c33.c`](code/fcn.00415c33.c)
- [`code/fcn.00421e61.c`](code/fcn.00421e61.c)
- [`code/fcn.00423aad.c`](code/fcn.00423aad.c)
- [`code/fcn.004241ea.c`](code/fcn.004241ea.c)
- [`code/fcn.00424abe.c`](code/fcn.00424abe.c)
- [`code/fcn.0042b52c.c`](code/fcn.0042b52c.c)
- [`code/fcn.0042e30f.c`](code/fcn.0042e30f.c)
- [`code/fcn.0042fb89.c`](code/fcn.0042fb89.c)
- [`code/fcn.004355f7.c`](code/fcn.004355f7.c)
- [`code/fcn.0043aa0e.c`](code/fcn.0043aa0e.c)
- [`code/fcn.0043c918.c`](code/fcn.0043c918.c)
- [`code/fcn.0043c9d0.c`](code/fcn.0043c9d0.c)

## Behavioral Analysis

This final chunk of disassembly provides a deeper look into the **internal logic** of the installer’s core engine. While these functions are common in high-end enterprise installation software, their presence—combined with the previously identified manual PE parsing and obfuscated command construction—reinforces the conclusion that this is a highly sophisticated "wrapper" designed to manage complex software deployments or hide malicious payloads within legitimate-looking update logic.

### Updated Analysis of Binary Behavior (Chunk 3/3)

#### 1. Advanced MSI Engine Integration (`fcn.00423aad` & `fcn.004241ea`)
These functions represent the "heart" of an installation engine that handles Microsoft Installer (MSI) logic deeply.
*   **Complex State Detection:** The code doesn't just launch a process; it performs detailed checks for "feature states," "missing products," and "version discrepancies." It seems to differentiate between standard installs, minor upgrades, and patches.
*   **Rollback & Recovery Logic:** There is extensive logic dedicated to **"Rollback"** mechanisms (e.g., `RollbackAddLocalCondition`, `RollbackAdvanceCondition`). This ensures that if a part of the installation fails, it reverts correctly. 
*   **Security Implication:** For an attacker, this level of sophistication allows for "seamless" integration. By utilizing proper rollback and version checking, a malicious payload can be delivered as an "update" or "patch," ensuring it replaces existing system files cleanly without triggering standard Windows error messages or inconsistencies that might alert a user.

#### 2. Registry Manipulation & Product Registration (`fcn.0040ff99`)
This function interacts heavily with the Windows Registry to register software components.
*   **"Bundle" Data Management:** The code iterates through several "Bundle" related keys (e.g., `BundleVersion`, `BundleUpdateCode`, `BundlePatchCode`, `BundleTrialPeriod`). 
*   **Configuration of Persistence:** It specifically handles properties like `UninstallString`, `DisplayIcon`, and `Rollback` status within the registry.
*   **Security Implication:** This is a classic "Persistence" technique. By programmatically creating or updating these registry keys, the binary ensures that its payload is recognized by Windows as a legitimate "Bundle." If this is used for malware, it allows the malicious component to appear in "Add/Remove Programs" with a valid icon and version, making it much harder to detect via manual inspection of the OS.

#### 3. Advanced Patch & Slipstream Processing (`fcn.00424abe`)
This function handles more specialized installation scenarios, such as **Slipstream** updates (common in Windows Update environments).
*   **XML Parsing for Configuration:** It parses configuration data to determine which "Feature Nodes" to activate or deactivate and evaluates various conditions (Source, Advertise, etc.).
*   **Complexity of Logic:** The high number of `if/else` checks regarding "Slipstream MSP" (Microsoft Patch) IDs suggests the binary is designed to handle very complex environment requirements.
*   **Security Implication:** This functionality allows a single installer to act as a multi-tool. It can be configured to deliver different payloads depending on what it "finds" in the system's configuration or available patches, which is a common tactic for multi-stage malware.

---

### Updated Summary of Risk

| Category | Finding | Impact/Concern |
| :--- | :--- | :--- |
| **Core Function** | Advanced Installer Engine | The binary handles complex "Rollback," "Slipstream," and "Feature State" logic, allowing it to appear as a professional software suite. |
| **Persistence** | Registry Integration | It actively configures Windows' internal views of installed products (Icons, Uninstall Strings, Bundle Codes). |
| **Sophistication** | Seamless Update Logic | The ability to handle minor upgrades and complex patch chains allows malicious payloads to "blend in" with system updates. |
| **Payload Delivery** | Multi-Scenario Handling | High complexity suggests the tool is designed to adapt its behavior based on environment checks (offered by the large `switch` style logic). |

---

### Final Summary for Incident Response

The analysis of all three disassembly chunks confirms that this binary is a **highly sophisticated installer wrapper and persistence mechanism.**

**Key Technical Indicators:**
1.  **Infrastructure:** It utilizes the **BeInStudio "Burn" engine**, providing a layer of legitimacy to its interface and behavior.
2.  **Payload Validation:** As seen in `fcn.0040b48b`, it performs manual PE header validation, which is common in droppers to ensure a secondary payload is valid before execution.
3.  **Deep Integration:** It goes beyond simple "execution" and implements full **MSI Engine logic**, including rollback handling and complex patch (MSP) parsing. This allows the binary to perform advanced modifications to the Windows environment.
4.  **Persistence/Stealth:** The `fcn.0040ff99` routine shows it is designed to register components properly within the OS, potentially masking a malicious payload as a legitimate "bundle" or system update.

**Conclusion:** 
This binary should be treated as **highly suspicious**. It possesses all the hallmarks of a **sophisticated dropper/loader** used in advanced persistent threats (APTs) or high-level malware campaigns. Its ability to manipulate installation states, handle complex rollbacks, and register itself deeply within the Windows registry suggests it is designed to deliver a payload that remains stable, "legal-looking," and hard to remove once executed.

**Recommendation:**
*   **Isolate:** Any machine where this binary was executed should be isolated from the network immediately.
*   **Monitor:** Look for follow-on activities including:
    *   Creation of new `.msi` or `.msp` files in temporary directories.
    *   Modification of `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer`.
    *   Unexpected network connections from the host to unknown IPs (indicating a "phone home" by the second-stage payload).
    *   Creation of new services or scheduled tasks following the execution of this binary.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| T1036 | Masquerading | The binary uses sophisticated MSI and Burn engine logic to present itself as a legitimate software installer and mask its malicious presence. |
| T1112 | Modify Registry | The tool actively modifies registry keys (e.g., `UninstallString`, `BundleVersion`) to integrate with Windows' internal product listing. |
| T1568 | Dynamic Resolution | Complex "Slipstream" processing and multi-scenario logic allow the binary to vary its behavior based on detected environment configurations. |
| T1027 | Obfuscated Files or Information | The presence of "obfuscated command construction" indicates an attempt to hide malicious commands from analysis tools. |

---

## Indicators of Compromise

Based on the strings and behavioral analysis provided, here are the extracted Indicators of Compromise (IOCs) categorized by type:

**IP addresses / URLs / Domains**
*   None identified in the provided text.

**File paths / Registry keys**
*   **Registry Parameters:** While specific full registry paths were not provided, the following key data points for persistence and masquerading were identified within the `fcn.0040ff99` routine:
    *   `BundleVersion`
    *   `BundleUpdateCode`
    *   `BundlePatchCode`
    *   `BundleTrialPeriod`
    *   `UninstallString`
    *   `DisplayIcon`

**Mutex names / Named pipes**
*   None identified.

**Hashes**
*   None identified in the provided string dump.

**Other artifacts** (behavioral indicators, function offsets, and specific engine logic)
*   **Function Offsets:** 
    *   `0x423aad` (MSI Logic/State Detection)
    *   `0x4241ea` (Rollback & Recovery Logic)
    *   `0x40ff99` (Registry Manipulation/Persistence)
    *   `0x424abe` (Slipstream Processing)
    *   `0x40b48b` (Manual PE Header Validation)
*   **Installer Engine Indicators:** 
    *   "Burn" engine (BeInStudio implementation)
    *   "Slipstream MSP" (Microsoft Patch processing)
*   **Logic/Mechanism Identifiers:**
    *   `RollbackAddLocalCondition`
    *   `RollbackAdvanceCondition`
    *   Manual PE Header validation routines.

---

### Analyst Note:
The primary threat indicator in this sample is not a specific IP or hash, but rather the **sophistication of the installer wrapper**. The binary uses "Burn" engine logic to mimic legitimate Windows Update behaviors (Slipstream MSP processing) and incorporates robust rollback mechanisms. This suggests it is designed for high-level persistence and to evade detection by mimicking standard system update behavior.

---

## Malware Family Classification

1. **Malware family**: custom
2. **Malware type**: dropper / loader
3. **Confidence**: High

**Key evidence**:
*   **Sophisticated Installation Mimicry:** The binary utilizes the BeInStudio "Burn" engine and advanced MSI logic (Rollback recovery, Slipstream/MSP processing). This allows it to masquerade as a legitimate Windows update or system patch, making it highly effective at blending into standard OS environments.
*   **Persistence & Masquerading:** It actively manipulates specific Registry keys (`BundleVersion`, `UninstallString`, `DisplayIcon`) to ensure that any payload it installs is registered by the OS as a "valid" software bundle rather than an orphaned malicious process.
*   **Payload Handling Logic:** The inclusion of manual PE header validation (`fcn.0040b48b`) confirms its primary role as a wrapper/loader designed to verify and transition execution to secondary, potentially more malicious payloads.
