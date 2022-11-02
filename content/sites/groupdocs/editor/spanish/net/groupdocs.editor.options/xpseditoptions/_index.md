---
title: XpsEditOptions
second_title: Referencia de API de GroupDocs.Editor para .NET
description: Permite especificar opciones personalizadas para editar documentos Especificaciones de papel XML
type: docs
weight: 1060
url: /es/net/groupdocs.editor.options/xpseditoptions/
---
## XpsEditOptions class

Permite especificar opciones personalizadas para editar documentos (Especificaciones de papel XML)

```csharp
public sealed class XpsEditOptions : FixedLayoutEditOptionsBase
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [XpsEditOptions](xpseditoptions#constructor)() | Crea y devuelve una nueva instancia de la clase XpsEditOptions, donde todas las opciones se establecen en sus valores predeterminados |
| [XpsEditOptions](xpseditoptions#constructor_1)(bool) | Crea y devuelve una nueva instancia de la clase XpsEditOptions con la paginación especificada y todas las demás opciones predeterminadas |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [EnablePagination](../../groupdocs.editor.options/fixedlayouteditoptionsbase/enablepagination) { get; set; } | Permite habilitar (verdadero) o deshabilitar (falso) la paginación en el documento HTML resultante. Por defecto está deshabilitado (falso). |
| [Pages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/pages) { get; set; } | Permite establecer un rango de páginas para procesar. De forma predeterminada, se procesan todas las páginas de un documento de diseño fijo. |
| [SkipImages](../../groupdocs.editor.options/fixedlayouteditoptionsbase/skipimages) { get; set; } | Obtiene o establece el indicador que indica si las imágenes se deben omitir al convertir el documento de diseño fijo de entrada al HTML resultante. El valor predeterminado es falso: las imágenes se conservan. |

### Ver también

* class [FixedLayoutEditOptionsBase](../fixedlayouteditoptionsbase)
* espacio de nombres [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* asamblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->