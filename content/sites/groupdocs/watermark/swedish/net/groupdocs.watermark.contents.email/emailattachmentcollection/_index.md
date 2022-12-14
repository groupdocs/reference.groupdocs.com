---
title: EmailAttachmentCollection
second_title: GroupDocs.Watermark for .NET API-referens
description: Representerar en samling bilagor i ett epostmeddelande.
type: docs
weight: 310
url: /sv/net/groupdocs.watermark.contents.email/emailattachmentcollection/
---
## EmailAttachmentCollection class

Representerar en samling bilagor i ett e-postmeddelande.

```csharp
public class EmailAttachmentCollection : RemoveOnlyListBase<EmailAttachment>
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| virtual [Count](../../groupdocs.watermark.common/readonlylistbase-1/count) { get; } | Hämtar antalet element som finns i samlingen. |
| override [IsReadOnly](../../groupdocs.watermark.common/removeonlylistbase-1/isreadonly) { get; } | Får ett värde som indikerar om samlingen är skrivskyddad. |
| virtual [Item](../../groupdocs.watermark.common/readonlylistbase-1/item) { get; } | Hämtar elementet vid angivet index i samlingen. |

## Metoder

| namn | Beskrivning |
| --- | --- |
| [Add](../../groupdocs.watermark.contents.email/emailattachmentcollection/add)(byte[], string) | Lägger till en bilaga till[`EmailContent`](../emailcontent) . |
| [Clear](../../groupdocs.watermark.common/removeonlylistbase-1/clear)() |  |
| virtual [Contains](../../groupdocs.watermark.common/readonlylistbase-1/contains)(EmailAttachment) |  |
| virtual [GetEnumerator](../../groupdocs.watermark.common/readonlylistbase-1/getenumerator)() |  |
| virtual [IndexOf](../../groupdocs.watermark.common/readonlylistbase-1/indexof)(EmailAttachment) |  |
| [Remove](../../groupdocs.watermark.common/removeonlylistbase-1/remove)(EmailAttachment) |  |
| [RemoveAt](../../groupdocs.watermark.common/removeonlylistbase-1/removeat)(int) |  |

### Anmärkningar

Den här samlingen innehåller föremål från[`EmailAttachment`](../emailattachment) typ.

### Se även

* class [RemoveOnlyListBase&lt;T&gt;](../../groupdocs.watermark.common/removeonlylistbase-1)
* class [EmailAttachment](../emailattachment)
* namnutrymme [GroupDocs.Watermark.Contents.Email](../../groupdocs.watermark.contents.email)
* hopsättning [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
