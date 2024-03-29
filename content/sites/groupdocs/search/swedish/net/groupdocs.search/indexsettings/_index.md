---
title: IndexSettings
second_title: GroupDocs.Search efter .NET API Reference
description: Representerar indexinställningarna som gör det möjligt att anpassa indexeringsoperationerna.
type: docs
weight: 700
url: /sv/net/groupdocs.search/indexsettings/
---
## IndexSettings class

Representerar indexinställningarna som gör det möjligt att anpassa indexeringsoperationerna.

```csharp
public class IndexSettings
```

## Konstruktörer

| namn | Beskrivning |
| --- | --- |
| [IndexSettings](indexsettings)() | Initierar en ny instans av[`IndexSettings`](../indexsettings) class. |

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [AutoDetectEncoding](../../groupdocs.search/indexsettings/autodetectencoding) { get; set; } | Hämtar eller ställer in ett värde som anger om kodning ska detekteras automatiskt eller inte. Standardvärdet är`falsk` . |
| [CustomExtractors](../../groupdocs.search/indexsettings/customextractors) { get; } | Hämtar den anpassade extraktionssamlingen. |
| [DocumentFilter](../../groupdocs.search/indexsettings/documentfilter) { get; set; } | Hämtar eller ställer in ett dokumentfilter. Den[`DocumentFilter`](./documentfilter) fungerar på inkluderingslogiken. Använd[`DocumentFilter`](../../groupdocs.search.options/documentfilter) klass för att skapa ett dokumentfilterinstanser. Standardvärdet är`null` , vilket innebär att alla tillagda dokument indexeras. |
| [IndexType](../../groupdocs.search/indexsettings/indextype) { get; set; } | Hämtar eller ställer in indextypen. Standardvärdet ärNormalIndex . |
| [InMemoryIndex](../../groupdocs.search/indexsettings/inmemoryindex) { get; } | Får ett värde som indikerar om indexet är lagrat i minnet eller på disken. |
| [Logger](../../groupdocs.search/indexsettings/logger) { get; set; } | Hämtar eller ställer in en logger som används för att logga händelser och fel i indexet. Observera att loggern inte sparas och måste skapas och tilldelas varje gång indexet skapas eller laddas. |
| [MaxIndexingReportCount](../../groupdocs.search/indexsettings/maxindexingreportcount) { get; set; } | Hämtar eller ställer in det maximala antalet indexeringsrapporter. Standardvärdet är`5` . |
| [MaxSearchReportCount](../../groupdocs.search/indexsettings/maxsearchreportcount) { get; set; } | Hämtar eller ställer in det maximala antalet sökrapporter. Standardvärdet är`10` . |
| [SearchThreads](../../groupdocs.search/indexsettings/searchthreads) { get; set; } | Hämtar eller ställer in antalet trådar som används för sökningen. Standardvärdet ärDefault , vilket innebär att sökningen kommer att utföras med antalet trådar lika med antalet processorkärnor. |
| [TextStorageSettings](../../groupdocs.search/indexsettings/textstoragesettings) { get; set; } | Hämtar eller ställer in textlagringsinställningarna. Standardvärdet är`null` , vilket innebär att dokumenttexter inte lagras. |
| [UseCharacterReplacements](../../groupdocs.search/indexsettings/usecharacterreplacements) { get; set; } | Hämtar eller ställer in ett värde som anger om teckenersättning ska användas eller inte. Standardvärdet är`falsk` . |
| [UseRawTextExtraction](../../groupdocs.search/indexsettings/userawtextextraction) { get; set; } | Hämtar eller ställer in ett värde som anger om råläget används för textextraktion om möjligt. Standardvärdet är`Sann` . Råläget kan öka indexeringshastigheten avsevärt, men normalt läge förbättrar formateringen av den extraherade texten. |
| [UseStopWords](../../groupdocs.search/indexsettings/usestopwords) { get; set; } | Hämtar eller ställer in ett värde som anger om stoppord ska användas eller inte. Standardvärdet är`Sann` . |

### Anmärkningar

**Läs mer**

* [Sök indexinställningar](https://docs.groupdocs.com/display/searchnet/Search+index+settings)

### Exempel

Exemplet visar en typisk användning av klassen.

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex; // Ställa in indextypen

Index index = new Index(indexFolder, settings); // Skapa ett index
```

### Se även

* namnutrymme [GroupDocs.Search](../../groupdocs.search)
* hopsättning [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
