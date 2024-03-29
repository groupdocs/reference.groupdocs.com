---
title: ConvertTo
second_title: .NET API 참조용 GroupDocs.Conversion
description: 변환된 문서를 file 로 저장
type: docs
weight: 20
url: /ko/net/groupdocs.conversion.fluent/iconversionto/convertto/
---
## ConvertTo(string) {#convertto_2}

변환된 문서를 file 로 저장

```csharp
public IConversionConvertOptionOrCompletedOrConvert ConvertTo(string fileName)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| fileName | String | 변환된 문서 |

### 반환 값

전환 구축을 계속하기 위한 인터페이스

### 또한보십시오

* interface [IConversionConvertOptionOrCompletedOrConvert](../../iconversionconvertoptionorcompletedorconvert)
* interface [IConversionTo](../../iconversionto)
* 네임스페이스 [GroupDocs.Conversion.Fluent](../../iconversionto)
* 집회 [GroupDocs.Conversion](../../../)

---

## ConvertTo(Func&lt;Stream&gt;) {#convertto}

변환된 문서를 stream 로 저장

```csharp
public IConversionConvertOptionOrCompletedOrConvert ConvertTo(Func<Stream> convertedStreamProvider)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| convertedStreamProvider | Func`1 | 변환된 문서 스트림 공급자 |

### 반환 값

전환 구축을 계속하기 위한 인터페이스

### 또한보십시오

* interface [IConversionConvertOptionOrCompletedOrConvert](../../iconversionconvertoptionorcompletedorconvert)
* interface [IConversionTo](../../iconversionto)
* 네임스페이스 [GroupDocs.Conversion.Fluent](../../iconversionto)
* 집회 [GroupDocs.Conversion](../../../)

---

## ConvertTo(Func&lt;FileType, Stream&gt;) {#convertto_1}

변환된 문서를 type 별로 스트림으로 저장합니다.

```csharp
public IConversionConvertOptionOrCompletedOrConvert ConvertTo(
    Func<FileType, Stream> convertedStreamProvider)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| convertedStreamProvider | Func`2 | 변환된 문서 스트림 provider |

### 반환 값

전환 구축을 계속하기 위한 인터페이스

### 또한보십시오

* interface [IConversionConvertOptionOrCompletedOrConvert](../../iconversionconvertoptionorcompletedorconvert)
* class [FileType](../../../groupdocs.conversion.filetypes/filetype)
* interface [IConversionTo](../../iconversionto)
* 네임스페이스 [GroupDocs.Conversion.Fluent](../../iconversionto)
* 집회 [GroupDocs.Conversion](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
