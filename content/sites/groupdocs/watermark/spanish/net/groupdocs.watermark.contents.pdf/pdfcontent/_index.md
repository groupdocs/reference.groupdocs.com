---
title: PdfContent
second_title: Referencia de API de GroupDocs.Watermark para .NET
description: Representa un documento pdf donde se puede colocar una marca de agua.
type: docs
weight: 610
url: /es/net/groupdocs.watermark.contents.pdf/pdfcontent/
---
## PdfContent class

Representa un documento pdf donde se puede colocar una marca de agua.

```csharp
public class PdfContent : Content
```

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [Attachments](../../groupdocs.watermark.contents.pdf/pdfcontent/attachments) { get; } | Obtiene la colección de todos los archivos adjuntos de este[`PdfContent`](../pdfcontent) . |
| [PageMarginType](../../groupdocs.watermark.contents.pdf/pdfcontent/pagemargintype) { get; set; } | Obtiene o establece los márgenes de la página PDF que se utilizarán durante la adición de la marca de agua. |
| [Pages](../../groupdocs.watermark.contents.pdf/pdfcontent/pages) { get; } | Obtiene la colección de todas las páginas de este[`PdfContent`](../pdfcontent) . |

## Métodos

| Nombre | Descripción |
| --- | --- |
| [Decrypt](../../groupdocs.watermark.contents.pdf/pdfcontent/decrypt)() | Descifra el contenido. |
| [Dispose](../../groupdocs.watermark.contents/content/dispose)() | Elimina la instancia actual. |
| [Encrypt](../../groupdocs.watermark.contents.pdf/pdfcontent/encrypt#encrypt)(string) | Cifra el documento utilizando la misma contraseña que la contraseña de usuario y la contraseña de propietario. |
| [Encrypt](../../groupdocs.watermark.contents.pdf/pdfcontent/encrypt#encrypt_1)(string, string, PdfPermissions, PdfCryptoAlgorithm) | Cifra el contenido. |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)() | Encuentra todas las imágenes en el contenido. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [FindImages](../../groupdocs.watermark.contents/contentpart/findimages)(ImageSearchCriteria) | Encuentra imágenes de acuerdo con los criterios de búsqueda especificados. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Rasterize](../../groupdocs.watermark.contents.pdf/pdfcontent/rasterize)(int, int, PdfImageConversionFormat) | Convierte todas las páginas de contenido en imágenes. |
| [Search](../../groupdocs.watermark.contents/contentpart/search)() | Encuentra todas las marcas de agua posibles en el contenido. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |
| [Search](../../groupdocs.watermark.contents/contentpart/search)(SearchCriteria) | Encuentra posibles marcas de agua de acuerdo con los criterios de búsqueda especificados. La búsqueda se realiza en los objetos especificados en[`SearchableObjects`](../../groupdocs.watermark/watermarker/searchableobjects) . |

### Observaciones

**Aprende más:**

* [Agregar marcas de agua a documentos PDF](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+PDF+documents)
* [Objetos existentes en el documento PDF](https://docs.groupdocs.com/display/watermarknet/Existing+objects+in+PDF+document)
* [Rasterizar documento o página](https://docs.groupdocs.com/display/watermarknet/Rasterize+document+or+page)
* [Marcas de agua en documento PDF](https://docs.groupdocs.com/display/watermarknet/Watermarks+in+PDF+document)

### Ver también

* class [Content](../../groupdocs.watermark.contents/content)
* espacio de nombres [GroupDocs.Watermark.Contents.Pdf](../../groupdocs.watermark.contents.pdf)
* asamblea [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->