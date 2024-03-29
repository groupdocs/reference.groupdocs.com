---
title: AviHeaderFlags
second_title: GroupDocs.Metadata untuk Referensi .NET API
description: Mewakili bendera AVI Header.
type: docs
weight: 2390
url: /id/net/groupdocs.metadata.formats.video/aviheaderflags/
---
## AviHeaderFlags enumeration

Mewakili bendera AVI Header.

```csharp
[Flags]
public enum AviHeaderFlags
```

### Nilai

| Nama | Nilai | Keterangan |
| --- | --- | --- |
| HasIndex | `10` | Menunjukkan file AVI memiliki indeks. |
| MustUseIndex | `20` | Menunjukkan bahwa aplikasi harus menggunakan indeks, bukan urutan fisik potongan dalam file, untuk menentukan urutan penyajian data. Misalnya, tanda ini dapat digunakan untuk membuat daftar bingkai untuk diedit. |
| IsInterleaved | `100` | Menunjukkan file AVI disisipkan. |
| TrustCkType | `800` | Gunakan CKType untuk menemukan bingkai kunci. |
| WasCaptureFile | `10000` | Menunjukkan bahwa file AVI adalah file yang dialokasikan secara khusus yang digunakan untuk merekam video real-time. Aplikasi harus memperingatkan pengguna sebelum menimpa file dengan flag yang disetel ini karena pengguna mungkin mendefrag file ini. |
| Copyrighted | `20000` | Menunjukkan file AVI berisi data dan perangkat lunak berhak cipta. Saat tanda ini digunakan, perangkat lunak tidak boleh mengizinkan data untuk diduplikasi. |

### Lihat juga

* ruang nama [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* perakitan [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
