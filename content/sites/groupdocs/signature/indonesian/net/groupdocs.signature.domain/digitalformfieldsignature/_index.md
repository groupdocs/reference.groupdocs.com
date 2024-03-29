---
title: DigitalFormFieldSignature
second_title: GroupDocs.Signature untuk Referensi .NET API
description: Berisi properti kolom formulir input tanda tangan digital untuk Dokumen Pdf.
type: docs
weight: 140
url: /id/net/groupdocs.signature.domain/digitalformfieldsignature/
---
## DigitalFormFieldSignature class

Berisi properti kolom formulir input tanda tangan digital untuk Dokumen Pdf.

```csharp
public sealed class DigitalFormFieldSignature : FormFieldSignature
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [DigitalFormFieldSignature](digitalformfieldsignature)(string) | Membuat PdfDigitalFormFieldSignature dengan nama yang telah ditentukan. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | Dapatkan atau tetapkan tanggal pembuatan tanda tangan. |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | Dapatkan bendera yang menunjukkan jika tanda tangan ini telah dihapus dari dokumen. Properti ini hanya digunakan untuk catatan log riwayat dokumen untuk menyimpan daftar tanda tangan yang dihapus. |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | Menentukan ketinggian tanda tangan. |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | Dapatkan atau setel tanda untuk menunjukkan apakah komponen ini adalah Tanda Tangan atau konten dokumen. Properti ini digunakan dengan metode Pembaruan untuk menetapkan elemen sebagai tanda tangan (benar) atau elemen dokumen (salah). |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | Menentukan posisi tanda tangan kiri. |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | Dapatkan atau tetapkan tanggal modifikasi tanda tangan. |
| [Name](../../groupdocs.signature.domain/formfieldsignature/name) { get; set; } | Menentukan nama bidang formulir yang unik. |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | Menentukan tanda tangan halaman ditemukan di. |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | Pengidentifikasi tanda tangan unik untuk mengubah tanda tangan dalam dokumen melalui metode Perbarui atau Hapus. Properti ini akan disetel secara otomatis setelah metode Tanda Tangan atau Cari dipanggil. Jika properti ini disimpan sebelum dapat disetel secara manual untuk memanipulasi tanda tangan. |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | Menentukan jenis tanda tangan. |
| [Signed](../../groupdocs.signature.domain/digitalformfieldsignature/signed) { get; } | Properti hanya baca yang menunjukkan jika Tanda Tangan Bidang Formulir ditandatangani dengan sertifikat digital. |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | Menentukan posisi teratas tanda tangan. |
| [Type](../../groupdocs.signature.domain/formfieldsignature/type) { get; } | Menentukan jenis kolom Formulir. |
| [Value](../../groupdocs.signature.domain/formfieldsignature/value) { get; set; } | Menentukan objek data bidang formulir. |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | Menentukan lebar tanda tangan. |

## Metode

| Nama | Keterangan |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/digitalformfieldsignature/clone)() | Contoh Tanda Tangan FormField Kloning. |
| override [Equals](../../groupdocs.signature.domain/digitalformfieldsignature/equals)(object) | Menimpa metode Sama dengan untuk membandingkan properti tanda tangan |
| override [GetHashCode](../../groupdocs.signature.domain/digitalformfieldsignature/gethashcode)() | Menimpa metode GetHashCode |

### Lihat juga

* class [FormFieldSignature](../formfieldsignature)
* ruang nama [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* perakitan [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
