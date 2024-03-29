---
title: FuzzySearchOptions
second_title: GroupDocs..NET API 참조 검색
description: 퍼지 검색 옵션을 제공합니다.
type: docs
weight: 850
url: /ko/net/groupdocs.search.options/fuzzysearchoptions/
---
## FuzzySearchOptions class

퍼지 검색 옵션을 제공합니다.

```csharp
public class FuzzySearchOptions
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [ConsiderTranspositions](../../groupdocs.search.options/fuzzysearchoptions/considertranspositions) { get; set; } | 퍼지 검색 알고리즘이 인접한 두 문자의 전치를 단일 실수로 간주해야 하는지 여부를 나타내는 값을 가져오거나 설정합니다. 기본값은`진실` . |
| [Enabled](../../groupdocs.search.options/fuzzysearchoptions/enabled) { get; set; } | 퍼지 검색 기능의 활성화 여부를 나타내는 값을 가져오거나 설정합니다. 기본값은`거짓` . |
| [FuzzyAlgorithm](../../groupdocs.search.options/fuzzysearchoptions/fuzzyalgorithm) { get; set; } | 퍼지 검색 알고리즘을 가져오거나 설정합니다. 현재 사용 가능한 퍼지 검색 알고리즘은 다음과 같습니다.[`SimilarityLevel`](../similaritylevel) 그리고[`TableDiscreteFunction`](../tablediscretefunction). 기본값은 다음의 인스턴스입니다.[`SimilarityLevel`](../similaritylevel) 유사성 수준 값이`0.5` . |
| [OnlyBestResults](../../groupdocs.search.options/fuzzysearchoptions/onlybestresults) { get; set; } | 최상의 결과만 반환할지 여부를 나타내는 값을 가져오거나 설정합니다. 기본값은`거짓` . |
| [OnlyBestResultsRange](../../groupdocs.search.options/fuzzysearchoptions/onlybestresultsrange) { get; set; } | 발견된 최소 오류 수를 초과하는 최대값을 가져오거나 설정합니다. 기본값은`0` . |

### 비고

**더 알아보기**

* [퍼지 검색](https://docs.groupdocs.com/display/searchnet/Fuzzy+search)
* [검색 옵션](https://docs.groupdocs.com/display/searchnet/Search+options)

### 또한보십시오

* 네임스페이스 [GroupDocs.Search.Options](../../groupdocs.search.options)
* 집회 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
