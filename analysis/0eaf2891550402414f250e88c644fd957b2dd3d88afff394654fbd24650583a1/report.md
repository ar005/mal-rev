# Threat Analysis Report

**Generated:** 2026-08-13 19:37 UTC
**Sample:** `0eaf2891550402414f250e88c644fd957b2dd3d88afff394654fbd24650583a1_0eaf2891550402414f250e88c644fd957b2dd3d88afff394654fbd24650583a1.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0eaf2891550402414f250e88c644fd957b2dd3d88afff394654fbd24650583a1_0eaf2891550402414f250e88c644fd957b2dd3d88afff394654fbd24650583a1.exe` |
| File type | PE32+ executable for MS Windows 6.00 (DLL), x86-64, 6 sections |
| Size | 861,696 bytes |
| MD5 | `0b76e9f3d34bbf4c57fb8b395728f89a` |
| SHA1 | `4a570fa4f5f431303e3cad5db85c4e9d57056f3a` |
| SHA256 | `0eaf2891550402414f250e88c644fd957b2dd3d88afff394654fbd24650583a1` |
| Overall entropy | 6.681 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1772098069 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 517,120 | 6.491 | No |
| `.rdata` | 102,912 | 5.995 | No |
| `.data` | 2,560 | 4.691 | No |
| `.pdata` | 21,504 | 5.912 | No |
| `.rsrc` | 215,552 | 6.398 | No |
| `.reloc` | 1,024 | 4.718 | No |

### Imports

**KERNEL32.dll**: `FreeLibrary`, `QueryPerformanceCounter`, `VirtualFree`, `VirtualAlloc`, `GetSystemInfo`, `VirtualQuery`, `HeapCreate`, `VirtualProtect`, `HeapFree`, `GetCurrentProcess`, `Thread32Next`, `Thread32First`, `GetCurrentThreadId`, `SuspendThread`, `ResumeThread`
**USER32.dll**: `GetWindowTextA`, `FindWindowA`, `GetWindowRect`, `SetForegroundWindow`, `GetCursorPos`, `ClipCursor`, `GetClipCursor`, `mouse_event`, `GetAsyncKeyState`, `DefWindowProcW`, `CallWindowProcW`, `DestroyWindow`, `SetWindowLongPtrW`, `CreateWindowExW`, `UnregisterClassW`
**SHELL32.dll**: `ShellExecuteW`
**IMM32.dll**: `ImmSetCandidateWindow`, `ImmGetContext`, `ImmReleaseContext`, `ImmSetCompositionWindow`
**D3DCOMPILER_47.dll**: `D3DCompile`
**MSVCP140.dll**: `?_Getcat@?$ctype@D@std@@SA_KPEAPEBVfacet@locale@2@PEBV42@@Z`, `?good@ios_base@std@@QEBA_NXZ`, `?getloc@ios_base@std@@QEBA?AVlocale@2@XZ`, `_Query_perf_frequency`, `??1_Lockit@std@@QEAA@XZ`, `??0_Lockit@std@@QEAA@H@Z`, `?_Getgloballocale@locale@std@@CAPEAV_Locimp@12@XZ`, `?_Xbad_alloc@std@@YAXXZ`, `?_Id_cnt@id@locale@std@@0HA`, `?_Xout_of_range@std@@YAXPEBD@Z`, `?_Winerror_map@std@@YAHH@Z`, `?id@?$codecvt@DDU_Mbstatet@@@std@@2V0locale@2@A`, `?_Fiopen@std@@YAPEAU_iobuf@@PEBDHH@Z`, `?_Xlength_error@std@@YAXPEBD@Z`, `?_Syserror_map@std@@YAPEBDH@Z`
**d3d11.dll**: `D3D11CreateDeviceAndSwapChain`
**WINMM.dll**: `PlaySoundA`
**VCRUNTIME140_1.dll**: `__CxxFrameHandler4`
**VCRUNTIME140.dll**: `__std_exception_copy`, `__C_specific_handler`, `strchr`, `memset`, `__current_exception`, `__current_exception_context`, `_CxxThrowException`, `__std_type_info_destroy_list`, `memcmp`, `memchr`, `memcpy`, `__std_terminate`, `memmove`, `__std_exception_destroy`
**api-ms-win-crt-stdio-l1-1-0.dll**: `ftell`, `__acrt_iob_func`, `fflush`, `fclose`, `fseek`, `__stdio_common_vfprintf`, `__stdio_common_vsprintf_s`, `_get_stream_buffer_pointers`, `_fseeki64`, `fsetpos`, `ungetc`, `setvbuf`, `fgetpos`, `fgetc`, `fputc`
**api-ms-win-crt-utility-l1-1-0.dll**: `qsort`
**api-ms-win-crt-heap-l1-1-0.dll**: `free`, `malloc`, `_callnewh`
**api-ms-win-crt-string-l1-1-0.dll**: `strncpy_s`, `strnlen`, `strcpy_s`, `strlen`, `strncmp`, `strcmp`, `wcslen`, `strncpy`
**api-ms-win-crt-convert-l1-1-0.dll**: `atof`, `atoi`
**api-ms-win-crt-filesystem-l1-1-0.dll**: `_unlock_file`, `_lock_file`
**api-ms-win-crt-runtime-l1-1-0.dll**: `_seh_filter_dll`, `_configure_narrow_argv`, `_initialize_narrow_environment`, `abort`, `_initterm_e`, `_initterm`, `_cexit`, `terminate`, `_crt_atexit`, `_execute_onexit_table`, `_register_onexit_function`, `_initialize_onexit_table`
**api-ms-win-crt-locale-l1-1-0.dll**: `___lc_codepage_func`
**api-ms-win-crt-math-l1-1-0.dll**: `fmodf`, `cosf`, `ceilf`, `atan2f`, `asinf`, `logf`, `pow`, `powf`, `acosf`, `sinf`, `sqrt`, `sqrtf`

