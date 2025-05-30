---
title: SvgPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents a native metadata package in a SVG image file.
type: docs
weight: 2440
url: /net/groupdocs.metadata.formats.image.svg/svgpackage/
---
## SvgPackage class

Represents a native metadata package in a SVG image file.

```csharp
public sealed class SvgPackage : CustomPackage
```

## Constructors

| Name | Description |
| --- | --- |
| [SvgPackage](svgpackage)() | Initializes a new instance of the [`SvgPackage`](../svgpackage) class. |

## Properties

| Name | Description |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [Height](../../groupdocs.metadata.formats.image.svg/svgpackage/height) { get; } | Gets the image height. |
| [HeightF](../../groupdocs.metadata.formats.image.svg/svgpackage/heightf) { get; } | Gets the object height, in inches. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Gets the [`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) with the specified name. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [Width](../../groupdocs.metadata.formats.image.svg/svgpackage/width) { get; } | Gets the image width. |
| [WidthF](../../groupdocs.metadata.formats.image.svg/svgpackage/widthf) { get; } | Gets the object width, in inches. |

## Methods

| Name | Description |
| --- | --- |
| virtual [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Adds known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determines whether the package contains a metadata property with the specified name. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Returns an enumerator that iterates through the collection. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Removes metadata properties satisfying the specified predicate. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Removes writable metadata properties from the package. The operation is recursive so it affects all nested packages as well. |
| virtual [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) and [`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in the package that satisfies the predicate it is added to the package. |
| virtual [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

### Remarks

**Learn more**

* [Handling metadata in SVG files](https://docs.groupdocs.com/display/metadatanet/Handling+metadata+in+SVG+files)

### Examples

This code sample shows how to extract technical information from a SVG file.

```csharp
using (Metadata metadata = new Metadata("input.svg"))
{
    var root = metadata.GetRootPackage<SvgRootPackage>();
    if (root.SvgPackage != null)
    {
        Console.WriteLine(root.SvgPackage.Title);
        Console.WriteLine(root.SvgPackage.Version);
        Console.WriteLine(root.SvgPackage.Album);
    }
}
```

### See Also

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* namespace [GroupDocs.Metadata.Formats.Image.Svg](../../groupdocs.metadata.formats.image.svg)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
