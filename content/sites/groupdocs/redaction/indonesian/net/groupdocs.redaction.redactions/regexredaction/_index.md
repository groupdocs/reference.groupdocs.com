---
title: RegexRedaction
second_title: GroupDocs.Redaction untuk Referensi .NET API
description: Merupakan redaksi teks yang mencari dan mengganti teks dalam dokumen dengan mencocokkan ekspresi reguler yang diberikan.
type: docs
weight: 590
url: /id/net/groupdocs.redaction.redactions/regexredaction/
---
## RegexRedaction class

Merupakan redaksi teks yang mencari dan mengganti teks dalam dokumen dengan mencocokkan ekspresi reguler yang diberikan.

```csharp
public class RegexRedaction : TextRedaction
```

## Konstruktor

| Nama | Keterangan |
| --- | --- |
| [RegexRedaction](regexredaction#constructor_1)(Regex, ReplacementOptions) | Menginisialisasi instance baru dari kelas RegexRedaction. |
| [RegexRedaction](regexredaction#constructor)(string, ReplacementOptions) | Menginisialisasi instance baru dari kelas RegexRedaction. |

## Properti

| Nama | Keterangan |
| --- | --- |
| [ActionOptions](../../groupdocs.redaction.redactions/textredaction/actionoptions) { get; } | Mendapatkan[`ReplacementOptions`](../replacementoptions) misalnya, menentukan jenis penggantian teks. |
| override [Description](../../groupdocs.redaction.redactions/regexredaction/description) { get; } | Mengembalikan sebuah string, menjelaskan redaksi dan parameternya. |
| [OcrConnector](../../groupdocs.redaction.redactions/textredaction/ocrconnector) { get; set; } | Mendapat atau menyetel[`IOcrConnector`](../../groupdocs.redaction.integration.ocr/iocrconnector) implementasi, diperlukan untuk mengekstrak teks dari konten grafik. |
| [RegularExpression](../../groupdocs.redaction.redactions/regexredaction/regularexpression) { get; } | Mencocokkan ekspresi reguler. |

## Metode

| Nama | Keterangan |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/regexredaction/applyto)(DocumentFormatInstance) | Menerapkan redaksi ke instance format tertentu. |

### Perkataan

**Belajarlah lagi**

* Detail lebih lanjut tentang menerapkan redaksi: [Dasar redaksi](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* Detail lebih lanjut tentang penyuntingan teks dokumen: [Redaksi teks](https://docs.groupdocs.com/redaction/net/text-redactions/)

### Contoh

Contoh berikut menunjukkan penggantian teks menggunakan ekspresi reguler.

```csharp
    using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
    {
      // ganti dengan teks
      redactor.Apply(new RegexRedaction("\\d{2}\\s*\\d{2}[^\\d]*\\d{6}", new ReplacementOptions("[removed]")));
      // ganti dengan persegi panjang padat berwarna biru
      redactor.Apply(new RegexRedaction(@"^\d+[,\.]{1}\d+$", new ReplacementOptions(System.Drawing.Color.Blue)));
      redactor.Save();
    }
```

### Lihat juga

* class [TextRedaction](../textredaction)
* ruang nama [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* perakitan [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