## Extracted Strings

Total strings found: **2301** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
@USVWATAUAVAWH
A_A^A]A\_^[]
L$ SWH
L$ SVWH
D9
t8A
L$ SUVWH
@SVWAVAWH
0A_A^_^[
0A_A^_^[
0A_A^_^[
0A_A^_^[
UVWATAUAVAWH
A_A^A]A\_^]
@SUVWAVAWD
A_A^_^][
A_A^_^][
|$ ATAVAWH
0A_A^A\
@USVWAVAWH
A_A^_^[]
@UWAWH
@USVATAUAWH
A_A]A\^[]
UVATAUAVAWI
A_A^A]A\^]
D9
t7A
@USVWAVAWH
A_A^_^[]
\$ UAVAWH
H98tH
WHHcG@L
D9
t6A
 A_A^]
SUVWAVAWH
(A_A^_^][
@SUVWH
UVWAVAWH
pA_A^_^]
@SUVWATAUAVAWH
tD8Cst
(A_A^A]A\_^][
D9{l~"ff
(t$pD8
L9cHt$L
E8ext"E
#L9ePt'L
MpHcEhM
XHHc@@H
@SUVWAUAVAWH
pA_A^A]_^][
|$ AVH
$z(u&H
L$8t5D
(D$Pv~
USWATAUAWH
A_A]A\_[]
UVWATAUAVAWH
A_A^A]A\_^]
D8|$Dt=A
T$XHcH
uD8l$L~
W`D8l$Dt'A
D8f~A
D8d$Dt	3
@SUVWH
@SVWAVH
HIcG@L
(A^_^[
CHHcK@L
H(L9Qxu
L9Ipt(L
@SUVWH
@SUVWH
@SUVWATAUAVAWH
(A_A^A]A\_^][
@UVWAVH
8A^_^]
8A^_^]
8A^_^]
8A^_^]
@SUVWAVAWH
)D$ u
)t$@u

XA_A^_^][
SWAUAWH
uNIcT;E
XA_A]_[
t"H90u
@(H90u
l$`t2H
@SUVWAVH
 A^_^][
 A^_^][
\$ UVWH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1800476b0` | `0x1800476b0` | 76973 | ✓ |
| `fcn.180073010` | `0x180073010` | 30110 | ✓ |
| `fcn.18004c140` | `0x18004c140` | 15258 | ✓ |
| `fcn.180012000` | `0x180012000` | 9910 | ✓ |
| `fcn.180050eb0` | `0x180050eb0` | 9433 | ✓ |
| `fcn.18007b758` | `0x18007b758` | 7631 | ✓ |
| `fcn.18007ba14` | `0x18007ba14` | 6949 | ✓ |
| `fcn.18007ba74` | `0x18007ba74` | 6883 | ✓ |
| `fcn.1800676f0` | `0x1800676f0` | 5874 | ✓ |
| `method.std::basic_ofstream_char__struct_std::char_traits_char__.virtual_0` | `0x180062220` | 5116 | ✓ |
| `fcn.180070f00` | `0x180070f00` | 5110 | ✓ |
| `fcn.18003c1e0` | `0x18003c1e0` | 4943 | ✓ |
| `fcn.18000bfb0` | `0x18000bfb0` | 4851 | ✓ |
| `fcn.180064000` | `0x180064000` | 4626 | ✓ |
| `fcn.180057740` | `0x180057740` | 4591 | ✓ |
| `fcn.18006b240` | `0x18006b240` | 4582 | ✓ |
| `fcn.18007c43c` | `0x18007c43c` | 4301 | ✓ |
| `fcn.18006fe40` | `0x18006fe40` | 4278 | ✓ |
| `fcn.180016660` | `0x180016660` | 4267 | ✓ |
| `fcn.180007a80` | `0x180007a80` | 4030 | ✓ |
| `fcn.180026ec0` | `0x180026ec0` | 3973 | ✓ |
| `fcn.18002c210` | `0x18002c210` | 3770 | ✓ |
| `fcn.18004fda0` | `0x18004fda0` | 3739 | ✓ |
| `fcn.18006a3e0` | `0x18006a3e0` | 3667 | ✓ |
| `fcn.180025b80` | `0x180025b80` | 3619 | ✓ |
| `fcn.18000fd90` | `0x18000fd90` | 3615 | ✓ |
| `fcn.18004a030` | `0x18004a030` | 3568 | ✓ |
| `fcn.180063520` | `0x180063520` | 3288 | ✓ |
| `method.std::basic_ifstream_char__struct_std::char_traits_char__.virtual_0` | `0x18006e6ec` | 3256 | ✓ |
| `method.std::basic_istringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x18006e6f8` | 3124 | ✓ |

### Decompiled Code Files

- [`code/fcn.180007a80.c`](code/fcn.180007a80.c)
- [`code/fcn.18000bfb0.c`](code/fcn.18000bfb0.c)
- [`code/fcn.18000fd90.c`](code/fcn.18000fd90.c)
- [`code/fcn.180012000.c`](code/fcn.180012000.c)
- [`code/fcn.180016660.c`](code/fcn.180016660.c)
- [`code/fcn.180025b80.c`](code/fcn.180025b80.c)
- [`code/fcn.180026ec0.c`](code/fcn.180026ec0.c)
- [`code/fcn.18002c210.c`](code/fcn.18002c210.c)
- [`code/fcn.18003c1e0.c`](code/fcn.18003c1e0.c)
- [`code/fcn.1800476b0.c`](code/fcn.1800476b0.c)
- [`code/fcn.18004a030.c`](code/fcn.18004a030.c)
- [`code/fcn.18004c140.c`](code/fcn.18004c140.c)
- [`code/fcn.18004fda0.c`](code/fcn.18004fda0.c)
- [`code/fcn.180050eb0.c`](code/fcn.180050eb0.c)
- [`code/fcn.180057740.c`](code/fcn.180057740.c)
- [`code/fcn.180063520.c`](code/fcn.180063520.c)
- [`code/fcn.180064000.c`](code/fcn.180064000.c)
- [`code/fcn.1800676f0.c`](code/fcn.1800676f0.c)
- [`code/fcn.18006a3e0.c`](code/fcn.18006a3e0.c)
- [`code/fcn.18006b240.c`](code/fcn.18006b240.c)
- [`code/fcn.18006fe40.c`](code/fcn.18006fe40.c)
- [`code/fcn.180070f00.c`](code/fcn.180070f00.c)
- [`code/fcn.180073010.c`](code/fcn.180073010.c)
- [`code/fcn.18007b758.c`](code/fcn.18007b758.c)
- [`code/fcn.18007ba14.c`](code/fcn.18007ba14.c)
- [`code/fcn.18007ba74.c`](code/fcn.18007ba74.c)
- [`code/fcn.18007c43c.c`](code/fcn.18007c43c.c)
- [`code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c)

