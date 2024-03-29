---
title: XpsEditOptions
second_title: GroupDocs.Editor untuk Referensi .NET API
description: Memungkinkan untuk menentukan opsi khusus untuk mengedit dokumen Spesifikasi Kertas XML
type: docs
weight: 1300
url: /id/net/groupdocs.editor.options/xpseditoptions/
---
## XpsEditOptions class

Memungkinkan untuk menentukan opsi khusus untuk mengedit dokumen (Spesifikasi Kertas XML)

```csharp
public sealed class XpsEditOptions : FixedLayoutEditOptionsBase
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [XpsEditOptions](xpseditoptions#constructor)() | Membuat dan mengembalikan instance baru dari kelas XpsEditOptions, di mana semua opsi disetel ke nilai defaultnya |
| [XpsEditOptions](xpseditoptions#constructor_1)(bool) | Membuat dan mengembalikan instance baru dari kelas XpsEditOptions dengan pagination yang ditentukan dan default semua opsi lainnya |

## Properti

| Nama | Keterangan |
| --- | --- |
| [EnablePagination](../../groupdocs.editor.options/fixedlayouteditoptionsbase/enablepagination) { get; set; } | Memungkinkan untuk mengaktifkan paginasi (benar) atau menonaktifkan (salah) dalam dokumen HTML yang dihasilkan. Secara default dinonaktifkan (false). |
| [Pages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/pages) { get; set; } | Memungkinkan untuk mengatur rentang halaman untuk diproses. Secara default, semua halaman dokumen tata letak tetap diproses. |
| [SkipImages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/skipimages) { get; set; } | Mendapat atau menyetel bendera yang menunjukkan apakah gambar harus dilewati saat mengonversi masukan dokumen tata letak tetap ke HTML yang dihasilkan. Default salah - gambar dipertahankan. |

### Lihat juga

* class [FixedLayoutEditOptionsBase](../fixedlayouteditoptionsbase)
* ruang nama [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* perakitan [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
