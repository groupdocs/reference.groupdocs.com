---
title: EpubPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Gets the EPUB metadata package.
type: docs
weight: 20
url: /net/groupdocs.metadata.formats.ebook/epubrootpackage/epubpackage/
---
## EpubRootPackage.EpubPackage property

Gets the EPUB metadata package.

```csharp
public EpubPackage EpubPackage { get; }
```

### Property Value

The EPUB metadata package.

### Remarks

**Learn more**

* [Working with metadata in EPUB E-Books](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+EPUB+E-Books)

### Examples

This code sample shows how to read EPUB format-specific metadata properties.

```csharp
using (Metadata metadata = new Metadata(Constants.InputEpub))
{
    var root = metadata.GetRootPackage<EpubRootPackage>();

    Console.WriteLine(root.EpubPackage.Version);
    Console.WriteLine(root.EpubPackage.UniqueIdentifier);
    Console.WriteLine(root.EpubPackage.ImageCover != null ? root.EpubPackage.ImageCover.Length : 0);
}
```

### See Also

* class [EpubPackage](../../epubpackage)
* class [EpubRootPackage](../../epubrootpackage)
* namespace [GroupDocs.Metadata.Formats.Ebook](../../epubrootpackage)
* assembly [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->