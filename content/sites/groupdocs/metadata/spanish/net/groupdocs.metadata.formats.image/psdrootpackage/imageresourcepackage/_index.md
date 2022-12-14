---
title: ImageResourcePackage
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Obtiene el paquete de metadatos de recursos de imagen de Photoshop. Los bloques de recursos de imagen son la unidad de creación básica del formato de archivo nativo de Photoshop.
type: docs
weight: 20
url: /es/net/groupdocs.metadata.formats.image/psdrootpackage/imageresourcepackage/
---
## PsdRootPackage.ImageResourcePackage property

Obtiene el paquete de metadatos de recursos de imagen de Photoshop. Los bloques de recursos de imagen son la unidad de creación básica del formato de archivo nativo de Photoshop.

```csharp
public ImageResourcePackage ImageResourcePackage { get; }
```

### El valor de la propiedad

El paquete de metadatos de recursos de imagen.

### Observaciones

**Aprende más**

* [Trabajar con metadatos en imágenes PSD](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+PSD+images)

### Ejemplos

El ejemplo de código siguiente muestra cómo extraer bloques de recursos de imagen (bloques de construcción del formato de archivo de Photoshop) de una imagen PSD.

```csharp
using (Metadata metadata = new Metadata(Constants.PsdWithIrb))
{
    var root = metadata.GetRootPackage<PsdRootPackage>();

    if (root.ImageResourcePackage != null)
    {
        foreach (var block in root.ImageResourcePackage.ToList())
        {
            Console.WriteLine(block.Signature);
            Console.WriteLine(block.ID);
            Console.WriteLine(block.Name);
            Console.WriteLine(block.Data);
        }
    }
}
```

### Ver también

* class [ImageResourcePackage](../../imageresourcepackage)
* class [PsdRootPackage](../../psdrootpackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Image](../../psdrootpackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
