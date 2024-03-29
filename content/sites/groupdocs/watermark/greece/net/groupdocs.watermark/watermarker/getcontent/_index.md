---
title: GetContent
second_title: GroupDocs.Watermark για Αναφορά API .NET
description: Επιστρέφει τοContentgroupdocs.watermark.contents/content αντικείμενο για το φορτωμένο έγγραφο.
type: docs
weight: 60
url: /el/net/groupdocs.watermark/watermarker/getcontent/
---
## Watermarker.GetContent&lt;T&gt; method

Επιστρέφει το[`Content`](../../../groupdocs.watermark.contents/content) αντικείμενο για το φορτωμένο έγγραφο.

```csharp
public T GetContent<T>()
    where T : Content
```

| Παράμετρος | Περιγραφή |
| --- | --- |
| T | Ο ζητούμενος τύπος του α[`Content`](../../../groupdocs.watermark.contents/content) αντικείμενο. |

### Επιστρεφόμενη Αξία

ο[`Content`](../../../groupdocs.watermark.contents/content) αντικείμενο για το φορτωμένο έγγραφο.

### Παραδείγματα

Ραστεροποίηση σελίδας εγγράφου pdf με πρόσθετο υδατογράφημα.

```csharp
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\doc.pdf", loadOptions))
{ 
    using (ImageWatermark watermark = new ImageWatermark(@"C:\watermark.png"))
    {
        watermarker.Add(watermark);
    }

    PdfContent content = watermarker.GetContent<PdfContent>();
    content.Rasterize(300, 300, PdfImageConversionFormat.Png);

    watermarker.Save();
}
```

### Δείτε επίσης

* class [Content](../../../groupdocs.watermark.contents/content)
* class [Watermarker](../../watermarker)
* χώρος ονομάτων [GroupDocs.Watermark](../../watermarker)
* συνέλευση [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
