---
title: PsdPackage
second_title: Referencia de API de GroupDocs.Metadata para .NET
description: Obtiene el paquete de metadatos que contiene información sobre el archivo PSD.
type: docs
weight: 40
url: /es/net/groupdocs.metadata.formats.image/psdrootpackage/psdpackage/
---
## PsdRootPackage.PsdPackage property

Obtiene el paquete de metadatos que contiene información sobre el archivo PSD.

```csharp
public PsdPackage PsdPackage { get; }
```

### El valor de la propiedad

El paquete de metadatos que contiene información sobre el archivo PSD.

### Observaciones

**Aprende más**

* [Trabajar con metadatos en imágenes PSD](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+PSD+images)

### Ejemplos

Este ejemplo de código demuestra cómo leer el encabezado de un archivo PSD y extraer información sobre las capas PSD.

```csharp
using (Metadata metadata = new Metadata(Constants.PsdWithIptc))
{
    var root = metadata.GetRootPackage<PsdRootPackage>();

    Console.WriteLine(root.PsdPackage.ChannelCount);
    Console.WriteLine(root.PsdPackage.ColorMode);
    Console.WriteLine(root.PsdPackage.Compression);
    Console.WriteLine(root.PsdPackage.PhotoshopVersion);

    foreach (var layer in root.PsdPackage.Layers)
    {
        Console.WriteLine(layer.Name);
        Console.WriteLine(layer.BitsPerPixel);
        Console.WriteLine(layer.ChannelCount);
        Console.WriteLine(layer.Flags);
        Console.WriteLine(layer.Height);
        Console.WriteLine(layer.Width);

        // ...
    }

    // ...
}
```

### Ver también

* class [PsdPackage](../../psdpackage)
* class [PsdRootPackage](../../psdrootpackage)
* espacio de nombres [GroupDocs.Metadata.Formats.Image](../../psdrootpackage)
* asamblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->