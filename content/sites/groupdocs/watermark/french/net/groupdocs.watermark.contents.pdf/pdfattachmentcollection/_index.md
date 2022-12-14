---
title: PdfAttachmentCollection
second_title: Référence de l'API GroupDocs.Watermark pour .NET
description: Représente une collection de pièces jointes dans un document pdf.
type: docs
weight: 600
url: /fr/net/groupdocs.watermark.contents.pdf/pdfattachmentcollection/
---
## PdfAttachmentCollection class

Représente une collection de pièces jointes dans un document pdf.

```csharp
public class PdfAttachmentCollection : RemoveOnlyListBase<PdfAttachment>
```

## Propriétés

| Nom | La description |
| --- | --- |
| virtual [Count](../../groupdocs.watermark.common/readonlylistbase-1/count) { get; } | Obtient le nombre d'éléments contenus dans la collection. |
| override [IsReadOnly](../../groupdocs.watermark.common/removeonlylistbase-1/isreadonly) { get; } | Obtient une valeur indiquant si la collection est en lecture seule. |
| virtual [Item](../../groupdocs.watermark.common/readonlylistbase-1/item) { get; } | Obtient l'élément à l'index spécifié dans la collection. |

## Méthodes

| Nom | La description |
| --- | --- |
| [Add](../../groupdocs.watermark.contents.pdf/pdfattachmentcollection/add)(byte[], string, string) | Ajoute une pièce jointe au[`PdfContent`](../pdfcontent) . |
| [Clear](../../groupdocs.watermark.common/removeonlylistbase-1/clear)() |  |
| virtual [Contains](../../groupdocs.watermark.common/readonlylistbase-1/contains)(PdfAttachment) |  |
| virtual [GetEnumerator](../../groupdocs.watermark.common/readonlylistbase-1/getenumerator)() |  |
| virtual [IndexOf](../../groupdocs.watermark.common/readonlylistbase-1/indexof)(PdfAttachment) |  |
| [Remove](../../groupdocs.watermark.common/removeonlylistbase-1/remove)(PdfAttachment) |  |
| [RemoveAt](../../groupdocs.watermark.common/removeonlylistbase-1/removeat)(int) |  |

### Remarques

Cette collection contient les éléments de[`PdfAttachment`](../pdfattachment) tapez.

### Voir également

* class [RemoveOnlyListBase&lt;T&gt;](../../groupdocs.watermark.common/removeonlylistbase-1)
* class [PdfAttachment](../pdfattachment)
* espace de noms [GroupDocs.Watermark.Contents.Pdf](../../groupdocs.watermark.contents.pdf)
* Assemblée [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
