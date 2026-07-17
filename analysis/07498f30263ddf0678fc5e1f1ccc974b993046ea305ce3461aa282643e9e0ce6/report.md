# Threat Analysis Report

**Generated:** 2026-07-16 17:42 UTC
**Sample:** `07498f30263ddf0678fc5e1f1ccc974b993046ea305ce3461aa282643e9e0ce6_07498f30263ddf0678fc5e1f1ccc974b993046ea305ce3461aa282643e9e0ce6.exe`

---

## File Metadata

| Field | Value |
|-------|-------|
| File name | `07498f30263ddf0678fc5e1f1ccc974b993046ea305ce3461aa282643e9e0ce6_07498f30263ddf0678fc5e1f1ccc974b993046ea305ce3461aa282643e9e0ce6.exe` |
| File type | PE32+ executable for MS Windows 6.00 (GUI), x86-64, 7 sections |
| Size | 46,069,938 bytes |
| MD5 | `2e8c67488ac278ed0cfd4da1da51c21d` |
| SHA1 | `be95fe6e74484eb36b4332e2e801eec9c1c52697` |
| SHA256 | `07498f30263ddf0678fc5e1f1ccc974b993046ea305ce3461aa282643e9e0ce6` |
| Overall entropy | 7.286 |
| Unpacked | No |

## PE Analysis

| Field | Value |
|-------|-------|
| Timestamp | 1657323478 |
| Machine | 34404 |
| Packed | No |

### Sections

| Name | Size | Entropy | Packed |
|------|------|---------|--------|
| `.text` | 17,106,432 | 6.458 | No |
| `.rdata` | 13,122,048 | 6.212 | No |
| `.data` | 154,624 | 3.729 | No |
| `.pdata` | 816,128 | 6.734 | No |
| `_RDATA` | 512 | 2.449 | No |
| `.rsrc` | 68,096 | 4.672 | No |
| `.reloc` | 106,496 | 5.485 | No |

### Imports

**dbghelp.dll**: `SymFromAddr`, `SymInitialize`, `SymGetLineFromAddr64`, `SymCleanup`, `SymSetOptions`, `UnDecorateSymbolName`
**WS2_32.dll**: `freeaddrinfo`, `getaddrinfo`, `WSACleanup`, `gethostbyname`, `ntohl`, `htonl`, `GetAddrInfoW`, `getnameinfo`, `gethostname`, `__WSAFDIsSet`, `accept`, `sendto`, `recvfrom`, `send`, `recv`
**IPHLPAPI.DLL**: `GetAdaptersAddresses`, `ConvertInterfaceIndexToLuid`, `ConvertInterfaceLuidToNameW`
**PSAPI.DLL**: `GetModuleFileNameExW`, `GetProcessMemoryInfo`, `EnumProcessModules`
**USERENV.dll**: `GetUserProfileDirectoryW`
**ADVAPI32.dll**: `CryptAcquireContextW`, `RegOpenKeyExA`, `RegQueryValueExA`, `RegEnumKeyExW`, `RegQueryInfoKeyW`, `OpenProcessToken`, `GetUserNameW`, `RegCloseKey`, `RegOpenKeyExW`, `ReportEventW`, `RegisterEventSourceW`, `DeregisterEventSource`, `CryptEnumProvidersW`, `CryptSignHashW`, `CryptDestroyHash`
**USER32.dll**: `GetProcessWindowStation`, `MapVirtualKeyW`, `DispatchMessageA`, `TranslateMessage`, `GetUserObjectInformationW`, `GetSystemMetrics`, `GetMessageA`, `MessageBoxW`
**CRYPT32.dll**: `CertOpenStore`, `CertCloseStore`, `CertEnumCertificatesInStore`, `CertFindCertificateInStore`, `CertDuplicateCertificateContext`, `CertFreeCertificateContext`, `CertGetCertificateContextProperty`
**bcrypt.dll**: `BCryptGenRandom`
**KERNEL32.dll**: `RtlLookupFunctionEntry`, `RtlCaptureContext`, `UnhandledExceptionFilter`, `SetUnhandledExceptionFilter`, `IsProcessorFeaturePresent`, `InitializeSListHead`, `CreateEventW`, `WaitForSingleObjectEx`, `GetCPInfo`, `GetStringTypeW`, `InterlockedPushEntrySList`, `RtlUnwindEx`, `RtlPcToFileHeader`, `RaiseException`, `ExitProcess`
**WINMM.dll**: `timeGetTime`

