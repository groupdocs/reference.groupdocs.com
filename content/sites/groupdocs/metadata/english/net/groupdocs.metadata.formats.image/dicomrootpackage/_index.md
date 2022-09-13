---
title: DicomRootPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents the root package intended to work with metadata in a DICOM image.
type: docs
weight: 1670
url: /net/groupdocs.metadata.formats.image/dicomrootpackage/
---
## DicomRootPackage class

Represents the root package intended to work with metadata in a DICOM image.

```csharp
public class DicomRootPackage : ImageRootPackage
```

## Properties

| Name | Description |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [DicomPackage](../../groupdocs.metadata.formats.image/dicomrootpackage/dicompackage) { get; } | Gets the DICOM native metadata package. |
| [FileType](../../groupdocs.metadata.formats.image/imagerootpackage/filetype) { get; } | Gets the file type metadata package. (2 properties) |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Gets the [`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) with the specified name. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |

## Methods

| Name | Description |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Adds known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determines whether the package contains a metadata property with the specified name. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Returns an enumerator that iterates through the collection. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Removes metadata properties satisfying the specified predicate. |
| override [Sanitize](../../groupdocs.metadata.common/rootmetadatapackage/sanitize)() | Removes writable metadata properties from the package. The operation is recursive so it affects all nested packages as well. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) and [`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in the package that satisfies the predicate it is added to the package. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

### Remarks

**Learn more**

* [Working with DICOM metadata](https://docs.groupdocs.com/display/metadatanet/Working+with+DICOM+metadata)

### Examples

This example demonstrates how to read DICOM format-specific metadata properties.

```csharp
using (Metadata metadata = new Metadata(Constants.InputDicom))
{
    var root = metadata.GetRootPackage<DicomRootPackage>();
    if (root.DicomPackage != null)
    {
        Console.WriteLine(root.DicomPackage.BitsAllocated);
        Console.WriteLine(root.DicomPackage.LengthValue);
        Console.WriteLine(root.DicomPackage.DicomFound);
        Console.WriteLine(root.DicomPackage.HeaderOffset);
        Console.WriteLine(root.DicomPackage.NumberOfFrames);

        // ...
    }
}
```

### See Also

* class [ImageRootPackage](../imagerootpackage)
* namespace [GroupDocs.Metadata.Formats.Image](../../groupdocs.metadata.formats.image)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->