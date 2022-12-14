---
title: ReadOnlyListT
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Proporciona una clase base abstracta para una lista de solo lectura fuertemente tipada.
type: docs
weight: 220
url: /es/net/groupdocs.metadata.common/readonlylist-1/
---
## ReadOnlyList&lt;T&gt; class

Proporciona una clase base abstracta para una lista de solo lectura fuertemente tipada.

```csharp
public class ReadOnlyList<T> : IList, IList<T>, IReadOnlyList<T>
```

| Parámetro | Descripción |
| --- | --- |
| T | El tipo del elemento. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Count](../../groupdocs.metadata.common/readonlylist-1/count) { get; } | Obtiene el número de elementos que contiene la colección. |
| [IsReadOnly](../../groupdocs.metadata.common/readonlylist-1/isreadonly) { get; } | Obtiene un valor que indica si la colección es de solo lectura. |
| [Item](../../groupdocs.metadata.common/readonlylist-1/item) { get; } | Obtiene el elemento en el índice especificado en la colección. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [Contains](../../groupdocs.metadata.common/readonlylist-1/contains)(T) | Determina si la colección contiene un elemento específico. |
| [GetEnumerator](../../groupdocs.metadata.common/readonlylist-1/getenumerator)() | Devuelve un enumerador que itera a través de una colección. |
| [IndexOf](../../groupdocs.metadata.common/readonlylist-1/indexof)(T) | Determina el índice de un elemento específico de la colección. |

### Ver también

* interface [IReadOnlyList&lt;T&gt;](../ireadonlylist-1)
* espacio de nombres [GroupDocs.Metadata.Common](../../groupdocs.metadata.common)
* asamblea [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
