---
title: EmailEmbeddedObject
second_title: GroupDocs.Watermark for .NET API Reference
description: Represents an object embedded to an email message body.
type: docs
weight: 340
url: /net/groupdocs.watermark.contents.email/emailembeddedobject/
---
## EmailEmbeddedObject class

Represents an object embedded to an email message body.

```csharp
public class EmailEmbeddedObject : EmailAttachmentBase
```

## Properties

| Name | Description |
| --- | --- |
| override [Content](../../groupdocs.watermark.contents.email/emailattachmentbase/content) { get; set; } | Gets or sets the attached file content. |
| [ContentId](../../groupdocs.watermark.contents.email/emailattachmentbase/contentid) { get; } | Gets the content id of this [`EmailAttachmentBase`](../emailattachmentbase). |
| [MediaType](../../groupdocs.watermark.contents.email/emailattachmentbase/mediatype) { get; } | Gets the media type of this [`EmailAttachmentBase`](../emailattachmentbase). |

## Methods

| Name | Description |
| --- | --- |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)() | Loads a content from the attached file. |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)(LoadOptions) | Loads a content from the attached file with the specified load options. |
| [CreateWatermarker](../../groupdocs.watermark.common/attachment/createwatermarker)(LoadOptions, WatermarkerSettings) | Loads a content from the attached file with the specified load options and settings. |
| [GetDocumentInfo](../../groupdocs.watermark.common/attachment/getdocumentinfo)() | Gets the information about a document stored in the attached file. |

### See Also

* class [EmailAttachmentBase](../emailattachmentbase)
* namespace [GroupDocs.Watermark.Contents.Email](../../groupdocs.watermark.contents.email)
* assembly [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->
