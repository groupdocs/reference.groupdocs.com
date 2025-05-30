---
title: Fb2Author
second_title: GroupDocs.Metadata for .NET API Reference
description: Represents an information about the author of the book.
type: docs
weight: 1520
url: /net/groupdocs.metadata.formats.ebook.fb2/fb2author/
---
## Fb2Author class

Represents an information about the author of the book.

```csharp
public class Fb2Author : CustomPackage
```

## Constructors

| Name | Description |
| --- | --- |
| [Fb2Author](fb2author)(string, string, string, string, string, string, string) |  |

## Properties

| Name | Description |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | Gets the number of metadata properties. |
| [Email](../../groupdocs.metadata.formats.ebook.fb2/fb2author/email) { get; } | Gets the Email. |
| [FirstName](../../groupdocs.metadata.formats.ebook.fb2/fb2author/firstname) { get; } | Gets the First Name. |
| [HomePage](../../groupdocs.metadata.formats.ebook.fb2/fb2author/homepage) { get; } | Gets the HomePage. |
| [Id](../../groupdocs.metadata.formats.ebook.fb2/fb2author/id) { get; } | Gets the Id. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | Gets the [`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) with the specified name. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | Gets a collection of the metadata property names. |
| [LastName](../../groupdocs.metadata.formats.ebook.fb2/fb2author/lastname) { get; } | Gets the Last Name. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | Gets the metadata type. |
| [MiddleName](../../groupdocs.metadata.formats.ebook.fb2/fb2author/middlename) { get; } | Gets the Middle Name. |
| [NickName](../../groupdocs.metadata.formats.ebook.fb2/fb2author/nickname) { get; } | Gets the NickName. |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | Gets a collection of descriptors that contain information about properties accessible through the GroupDocs.Metadata search engine. |

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

### See Also

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* namespace [GroupDocs.Metadata.Formats.Ebook.Fb2](../../groupdocs.metadata.formats.ebook.fb2)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
