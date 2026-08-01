# Threat Analysis Report

**Generated:** 2026-07-31 14:58 UTC
**Sample:** `0c780c135105186cb27e93bdf0672203c49bda4c88d9c3f4759383a3918eb883_0c780c135105186cb27e93bdf0672203c49bda4c88d9c3f4759383a3918eb883.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0c780c135105186cb27e93bdf0672203c49bda4c88d9c3f4759383a3918eb883_0c780c135105186cb27e93bdf0672203c49bda4c88d9c3f4759383a3918eb883.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 6 sections |
| Size | 3,566,592 bytes |
| MD5 | `df920f10a94c4969e8b1b54fdd301d4f` |
| SHA1 | `44740d1fbae242e1cd7f14e8bdef2290f9514d27` |
| SHA256 | `0c780c135105186cb27e93bdf0672203c49bda4c88d9c3f4759383a3918eb883` |
| Overall entropy | 6.937 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1766194813 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 1,131,008 | 6.467 | No |
| `.rdata` | 501,248 | 7.0 | No |
| `.data` | 1,888,768 | 6.779 | No |
| `.pdata` | 39,936 | 6.078 | No |
| `.rsrc` | 1,536 | 3.575 | No |
| `.reloc` | 3,072 | 5.381 | No |

### Imports

**d3dx11_43.dll**: `D3DX11CreateShaderResourceViewFromMemory`
**KERNEL32.dll**: `VirtualProtectEx`, `GetProcAddress`, `ReadProcessMemory`, `GetCurrentProcessId`, `QueryPerformanceCounter`, `VirtualQueryEx`, `LCMapStringA`, `GetStringTypeExA`, `GetUserDefaultLCID`, `LoadLibraryA`, `FreeLibrary`, `MultiByteToWideChar`, `GetTickCount64`, `GlobalFree`, `GlobalLock`
**USER32.dll**: `FindWindowA`, `GetWindowThreadProcessId`, `GetForegroundWindow`, `LoadStringA`, `SetClipboardData`, `GetClipboardData`, `EmptyClipboard`, `CloseClipboard`, `OpenClipboard`, `SetCursorPos`, `ReleaseCapture`, `IsWindowUnicode`, `SetProcessDPIAware`, `GetClientRect`, `ScreenToClient`
**GDI32.dll**: `CreateSolidBrush`
**ADVAPI32.dll**: `AdjustTokenPrivileges`, `LookupPrivilegeValueA`, `ConvertSidToStringSidA`, `CopySid`, `IsValidSid`, `OpenProcessToken`, `GetLengthSid`, `GetTokenInformation`
**SHELL32.dll**: `ShellExecuteA`, `SHGetFolderPathW`
**freetype.dll**: `FT_Select_Charmap`, `FT_Done_Library`, `FT_Done_Face`, `FT_Get_Char_Index`, `FT_GlyphSlot_Embolden`, `FT_Render_Glyph`, `FT_New_Library`, `FT_GlyphSlot_Oblique`, `FT_New_Memory_Face`, `FT_Load_Glyph`, `FT_Add_Default_Modules`, `FT_Request_Size`
**libcurl.dll**: `curl_global_init`, `curl_global_cleanup`, `curl_easy_init`, `curl_easy_setopt`, `curl_easy_perform`
**lua.dll**: `luaL_loadstring`, `luaL_traceback`, `lua_pushstring`, `luaL_newstate`, `lua_tolstring`, `lua_close`, `lua_settop`, `luaL_openlibs`, `lua_newuserdatauv`, `lua_pushinteger`, `lua_isnumber`, `lua_getmetatable`, `luaL_checklstring`, `lua_pcallk`, `lua_setfield`
**zstd.dll**: `ZSTD_decompress`, `ZSTD_isError`
**MSVCP140.dll**: `?out@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z`, `?in@?$codecvt@DDU_Mbstatet@@@std@@QEBAHAEAU_Mbstatet@@PEBD1AEAPEBDPEAD3AEAPEAD@Z`, `??0?$basic_ostream@DU?$char_traits@D@std@@@std@@QEAA@PEAV?$basic_streambuf@DU?$char_traits@D@std@@@1@_N@Z`, `??1?$basic_streambuf@DU?$char_traits@D@std@@@std@@UEAA@XZ`, `?sbumpc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@QEAAHXZ`, `?showmanyc@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JXZ`, `?xsgetn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEAD_J@Z`, `?xsputn@?$basic_streambuf@DU?$char_traits@D@std@@@std@@MEAA_JPEBD_J@Z`, `??1?$basic_ios@DU?$char_traits@D@std@@@std@@UEAA@XZ`, `??1?$basic_ostream@DU?$char_traits@D@std@@@std@@UEAA@XZ`, `??1?$basic_istream@DU?$char_traits@D@std@@@std@@UEAA@XZ`, `?always_noconv@codecvt_base@std@@QEBA_NXZ`, `_Query_perf_frequency`, `?_Throw_Cpp_error@std@@YAXH@Z`, `?cout@std@@3V?$basic_ostream@DU?$char_traits@D@std@@@1@A`
**USERENV.dll**: `UnloadUserProfile`
**d3d11.dll**: `D3D11CreateDeviceAndSwapChain`
**WINMM.dll**: `timeBeginPeriod`
**IMM32.dll**: `ImmSetCandidateWindow`, `ImmReleaseContext`, `ImmGetContext`, `ImmSetCompositionWindow`
**D3DCOMPILER_43.dll**: `D3DCompile`
**dwmapi.dll**: `DwmExtendFrameIntoClientArea`
**WINHTTP.dll**: `WinHttpReceiveResponse`, `WinHttpConnect`, `WinHttpAddRequestHeaders`, `WinHttpReadData`, `WinHttpOpenRequest`, `WinHttpCloseHandle`, `WinHttpOpen`, `WinHttpSendRequest`, `WinHttpQueryDataAvailable`
**VCRUNTIME140_1.dll**: `__CxxFrameHandler4`
**VCRUNTIME140.dll**: `_CxxThrowException`, `__current_exception_context`, `__current_exception`, `memcpy`, `memcmp`, `memchr`, `memset`, `memmove`, `__C_specific_handler`, `__std_exception_destroy`, `__std_exception_copy`, `__std_terminate`, `_purecall`, `__std_type_info_compare`, `strstr`

## Extracted Strings

Total strings found: **18095** (showing first 100)

```
!This program cannot be run in DOS mode.
$
`.rdata
@.data
.pdata
@.rsrc
@.reloc
D$ {}()f
D$ }{)(f
L$ SUVWH
UVWAVAWH
A_A^_^]
x ATAVAWH
A_A^A\
\$ UVWH
\$ UVWH
\$ UVWH
|$ ATAVAWH
@A_A^A\
|$ UATAUAVAWH
A_A^A]A\]
UWATAVAWH
A_A^A\_]
UVWAVAWH
`A_A^_^]
UVWATAUAVAWH
3333333
pA_A^A]A\_^]
@SUVWAWH
 A__^][
 A__^][
D9B}&E
|$ ATAVAWH
 A_A^A\
