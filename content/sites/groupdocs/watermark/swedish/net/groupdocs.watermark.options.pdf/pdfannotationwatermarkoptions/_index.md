---
title: PdfAnnotationWatermarkOptions
second_title: GroupDocs.Watermark for .NET API-referens
description: Representerar alternativ för att lägga till vattenstämplar när du lägger till anteckningsvattenstämpel i ett pdfdokument.
type: docs
weight: 1860
url: /sv/net/groupdocs.watermark.options.pdf/pdfannotationwatermarkoptions/
---
## PdfAnnotationWatermarkOptions class

Representerar alternativ för att lägga till vattenstämplar när du lägger till anteckningsvattenstämpel i ett pdf-dokument.

```csharp
public sealed class PdfAnnotationWatermarkOptions : PdfWatermarkOptions
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [PdfAnnotationWatermarkOptions](pdfannotationwatermarkoptions)() | Initierar en ny instans av[`PdfAnnotationWatermarkOptions`](../pdfannotationwatermarkoptions) class. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [PageIndex](../../groupdocs.watermark.options.pdf/pdfannotationwatermarkoptions/pageindex) { get; set; } | Hämtar eller ställer in sidindexet för att lägga till vattenstämpel. |
| [PrintOnly](../../groupdocs.watermark.options.pdf/pdfannotationwatermarkoptions/printonly) { get; set; } | Hämta eller ställer in värdet som anger om anteckningen kommer att skrivas ut, men inte visas i pdf-visningsprogrammet. |

### Anmärkningar

**Läs mer:**

* [Lägg till vattenstämplar i PDF-dokument](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+PDF+documents)

### Exempel

Lägg till en bildanteckningsvattenstämpel i ett PDF-dokument.

```csharp
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\test.pdf", loadOptions))
{
    using (ImageWatermark watermark = new ImageWatermark(@"D:\icon.png"))
    {
        PdfAnnotationWatermarkOptions options = new PdfAnnotationWatermarkOptions();
        options.PageIndex = -1; // default - alla sidor

        watermarker.Add(watermark, options);
    }

    watermarker.Save();
}
```

### Se även

* class [PdfWatermarkOptions](../pdfwatermarkoptions)
* namnutrymme [GroupDocs.Watermark.Options.Pdf](../../groupdocs.watermark.options.pdf)
* hopsättning [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
