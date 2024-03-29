---
title: ExtractText
second_title: .NET API 참조용 GroupDocs.Parser
description: 문서에서 텍스트를 추출합니다.TocItemgroupdocs.parser.data/tocitem 개체가 참조합니다.
type: docs
weight: 50
url: /ko/net/groupdocs.parser.data/tocitem/extracttext/
---
## TocItem.ExtractText method

문서에서 텍스트를 추출합니다.[`TocItem`](../../tocitem) 개체가 참조합니다.

```csharp
public virtual TextReader ExtractText()
```

### 반환 값

인스턴스TextReader 추출된 텍스트가 있는 클래스.

### 예

다음 예는 목차 항목별로 텍스트를 추출하는 방법입니다.

```csharp
// Parser 클래스의 인스턴스 생성
using (Parser parser = new Parser(Constants.SampleDocxWithToc))
{
    // 목차 가져오기
    IEnumerable<TocItem> tocItems = parser.GetToc();
    // toc 추출 지원 여부 확인
    if (tocItems == null)
    {
        Console.WriteLine("Table of contents extraction isn't supported");
    }
    // 항목 반복
    foreach (TocItem tocItem in tocItems)
    {
        // 장의 텍스트를 인쇄합니다.
        using (TextReader reader = tocItem.ExtractText())
        {
            Console.WriteLine("----");
            Console.WriteLine(reader.ReadToEnd());
        }
    }
}
```

### 또한보십시오

* class [TocItem](../../tocitem)
* 네임스페이스 [GroupDocs.Parser.Data](../../tocitem)
* 집회 [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
