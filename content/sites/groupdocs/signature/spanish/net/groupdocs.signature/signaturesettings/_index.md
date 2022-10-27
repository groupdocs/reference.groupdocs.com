---
title: SignatureSettings
second_title: Referencia de API de GroupDocs.Signature para .NET
description: Define la configuración para personalizarSignature./signature comportamiento.
type: docs
weight: 1810
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
| [SignatureSettings](signaturesettings)() | Constructor predeterminado |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [DefaultCulture](../../groupdocs.signature/signaturesettings/defaultculture) { get; set; } | Obtiene o establece la cultura predeterminada que se usará durante el procesamiento de documentos. El valor predeterminado es "en-US". |
| [SaveDocumentOnEmptyDelete](../../groupdocs.signature/signaturesettings/savedocumentonemptydelete) { get; set; } | Obtiene o establece el indicador para volver a guardar el documento de origen cuando el método Eliminar no tiene firmas afectadas para eliminar. Si este indicador se establece en verdadero (de forma predeterminada), el documento se guardará con el registro del proceso de historial correspondiente (fecha y tipo de operación) incluso si el método Eliminar no tiene firmas para eliminar. Cuando este plano se configura como falso, el documento de origen no se modificará en absoluto. |
| [SaveDocumentOnEmptyUpdate](../../groupdocs.signature/signaturesettings/savedocumentonemptyupdate) { get; set; } | Obtiene o establece el indicador para volver a guardar el documento de origen cuando el método de actualización no tiene firmas para actualizar. Si este indicador se establece en verdadero (de forma predeterminada), el documento se guardará con el registro del proceso de historial correspondiente (fecha y tipo de operación) incluso si el método de actualización tiene no hay firmas para actualizar. Cuando este plano se configura como falso, el documento de origen no se modificará en absoluto. |
| [ShowDeletedSignaturesInfo](../../groupdocs.signature/signaturesettings/showdeletedsignaturesinfo) { get; set; } | Obtiene o establece un indicador que incluye las firmas eliminadas en el resultado de información del documento. Cada firma[`BaseSignature`](../../groupdocs.signature.domain/basesignature) ha eliminado la bandera[`Deleted`](../../groupdocs.signature.domain/basesignature/deleted) para detectar si fue borrado. |

### Ver también

* espacio de nombres [GroupDocs.Signature](../../groupdocs.signature)
* asamblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->