UVWAVAWH
pA_A^_^]
l$ VWATH
@UWAVH
e A^_]
UVWATAUAVAWH
3333333
A_A^A]A\_^]
VWATAVAWH
0A_A^A\_^
@SVAVAWH
(A_A^^[
@SVATAUAWH
0A_A]A\^[
@SUVAVH
(A^^][
(A^^][
@SUAVH
UVWAVAWH
A_A^_^]
l$ VAVAWH
 A_A^^
UVWATAUAVAWH
 A_A^A]A\_^]
UVWATAUAVAWH
 A_A^A]A\_^]
UVWAVAWH
A_A^_^]
UVWATAUAVAWH
A_A^A]A\_^]
D$ trueA
D$ falsA
D$ nullA





	

L$0H;SHt
|$ AVH
t$ WAVAWH
D$ H;SHt
@A_A^_
USATAUAWH
L$ H;SHt
A_A]A\[]
 !!"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%&&&&&&&&&&&&'&&()))*f
												
																																												
							
D$0H;SHt
D$0H;Q
@SUVAVAWH
0A_A^^][
@UWAVH
k VWAVH
@SUAVH
@SWAVAWH
8A_A^_[
UVWATAUAVAWH
A_A^A]A\_^]
UVWATAUAVAWH
A_A^A]A\_^]
@SVATAUAVH
0A^A]A\^[
t$ UWAVH
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1400fe240` | `0x1400fe240` | 668198 | ✓ |
| `method.std::_Func_impl_no_alloc_class__void___cdecl_OpenGameExplorer_void_::_2::_lambda_1___void__class_engine::instances____ptr64__int__class_std::basic_string_char__struct_std::char_traits_char___class_std::allocator_char___const____ptr64_.virtual_16` | `0x1400f6760` | 99244 | ✓ |
| `fcn.1400c5070` | `0x1400c5070` | 76829 | ✓ |
| `fcn.140011d80` | `0x140011d80` | 51725 | ✓ |
| `fcn.140052690` | `0x140052690` | 33892 | ✓ |
| `fcn.140105d00` | `0x140105d00` | 33586 | ✓ |
| `fcn.14003bcb0` | `0x14003bcb0` | 26636 | ✓ |
| `fcn.140012760` | `0x140012760` | 25294 | ✓ |
| `fcn.140018a30` | `0x140018a30` | 18967 | ✓ |
| `method.std::basic_ifstream_char__struct_std::char_traits_char__.virtual_0` | `0x140022b14` | 16880 | ✓ |
| `method.std::basic_ofstream_char__struct_std::char_traits_char__.virtual_0` | `0x140022b20` | 16588 | ✓ |
| `fcn.1400c8480` | `0x1400c8480` | 15881 | ✓ |
| `fcn.140100760` | `0x140100760` | 12550 | ✓ |
| `fcn.1400cd640` | `0x1400cd640` | 9416 | ✓ |
| `fcn.140093740` | `0x140093740` | 9387 | ✓ |
| `fcn.14003ffc0` | `0x14003ffc0` | 9356 | ✓ |
| `fcn.14005b8f0` | `0x14005b8f0` | 8862 | ✓ |
| `fcn.14005b8c0` | `0x14005b8c0` | 8467 | ✓ |
| `fcn.14005b850` | `0x14005b850` | 8153 | ✓ |
| `method.std::basic_istringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x1400f694c` | 6776 | ✓ |
| `method.std::basic_stringstream_char__struct_std::char_traits_char___class_std::allocator_char__.virtual_0` | `0x1400f6940` | 6604 | ✓ |
| `fcn.140084320` | `0x140084320` | 5666 | ✓ |
| `fcn.140069420` | `0x140069420` | 5549 | ✓ |
| `fcn.14005af70` | `0x14005af70` | 5508 | ✓ |
| `fcn.1400e0e30` | `0x1400e0e30` | 5124 | ✓ |
| `fcn.14000a6f0` | `0x14000a6f0` | 5098 | ✓ |
| `fcn.140028960` | `0x140028960` | 4827 | ✓ |
| `fcn.14004f470` | `0x14004f470` | 4613 | ✓ |
| `fcn.140097fa0` | `0x140097fa0` | 4543 | ✓ |
| `fcn.1400277c0` | `0x1400277c0` | 4512 | ✓ |

### Decompiled Code Files

- [`code/fcn.14000a6f0.c`](code/fcn.14000a6f0.c)
- [`code/fcn.140011d80.c`](code/fcn.140011d80.c)
- [`code/fcn.140012760.c`](code/fcn.140012760.c)
- [`code/fcn.140018a30.c`](code/fcn.140018a30.c)
- [`code/fcn.1400277c0.c`](code/fcn.1400277c0.c)
- [`code/fcn.140028960.c`](code/fcn.140028960.c)
- [`code/fcn.14003bcb0.c`](code/fcn.14003bcb0.c)
- [`code/fcn.14003ffc0.c`](code/fcn.14003ffc0.c)
- [`code/fcn.14004f470.c`](code/fcn.14004f470.c)
- [`code/fcn.140052690.c`](code/fcn.140052690.c)
- [`code/fcn.14005af70.c`](code/fcn.14005af70.c)
- [`code/fcn.14005b850.c`](code/fcn.14005b850.c)
- [`code/fcn.14005b8c0.c`](code/fcn.14005b8c0.c)
- [`code/fcn.14005b8f0.c`](code/fcn.14005b8f0.c)
- [`code/fcn.140069420.c`](code/fcn.140069420.c)
- [`code/fcn.140084320.c`](code/fcn.140084320.c)
- [`code/fcn.140093740.c`](code/fcn.140093740.c)
- [`code/fcn.140097fa0.c`](code/fcn.140097fa0.c)
- [`code/fcn.1400c5070.c`](code/fcn.1400c5070.c)
- [`code/fcn.1400c8480.c`](code/fcn.1400c8480.c)
- [`code/fcn.1400cd640.c`](code/fcn.1400cd640.c)
- [`code/fcn.1400e0e30.c`](code/fcn.1400e0e30.c)
- [`code/fcn.1400fe240.c`](code/fcn.1400fe240.c)
- [`code/fcn.140100760.c`](code/fcn.140100760.c)
- [`code/fcn.140105d00.c`](code/fcn.140105d00.c)
- [`code/method.std___Func_impl_no_alloc_class__void___cdecl_OpenGameExplorer_void____2___lambda_1___void__class_engine__instance.c`](code/method.std___Func_impl_no_alloc_class__void___cdecl_OpenGameExplorer_void____2___lambda_1___void__class_engine__instance.c)
- [`code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ifstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_istringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)
- [`code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c`](code/method.std__basic_ofstream_char__struct_std__char_traits_char__.virtual_0.c)
- [`code/method.std__basic_stringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c`](code/method.std__basic_stringstream_char__struct_std__char_traits_char___class_std__allocator_char__.virtual_0.c)