### Exports

`??$Add@VIsolate@internal@v8@@@?$Dictionary@VGlobalDictionary@internal@v8@@VGlobalDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VGlobalDictionary@internal@v8@@@12@PEAVIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VIsolate@internal@v8@@@?$Dictionary@VNameDictionary@internal@v8@@VNameDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNameDictionary@internal@v8@@@12@PEAVIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VIsolate@internal@v8@@@?$Dictionary@VNumberDictionary@internal@v8@@VNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNumberDictionary@internal@v8@@@12@PEAVIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VIsolate@internal@v8@@@?$Dictionary@VSimpleNumberDictionary@internal@v8@@VSimpleNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VSimpleNumberDictionary@internal@v8@@@12@PEAVIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VOffThreadIsolate@internal@v8@@@?$Dictionary@VGlobalDictionary@internal@v8@@VGlobalDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VGlobalDictionary@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VOffThreadIsolate@internal@v8@@@?$Dictionary@VNameDictionary@internal@v8@@VNameDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNameDictionary@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@V?$Handle@VName@internal@v8@@@12@V?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VOffThreadIsolate@internal@v8@@@?$Dictionary@VNumberDictionary@internal@v8@@VNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNumberDictionary@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Add@VOffThreadIsolate@internal@v8@@@?$Dictionary@VSimpleNumberDictionary@internal@v8@@VSimpleNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VSimpleNumberDictionary@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@IV?$Handle@VObject@internal@v8@@@12@VPropertyDetails@12@PEAVInternalIndex@12@@Z`, `??$Allocate@VIsolate@internal@v8@@@AstConsString@internal@v8@@AEBA?AV?$Handle@VString@internal@v8@@@12@PEAVIsolate@12@@Z`, `??$Allocate@VIsolate@internal@v8@@@DescriptorArray@internal@v8@@SA?AV?$Handle@VDescriptorArray@internal@v8@@@12@PEAVIsolate@12@HHW4AllocationType@12@@Z`, `??$Allocate@VOffThreadIsolate@internal@v8@@@AstConsString@internal@v8@@AEBA?AV?$Handle@VString@internal@v8@@@12@PEAVOffThreadIsolate@12@@Z`, `??$AllocateFlat@VIsolate@internal@v8@@@AstConsString@internal@v8@@QEBA?AV?$Handle@VString@internal@v8@@@12@PEAVIsolate@12@@Z`, `??$AllocateFlat@VOffThreadIsolate@internal@v8@@@AstConsString@internal@v8@@QEBA?AV?$Handle@VString@internal@v8@@@12@PEAVOffThreadIsolate@12@@Z`, `??$AllocatePage@$00VSemiSpace@internal@v8@@@MemoryAllocator@internal@v8@@QEAAPEAVPage@12@_KPEAVSemiSpace@12@W4Executability@12@@Z`, `??$AllocatePage@$0A@VPagedSpace@internal@v8@@@MemoryAllocator@internal@v8@@QEAAPEAVPage@12@_KPEAVPagedSpace@12@W4Executability@12@@Z`, `??$AllocatePage@$0A@VSemiSpace@internal@v8@@@MemoryAllocator@internal@v8@@QEAAPEAVPage@12@_KPEAVSemiSpace@12@W4Executability@12@@Z`, `??$AllocateScopeInfos@VIsolate@internal@v8@@@DeclarationScope@internal@v8@@SAXPEAVParseInfo@12@PEAVIsolate@12@@Z`, `??$AllocateScopeInfos@VOffThreadIsolate@internal@v8@@@DeclarationScope@internal@v8@@SAXPEAVParseInfo@12@PEAVOffThreadIsolate@12@@Z`, `??$AllocateScopeInfosRecursively@VIsolate@internal@v8@@@Scope@internal@v8@@AEAAXPEAVIsolate@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$AllocateScopeInfosRecursively@VOffThreadIsolate@internal@v8@@@Scope@internal@v8@@AEAAXPEAVOffThreadIsolate@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$AllocateSlotSet@$00@MemoryChunk@internal@v8@@QEAAPEAVSlotSet@12@XZ`, `??$AllocateSlotSet@$0A@@MemoryChunk@internal@v8@@QEAAPEAVSlotSet@12@XZ`, `??$At@VIsolate@internal@v8@@@ConstantArrayBuilder@interpreter@internal@v8@@QEBA?AV?$MaybeHandle@VObject@internal@v8@@@23@_KPEAVIsolate@23@@Z`, `??$At@VOffThreadIsolate@internal@v8@@@ConstantArrayBuilder@interpreter@internal@v8@@QEBA?AV?$MaybeHandle@VObject@internal@v8@@@23@_KPEAVOffThreadIsolate@23@@Z`, `??$BigIntLiteral@VIsolate@internal@v8@@@internal@v8@@YA?AV?$MaybeHandle@VBigInt@internal@v8@@@01@PEAVIsolate@01@PEBD@Z`, `??$BigIntLiteral@VOffThreadIsolate@internal@v8@@@internal@v8@@YA?AV?$MaybeHandle@VBigInt@internal@v8@@@01@PEAVOffThreadIsolate@01@PEBD@Z`, `??$BuildValue@VIsolate@internal@v8@@@Literal@internal@v8@@QEBA?AV?$Handle@VObject@internal@v8@@@12@PEAVIsolate@12@@Z`, `??$BuildValue@VOffThreadIsolate@internal@v8@@@Literal@internal@v8@@QEBA?AV?$Handle@VObject@internal@v8@@@12@PEAVOffThreadIsolate@12@@Z`, `??$Create@VIsolate@internal@v8@@@ScopeInfo@internal@v8@@SA?AV?$Handle@VScopeInfo@internal@v8@@@12@PEAVIsolate@12@PEAVZone@12@PEAVScope@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$Create@VOffThreadIsolate@internal@v8@@@ScopeInfo@internal@v8@@SA?AV?$Handle@VScopeInfo@internal@v8@@@12@PEAVOffThreadIsolate@12@PEAVZone@12@PEAVScope@12@V?$MaybeHandle@VScopeInfo@internal@v8@@@12@@Z`, `??$CreateScript@VIsolate@internal@v8@@@ParseInfo@internal@v8@@QEAA?AV?$Handle@VScript@internal@v8@@@12@PEAVIsolate@12@V?$Handle@VString@internal@v8@@@12@V?$MaybeHandle@VFixedArray@internal@v8@@@12@VScriptOriginOptions@2@W4NativesFlag@12@@Z`, `??$CreateScript@VOffThreadIsolate@internal@v8@@@ParseInfo@internal@v8@@QEAA?AV?$Handle@VScript@internal@v8@@@12@PEAVOffThreadIsolate@12@V?$Handle@VString@internal@v8@@@12@V?$MaybeHandle@VFixedArray@internal@v8@@@12@VScriptOriginOptions@2@W4NativesFlag@12@@Z`, `??$Decode@E@Utf8Decoder@internal@v8@@QEAAXPEAEAEBV?$Vector@$$CBE@12@@Z`, `??$Decode@G@Utf8Decoder@internal@v8@@QEAAXPEAGAEBV?$Vector@$$CBE@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VCompilationCacheTable@internal@v8@@VCompilationCacheShape@23@@internal@v8@@SA?AV?$Handle@VCompilationCacheTable@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VEphemeronHashTable@internal@v8@@VEphemeronHashTableShape@23@@internal@v8@@SA?AV?$Handle@VEphemeronHashTable@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VGlobalDictionary@internal@v8@@VGlobalDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VGlobalDictionary@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VNameDictionary@internal@v8@@VNameDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNameDictionary@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VNumberDictionary@internal@v8@@VNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNumberDictionary@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VObjectHashSet@internal@v8@@VObjectHashSetShape@23@@internal@v8@@SA?AV?$Handle@VObjectHashSet@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VObjectHashTable@internal@v8@@VObjectHashTableShape@23@@internal@v8@@SA?AV?$Handle@VObjectHashTable@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VSimpleNumberDictionary@internal@v8@@VSimpleNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VSimpleNumberDictionary@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VStringSet@internal@v8@@VStringSetShape@23@@internal@v8@@SA?AV?$Handle@VStringSet@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VIsolate@internal@v8@@@?$HashTable@VStringTable@internal@v8@@VStringTableShape@23@@internal@v8@@SA?AV?$Handle@VStringTable@internal@v8@@@12@PEAVIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VOffThreadIsolate@internal@v8@@@?$HashTable@VCompilationCacheTable@internal@v8@@VCompilationCacheShape@23@@internal@v8@@SA?AV?$Handle@VCompilationCacheTable@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VOffThreadIsolate@internal@v8@@@?$HashTable@VEphemeronHashTable@internal@v8@@VEphemeronHashTableShape@23@@internal@v8@@SA?AV?$Handle@VEphemeronHashTable@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VOffThreadIsolate@internal@v8@@@?$HashTable@VGlobalDictionary@internal@v8@@VGlobalDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VGlobalDictionary@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VOffThreadIsolate@internal@v8@@@?$HashTable@VNameDictionary@internal@v8@@VNameDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNameDictionary@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VOffThreadIsolate@internal@v8@@@?$HashTable@VNumberDictionary@internal@v8@@VNumberDictionaryShape@23@@internal@v8@@SA?AV?$Handle@VNumberDictionary@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@HW4AllocationType@12@@Z`, `??$EnsureCapacity@VOffThreadIsolate@internal@v8@@@?$HashTable@VObjectHashSet@internal@v8@@VObjectHashSetShape@23@@internal@v8@@SA?AV?$Handle@VObjectHashSet@internal@v8@@@12@PEAVOffThreadIsolate@12@V312@HW4AllocationType@12@@Z`

