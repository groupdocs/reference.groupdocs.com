---
title: ImageSearchOptions
second_title: GroupDocs.Signature untuk Referensi .NET API
description: Mewakili opsi pencarian untuk Tanda tangan gambar.
type: docs
weight: 1410
url: /id/net/groupdocs.signature.options/imagesearchoptions/
---
## ImageSearchOptions class

Mewakili opsi pencarian untuk Tanda tangan gambar.

```csharp
public class ImageSearchOptions : SearchOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [ImageSearchOptions](imagesearchoptions)() | Menginisialisasi instance baru dari kelas ImageSearchOptions dengan nilai default. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/searchoptions/allpages) { get; set; } | Tandai untuk mencari di setiap halaman Dokumen. Secara default nilai ini disetel ke true. |
| [MaxContentSize](../../groupdocs.signature.options/imagesearchoptions/maxcontentsize) { get; set; } | Untuk nilai bukan nol, flag ini menentukan ukuran maksimum gambar untuk kriteria pencarian. Secara default, flag ini disetel ke nol dan tidak memengaruhi hasil pencarian. |
| [MinContentSize](../../groupdocs.signature.options/imagesearchoptions/mincontentsize) { get; set; } | Untuk nilai bukan nol, flag ini menentukan ukuran minimal gambar untuk kriteria pencarian. Secara default, flag ini disetel ke nol dan tidak memengaruhi hasil pencarian. |
| [PageNumber](../../groupdocs.signature.options/searchoptions/pagenumber) { get; set; } | Mendapat atau menyetel nomor halaman Dokumen untuk pencarian. Nilai bersifat opsional. |
| [PagesSetup](../../groupdocs.signature.options/searchoptions/pagessetup) { get; set; } | Opsi untuk menentukan halaman untuk pencarian Tanda Tangan. |
| [ReturnContent](../../groupdocs.signature.options/imagesearchoptions/returncontent) { get; set; } | Mendapat atau menyetel flag untuk mengambil konten gambar tanda tangan pada halaman dokumen. Jika flag ini disetel true, konten tanda tangan gambar akan menyimpan data gambar mentah dengan format yang diperlukan[`ReturnContentType`](./returncontenttype) . Secara default opsi ini dinonaktifkan. |
| [ReturnContentType](../../groupdocs.signature.options/imagesearchoptions/returncontenttype) { get; set; } | Menentukan jenis file konten yang dikembalikan dari tanda tangan gambar saat properti ReturnContent diaktifkan. Secara default diatur ke Null. Itu berarti mengembalikan konten gambar dalam format aslinya. Format gambar ini ditentukan di[`Format`](../../groupdocs.signature.domain/imagesignature/format) Kemungkinan nilai yang didukung adalah: FileType.JPEG, FileType.PNG, FileType.BMP. Jika format yang diberikan tidak didukung maka konten gambar dalam format aslinya akan dikembalikan. |
| [SkipExternal](../../groupdocs.signature.options/searchoptions/skipexternal) { get; set; } | Tandai untuk mengembalikan hanya tanda tangan yang ditandai sebagai IsSignature. Secara default nilai salah yang menunjukkan untuk mengembalikan semua tanda tangan yang cocok dengan kriteria yang ditentukan. |

### Perkataan

**Belajarlah lagi**

* Penggunaan dasar pencarian tanda tangan elektronik Gambar oleh GroupDocs.Signature: [ Cara eSearch Tanda tangan gambar dalam dokumen](https://docs.groupdocs.com/display/signaturenet/Search+for+Image+e-signatures)
* Penggunaan lanjutan pengaturan penelusuran untuk tanda tangan elektronik Gambar dengan GroupDocs.Signature: [Penggunaan lanjutan tanda tangan Gambar eSearch dalam dokumen dan pengaturan tambahan](https://docs.groupdocs.com/display/signaturenet/Advanced+search+for+Image+signatures)

### Lihat juga

* class [SearchOptions](../searchoptions)
* ruang nama [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* perakitan [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
