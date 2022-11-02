---
title: PreviewOptions
second_title: GroupDocs.Merger für .NET-API-Referenz
description: Steht für Dokumentvorschauoptionen.
type: docs
weight: 530
url: /de/net/groupdocs.merger.domain.options/previewoptions/
---
## PreviewOptions class

Steht für Dokumentvorschauoptionen.

```csharp
public class PreviewOptions : PageOptions, IPreviewOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [PreviewOptions](previewoptions#constructor_4)(CreatePageStream, PreviewMode) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |
| [PreviewOptions](previewoptions#constructor_7)(CreatePageStream, PreviewMode, int[]) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |
| [PreviewOptions](previewoptions#constructor)(CreatePageStream, ReleasePageStream, PreviewMode) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |
| [PreviewOptions](previewoptions#constructor_5)(CreatePageStream, PreviewMode, int, int) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |
| [PreviewOptions](previewoptions#constructor_3)(CreatePageStream, ReleasePageStream, PreviewMode, int[]) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |
| [PreviewOptions](previewoptions#constructor_6)(CreatePageStream, PreviewMode, int, int, RangeMode) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |
| [PreviewOptions](previewoptions#constructor_1)(CreatePageStream, ReleasePageStream, PreviewMode, int, int) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |
| [PreviewOptions](previewoptions#constructor_2)(CreatePageStream, ReleasePageStream, PreviewMode, int, int, RangeMode) | Initialisiert eine neue Instanz von[`PreviewOptions`](../previewoptions) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [CreateStream](../../groupdocs.merger.domain.options/previewoptions/createstream) { get; } | Delegierter, der die Methode zum Erstellen des Vorschaustreams der Ausgabeseite definiert. |
| [Height](../../groupdocs.merger.domain.options/previewoptions/height) { get; set; } | Vorschauhöhe. |
| [Mode](../../groupdocs.merger.domain.options/previewoptions/mode) { get; } | Modus für Vorschau. |
| [Pages](../../groupdocs.merger.domain.options/pageoptions/pages) { get; } | Sammlung von Seitenzahlen abrufen. |
| [ReleaseStream](../../groupdocs.merger.domain.options/previewoptions/releasestream) { get; } | Delegierter, der die Methode zum Freigeben des Vorschaustreams der Ausgabeseite definiert. |
| [Width](../../groupdocs.merger.domain.options/previewoptions/width) { get; set; } | Vorschaubreite. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [GetPathByPageNumber](../../groupdocs.merger.domain.options/previewoptions/getpathbypagenumber)(int, string) | Ruft den vollständigen Dateipfad des in der Vorschau angezeigten Dokuments nach Seitenzahl mit definierter Erweiterung ab. |
| [Validate](../../groupdocs.merger.domain.options/previewoptions/validate)(FileType) | Validiert die Vorschauoptionen. |

### Siehe auch

* class [PageOptions](../pageoptions)
* interface [IPreviewOptions](../ipreviewoptions)
* namensraum [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* Montage [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->