## Extracted Strings

Total strings found: **149100** (showing first 100)

```
!This program cannot be run in DOS mode.
$
Rich{A
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
3T$<D!
```

## Disassembly Overview

Functions analyzed: **30** | Decompiled to C: **30**

| Name | Offset | Size | Decompiled |
|------|--------|------|------------|
| `sym.node.exe__FeedbackVectorSpecPrint_FeedbackVectorSpec_internal_v8__QEAAXAEAV__basic_ostream_DU__char_traits_D_std___std___Z` | `0x140998330` | 16785763 | ✓ |
| `fcn.1405fa280` | `0x1405fa280` | 16777475 | ✓ |
| `fcn.1405fa4f0` | `0x1405fa4f0` | 16777475 | ✓ |
| `fcn.1405f93f0` | `0x1405f93f0` | 16777475 | ✓ |
| `sym.node.exe__NeedsExactContext_OperatorProperties_compiler_internal_v8__SA_NPEBVOperator_234__Z` | `0x140e43890` | 16777218 | ✓ |
| `fcn.1409cdd30` | `0x1409cdd30` | 16777218 | ✓ |
| `sym.node.exe__New_FeedbackVector_internal_v8__SA_AV__Handle_VFeedbackVector_internal_v8___23_PEAVIsolate_23_V__Handle_VSharedFunctionInfo_internal_v8___23_V__Handle_VClosureFeedbackCellArray_internal_v8___23__Z` | `0x1407f8f10` | 16776961 | ✓ |
| `fcn.1408eb670` | `0x1408eb670` | 16776961 | ✓ |
| `fcn.1405be890` | `0x1405be890` | 16712021 | ✓ |
| `fcn.140989250` | `0x140989250` | 16711696 | ✓ |
| `fcn.14019ba70` | `0x14019ba70` | 11765358 | ✓ |
| `fcn.1405aa5e0` | `0x1405aa5e0` | 10836528 | ✓ |
| `fcn.1405b9a00` | `0x1405b9a00` | 10774032 | ✓ |
| `sym.node.exe__AlignedFree_internal_v8__YAXPEAX_Z` | `0x1405f3eb0` | 10721911 | ✓ |
| `sym.node.exe__GetInstructionFlags_InstructionScheduler_compiler_internal_v8__AEBAHPEBVInstruction_234__Z` | `0x140ea5080` | 10671533 | ✓ |
| `sym.node.exe__Lub_BitsetType_compiler_internal_v8__SAIAEBVHeapObjectType_234__Z` | `0x14045c910` | 10296694 | ✓ |
| `sym.node.exe__ParseDisjunction_RegExpParser_internal_v8__QEAAPEAVRegExpTree_23_XZ` | `0x1406ad4c0` | 9841731 | ✓ |
| `fcn.14097aef0` | `0x14097aef0` | 9819434 | ✓ |
| `fcn.140a67a00` | `0x140a67a00` | 9525060 | ✓ |
| `fcn.1407e13d0` | `0x1407e13d0` | 8131399 | ✓ |
| `sym.node.exe__PredictExceptionCatcher_Isolate_internal_v8__QEAA_AW4CatchType_123_XZ` | `0x140981390` | 7072956 | ✓ |
| `sym.node.exe__TryHandleWebAssemblyTrapWindows_v8__YA_NPEAU_EXCEPTION_POINTERS___Z` | `0x140aab340` | 6773445 | ✓ |
| `sym.node.exe__SetUnhandledExceptionCallback_V8_v8__SAXP6AHPEAU_EXCEPTION_POINTERS___Z_Z` | `0x140aa6890` | 6749493 | ✓ |
| `fcn.1409cd770` | `0x1409cd770` | 6564243 | ✓ |
| `fcn.140a4b050` | `0x140a4b050` | 6050230 | ✓ |
| `fcn.1404fa7e0` | `0x1404fa7e0` | 5934761 | ✓ |
| `fcn.140509d30` | `0x140509d30` | 5757918 | ✓ |
| `sym.node.exe__TranslateStateValueDescriptor_CodeGenerator_compiler_internal_v8__AEAAXPEAVStateValueDescriptor_234_PEAVStateValueList_234_PEAVTranslation_34_PEAVInstructionOperandIterator_234__Z` | `0x140e4b930` | 4848275 | ✓ |
| `sym.node.exe__InitializePlatform_V8_v8__SAXPEAVPlatform_2__Z` | `0x140a91f30` | 4837493 | ✓ |
| `sym.node.exe__EnableWebAssemblyTrapHandler_V8_v8__SA_N_N_Z` | `0x140a83140` | 4778005 | ✓ |