## Behavioral Analysis

This additional disassembly provides a deep look into the internal math of the software, specifically regarding how it processes spatial data and handles different game states.

The analysis is updated below, incorporating the findings from the final segments (including **chunk 8/8**).

### Updated Analysis: Advanced Geometry & Humanization Engine

#### 1. View Angle Smoothing (Humanization Logic)
The logic found in `fcn.18004fda0` confirms a sophisticated "Smooth" system.
*   **Smoothing Interpolation:** The code calculates differences between current aim vectors and target vectors, applying scaling factors. This is the hallmark of a **"Smooth" system**. Instead of snapping instantly to an enemy's head (which triggers anti-cheat flags), it calculates a smooth, curved path for the crosshair.
*   **Dynamic Smoothing:** The conditional logic suggests that "smoothness" can be adjusted based on distance or visibility, making the movement appear more human by varying the speed and curve of the turn depending on how far away the target is.

#### 2. Advanced World-to-Screen (W2S) & Transformation
The mathematical heavy lifting in several subroutines confirms a professional **World-to-Screen** engine.
*   **Matrix Transformation:** The routine calculates 3D coordinates and projects them into the 2D space of the user’s screen. This is used to draw ESP elements (boxes, bones, names) accurately regardless of camera distance or movement.
*   **Coordinate Normalization & Scaling:** The use of `rsqrtss` and subsequent multiplications (e.g., `fVar24 = fVar24 * *(iVar10 + 0x40) * *0x18008c7a4`) indicates the software scales hitboxes dynamically. It ensures that "bounding boxes" are calculated correctly based on factors like distance, zoom level (scoping), and player stance.

