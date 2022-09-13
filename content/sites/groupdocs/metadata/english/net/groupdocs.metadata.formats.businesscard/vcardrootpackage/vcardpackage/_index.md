---
title: VCardPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets the VCard metadata package.
type: docs
weight: 10
url: /net/groupdocs.metadata.formats.businesscard/vcardrootpackage/vcardpackage/
---
## VCardRootPackage.VCardPackage property

Gets the VCard metadata package.

```csharp
public VCardPackage VCardPackage { get; }
```

### Property Value

The VCard metadata package.

### Remarks

**Learn more**

* [Working with vCard metadata](https://docs.groupdocs.com/display/metadatanet/Working+with+vCard+metadata)

### Examples

This code sample demonstrates how to extract vCard fields along with descriptive parameters.

```csharp
using (Metadata metadata = new Metadata(Constants.InputVcf))
{
    var root = metadata.GetRootPackage<VCardRootPackage>();

    foreach (var vCard in root.VCardPackage.Cards)
    {
        if (vCard.IdentificationRecordset.PhotoUriRecords != null)
        {
            // Iterate all photos represented by URIs
            foreach (var photoUriRecord in vCard.IdentificationRecordset.PhotoUriRecords)
            {
                // Print the property value
                Console.WriteLine(photoUriRecord.Value);

                // Print some additional parameters of the property
                Console.WriteLine(photoUriRecord.ContentType);
                Console.WriteLine(photoUriRecord.MediaTypeParameter);
                if (photoUriRecord.TypeParameters != null)
                {
                    foreach (string parameter in photoUriRecord.TypeParameters)
                    {
                        Console.WriteLine(parameter);
                    }
                }
                Console.WriteLine(photoUriRecord.PrefParameter);
            }
        }
    }
}
```

### See Also

* class [VCardPackage](../../vcardpackage)
* class [VCardRootPackage](../../vcardrootpackage)
* namespace [GroupDocs.Metadata.Formats.BusinessCard](../../vcardrootpackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->