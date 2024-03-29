---
title: ZipFile
second_title: .NET API 참조용 GroupDocs.Metadata
description: 보관된 파일 또는 디렉터리와 관련된 메타데이터를 나타냅니다.
type: docs
weight: 350
url: /ko/net/groupdocs.metadata.formats.archive/zipfile/
---
## ZipFile class

보관된 파일 또는 디렉터리와 관련된 메타데이터를 나타냅니다.

```csharp
public sealed class ZipFile : CustomPackage
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [CompressedSize](../../groupdocs.metadata.formats.archive/zipfile/compressedsize) { get; } | 바이트 단위로 압축된 크기를 가져옵니다. |
| [CompressionMethod](../../groupdocs.metadata.formats.archive/zipfile/compressionmethod) { get; } | 압축 방법을 가져옵니다. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | 메타데이터 속성의 수를 가져옵니다. |
| [Flags](../../groupdocs.metadata.formats.archive/zipfile/flags) { get; } | ZIP 항목 플래그를 가져옵니다. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | 가져오기[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) 지정된 이름으로. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | 메타데이터 속성 이름의 컬렉션을 가져옵니다. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | 메타데이터 유형을 가져옵니다. |
| [ModificationDateTime](../../groupdocs.metadata.formats.archive/zipfile/modificationdatetime) { get; } | 마지막 수정 날짜 및 시간을 가져옵니다. |
| [Name](../../groupdocs.metadata.formats.archive/zipfile/name) { get; } | 항목 이름을 가져옵니다. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | GroupDocs.Metadata 검색 엔진을 통해 액세스할 수 있는 속성에 대한 정보가 포함된 설명자 모음을 가져옵니다. |
| [RawName](../../groupdocs.metadata.formats.archive/zipfile/rawname) { get; } | 항목 이름을 나타내는 바이트 배열을 가져옵니다. |
| [UncompressedSize](../../groupdocs.metadata.formats.archive/zipfile/uncompressedsize) { get; } | 압축되지 않은 크기를 바이트 단위로 가져옵니다. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 지정된 조건자를 만족하는 알려진 메타데이터 속성을 추가합니다. 이 작업은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | 패키지에 지정된 이름의 메타데이터 속성이 포함되어 있는지 확인합니다. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | 지정된 조건자를 만족하는 메타데이터 속성을 찾습니다. 검색은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | 컬렉션을 반복하는 열거자를 반환합니다. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | 지정된 조건자를 만족하는 메타데이터 속성을 제거합니다. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | 패키지에서 쓰기 가능한 메타데이터 속성을 제거합니다. 이 작업은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 지정된 술어를 만족하는 알려진 메타데이터 속성을 설정합니다. 이 작업은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다. 이 방법은[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) 그리고[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) 기존 속성이 술어를 충족하면 해당 값이 업데이트됩니다. 조건자를 충족하는 패키지에 알려진 속성이 누락된 경우 패키지에 추가됩니다. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 지정된 술어를 만족하는 알려진 메타데이터 속성을 업데이트합니다. 이 작업은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다. |

### 비고

**더 알아보기**

* [ZIP 아카이브 작업](https://docs.groupdocs.com/display/metadatanet/Working+with+ZIP+archives)

### 또한보십시오

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* 네임스페이스 [GroupDocs.Metadata.Formats.Archive](../../groupdocs.metadata.formats.archive)
* 집회 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