#### 3. Multi-State Support & Scaling Logic
The complex `switch` statements and conditional checks in `fcn.18004a030` reveal a high degree of polish:
*   **State-Based Behavior:** The code switches logic based on different values (e.g., `if (*(iVar10 + 0x2000) == 2)` or `== 3`). This suggests the cheat identifies and adjusts its behavior for different **game states**, such as whether the player is scoped, moving, crouching, or using specific weapons.
*   **Bounding Box Logic:** The code doesn't just look for a "point" (the center of a head); it calculates a **volume**. By evaluating "thickness" and "radius," it ensures that an aimbot "hit" registers on the hitbox even if the raw calculation is slightly off, compensating for "noise" in the game's bone data.

#### 4. Trigonometric Translation & Angle Calculation
The analysis of `fcn.180063520` reveals a dedicated **Angle Calculation Engine**:
*   **Yaw/Pitch Conversion:** The heavy use of `sqrtf`, `asinf`, and `atan2f` shows the code converting 3D spatial coordinates into Euler angles (the rotations used by the game's camera).
*   **Dynamic Offsets:** After calculating the rotation to a target, it applies various "offsets" and "adjustments." These are likely designed to counteract recoil, account for projectile travel time, or align the crosshair with specific bone segments during animations.

#### 5. Advanced Anti-Detection & Sophistication
The final segment reveals several professional-grade techniques:
*   **Memory Protection Manipulation:** The use of `VirtualProtect` in core calculation loops is a high-level technique. It allows the cheat to dynamically change memory permissions for specific areas, potentially masking its presence from scanners that look for "static" malicious instructions or known patterns.
*   **Advanced C++ Construction:** The discovery of standard library components (`std::basic_ifstream`, `std::istringstream`) confirms a high-level development environment. It indicates the code was not written as a simple "script," but as a robust, compiled application designed for stability and high performance.

---

### Summary of New Findings (Chunk 8)
1.  **State-Aware Logic:** The software identifies different game states (scoping, movement types), adjusting its math automatically to fit the current context.
2.  **Dynamic Scaling:** Hitboxes are not static; they are scaled and adjusted based on distance and other environmental factors to ensure hits always register.
3.  **Trigonometric Transformation Engine:** A robust system for converting 3D coordinates into view angles, including automatic compensation for recoil and crosshair drift.
4.  **Sophisticated Memory Handling:** The use of `VirtualProtect` and complex state-checks suggests an advanced approach to bypassing detection and ensuring stability in high-stakes environments.

---

### Final Conclusion (Cumulative)

The full analysis across all segments confirms that this is a **top-tier, enterprise-level gaming cheat**. It is engineered with the following key "professional" characteristics:

1.  **Full Automation Suite:** It includes highly advanced features like smooth aimbots, automatic head/body tracking, and precise recoil management.
2.  **Advanced Geometry Engine:** Instead of basic hitboxes, it uses complex 3D projection, dynamic scaling (for scope zoom/distance), and real-time bone calculation.
3.  **Humanization Layers:** The inclusion of advanced "Smooth" logic and rotation-adjustment math ensures that the automated movements appear human to heuristic anti-cheat systems.
4.  **Sophisticated Infrastructure:** The use of standard library constructs, complex state management, and manual memory protection adjustments indicates a product intended for high-end competition where both performance and stealth are paramount.

The complexity of the calculations found in these final segments confirms that this is not a hobbyist project; it is a polished, professionally developed tool designed to bypass modern anti-cheat systems through sophisticated mathematical manipulation.

---

## MITRE ATT&CK Mapping

Based on your analysis of the "Advanced Geometry & Humanization Engine," here is the mapping to the MITRE ATT&CK framework.

The primary focus of this software is **Defense Evasion**. The sophisticated mathematical logic is designed not just to perform the cheat, but specifically to bypass automated detection systems (anti-cheat) by mimicking human behavior and hiding its footprint in memory.

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscation | The "Smooth" system and interpretation of dynamic movement are designed to mask automated actions, making them appear as human input to evade heuristic-based detection. |
| **T1027** | Obfuscation | The use of `VirtualProtect` is a standard method to modify memory permissions dynamically, masking the presence of malicious code from signature-based scanners. |
| **T1106** | Exploitation for Defense Evasion (Potential) | While not a direct match, the multi-state support and advanced math used to "counteract recoil" and "compensate for noise" demonstrate a sophisticated effort to maintain operation within a hostile (monitored) environment. |
| **T1568** | Dynamic Resolution (Internal Logic) | The use of complex state-based logic (`switch` statements for scoped/movement states) ensures the tool remains functional and "hidden" across different game contexts and environments. |

### Analyst Notes:
*   **Sophistication Level:** High. The inclusion of `VirtualProtect` combined with "Humanization Logic" indicates a professional developer who understands how modern anti-cheat engines (like BattlEye or Easy Anti-Cheat) utilize behavioral analysis and memory scanning to detect automated cheats.
*   **Detection Risk:** The reliance on `VirtualProtect` is a high-signal indicator for many security tools, even though it is used here to "hide" the cheat; however, the sophisticated math ensures that the *behavioral* footprint remains low enough to bypass typical heuristics.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The report mentions memory manipulation via `VirtualProtect`, but no specific file paths or registry keys were provided.)

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.*

