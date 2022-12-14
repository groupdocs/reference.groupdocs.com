---
title: PdfShapeFormattedTextFragmentCollection
second_title: .NET API Başvurusu için GroupDocs.Watermark
description: XObject Artifact veya Annotation. pdf belgesindeki biçimlendirilmiş metin parçalarından oluşan bir koleksiyonu temsil eder.
type: docs
weight: 710
url: /tr/net/groupdocs.watermark.contents.pdf/pdfshapeformattedtextfragmentcollection/
---
## PdfShapeFormattedTextFragmentCollection class

XObject, Artifact veya Annotation. pdf belgesindeki biçimlendirilmiş metin parçalarından oluşan bir koleksiyonu temsil eder.

```csharp
public class PdfShapeFormattedTextFragmentCollection : PdfFormattedTextFragmentCollection
```

## Özellikleri

| İsim | Tanım |
| --- | --- |
| [CollectionType](../../groupdocs.watermark.search/formattedtextfragmentcollection/collectiontype) { get; } | Biçimlendirilmiş parça toplama türünü alır. |
| virtual [Count](../../groupdocs.watermark.common/readonlylistbase-1/count) { get; } | Koleksiyonda bulunan öğelerin sayısını alır. |
| override [IsReadOnly](../../groupdocs.watermark.common/removeonlylistbase-1/isreadonly) { get; } | Koleksiyonun salt okunur olup olmadığını gösteren bir değer alır. |
| virtual [Item](../../groupdocs.watermark.common/readonlylistbase-1/item) { get; } | Koleksiyonda belirtilen dizindeki öğeyi alır. |

## yöntemler

| İsim | Tanım |
| --- | --- |
| [Add](../../groupdocs.watermark.search/formattedtextfragmentcollection/add)(string) | Koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Add](../../groupdocs.watermark.search/formattedtextfragmentcollection/add)(string, Font) | Koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Add](../../groupdocs.watermark.search/formattedtextfragmentcollection/add)(string, Font, Color) | Koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Add](../../groupdocs.watermark.search/formattedtextfragmentcollection/add)(string, Font, Color, Color) | Koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Clear](../../groupdocs.watermark.common/removeonlylistbase-1/clear)() |  |
| virtual [Contains](../../groupdocs.watermark.common/readonlylistbase-1/contains)(FormattedTextFragment) |  |
| virtual [GetEnumerator](../../groupdocs.watermark.common/readonlylistbase-1/getenumerator)() |  |
| virtual [IndexOf](../../groupdocs.watermark.common/readonlylistbase-1/indexof)(FormattedTextFragment) |  |
| [Insert](../../groupdocs.watermark.search/formattedtextfragmentcollection/insert)(int, string) | Belirli bir dizindeki koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Insert](../../groupdocs.watermark.search/formattedtextfragmentcollection/insert)(int, string, Font) | Belirli bir dizindeki koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Insert](../../groupdocs.watermark.search/formattedtextfragmentcollection/insert)(int, string, Font, Color) | Belirli bir dizindeki koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Insert](../../groupdocs.watermark.search/formattedtextfragmentcollection/insert)(int, string, Font, Color, Color) | Belirli bir dizindeki koleksiyona biçimlendirilmiş bir metin parçası ekler. |
| [Remove](../../groupdocs.watermark.common/removeonlylistbase-1/remove)(FormattedTextFragment) |  |
| [RemoveAt](../../groupdocs.watermark.common/removeonlylistbase-1/removeat)(int) |  |

### Notlar

Bu koleksiyon şunları içerir:[`PdfFormattedTextFragment`](../pdfformattedtextfragment) yazın.

### Ayrıca bakınız

* class [PdfFormattedTextFragmentCollection](../pdfformattedtextfragmentcollection)
* ad alanı [GroupDocs.Watermark.Contents.Pdf](../../groupdocs.watermark.contents.pdf)
* toplantı [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
