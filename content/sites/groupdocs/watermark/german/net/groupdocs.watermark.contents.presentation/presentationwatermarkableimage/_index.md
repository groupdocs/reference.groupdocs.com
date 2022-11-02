---
title: PresentationWatermarkableImage
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Stellt ein Bild in einem PowerPointDokument dar.
type: docs
weight: 1020
url: /de/net/groupdocs.watermark.contents.presentation/presentationwatermarkableimage/
---
## PresentationWatermarkableImage class

Stellt ein Bild in einem PowerPoint-Dokument dar.

```csharp
public class PresentationWatermarkableImage : WatermarkableImage
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [PresentationWatermarkableImage](presentationwatermarkableimage)(byte[]) | Initialisiert eine neue Instanz von[`PresentationWatermarkableImage`](../presentationwatermarkableimage) -Klasse mit angegebenen Bilddaten. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [Height](../../groupdocs.watermark.contents.image/watermarkableimage/height) { get; } | Ruft die Höhe davon ab[`WatermarkableImage`](../../groupdocs.watermark.contents.image/watermarkableimage) in Pixel. |
| [Width](../../groupdocs.watermark.contents.image/watermarkableimage/width) { get; } | Ruft die Breite davon ab[`WatermarkableImage`](../../groupdocs.watermark.contents.image/watermarkableimage) in Pixel. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [Add](../../groupdocs.watermark.contents.image/watermarkableimage/add)(Watermark) | Fügt ein Wasserzeichen hinzu[`WatermarkableImage`](../../groupdocs.watermark.contents.image/watermarkableimage). Diese Methode geht davon aus, dass Offset und Größe des Wasserzeichens in Pixel gemessen werden (sofern zugewiesen). |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | Findet alle Bilder im Inhalt. Die Suche wird in den angegebenen Objekten durchgeführt[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Findet Bilder nach den angegebenen Suchkriterien. Die Suche wird in den angegebenen Objekten durchgeführt[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [GetBytes](../../groupdocs.watermark.contents.image/watermarkableimage/getbytes)() | Ruft das Bild als Byte-Array ab. |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | Findet alle möglichen Wasserzeichen im Inhalt. Die Suche wird in den in angegebenen Objekten durchgeführt[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Findet mögliche Wasserzeichen nach vorgegebenen Suchkriterien. Die Suche wird in den in angegebenen Objekten durchgeführt[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Siehe auch

* class [WatermarkableImage](../../groupdocs.watermark.contents.image/watermarkableimage)
* namensraum [GroupDocs.Watermark.Contents.Presentation](../../groupdocs.watermark.contents.presentation)
* Montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->