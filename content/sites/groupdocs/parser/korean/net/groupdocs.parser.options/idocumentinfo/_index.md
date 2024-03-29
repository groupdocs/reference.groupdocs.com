---
title: IDocumentInfo
second_title: .NET API 참조용 GroupDocs.Parser
description: 문서 정보를 나타냅니다.
type: docs
weight: 430
url: /ko/net/groupdocs.parser.options/idocumentinfo/
---
## IDocumentInfo interface

문서 정보를 나타냅니다.

```csharp
public interface IDocumentInfo
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [FileType](../../groupdocs.parser.options/idocumentinfo/filetype) { get; } | 문서 유형을 가져옵니다. |
| [PageCount](../../groupdocs.parser.options/idocumentinfo/pagecount) { get; } | 총 문서 페이지 수를 가져옵니다. |
| [Pages](../../groupdocs.parser.options/idocumentinfo/pages) { get; } | 인덱스 및 페이지 크기와 같은 페이지에 대한 정보를 가져옵니다. |
| [RawPageCount](../../groupdocs.parser.options/idocumentinfo/rawpagecount) { get; } | 총 문서 원시 페이지 수를 가져옵니다. |
| [Size](../../groupdocs.parser.options/idocumentinfo/size) { get; } | 문서의 크기를 바이트 단위로 가져옵니다. |

### 비고

이 인터페이스를 구현하는 개체는 다음에 의해 반환됩니다.[`GetDocumentInfo`](../../groupdocs.parser/parser/getdocumentinfo) 방법. 사용 예를 참조하십시오. **더 알아보기:**

* [문서 정보 얻기](https://docs.groupdocs.com/display/parsernet/Get+document+info)
* [인코딩 감지](https://docs.groupdocs.com/display/parsernet/Detect+encoding)

### 또한보십시오

* 네임스페이스 [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* 집회 [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
