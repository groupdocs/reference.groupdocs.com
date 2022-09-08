---
title: IndexingReport
second_title: GroupDocs.Search for .NET API Reference
description: Represents a detailed information on an indexing operation.
type: docs
weight: 200
url: /net/groupdocs.search.common/indexingreport/
---
## IndexingReport class

Represents a detailed information on an indexing operation.

```csharp
public class IndexingReport
```

## Properties

| Name | Description |
| --- | --- |
| [EndTime](../../groupdocs.search.common/indexingreport/endtime) { get; } | Gets the indexing end time. |
| [Errors](../../groupdocs.search.common/indexingreport/errors) { get; } | Gets the list of errors. |
| [IndexedDocuments](../../groupdocs.search.common/indexingreport/indexeddocuments) { get; } | Gets the list of indexed documents. |
| [IndexedDocumentsSize](../../groupdocs.search.common/indexingreport/indexeddocumentssize) { get; } | Gets the total length of indexed documents in MB. |
| [IndexingTime](../../groupdocs.search.common/indexingreport/indexingtime) { get; } | Gets the indexing duration. |
| [RemovedDocuments](../../groupdocs.search.common/indexingreport/removeddocuments) { get; } | Gets the list of removed from index documents. |
| [SegmentCount](../../groupdocs.search.common/indexingreport/segmentcount) { get; } | Gets the number of index segments. |
| [StartTime](../../groupdocs.search.common/indexingreport/starttime) { get; } | Gets the indexing start time. |
| [TotalDocumentsInIndex](../../groupdocs.search.common/indexingreport/totaldocumentsinindex) { get; } | Gets the total number of documents in the index. |
| [TotalIndexSize](../../groupdocs.search.common/indexingreport/totalindexsize) { get; } | Gets the total index size in bytes. |
| [TotalTermCount](../../groupdocs.search.common/indexingreport/totaltermcount) { get; } | Gets the total number of terms in index. |
| [UpdatedDocuments](../../groupdocs.search.common/indexingreport/updateddocuments) { get; } | Gets the list of updated documents. |

### Remarks

**Learn more**

* [Indexing reports](https://docs.groupdocs.com/display/searchnet/Indexing+reports)

### Examples

The example demonstrates a typical usage of the class.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder1 = @"c:\MyDocuments1\";
string documentsFolder2 = @"c:\MyDocuments2\";

// Creating an index in the specified folder
Index index = new Index(indexFolder);

// Indexing documents
index.Add(documentsFolder1);
index.Add(documentsFolder2);

// Getting indexing reports
IndexingReport[] reports = index.GetIndexingReports();

// Printing reports to the console
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

### See Also

* namespace [GroupDocs.Search.Common](../../groupdocs.search.common)
* assembly [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->