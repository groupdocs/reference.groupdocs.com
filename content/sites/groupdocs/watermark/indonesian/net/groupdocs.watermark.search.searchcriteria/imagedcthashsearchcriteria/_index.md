---
title: ImageDctHashSearchCriteria
second_title: GroupDocs.Watermark untuk Referensi .NET API
description: Mewakili kriteria pencarian untuk menemukan gambar dalam dokumen.
type: docs
weight: 2590
url: /id/net/groupdocs.watermark.search.searchcriteria/imagedcthashsearchcriteria/
---
## ImageDctHashSearchCriteria class

Mewakili kriteria pencarian untuk menemukan gambar dalam dokumen.

```csharp
public class ImageDctHashSearchCriteria : ImageSearchCriteria
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [ImageDctHashSearchCriteria](imagedcthashsearchcriteria#constructor)(Stream) | Menginisialisasi instance baru dari[`ImageDctHashSearchCriteria`](../imagedcthashsearchcriteria) kelas dengan aliran tertentu. |
| [ImageDctHashSearchCriteria](imagedcthashsearchcriteria#constructor_1)(string) | Menginisialisasi instance baru dari[`ImageDctHashSearchCriteria`](../imagedcthashsearchcriteria) kelas dengan jalur file tertentu. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [MaxDifference](../../groupdocs.watermark.search.searchcriteria/imagesearchcriteria/maxdifference) { get; set; } | Mendapat atau menyetel perbedaan maksimum yang diizinkan di antara gambar. |

## Metode

| Nama | Keterangan |
| --- | --- |
| [And](../../groupdocs.watermark.search.searchcriteria/searchcriteria/and)(SearchCriteria) | Gabungkan ini[`SearchCriteria`](../searchcriteria) dengan kriteria lain menggunakan logika AND operator. |
| [Not](../../groupdocs.watermark.search.searchcriteria/searchcriteria/not)() | Meniadakan ini[`SearchCriteria`](../searchcriteria) . |
| [Or](../../groupdocs.watermark.search.searchcriteria/searchcriteria/or)(SearchCriteria) | Gabungkan ini[`SearchCriteria`](../searchcriteria) dengan kriteria lain menggunakan logika OR operator. |

### Perkataan

Kriteria pencarian ini menggunakan hash gambar perseptual berbasis DCT untuk menghitung kemiripan gambar. **Belajarlah lagi:**

* [Mencari tanda air](https://docs.groupdocs.com/display/watermarknet/Searching+watermarks)

### Contoh

Cari gambar dalam file terlampir (pdf).

```csharp
WatermarkerSettings settings = new WatermarkerSettings();
settings.SearchableObjects = new SearchableObjects
{
    PdfSearchableObjects = PdfSearchableObjects.All
};
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\test.pdf", loadOptions, settings))
{
    // Tentukan sampel gambar untuk dibandingkan dengan gambar dokumen
    ImageSearchCriteria criteria = new ImageDctHashSearchCriteria(@"D:\sample.png");
    // Cari gambar yang mirip
    PossibleWatermarkCollection possibleWatermarks = watermarker.Search(criteria);
    // Hapus atau modifikasi tanda air gambar yang ditemukan
    // ...
}
```

### Lihat juga

* class [ImageSearchCriteria](../imagesearchcriteria)
* ruang nama [GroupDocs.Watermark.Search.SearchCriteria](../../groupdocs.watermark.search.searchcriteria)
* perakitan [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
