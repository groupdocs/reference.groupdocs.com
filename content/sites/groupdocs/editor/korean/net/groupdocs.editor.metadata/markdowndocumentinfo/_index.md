---
title: MarkdownDocumentInfo
second_title: .NET API 참조용 GroupDocs.Editor
description: 하나의 마크다운 문서 의 메타데이터를 나타냅니다.
type: docs
weight: 750
url: /ko/net/groupdocs.editor.metadata/markdowndocumentinfo/
---
## MarkdownDocumentInfo structure

하나의 마크다운 문서 의 메타데이터를 나타냅니다.

```csharp
public struct MarkdownDocumentInfo : IDocumentInfo, IEquatable<MarkdownDocumentInfo>
```

## 속성

| 이름 | 설명 |
| --- | --- |
| [Format](../../groupdocs.editor.metadata/markdowndocumentinfo/format) { get; } | 이 Markdown 문서의 형식을 반환합니다.[`Md`](../../groupdocs.editor.formats/textualformats/md) |
| [IsEncrypted](../../groupdocs.editor.metadata/markdowndocumentinfo/isencrypted) { get; } | 마크다운 문서는 암호로 암호화할 수 없기 때문에 이 속성은 항상 ``거짓` |
| [PageCount](../../groupdocs.editor.metadata/markdowndocumentinfo/pagecount) { get; } | 페이지 수를 반환합니다. Markdown 문서에는 일반적으로 고정된 페이지가 없으므로 페이지 수가 있으므로 이 숫자는 세로 방향에서 A4로 설정된 표준 페이지 크기에서 계산됩니다. |
| [Size](../../groupdocs.editor.metadata/markdowndocumentinfo/size) { get; } | 이 Markdown document 의 크기를 바이트 단위로 반환합니다. |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [Equals](../../groupdocs.editor.metadata/markdowndocumentinfo/equals#equals)(MarkdownDocumentInfo) | 이 인스턴스가 지정된 다른 인스턴스와 같은지 여부를 결정합니다.[`MarkdownDocumentInfo`](../markdowndocumentinfo) 인스턴스. |

### 또한보십시오

* interface [IDocumentInfo](../idocumentinfo)
* 네임스페이스 [GroupDocs.Editor.Metadata](../../groupdocs.editor.metadata)
* 집회 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
