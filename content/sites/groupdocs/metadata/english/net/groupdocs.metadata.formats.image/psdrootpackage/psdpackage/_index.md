---
title: PsdPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets the metadata package containing information about the PSD file.
type: docs
weight: 40
url: /net/groupdocs.metadata.formats.image/psdrootpackage/psdpackage/
---
## PsdRootPackage.PsdPackage property

Gets the metadata package containing information about the PSD file.

```csharp
public PsdPackage PsdPackage { get; }
```

### Property Value

The metadata package containing information about the PSD file.

### Remarks

**Learn more**

* [Working with metadata in PSD images](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+PSD+images)

### Examples

This code sample demonstrates how to read the header of a PSD file and extract some information about the PSD layers.

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

### See Also

* class [PsdPackage](../../psdpackage)
* class [PsdRootPackage](../../psdrootpackage)
* namespace [GroupDocs.Metadata.Formats.Image](../../psdrootpackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->