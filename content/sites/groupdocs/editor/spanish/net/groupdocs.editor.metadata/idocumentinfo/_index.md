---
title: IDocumentInfo
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Interfaz común para todos los contenedores de metadatos de archivos
type: docs
weight: 740
url: /es/net/groupdocs.editor.metadata/idocumentinfo/
---
## IDocumentInfo interface

Interfaz común para todos los contenedores de metadatos de archivos

```csharp
public interface IDocumentInfo
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Format](../../groupdocs.editor.metadata/idocumentinfo/format) { get; } | Al implementar el tipo, debe devolver un formato de documento como un valor único de un tipo, que representa una familia de formatos y se hereda de la interfaz IDocumentFormat |
| [IsEncrypted](../../groupdocs.editor.metadata/idocumentinfo/isencrypted) { get; } | Indica si un archivo específico está encriptado y requiere contraseña para abrirlo. Para los tipos de documentos que no se pueden cifrar (como todos los basados en texto) siempre deben devolver 'falso'. |
| [PageCount](../../groupdocs.editor.metadata/idocumentinfo/pagecount) { get; } | Al implementar el tipo, debe devolver el recuento (número) de páginas u otras entidades similares dependientes del formato (pestañas, diapositivas, etc.). Para los tipos de familia que no tienen algo similar (como documentos de texto sin formato o XML) deben 1. |
| [Size](../../groupdocs.editor.metadata/idocumentinfo/size) { get; } | Tamaño del documento en bytes |

### Ver también

* espacio de nombres [GroupDocs.Editor.Metadata](../../groupdocs.editor.metadata)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
