---
title: OperationProgressEventArgs
second_title: GroupDocs.Buscar referencia de API de .NET
description: Representa argumentos para el evento de actualización del progreso de la operación de indexación.
type: docs
weight: 560
url: /es/net/groupdocs.search.events/operationprogresseventargs/
---
## OperationProgressEventArgs class

Representa argumentos para el evento de actualización del progreso de la operación de indexación.

```csharp
public class OperationProgressEventArgs : BaseIndexEventArgs
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [IndexFolder](../../groupdocs.search.events/baseindexeventargs/indexfolder) { get; } | Obtiene la carpeta de índice. |
| [IndexId](../../groupdocs.search.events/baseindexeventargs/indexid) { get; } | Obtiene el ID del índice. |
| [LastDocumentKey](../../groupdocs.search.events/operationprogresseventargs/lastdocumentkey) { get; } | Obtiene la clave del último documento procesado. |
| [LastDocumentPath](../../groupdocs.search.events/operationprogresseventargs/lastdocumentpath) { get; } | Obtiene la ruta del último documento procesado. |
| [LastDocumentStatus](../../groupdocs.search.events/operationprogresseventargs/lastdocumentstatus) { get; } | Obtiene el estado del último documento procesado. |
| [ProcessedDocuments](../../groupdocs.search.events/operationprogresseventargs/processeddocuments) { get; } | Obtiene el número de documentos procesados con éxito. |
| [ProgressPercentage](../../groupdocs.search.events/operationprogresseventargs/progresspercentage) { get; } | Obtiene el porcentaje del progreso. |
| [SkippedDocuments](../../groupdocs.search.events/operationprogresseventargs/skippeddocuments) { get; } | Obtiene el número de documentos omitidos. |
| [Status](../../groupdocs.search.events/baseindexeventargs/status) { get; } | Obtiene el estado del índice. |
| [Time](../../groupdocs.search.events/baseindexeventargs/time) { get; } | Obtiene la hora de un evento. |
| [TotalDocuments](../../groupdocs.search.events/operationprogresseventargs/totaldocuments) { get; } | Obtiene el número total de documentos procesados. |

### Observaciones

**Aprende más**

* [Buscar eventos de índice](https://docs.groupdocs.com/display/searchnet/Search+index+events)

### Ver también

* class [BaseIndexEventArgs](../baseindexeventargs)
* espacio de nombres [GroupDocs.Search.Events](../../groupdocs.search.events)
* asamblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
