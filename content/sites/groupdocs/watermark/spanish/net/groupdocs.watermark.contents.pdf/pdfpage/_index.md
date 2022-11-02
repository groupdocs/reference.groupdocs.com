---
title: PdfPage
second_title: Referencia de API de GroupDocs.Watermark para .NET
description: Representa la página del documento pdf.
type: docs
weight: 660
url: /es/net/groupdocs.watermark.contents.pdf/pdfpage/
---
## PdfPage class

Representa la página del documento pdf.

```csharp
public class PdfPage : ContentPart
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Annotations](../../groupdocs.watermark.contents.pdf/pdfpage/annotations) { get; } | Obtiene la colección de todas las anotaciones de este[`PdfPage`](../pdfpage) . |
| [Artifacts](../../groupdocs.watermark.contents.pdf/pdfpage/artifacts) { get; } | Obtiene la colección de todos los artefactos de este[`PdfPage`](../pdfpage) . |
| [Height](../../groupdocs.watermark.contents.pdf/pdfpage/height) { get; } | Obtiene la altura de este[`PdfPage`](../pdfpage)en puntos. |
| [Width](../../groupdocs.watermark.contents.pdf/pdfpage/width) { get; } | Obtiene el ancho de este[`PdfPage`](../pdfpage)en puntos. |
| [XObjects](../../groupdocs.watermark.contents.pdf/pdfpage/xobjects) { get; } | Obtiene la colección de todos los XObjects de este[`PdfPage`](../pdfpage) . |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | Encuentra todas las imágenes en el contenido. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Encuentra imágenes de acuerdo con los criterios de búsqueda especificados. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| virtual [Rasterize](../../groupdocs.watermark.contents.pdf/pdfpage/rasterize)(int, int, PdfImageConversionFormat) | Convierte el contenido de la página en una imagen. |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | Encuentra todas las marcas de agua posibles en el contenido. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Encuentra posibles marcas de agua de acuerdo con los criterios de búsqueda especificados. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Ver también

* class [ContentPart](../../groupdocs.watermark.contents/contentpart)
* espacio de nombres [GroupDocs.Watermark.Contents.Pdf](../../groupdocs.watermark.contents.pdf)
* asamblea [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->