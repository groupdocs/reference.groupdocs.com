---
title: PreviewOptions
second_title: GroupDocs.Merger untuk Referensi .NET API
description: Mewakili opsi pratinjau dokumen.
type: docs
weight: 530
url: /id/net/groupdocs.merger.domain.options/previewoptions/
---
## PreviewOptions class

Mewakili opsi pratinjau dokumen.

```csharp
public class PreviewOptions : PageOptions, IPreviewOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [PreviewOptions](previewoptions#constructor_4)(CreatePageStream, PreviewMode) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |
| [PreviewOptions](previewoptions#constructor_7)(CreatePageStream, PreviewMode, int[]) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |
| [PreviewOptions](previewoptions#constructor)(CreatePageStream, ReleasePageStream, PreviewMode) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |
| [PreviewOptions](previewoptions#constructor_5)(CreatePageStream, PreviewMode, int, int) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |
| [PreviewOptions](previewoptions#constructor_3)(CreatePageStream, ReleasePageStream, PreviewMode, int[]) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |
| [PreviewOptions](previewoptions#constructor_6)(CreatePageStream, PreviewMode, int, int, RangeMode) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |
| [PreviewOptions](previewoptions#constructor_1)(CreatePageStream, ReleasePageStream, PreviewMode, int, int) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |
| [PreviewOptions](previewoptions#constructor_2)(CreatePageStream, ReleasePageStream, PreviewMode, int, int, RangeMode) | Menginisialisasi instance baru dari[`PreviewOptions`](../previewoptions) kelas. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [CreateStream](../../groupdocs.merger.domain.options/previewoptions/createstream) { get; } | Delegasi yang menentukan metode untuk membuat aliran pratinjau halaman keluaran. |
| [Height](../../groupdocs.merger.domain.options/previewoptions/height) { get; set; } | Tinggi pratinjau. |
| [Mode](../../groupdocs.merger.domain.options/previewoptions/mode) { get; } | Mode untuk pratinjau. |
| [Pages](../../groupdocs.merger.domain.options/pageoptions/pages) { get; } | Dapatkan koleksi nomor halaman. |
| [ReleaseStream](../../groupdocs.merger.domain.options/previewoptions/releasestream) { get; } | Delegasi yang menentukan metode untuk merilis aliran pratinjau halaman keluaran. |
| [Width](../../groupdocs.merger.domain.options/previewoptions/width) { get; set; } | Lebar pratinjau. |

## Metode

| Nama | Keterangan |
| --- | --- |
| [GetPathByPageNumber](../../groupdocs.merger.domain.options/previewoptions/getpathbypagenumber)(int, string) | Mendapatkan jalur file lengkap dari dokumen yang dipratinjau berdasarkan nomor halaman dengan ekstensi yang ditentukan. |
| [Validate](../../groupdocs.merger.domain.options/previewoptions/validate)(FileType) | Memvalidasi opsi pratinjau. |

### Lihat juga

* class [PageOptions](../pageoptions)
* interface [IPreviewOptions](../ipreviewoptions)
* ruang nama [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* perakitan [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