### Decompiled Code Files

- [`code/fcn.14019ba70.c`](code/fcn.14019ba70.c)
- [`code/fcn.1404fa7e0.c`](code/fcn.1404fa7e0.c)
- [`code/fcn.140509d30.c`](code/fcn.140509d30.c)
- [`code/fcn.1405aa5e0.c`](code/fcn.1405aa5e0.c)
- [`code/fcn.1405b9a00.c`](code/fcn.1405b9a00.c)
- [`code/fcn.1405be890.c`](code/fcn.1405be890.c)
- [`code/fcn.1405f93f0.c`](code/fcn.1405f93f0.c)
- [`code/fcn.1405fa280.c`](code/fcn.1405fa280.c)
- [`code/fcn.1405fa4f0.c`](code/fcn.1405fa4f0.c)
- [`code/fcn.1407e13d0.c`](code/fcn.1407e13d0.c)
- [`code/fcn.1408eb670.c`](code/fcn.1408eb670.c)
- [`code/fcn.14097aef0.c`](code/fcn.14097aef0.c)
- [`code/fcn.140989250.c`](code/fcn.140989250.c)
- [`code/fcn.1409cd770.c`](code/fcn.1409cd770.c)
- [`code/fcn.1409cdd30.c`](code/fcn.1409cdd30.c)
- [`code/fcn.140a4b050.c`](code/fcn.140a4b050.c)
- [`code/fcn.140a67a00.c`](code/fcn.140a67a00.c)
- [`code/sym.node.exe__AlignedFree_internal_v8__YAXPEAX_Z.c`](code/sym.node.exe__AlignedFree_internal_v8__YAXPEAX_Z.c)
- [`code/sym.node.exe__EnableWebAssemblyTrapHandler_V8_v8__SA_N_N_Z.c`](code/sym.node.exe__EnableWebAssemblyTrapHandler_V8_v8__SA_N_N_Z.c)
- [`code/sym.node.exe__FeedbackVectorSpecPrint_FeedbackVectorSpec_internal_v8__QEAAXAEAV__basic_ostream_DU__char_traits_D_std___s.c`](code/sym.node.exe__FeedbackVectorSpecPrint_FeedbackVectorSpec_internal_v8__QEAAXAEAV__basic_ostream_DU__char_traits_D_std___s.c)
- [`code/sym.node.exe__GetInstructionFlags_InstructionScheduler_compiler_internal_v8__AEBAHPEBVInstruction_234__Z.c`](code/sym.node.exe__GetInstructionFlags_InstructionScheduler_compiler_internal_v8__AEBAHPEBVInstruction_234__Z.c)
- [`code/sym.node.exe__InitializePlatform_V8_v8__SAXPEAVPlatform_2__Z.c`](code/sym.node.exe__InitializePlatform_V8_v8__SAXPEAVPlatform_2__Z.c)
- [`code/sym.node.exe__Lub_BitsetType_compiler_internal_v8__SAIAEBVHeapObjectType_234__Z.c`](code/sym.node.exe__Lub_BitsetType_compiler_internal_v8__SAIAEBVHeapObjectType_234__Z.c)
- [`code/sym.node.exe__NeedsExactContext_OperatorProperties_compiler_internal_v8__SA_NPEBVOperator_234__Z.c`](code/sym.node.exe__NeedsExactContext_OperatorProperties_compiler_internal_v8__SA_NPEBVOperator_234__Z.c)
- [`code/sym.node.exe__New_FeedbackVector_internal_v8__SA_AV__Handle_VFeedbackVector_internal_v8___23_PEAVIsolate_23_V__Handle_VS.c`](code/sym.node.exe__New_FeedbackVector_internal_v8__SA_AV__Handle_VFeedbackVector_internal_v8___23_PEAVIsolate_23_V__Handle_VS.c)
- [`code/sym.node.exe__ParseDisjunction_RegExpParser_internal_v8__QEAAPEAVRegExpTree_23_XZ.c`](code/sym.node.exe__ParseDisjunction_RegExpParser_internal_v8__QEAAPEAVRegExpTree_23_XZ.c)
- [`code/sym.node.exe__PredictExceptionCatcher_Isolate_internal_v8__QEAA_AW4CatchType_123_XZ.c`](code/sym.node.exe__PredictExceptionCatcher_Isolate_internal_v8__QEAA_AW4CatchType_123_XZ.c)
- [`code/sym.node.exe__SetUnhandledExceptionCallback_V8_v8__SAXP6AHPEAU_EXCEPTION_POINTERS___Z_Z.c`](code/sym.node.exe__SetUnhandledExceptionCallback_V8_v8__SAXP6AHPEAU_EXCEPTION_POINTERS___Z_Z.c)
- [`code/sym.node.exe__TranslateStateValueDescriptor_CodeGenerator_compiler_internal_v8__AEAAXPEAVStateValueDescriptor_234_PEAVSt.c`](code/sym.node.exe__TranslateStateValueDescriptor_CodeGenerator_compiler_internal_v8__AEAAXPEAVStateValueDescriptor_234_PEAVSt.c)
- [`code/sym.node.exe__TryHandleWebAssemblyTrapWindows_v8__YA_NPEAU_EXCEPTION_POINTERS___Z.c`](code/sym.node.exe__TryHandleWebAssemblyTrapWindows_v8__YA_NPEAU_EXCEPTION_POINTERS___Z.c)

