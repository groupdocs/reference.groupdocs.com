---
title: StatusChanged
second_title: GroupDocs.Buscar referencia de API de .NET
description: Ocurre cuando cambia el estado del índice.
type: docs
weight: 80
url: /es/net/groupdocs.search.events/eventhub/statuschanged/
---
## EventHub.StatusChanged event

Ocurre cuando cambia el estado del índice.

```csharp
public event EventHandler<BaseIndexEventArgs> StatusChanged;
```

### Ejemplos

El ejemplo demuestra cómo usar el evento.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// Creando un índice
Index index = new Index(indexFolder);

// Suscribiendose al evento
index.Events.StatusChanged += (sender, args) =>
{
    if (args.Status != IndexStatus.InProgress)
    {
        // Una notificación de la finalización de la operación debe estar aquí
    }
};

// Estableciendo la bandera para la indexación asíncrona
IndexingOptions options = new IndexingOptions();
options.IsAsync = true;

// Documentos de indexación asincrónica de la carpeta especificada
// El método termina antes de que se complete la operación
index.Add(documentsFolder, options);
```

### Ver también

* class [BaseIndexEventArgs](../../baseindexeventargs)
* class [EventHub](../../eventhub)
* espacio de nombres [GroupDocs.Search.Events](../../eventhub)
* asamblea [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->