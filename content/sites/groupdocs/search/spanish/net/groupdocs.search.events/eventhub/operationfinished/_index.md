---
title: OperationFinished
second_title: GroupDocs.Buscar referencia de API de .NET
description: Ocurre cuando finaliza una operación de indexación.
type: docs
weight: 40
url: /es/net/groupdocs.search.events/eventhub/operationfinished/
---
## EventHub.OperationFinished event

Ocurre cuando finaliza una operación de indexación.

```csharp
public event EventHandler<OperationFinishedEventArgs> OperationFinished;
```

### Ejemplos

El ejemplo demuestra cómo usar el evento.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Creando un índice
Index index = new Index(indexFolder);

// Suscribiendose al evento
index.Events.OperationFinished += (sender, args) =>
{
    Console.WriteLine("Operation finished: " + args.OperationType);
    Console.WriteLine("Message: " + args.Message);
    Console.WriteLine("Index folder: " + args.IndexFolder);
    Console.WriteLine("Time: " + args.Time);
};

// Indexación de documentos de la carpeta especificada
index.Add(documentsFolder);
```

### Ver también

* class [OperationFinishedEventArgs](../../operationfinishedeventargs)
* class [EventHub](../../eventhub)
* espacio de nombres [GroupDocs.Search.Events](../../eventhub)
* asamblea [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
