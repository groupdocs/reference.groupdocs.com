---
title: FontEmbeddingOptions
second_title: GroupDocs.Editor untuk Referensi .NET API
description: Opsi penyematan font mengontrol sumber daya font mana yang harus disematkan ke output WordProcessing atau dokumen PDF
type: docs
weight: 890
url: /id/net/groupdocs.editor.options/fontembeddingoptions/
---
## FontEmbeddingOptions enumeration

Opsi penyematan font mengontrol sumber daya font mana yang harus disematkan ke output WordProcessing atau dokumen PDF

```csharp
public enum FontEmbeddingOptions : byte
```

### Nilai

| Nama | Nilai | Keterangan |
| --- | --- | --- |
| NotEmbed | `0` | Jangan menyematkan sumber daya font apa pun baik dari EditableDocument maupun dari sistem. Nilai default. |
| EmbedAll | `1` | Analisis konten dokumen dari masukan EditableDocument, temukan semua font yang digunakan dan sematkan ke dalam dokumen WordProcessing atau PDF keluaran. Di tempat pertama GroupDocs.Editor mengambil font dari sumber font dalam EditableDocument. Jika tidak mencukupi atau hilang, maka GroupDocs.Editor mengambil font dari OS. |
| EmbedWithoutSystem | `2` | Tepat untukEmbedAll , tetapi kecualikan font tersebut, yang diperlakukan oleh OS sebagai font sistem |

### Perkataan

Opsi penyematan font diterapkan selama penyimpanan dokumen (dari EditableDocument menengah ke output WordProcessing atau format PDF), enum ini disertakan sebagai properti di WordProcessingSaveOptions dan PdfSaveOptions, dari mana ia harus digunakan

### Lihat juga

* ruang nama [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* perakitan [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
