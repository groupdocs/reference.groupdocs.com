---
title: FuzzyAlgorithm
second_title: .NET API Başvurusu için GroupDocs.Search
description: Bulanık arama algoritmasını alır veya ayarlar. Şu anda kullanılabilen bulanık arama algoritmaları şunlardırSimilarityLevelgroupdocs.search.options/similaritylevel VeTableDiscreteFunctiongroupdocs.search.options/tablediscretefunction. Varsayılan değerSimilarityLevelgroupdocs.search.options/similaritylevel benzerlik düzeyi değeri ile05 .
type: docs
weight: 30
url: /tr/net/groupdocs.search.options/fuzzysearchoptions/fuzzyalgorithm/
---
## FuzzySearchOptions.FuzzyAlgorithm property

Bulanık arama algoritmasını alır veya ayarlar. Şu anda kullanılabilen bulanık arama algoritmaları şunlardır:[`SimilarityLevel`](../../similaritylevel) Ve[`TableDiscreteFunction`](../../tablediscretefunction). Varsayılan değer,[`SimilarityLevel`](../../similaritylevel) benzerlik düzeyi değeri ile`0,5` .

```csharp
public FuzzyAlgorithm FuzzyAlgorithm { get; set; }
```

### Mülk değeri

Bulanık arama algoritması.

### istisnalar

| istisna | şart |
| --- | --- |
| ArgumentNullException | Ne zaman atıldı*value* dır-dir`hükümsüz`. |

### Örnekler

Örnek, bulanık arama algoritmasının nasıl ayarlanacağını gösterir.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";

Index index = new Index(indexFolder); // Belirtilen klasörde bir dizin oluşturma
index.Add(documentsFolder); // Belgeleri belirtilen klasörden indeksleme

SearchOptions options = new SearchOptions();
options.FuzzySearch.Enabled = true; // Bulanık aramayı etkinleştirme
options.FuzzySearch.FuzzyAlgorithm = new TableDiscreteFunction(1, new Step(5, 2), new Step(8, 3)); // Bulanık arama algoritmasının oluşturulması
// Bu işlev, 1 ile 4 karakter arasındaki kelimeler için maksimum hata sayısı olarak 1'i belirtir.
// 5 ile 7 karakter arasındaki kelimeler için maksimum hata sayısını 2 olarak belirtir.
// 8 ve daha fazla karakterden oluşan kelimeler için maksimum hata sayısı olarak 3'ü belirtir.

SearchResult result = index.Search(query, options); // Dizinde ara
```

### Ayrıca bakınız

* class [FuzzyAlgorithm](../../fuzzyalgorithm)
* class [FuzzySearchOptions](../../fuzzysearchoptions)
* ad alanı [GroupDocs.Search.Options](../../fuzzysearchoptions)
* toplantı [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
