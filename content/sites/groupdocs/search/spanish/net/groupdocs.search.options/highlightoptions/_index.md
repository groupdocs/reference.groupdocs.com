---
title: HighlightOptions
second_title: GroupDocs.Buscar referencia de API de .NET
description: Proporciona opciones para resaltar los términos encontrados.
type: docs
weight: 830
url: /es/net/groupdocs.search.options/highlightoptions/
---
## HighlightOptions class

Proporciona opciones para resaltar los términos encontrados.

```csharp
public class HighlightOptions : TextOptions
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [HighlightOptions](highlightoptions)() | Inicializa una nueva instancia del[`HighlightOptions`](../highlightoptions) clase. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [AdditionalFields](../../groupdocs.search.options/textoptions/additionalfields) { get; set; } | Obtiene o establece los campos de documento adicionales que se usaron para la indexación. El valor predeterminado es`nulo` . Tenga en cuenta que este valor se usa solo si el texto del documento no se guardó en el índice. |
| [Cancellation](../../groupdocs.search.options/textoptions/cancellation) { get; set; } | Obtiene o establece el objeto de cancelación. El valor predeterminado es`nulo` . |
| [CustomExtractor](../../groupdocs.search.options/textoptions/customextractor) { get; set; } | Obtiene o establece el extractor de texto personalizado que se utilizó para la indexación. El valor predeterminado es`nulo` . Tenga en cuenta que este valor se usa solo si el texto del documento no se guardó en el índice. |
| [GenerateHead](../../groupdocs.search.options/textoptions/generatehead) { get; set; } | Obtiene o establece un valor que indica si la etiqueta Head se genera en el HTML de salida. El valor predeterminado es`verdadero` . |
| [HighlightColor](../../groupdocs.search.options/highlightoptions/highlightcolor) { get; set; } | Obtiene o establece un color que se usa para resaltar ocurrencias. El valor predeterminado es #FFD800. |
| [ImageIndexingOptions](../../groupdocs.search.options/textoptions/imageindexingoptions) { get; } | Obtiene las opciones de indexación de imágenes para la búsqueda inversa de imágenes. |
| [MetadataIndexingOptions](../../groupdocs.search.options/textoptions/metadataindexingoptions) { get; } | Obtiene las opciones para indexar campos de metadatos. |
| [OcrIndexingOptions](../../groupdocs.search.options/textoptions/ocrindexingoptions) { get; } | Obtiene las opciones para el procesamiento de OCR y la indexación de texto reconocido. |
| [TermsAfter](../../groupdocs.search.options/highlightoptions/termsafter) { get; set; } | Obtiene o establece el número máximo de palabras en un fragmento de texto después de la palabra resaltada. El valor debe estar en el rango de 0 a 10000. El valor predeterminado es`7` . |
| [TermsBefore](../../groupdocs.search.options/highlightoptions/termsbefore) { get; set; } | Obtiene o establece el número máximo de palabras en un fragmento de texto antes de la palabra resaltada. El valor debe estar en el rango de 0 a 10000. El valor predeterminado es`7` . |
| [TermsTotal](../../groupdocs.search.options/highlightoptions/termstotal) { get; set; } | Obtiene o establece el número máximo de palabras en un fragmento de texto. El valor debe estar en el rango de 0 a 10000. El valor predeterminado es`21` . |
| [UseInlineStyles](../../groupdocs.search.options/highlightoptions/useinlinestyles) { get; set; } | Obtiene o establece un valor que indica si se utilizan estilos en línea para resaltar ocurrencias. El valor predeterminado es`verdadero` . |

### Observaciones

**Aprende más**

* [Resaltar resultados de búsqueda](https://docs.groupdocs.com/display/searchnet/Highlighting+search+results)

### Ver también

* class [TextOptions](../textoptions)
* espacio de nombres [GroupDocs.Search.Options](../../groupdocs.search.options)
* asamblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->