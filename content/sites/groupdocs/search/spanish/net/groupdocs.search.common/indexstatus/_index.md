---
title: IndexStatus
second_title: GroupDocs.Buscar referencia de API de .NET
description: Especifica un estado de índice.
type: docs
weight: 230
url: /es/net/groupdocs.search.common/indexstatus/
---
## IndexStatus enumeration

Especifica un estado de índice.

```csharp
public enum IndexStatus
```

### Valores

| Nombre | Valor | Descripción |
| --- | --- | --- |
| Ready | `0` | El índice es gratuito y está listo para cambiar. |
| Failed | `1` | El índice debe recargarse debido a un error. |
| Indexing | `2` | Index realiza una operación de indexación. |
| Updating | `3` | Index realiza una operación de actualización. |
| Merging | `4` | Index realiza una operación de fusión. |
| Optimizing | `5` | Index realiza una operación de optimización. |
| Deleting | `6` | Index realiza una operación de borrado. |
| Renaming | `7` | Index realiza una operación de cambio de nombre. |
| ChangingAttributes | `8` | Índice cambia atributos. |

### Ver también

* espacio de nombres [GroupDocs.Search.Common](../../groupdocs.search.common)
* asamblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->