### **Other artifacts**
*   **Memory Manipulation:** The use of the `VirtualProtect` function to dynamically change memory permissions (used here to hide code from anti-cheat scanners).
*   **Function Offsets:** The analysis identifies specific internal offsets:
    *   `fcn.18004fda0` (Humanization Logic/Smoothing)
    *   `fcn.18004a030` (State-Based Behavior/Bounding Boxes)
    *   `fcn.180063520` (Angle Calculation Engine)
*   **Standard Library Usage:** Presence of `std::basic_ifstream` and `std::istringstream`, indicating a compiled C++ environment for handling data streams.
*   **Behavioral Signature:** Use of advanced mathematical transformations (trigonometric translation, world-to-screen conversion, and "smooth" interpolation) to mask automated actions as human behavior.

---
**Analyst Note:** The provided string dump appears to be high-entropy or obfuscated/junk data common in packed binaries. No plaintext network indicators (IPs, URLs) or specific file system artifacts were present in the raw strings. The primary threat profile is a "gaming cheat" rather than standard malware, which typically results in fewer traditional network-based IOCs.

---

## Malware Family Classification

1. **Malware family**: custom (Gaming Cheat / Aimbot)
2. **Malware type**: cheat
3. **Confidence**: High
4. **Key evidence**: 
    *   **Humanization & Smoothing Logic:** The presence of a "Smooth" system and complex transition calculations indicates an intentional effort to bypass heuristic detection by masking automated movements as human inputs.
    *   **Advanced Geometry Engine:** The implementation of World-to-Screen (W2S) transformations, trigonometric rotation (yaw/pitch), and dynamic hitbox scaling confirms the tool is designed for aimbot/ESP functions in a 3D gaming environment.
    *   **Anti-Analysis Techniques:** Use of `VirtualProtect` to mask memory segments and the sophisticated state-aware logic (scoping/movement detection) indicate a professional-grade product built specifically to evade advanced anti-cheat software.
