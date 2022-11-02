---
title: SearchReport
second_title: GroupDocs.Suche nach .NET-API-Referenz
description: Stellt detaillierte Informationen zu einem Suchvorgang dar.
type: docs
weight: 290
url: /de/net/groupdocs.search.common/searchreport/
---
## SearchReport class

Stellt detaillierte Informationen zu einem Suchvorgang dar.

```csharp
public class SearchReport
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [DocumentCount](../../groupdocs.search.common/searchreport/documentcount) { get; } | Ruft die Anzahl der gefundenen Dokumente ab. |
| [EndTime](../../groupdocs.search.common/searchreport/endtime) { get; } | Ruft die Endzeit der Suche ab. |
| [ObjectQuery](../../groupdocs.search.common/searchreport/objectquery) { get; } | Ruft die Suchanfrage in Objektform ab. |
| [OccurrenceCount](../../groupdocs.search.common/searchreport/occurrencecount) { get; } | Ruft die Gesamtzahl der gefundenen Vorkommen ab. |
| [SearchDuration](../../groupdocs.search.common/searchreport/searchduration) { get; } | Ruft die Suchdauer ab. |
| [SearchOptions](../../groupdocs.search.common/searchreport/searchoptions) { get; } | Ruft die Suchoptionen ab. |
| [StartTime](../../groupdocs.search.common/searchreport/starttime) { get; } | Ruft die Startzeit der Suche ab. |
| [TextQuery](../../groupdocs.search.common/searchreport/textquery) { get; } | Ruft die Suchanfrage in Textform ab. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| override [ToString](../../groupdocs.search.common/searchreport/tostring)() | Gibt a zurückString das repräsentiert den Strom[`SearchReport`](../searchreport) . |

### Bemerkungen

**Mehr erfahren**

* [Berichte suchen](https://docs.groupdocs.com/display/searchnet/Search+reports)

### Beispiele

Das Beispiel zeigt eine typische Verwendung der Klasse.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Index im angegebenen Ordner erstellen
Index index = new Index(indexFolder);

// Indizierung von Dokumenten aus dem angegebenen Ordner
index.Add(documentsFolder);

// Suche im Index
SearchResult result1 = index.Search("Einstein");
SearchResult result2 = index.Search("\"Theory of Relativity\"");

// Suchberichte abrufen
SearchReport[] reports = index.GetSearchReports();

// Berichte an die Konsole drucken
foreach (SearchReport report in reports)
{
    Console.WriteLine("Query: " + report.TextQuery);
    Console.WriteLine("Time: " + report.StartTime);
    Console.WriteLine("Duration: " + report.SearchDuration);
    Console.WriteLine("Documents: " + report.DocumentCount);
    Console.WriteLine("Occurrences: " + report.OccurrenceCount);
    Console.WriteLine();
}
```

### Siehe auch

* namensraum [GroupDocs.Search.Common](../../groupdocs.search.common)
* Montage [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->