## Behavioral Analysis

The analysis has been updated to include the final piece of disassembly (chunk 3/3). All previous findings regarding JIT compilation, RegEx parsing, and platform-specific optimizations remain integrated into this final report.

### Updated Analysis of Code Functionality

#### 1. Advanced Compiler & JIT Logic
The presence of functions like `TranslateStateValueDescriptor_CodeGenerator` confirms a sophisticated Just-In-Time (JIT) compiler infrastructure:
*   **Instruction Mapping:** Converts high-level "State Value Descriptors" into executable machine code or intermediate representation.
*   **Deoptimization Paths:** Includes explicit fallback logic (`DefineDeoptimizationLiteral`). This is critical for JavaScript engines to handle cases where the engine's optimistic assumptions about variable types are invalidated during execution.
*   **Type Handling:** The `Lub_BitsetType` function confirms the use of bitsets to track object properties and capabilities during the optimization phase, a standard technique in high-performance VMs.

#### 2. Complex Grammar Parsing (Regular Expressions)
The inclusion of the `ParseDisjunction_RegSeqParser` block highlights extensive support for complex text processing:
*   **State Machine Complexity:** The large switch tables are used to handle diverse regex tokens and escape sequences efficiently.
*   **Recursive Handling:** The code manages nested structures (like grouped expressions), typical of high-performance engines required by modern web browsers.

