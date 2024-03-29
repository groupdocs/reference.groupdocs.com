---
title: FindProperties
second_title: .NET API 참조용 GroupDocs.Metadata
description: 지정된 조건자를 만족하는 메타데이터 속성을 찾습니다. 검색은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다.
type: docs
weight: 80
url: /ko/net/groupdocs.metadata.common/metadatapackage/findproperties/
---
## MetadataPackage.FindProperties method

지정된 조건자를 만족하는 메타데이터 속성을 찾습니다. 검색은 재귀적이므로 중첩된 모든 패키지에도 영향을 미칩니다.

```csharp
public virtual IEnumerable<MetadataProperty> FindProperties(Func<MetadataProperty, bool> predicate)
```

| 모수 | 유형 | 설명 |
| --- | --- | --- |
| predicate | Func`2 | 조건에 대한 각 메타데이터 속성을 테스트하는 기능입니다. |

### 반환 값

안IEnumerable 조건을 만족하는 패키지의 속성을 포함하는

### 비고

**더 알아보기**

* 이 방법의 사용법을 보여주는 추가 예: [메타데이터 추출](https://docs.groupdocs.com/display/metadatanet/Extracting+metadata)

### 또한보십시오

* class [MetadataProperty](../../metadataproperty)
* delegate [Func&lt;T,TResult&gt;](../../func-2)
* class [MetadataPackage](../../metadatapackage)
* 네임스페이스 [GroupDocs.Metadata.Common](../../metadatapackage)
* 집회 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
