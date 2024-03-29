---
title: ID3V1Tag
second_title: .NET API 참조용 GroupDocs.Metadata
description: 는 ID3v1 태그를 나타냅니다. 자세한 내용은 다음을 참조하십시오.https//en.wikipedia.org/wiki/ID3ID3v1https//en.wikipedia.org/wiki/ID3ID3v1 .
type: docs
weight: 410
url: /ko/net/groupdocs.metadata.formats.audio/id3v1tag/
---
## ID3V1Tag class

는 ID3v1 태그를 나타냅니다. 자세한 내용은 다음을 참조하십시오.[https://en.wikipedia.org/wiki/ID3#ID3v1](https://en.wikipedia.org/wiki/ID3#ID3v1) .

```csharp
public sealed class ID3V1Tag : ID3Tag
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [ID3V1Tag](id3v1tag)() | 의 새 인스턴스를 초기화합니다.[`ID3V1Tag`](../id3v1tag) 클래스. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [Album](../../groupdocs.metadata.formats.audio/id3v1tag/album) { get; set; } | 앨범을 가져오거나 설정합니다. 최대 길이는 30자입니다. |
| [Artist](../../groupdocs.metadata.formats.audio/id3v1tag/artist) { get; set; } | 아티스트를 가져오거나 설정합니다. 최대 길이는 30자입니다. |
| [Comment](../../groupdocs.metadata.formats.audio/id3v1tag/comment) { get; set; } | 설명을 가져오거나 설정합니다. 최대 길이는 30자입니다. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | 메타데이터 속성의 수를 가져옵니다. |
| [GenreValue](../../groupdocs.metadata.formats.audio/id3v1tag/genrevalue) { get; } | 장르 식별자를 가져오거나 설정합니다. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | 가져오기[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) 지정된 이름으로. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | 메타데이터 속성 이름의 컬렉션을 가져옵니다. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | 메타데이터 유형을 가져옵니다. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | GroupDocs.Metadata 검색 엔진을 통해 액세스할 수 있는 속성에 대한 정보가 포함된 설명자 모음을 가져옵니다. |
| [Title](../../groupdocs.metadata.formats.audio/id3v1tag/title) { get; set; } | 제목을 가져오거나 설정합니다. |
| [TrackNumber](../../groupdocs.metadata.formats.audio/id3v1tag/tracknumber) { get; set; } | 트랙 번호를 가져오거나 설정합니다. ID3v1.1 태그로만 제공됩니다. |
| override [Version](../../groupdocs.metadata.formats.audio/id3v1tag/version) { get; } | ID3 버전을 가져옵니다. ID3 또는 ID3v1.1 일 수 있습니다. |
| [Year](../../groupdocs.metadata.formats.audio/id3v1tag/year) { get; set; } | 연도를 가져오거나 설정합니다. 최대 길이는 4자입니다. |

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

ID3(v1) 태그는 MP3 끝에 있는 추가 데이터의 작은 덩어리입니다. 자세한 내용은 다음을 참조하세요.[http://id3.org/ID3v1](http://id3.org/ID3v1) .

**더 알아보기**

* [ID3v1 태그 처리](https://docs.groupdocs.com/display/metadatanet/Handling+the+ID3v1+tag)

### 예

이 코드 샘플은 MP3 파일에서 ID3v1 태그를 읽는 방법을 보여줍니다.

```csharp
using (Metadata metadata = new Metadata(Constants.MP3WithID3V1))
{
    var root = metadata.GetRootPackage<MP3RootPackage>();

    if (root.ID3V1 != null)
    {
        Console.WriteLine(root.ID3V1.Album);
        Console.WriteLine(root.ID3V1.Artist);
        Console.WriteLine(root.ID3V1.Title);
        Console.WriteLine(root.ID3V1.Version);
        Console.WriteLine(root.ID3V1.Comment);

        // ...
    }
}
```

### 또한보십시오

* class [ID3Tag](../id3tag)
* 네임스페이스 [GroupDocs.Metadata.Formats.Audio](../../groupdocs.metadata.formats.audio)
* 집회 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
