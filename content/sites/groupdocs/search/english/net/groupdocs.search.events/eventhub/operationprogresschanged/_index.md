---
title: OperationProgressChanged
second_title: GroupDocs.Search for .NET API Reference
description: Occurs when the progress of indexing or update operation is changed.
type: docs
weight: 40
url: /net/groupdocs.search.events/eventhub/operationprogresschanged/
---
## EventHub.OperationProgressChanged event

Occurs when the progress of indexing or update operation is changed.

```csharp
public event EventHandler<OperationProgressEventArgs> OperationProgressChanged;
```

### Examples

The example demonstrates how to use the event.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Creating an index
Index index = new Index(indexFolder);

// Subscribing to the event
index.Events.OperationProgressChanged += (sender, args) =>
{
    Console.WriteLine("Last processed: " + args.LastDocumentPath);
    Console.WriteLine("Result: " + args.LastDocumentStatus);
    Console.WriteLine("Processed documents: " + args.TotalDocuments);
    Console.WriteLine("Progress percentage: " + args.ProgressPercentage);
};

// Indexing documents from the specified folder
index.Add(documentsFolder);
```

### See Also

* class [OperationProgressEventArgs](../../operationprogresseventargs)
* class [EventHub](../../eventhub)
* namespace [GroupDocs.Search.Events](../../eventhub)
* assembly [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.search.dll -->