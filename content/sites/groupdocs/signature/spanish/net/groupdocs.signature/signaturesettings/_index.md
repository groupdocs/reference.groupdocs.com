---
title: SignatureSettings
second_title: Referencia de API de GroupDocs.Signature para .NET
description: Define la configuración para personalizarSignature./signature comportamiento.
type: docs
weight: 1890
url: /es/net/groupdocs.signature/signaturesettings/
---
## SignatureSettings class

Define la configuración para personalizar[`Signature`](../signature) comportamiento.

```csharp
public class SignatureSettings
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [SignatureSettings](signaturesettings#constructor)() | Crea una instancia predeterminada de SignatureSettings con valores predeterminados. |
| [SignatureSettings](signaturesettings#constructor_1)(ILogger) | Crea una instancia predeterminada de SignatureSettings con la implementación de Logger. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [DefaultCulture](../../groupdocs.signature/signaturesettings/defaultculture) { get; set; } | Obtiene o establece la cultura predeterminada que se usará durante el procesamiento de documentos. El valor predeterminado es "en-US". |
| [IncludeStandardMetadataSignatures](../../groupdocs.signature/signaturesettings/includestandardmetadatasignatures) { get; set; } | Obtiene o establece el indicador para incluir en la lista de metadatos las firmas de metadatos del documento estándar incrustado, como autor, propietario, fecha de creación del documento, fecha de modificación, etc. Si este indicador se establece en falso (de forma predeterminada), GetDocumentInfo no incluirá estos metadatos firmas. Cuando este indicador se establece en verdadero, la información del documento incluirá estas firmas de metadatos estándar. |
| [Logger](../../groupdocs.signature/signaturesettings/logger) { get; } | La implementación del registrador utilizada para el registro (Errores, Advertencias, Rastreos).[`ILogger`](../../groupdocs.signature.logging/ilogger) . |
| [LogLevel](../../groupdocs.signature/signaturesettings/loglevel) { get; set; } | El nivel del registro para limitar los mensajes (Todos, Seguimientos, Advertencias, Errores).[`LogLevel`](./loglevel) . POR defecto, el tipo de todos los niveles está configurado. |
| [SaveDocumentOnEmptyDelete](../../groupdocs.signature/signaturesettings/savedocumentonemptydelete) { get; set; } | Obtiene o establece el indicador para volver a guardar el documento de origen cuando el método de eliminación no tiene firmas afectadas para eliminar. El método de eliminación no tiene firmas para eliminar. Cuando este plano se configura como falso, el documento de origen no se modificará en absoluto. |
| [SaveDocumentOnEmptyUpdate](../../groupdocs.signature/signaturesettings/savedocumentonemptyupdate) { get; set; } | Obtiene o establece el indicador para volver a guardar el documento de origen cuando el método de actualización no tiene firmas para actualizar. el método no tiene firmas para actualizar. Cuando este plano se configura como falso, el documento de origen no se modificará en absoluto. |
| [ShowDeletedSignaturesInfo](../../groupdocs.signature/signaturesettings/showdeletedsignaturesinfo) { get; set; } | Obtiene o establece un indicador que incluye las firmas eliminadas en el resultado de información del documento. Cada firma[`BaseSignature`](../../groupdocs.signature.domain/basesignature) ha eliminado la bandera[`Deleted`](../../groupdocs.signature.domain/basesignature/deleted) para detectar si fue borrado. |

### Ver también

* espacio de nombres [GroupDocs.Signature](../../groupdocs.signature)
* asamblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
