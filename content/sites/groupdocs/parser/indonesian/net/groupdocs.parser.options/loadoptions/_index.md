---
title: LoadOptions
second_title: GroupDocs.Parser untuk Referensi .NET API
description: Menyediakan opsi yang digunakan untuk membuka file.
type: docs
weight: 470
url: /id/net/groupdocs.parser.options/loadoptions/
---
## LoadOptions class

Menyediakan opsi yang digunakan untuk membuka file.

```csharp
public sealed class LoadOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [LoadOptions](loadoptions#constructor)() | Menginisialisasi instance baru dari[`LoadOptions`](../loadoptions) kelas dengan kosong[`Password`](./password) ,[`FileFormat`](./fileformat) sama denganUnknown dan penyandian default. |
| [LoadOptions](loadoptions#constructor_1)(FileFormat) | Menginisialisasi instance baru dari[`LoadOptions`](../loadoptions) class dengan kosong[`Password`](./password)dan penyandian default. |
| [LoadOptions](loadoptions#constructor_4)(string) | Menginisialisasi instance baru dari[`LoadOptions`](../loadoptions) kelas dengan[`FileFormat`](./fileformat) sama denganUnknown dan penyandian default. |
| [LoadOptions](loadoptions#constructor_2)(FileFormat, string) | Menginisialisasi instance baru dari[`LoadOptions`](../loadoptions) kelas dengan kata sandi dan penyandian default. |
| [LoadOptions](loadoptions#constructor_3)(FileFormat, string, Encoding, Encoding) | Menginisialisasi instance baru dari[`LoadOptions`](../loadoptions) kelas dengan penyandian khusus. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [DefaultAnsiEncoding](../../groupdocs.parser.options/loadoptions/defaultansiencoding) { get; } | Mendapat pengkodean ANSI default yang digunakan untuk deteksi pengkodean. |
| [Encoding](../../groupdocs.parser.options/loadoptions/encoding) { get; } | Mendapat penyandian dokumen. |
| [FileFormat](../../groupdocs.parser.options/loadoptions/fileformat) { get; } | Mendapatkan format file. |
| [Password](../../groupdocs.parser.options/loadoptions/password) { get; } | Mendapatkan kata sandi. |

### Perkataan

Instance dari kelas ini digunakan sebagai parameter di[`Parser`](../../groupdocs.parser/parser) konstruktor kelas:

* [`Parser`](../../groupdocs.parser/parser/parser)
* [`Parser`](../../groupdocs.parser/parser/parser)

Lihat contoh penggunaan di sana.

**Belajarlah lagi:**

* [Memuat format file tertentu](https://docs.groupdocs.com/display/parsernet/Loading+specific+file+formats)
* [Memuat dokumen yang dilindungi kata sandi](https://docs.groupdocs.com/display/parsernet/Password-protected+documents)

### Lihat juga

* ruang nama [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* perakitan [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
