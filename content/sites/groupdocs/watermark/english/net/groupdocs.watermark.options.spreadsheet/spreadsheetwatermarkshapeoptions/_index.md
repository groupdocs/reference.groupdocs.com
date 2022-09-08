---
title: SpreadsheetWatermarkShapeOptions
second_title: GroupDocs.Watermark for .NET API Reference
description: Represents options when adding shape watermark to a Spreadsheet worksheet.
type: docs
weight: 2230
url: /net/groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkshapeoptions/
---
## SpreadsheetWatermarkShapeOptions class

Represents options when adding shape watermark to a Spreadsheet worksheet.

```csharp
public sealed class SpreadsheetWatermarkShapeOptions : SpreadsheetWatermarkBaseOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [SpreadsheetWatermarkShapeOptions](spreadsheetwatermarkshapeoptions)() | Initializes a new instance of the [`SpreadsheetWatermarkShapeOptions`](../spreadsheetwatermarkshapeoptions) class. |

## Properties

| Name | Description |
| --- | --- |
| [AlternativeText](../../groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkbaseoptions/alternativetext) { get; set; } | Gets or sets the descriptive (alternative) text that will be associated with a shape. |
| [Effects](../../groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkshapeoptions/effects) { get; set; } | Gets or sets a value of [`SpreadsheetImageEffects`](../spreadsheetimageeffects) or [`SpreadsheetTextEffects`](../spreadsheettexteffects) for effects that should be applied to the watermark. |
| [IsLocked](../../groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkbaseoptions/islocked) { get; set; } | Gets or sets a value indicating whether an editing of the shape in Excel is forbidden. |
| [Name](../../groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkbaseoptions/name) { get; set; } | Gets or sets the name a shape. |
| [WorksheetIndex](../../groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkshapeoptions/worksheetindex) { get; set; } | Gets or sets the index of worksheet to add the watermark to. |

### Remarks

**Learn more:**

* [Add watermarks to spreadsheet documents](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+spreadsheet+documents)

### Examples

Add watermark to a particular worksheet of an Excel document.

```csharp
SpreadsheetLoadOptions loadOptions = new SpreadsheetLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\Documents\test.xls", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test watermark", new Font("Arial", 36, FontStyle.Bold | FontStyle.Italic));
    watermark.HorizontalAlignment = HorizontalAlignment.Center;
    watermark.VerticalAlignment = VerticalAlignment.Center;

    SpreadsheetWatermarkShapeOptions options = new SpreadsheetWatermarkShapeOptions();
    options.WorksheetIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### See Also

* class [SpreadsheetWatermarkBaseOptions](../spreadsheetwatermarkbaseoptions)
* namespace [GroupDocs.Watermark.Options.Spreadsheet](../../groupdocs.watermark.options.spreadsheet)
* assembly [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->