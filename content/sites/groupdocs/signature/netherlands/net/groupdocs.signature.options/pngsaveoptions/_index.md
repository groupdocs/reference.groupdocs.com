---
title: PngSaveOptions
second_title: GroupDocs.Signature voor .NET API-referentie
description: Png Bewaar opties voor afbeeldingsdocumenten.
type: docs
weight: 1560
url: /nl/net/groupdocs.signature.options/pngsaveoptions/
---
## PngSaveOptions class

Png Bewaar opties voor afbeeldingsdocumenten.

```csharp
public sealed class PngSaveOptions : ImageSaveOptions
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [PngSaveOptions](pngsaveoptions)() | Creëert PngSaveOptions met standaardwaarden. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Haalt de vlag op of stelt deze in om automatisch een extensie toe te voegen wanneer deze ontbrak in uitvoerbestand path Standaardwaarde is false. |
| [BitDepth](../../groupdocs.signature.options/pngsaveoptions/bitdepth) { get; set; } | De bitdiepte. |
| [ColorType](../../groupdocs.signature.options/pngsaveoptions/colortype) { get; set; } | Haalt of stelt het type in van de[`PngColorType`](../pngcolortype) . |
| [CompressionLevel](../../groupdocs.signature.options/pngsaveoptions/compressionlevel) { get; set; } | Het compressieniveau van png-afbeeldingen in het bereik 0-9, waarbij 9 maximale compressie is en 0 de opslagmodus is. |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | Haalt het bestandsformaat van het ondertekende document op of stelt het in. |
| [FilterType](../../groupdocs.signature.options/pngsaveoptions/filtertype) { get; set; } | Haalt of stelt het filtertype in[`PngFilterType`](../pngfiltertype) gebruikt tijdens het opslaan van png-bestanden. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Haalt op of stelt in of een bestaand bestand moet worden overschreven met een nieuw uitvoerbestand. Anders wordt er een nieuw bestand gemaakt met nummer als achtervoegsel. Standaard is deze waarde ingesteld op true, wat betekent dat het bestand wordt overschreven. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | Krijgt of stelt wachtwoord in om ondertekend document op te slaan met wachtwoordbeveiliging. Deze eigenschap wordt niet ondersteund voor afbeeldingsdocumenten. |
| [Progressive](../../groupdocs.signature.options/pngsaveoptions/progressive) { get; set; } | Krijgt of stelt een waarde in die aangeeft of deze PngSaveOptions progressief is. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | Haalt of stelt in of het wachtwoord van LoadOptions moet worden gebruikt om ondertekend document als beveiligd op te slaan. Standaardwaarde is waar. Deze eigenschap wordt niet ondersteund voor afbeeldingsdocumenten. |

### Zie ook

* class [ImageSaveOptions](../imagesaveoptions)
* naamruimte [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* montage [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
