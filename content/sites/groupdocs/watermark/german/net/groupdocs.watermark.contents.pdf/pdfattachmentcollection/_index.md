---
title: PdfAttachmentCollection
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Stellt eine Sammlung von Anhängen in einem PDFDokument dar.
type: docs
weight: 600
url: /de/net/groupdocs.watermark.contents.pdf/pdfattachmentcollection/
---
## PdfAttachmentCollection class

Stellt eine Sammlung von Anhängen in einem PDF-Dokument dar.

```csharp
public class PdfAttachmentCollection : RemoveOnlyListBase<PdfAttachment>
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| virtual [Count](../../groupdocs.watermark.common/readonlylistbase-1/count) { get; } | Ruft die Anzahl der in der Sammlung enthaltenen Elemente ab. |
| override [IsReadOnly](../../groupdocs.watermark.common/removeonlylistbase-1/isreadonly) { get; } | Ruft einen Wert ab, der angibt, ob die Sammlung schreibgeschützt ist. |
| virtual [Item](../../groupdocs.watermark.common/readonlylistbase-1/item) { get; } | Ruft das Element am angegebenen Index in der Sammlung ab. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [Add](../../groupdocs.watermark.contents.pdf/pdfattachmentcollection/add)(byte[], string, string) | Fügt einen Anhang hinzu[`PdfContent`](../pdfcontent) . |
| [Clear](../../groupdocs.watermark.common/removeonlylistbase-1/clear)() |  |
| virtual [Contains](../../groupdocs.watermark.common/readonlylistbase-1/contains)(PdfAttachment) |  |
| virtual [GetEnumerator](../../groupdocs.watermark.common/readonlylistbase-1/getenumerator)() |  |
| virtual [IndexOf](../../groupdocs.watermark.common/readonlylistbase-1/indexof)(PdfAttachment) |  |
| [Remove](../../groupdocs.watermark.common/removeonlylistbase-1/remove)(PdfAttachment) |  |
| [RemoveAt](../../groupdocs.watermark.common/removeonlylistbase-1/removeat)(int) |  |

### Bemerkungen

Diese Sammlung enthält die Artikel von[`PdfAttachment`](../pdfattachment) Typ.

### Siehe auch

* class [RemoveOnlyListBase&lt;T&gt;](../../groupdocs.watermark.common/removeonlylistbase-1)
* class [PdfAttachment](../pdfattachment)
* namensraum [GroupDocs.Watermark.Contents.Pdf](../../groupdocs.watermark.contents.pdf)
* Montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->