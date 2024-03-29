---
title: SpreadsheetWatermarkHeaderFooterOptions
second_title: GroupDocs.Watermark untuk Referensi .NET API
description: Mewakili opsi saat menambahkan watermark ke header/footer Spreadsheet.
type: docs
weight: 2200
url: /id/net/groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkheaderfooteroptions/
---
## SpreadsheetWatermarkHeaderFooterOptions class

Mewakili opsi saat menambahkan watermark ke header/footer Spreadsheet.

```csharp
public sealed class SpreadsheetWatermarkHeaderFooterOptions : SpreadsheetWatermarkOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [SpreadsheetWatermarkHeaderFooterOptions](spreadsheetwatermarkheaderfooteroptions)() | Menginisialisasi instance baru dari[`SpreadsheetWatermarkHeaderFooterOptions`](../spreadsheetwatermarkheaderfooteroptions) kelas. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [WorksheetIndex](../../groupdocs.watermark.options.spreadsheet/spreadsheetwatermarkheaderfooteroptions/worksheetindex) { get; set; } | Mendapat atau menyetel indeks lembar kerja untuk ditambahkan tanda air. |

### Perkataan

**Belajarlah lagi:**

* [Tambahkan watermark ke dokumen spreadsheet](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+spreadsheet+documents)

### Contoh

Tambahkan tanda air teks ke dalam header lembar kerja Excel.

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

### Lihat juga

* class [SpreadsheetWatermarkOptions](../spreadsheetwatermarkoptions)
* ruang nama [GroupDocs.Watermark.Options.Spreadsheet](../../groupdocs.watermark.options.spreadsheet)
* perakitan [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
