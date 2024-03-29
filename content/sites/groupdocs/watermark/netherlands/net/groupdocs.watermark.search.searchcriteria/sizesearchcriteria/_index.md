---
title: SizeSearchCriteria
second_title: GroupDocs.Watermark voor .NET API-referentie
description: Vertegenwoordigt criteria die filteren op watermerkgrootte mogelijk maken.
type: docs
weight: 2680
url: /nl/net/groupdocs.watermark.search.searchcriteria/sizesearchcriteria/
---
## SizeSearchCriteria class

Vertegenwoordigt criteria die filteren op watermerkgrootte mogelijk maken.

```csharp
public class SizeSearchCriteria : SearchCriteria
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [SizeSearchCriteria](sizesearchcriteria)(Dimension, double, double) | Initialiseert een nieuw exemplaar van het[`SizeSearchCriteria`](../sizesearchcriteria)class met een opgegeven dimensie, een beginwaarde en een eindwaarde. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [Dimension](../../groupdocs.watermark.search.searchcriteria/sizesearchcriteria/dimension) { get; } | Haalt de dimensie van het watermerk op om op te zoeken. |
| [Maximum](../../groupdocs.watermark.search.searchcriteria/sizesearchcriteria/maximum) { get; } | Haalt de eindwaarde op. |
| [Minimum](../../groupdocs.watermark.search.searchcriteria/sizesearchcriteria/minimum) { get; } | Haalt de startwaarde op. |

## methoden

| Naam | Beschrijving |
| --- | --- |
| [And](../../groupdocs.watermark.search.searchcriteria/searchcriteria/and)(SearchCriteria) | Combineert dit[`SearchCriteria`](../searchcriteria) met andere criteria met behulp van de logische AND-operator. |
| [Not](../../groupdocs.watermark.search.searchcriteria/searchcriteria/not)() | Negeert dit[`SearchCriteria`](../searchcriteria) . |
| [Or](../../groupdocs.watermark.search.searchcriteria/searchcriteria/or)(SearchCriteria) | Combineert dit[`SearchCriteria`](../searchcriteria) met andere criteria met behulp van de logische OR-operator. |

### Opmerkingen

**Kom meer te weten:**

* [Watermerken zoeken](https://docs.groupdocs.com/display/watermarknet/Searching+watermarks)

### Voorbeelden

Watermerk zoeken en verwijderen met behulp van zoekcriteria.

```csharp
using (Watermarker watermarker = new Watermarker(@"C:\test.some_ext"))
{
    SizeSearchCriteria widthRange = new SizeSearchCriteria(Dimension.Width, 50, 100);
    RotateAngleSearchCriteria rotateAngle = new RotateAngleSearchCriteria(0, 45);
    TextSearchCriteria textCriteria = new TextSearchCriteria(new Regex("^Test watermark$"));
    PossibleWatermarkCollection watermarks = watermarker.Search(textCriteria.And(widthRange.Or(rotateAngle)));
    watermarks.Clear();
    watermarker.Save();
}
```

### Zie ook

* class [SearchCriteria](../searchcriteria)
* naamruimte [GroupDocs.Watermark.Search.SearchCriteria](../../groupdocs.watermark.search.searchcriteria)
* montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
