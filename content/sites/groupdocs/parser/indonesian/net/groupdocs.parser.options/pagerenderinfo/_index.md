---
title: PageRenderInfo
second_title: GroupDocs.Parser untuk Referensi .NET API
description: Mewakili informasi tentang bagaimana suatu halaman dirender.
type: docs
weight: 530
url: /id/net/groupdocs.parser.options/pagerenderinfo/
---
## PageRenderInfo class

Mewakili informasi tentang bagaimana suatu halaman dirender.

```csharp
public sealed class PageRenderInfo
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [PageRenderInfo](pagerenderinfo)(int, int, int) | Menginisialisasi instance baru dari[`PageRenderInfo`](../pagerenderinfo) kelas. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [ColumnCount](../../groupdocs.parser.options/pagerenderinfo/columncount) { get; } | Dapatkan jumlah total kolom petak. |
| [PageNumber](../../groupdocs.parser.options/pagerenderinfo/pagenumber) { get; } | Mendapat nomor halaman. |
| [RowCount](../../groupdocs.parser.options/pagerenderinfo/rowcount) { get; } | Dapatkan jumlah total baris petak. |

## Metode

| Nama | Keterangan |
| --- | --- |
| [GetColumn](../../groupdocs.parser.options/pagerenderinfo/getcolumn)(int) | Mengembalikan indeks kolom tempat ubin berada*tileIndex* ditempatkan. |
| [GetRow](../../groupdocs.parser.options/pagerenderinfo/getrow)(int) | Mengembalikan indeks baris tempat ubin berada*tileIndex* ditempatkan. |

### Perkataan

Beberapa dokumen (spreadsheet, misalnya) tidak mungkin merender halaman sebagai gambar tunggal. Untuk dokumen-dokumen itu, sebuah halaman dirender sebagai satu set petak. Ubin ini ditempatkan di meja persegi panjang.

[`RowCount`](./rowcount) Dan[`ColumnCount`](./columncount) mewakili jumlah baris dan kolom dari tabel ini. Jika halaman dokumen dirender menjadi gambar tunggal, properti ini sama dengan 1.

### Lihat juga

* ruang nama [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* perakitan [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
