---
title: XmlFormatOptions
second_title: GroupDocs.Editor untuk Referensi .NET API
description: Berisi opsi yang memungkinkan untuk menyesuaikan format dokumen XML bila direpresentasikan sebagai HTML
type: docs
weight: 1280
url: /id/net/groupdocs.editor.options/xmlformatoptions/
---
## XmlFormatOptions class

Berisi opsi, yang memungkinkan untuk menyesuaikan format dokumen XML, bila direpresentasikan sebagai HTML

```csharp
public sealed class XmlFormatOptions : IEditOptions
```

## Properti

| Nama | Keterangan |
| --- | --- |
| [EachAttributeFromNewline](../../groupdocs.editor.options/xmlformatoptions/eachattributefromnewline) { get; set; } | Saat diaktifkan, setiap pasangan nilai atribut di setiap elemen XML akan ditempatkan pada baris baru. Secara default adalah salah (dinonaktifkan) — semua pasangan nilai atribut ditempatkan dalam satu baris. |
| [IsDefault](../../groupdocs.editor.options/xmlformatoptions/isdefault) { get; } | Menunjukkan apakah instance opsi pemformatan XML ini memiliki nilai default |
| [LeafTextNodesOnNewline](../../groupdocs.editor.options/xmlformatoptions/leaftextnodesonnewline) { get; set; } | Saat diaktifkan, simpul teks daun (konten tekstual di dalam elemen XML, yang tidak memiliki turunan) akan dirender pada baris baru dengan indentasi kiri lebih besar. Secara default salah (dinonaktifkan) — simpul teks daun ditempatkan pada baris yang sama dengan orang tuanya, tanpa indentasi baru. |
| [LeftIndent](../../groupdocs.editor.options/xmlformatoptions/leftindent) { get; set; } | Memungkinkan untuk menentukan offset untuk indentasi kiri setiap baris baru. Tidak boleh nilai bukan nol tanpa unit. Secara default adalah 10pt |

### Lihat juga

* interface [IEditOptions](../ieditoptions)
* ruang nama [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* perakitan [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
