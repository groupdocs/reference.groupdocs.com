---
title: CreateLazy
second_title: GroupDocs.Buscar referencia de API de .NET
description: Crea un documento con carga diferida.
type: docs
weight: 40
url: /es/net/groupdocs.search.common/document/createlazy/
---
## Document.CreateLazy method

Crea un documento con carga diferida.

```csharp
public static Document CreateLazy(DocumentSourceKind documentSourceKind, string documentKey, 
    IDocumentLoader documentLoader)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| documentSourceKind | DocumentSourceKind | El tipo de fuente del documento. Este valor debe coincidir con el tipo de documento cargado. |
| documentKey | String | La clave del documento. Este valor debe coincidir con la clave del documento cargado. |
| documentLoader | IDocumentLoader | El cargador de documentos. |

### Valor_devuelto

El documento creado.

### Ver también

* enum [DocumentSourceKind](../../documentsourcekind)
* interface [IDocumentLoader](../../idocumentloader)
* class [Document](../../document)
* espacio de nombres [GroupDocs.Search.Common](../../document)
* asamblea [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->