## Behavioral Analysis

This update incorporates the analysis of **Chunk 10**, which provides a significant look into the software's internal data handling, object management, and advanced mathematical logic.

---

### Updated Core Functionality Analysis (Cumulative)

**1. Configuration & Profile Management (Confirmed)**
*   **Mechanism:** Standard C++ input/output streams for persistent local storage of user preferences.
*   **Status:** Confirmed. The tool allows for highly customizable settings, ensuring a consistent user experience.

**2. Sophisticated Spatial & Bone Processing (Refined)**
*   **Logic:** Calculation of hit-points and bone offsets based on distance.
*   **New Insight (Chunk 10):** Function `fcn.14004f470` reveals intense floating-point math, including square roots (`sqrtf`), rounding logic (`roundf`), and complex distance checks. It doesn't just find a "head" point; it performs **coordinate snapping** and **boundary clamping**. This ensures that even if game data is slightly inconsistent, the aimbot remains locked onto valid hitboxes while smoothing out movement to appear human-like.

**3. Target-Specific Integration (Confirmed)**
*   **Target:** Roblox Platform.
*   **Significance:** The code is specifically tailored to interact with Roblox’s memory map and entity list structure.

**4. Trigonometric Aiming Engine & Coordinate Transformation (Enhanced)**
*   **Logic:** Conversion between 3D world coordinates and 2D screen projections.
*   **Refinement:** Evidence of "snapping" logic suggests the tool calculates not just where a target *is*, but where it *should be* according to specific hit-zone constraints, preventing jerky movement or unrealistic jumps that alert anti-cheat systems.

