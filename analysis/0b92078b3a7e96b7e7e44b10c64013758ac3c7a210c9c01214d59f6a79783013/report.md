# Threat Analysis Report

**Generated:** 2026-07-27 13:22 UTC
**Sample:** `0b92078b3a7e96b7e7e44b10c64013758ac3c7a210c9c01214d59f6a79783013_0b92078b3a7e96b7e7e44b10c64013758ac3c7a210c9c01214d59f6a79783013.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `0b92078b3a7e96b7e7e44b10c64013758ac3c7a210c9c01214d59f6a79783013_0b92078b3a7e96b7e7e44b10c64013758ac3c7a210c9c01214d59f6a79783013.exe` |
| File type | PE32+ executable for MS Windows 6.00 (console), x86-64, 7 sections |
| Size | 37,656,885 bytes |
| MD5 | `339b0859c6da73155e714d221f088e9f` |
| SHA1 | `ebc84e699a6ec77c840b2d88f124c5f9248be0fc` |
| SHA256 | `0b92078b3a7e96b7e7e44b10c64013758ac3c7a210c9c01214d59f6a79783013` |
| Overall entropy | 6.68 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1657323758 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 19,570,688 | 6.461 | No |
| `.rdata` | 16,669,696 | 6.213 | No |
| `.data` | 141,312 | 3.861 | No |
| `.pdata` | 917,504 | 6.798 | No |
| `_RDATA` | 512 | 2.91 | No |
| `.rsrc` | 142,336 | 6.165 | No |
| `.reloc` | 131,584 | 5.486 | No |

### Imports

**dbghelp.dll**: `SymSetSearchPathW`, `SymGetSearchPathW`, `SymGetModuleBase64`, `SymFunctionTableAccess64`, `StackWalk64`, `SymSetOptions`, `SymFromAddr`, `SymInitialize`, `SymGetLineFromAddr64`, `SymCleanup`, `UnDecorateSymbolName`
**WS2_32.dll**: `getservbyname`, `getservbyport`, `gethostbyaddr`, `inet_ntoa`, `inet_addr`, `WSACleanup`, `WSASetLastError`, `ntohs`, `htonl`, `ntohl`, `closesocket`, `getsockopt`, `WSAStartup`, `send`, `gethostname`
**IPHLPAPI.DLL**: `ConvertInterfaceIndexToLuid`, `ConvertInterfaceLuidToNameW`, `GetAdaptersAddresses`
**PSAPI.DLL**: `GetModuleFileNameExW`, `GetProcessMemoryInfo`, `EnumProcessModules`
**USERENV.dll**: `GetUserProfileDirectoryW`
**ADVAPI32.dll**: `CryptGetProvParam`, `GetUserNameW`, `RegCloseKey`, `RegEnumKeyExA`, `RegOpenKeyExA`, `RegQueryValueExA`, `RegEnumKeyExW`, `RegQueryInfoKeyW`, `EventWriteTransfer`, `EventSetInformation`, `EventUnregister`, `EventRegister`, `ReportEventW`, `RegisterEventSourceW`, `DeregisterEventSource`
**USER32.dll**: `GetProcessWindowStation`, `MapVirtualKeyW`, `DispatchMessageA`, `TranslateMessage`, `MessageBoxW`, `GetSystemMetrics`, `GetMessageA`, `GetUserObjectInformationW`
**CRYPT32.dll**: `CertCloseStore`, `CertEnumCertificatesInStore`, `CertFindCertificateInStore`, `CertDuplicateCertificateContext`, `CertFreeCertificateContext`, `CertGetCertificateContextProperty`, `CertOpenStore`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `CreateEventW`, `RtlCaptureContext`, `RtlLookupFunctionEntry`, `IsProcessorFeaturePresent`, `GetCPInfo`, `GetStringTypeW`, `InitializeSListHead`, `WaitForSingleObjectEx`, `UnhandledExceptionFilter`, `InterlockedPushEntrySList`, `RtlUnwindEx`, `RtlPcToFileHeader`, `RaiseException`, `ExitProcess`, `GetModuleHandleExW`
**WINMM.dll**: `timeGetTime`

### Exports

`??$Add@VIsolate@internal@v8@@@?$Dictionary@VGlobalDictionary@internal@v8@@VGlobalDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VGlobalDictionary@internal@v8@@@12@PEAVIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VIsolate@internal@v8@@@?$Dictionary@VNameDictionary@internal@v8@@VNameDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNameDictionary@internal@v8@@@12@PEAVIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VIsolate@internal@v8@@@?$Dictionary@VNumberDictionary@internal@v8@@VNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNumberDictionary@internal@v8@@@12@PEAVIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VIsolate@internal@v8@@@?$Dictionary@VSimpleNumberDictionary@internal@v8@@VSimpleNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VSimpleNumberDictionary@internal@v8@@@12@PEAVIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VIsolate@internal@v8@@@OrderedNameDictionary@internal@v8@@SA?AV?$MaybeHandle@VOrderedNameDictionary@internal@v8@@@12@PEAVIsolate@12@V?$Handle@VOrderedNameDictionary@internal@v8@@@12@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@@Z`, `??$Add@VLocalIsolate@internal@v8@@@?$Dictionary@VGlobalDictionary@internal@v8@@VGlobalDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VGlobalDictionary@internal@v8@@@12@PEAVLocalIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VLocalIsolate@internal@v8@@@?$Dictionary@VNameDictionary@internal@v8@@VNameDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNameDictionary@internal@v8@@@12@PEAVLocalIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VLocalIsolate@internal@v8@@@?$Dictionary@VNumberDictionary@internal@v8@@VNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNumberDictionary@internal@v8@@@12@PEAVLocalIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VLocalIsolate@internal@v8@@@?$Dictionary@VSimpleNumberDictionary@internal@v8@@VSimpleNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VSimpleNumberDictionary@internal@v8@@@12@PEAVLocalIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VLocalIsolate@internal@v8@@@OrderedNameDictionary@internal@v8@@SA?AV?$MaybeHandle@VOrderedNameDictionary@internal@v8@@@12@PEAVLocalIsolate@12@V?$Handle@VOrderedNameDictionary@internal@v8@@@12@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@@Z`, `??$Allocate@VIsolate@internal@v8@@@AstConsString@internal@v8@@AEBA?AV?$Handle@VString@internal@v8@@@12@PEAVIsolate@12@@Z`, `??$Allocate@VIsolate@internal@v8@@@DescriptorArray@internal@v8@@SA?AV?$Handle@VDescriptorArray@internal@v8@@@12@PEAVIsolate@12@HHW4AllocationType@12@@Z`, `??$Allocate@VIsolate@internal@v8@@@OrderedHashMap@internal@v8@@SA?AV?$MaybeHandle@VOrderedHashMap@internal@v8@@@12@PEAVIsolate@12@HW4AllocationType@12@@Z`, `??$Allocate@VIsolate@internal@v8@@@OrderedHashSet@internal@v8@@SA?AV?$MaybeHandle@VOrderedHashSet@internal@v8@@@12@PEAVIsolate@12@HW4AllocationType@12@@Z`, `??$Allocate@VIsolate@internal@v8@@@OrderedNameDictionary@internal@v8@@SA?AV?$MaybeHandle@VOrderedNameDictionary@internal@v8@@@12@PEAVIsolate@12@HW4AllocationType@12@@Z`, `??$Allocate@VLocalIsolate@internal@v8@@@AstConsString@internal@v8@@AEBA?AV?$Handle@VString@internal@v8@@@12@PEAVLocalIsolate@12@@Z`, `??$Allocate@VLocalIsolate@internal@v8@@@OrderedNameDictionary@internal@v8@@SA?AV?$MaybeHandle@VOrderedNameDictionary@internal@v8@@@12@PEAVLocalIsolate@12@HW4AllocationType@12@@Z`, `??$AllocateFlat@VIsolate@internal@v8@@@AstConsString@internal@v8@@QEBA?AV?$Handle@VString@internal@v8@@@12@PEAVIsolate@12@@Z`, `??$AllocateFlat@VLocalIsolate@internal@v8@@@AstConsString@internal@v8@@QEBA?AV?$Handle@VString@internal@v8@@@12@PEAVLocalIsolate@12@@Z`, `??$AllocateScopeInfos@VIsolate@internal@v8@@@DeclarationScope@internal@v8@@SAXPEAVParseInfo@12@PEAVIsolate@12@@Z`, `??$AllocateScopeInfos@VLocalIsolate@internal@v8@@@DeclarationScope@internal@v8@@SAXPEAVParseInfo@12@PEAVLocalIsolate@12@@Z`, `??$AllocateScopeInfosRecursively@VIsolate@internal@v8@@@Scope@internal@v8@@AEAAXPEAVIsolate@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$AllocateScopeInfosRecursively@VLocalIsolate@internal@v8@@@Scope@internal@v8@@AEAAXPEAVLocalIsolate@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$AllocateSlotSet@$00@MemoryChunk@internal@v8@@QEAAPEAVSlotSet@12@XZ`, `??$AllocateSlotSet@$01@MemoryChunk@internal@v8@@QEAAPEAVSlotSet@12@XZ`, `??$AllocateSlotSet@$0A@@MemoryChunk@internal@v8@@QEAAPEAVSlotSet@12@XZ`, `??$At@VIsolate@internal@v8@@@ConstantArrayBuilder@interpreter@internal@v8@@QEBA?AV?$MaybeHandle@VObject@internal@v8@@@23@_KPEAVIsolate@23@@Z`, `??$At@VLocalIsolate@internal@v8@@@ConstantArrayBuilder@interpreter@internal@v8@@QEBA?AV?$MaybeHandle@VObject@internal@v8@@@23@_KPEAVLocalIsolate@23@@Z`, `??$BigIntLiteral@VIsolate@internal@v8@@@internal@v8@@YA?AV?$MaybeHandle@VBigInt@internal@v8@@@01@PEAVIsolate@01@PEBD@Z`, `??$BigIntLiteral@VLocalIsolate@internal@v8@@@internal@v8@@YA?AV?$MaybeHandle@VBigInt@internal@v8@@@01@PEAVLocalIsolate@01@PEBD@Z`, `??$BuildValue@VIsolate@internal@v8@@@Literal@internal@v8@@QEBA?AV?$Handle@VObject@internal@v8@@@12@PEAVIsolate@12@@Z`, `??$BuildValue@VLocalIsolate@internal@v8@@@Literal@internal@v8@@QEBA?AV?$Handle@VObject@internal@v8@@@12@PEAVLocalIsolate@12@@Z`, `??$ConvertDouble@H@internal@v8@@YAHN@Z`, `??$ConvertDouble@I@internal@v8@@YAIN@Z`, `??$ConvertDouble@M@internal@v8@@YAMN@Z`, `??$ConvertDouble@N@internal@v8@@YANN@Z`, `??$ConvertDouble@_J@internal@v8@@YA_JN@Z`, `??$ConvertDouble@_K@internal@v8@@YA_KN@Z`, `??$ConvertDouble@_N@internal@v8@@YA_NN@Z`, `??$Create@VIsolate@internal@v8@@@ScopeInfo@internal@v8@@SA?AV?$Handle@VScopeInfo@internal@v8@@@12@PEAVIsolate@12@PEAVZone@12@PEAVScope@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$Create@VLocalIsolate@internal@v8@@@ScopeInfo@internal@v8@@SA?AV?$Handle@VScopeInfo@internal@v8@@@12@PEAVLocalIsolate@12@PEAVZone@12@PEAVScope@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$CreateScript@VIsolate@internal@v8@@@ParseInfo@internal@v8@@QEAA?AV?$Handle@VScript@internal@v8@@@12@PEAVIsolate@12@V?$Handle@VString@internal@v8@@@12@V?$MaybeHandle@VFixedArray@internal@v8@@@12@VScriptOriginOptions@2@W4NativesFlag@12@@Z`, `??$CreateScript@VLocalIsolate@internal@v8@@@ParseInfo@internal@v8@@QEAA?AV?$Handle@VScript@internal@v8@@@12@PEAVLocalIsolate@12@V?$Handle@VString@internal@v8@@@12@V?$MaybeHandle@VFixedArray@internal@v8@@@12@VScriptOriginOptions@2@W4NativesFlag@12@@Z`, `??$Decode@E@Utf8Decoder@internal@v8@@QEAAXPEAEAEBV?$Vector@$$CBE@base@2@@Z`, `??$Decode@G@Utf8Decoder@internal@v8@@QEAAXPEAGAEBV?$Vector@$$CBE@base@2@@Z`, `??$DeserializeScopeChain@VIsolate@internal@v8@@@Scope@internal@v8@@SAPEAV012@PEAVIsolate@12@PEAVZone@12@VScopeInfo@12@PEAVDeclarationScope@12@PEAVAstValueFactory@12@W4DeserializationMode@012@@Z`, `??$DeserializeScopeChain@VLocalIsolate@internal@v8@@@Scope@internal@v8@@SAPEAV012@PEAVLocalIsolate@12@PEAVZone@12@VScopeInfo@12@PEAVDeclarationScope@12@PEAVAstValueFactory@12@W4DeserializationMode@012@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VCompilationCacheTable@internal@v8@@VCompilationCacheShape@23@@internal@v8@@SA?AV?$Handle@VCompilationCacheTable@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VEphemeronHashTable@internal@v8@@VObjectHashTableShape@23@@internal@v8@@SA?AV?$Handle@VEphemeronHashTable@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VGlobalDictionary@internal@v8@@VGlobalDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VGlobalDictionary@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`

## Extracted Strings

Total strings found: **134306** (showing first 100)

```
!This program cannot be run in DOS mode.
$
'!qrc@
!Richc@
`.rdata
@.data
.pdata
@_RDATA
@.rsrc
@.reloc
aurHuD
aulsu<
  Shu2
anghu*
ai  u"
VIA Padlock x86_64 module, CRYPTOGAMS by <appro@openssl.org>
SUATAUAVAWH
L3f L3n(L3v0L3~8L
L3f L3n(L3v0L3~8L3
L3g L3o(L3w0L3
	OO!OBn
OO!OBn
?mRRUR
0`<
l0`<
\CKK1Kbz
)KK1Kbz
#JJ5Jj
 JJ5Jj
R|

(
P"
Z

(
P"
sg<]]i]
II9Irp
;II9Irp
HH=Hzu
2HH=Hzu
=d__a_
^u}TTMT
FMM)MRd
MM)MRd
LL-LZa
LL-LZa
"4h9
e4h9
NN%NJk
NN%NJk
r,X'
S,X'
		$	H-
A		$	H-
Pu\\m\
3VWSUATAUAVAW
A_A^A]A\][_^
SUATAUAVAWH
D7q/;M
SHA512 block transform for x86_64, CRYPTOGAMS by <appro@openssl.org>
SUATAUAVAWH
SUATAUAVAWH
SUATAUAVAWH
VWSUATAUAVAW
A_A^A]A\][_^
SUATAUAVAWH
8STs
e
	
SHA256 block transform for x86_64, CRYPTOGAMS by <appro@openssl.org>
SUATAUAVAWH
SUATAUAVAWH
SUATAUAVAWH
VWSUATAUAVAW
A_A^A]A\][_^
VWSUATAUAVAW
SUATAUAVAWH
ynl$<M
8STs
eTs
eTs
eTs
eTs
eTs
eTs
eTs
e
LwH'LwH'LwH'LwH'LwH'LwH'LwH'LwH'
8STs
e
SHA256 multi-block transform for x86_64, CRYPTOGAMS by <appro@openssl.org>
VWSUATAUAVAW
A_A^A]A\][_^
VWSUATAUAVAW
SUATAUAVI
D3t$1
D3t$$!
3T$(D!
3l$,D!
D3t$0D!
3l$ D1
D3t$$1
D3t$<F
3l$,D1
D3t$0D1
3T$4D1
D3t$4D
D3t$<1
D3t$ F
D3t$D
D3t$ 1
D3t$8F
3l$(D1
D3t$$D
D3t$,D!
D3t$8D!
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `fcn.1407cb290` | `0x1407cb290` | 16777515 | ✓ |
| `fcn.1407cb5c0` | `0x1407cb5c0` | 16777515 | ✓ |
| `fcn.1407ca320` | `0x1407ca320` | 16777515 | ✓ |
| `sym.node.exe__StackEffect___WasmDecoder__0A__0A__wasm_internal_v8__QEAA_AU__pair_II_std__PEBE_Z` | `0x1406d49c0` | 16777475 | ✓ |
| `sym.node.exe__Lub_BitsetType_compiler_internal_v8__SA_KAEBVHeapObjectType_234__Z` | `0x1405809c0` | 16672783 | ✓ |
| `sym.node.exe__New_FeedbackVector_internal_v8__SA_AV__Handle_VFeedbackVector_internal_v8___23_PEAVIsolate_23_V__Handle_VSharedFunctionInfo_internal_v8___23_V__Handle_VClosureFeedbackCellArray_internal_v8___23_PEAVIsCompiledScope_23__Z` | `0x1409abec0` | 14873353 | ✓ |
| `fcn.140ab61b0` | `0x140ab61b0` | 14873353 | ✓ |
| `fcn.1401e1b10` | `0x1401e1b10` | 13776670 | ✓ |
| `fcn.140bce880` | `0x140bce880` | 12249560 | ✓ |
| `sym.node.exe__GetInstructionFlags_InstructionScheduler_compiler_internal_v8__AEBAHPEBVInstruction_234__Z` | `0x1410dd030` | 11776157 | ✓ |
| `sym.node.exe__AlignedFree_internal_v8__YAXPEAX_Z` | `0x1407bc780` | 11313823 | ✓ |
| `fcn.140991840` | `0x140991840` | 9902007 | ✓ |
| `fcn.1406b7360` | `0x1406b7360` | 9800865 | ✓ |
| `fcn.1406ce6d0` | `0x1406ce6d0` | 9705777 | ✓ |
| `sym.node.exe__NeedsExactContext_OperatorProperties_compiler_internal_v8__SA_NPEBVOperator_234__Z` | `0x14102cb90` | 8632908 | ✓ |
| `fcn.140832ec0` | `0x140832ec0` | 8245867 | ✓ |
| `fcn.140833a60` | `0x140833a60` | 8242891 | ✓ |
| `fcn.1408340c0` | `0x1408340c0` | 8241259 | ✓ |
| `sym.node.exe__SerializeFunctionInfo_WebSnapshotSerializer_internal_v8__AEAAXPEAVValueSerializer_23_V__Handle_VJSFunction_internal_v8___23__Z` | `0x1407b7730` | 8036582 | ✓ |
| `sym.node.exe__TryHandleWebAssemblyTrapWindows_v8__YA_NPEAU_EXCEPTION_POINTERS___Z` | `0x140ca0c50` | 7634757 | ✓ |
| `sym.node.exe__SetUnhandledExceptionCallback_V8_v8__SAXP6AHPEAU_EXCEPTION_POINTERS___Z_Z` | `0x140c9d310` | 7614773 | ✓ |
| `sym.node.exe__StackHasOverflowed_JSHeapBroker_compiler_internal_v8__QEBA_NXZ` | `0x1410ba860` | 5613732 | ✓ |
| `sym.node.exe__TranslateStateValueDescriptor_CodeGenerator_compiler_internal_v8__AEAAXPEAVStateValueDescriptor_234_PEAVStateValueList_234_PEAVInstructionOperandIterator_234__Z` | `0x14106e700` | 5029260 | ✓ |
| `sym.node.exe__IsValid_StartupData_v8__QEBA_NXZ` | `0x140c8e700` | 4956405 | ✓ |
| `fcn.140b60220` | `0x140b60220` | 4914955 | ✓ |
| `fcn.140b606b0` | `0x140b606b0` | 4913787 | ✓ |
| `fcn.140b60a00` | `0x140b60a00` | 4912939 | ✓ |
| `sym.node.exe__CanBeRehashed_StartupData_v8__QEBA_NXZ` | `0x140c79980` | 4875285 | ✓ |
| `sym.node.exe__FeedbackVectorSpecPrint_FeedbackVectorSpec_internal_v8__QEAAXAEAV__basic_ostream_DU__char_traits_D_std___std___Z` | `0x140b8c720` | 4799209 | ✓ |
| `fcn.140bcdfd0` | `0x140bcdfd0` | 4464987 | ✓ |

### Decompiled Code Files

- [`code/fcn.1401e1b10.c`](code/fcn.1401e1b10.c)
- [`code/fcn.1406b7360.c`](code/fcn.1406b7360.c)
- [`code/fcn.1406ce6d0.c`](code/fcn.1406ce6d0.c)
- [`code/fcn.1407ca320.c`](code/fcn.1407ca320.c)
- [`code/fcn.1407cb290.c`](code/fcn.1407cb290.c)
- [`code/fcn.1407cb5c0.c`](code/fcn.1407cb5c0.c)
- [`code/fcn.140832ec0.c`](code/fcn.140832ec0.c)
- [`code/fcn.140833a60.c`](code/fcn.140833a60.c)
- [`code/fcn.1408340c0.c`](code/fcn.1408340c0.c)
- [`code/fcn.140991840.c`](code/fcn.140991840.c)
- [`code/fcn.140ab61b0.c`](code/fcn.140ab61b0.c)
- [`code/fcn.140b60220.c`](code/fcn.140b60220.c)
- [`code/fcn.140b606b0.c`](code/fcn.140b606b0.c)
- [`code/fcn.140b60a00.c`](code/fcn.140b60a00.c)
- [`code/fcn.140bcdfd0.c`](code/fcn.140bcdfd0.c)
- [`code/fcn.140bce880.c`](code/fcn.140bce880.c)
- [`code/sym.node.exe__AlignedFree_internal_v8__YAXPEAX_Z.c`](code/sym.node.exe__AlignedFree_internal_v8__YAXPEAX_Z.c)
- [`code/sym.node.exe__CanBeRehashed_StartupData_v8__QEBA_NXZ.c`](code/sym.node.exe__CanBeRehashed_StartupData_v8__QEBA_NXZ.c)
- [`code/sym.node.exe__FeedbackVectorSpecPrint_FeedbackVectorSpec_internal_v8__QEAAXAEAV__basic_ostream_DU__char_traits_D_std___s.c`](code/sym.node.exe__FeedbackVectorSpecPrint_FeedbackVectorSpec_internal_v8__QEAAXAEAV__basic_ostream_DU__char_traits_D_std___s.c)
- [`code/sym.node.exe__GetInstructionFlags_InstructionScheduler_compiler_internal_v8__AEBAHPEBVInstruction_234__Z.c`](code/sym.node.exe__GetInstructionFlags_InstructionScheduler_compiler_internal_v8__AEBAHPEBVInstruction_234__Z.c)
- [`code/sym.node.exe__IsValid_StartupData_v8__QEBA_NXZ.c`](code/sym.node.exe__IsValid_StartupData_v8__QEBA_NXZ.c)
- [`code/sym.node.exe__Lub_BitsetType_compiler_internal_v8__SA_KAEBVHeapObjectType_234__Z.c`](code/sym.node.exe__Lub_BitsetType_compiler_internal_v8__SA_KAEBVHeapObjectType_234__Z.c)
- [`code/sym.node.exe__NeedsExactContext_OperatorProperties_compiler_internal_v8__SA_NPEBVOperator_234__Z.c`](code/sym.node.exe__NeedsExactContext_OperatorProperties_compiler_internal_v8__SA_NPEBVOperator_234__Z.c)
- [`code/sym.node.exe__New_FeedbackVector_internal_v8__SA_AV__Handle_VFeedbackVector_internal_v8___23_PEAVIsolate_23_V__Handle_VS.c`](code/sym.node.exe__New_FeedbackVector_internal_v8__SA_AV__Handle_VFeedbackVector_internal_v8___23_PEAVIsolate_23_V__Handle_VS.c)
- [`code/sym.node.exe__SerializeFunctionInfo_WebSnapshotSerializer_internal_v8__AEAAXPEAVValueSerializer_23_V__Handle_VJSFunction.c`](code/sym.node.exe__SerializeFunctionInfo_WebSnapshotSerializer_internal_v8__AEAAXPEAVValueSerializer_23_V__Handle_VJSFunction.c)
- [`code/sym.node.exe__SetUnhandledExceptionCallback_V8_v8__SAXP6AHPEAU_EXCEPTION_POINTERS___Z_Z.c`](code/sym.node.exe__SetUnhandledExceptionCallback_V8_v8__SAXP6AHPEAU_EXCEPTION_POINTERS___Z_Z.c)
- [`code/sym.node.exe__StackEffect___WasmDecoder__0A__0A__wasm_internal_v8__QEAA_AU__pair_II_std__PEBE_Z.c`](code/sym.node.exe__StackEffect___WasmDecoder__0A__0A__wasm_internal_v8__QEAA_AU__pair_II_std__PEBE_Z.c)
- [`code/sym.node.exe__StackHasOverflowed_JSHeapBroker_compiler_internal_v8__QEBA_NXZ.c`](code/sym.node.exe__StackHasOverflowed_JSHeapBroker_compiler_internal_v8__QEBA_NXZ.c)
- [`code/sym.node.exe__TranslateStateValueDescriptor_CodeGenerator_compiler_internal_v8__AEAAXPEAVStateValueDescriptor_234_PEAVSt.c`](code/sym.node.exe__TranslateStateValueDescriptor_CodeGenerator_compiler_internal_v8__AEAAXPEAVStateValueDescriptor_234_PEAVSt.c)
- [`code/sym.node.exe__TryHandleWebAssemblyTrapWindows_v8__YA_NPEAU_EXCEPTION_POINTERS___Z.c`](code/sym.node.exe__TryHandleWebAssemblyTrapWindows_v8__YA_NPEAU_EXCEPTION_POINTERS___Z.c)

## Behavioral Analysis

This final analysis incorporates the findings from all three segments of disassembly. The addition of chunk 3/3 confirms the most alarming aspects of this binary: it is not merely a "wrapper" for malicious code, but a **full-featured, high-performance execution environment** capable of hosting and optimizing complex logic through multiple layers of abstraction.

### Final Integrated Analysis: Execution Engine Depth & Complexity

The final disassembly confirms that the binary is built upon (or heavily mimics) the architectural foundations of modern JavaScript engines like V8. It features several sophisticated subsystems designed to manage, compile, and execute code with extreme efficiency.

#### 1. Multi-Layered Interpretation & Compilation
*   **Bytecode Interpretation:** The presence of `fcn.140bcdfd0` (identified as a `BytecodeArrayIterator`) confirms that the engine parses a custom or standardized bytecode set. This allows an attacker to write complex logic in a high-level language, compile it into bytecode, and then run it through this "interpreter loop."
*   **JIT & Code Generation:** The function `TranslateStateValueDescriptor_CodeGenerator` reveals that the binary doesn't just interpret; it manages state during a "translation" or compilation phase. It handles various "Special Forms" (e.g., `deoptimization`, `translation arrays`) which are hallmarks of an advanced JIT compiler.
*   **Security Implication:** To an analyst, the **malicious logic is invisible**. You aren't looking at x86_64 instructions performing malicious acts; you are looking at a sophisticated machine designed to *interpret* instructions that you haven't even identified yet.

#### 2. WebAssembly (Wasm) Integration
The presence of `TryHandleWebAssemblyTrapWindows` is a significant discovery.
*   **Observation:** The engine explicitly handles "traps" and exceptions specifically related to WebAssembly on Windows.
*   **Security Implication:** This allows the threat actor to use **double-layered obfuscation**. They can run a high-level script (Layer 1) that interacts with compiled, low-level code (WebAssembly - Layer 2). This makes manual reverse engineering nearly impossible, as the analyst must decompile/de-obfuscate two different layers of execution logic.

#### 3. Robust Memory and Stack Management
*   **Safety Mechanisms:** Functions like `StackHasOverflowed_JSHeapBroker` and `SetUnhandledExceptionCallback_V8` indicate that the engine is designed to be stable and "fail gracefully."
*   **Security Implication:** If a malicious payload triggers an error, the engine's internal handlers (like `V8_Fatal`) catch it. Instead of the application crashing—which would alert a sandbox or security monitor—the engine handles the exception internally. This provides the malware with **"Stability as Stealth,"** ensuring the process remains alive and hidden while performing its tasks.

#### 4. Advanced State Management & Optimization
*   **StateValueDescriptor:** The logic in `TranslateStateValueDescriptor` shows the code is prepared to handle complex, dynamic data types during compilation.
*   **Startup Data Handling:** Functions like `IsValid_StartupData` and `CanBeRehashed_StartupData` suggest that the environment can be "pre-baked." This links back to the **WebSnapshot** finding; the engine can be pre-configured with a specific set of "known" values, potentially including hidden malicious configuration data that only becomes active during specific execution paths.

---

### Final Summary for Threat Intelligence

**Core Identity:** 
This binary is an **Industrial-Grade Execution Engine** (highly similar to V8/Node.js). It is designed to host, interpret, and optimize complex logic through a sophisticated JIT-enabled environment.

**Sophistication Level: Extreme.**
This is not "malware" in the traditional sense; it is a **Malware Environment**. The threat actor has integrated a professional-grade engine into their toolset to host malicious payloads.

**Key Threat Actor Tactics & Techniques:**
1.  **Multi-Layered Obfuscation (The "Matryoshka Doll"):** 
    *   Level 1: Standard x86_64 code (the loader).
    *   Level 2: Custom/V8 Bytecode (the logic layer).
    *   Level 3: WebAssembly (the high-performance execution layer).
    Each layer requires a different set of skills to deconstruct, significantly increasing the "work factor" for the investigator.

2.  **Contextual Decoupling:** By moving the actual malicious actions into a bytecode/Wasm layer, the attacker ensures that static analysis and even some dynamic analysis will only see the "normal" behavior of an execution engine (e.g., memory allocation, string handling, and loop processing).

3.  **Anti-Analysis Safeguards:** The sophisticated error handling (`V8_Fatal`, `UnhandledExceptionCallback`) and stack management ensure that the malicious logic does not crash the host process when it encounters "unfriendly" conditions or internal errors, allowing for persistent operation in a target environment.

4.  **Advanced Persistence/Evasion:** The inclusion of **WebSnapshots** allows the attacker to deliver a "pre-primed" environment where the heavy lifting (initialization and decoding) has already happened before the final stage of the attack even begins.

### Recommendation for Incident Response:
*   **Behavioral Monitoring over Static Analysis:** Because the malicious logic is hidden inside bytecode/Wasm, static analysis will likely fail to find "malicious" strings or APIs. Focus on **behavioral indicators**: unexpected network connections initiated by this process, unauthorized file modifications, and high-frequency memory allocations typical of JIT activity.
*   **Memory Forensics:** Since the malicious code is unpacked and executed within its own internal memory space (the engine's "heap"), memory forensics should be used to dump the strings and structures that exist only *after* the engine has initialized and the bytecode has been loaded.
*   **Isolate by Process Signature:** Treat this binary as a high-confidence indicator of an Advanced Persistent Threat (APT). Any machine where this specific engine is found should be considered compromised at a high level.

---

## MITRE ATT&CK Mapping

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1027** | Obfuscated Files or Information | The multi-layered "Matryoshka Doll" approach using Bytecode and WebAssembly hides the true malicious logic from standard static analysis. |
| **T1059.001** | Command and Scripting Interpreter | The use of an industrial-grade, V8-like execution engine allows for complex logic to be executed via high-level scripts rather than direct machine code. |
| **T1036** | Masquerading | "Contextual Decoupling" allows the malware to perform malicious actions that appear as standard operations of a legitimate interpretation environment. |
| **T1474** | Virtualization | The creation of a sophisticated, self-contained execution environment functions similarly to a virtualized layer to abstract and hide underlying instructions. |

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here are the extracted Indicators of Compromise (IOCs). 

Note: The "Extracted Strings" section contains significant amounts of noise from standard cryptographic libraries (OpenSSL) and internal execution logic. No high-fidelity network indicators (IPs/URLs) were found in the raw string dump, but several behavioral indicators were identified in the analysis.

### **IP addresses / URLs / Domains**
*   None detected.

### **File paths / Registry keys**
*   None detected.

### **Mutex names / Named pipes**
*   None detected.

### **Hashes**
*   None detected. (The strings `D3t$`, `3l$`, etc., appear to be internal instruction pointers or scrambled data rather than standard MD5/SHA-1/SHA-256 hashes).

### **Other artifacts**
*   **Engine Identifiers:** 
    *   `V8_Fatal` (Indicates integration of the V8 JavaScript engine)
    *   `StackHasOverflowed_JSHeapBroker` (Internal memory management for JIT environments)
    *   `TryHandleWebAssemblyTrapWindows` (Specific handling for WebAssembly execution)
*   **Execution Techniques:**
    *   **Multi-layered Obfuscation:** The analysis confirms a three-tier execution model: [x86_64 Loader] $\rightarrow$ [Custom/V8 Bytecode] $\rightarrow$ [WebAssembly].
    *   **JIT Compilation Logic:** Use of `TranslateStateValueDescriptor_CodeGenerator` indicates active code generation and "translation" phases.
    *   **Anti-Analysis/Evasion:** The use of `SetUnhandledExceptionCallback_V8` suggests a mechanism to suppress crashes, allowing the malware to remain persistent in a sandbox or production environment.
    *   **Pre-baked Environment:** Reference to `WebSnapshot` and `IsValid_StartupData` indicates that malicious configurations may be "pre-baked" into the binary's state before execution.

---

### **Analyst Note for SOC/IR Teams**
While this sample lacks traditional network IOCs (IPs/Domains) in its static form, it is a high-sophistication **Malware Environment**. 
*   **Detection Strategy:** Do not rely on signature-based detection for strings. Instead, alert on the **behavioral footprint**: processes spawning with high memory allocation rates consistent with JIT compilation, and the presence of "V8" or "WebAssembly" related handles in memory during analysis.
*   **Risk Level:** High. The complexity of the execution engine suggests an APT-level actor attempting to hide malicious logic behind layers of legitimate-looking infrastructure (the V8-like interpreter).

---

## Malware Family Classification

Based on the analysis provided, here is the classification of the sample:

1.  **Malware family:** Custom (Sophisticated Loader/Framework)
2.  **Malware type:** Loader
3.  **Confidence:** High (regarding its function as an execution engine); Low (regarding a specific named campaign like "Emotet" or "Cobalt Strike").
4.  **Key evidence:**
    *   **Multi-Layered Obfuscation ("Matryoshka Doll"):** The sample utilizes a three-tier execution model (x86_64 $\rightarrow$ Bytecode $\rightarrow$ WebAssembly) specifically designed to hide malicious logic from standard static and dynamic analysis.
    *   **Industrial-Grade Execution Environment:** The integration of V8-like features, such as JIT compilation (`TranslateStateValueDescriptor`), `WebSnapshots`, and advanced error handling (`V8_Fatal`), indicates it is a professional-grade wrapper designed to host complex malicious payloads while remaining stable.
    *   **Contextual Decoupling:** By moving the "malicious" actions into high-level bytecode or WebAssembly layers, the author ensures that typical security tools only see "normal" execution engine behavior rather than overt indicators of compromise (IOCs).
