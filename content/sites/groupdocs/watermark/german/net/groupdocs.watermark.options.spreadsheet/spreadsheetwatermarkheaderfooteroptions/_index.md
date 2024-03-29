---
title: SpreadsheetWatermarkHeaderFooterOptions
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Repräsentiert Optionen beim Hinzufügen des Wasserzeichens zur Kopf/Fußzeile einer Tabelle.
type: docs
weight: 2200
url: /de/net/groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkheaderfooteroptions/
---
## SpreadsheetWatermarkHeaderFooterOptions class

Repräsentiert Optionen beim Hinzufügen des Wasserzeichens zur Kopf-/Fußzeile einer Tabelle.

```csharp
public sealed class SpreadsheetWatermarkHeaderFooterOptions : SpreadsheetWatermarkOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [SpreadsheetWatermarkHeaderFooterOptions](spreadsheetwatermarkheaderfooteroptions)() | Initialisiert eine neue Instanz von[`SpreadsheetWatermarkHeaderFooterOptions`](../spreadsheetwatermarkheaderfooteroptions) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [WorksheetIndex](../../groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkheaderfooteroptions/worksheetindex) { get; set; } | Ruft den Index des Arbeitsblatts ab oder legt ihn fest, dem das Wasserzeichen hinzugefügt werden soll. |

### Bemerkungen

**Erfahren Sie mehr:**

* [Fügen Sie Tabellendokumenten Wasserzeichen hinzu](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+spreadsheet+documents)

### Beispiele

Fügen Sie Textwasserzeichen in die Überschrift des Excel-Arbeitsblatts ein.

```csharp
SpreadsheetLoadOptions loadOptions = new SpreadsheetLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\test.xls", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test", new Font("Arial", 14));

    SpreadsheetWatermarkHeaderFooterOptions options = new SpreadsheetWatermarkHeaderFooterOptions();
    options.WorksheetIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Siehe auch

* class [SpreadsheetWatermarkOptions](../spreadsheetwatermarkoptions)
* namensraum [GroupDocs.Watermark.Options.Spreadsheet](../../groupdocs.watermark.options.spreadsheet)
* Montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
