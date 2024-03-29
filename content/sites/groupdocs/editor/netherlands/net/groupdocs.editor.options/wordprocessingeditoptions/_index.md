---
title: WordProcessingEditOptions
second_title: GroupDocs.Editor voor .NET API-referentie
description: Maakt het mogelijk om aangepaste opties te specificeren voor het bewerken van documenten van alle ondersteunde WordProcessing Wordscompatibele formaten zoals DOCX RTF ODT etc.
type: docs
weight: 1200
url: /nl/net/groupdocs.editor.options/wordprocessingeditoptions/
---
## WordProcessingEditOptions class

Maakt het mogelijk om aangepaste opties te specificeren voor het bewerken van documenten van alle ondersteunde WordProcessing (Words-compatibele) formaten zoals DOC(X), RTF, ODT etc.

```csharp
public class WordProcessingEditOptions : IEditOptions
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [WordProcessingEditOptions](wordprocessingeditoptions#constructor)() | Maakt en retourneert een nieuwe instantie van de klasse WordProcessingEditOptions, waarin alle opties zijn ingesteld op hun standaardwaarden |
| [WordProcessingEditOptions](wordprocessingeditoptions#constructor_1)(bool) | Maakt en retourneert een nieuwe instantie van de klasse WordProcessingEditOptions met gespecificeerde paginering en standaard alle andere opties |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [EnableLanguageInformation](../../groupdocs.editor.options/wordprocessingeditoptions/enablelanguageinformation) { get; set; } | Geeft aan of taalinformatie wordt geëxporteerd naar de HTML-opmaak in de vorm van 'lang' HTML-attributen. Deze optie kan handig zijn voor roundtrip-conversie van de meertalige documenten. Standaard is het uitgeschakeld (false). |
| [EnablePagination](../../groupdocs.editor.options/wordprocessingeditoptions/enablepagination) { get; set; } | Hiermee kan paginering in het resulterende HTML-document worden in- of uitgeschakeld. Standaard is uitgeschakeld (false). |
| [ExtractOnlyUsedFont](../../groupdocs.editor.options/wordprocessingeditoptions/extractonlyusedfont) { get; set; } | Hiermee wordt een waarde opgehaald of ingesteld die aangeeft of alleen lettertypebronnen worden geëxtraheerd die worden gebruikt in de tekstuele inhoud van het document. |
| [FontExtraction](../../groupdocs.editor.options/wordprocessingeditoptions/fontextraction) { get; set; } | Verantwoordelijk voor het extraheren van lettertypebronnen, die worden gebruikt in het tekstverwerkingsdocument. Extraheert standaard geen lettertypen (NotExtract). |
| [InputControlsClassName](../../groupdocs.editor.options/wordprocessingeditoptions/inputcontrolsclassname) { get; set; } | Maakt het mogelijk om een klassenaam te specificeren, die wordt geplaatst bij de 'klasse'-attributen in elk HTML-element, die een bepaald veld vertegenwoordigt in het tekstverwerkingsdocument. Standaard is NULL - 'klasse'-attributen worden niet toegepast. |

### Zie ook

* interface [IEditOptions](../ieditoptions)
* naamruimte [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
