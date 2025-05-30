---
title: Cr2ModifiedInfoPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents Canon MakerNotes tags.
type: docs
weight: 3070
url: /net/groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/
---
## Cr2ModifiedInfoPackage class

Represents Canon MakerNotes tags.

```csharp
public sealed class Cr2ModifiedInfoPackage : RawDictionaryBasePackage
```

## Constructors

| Name | Description |
| --- | --- |
| [Cr2ModifiedInfoPackage](cr2modifiedinfopackage)() | Initializes a new instance of the [`Cr2ModifiedInfoPackage`](../cr2modifiedinfopackage) class. |

## Properties

| Name | Description |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [Item](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/item) { get; } | Gets the Raw tag with the specified id. (2 indexers) |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [ModifiedColorTemp](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedcolortemp) { get; } | Gets the ModifiedColorTemp. |
| [ModifiedDigitalGain](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifieddigitalgain) { get; } | Gets the ModifiedDigitalGain. |
| [ModifiedPictureStyle](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedpicturestyle) { get; } | Gets the ModifiedPictureStyle. |
| [ModifiedSensorBlueLevel](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedsensorbluelevel) { get; } | Gets the ModifiedSensorBlueLevel. |
| [ModifiedSensorRedLevel](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedsensorredlevel) { get; } | Gets the ModifiedSensorRedLevel. |
| [ModifiedSharpness](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedsharpness) { get; } | Gets the ModifiedSharpness. |
| [ModifiedSharpnessFreq](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedsharpnessfreq) { get; } | Gets the ModifiedSharpnessFreq. |
| [ModifiedToneCurve](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedtonecurve) { get; } | Gets the ModifiedToneCurve. |
| [ModifiedWhiteBalance](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedwhitebalance) { get; } | Gets the ModifiedWhiteBalance. |
| [ModifiedWhiteBalanceBlue](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedwhitebalanceblue) { get; } | Gets the ModifiedWhiteBalanceBlue. |
| [ModifiedWhiteBalanceRed](../../groupdocs.metadata.formats.raw.cr2/cr2modifiedinfopackage/modifiedwhitebalancered) { get; } | Gets the ModifiedWhiteBalanceRed. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |

## Methods

| Name | Description |
| --- | --- |
| virtual [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Adds known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |
| [Clear](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/clear)() | Removes all Raw tags stored in the package. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determines whether the package contains a metadata property with the specified name. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Returns an enumerator that iterates through the collection. |
| [Remove](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/remove)(uint) | Removes the property with the specified id. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Removes metadata properties satisfying the specified predicate. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Removes writable metadata properties from the package. The operation is recursive so it affects all nested packages as well. |
| [Set](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/set)(RawTag) | Adds or replaces the specified tag. |
| virtual [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) and [`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in the package that satisfies the predicate it is added to the package. |
| [ToList](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage/tolist)() | Creates a list from the package. |
| virtual [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

### See Also

* class [RawDictionaryBasePackage](../../groupdocs.metadata.formats.raw/rawdictionarybasepackage)
* namespace [GroupDocs.Metadata.Formats.Raw.Cr2](../../groupdocs.metadata.formats.raw.cr2)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
