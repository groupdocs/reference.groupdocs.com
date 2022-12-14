---
title: FileType
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Obtiene el paquete de metadatos del tipo de archivo.
type: docs
weight: 30
url: /es/net/groupdocs.metadata.formats.document/wordprocessingrootpackage/filetype/
---
## WordProcessingRootPackage.FileType property

Obtiene el paquete de metadatos del tipo de archivo.

```csharp
public WordProcessingTypePackage FileType { get; }
```

### El valor de la propiedad

El paquete de metadatos del tipo de archivo.

### Ejemplos

Este ejemplo muestra cómo detectar el tipo exacto de un documento cargado y extraer información adicional sobre el formato de archivo.

```csharp
using (Metadata metadata = new Metadata(Constants.InputDoc))
{
    var root = metadata.GetRootPackage<WordProcessingRootPackage>();

    Console.WriteLine(root.FileType.FileFormat);
    Console.WriteLine(root.FileType.WordProcessingFormat);
    Console.WriteLine(root.FileType.MimeType);
    Console.WriteLine(root.FileType.Extension);
}
```

### Ver también

* class [WordProcessingTypePackage](../../wordprocessingtypepackage)
* class [WordProcessingRootPackage](../../wordprocessingrootpackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Document](../../wordprocessingrootpackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
