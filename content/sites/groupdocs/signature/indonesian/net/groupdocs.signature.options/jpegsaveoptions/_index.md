---
title: JpegSaveOptions
second_title: GroupDocs.Signature untuk Referensi .NET API
description: Opsi Simpan Jpeg untuk dokumen gambar.
type: docs
weight: 1460
url: /id/net/groupdocs.signature.options/jpegsaveoptions/
---
## JpegSaveOptions class

Opsi Simpan Jpeg untuk dokumen gambar.

```csharp
public sealed class JpegSaveOptions : ImageSaveOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [JpegSaveOptions](jpegsaveoptions)() | Membuat JpegSaveOptions dengan nilai default. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Mendapat atau menyetel bendera untuk menambahkan ekstensi secara otomatis ketika tidak ada di jalur file keluaran Nilai default adalah false. |
| [BitsPerChannel](../../groupdocs.signature.options/jpegsaveoptions/bitsperchannel) { get; set; } | Mendapat atau menyetel bit per saluran untuk gambar jpeg lossless. Sekarang kami mendukung dari 2 hingga 8 bit per saluran. |
| [ColorType](../../groupdocs.signature.options/jpegsaveoptions/colortype) { get; set; } | Mendapat atau mengatur jenis warna untuk gambar jpeg. |
| [Comment](../../groupdocs.signature.options/jpegsaveoptions/comment) { get; set; } | Mendapat atau menyetel komentar file jpeg. |
| [CompressionType](../../groupdocs.signature.options/jpegsaveoptions/compressiontype) { get; set; } | Mendapat atau menyetel jenis kompresi. |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | Mendapat atau mengatur format file dari dokumen yang ditandatangani. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Mendapat atau mengatur apakah akan menimpa file yang ada dengan file keluaran baru. Jika tidak, file baru akan dibuat dengan angka sebagai akhiran. Secara default nilai ini disetel ke true yang berarti file akan ditimpa. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | Mendapatkan atau menyetel kata sandi untuk menyimpan dokumen yang ditandatangani dengan proteksi kata sandi. Properti ini tidak didukung untuk dokumen Gambar. |
| [Quality](../../groupdocs.signature.options/jpegsaveoptions/quality) { get; set; } | Mendapat atau menyetel kualitas gambar. |
| [SampleRoundingMode](../../groupdocs.signature.options/jpegsaveoptions/sampleroundingmode) { get; set; } | Mendapatkan atau menyetel mode pembulatan sampel agar sesuai dengan nilai 8-bit ke nilai n-bit JpegOptions.BitsPerChannel. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | Mendapat atau menyetel apakah akan menggunakan kata sandi dari LoadOptions untuk menyimpan dokumen yang ditandatangani sebagai dilindungi. Nilai default adalah true. Properti ini tidak didukung untuk dokumen Gambar. |

### Lihat juga

* class [ImageSaveOptions](../imagesaveoptions)
* ruang nama [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* perakitan [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
