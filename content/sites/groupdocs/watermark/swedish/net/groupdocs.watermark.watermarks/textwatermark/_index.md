---
title: TextWatermark
second_title: GroupDocs.Watermark for .NET API-referens
description: Representerar en textvattenstämpel.
type: docs
weight: 3160
url: /sv/net/groupdocs.watermark.watermarks/textwatermark/
---
## TextWatermark class

Representerar en textvattenstämpel.

```csharp
public class TextWatermark : Watermark
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [TextWatermark](textwatermark)(string, Font) | Initierar en ny instans av[`TextWatermark`](../textwatermark)klass med en specificerad text och ett typsnitt. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [BackgroundColor](../../groupdocs.watermark.watermarks/textwatermark/backgroundcolor) { get; set; } | Hämtar eller ställer in bakgrundsfärgen för texten. |
| [ConsiderParentMargins](../../groupdocs.watermark/watermark/considerparentmargins) { get; set; } | Hämtar eller ställer in ett värde som anger om vattenstämpelns storlek och koordinater beräknas med hänsyn till överordnade marginaler. |
| [Font](../../groupdocs.watermark.watermarks/textwatermark/font) { get; set; } | Hämtar eller ställer in teckensnittet för texten. |
| [ForegroundColor](../../groupdocs.watermark.watermarks/textwatermark/foregroundcolor) { get; set; } | Hämtar eller ställer in textens förgrundsfärg. |
| [Height](../../groupdocs.watermark/watermark/height) { get; set; } | Får eller ställer in önskad höjd på detta[`Watermark`](../../groupdocs.watermark/watermark) . |
| [HorizontalAlignment](../../groupdocs.watermark/watermark/horizontalalignment) { get; set; } | Hämtar eller ställer in den horisontella justeringen av detta[`Watermark`](../../groupdocs.watermark/watermark) . |
| [IsBackground](../../groupdocs.watermark/watermark/isbackground) { get; set; } | Hämtar eller ställer in ett värde som anger om vattenstämpeln ska placeras i bakgrunden. |
| [Margins](../../groupdocs.watermark/watermark/margins) { get; set; } | Hämtar eller ställer in marginalinställningarna för detta[`Watermark`](../../groupdocs.watermark/watermark) . |
| [Opacity](../../groupdocs.watermark/watermark/opacity) { get; set; } | Hämtar eller ställer in opaciteten för detta[`Watermark`](../../groupdocs.watermark/watermark) . |
| [Padding](../../groupdocs.watermark.watermarks/textwatermark/padding) { get; set; } | Hämtar eller ställer in utfyllnadsinställningarna för detta[`TextWatermark`](../textwatermark) . Den här egenskapen är endast tillämplig på bildfiler. |
| [RotateAngle](../../groupdocs.watermark/watermark/rotateangle) { get; set; } | Hämtar eller ställer in rotationsvinkeln för denna[`Watermark`](../../groupdocs.watermark/watermark) i grader. |
| [ScaleFactor](../../groupdocs.watermark/watermark/scalefactor) { get; set; } | Hämtar eller ställer in ett värde som definierar hur vattenstämpelns storlek beror på överordnad storlek. |
| [SizingType](../../groupdocs.watermark/watermark/sizingtype) { get; set; } | Hämtar eller ställer in ett värde som anger hur vattenstämpeln ska dimensioneras. |
| [Text](../../groupdocs.watermark.watermarks/textwatermark/text) { get; set; } | Hämtar eller ställer in texten som ska användas som vattenstämpel. |
| [TextAlignment](../../groupdocs.watermark.watermarks/textwatermark/textalignment) { get; set; } | Hämtar eller ställer in vattenstämpelns textjustering. |
| [VerticalAlignment](../../groupdocs.watermark/watermark/verticalalignment) { get; set; } | Hämtar eller ställer in den vertikala justeringen av detta[`Watermark`](../../groupdocs.watermark/watermark) . |
| [Width](../../groupdocs.watermark/watermark/width) { get; set; } | Hämtar eller ställer in önskad bredd på detta[`Watermark`](../../groupdocs.watermark/watermark) . |
| [X](../../groupdocs.watermark/watermark/x) { get; set; } | Hämtar eller ställer in x-koordinaten för detta[`Watermark`](../../groupdocs.watermark/watermark) . |
| [Y](../../groupdocs.watermark/watermark/y) { get; set; } | Hämtar eller ställer in y-koordinaten för detta[`Watermark`](../../groupdocs.watermark/watermark) . |

### Anmärkningar

**Läs mer:**

* [Lägga till textvattenstämplar](https://docs.groupdocs.com/display/watermarknet/Adding+text+watermarks)

### Exempel

Skala textens vattenstämpel beroende på överordnad storlek.

```csharp
foreach (string file in Directory.GetFiles("C:\\test"))
{
    using (Watermarker watermarker = new Watermarker(file))
    {
        TextWatermark watermark = new TextWatermark("test watermark", new Font("Arial", 36));
        watermark.HorizontalAlignment = HorizontalAlignment.Center;
        watermark.VerticalAlignment = VerticalAlignment.Center;
        watermark.SizingType = SizingType.ScaleToParentDimensions;
        watermark.RotateAngle = 45;
        watermark.ScaleFactor = 0.4;

        watermarker.Add(watermark);
        watermarker.Save();
    }
}
```

### Se även

* class [Watermark](../../groupdocs.watermark/watermark)
* namnutrymme [GroupDocs.Watermark.Watermarks](../../groupdocs.watermark.watermarks)
* hopsättning [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
