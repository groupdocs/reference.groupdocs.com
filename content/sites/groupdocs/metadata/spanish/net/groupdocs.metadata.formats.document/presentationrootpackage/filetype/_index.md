---
title: FileType
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Obtiene el paquete de metadatos del tipo de archivo.
type: docs
weight: 20
url: /es/net/groupdocs.metadata.formats.document/presentationrootpackage/filetype/
---
## PresentationRootPackage.FileType property

Obtiene el paquete de metadatos del tipo de archivo.

```csharp
public PresentationTypePackage FileType { get; }
```

### El valor de la propiedad

El paquete de metadatos del tipo de archivo.

### Ejemplos

Este ejemplo demuestra cómo detectar el tipo exacto de una presentación y extraer información adicional sobre el formato de archivo.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPptx))
{
    var root = metadata.GetRootPackage<PresentationRootPackage>();

    Console.WriteLine(root.FileType.FileFormat);
    Console.WriteLine(root.FileType.PresentationFormat);
    Console.WriteLine(root.FileType.MimeType);
    Console.WriteLine(root.FileType.Extension);
}
```

### Ver también

* class [PresentationTypePackage](../../presentationtypepackage)
* class [PresentationRootPackage](../../presentationrootpackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Document](../../presentationrootpackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->