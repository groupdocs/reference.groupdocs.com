---
title: ExifPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets or sets the EXIF metadata package.
type: docs
weight: 10
url: /net/groupdocs.metadata.formats.image/jpeg2000rootpackage/exifpackage/
---
## Jpeg2000RootPackage.ExifPackage property

Gets or sets the EXIF metadata package.

```csharp
public ExifPackage ExifPackage { get; set; }
```

### Property Value

The EXIF metadata package.

### Remarks

**Learn more**

* [Working with EXIF metadata](https://docs.groupdocs.com/display/metadatanet/Working+with+EXIF+metadata)

### Examples

This code sample demonstrates how to extract basic EXIF metadata properties.

```csharp
using (Metadata metadata = new Metadata(Constants.Jpeg2000WithExif))
{
    var root = metadata.GetRootPackage<Jpeg2000RootPackage>();
    if (root.ExifPackage != null)
    {
        Console.WriteLine(root.ExifPackage.Artist);
        Console.WriteLine(root.ExifPackage.Copyright);
        Console.WriteLine(root.ExifPackage.ImageDescription);
        Console.WriteLine(root.ExifPackage.Make);
        Console.WriteLine(root.ExifPackage.Model);
        Console.WriteLine(root.ExifPackage.Software);
        Console.WriteLine(root.ExifPackage.ImageWidth);
        Console.WriteLine(root.ExifPackage.ImageLength);

        // ...

        Console.WriteLine(root.ExifPackage.ExifIfdPackage.BodySerialNumber);
        Console.WriteLine(root.ExifPackage.ExifIfdPackage.CameraOwnerName);
        Console.WriteLine(root.ExifPackage.ExifIfdPackage.UserComment);

        // ...

        Console.WriteLine(root.ExifPackage.GpsPackage.Altitude);
        Console.WriteLine(root.ExifPackage.GpsPackage.LatitudeRef);
        Console.WriteLine(root.ExifPackage.GpsPackage.LongitudeRef);

        // ...
    }
}
```

### See Also

* class [ExifPackage](../../../groupdocs.metadata.standards.exif/exifpackage)
* class [Jpeg2000RootPackage](../../jpeg2000rootpackage)
* namespace [GroupDocs.Metadata.Formats.Image](../../jpeg2000rootpackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->