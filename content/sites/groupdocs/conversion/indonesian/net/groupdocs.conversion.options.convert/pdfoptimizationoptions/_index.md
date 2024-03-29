---
title: PdfOptimizationOptions
second_title: GroupDocs.Konversi untuk Referensi .NET API
description: Menentukan opsi pengoptimalan Pdf.
type: docs
weight: 1780
url: /id/net/groupdocs.conversion.options.convert/pdfoptimizationoptions/
---
## PdfOptimizationOptions class

Menentukan opsi pengoptimalan Pdf.

```csharp
public sealed class PdfOptimizationOptions : ValueObject
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [PdfOptimizationOptions](pdfoptimizationoptions)() | Menginisialisasi instance baru[`PdfOptimizationOptions`](../pdfoptimizationoptions) kelas. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [CompressImages](../../groupdocs.conversion.options.convert/pdfoptimizationoptions/compressimages) { get; set; } | Jika CompressImages disetel ke`BENAR` , semua gambar dalam dokumen dikompres ulang. Kompresi ditentukan oleh properti ImageQuality. |
| [ImageQuality](../../groupdocs.conversion.options.convert/pdfoptimizationoptions/imagequality) { get; set; } | Nilai dalam persen dengan kualitas dan ukuran gambar 100% tidak berubah. Untuk memperkecil ukuran gambar, atur properti ini menjadi kurang dari 100 |
| [LinkDuplicateStreams](../../groupdocs.conversion.options.convert/pdfoptimizationoptions/linkduplicatestreams) { get; set; } | Tautkan aliran duplikat |
| [RemoveUnusedObjects](../../groupdocs.conversion.options.convert/pdfoptimizationoptions/removeunusedobjects) { get; set; } | Hapus objek yang tidak terpakai |
| [RemoveUnusedStreams](../../groupdocs.conversion.options.convert/pdfoptimizationoptions/removeunusedstreams) { get; set; } | Hapus aliran yang tidak digunakan |
| [UnembedFonts](../../groupdocs.conversion.options.convert/pdfoptimizationoptions/unembedfonts) { get; set; } | Membuat font tidak disematkan jika disetel ke true |

## Metode

| Nama | Keterangan |
| --- | --- |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Menentukan apakah dua instance objek sama. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Menentukan apakah dua instance objek sama. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Berfungsi sebagai fungsi hash default. |

### Lihat juga

* class [ValueObject](../../groupdocs.conversion.contracts/valueobject)
* ruang nama [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* perakitan [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
