---
title: Search
second_title: .NET API Başvurusu için GroupDocs.Watermark
description: Belgedeki tüm olası filigranları arar.
type: docs
weight: 110
url: /tr/net/groupdocs.watermark/watermarker/search/
---
## Search() {#search}

Belgedeki tüm olası filigranları arar.

```csharp
public PossibleWatermarkCollection Search()
```

### Geri dönüş değeri

Olası filigranların toplanması.

### Notlar

Arama belirtilen nesnelerde gerçekleştirilir.[`SearchableObjects`](../searchableobjects).

Watermarks arama hakkında daha fazla bilgi edinin[Filigran arama](https://docs.groupdocs.com/display/watermarknet/Searching+watermarks).

### Örnekler

Desteklenen herhangi bir türde bir belgedeki olası filigranları sayın.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    PossibleWatermarkCollection watermarks = watermarker.Search();
    Console.WrileLine(watermarks.Count);
}
```

### Ayrıca bakınız

* class [PossibleWatermarkCollection](../../../groupdocs.watermark.search/possiblewatermarkcollection)
* class [Watermarker](../../watermarker)
* ad alanı [GroupDocs.Watermark](../../watermarker)
* toplantı [GroupDocs.Watermark](../../../)

---

## Search(SearchCriteria) {#search_1}

Belirtilen arama kriterlerine göre olası filigranları arar.

```csharp
public PossibleWatermarkCollection Search(SearchCriteria searchCriteria)
```

| Parametre | Tip | Tanım |
| --- | --- | --- |
| searchCriteria | SearchCriteria | Kullanılacak arama kriterleri. |

### Geri dönüş değeri

Olası filigranların toplanması.

### Notlar

Arama belirtilen nesnelerde gerçekleştirilir.[`SearchableObjects`](../searchableobjects).

Watermarks arama hakkında daha fazla bilgi edinin[Filigran arama](https://docs.groupdocs.com/display/watermarknet/Searching+watermarks).

### Örnekler

Belirli bir metni veya resmi içeren tüm olası filigranları bulun ve desteklenen herhangi bir türden bir belge 'den kaldırın.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    ImageSearchCriteria imageSearchCriteria = new ImageDctHashSearchCriteria(@"D:\logo.png");
    Regex regex = new Regex(@"^Company\sName$", RegexOptions.IgnoreCase);
    TextSearchCriteria textSearchCriteria = new TextSearchCriteria(regex);
    PossibleWatermarkCollection watermarks = watermarker.Search(textSearchCriteria.Or(imageSearchCriteria));
    watermarks.Clear();
    watermarker.Save(@"D:\output.doc");
}
```

### Ayrıca bakınız

* class [PossibleWatermarkCollection](../../../groupdocs.watermark.search/possiblewatermarkcollection)
* class [SearchCriteria](../../../groupdocs.watermark.search.searchcriteria/searchcriteria)
* class [Watermarker](../../watermarker)
* ad alanı [GroupDocs.Watermark](../../watermarker)
* toplantı [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
