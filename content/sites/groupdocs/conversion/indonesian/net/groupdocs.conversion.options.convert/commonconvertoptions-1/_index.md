---
title: CommonConvertOptionsTFileType
second_title: GroupDocs.Konversi untuk Referensi .NET API
description: Kelas opsi konversi umum umum abstrak.
type: docs
weight: 1440
url: /id/net/groupdocs.conversion.options.convert/commonconvertoptions-1/
---
## CommonConvertOptions&lt;TFileType&gt; class

Kelas opsi konversi umum umum abstrak.

```csharp
public abstract class CommonConvertOptions<TFileType> : ConvertOptions<TFileType>, 
    IPagedConvertOptions, IPageRangedConvertOptions, IWatermarkedConvertOptions
    where TFileType : FileType
```

## Properti

| Nama | Keterangan |
| --- | --- |
| [Format](../../groupdocs.conversion.options.convert/convertoptions-1/format) { get; set; } | Jenis file yang diinginkan untuk konversi dokumen masukan. |
| virtual [Format](../../groupdocs.conversion.options.convert/convertoptions/format) { get; set; } | Jenis file yang diinginkan untuk konversi dokumen masukan. |
| [PageNumber](../../groupdocs.conversion.options.convert/commonconvertoptions-1/pagenumber) { get; set; } | Nomor halaman untuk memulai konversi. |
| [Pages](../../groupdocs.conversion.options.convert/commonconvertoptions-1/pages) { get; set; } | Daftar indeks halaman yang akan dikonversi. Harus ditentukan untuk mengonversi halaman tertentu. |
| [PagesCount](../../groupdocs.conversion.options.convert/commonconvertoptions-1/pagescount) { get; set; } | Jumlah halaman yang akan dikonversi mulai dari`Nomor halaman` . |
| [Watermark](../../groupdocs.conversion.options.convert/commonconvertoptions-1/watermark) { get; set; } | Opsi khusus tanda air |

## Metode

| Nama | Keterangan |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.convert/convertoptions/clone)() | Klon instance opsi saat ini. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Menentukan apakah dua instance objek sama. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Menentukan apakah dua instance objek sama. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Berfungsi sebagai fungsi hash default. |

### Lihat juga

* class [ConvertOptions&lt;TFileType&gt;](../convertoptions-1)
* interface [IPagedConvertOptions](../ipagedconvertoptions)
* interface [IPageRangedConvertOptions](../ipagerangedconvertoptions)
* interface [IWatermarkedConvertOptions](../iwatermarkedconvertoptions)
* class [FileType](../../groupdocs.conversion.filetypes/filetype)
* ruang nama [GroupDocs.Conversion.Options.Convert](../../groupdocs.conversion.options.convert)
* perakitan [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
