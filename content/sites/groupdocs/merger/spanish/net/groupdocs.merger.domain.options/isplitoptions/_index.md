---
title: ISplitOptions
second_title: Referencia de API de GroupDocs.Merger para .NET
description: Interfaz para las opciones de división de páginas.
type: docs
weight: 340
url: /es/net/groupdocs.merger.domain.options/isplitoptions/
---
## ISplitOptions interface

Interfaz para las opciones de división de páginas.

```csharp
public interface ISplitOptions : IPageOptions
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [CreateStream](../../groupdocs.merger.domain.options/isplitoptions/createstream) { get; } | Delegado que define el método para crear un flujo dividido de salida. |
| [Mode](../../groupdocs.merger.domain.options/isplitoptions/mode) { get; } | Obtiene el modo de división de páginas. |
| [ReleaseStream](../../groupdocs.merger.domain.options/isplitoptions/releasestream) { get; } | Delegado que define el método para liberar el flujo dividido de salida. |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [GetPathByIndex](../../groupdocs.merger.domain.options/isplitoptions/getpathbyindex)(int, string) | Obtiene la ruta completa del archivo del documento dividido por índice con extensión definida. |
| [Validate](../../groupdocs.merger.domain.options/isplitoptions/validate)(FileType) | Valida las opciones de split. |

### Ver también

* interface [IPageOptions](../ipageoptions)
* espacio de nombres [GroupDocs.Merger.Domain.Options](../../groupdocs.merger.domain.options)
* asamblea [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
