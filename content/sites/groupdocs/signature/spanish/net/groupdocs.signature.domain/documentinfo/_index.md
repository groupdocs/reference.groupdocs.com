---
title: DocumentInfo
second_title: Referencia de API de GroupDocs.Signature para .NET
description: Define las propiedades de la descripción del documento.
type: docs
weight: 160
url: /es/net/groupdocs.signature.domain/documentinfo/
---
## DocumentInfo class

Define las propiedades de la descripción del documento.

```csharp
public class DocumentInfo : IDocumentInfo
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [DocumentInfo](documentinfo)() | Inicializa una nueva instancia del[`DocumentInfo`](../documentinfo)clase. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [BarcodeSignatures](../../groupdocs.signature.domain/documentinfo/barcodesignatures) { get; } | Colección de firmas de códigos de barras de documentos agregadas o actualizadas por[`Signature`](../../groupdocs.signature/signature) métodos. |
| [DigitalSignatures](../../groupdocs.signature.domain/documentinfo/digitalsignatures) { get; } | Colección de firmas digitales de documentos agregadas o actualizadas por[`Signature`](../../groupdocs.signature/signature) métodos. |
| [FileType](../../groupdocs.signature.domain/documentinfo/filetype) { get; set; } | Tipo de formato de archivo. |
| [FormFields](../../groupdocs.signature.domain/documentinfo/formfields) { get; } | Colección de todos los campos de formulario compatibles existentes en el documento. Esta propiedad solo se admite para los tipos de documento Pdf y Word Processing. |
| [FormFieldSignatures](../../groupdocs.signature.domain/documentinfo/formfieldsignatures) { get; } | Recopilación de documento Formulario Campo Firmas añadidas o actualizadas por[`Signature`](../../groupdocs.signature/signature) métodos. |
| [ImageSignatures](../../groupdocs.signature.domain/documentinfo/imagesignatures) { get; } | Colección de firmas de imágenes de documentos añadidas o actualizadas por[`Signature`](../../groupdocs.signature/signature) métodos. |
| [MaxPageHeight](../../groupdocs.signature.domain/documentinfo/maxpageheight) { get; set; } | Especifica la altura máxima de página. |
| [MetadataSignatures](../../groupdocs.signature.domain/documentinfo/metadatasignatures) { get; } | Colección de firmas de metadatos de documentos. |
| [PageCount](../../groupdocs.signature.domain/documentinfo/pagecount) { get; set; } | Número de páginas del documento. |
| [Pages](../../groupdocs.signature.domain/documentinfo/pages) { get; set; } | Colección de descripciones de páginas de documentos. |
| [ProcessLogs](../../groupdocs.signature.domain/documentinfo/processlogs) { get; } | Colección de procesos de historial de documentos como Firmar, Actualizar, Eliminar. |
| [QrCodeSignatures](../../groupdocs.signature.domain/documentinfo/qrcodesignatures) { get; } | Colección de firmas de códigos QR de documentos añadidas o actualizadas por[`Signature`](../../groupdocs.signature/signature) métodos. |
| [Signatures](../../groupdocs.signature.domain/documentinfo/signatures) { get; } | Recogida de documentos todo tipo de firmas[`BaseSignature`](../basesignature) . |
| [Size](../../groupdocs.signature.domain/documentinfo/size) { get; set; } | Tamaño del documento en bytes. |
| [TextSignatures](../../groupdocs.signature.domain/documentinfo/textsignatures) { get; } | Colección de firmas de texto de documentos. |
| [WidthForMaxHeight](../../groupdocs.signature.domain/documentinfo/widthformaxheight) { get; set; } | Especifica el ancho para la altura máxima de página. |

### Ver también

* interface [IDocumentInfo](../idocumentinfo)
* espacio de nombres [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* asamblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
