---
title: TextSplitOptions
second_title: GroupDocs.Merger voor .NET API-referentie
description: Biedt opties voor het splitsen van documenttekst.
type: docs
weight: 630
url: /nl/net/groupdocs.merger.domain.options/textsplitoptions/
---
## TextSplitOptions class

Biedt opties voor het splitsen van documenttekst.

```csharp
public class TextSplitOptions : ITextSplitOptions
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [TextSplitOptions](textsplitoptions#constructor_3)(CreateSplitStream, int[]) | Initialiseert een nieuw exemplaar van het[`TextSplitOptions`](../textsplitoptions) klasse. |
| [TextSplitOptions](textsplitoptions#constructor_5)(string, int[]) | Initialiseert een nieuw exemplaar van het[`TextSplitOptions`](../textsplitoptions) klasse. |
| [TextSplitOptions](textsplitoptions#constructor_1)(CreateSplitStream, ReleaseSplitStream, int[]) | Initialiseert een nieuw exemplaar van het[`TextSplitOptions`](../textsplitoptions) klasse. |
| [TextSplitOptions](textsplitoptions#constructor_2)(CreateSplitStream, TextSplitMode, int[]) | Initialiseert een nieuw exemplaar van het[`TextSplitOptions`](../textsplitoptions) klasse. |
| [TextSplitOptions](textsplitoptions#constructor_4)(string, TextSplitMode, int[]) | Initialiseert een nieuw exemplaar van het[`TextSplitOptions`](../textsplitoptions) klasse. |
| [TextSplitOptions](textsplitoptions#constructor)(CreateSplitStream, ReleaseSplitStream, TextSplitMode, int[]) | Initialiseert een nieuw exemplaar van het[`TextSplitOptions`](../textsplitoptions) klasse. |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [CreateStream](../../groupdocs.merger.domain.options/textsplitoptions/createstream) { get; } | Delegate die de methode definieert om output split stream te creëren. |
| [LineNumbers](../../groupdocs.merger.domain.options/textsplitoptions/linenumbers) { get; } | Regelnummers voor tekstsplitsing. |
| [Mode](../../groupdocs.merger.domain.options/textsplitoptions/mode) { get; } | Modus voor het splitsen van tekst. |
| [ReleaseStream](../../groupdocs.merger.domain.options/textsplitoptions/releasestream) { get; } | Delegate die de methode definieert om output split stream vrij te geven. |

## methoden

| Naam | Beschrijving |
| --- | --- |
| [GetPathByIndex](../../groupdocs.merger.domain.options/textsplitoptions/getpathbyindex)(int, string) | Haalt het volledige bestandspad op van een gesplitst document per index met gedefinieerde extensie. |
| [Validate](../../groupdocs.merger.domain.options/textsplitoptions/validate)(FileType) | Valideert de splitsingsopties. |

### Zie ook

* interface [ITextSplitOptions](../itextsplitoptions)
* naamruimte [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* montage [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
