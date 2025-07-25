---
title: XmpPhotoshopPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents Adobe Photoshop namespace.
type: docs
weight: 4780
url: /net/groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/
---
## XmpPhotoshopPackage class

Represents Adobe Photoshop namespace.

```csharp
public sealed class XmpPhotoshopPackage : XmpPackage
```

## Constructors

| Name | Description |
| --- | --- |
| [XmpPhotoshopPackage](xmpphotoshoppackage)() | Initializes a new instance of the [`XmpPhotoshopPackage`](../xmpphotoshoppackage) class. |

## Properties

| Name | Description |
| --- | --- |
| [AuthorsPosition](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/authorsposition) { get; set; } | Gets or sets the by-line title. |
| [CaptionWriter](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/captionwriter) { get; set; } | Gets or sets the writer/editor. |
| [Category](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/category) { get; set; } | Gets or sets the category. Limited to 3 7-bit ASCII characters. |
| [City](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/city) { get; set; } | Gets or sets the city. |
| [ColorMode](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/colormode) { get; set; } | Gets or sets the color mode. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [Country](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/country) { get; set; } | Gets or sets the country. |
| [Credit](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/credit) { get; set; } | Gets or sets the credit. |
| [DateCreated](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/datecreated) { get; set; } | Gets or sets the date the intellectual content of the document was created. |
| [Headline](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/headline) { get; set; } | Gets or sets the headline. |
| [History](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/history) { get; set; } | Gets or sets the history that appears in the FileInfo panel, if activated in the application preferences. |
| [IccProfile](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/iccprofile) { get; set; } | Gets or sets the color profile, such as AppleRGB, AdobeRGB1998. |
| [Instructions](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/instructions) { get; set; } | Gets or sets the special instructions. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Gets the [`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) with the specified name. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [NamespaceUri](../../groupdocs.metadata.standards.xmp/xmppackage/namespaceuri) { get; } | Gets the namespace URI. |
| [Prefix](../../groupdocs.metadata.standards.xmp/xmppackage/prefix) { get; } | Gets the xmlns prefix. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [Source](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/source) { get; set; } | Gets or sets the source. |
| [State](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/state) { get; set; } | Gets or sets the province/state. |
| [SupplementalCategories](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/supplementalcategories) { get; set; } | Gets or sets the supplemental categories. |
| [TransmissionReference](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/transmissionreference) { get; set; } | Gets or sets the original transmission reference. |
| [Urgency](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/urgency) { get; set; } | Gets or sets the urgency. |
| [XmlNamespace](../../groupdocs.metadata.standards.xmp/xmppackage/xmlnamespace) { get; } | Gets the XML namespace. |

## Methods

| Name | Description |
| --- | --- |
| virtual [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Adds known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |
| [Clear](../../groupdocs.metadata.standards.xmp/xmppackage/clear)() | Removes all XMP properties. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | Determines whether the package contains a metadata property with the specified name. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | Returns an enumerator that iterates through the collection. |
| override [GetXmpRepresentation](../../groupdocs.metadata.standards.xmp/xmppackage/getxmprepresentation)() | Converts the XMP value to the XML representation. |
| [Remove](../../groupdocs.metadata.standards.xmp/xmppackage/remove)(string) | Removes the property with the specified name. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Removes metadata properties satisfying the specified predicate. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | Removes writable metadata properties from the package. The operation is recursive so it affects all nested packages as well. |
| [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, bool) | Sets boolean property. |
| [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, DateTime) | Sets DateTime property. |
| [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, double) | Sets double property. |
| [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, int) | Sets integer property. |
| override [Set](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/set#set_7)(string, string) | Sets string property. |
| virtual [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, XmpArray) | Sets the value inherited from [`XmpArray`](../../groupdocs.metadata.standards.xmp/xmparray) . |
| virtual [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, XmpComplexType) | Sets the value inherited from [`XmpComplexType`](../../groupdocs.metadata.standards.xmp/xmpcomplextype) . |
| [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, XmpValueBase) | Sets the value inherited from [`XmpValueBase`](../../groupdocs.metadata.standards.xmp/xmpvaluebase) . |
| virtual [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) and [`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in the package that satisfies the predicate it is added to the package. |
| virtual [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

## Fields

| Name | Description |
| --- | --- |
| const [UrgencyMax](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/urgencymax) | Urgency max value. |
| const [UrgencyMin](../../groupdocs.metadata.standards.xmp.schemes/xmpphotoshoppackage/urgencymin) | Urgency min value. |

### See Also

* class [XmpPackage](../../groupdocs.metadata.standards.xmp/xmppackage)
* namespace [GroupDocs.Metadata.Standards.Xmp.Schemes](../../groupdocs.metadata.standards.xmp.schemes)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
