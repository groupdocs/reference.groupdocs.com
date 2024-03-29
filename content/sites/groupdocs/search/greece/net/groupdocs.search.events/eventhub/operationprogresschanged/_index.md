---
title: OperationProgressChanged
second_title: GroupDocs.Αναζήτηση για αναφορά API .NET
description: Εμφανίζεται όταν αλλάζει η πρόοδος της λειτουργίας ευρετηρίασης ή ενημέρωσης.
type: docs
weight: 50
url: /el/net/groupdocs.search.events/eventhub/operationprogresschanged/
---
## EventHub.OperationProgressChanged event

Εμφανίζεται όταν αλλάζει η πρόοδος της λειτουργίας ευρετηρίασης ή ενημέρωσης.

```csharp
public event EventHandler<OperationProgressEventArgs> OperationProgressChanged;
```

### Παραδείγματα

Το παράδειγμα δείχνει πώς να χρησιμοποιήσετε το συμβάν.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Δημιουργία ευρετηρίου
Index index = new Index(indexFolder);

// Εγγραφή στην εκδήλωση
index.Events.OperationProgressChanged += (sender, args) =>
{
    Console.WriteLine("Last processed: " + args.LastDocumentPath);
    Console.WriteLine("Result: " + args.LastDocumentStatus);
    Console.WriteLine("Processed documents: " + args.TotalDocuments);
    Console.WriteLine("Progress percentage: " + args.ProgressPercentage);
};

// Δημιουργία ευρετηρίου εγγράφων από τον καθορισμένο φάκελο
index.Add(documentsFolder);
```

### Δείτε επίσης

* class [OperationProgressEventArgs](../../operationprogresseventargs)
* class [EventHub](../../eventhub)
* χώρος ονομάτων [GroupDocs.Search.Events](../../eventhub)
* συνέλευση [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
