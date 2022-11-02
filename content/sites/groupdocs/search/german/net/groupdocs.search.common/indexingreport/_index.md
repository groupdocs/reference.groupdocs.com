---
title: IndexingReport
second_title: GroupDocs.Suche nach .NET-API-Referenz
description: Stellt detaillierte Informationen zu einem Indizierungsvorgang dar.
type: docs
weight: 240
url: /de/net/groupdocs.search.common/indexingreport/
---
## IndexingReport class

Stellt detaillierte Informationen zu einem Indizierungsvorgang dar.

```csharp
public class IndexingReport
```

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [EndTime](../../groupdocs.search.common/indexingreport/endtime) { get; } | Ruft die Endzeit der Indizierung ab. |
| [Errors](../../groupdocs.search.common/indexingreport/errors) { get; } | Ruft die Fehlerliste ab. |
| [IndexedDocuments](../../groupdocs.search.common/indexingreport/indexeddocuments) { get; } | Ruft die Liste der indizierten Dokumente ab. |
| [IndexedDocumentsSize](../../groupdocs.search.common/indexingreport/indexeddocumentssize) { get; } | Ruft die Gesamtlänge der indizierten Dokumente in MB ab. |
| [IndexingTime](../../groupdocs.search.common/indexingreport/indexingtime) { get; } | Ruft die Indizierungsdauer ab. |
| [RemovedDocuments](../../groupdocs.search.common/indexingreport/removeddocuments) { get; } | Ruft die Liste der aus dem Index entfernten Dokumente ab. |
| [SegmentCount](../../groupdocs.search.common/indexingreport/segmentcount) { get; } | Ruft die Anzahl der Indexsegmente ab. |
| [StartTime](../../groupdocs.search.common/indexingreport/starttime) { get; } | Ruft die Startzeit der Indizierung ab. |
| [TotalDocumentsInIndex](../../groupdocs.search.common/indexingreport/totaldocumentsinindex) { get; } | Ruft die Gesamtzahl der Dokumente im Index ab. |
| [TotalIndexSize](../../groupdocs.search.common/indexingreport/totalindexsize) { get; } | Ruft die Gesamtindexgröße in Byte ab. |
| [TotalTermCount](../../groupdocs.search.common/indexingreport/totaltermcount) { get; } | Ruft die Gesamtzahl der Begriffe im Index ab. |
| [UpdatedDocuments](../../groupdocs.search.common/indexingreport/updateddocuments) { get; } | Ruft die Liste der aktualisierten Dokumente ab. |

### Bemerkungen

**Mehr erfahren**

* [Indizierung von Berichten](https://docs.groupdocs.com/display/searchnet/Indexing+reports)

### Beispiele

Das Beispiel zeigt eine typische Verwendung der Klasse.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder1 = @"c:\MyDocuments1\";
string documentsFolder2 = @"c:\MyDocuments2\";

// Index im angegebenen Ordner erstellen
Index index = new Index(indexFolder);

// Indizierung von Dokumenten
index.Add(documentsFolder1);
index.Add(documentsFolder2);

// Abrufen von Indizierungsberichten
IndexingReport[] reports = index.GetIndexingReports();

// Berichte an die Konsole drucken
foreach (IndexingReport report in reports)
{
    Console.WriteLine("Time: " + report.StartTime);
    Console.WriteLine("Duration: " + report.IndexingTime);
    Console.WriteLine("Documents total: " + report.TotalDocumentsInIndex);
    Console.WriteLine("Terms total: " + report.TotalTermCount);
    Console.WriteLine("Indexed documents size (MB): " + report.IndexedDocumentsSize);
    Console.WriteLine("Index size (MB): " + (report.TotalIndexSize / 1024.0 / 1024.0));
    Console.WriteLine();
}
```

### Siehe auch

* namensraum [GroupDocs.Search.Common](../../groupdocs.search.common)
* Montage [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->