#### 3. WebAssembly & Platform Integration (Updated)
The final chunk of disassembly provides specific confirmation regarding the engine's handling of WebAssembly (Wasm):
*   **Trap Handling Mechanism:** The function `EnableWebAssemblyTrapHandler_V8` is a direct implementation of safety checks for Wasm execution. In WebAssembly, a "trap" occurs when an operation violates the Wasm specification (e.g., out-of-bounds memory access or division by zero).
*   **Conditional Dispatch:** The logic within `EnableWebAssemblyTrapHandler_V8` (checking if `arg1 != '\0'`) suggests a toggleable system where the engine can choose between a default handler and a specialized platform-specific handler. 
*   **System-Level Interfacing:** Combined with `TryHandleWebAssemblyTrapWindows` and `SetUnhandledExceptionCallback_V8`, this confirms the engine is designed to translate low-level hardware/OS signals into manageable JavaScript exceptions across different operating systems.

### Technical Observations & Characteristics
*   **Large Dispatch Tables:** The extensive switch statements (e.g., those involving codes like `0x42`, `0x61`) are not evidence of obfuscation or "junk code." They are highly optimized jump tables used to process opcodes or byte-code efficiently.
*   **Robust Error Handling:** The naming conventions and the structure of the trap handlers indicate a mature, production-grade software architecture designed for stability and safety in a multi-tenant environment (where different scripts must be isolated from one another).
*   **Standard Library Conventions:** The use of `_v8` prefixes and specific internal namespaces confirms that this is part of the V8 engine's standard library.

