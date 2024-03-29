---
title: TiffSaveOptions
second_title: Referencia de API de GroupDocs.Signature para .NET
description: Opciones de guardado Tiff para documentos de imagen.
type: docs
weight: 1760
url: /es/net/groupdocs.signature.options/tiffsaveoptions/
---
## TiffSaveOptions class

Opciones de guardado Tiff para documentos de imagen.

```csharp
public sealed class TiffSaveOptions : ImageSaveOptions
```

## Constructores

| Nombre | Descripción |
| --- | --- |
| [TiffSaveOptions](tiffsaveoptions)() | Crea TiffSaveOptions con valores predeterminados. |

## Propiedades

| Nombre | Descripción |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Obtiene o establece el indicador para agregar automáticamente la extensión cuando faltaba en la ruta del archivo de salida El valor predeterminado es false. |
| [ExpectedTiffFormat](../../groupdocs.signature.options/tiffsaveoptions/expectedtiffformat) { get; set; } | Obtiene o establece el formato TIFF del documento firmado. |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | Obtiene o establece el formato de archivo del documento firmado. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Obtiene o establece si se sobrescribe el archivo existente con un nuevo archivo de salida. De lo contrario, se creará un nuevo archivo con el número como sufijo. De forma predeterminada, este valor se establece en verdadero, lo que significa que se sobrescribirá el archivo. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | Obtiene o establece la contraseña para guardar el documento firmado con protección de contraseña. Esta propiedad no es compatible con los documentos de imagen. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | Obtiene o establece si usar la contraseña de LoadOptions para guardar el documento firmado como protegido. El valor predeterminado es verdadero. Esta propiedad no se admite para documentos de imagen. |

### Ver también

* class [ImageSaveOptions](../imagesaveoptions)
* espacio de nombres [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* asamblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
