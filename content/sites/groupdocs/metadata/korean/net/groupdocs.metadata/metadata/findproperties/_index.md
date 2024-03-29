---
title: FindProperties
second_title: .NET API 참조용 GroupDocs.Metadata
description: 지정된 조건자를 만족하는 메타데이터 속성을 찾습니다. 검색은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다.
type: docs
weight: 50
url: /ko/net/groupdocs.metadata/metadata/findproperties/
---
## Metadata.FindProperties method

지정된 조건자를 만족하는 메타데이터 속성을 찾습니다. 검색은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다.

```csharp
public IEnumerable<MetadataProperty> FindProperties(Func<MetadataProperty, bool> predicate)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| predicate | Func`2 | 조건에 대한 각 메타데이터 속성을 테스트하는 기능입니다. |

### 반환 값

안IEnumerable 조건을 만족하는 패키지의 속성을 포함하는

### 비고

**더 알아보기**

* 이 방법의 사용법을 보여주는 추가 예: [메타데이터 추출](https://docs.groupdocs.com/display/metadatanet/Extracting+metadata)

### 예

이 예는 태그를 사용하여 특정 메타데이터 속성을 검색하는 방법을 보여줍니다.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPptx))
{
    // 술어를 만족하는 모든 속성을 가져옵니다.
    // 속성에는 마지막 문서 편집기의 이름 또는 문서가 마지막으로 수정된 날짜/시간이 포함됩니다.
    var properties = metadata.FindProperties(p => p.Tags.Contains(Tags.Person.Editor) || p.Tags.Contains(Tags.Time.Modified));
    foreach (var property in properties)
    {
        Console.WriteLine("Property name: {0}, Property value: {1}", property.Name, property.Value);
    }
}
```

### 또한보십시오

* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [Metadata](../../metadata)
* 네임스페이스 [GroupDocs.Metadata](../../metadata)
* 집회 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
