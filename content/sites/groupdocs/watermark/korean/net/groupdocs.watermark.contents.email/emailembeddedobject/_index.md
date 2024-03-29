---
title: EmailEmbeddedObject
second_title: .NET API 참조용 GroupDocs.Watermark
description: 전자 메일 메시지 본문에 포함된 개체를 나타냅니다.
type: docs
weight: 340
url: /ko/net/groupdocs.watermark.contents.email/emailembeddedobject/
---
## EmailEmbeddedObject class

전자 메일 메시지 본문에 포함된 개체를 나타냅니다.

```csharp
public class EmailEmbeddedObject : EmailAttachmentBase
```

## 속성

| 이름 | 설명 |
| --- | --- |
| override [Content](../../groupdocs.watermark.contents.email/emailattachmentbase/content) { get; set; } | 첨부파일 내용을 가져오거나 설정합니다. |
| [ContentId](../../groupdocs.watermark.contents.email/emailattachmentbase/contentid) { get; } | 이것의 콘텐츠 ID를 가져옵니다.[`EmailAttachmentBase`](../emailattachmentbase) . |
| [MediaType](../../groupdocs.watermark.contents.email/emailattachmentbase/mediatype) { get; } | 이 미디어 유형을 가져옵니다.[`EmailAttachmentBase`](../emailattachmentbase) . |

## 행동 양식

| 이름 | 설명 |
| --- | --- |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)() | 첨부파일에서 컨텐츠를 불러옵니다. |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)(LoadOptions) | 지정된 로드 옵션으로 첨부 파일에서 콘텐츠를 로드합니다. |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)(LoadOptions, WatermarkerSettings) | 지정된 로드 옵션 및 설정으로 첨부 파일에서 콘텐츠를 로드합니다. |
| [GetDocumentInfo](../../groupdocs.watermark.common/attachment/getdocumentinfo)() | 첨부파일에 저장된 문서의 정보를 가져옵니다. |

### 또한보십시오

* class [EmailAttachmentBase](../emailattachmentbase)
* 네임스페이스 [GroupDocs.Watermark.Contents.Email](../../groupdocs.watermark.contents.email)
* 집회 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