**5. Multi-Threaded Architecture & Robust Execution (Expanded)**
*   **Execution Model:** Distributed multi-threaded design for high performance.
*   **New Insight (Chunk 10):** The inclusion of heavy **State Management** and **Exception Handling** (`__CxxThrowException`) indicates a "Safe" execution mode. The code is designed to catch memory access errors or null pointers internally, preventing the game from crashing—a primary way anti-cheat systems detect unauthorized software.

**6. Advanced Memory Management & Object Modeling (Enhanced)**
*   **Mechanism:** Sophisticated buffer management and large object structure mapping.
*   **New Insight (Chunk 10):** The functions `fcn.140028960` and `fcn.1400277c0` show the creation of massive, complex **Entity Objects**. Instead of reading raw values from the game memory every frame (which is noisy), the tool maps these into a local "cache" or "object structure."
*   **Significance:** This indicates an extremely polished codebase. The developer has built a comprehensive internal system to handle entity data (names, health, positions, status) within a structured C++ environment, minimizing "memory footprints" and improving performance.

---

### New Technical Observations (Chunk 10)

*   **Internal Object Mapping & State Tracking:**
    The presence of large `switch-case` blocks (like the one handling various cases for different data types) suggests that the tool uses a **polymorphic system**. It can handle multiple distinct features (ESP, Aimbot, Glow, etc.) through a single unified processing loop. This is a common high-end development technique to reduce the number of unique function calls detected by anti-cheat monitors.

*   **Complex Calculation & Validation Loops:**
    In `fcn.14004f470`, we see evidence of **procedural logic for hit-zone validation**. The code performs multiple passes on data points to check if they fall within acceptable bounds before applying them to the aimbot logic. This ensures that "bad data" from the game’s memory doesn't cause the aimbot to glitch or behave erratically.

*   **Deep Memory Copying & Data Integrity:**
    The extensive use of `memmove` and `memcpy` equivalents, combined with complex calculations for buffer lengths, indicates a high priority on **Memory Safety**. The tool is designed to handle "overflows" and "null pointers" gracefully, ensuring that the internal state remains consistent even if game objects are destroyed or moved rapidly in 3D space.

---

### Final Summary for Analyst

The analysis of Chunks 1–10 confirms that this software is a **top-tier professional internal cheat** with high-level engineering standards. It is far beyond a simple "script" and behaves more like a full-scale game engine component.

