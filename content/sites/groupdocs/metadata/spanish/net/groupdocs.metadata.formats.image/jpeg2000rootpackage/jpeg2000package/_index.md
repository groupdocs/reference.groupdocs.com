---
title: Jpeg2000Package
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Obtiene el paquete de metadatos nativos JPEG2000.
type: docs
weight: 20
url: /es/net/groupdocs.metadata.formats.image/jpeg2000rootpackage/jpeg2000package/
---
## Jpeg2000RootPackage.Jpeg2000Package property

Obtiene el paquete de metadatos nativos JPEG2000.

```csharp
public Jpeg2000Package Jpeg2000Package { get; }
```

### El valor de la propiedad

El paquete de metadatos nativos JPEG2000.

### Observaciones

**Aprende más**

* [Trabajar con metadatos en imágenes JPEG2000](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+JPEG2000+images)

### Ejemplos

Este fragmento de código demuestra cómo leer comentarios de imágenes JPEG2000.

```csharp
using (Metadata metadata = new Metadata(Constants.InputJpeg2000))
{
    var root = metadata.GetRootPackage<Jpeg2000RootPackage>();

    if (root.Jpeg2000Package.Comments != null)
    {
        foreach (var comment in root.Jpeg2000Package.Comments)
        {
            Console.WriteLine(comment);
        }
    }
}
```

### Ver también

* class [Jpeg2000Package](../../jpeg2000package)
* class [Jpeg2000RootPackage](../../jpeg2000rootpackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Image](../../jpeg2000rootpackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->