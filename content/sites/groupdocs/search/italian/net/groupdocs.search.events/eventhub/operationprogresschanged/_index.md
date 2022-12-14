---
title: OperationProgressChanged
second_title: GroupDocs.Cerca il riferimento dell'API .NET
description: Si verifica quando lavanzamento dellindicizzazione o delloperazione di aggiornamento viene modificato.
type: docs
weight: 50
url: /it/net/groupdocs.search.events/eventhub/operationprogresschanged/
---
## EventHub.OperationProgressChanged event

Si verifica quando l'avanzamento dell'indicizzazione o dell'operazione di aggiornamento viene modificato.

```csharp
public event EventHandler<OperationProgressEventArgs> OperationProgressChanged;
```

### Esempi

L'esempio mostra come utilizzare l'evento.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Creazione di un indice
Index index = new Index(indexFolder);

// Iscrizione all'evento
index.Events.OperationProgressChanged += (sender, args) =>
{
    Console.WriteLine("Last processed: " + args.LastDocumentPath);
    Console.WriteLine("Result: " + args.LastDocumentStatus);
    Console.WriteLine("Processed documents: " + args.TotalDocuments);
    Console.WriteLine("Progress percentage: " + args.ProgressPercentage);
};

// Indicizzazione dei documenti dalla cartella specificata
index.Add(documentsFolder);
```

### Guarda anche

* class [OperationProgressEventArgs](../../operationprogresseventargs)
* class [EventHub](../../eventhub)
* spazio dei nomi [GroupDocs.Search.Events](../../eventhub)
* assemblea [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
