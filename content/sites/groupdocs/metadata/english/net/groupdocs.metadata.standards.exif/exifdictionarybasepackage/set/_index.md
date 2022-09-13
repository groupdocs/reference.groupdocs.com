---
title: Set
second_title: GroupDocs.Metadata for .NET API Reference
description: Adds or replaces the specified tag.
type: docs
weight: 40
url: /net/groupdocs.metadata.standards.exif/exifdictionarybasepackage/set/
---
## ExifDictionaryBasePackage.Set method

Adds or replaces the specified tag.

```csharp
public void Set(TiffTag tag)
```

| Parameter | Type | Description |
| --- | --- | --- |
| tag | TiffTag | The tag to set. |

### Examples

This code sample demonstrates how to add a custom tag to an EXIF package.

```csharp
using (Metadata metadata = new Metadata(Constants.TiffWithExif))
{
    IExif root = metadata.GetRootPackage() as IExif;
    if (root != null)
    {
        // Set the EXIF package if it's missing
        if (root.ExifPackage == null)
        {
            root.ExifPackage = new ExifPackage();
        }

        // Add a known property
        root.ExifPackage.Set(new TiffAsciiTag(TiffTagID.Artist, "test artist"));

        // Add a fully custom property (which is not described in the EXIF specification).
        // Please note that the chosen ID may intersect with the IDs used by some third party tools.
        root.ExifPackage.Set(new TiffAsciiTag((TiffTagID)65523, "custom"));

        metadata.Save(Constants.OutputTiff);
    }
}
```

### See Also

* class [TiffTag](../../../groupdocs.metadata.formats.image/tifftag)
* class [ExifDictionaryBasePackage](../../exifdictionarybasepackage)
* namespace [GroupDocs.Metadata.Standards.Exif](../../exifdictionarybasepackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->