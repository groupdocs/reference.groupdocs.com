---
title: FileType
second_title: .NET API Başvurusu için GroupDocs.Conversion
description: Dosya türü temel sınıf
type: docs
weight: 850
url: /tr/net/groupdocs.conversion.filetypes/filetype/
---
## FileType class

Dosya türü temel sınıf

```csharp
public class FileType : Enumeration
```

## yapıcılar

| İsim | Tanım |
| --- | --- |
| [FileType](filetype)() | Serileştirme yapıcısı |

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [Description](../../groupdocs.conversion.filetypes/filetype/description) { get; } | Dosya türü açıklaması |
| [Extension](../../groupdocs.conversion.filetypes/filetype/extension) { get; } | Dosya uzantısı |
| [Family](../../groupdocs.conversion.filetypes/filetype/family) { get; } | family dosyası |
| [FileFormat](../../groupdocs.conversion.filetypes/filetype/fileformat) { get; } | Dosya biçimi |

## yöntemler

| İsim | Tanım |
| --- | --- |
| static [FromExtension](../../groupdocs.conversion.filetypes/filetype/fromextension)(string) | Sağlanan fileExtension için FileType'ı alır |
| static [FromFilename](../../groupdocs.conversion.filetypes/filetype/fromfilename)(string) | Belirtilen fileName için FileType döndürür |
| static [FromStream](../../groupdocs.conversion.filetypes/filetype/fromstream)(Stream) | Sağlanan belge akışı için FileType'ı döndürür |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | Geçerli nesneyi diğeriyle karşılaştırır. |
| virtual [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(Enumeration) | İki nesne örneğinin eşit olup olmadığını belirler. |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | İki nesne örneğinin eşit olup olmadığını belirler. |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | Varsayılan hash işlevi olarak işlev görür. |
| override [ToString](../../groupdocs.conversion.filetypes/filetype/tostring)() | Dizi gösterimi |
| static [GetAll&lt;T&gt;](../../groupdocs.conversion.filetypes/filetype/getall)() | Tüm numaralandırma değerlerini döndürür. |
| [implicit operator](../../groupdocs.conversion.filetypes/filetype/op_implicit) | string 'ye dolaylı dönüştürme |

## Alanlar

| İsim | Tanım |
| --- | --- |
| static readonly [Unknown](../../groupdocs.conversion.filetypes/filetype/unknown) | Bilinmeyen dosya türü |

### Ayrıca bakınız

* class [Enumeration](../../groupdocs.conversion.contracts/enumeration)
* ad alanı [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* toplantı [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
