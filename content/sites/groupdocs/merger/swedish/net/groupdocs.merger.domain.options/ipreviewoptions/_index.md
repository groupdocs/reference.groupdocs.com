---
title: IPreviewOptions
second_title: GroupDocs.Merger för .NET API-referens
description: Gränssnitt för förhandsgranskningsalternativen.
type: docs
weight: 290
url: /sv/net/groupdocs.merger.domain.options/ipreviewoptions/
---
## IPreviewOptions interface

Gränssnitt för förhandsgranskningsalternativen.

```csharp
public interface IPreviewOptions : IPageOptions
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [CreateStream](../../groupdocs.merger.domain.options/ipreviewoptions/createstream) { get; } | Delegat som definierar metod för att skapa förhandsvisningsström för utdatasida. |
| [Height](../../groupdocs.merger.domain.options/ipreviewoptions/height) { get; set; } | Förhandsgranskningshöjd. |
| [Mode](../../groupdocs.merger.domain.options/ipreviewoptions/mode) { get; } | Hämtar läge för förhandsgranskning. |
| [ReleaseStream](../../groupdocs.merger.domain.options/ipreviewoptions/releasestream) { get; } | Delegat som definierar metod för att frigöra förhandsvisningsström för utdatasida. |
| [Width](../../groupdocs.merger.domain.options/ipreviewoptions/width) { get; set; } | Förhandsgranskningsbredd. |

## Metoder

| namn | Beskrivning |
| --- | --- |
| [GetPathByPageNumber](../../groupdocs.merger.domain.options/ipreviewoptions/getpathbypagenumber)(int, string) | Får den fullständiga sökvägen för det förhandsgranskade dokumentet efter sidnummer med definierat tillägg. |
| [Validate](../../groupdocs.merger.domain.options/ipreviewoptions/validate)(FileType) | Validerar delade alternativen. |

### Se även

* interface [IPageOptions](../ipageoptions)
* namnutrymme [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* hopsättning [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
