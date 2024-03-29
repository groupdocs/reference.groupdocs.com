---
title: ImageDctHashSearchCriteria
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Repräsentiert ein Suchkriterium zum Auffinden von Bildern in einem Dokument.
type: docs
weight: 2590
url: /de/net/groupdocs.watermark.search.searchcriteria/imagedcthashsearchcriteria/
---
## ImageDctHashSearchCriteria class

Repräsentiert ein Suchkriterium zum Auffinden von Bildern in einem Dokument.

```csharp
public class ImageDctHashSearchCriteria : ImageSearchCriteria
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [ImageDctHashSearchCriteria](imagedcthashsearchcriteria#constructor)(Stream) | Initialisiert eine neue Instanz von[`ImageDctHashSearchCriteria`](../imagedcthashsearchcriteria) Klasse mit einem bestimmten Stream. |
| [ImageDctHashSearchCriteria](imagedcthashsearchcriteria#constructor_1)(string) | Initialisiert eine neue Instanz von[`ImageDctHashSearchCriteria`](../imagedcthashsearchcriteria) Klasse mit einem angegebenen Dateipfad. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [MaxDifference](../../groupdocs.watermark.search.searchcriteria/imagesearchcriteria/maxdifference) { get; set; } | Ruft die maximal zulässige Differenz zwischen Bildern ab oder legt sie fest. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [And](../../groupdocs.watermark.search.searchcriteria/searchcriteria/and)(SearchCriteria) | Kombiniert dies[`SearchCriteria`](../searchcriteria) mit anderen Kriterien unter Verwendung des logischen UND-Operators. |
| [Not](../../groupdocs.watermark.search.searchcriteria/searchcriteria/not)() | Negiert dies[`SearchCriteria`](../searchcriteria) . |
| [Or](../../groupdocs.watermark.search.searchcriteria/searchcriteria/or)(SearchCriteria) | Kombiniert dies[`SearchCriteria`](../searchcriteria) mit anderen Kriterien mit logischem OR-Operator. |

### Bemerkungen

Dieses Suchkriterium verwendet DCT-basierten perzeptiven Bild-Hash zur Berechnung der Bildähnlichkeit. **Erfahren Sie mehr:**

* [Suche nach Wasserzeichen](https://docs.groupdocs.com/display/watermarknet/Searching+watermarks)

### Beispiele

Suche nach Bildern in den angehängten Dateien (pdf).

```csharp
WatermarkerSettings settings = new WatermarkerSettings();
settings.SearchableObjects = new SearchableObjects
{
    PdfSearchableObjects = PdfSearchableObjects.All
};
PdfLoadOptions loadOptions = new PdfLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\test.pdf", loadOptions, settings))
{
    // Beispielbild angeben, mit dem Dokumentbilder verglichen werden sollen
    ImageSearchCriteria criteria = new ImageDctHashSearchCriteria(@"D:\sample.png");
    // Nach ähnlichen Bildern suchen
    PossibleWatermarkCollection possibleWatermarks = watermarker.Search(criteria);
    // Gefundene Bildwasserzeichen entfernen oder ändern
    // ...
}
```

### Siehe auch

* class [ImageSearchCriteria](../imagesearchcriteria)
* namensraum [GroupDocs.Watermark.Search.SearchCriteria](../../groupdocs.watermark.search.searchcriteria)
* Montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