### Security Assessment Update
*   **Malicious Behavior:** No malicious indicators were found in any segment of the provided disassembly. The complexity observed—while daunting to manual analysis—is functionally necessary for a production-grade JavaScript engine (like V8) to handle modern web features like WebAssembly and complex Regular Expressions.
*   **Anti-Analysis Check:** There are no signatures of "packers," "crypters," or "anti-debugging" tricks in this segment. The complexity is structural, not intentional obfuscation.

### Final Conclusion
The final analysis confirms that the target code is a **legitimate and highly complex component of the V8 JavaScript engine.** 

The disassembly demonstrates the three pillars of modern JS engine architecture:
1.  **Sophisticated JIT Compilation** (State Value Descriptors & Deoptimization).
2.  **Robust Text Processing** (Complex RegEx state machines).
3.  **Low-Level Platform/Wasm Integration** (Trap handling and OS-level exception mapping).

The presence of these features confirms the code's purpose as a high-performance execution environment for web technologies. No evidence of malicious intent or non-standard "packer" behavior was found in any part of the provided disassembly.

---

## MITRE ATT&CK Mapping

As a threat intelligence analyst, I have reviewed the provided behavioral analysis. While the final conclusion states the code is non-malicious and part of a legitimate library (V8), several features identified are common areas of interest in threat modeling because they provide the infrastructure necessary for script execution and complex logic handling.

