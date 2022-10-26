---
title: GetResourceFilter
second_title: Referencia de API de GroupDocs.Viewer para .NET
description: Devuelve la cadena de filtro para buscar entradas de caché que representanResourcegroupdocs.viewer.results/resource objetos.
type: docs
weight: 60
url: /es/net/groupdocs.viewer.caching/cachekeys/getresourcefilter/
---
## CacheKeys.GetResourceFilter method

Devuelve la cadena de filtro para buscar entradas de caché que representan[`Resource`](../../../groupdocs.viewer.results/resource) objetos.

```csharp
public static string GetResourceFilter(int pageNumber)
```

| Parámetro | Escribe | Descripción |
| --- | --- | --- |
| pageNumber | Int32 | El número de página. |

### Valor_devuelto

Cadena de filtro para buscar entradas de caché que representen[`Resource`](../../../groupdocs.viewer.results/resource) objetos.

### Excepciones

| excepción | condición |
| --- | --- |
| ArgumentException | arrojado cuando*pageNumber* es menor o igual a cero. |

### Ver también

* class [CacheKeys](../../cachekeys)
* espacio de nombres [GroupDocs.Viewer.Caching](../../cachekeys)
* asamblea [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->