---
title: XmpMediaManagementPackage
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents the XMP Media Management namespace.
type: docs
weight: 4740
url: /net/groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/
---
## XmpMediaManagementPackage class

Represents the XMP Media Management namespace.

```csharp
public sealed class XmpMediaManagementPackage : XmpPackage
```

## Constructors

| Name | Description |
| --- | --- |
| [XmpMediaManagementPackage](xmpmediamanagementpackage)() | Initializes a new instance of the [`XmpMediaManagementPackage`](../xmpmediamanagementpackage) class. |

## Properties

| Name | Description |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [DerivedFrom](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/derivedfrom) { get; set; } | Gets or sets the reference to the resource from which this one is derived. |
| [DocumentID](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/documentid) { get; set; } | Gets or sets the common identifier for all versions and renditions of the resource. |
| [History](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/history) { get; set; } | Gets or sets an array of high-level actions that resulted in this resource. |
| [Ingredients](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/ingredients) { get; set; } | Gets or sets the references to resources that were incorporated, by inclusion or reference, into this resource. |
| [InstanceID](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/instanceid) { get; set; } | Gets or sets the identifier for a specific incarnation of a resource, updated each time the file is saved. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Gets the [`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) with the specified name. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [ManagedFrom](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/managedfrom) { get; set; } | Gets or sets the reference to the document as it was prior to becoming managed. |
| [Manager](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/manager) { get; set; } | Gets or sets the name of the asset management system that manages this resource. |
| [ManagerVariant](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/managervariant) { get; set; } | Gets or sets the particular variant of the asset management system. |
| [ManageTo](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/manageto) { get; set; } | Gets or sets the URI identifying the managed resource to the asset management system |
| [ManageUI](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/manageui) { get; set; } | Gets or sets the URI that can be used to access information about the managed resource through a web browser. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [NamespaceUri](../../groupdocs.metadata.standards.xmp/xmppackage/namespaceuri) { get; } | Gets the namespace URI. |
| [OriginalDocumentID](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/originaldocumentid) { get; set; } | Gets or sets the common identifier for the original resource from which the current resource is derived. |
| [Prefix](../../groupdocs.metadata.standards.xmp/xmppackage/prefix) { get; } | Gets the xmlns prefix. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |
| [RenditionClass](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/renditionclass) { get; set; } | Gets or sets the rendition class name for this resource. |
| [RenditionParams](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/renditionparams) { get; set; } | Gets or sets the value that is used to provide additional rendition parameters that are too complex or verbose to encode in xmpMM:RenditionClass. |
| [VersionID](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/versionid) { get; set; } | Gets or sets the document version identifier for this resource. |
| [Versions](../../groupdocs.metadata.standards.xmp.schemes/xmpmediamanagementpackage/versions) { get; set; } | Gets or sets the version history associated with this resource. |
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
| virtual [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, string) | Sets string property. |
| virtual [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, XmpArray) | Sets the value inherited from [`XmpArray`](../../groupdocs.metadata.standards.xmp/xmparray) . |
| virtual [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, XmpComplexType) | Sets the value inherited from [`XmpComplexType`](../../groupdocs.metadata.standards.xmp/xmpcomplextype) . |
| [Set](../../groupdocs.metadata.standards.xmp/xmppackage/set)(string, XmpValueBase) | Sets the value inherited from [`XmpValueBase`](../../groupdocs.metadata.standards.xmp/xmpvaluebase) . |
| virtual [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) and [`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in the package that satisfies the predicate it is added to the package. |
| virtual [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

### See Also

* class [XmpPackage](../../groupdocs.metadata.standards.xmp/xmppackage)
* namespace [GroupDocs.Metadata.Standards.Xmp.Schemes](../../groupdocs.metadata.standards.xmp.schemes)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
