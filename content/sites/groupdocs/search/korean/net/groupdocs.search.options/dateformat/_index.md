---
title: DateFormat
second_title: GroupDocs..NET API 참조 검색
description: 날짜 형식을 나타냅니다.
type: docs
weight: 770
url: /ko/net/groupdocs.search.options/dateformat/
---
## DateFormat class

날짜 형식을 나타냅니다.

```csharp
public class DateFormat
```

## 생성자

| 이름 | 설명 |
| --- | --- |
| [DateFormat](dateformat#constructor)(DateFormatElement[], string) | 의 새 인스턴스를 초기화합니다.[`DateFormat`](../dateformat) 클래스. |
| [DateFormat](dateformat#constructor_1)(string, DateFormatElement[]) | 의 새 인스턴스를 초기화합니다.[`DateFormat`](../dateformat) 클래스. |

## 속성

| 이름 | 설명 |
| --- | --- |
| [DateSeparator](../../groupdocs.search.options/dateformat/dateseparator) { get; } | 날짜 구분 기호를 가져옵니다. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| override [ToString](../../groupdocs.search.options/dateformat/tostring)() | 반환String 현재를 나타내는[`DateFormat`](../dateformat) . |

### 비고

**더 알아보기**

* [날짜 범위 검색](https://docs.groupdocs.com/display/searchnet/Date+range+search)

### 예

이 예제는 클래스의 일반적인 사용법을 보여줍니다.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "daterange(2017-01-01 ~~ 2019-12-31)";

Index index = new Index(indexFolder); // 지정된 폴더에 인덱스 생성
index.Add(documentsFolder); // 지정된 폴더에서 문서 인덱싱

SearchOptions options = new SearchOptions();
options.DateFormats.Clear(); // 기본 날짜 형식 제거
DateFormatElement[] elements = new DateFormatElement[]
{
    DateFormatElement.MonthTwoDigits,
    DateFormatElement.DateSeparator,
    DateFormatElement.DayOfMonthTwoDigits,
    DateFormatElement.DateSeparator,
    DateFormatElement.YearFourDigits,
};
// 날짜 형식 패턴 'MM/dd/yyyy' 생성
DateFormat dateFormat = new DateFormat(elements, "/");
options.DateFormats.Add(dateFormat);

SearchResult result = index.Search(query, options); // 인덱스에서 검색
```

### 또한보십시오

* 네임스페이스 [GroupDocs.Search.Options](../../groupdocs.search.options)
* 집회 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
