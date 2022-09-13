---
title: JpegRootPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents the root package allowing working with metadata in a JPEG image.
type: docs
weight: 1800
url: /net/groupdocs.metadata.formats.image/jpegrootpackage/
---
## JpegRootPackage class

Represents the root package allowing working with metadata in a JPEG image.

```csharp
public class JpegRootPackage : ImageRootPackage, IExif, IIptc, IXmp
```

## Properties

| Name | Description |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [ExifPackage](../../groupdocs.metadata.formats.image/jpegrootpackage/exifpackage) { get; set; } | Gets or sets the EXIF metadata package. |
| [FileType](../../groupdocs.metadata.formats.image/imagerootpackage/filetype) { get; } | Gets the file type metadata package. (2 properties) |
| [ImageResourcePackage](../../groupdocs.metadata.formats.image/jpegrootpackage/imageresourcepackage) { get; } | Gets the Photoshop Image Resource metadata package. Image resource blocks are the basic building unit of Photoshop native file format. |
| [IptcPackage](../../groupdocs.metadata.formats.image/jpegrootpackage/iptcpackage) { get; set; } | Gets or sets the IPTC metadata package. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Gets the [`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) with the specified name. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [MakerNotePackage](../../groupdocs.metadata.formats.image/jpegrootpackage/makernotepackage) { get; } | Gets or sets the MakerNote metadata package. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [XmpPackage](../../groupdocs.metadata.formats.image/jpegrootpackage/xmppackage) { get; set; } | Gets or sets the XMP metadata package. |

## Methods

| Name | Description |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Adds known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determines whether the package contains a metadata property with the specified name. |
| [DetectBarcodeTypes](../../groupdocs.metadata.formats.image/jpegrootpackage/detectbarcodetypes)() | Extracts the types of the barcodes presented in the image. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Returns an enumerator that iterates through the collection. |
| [RemoveImageResourcePackage](../../groupdocs.metadata.formats.image/jpegrootpackage/removeimageresourcepackage)() | Removes Photoshop Image Resource metadata package. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Removes metadata properties satisfying the specified predicate. |
| override [Sanitize](../../groupdocs.metadata.formats.image/jpegrootpackage/sanitize)() | Removes writable metadata properties from the package. The operation is recursive so it affects all nested packages as well. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) and [`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in the package that satisfies the predicate it is added to the package. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

### Remarks

**Learn more**

* [Working with metadata in JPEG images](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+JPEG+images)
* [Working with EXIF metadata](https://docs.groupdocs.com/display/metadatanet/Working+with+EXIF+metadata)
* [Working with XMP metadata](https://docs.groupdocs.com/display/metadatanet/Working+with+XMP+metadata)
* [Working with IPTC IIM metadata](https://docs.groupdocs.com/display/metadatanet/Working+with+IPTC+IIM+metadata)

### See Also

* class [ImageRootPackage](../imagerootpackage)
* interface [IExif](../../groupdocs.metadata.standards.exif/iexif)
* interface [IIptc](../../groupdocs.metadata.standards.iptc/iiptc)
* interface [IXmp](../../groupdocs.metadata.standards.xmp/ixmp)
* namespace [GroupDocs.Metadata.Formats.Image](../../groupdocs.metadata.formats.image)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->