---
title: FuzzySearchOptions
second_title: GroupDocs.Mencari Referensi .NET API
description: Menyediakan opsi pencarian fuzzy.
type: docs
weight: 850
url: /id/net/groupdocs.search.options/fuzzysearchoptions/
---
## FuzzySearchOptions class

Menyediakan opsi pencarian fuzzy.

```csharp
public class FuzzySearchOptions
```

## Properti

| Nama | Keterangan |
| --- | --- |
| [ConsiderTranspositions](../../groupdocs.search.options/fuzzysearchoptions/considertranspositions) { get; set; } | Mendapat atau menetapkan nilai yang menunjukkan apakah algoritma pencarian fuzzy harus mempertimbangkan transposisi dua karakter yang berdekatan sebagai satu kesalahan. Nilai defaultnya adalah`BENAR` . |
| [Enabled](../../groupdocs.search.options/fuzzysearchoptions/enabled) { get; set; } | Mendapat atau menetapkan nilai yang menunjukkan apakah fitur pencarian fuzzy diaktifkan. Nilai defaultnya adalah`PALSU` . |
| [FuzzyAlgorithm](../../groupdocs.search.options/fuzzysearchoptions/fuzzyalgorithm) { get; set; } | Mendapat atau mengatur algoritma pencarian fuzzy. Algoritma pencarian fuzzy yang tersedia saat ini adalah[`SimilarityLevel`](../similaritylevel) Dan[`TableDiscreteFunction`](../tablediscretefunction). Nilai default adalah instance dari[`SimilarityLevel`](../similaritylevel) dengan nilai tingkat kemiripan sebesar`0,5` . |
| [OnlyBestResults](../../groupdocs.search.options/fuzzysearchoptions/onlybestresults) { get; set; } | Mendapat atau menetapkan nilai yang menunjukkan apakah hanya hasil terbaik yang akan dikembalikan. Nilai defaultnya adalah`PALSU` . |
| [OnlyBestResultsRange](../../groupdocs.search.options/fuzzysearchoptions/onlybestresultsrange) { get; set; } | Mendapat atau menyetel jumlah maksimum kesalahan yang ditemukan. Nilai defaultnya adalah`0` . |

### Perkataan

**Belajarlah lagi**

* [Pencarian kabur](https://docs.groupdocs.com/display/searchnet/Fuzzy+search)
* [pilihan pencarian](https://docs.groupdocs.com/display/searchnet/Search+options)

### Lihat juga

* ruang nama [GroupDocs.Search.Options](../../groupdocs.search.options)
* perakitan [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
