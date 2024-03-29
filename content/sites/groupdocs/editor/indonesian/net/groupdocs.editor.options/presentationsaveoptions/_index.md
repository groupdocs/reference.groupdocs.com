---
title: PresentationSaveOptions
second_title: GroupDocs.Editor untuk Referensi .NET API
description: Memungkinkan untuk menentukan opsi khusus untuk membuat dan menyimpan dokumen Presentasi kompatibel dengan PowerPoint
type: docs
weight: 1090
url: /id/net/groupdocs.editor.options/presentationsaveoptions/
---
## PresentationSaveOptions class

Memungkinkan untuk menentukan opsi khusus untuk membuat dan menyimpan dokumen Presentasi (kompatibel dengan PowerPoint)

```csharp
public sealed class PresentationSaveOptions : ISaveOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [PresentationSaveOptions](presentationsaveoptions)(PresentationFormats) | Membuat instance baru dari PresentationSaveOptions dengan format keluaran Presentasi wajib yang ditentukan, sementara semua parameter lainnya adalah default |

## Properti

| Nama | Keterangan |
| --- | --- |
| [InsertAsNewSlide](../../groupdocs.editor.options/presentationsaveoptions/insertasnewslide) { get; set; } | Boolean flag, yang menentukan apakah slide yang diedit harus menggantikan slide yang ada dalam presentasi asli pada posisi, yang ditentukan oleh[`SlideNumber`](./slidenumber) properti, atau harus disuntikkan antara slide yang ada dan yang sebelumnya, tanpa mengganti kontennya. Secara default salah — slide yang ada akan diganti. Properti ini diabaikan, jika nilai[`SlideNumber`](./slidenumber) properti disetel ke '0'. |
| [OutputFormat](../../groupdocs.editor.options/presentationsaveoptions/outputformat) { get; set; } | Memungkinkan untuk menentukan format Presentasi, yang akan digunakan untuk menyimpan dokumen |
| [Password](../../groupdocs.editor.options/presentationsaveoptions/password) { get; set; } | Memungkinkan untuk menentukan, memodifikasi dan mendapatkan kata sandi, yang akan digunakan untuk menyandikan dokumen Presentasi yang dihasilkan. Secara default adalah NULL - kata sandi tidak akan disetel. Setel ke NULL atau kosongkan string untuk menghapus kata sandi, jika sudah disetel sebelumnya. |
| [SlideNumber](../../groupdocs.editor.options/presentationsaveoptions/slidenumber) { get; set; } | Memungkinkan untuk menyisipkan slide yang telah diedit ke dalam presentasi yang sudah ada alih-alih membuat presentasi satu slide baru (perilaku default). Nomor slide adalah nomor berbasis 1 dari slide dalam presentasi, dimuat di kelas Editor. Jika 0 (nilai default), presentasi baru akan dibuat dengan satu slide yang diedit. Jika lebih besar atau lebih kecil dari nol, dan ada presentasi yang valid, dimuat di kelas Editor, slide yang diedit, disimpan di dalam instance input EditableDocument, akan dimasukkan ke dalam presentasi ini. |

### Perkataan

Instance kelas ini harus diteruskan ke[`Save`](../../groupdocs.editor/editor/save)metode untuk menyimpan presentasi yang diedit ke dalam dokumen akhir dari beberapa format khusus Presentasi. Konstruktornya memiliki satu parameter wajib — format Presentasi output. Semua parameter lainnya bersifat opsional dan dapat dihilangkan.

### Lihat juga

* interface [ISaveOptions](../isaveoptions)
* ruang nama [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* perakitan [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