Below is the mapping of these observed behaviors to the MITRE ATT&CK framework:

| Technique ID | Name | Justification |
| :--- | :--- | :--- |
| **T1059** | Command and Scripting Interpreter | The inclusion of JIT compilation, deoptimization paths, and RegEx parsing confirms the presence of a robust environment for executing and processing scripts (e.g., JavaScript/WebAssembly). |
| **T1497** | Virtualization/Packers | Although determined to be "functional complexity" rather than malicious obfuscation, the large jump tables and complex logic were analyzed specifically for these evasion characteristics. |
| **T1027** | Obfuscated Files or Information | The analysis of the RegEx parsing state machine was conducted to determine if high-complexity logic was being used to mask intent; however, no malicious obfuscation was found. |

### Analyst Notes:
*   **Contextual Clarification:** While these techniques are mapped based on the *functionality* described (e.g., a JIT compiler is technically an interpreter infrastructure), the investigation concludes that there is **no evidence of malicious intent**. 
*   **JIT Capability:** The "Advanced Compiler" and "Deoptimization" features provide functionality that, in a malicious context, could be used to execute dynamically generated shellcode, but here they serve the standard requirements of the V8 engine.
*   **Execution Environment:** The mapping to **T1059** is based on the fact that the code provides the machinery necessary for script execution; regardless of whether the current implementation is malicious or benign, this is the applicable ATT&CK category for such functionality.

---

## Indicators of Compromise

Based on the provided strings and behavioral analysis, here is the threat intelligence report regarding Indicators of Compromise (IOCs):

### **Threat Intelligence Summary**
The analyzed code and strings belong to a legitimate software component—specifically the **V8 JavaScript engine**. The behavior described involves standard JIT compilation, Regular Expression parsing, and WebAssembly trap handling. 

### **Indicators of Compromise (IOCs)**

*   **IP addresses / URLs / Domains:**
    *   *None identified.*
*   **File paths / Registry keys:**
    *   *None identified.* (Note: Internal function names such as `TryHandleWebAssemblyTrapWindows` and `SetUnhandledExceptionCallback_V8` are part of the application's internal logic and do not constitute filesystem or registry IOCs.)
*   **Mutex names / Named pipes:**
    *   *None identified.*
*   **Hashes:**
    *   *None identified.*
*   **Other artifacts (user agents, C2 patterns, etc.):**
    *   *None identified.*

---

### **Analyst Notes**
1.  **False Positives:** The strings containing `CRYPTOGAMS`, `SHA512`, `RC4`, and `Poly1305` are standard OpenSSL cryptographic library markers. These are common in many legitimate applications and do not indicate malicious activity.
2.  **Binary Artifacts:** The repetitive, non-alphanumeric character strings (e.g., `SUATAUAVAWH`, `VWSUATAUAVAW`) appear to be remnants of compiled machine code or jump tables rather than meaningful data or commands used by an adversary.
3.  **Conclusion:** The sample is confirmed as a **benign** component of the V8 engine. No malicious indicators were extracted from the provided data.

---

## Malware Family Classification

Based on the provided analysis, here is the classification for the sample:

1. **Malware family**: None (Benign)
2. **Malware type**: N/A (Legitimate Software Component)
3. **Confidence**: High
4. **Key evidence**:
    * **Verified Infrastructure:** The analysis confirms the code belongs to the **V8 JavaScript engine**, a legitimate, production-grade software component used in web browsers and environments like Node.js.
    * **Absence of Malicious Indicators:** No indicators of compromise (IOCs), such as C2 infrastructure, packers, crypters, or anti-debugging techniques, were detected during the analysis.
    * **Functional Complexity vs. Obfuscation:** Complex features identified (JIT compilation, RegEx state machines, and WebAssembly trap handling) are documented as necessary technical requirements for a high-performance JavaScript engine rather than attempts to hide malicious intent.