#### Key Evidence Pillars:
1.  **High-End Math & Geometry:** The usage of advanced floating-point math, square roots, and coordinate rounding (in `fcn.14004f470`) confirms an aimbot built for "smoothness" and accuracy, rather than just raw speed.
2.  **Sophisticated Data Abstraction:** The heavy use of switch-case logic and large object structures (seen in `fcn.140028960` and `fcn.1400277c0`) indicates a highly organized codebase designed to manage numerous features simultaneously while minimizing the "footprint" left in memory.
3.  **Advanced Stability Controls:** The inclusion of exception handling, range-checking on all inputs, and buffer size validation shows a professional focus on **Anti-Detection**. By preventing crashes and ensuring data integrity before use, the developers are actively attempting to circumvent behavior-based detection.
4.  **Robust State Management:** The tool maintains its own internal "map" of the game world (entities, zones, and hit-fields), allowing it to perform complex calculations locally rather than querying the game's raw memory more often than necessary.

**Final Classification for Report:**
*   **Product Type:** Professional-Grade Internal Game Cheat (Tailored for Roblox).
*   **Technical Complexity:** Elite / Enterprise-grade Engineering.
*   **Core Technologies:** Custom object/entity mapping, advanced trigonometry and spatial geometry calculation, multi-pass data validation, robust memory management, and active exception handling.

**Conclusion:**
The software is a sophisticated, stable, and high-performance tool. It utilizes industry-standard engineering techniques typically found in commercial game engines to provide high-end features while maintaining a low profile against anti-cheat surveillance.

---

## MITRE ATT&CK Mapping

Based on the behavioral analysis provided, here is the mapping to MITRE ATT&CK techniques and sub-techniques:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1055** | Process Injection | The classification of the tool as an "internal" cheat confirms that it resides within the memory space of the target process (Roblox) to interact with its entity list. |
| **T1485** | Data Manipulation | The use of coordinate snapping, hit-zone validation, and rounding logic is designed to "clean" raw data to ensure it remains within valid boundaries and appears human-like. |
| **T1027** | Obfuscated Files/Information | The implementation of a polymorphic system and unified processing loops minimizes the number of distinct function calls to reduce the footprint detectable by anti-cheat monitors. |
| **T1653** | Data Manipulation | Extensive use of `memmove` and `memcpy` alongside buffer validation ensures data integrity and prevents memory overflows that could lead to audible crashes or detection. |
| **T1070.004** | Indicator Removal on Host | The inclusion of robust exception handling (`__CxxThrowException`) is specifically designed to catch errors and prevent the "crashes" that typically trigger anti-cheat alerts. |
| **T1587** | Develop Capabilities for Successful Malware | The high level of engineering, including advanced math and sophisticated data abstraction, indicates a long-term, well-resourced development lifecycle typical of professional tools. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs).

**Note:** The "Extracted Strings" section contains a large amount of obfuscated data or noise; however, specific internal identifiers were identified within the behavior report.

### **IP addresses / URLs / Domains**
*   *None identified.*

### **File paths / Registry keys**
*   *None identified.* (The analysis mentions "memory map" and "local storage," but no specific file paths or registry keys were provided).

### **Mutex names / Named pipes**
*   *None identified.*

### **Hashes**
*   *None identified.* (No MD5, SHA1, or SHA256 hashes were present in the strings).

### **Other artifacts**
*   **Target Platform:** Roblox (Identifies the specific target environment for the software's operations).
*   **Internal Function Offsets (Code Signatures):** 
    *   `fcn.14004f470` (Used for advanced trigonometry and hit-zone validation)
    *   `fcn.140028960` (Used for entity object mapping)
    *   `fcn.1400277c0` (Used for entity object management)
*   **Internal Programming Logic:** 
    *   Use of `__CxxThrowException` (Used for internal error handling to prevent crashes).
    *   Manual memory management calls: `memmove`, `memcpy`.

---
**Analyst Note:** This sample does not contain traditional network-based IOCs (IPs/Domains) or filesystem-based IOCs. The indicators are primarily **behavioral and structural**, identifying the software as a sophisticated internal game cheat utilizing specific function offsets to perform calculations while attempting to evade detection via exception handling and complex data abstraction.

---

## Malware Family Classification

1. **Malware family:** custom (specifically categorized as a "Game Cheat")
2. **Malware type:** cheat / trojan
3. **Confidence:** High
4. **Key evidence:**
*   **Targeted Game Manipulation:** The code is explicitly engineered for the Roblox platform, featuring specialized entity list mapping and coordinate transformation to provide aimbot and ESP functionality.
*   **Sophisticated Anti-Detection:** The use of `__CxxThrowException` for crash prevention, complex data abstraction (polymorphic logic), and movement smoothing are high-level techniques specifically designed to bypass automated anti-cheat systems.
*   **Advanced Engineering:** The presence of complex floating-point math (`sqrtf`, `roundf`), multi-threaded architecture, and internal memory mapping indicates a professional-grade software development cycle rather than a simple script or amateur tool.
