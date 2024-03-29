---
title: TiffImageWatermarkOptions
second_title: GroupDocs.Watermark untuk Referensi .NET API
description: Mewakili opsi penambahan tanda air saat menambahkan tanda air ke gambar TIFF.
type: docs
weight: 1830
url: /id/net/groupdocs.watermark.options.image/tiffimagewatermarkoptions/
---
## TiffImageWatermarkOptions class

Mewakili opsi penambahan tanda air saat menambahkan tanda air ke gambar TIFF.

```csharp
public sealed class TiffImageWatermarkOptions : MultiframeImageWatermarkOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [TiffImageWatermarkOptions](tiffimagewatermarkoptions#constructor)() | Menginisialisasi instance baru dari[`TiffImageWatermarkOptions`](../tiffimagewatermarkoptions) kelas. |
| [TiffImageWatermarkOptions](tiffimagewatermarkoptions#constructor_1)(int) | Menginisialisasi instance baru dari[`TiffImageWatermarkOptions`](../tiffimagewatermarkoptions) class dengan indeks frame yang ditentukan. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [FrameIndex](../../groupdocs.watermark.options.image/multiframeimagewatermarkoptions/frameindex) { get; set; } | Mendapat atau menetapkan indeks bingkai untuk menambahkan watermark. |

### Perkataan

**Belajarlah lagi:**

* [Tambahkan tanda air ke gambar](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+images)

### Contoh

Tambahkan tanda air ke bingkai gambar TIFF tertentu.

```csharp
TiffImageLoadOptions loadOptions = new TiffImageLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\test.tiff", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test", new Font("Arial", 12));

    TiffImageWatermarkOptions options = new TiffImageWatermarkOptions();
    options.FrameIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Lihat juga

* class [MultiframeImageWatermarkOptions](../multiframeimagewatermarkoptions)
* ruang nama [GroupDocs.Watermark.Options.Image](../../groupdocs.watermark.options.image)
* perakitan [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
