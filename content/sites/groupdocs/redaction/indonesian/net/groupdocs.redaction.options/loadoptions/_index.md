---
title: LoadOptions
second_title: GroupDocs.Redaction untuk Referensi .NET API
description: Memberikan pilihan yang akan digunakan untuk membuka file.
type: docs
weight: 310
url: /id/net/groupdocs.redaction.options/loadoptions/
---
## LoadOptions class

Memberikan pilihan yang akan digunakan untuk membuka file.

```csharp
public class LoadOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [LoadOptions](loadoptions#constructor)() | Menginisialisasi instance baru dari kelas LoadOptions. |
| [LoadOptions](loadoptions#constructor_1)(string) | Menginisialisasi instance baru dari kelas LoadOptions dengan kata sandi yang ditentukan. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [Password](../../groupdocs.redaction.options/loadoptions/password) { get; set; } | Mendapatkan atau menyetel kata sandi untuk dokumen yang dilindungi kata sandi. |

### Perkataan

**Belajarlah lagi**

* [Memuat dokumen](https://docs.groupdocs.com/redaction/net/loading-documents/)
* [Muat dari disk lokal](https://docs.groupdocs.com/redaction/net/load-from-local-disc/)
* [Muat dari aliran](https://docs.groupdocs.com/redaction/net/load-from-stream/)
* [Muat dokumen yang dilindungi kata sandi](https://docs.groupdocs.com/redaction/net/load-password-protected-file/)

### Contoh

Contoh berikut menunjukkan cara membuka dokumen yang dilindungi kata sandi.

```csharp
LoadOptions loadOptions = new LoadOptions("mysecretpassword");
using (var redactor = new Redactor("PasswordProtected.pdf", loadOptions))
{
    // bekerja dengan dokumen
}
```

### Lihat juga

* ruang nama [GroupDocs.Redaction.Options](../../groupdocs.redaction.options)
* perakitan [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
