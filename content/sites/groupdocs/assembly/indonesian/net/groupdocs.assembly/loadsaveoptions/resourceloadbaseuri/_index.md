---
title: ResourceLoadBaseUri
second_title: GroupDocs.Assembly untuk Referensi .NET API
description: Mendapat atau menyetel URI dasar untuk menyelesaikan URI relatif file sumber daya eksternal menjadi URI absolut saat memuat dokumen template HTML untuk dirakit dan disimpan ke format nonHTML. Nilai default adalah string kosong.
type: docs
weight: 20
url: /id/net/groupdocs.assembly/loadsaveoptions/resourceloadbaseuri/
---
## LoadSaveOptions.ResourceLoadBaseUri property

Mendapat atau menyetel URI dasar untuk menyelesaikan URI relatif file sumber daya eksternal menjadi URI absolut saat memuat dokumen template HTML untuk dirakit dan disimpan ke format non-HTML. Nilai default adalah string kosong.

```csharp
public string ResourceLoadBaseUri { get; set; }
```

### Perkataan

Saat memuat dokumen HTML dari file, folder yang memuatnya digunakan sebagai URI dasar secara default, yang tidak dapat terjadi saat memuat dokumen HTML dari aliran. Setel properti ini untuk menentukan URI dasar saat memuat dokumen HTML dari aliran atau untuk mengganti URI dasar default saat memuat dokumen HTML dari file.

Nilai properti ini diabaikan dalam kasus berikut:

* Dokumen HTML yang dimuat berisi elemen BASE HTML yang menyediakan URI dasar.
* Dokumen HTML yang dimuat harus dirakit dan disimpan ke HTML (file sumber daya eksternal tidak dimuat dan URI relatif tidak diubah).

### Lihat juga

* class [LoadSaveOptions](../../loadsaveoptions)
* ruang nama [GroupDocs.Assembly](../../loadsaveoptions)
* perakitan [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
