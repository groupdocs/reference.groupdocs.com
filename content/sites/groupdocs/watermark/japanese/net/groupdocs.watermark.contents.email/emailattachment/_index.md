---
title: EmailAttachment
second_title: GroupDocs.Watermark for .NET API リファレンス
description: 電子メール メッセージに添付されたファイルを表します
type: docs
weight: 290
url: /ja/net/groupdocs.watermark.contents.email/emailattachment/
---
## EmailAttachment class

電子メール メッセージに添付されたファイルを表します。

```csharp
public class EmailAttachment : EmailAttachmentBase
```

## プロパティ

| 名前 | 説明 |
| --- | --- |
| override [Content](../../groupdocs.watermark.contents.email/emailattachmentbase/content) { get; set; } | 添付ファイルの内容を取得または設定します。 |
| [ContentId](../../groupdocs.watermark.contents.email/emailattachmentbase/contentid) { get; } | このコンテンツ ID を取得します[`EmailAttachmentBase`](../emailattachmentbase). |
| [MediaType](../../groupdocs.watermark.contents.email/emailattachmentbase/mediatype) { get; } | このメディア タイプを取得します[`EmailAttachmentBase`](../emailattachmentbase). |
| [Name](../../groupdocs.watermark.contents.email/emailattachment/name) { get; set; } | 添付ファイルの名前を取得または設定します。 |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)() | 添付ファイルからコンテンツを読み込みます。 |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)(LoadOptions) | 指定されたロード オプションを使用して、添付ファイルからコンテンツをロードします。 |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)(LoadOptions, WatermarkerSettings) | 指定されたロード オプションと設定を使用して、添付ファイルからコンテンツをロードします。 |
| [GetDocumentInfo](../../groupdocs.watermark.common/attachment/getdocumentinfo)() | 添付ファイルに格納されているドキュメントに関する情報を取得します。 |

### 関連項目

* class [EmailAttachmentBase](../emailattachmentbase)
* 名前空間 [GroupDocs.Watermark.Contents.Email](../../groupdocs.watermark.contents.email)
* 組み立て [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
