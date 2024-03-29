---
title: ImageSaveOptions
second_title: GroupDocs.Signature untuk Referensi .NET API
description: Menyimpan opsi untuk dokumen gambar.
type: docs
weight: 1400
url: /id/net/groupdocs.signature.options/imagesaveoptions/
---
## ImageSaveOptions class

Menyimpan opsi untuk dokumen gambar.

```csharp
public class ImageSaveOptions : SaveOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [ImageSaveOptions](imagesaveoptions#constructor)() | Menginisialisasi instance baru dari kelas ImagesSaveOptions dengan nilai default. |
| [ImageSaveOptions](imagesaveoptions#constructor_1)(bool) | Menginisialisasi instance baru dari kelas ImagesSaveOptions dengan tanda timpa. |
| [ImageSaveOptions](imagesaveoptions#constructor_2)(ImageSaveFileFormat, bool) | Menginisialisasi instance baru dari kelas ImagesSaveOptions dengan tipe output yang ditentukan dan menimpa flag. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Mendapat atau menyetel bendera untuk menambahkan ekstensi secara otomatis ketika tidak ada di jalur file keluaran Nilai default adalah false. |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | Mendapat atau mengatur format file dari dokumen yang ditandatangani. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Mendapat atau mengatur apakah akan menimpa file yang ada dengan file keluaran baru. Jika tidak, file baru akan dibuat dengan angka sebagai akhiran. Secara default nilai ini disetel ke true yang berarti file akan ditimpa. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | Mendapatkan atau menyetel kata sandi untuk menyimpan dokumen yang ditandatangani dengan proteksi kata sandi. Properti ini tidak didukung untuk dokumen Gambar. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | Mendapat atau menyetel apakah akan menggunakan kata sandi dari LoadOptions untuk menyimpan dokumen yang ditandatangani sebagai dilindungi. Nilai default adalah true. Properti ini tidak didukung untuk dokumen Gambar. |

### Lihat juga

* class [SaveOptions](../saveoptions)
* ruang nama [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* perakitan [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
