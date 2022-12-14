---
title: OperationFinished
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Se produit lorsquune opération dindex est terminée.
type: docs
weight: 40
url: /fr/net/groupdocs.search.events/eventhub/operationfinished/
---
## EventHub.OperationFinished event

Se produit lorsqu'une opération d'index est terminée.

```csharp
public event EventHandler<OperationFinishedEventArgs> OperationFinished;
```

### Exemples

L'exemple montre comment utiliser l'événement.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Création d'un index
Index index = new Index(indexFolder);

// S'inscrire à l'événement
index.Events.OperationFinished += (sender, args) =>
{
    Console.WriteLine("Operation finished: " + args.OperationType);
    Console.WriteLine("Message: " + args.Message);
    Console.WriteLine("Index folder: " + args.IndexFolder);
    Console.WriteLine("Time: " + args.Time);
};

// Indexation des documents du dossier spécifié
index.Add(documentsFolder);
```

### Voir également

* class [OperationFinishedEventArgs](../../operationfinishedeventargs)
* class [EventHub](../../eventhub)
* espace de noms [GroupDocs.Search.Events](../../eventhub)
* Assemblée [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
