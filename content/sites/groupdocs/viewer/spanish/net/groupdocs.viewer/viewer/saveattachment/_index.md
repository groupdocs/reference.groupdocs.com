---
title: SaveAttachment
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Guarda el archivo adjunto endestination flujo.
type: docs
weight: 60
url: /es/net/groupdocs.viewer/viewer/saveattachment/
---
## SaveAttachment(Attachment, Stream, CancellationToken) {#saveattachment_1}

Guarda el archivo adjunto en*destination* flujo.

```csharp
public void SaveAttachment(Attachment attachment, Stream destination, 
    CancellationToken cancellationToken)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| attachment | Attachment | El adjunto. |
| destination | Stream | El flujo de escritura. |
| cancellationToken | CancellationToken | Ficha de cancelación. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*attachment* es nulo. |
| ArgumentNullException | arrojado cuando*destination* es nulo. |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Se lanza cuando se requiere una contraseña para abrir el documento. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Se lanza cuando la contraseña que se especificó es incorrecta. |
| [GroupDocsViewerException](../../../groupdocs.viewer.exceptions/groupdocsviewerexception) | Lanzado cuando no se pudo encontrar el archivo adjunto. |

### Observaciones

**Aprende más**

* Obtenga más información sobre cómo obtener documentos adjuntos en C#: [Cómo obtener una lista de documentos adjuntos usando GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+attachments)
* Obtenga más información sobre cómo guardar documentos adjuntos en C#: [Cómo guardar documentos adjuntos usando GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Save+attachments)

### Ver también

* class [Attachment](../../../groupdocs.viewer.results/attachment)
* class [Viewer](../../viewer)
* espacio de nombres [GroupDocs.Viewer](../../viewer)
* asamblea [GroupDocs.Viewer](../../../)

---

## SaveAttachment(Attachment, Stream) {#saveattachment}

Guarda el archivo adjunto en*destination* flujo.

```csharp
public void SaveAttachment(Attachment attachment, Stream destination)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| attachment | Attachment | El adjunto. |
| destination | Stream | El flujo de escritura. |

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentNullException | arrojado cuando*attachment* es nulo. |
| ArgumentNullException | arrojado cuando*destination* es nulo. |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Se lanza cuando se requiere una contraseña para abrir el documento. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Se lanza cuando la contraseña que se especificó es incorrecta. |
| [GroupDocsViewerException](../../../groupdocs.viewer.exceptions/groupdocsviewerexception) | Lanzado cuando no se pudo encontrar el archivo adjunto. |

### Observaciones

**Aprende más**

* Obtenga más información sobre cómo obtener documentos adjuntos en C#: [Cómo obtener una lista de documentos adjuntos usando GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+attachments)
* Obtenga más información sobre cómo guardar documentos adjuntos en C#: [Cómo guardar documentos adjuntos usando GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Save+attachments)

### Ver también

* class [Attachment](../../../groupdocs.viewer.results/attachment)
* class [Viewer](../../viewer)
* espacio de nombres [GroupDocs.Viewer](../../viewer)
* asamblea [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
