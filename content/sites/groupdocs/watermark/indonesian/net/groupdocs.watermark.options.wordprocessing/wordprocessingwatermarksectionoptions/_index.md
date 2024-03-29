---
title: WordProcessingWatermarkSectionOptions
second_title: GroupDocs.Watermark untuk Referensi .NET API
description: Mewakili opsi saat menambahkan tanda air bentuk ke bagian dokumen Word.
type: docs
weight: 2380
url: /id/net/groupdocs.watermark.options.wordprocessing/wordprocessingwatermarksectionoptions/
---
## WordProcessingWatermarkSectionOptions class

Mewakili opsi saat menambahkan tanda air bentuk ke bagian dokumen Word.

```csharp
public sealed class WordProcessingWatermarkSectionOptions : WordProcessingWatermarkBaseOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [WordProcessingWatermarkSectionOptions](wordprocessingwatermarksectionoptions)() | Menginisialisasi instance baru dari[`WordProcessingWatermarkSectionOptions`](../wordprocessingwatermarksectionoptions) kelas. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [AlternativeText](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/alternativetext) { get; set; } | Mendapatkan atau menyetel teks deskriptif (alternatif) yang akan dikaitkan dengan bentuk. |
| [Effects](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/effects) { get; set; } | Mendapat atau menetapkan nilai[`WordProcessingImageEffects`](../wordprocessingimageeffects) or [`WordProcessingTextEffects`](../wordprocessingtexteffects) untuk efek yang harus diterapkan pada watermark. |
| [IsLocked](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/islocked) { get; set; } | Mendapat atau menetapkan nilai yang menunjukkan apakah pengeditan bentuk di Word dilarang. |
| [LockType](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/locktype) { get; set; } | Mendapat atau menyetel jenis kunci tanda air. |
| [Name](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/name) { get; set; } | Mendapatkan atau menyetel nama menjadi bentuk. |
| [Password](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/password) { get; set; } | Mendapatkan atau menyetel kata sandi yang digunakan untuk mengunci tanda air. |
| [SectionIndex](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarksectionoptions/sectionindex) { get; set; } | Mendapat atau menyetel indeks bagian untuk ditambahkan watermark. |

### Perkataan

**Belajarlah lagi:**

* [Tambahkan watermark ke dokumen pengolah kata](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+word+processing+documents)

### Contoh

Tambahkan watermark ke bagian tertentu dari dokumen Word.

```csharp
WordProcessingLoadOptions loadOptions = new WordProcessingLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\Documents\test.doc", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test watermark", new Font("Arial", 36, FontStyle.Bold | FontStyle.Italic));
    watermark.HorizontalAlignment = HorizontalAlignment.Center;
    watermark.VerticalAlignment = VerticalAlignment.Center;
    watermark.ForegroundColor = Color.Red;

    WordProcessingWatermarkSectionOptions options = new WordProcessingWatermarkSectionOptions();
    options.SectionIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Lihat juga

* class [WordProcessingWatermarkBaseOptions](../wordprocessingwatermarkbaseoptions)
* ruang nama [GroupDocs.Watermark.Options.WordProcessing](../../groupdocs.watermark.options.wordprocessing)
* perakitan [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
