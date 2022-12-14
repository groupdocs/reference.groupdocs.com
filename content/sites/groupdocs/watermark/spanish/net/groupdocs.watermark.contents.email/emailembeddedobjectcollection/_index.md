---
title: EmailEmbeddedObjectCollection
second_title: Referencia de API de GroupDocs.Watermark para .NET
description: Representa una colección de objetos incrustados en un mensaje de correo electrónico.
type: docs
weight: 350
url: /es/net/groupdocs.watermark.contents.email/emailembeddedobjectcollection/
---
## EmailEmbeddedObjectCollection class

Representa una colección de objetos incrustados en un mensaje de correo electrónico.

```csharp
public class EmailEmbeddedObjectCollection : RemoveOnlyListBase<EmailEmbeddedObject>
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| virtual [Count](../../groupdocs.watermark.common/readonlylistbase-1/count) { get; } | Obtiene el número de elementos que contiene la colección. |
| override [IsReadOnly](../../groupdocs.watermark.common/removeonlylistbase-1/isreadonly) { get; } | Obtiene un valor que indica si la colección es de solo lectura. |
| virtual [Item](../../groupdocs.watermark.common/readonlylistbase-1/item) { get; } | Obtiene el elemento en el índice especificado en la colección. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [Add](../../groupdocs.watermark.contents.email/emailembeddedobjectcollection/add)(byte[], string) | Agrega un recurso incrustado al[`EmailContent`](../emailcontent) . |
| [Clear](../../groupdocs.watermark.common/removeonlylistbase-1/clear)() |  |
| virtual [Contains](../../groupdocs.watermark.common/readonlylistbase-1/contains)(EmailEmbeddedObject) |  |
| virtual [GetEnumerator](../../groupdocs.watermark.common/readonlylistbase-1/getenumerator)() |  |
| virtual [IndexOf](../../groupdocs.watermark.common/readonlylistbase-1/indexof)(EmailEmbeddedObject) |  |
| [Remove](../../groupdocs.watermark.common/removeonlylistbase-1/remove)(EmailEmbeddedObject) |  |
| [RemoveAt](../../groupdocs.watermark.common/removeonlylistbase-1/removeat)(int) |  |

### Observaciones

Esta colección contiene los elementos de[`EmailEmbeddedObject`](../emailembeddedobject) tipo.

### Ver también

* class [RemoveOnlyListBase&lt;T&gt;](../../groupdocs.watermark.common/removeonlylistbase-1)
* class [EmailEmbeddedObject](../emailembeddedobject)
* espacio de nombres [GroupDocs.Watermark.Contents.Email](../../groupdocs.watermark.contents.email)
* asamblea [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
