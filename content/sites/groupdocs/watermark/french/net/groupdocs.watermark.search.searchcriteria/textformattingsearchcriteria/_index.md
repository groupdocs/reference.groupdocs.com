---
title: TextFormattingSearchCriteria
second_title: Référence de l'API GroupDocs.Watermark pour .NET
description: Représente les critères permettant le filtrage par mise en forme du texte.
type: docs
weight: 2690
url: /fr/net/groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/
---
## TextFormattingSearchCriteria class

Représente les critères permettant le filtrage par mise en forme du texte.

```csharp
public class TextFormattingSearchCriteria : SearchCriteria
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [TextFormattingSearchCriteria](textformattingsearchcriteria)() | Initialise une nouvelle instance du[`TextFormattingSearchCriteria`](../textformattingsearchcriteria) classe. |

## Propriétés

| Nom | La description |
| --- | --- |
| [BackgroundColorRange](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/backgroundcolorrange) { get; set; } | Obtient ou définit la gamme de couleurs utilisées pour filtrer les filigranes par couleur d'arrière-plan du texte. |
| [FontBold](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/fontbold) { get; set; } | Obtient ou définit une valeur indiquant si la police utilisée dans la mise en forme du texte du filigrane est en gras. |
| [FontItalic](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/fontitalic) { get; set; } | Obtient ou définit une valeur indiquant si la police utilisée dans la mise en forme du texte du filigrane est en italique. |
| [FontName](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/fontname) { get; set; } | Obtient ou définit le nom de la police utilisée dans la mise en forme possible du texte du filigrane. |
| [FontStrikeout](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/fontstrikeout) { get; set; } | Obtient ou définit une valeur indiquant si la police utilisée dans la mise en forme du texte du filigrane est barrée. |
| [FontUnderline](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/fontunderline) { get; set; } | Obtient ou définit une valeur indiquant si la police utilisée dans la mise en forme du texte du filigrane est soulignée. |
| [ForegroundColorRange](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/foregroundcolorrange) { get; set; } | Obtient ou définit la gamme de couleurs utilisées pour filtrer les filigranes par couleur de premier plan du texte. |
| [MaxFontSize](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/maxfontsize) { get; set; } | Obtient ou définit la valeur de fin de la taille de la police. |
| [MinFontSize](../../groupdocs.watermark.search.searchcriteria/textformattingsearchcriteria/minfontsize) { get; set; } | Obtient ou définit la valeur de départ de la taille de la police. |

## Méthodes

| Nom | La description |
| --- | --- |
| [And](../../groupdocs.watermark.search.searchcriteria/searchcriteria/and)(SearchCriteria) | Combine ceci[`SearchCriteria`](../searchcriteria) avec d'autres critères en utilisant l'opérateur logique AND. |
| [Not](../../groupdocs.watermark.search.searchcriteria/searchcriteria/not)() | Annule cela[`SearchCriteria`](../searchcriteria) . |
| [Or](../../groupdocs.watermark.search.searchcriteria/searchcriteria/or)(SearchCriteria) | Combine ceci[`SearchCriteria`](../searchcriteria) avec d'autres critères en utilisant l'opérateur logique OR. |

### Remarques

**Apprendre encore plus:**

* [Recherche de filigranes](https://docs.groupdocs.com/display/watermarknet/Searching+watermarks)

### Exemples

Supprimez les éventuels filigranes avec une mise en forme de texte particulière (quel que soit le type de document).

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\test.doc"))
{
    TextFormattingSearchCriteria criteria = new TextFormattingSearchCriteria();
    criteria.ForegroundColorRange = new ColorRange();
    criteria.ForegroundColorRange.MinHue = -5;
    criteria.ForegroundColorRange.MaxHue = 10;
    criteria.ForegroundColorRange.MinBrightness = 0.01f;
    criteria.ForegroundColorRange.MaxBrightness = 0.99f;
    criteria.BackgroundColorRange = new ColorRange();
    criteria.BackgroundColorRange.IsEmpty = true;
    criteria.FontName = "Arial";
    criteria.MinFontSize = 19;
    criteria.MaxFontSize = 42;
    criteria.FontBold = true;

    PossibleWatermarkCollection watermarks = watermarker.Search(criteria);
    watermarks.Clear();
    watermarker.Save();
}
```

### Voir également

* class [SearchCriteria](../searchcriteria)
* espace de noms [GroupDocs.Watermark.Search.SearchCriteria](../../groupdocs.watermark.search.searchcriteria)
* Assemblée [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
