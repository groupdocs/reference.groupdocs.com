---
title: TextualDocumentInfo
second_title: .NET API Başvurusu için GroupDocs.Editor
description: XML HTML veya düz metin TXT gibi bir metin belgesinin meta verilerini temsil eder
type: docs
weight: 630
url: /tr/net/groupdocs.editor.metadata/textualdocumentinfo/
---
## TextualDocumentInfo structure

XML, HTML veya düz metin (TXT) gibi bir metin belgesinin meta verilerini temsil eder

```csharp
public struct TextualDocumentInfo : IDocumentInfo
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Encoding](../../groupdocs.editor.metadata/textualdocumentinfo/encoding) { get; } | Metin belgesinin algılanan varsayılan kodlamasını döndürür |
| [Format](../../groupdocs.editor.metadata/textualdocumentinfo/format) { get; } | Bu metin belgesinin biçimini döndürür. Bazı durumlarda %100 doğru olmayabilir. |
| [IsEncrypted](../../groupdocs.editor.metadata/textualdocumentinfo/isencrypted) { get; } | Metin belgeleri şifrelenemediği için her zaman 'yanlış' değerini döndürür. |
| [PageCount](../../groupdocs.editor.metadata/textualdocumentinfo/pagecount) { get; } | Her zaman 1 döndürür |
| [Size](../../groupdocs.editor.metadata/textualdocumentinfo/size) { get; } | Bu metinsel belgenin boyutunu bayt cinsinden (karakter sayısını değil) verir |

### Ayrıca bakınız

* interface [IDocumentInfo](../idocumentinfo)
* ad alanı [GroupDocs.Editor.Metadata](../../groupdocs.editor.metadata)
* toplantı [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
