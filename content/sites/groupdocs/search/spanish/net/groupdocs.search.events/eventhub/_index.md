---
title: EventHub
second_title: GroupDocs.Buscar referencia de API de .NET
description: Proporciona eventos de índice para suscribirse.
type: docs
weight: 500
url: /es/net/groupdocs.search.events/eventhub/
---
## EventHub class

Proporciona eventos de índice para suscribirse.

```csharp
public class EventHub
```

## Eventos

| Nombre | Descripción |
| --- | --- |
| event [ErrorOccurred](../../groupdocs.search.events/eventhub/erroroccurred) | Ocurre cuando ocurre un error durante una operación de índice. |
| event [FileIndexing](../../groupdocs.search.events/eventhub/fileindexing) | Ocurre cuando se va a indexar un documento. |
| event [ImagePreparing](../../groupdocs.search.events/eventhub/imagepreparing) | Ocurre cuando se va a preparar una imagen para la indexación. |
| event [OperationFinished](../../groupdocs.search.events/eventhub/operationfinished) | Ocurre cuando finaliza una operación de indexación. |
| event [OperationProgressChanged](../../groupdocs.search.events/eventhub/operationprogresschanged) | Ocurre cuando se cambia el progreso de la indexación o la operación de actualización. |
| event [PasswordRequired](../../groupdocs.search.events/eventhub/passwordrequired) | Ocurre cuando un documento requiere contraseña para abrirlo. |
| event [SearchPhaseCompleted](../../groupdocs.search.events/eventhub/searchphasecompleted) | Ocurre cuando se completa la fase de búsqueda. |
| event [StatusChanged](../../groupdocs.search.events/eventhub/statuschanged) | Ocurre cuando cambia el estado del índice. |

### Observaciones

**Aprende más**

* [Buscar eventos de índice](https://docs.groupdocs.com/display/searchnet/Search+index+events)

### Ejemplos

El ejemplo demuestra un uso típico de la interfaz.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";

// Creando un índice
Index index = new Index(indexFolder);

// Suscribiendose al evento
index.Events.ErrorOccurred += (sender, args) =>
{
    Console.WriteLine(args.Message);
};

// Indexación de documentos de la carpeta especificada
index.Add(documentsFolder);

// Buscando en el índice
SearchResult result = index.Search(query);
```

### Ver también

* espacio de nombres [GroupDocs.Search.Events](../../groupdocs.search.events)
* asamblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->