---
title: Content
second_title: GroupDocs.Watermark for .NET API-referens
description: Representerar ett innehåll där en vattenstämpel kan placeras.
type: docs
weight: 120
url: /sv/net/groupdocs.watermark.contents/content/
---
## Content class

Representerar ett innehåll där en vattenstämpel kan placeras.

```csharp
public abstract class Content : ContentPart, IDisposable
```

## Metoder

| namn | Beskrivning |
| --- | --- |
| [Dispose](../../groupdocs.watermark.contents/content/dispose)() | Tar bort den aktuella instansen. |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | Hittar alla bilder i innehållet. Sökningen utförs i de objekt som anges i[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Hittar bilder enligt de angivna sökkriterierna. Sökningen utförs i de objekt som anges i[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | Hittar alla möjliga vattenstämplar i innehållet. Sökningen utförs i de objekt som anges i[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Hittar möjliga vattenstämplar enligt angivna sökkriterier. Sökningen utförs i de objekt som anges i[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Se även

* class [ContentPart](../contentpart)
* namnutrymme [GroupDocs.Watermark.Contents](../../groupdocs.watermark.contents)
* hopsättning [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
