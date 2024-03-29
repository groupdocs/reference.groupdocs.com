---
title: PdfRecognitionMode
second_title: GroupDocs.Konversi untuk Referensi .NET API
description: Memungkinkan untuk mengontrol bagaimana dokumen PDF diubah menjadi dokumen pengolah kata.
type: docs
weight: 1820
url: /id/net/groupdocs.conversion.options.convert/pdfrecognitionmode/
---
## PdfRecognitionMode class

Memungkinkan untuk mengontrol bagaimana dokumen PDF diubah menjadi dokumen pengolah kata.

```csharp
public sealed class PdfRecognitionMode : Enumeration
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [PdfRecognitionMode](pdfrecognitionmode)() | Konstruktor serialisasi |

## Metode

| Nama | Keterangan |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | Membandingkan objek saat ini dengan yang lain. |
| virtual [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(Enumeration) | Menentukan apakah dua instance objek sama. |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | Menentukan apakah dua instance objek sama. |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | Berfungsi sebagai fungsi hash default. |
| override [ToString](../../groupdocs.conversion.contracts/enumeration/tostring)() | Mengembalikan string yang mewakili objek saat ini. |

## Bidang

| Nama | Keterangan |
| --- | --- |
| static readonly [Flow](../../groupdocs.conversion.options.convert/pdfrecognitionmode/flow) | Mode pengenalan penuh, mesin melakukan pengelompokan dan analisis multi-level untuk memulihkan maksud penulis dokumen asli dan menghasilkan dokumen yang dapat diedit secara maksimal. Sisi negatifnya adalah dokumen keluaran mungkin terlihat berbeda dari file PDF asli. |
| static readonly [Textbox](../../groupdocs.conversion.options.convert/pdfrecognitionmode/textbox) | Mode ini cepat dan bagus untuk mempertahankan tampilan asli file PDF secara maksimal, tetapi kemampuan mengedit dokumen yang dihasilkan dapat dibatasi. Setiap blok teks yang dikelompokkan secara visual dalam file PDF asli diubah menjadi kotak teks dalam dokumen yang dihasilkan. Ini mencapai kemiripan maksimal dokumen keluaran the dengan file PDF asli. Dokumen keluaran akan terlihat bagus, tetapi seluruhnya terdiri dari kotak teks dan dapat membuat pengeditan lebih lanjut dokumen di Microsoft Word cukup sulit. Ini adalah mode default. |

### Lihat juga

* class [Enumeration](../../groupdocs.conversion.contracts/enumeration)
* ruang nama [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* perakitan [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
