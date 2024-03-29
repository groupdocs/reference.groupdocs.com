---
title: TextSplitOptions
second_title: GroupDocs.Merger untuk Referensi .NET API
description: Menyediakan opsi untuk pemisahan teks dokumen.
type: docs
weight: 630
url: /id/net/groupdocs.merger.domain.options/textsplitoptions/
---
## TextSplitOptions class

Menyediakan opsi untuk pemisahan teks dokumen.

```csharp
public class TextSplitOptions : ITextSplitOptions
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [TextSplitOptions](textsplitoptions#constructor_3)(CreateSplitStream, int[]) | Menginisialisasi instance baru dari[`TextSplitOptions`](../textsplitoptions) kelas. |
| [TextSplitOptions](textsplitoptions#constructor_5)(string, int[]) | Menginisialisasi instance baru dari[`TextSplitOptions`](../textsplitoptions) kelas. |
| [TextSplitOptions](textsplitoptions#constructor_1)(CreateSplitStream, ReleaseSplitStream, int[]) | Menginisialisasi instance baru dari[`TextSplitOptions`](../textsplitoptions) kelas. |
| [TextSplitOptions](textsplitoptions#constructor_2)(CreateSplitStream, TextSplitMode, int[]) | Menginisialisasi instance baru dari[`TextSplitOptions`](../textsplitoptions) kelas. |
| [TextSplitOptions](textsplitoptions#constructor_4)(string, TextSplitMode, int[]) | Menginisialisasi instance baru dari[`TextSplitOptions`](../textsplitoptions) kelas. |
| [TextSplitOptions](textsplitoptions#constructor)(CreateSplitStream, ReleaseSplitStream, TextSplitMode, int[]) | Menginisialisasi instance baru dari[`TextSplitOptions`](../textsplitoptions) kelas. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [CreateStream](../../groupdocs.merger.domain.options/textsplitoptions/createstream) { get; } | Delegasi yang menentukan metode untuk membuat aliran keluaran terpisah. |
| [LineNumbers](../../groupdocs.merger.domain.options/textsplitoptions/linenumbers) { get; } | Nomor baris untuk pemisahan teks. |
| [Mode](../../groupdocs.merger.domain.options/textsplitoptions/mode) { get; } | Mode untuk pemisahan teks. |
| [ReleaseStream](../../groupdocs.merger.domain.options/textsplitoptions/releasestream) { get; } | Delegasi yang menentukan metode untuk merilis aliran pemisahan output. |

## Metode

| Nama | Keterangan |
| --- | --- |
| [GetPathByIndex](../../groupdocs.merger.domain.options/textsplitoptions/getpathbyindex)(int, string) | Mendapatkan jalur file lengkap dari dokumen yang dipisah berdasarkan indeks dengan ekstensi yang ditentukan. |
| [Validate](../../groupdocs.merger.domain.options/textsplitoptions/validate)(FileType) | Memvalidasi opsi pemisahan. |

### Lihat juga

* interface [ITextSplitOptions](../itextsplitoptions)
* ruang nama [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* perakitan [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
