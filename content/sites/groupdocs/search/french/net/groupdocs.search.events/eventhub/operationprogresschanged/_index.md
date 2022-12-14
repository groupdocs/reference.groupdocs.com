---
title: OperationProgressChanged
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Se produit lorsque la progression de lindexation ou de lopération de mise à jour est modifiée.
type: docs
weight: 50
url: /fr/net/groupdocs.search.events/eventhub/operationprogresschanged/
---
## EventHub.OperationProgressChanged event

Se produit lorsque la progression de l'indexation ou de l'opération de mise à jour est modifiée.

```csharp
public event EventHandler<OperationProgressEventArgs> OperationProgressChanged;
```

### Exemples

L'exemple montre comment utiliser l'événement.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Création d'un index
Index index = new Index(indexFolder);

// S'inscrire à l'événement
index.Events.OperationProgressChanged += (sender, args) =>
{
    Console.WriteLine("Last processed: " + args.LastDocumentPath);
    Console.WriteLine("Result: " + args.LastDocumentStatus);
    Console.WriteLine("Processed documents: " + args.TotalDocuments);
    Console.WriteLine("Progress percentage: " + args.ProgressPercentage);
};

// Indexation des documents du dossier spécifié
index.Add(documentsFolder);
```

### Voir également

* class [OperationProgressEventArgs](../../operationprogresseventargs)
* class [EventHub](../../eventhub)
* espace de noms [GroupDocs.Search.Events](../../eventhub)
* Assemblée [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
