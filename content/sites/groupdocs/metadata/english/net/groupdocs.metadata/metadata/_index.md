---
title: Metadata
second_title: GroupDocs.Metadata for .NET API Reference
description: Provides the main class to access metadata in all supported formats.
type: docs
weight: 4220
url: /net/groupdocs.metadata/metadata/
---
## Metadata class

Provides the main class to access metadata in all supported formats.

```csharp
public sealed class Metadata : IDisposable
```

## Constructors

| Name | Description |
| --- | --- |
| [Metadata](metadata#constructor)(Stream) | Initializes a new instance of the [`Metadata`](../metadata) class. |
| [Metadata](metadata#constructor_2)(string) | Initializes a new instance of the [`Metadata`](../metadata) class. |
| [Metadata](metadata#constructor_4)(Uri) | Initializes a new instance of the [`Metadata`](../metadata) class. |
| [Metadata](metadata#constructor_1)(Stream, LoadOptions) | Initializes a new instance of the [`Metadata`](../metadata) class. |
| [Metadata](metadata#constructor_3)(string, LoadOptions) | Initializes a new instance of the [`Metadata`](../metadata) class. |
| [Metadata](metadata#constructor_5)(Uri, LoadOptions) | Initializes a new instance of the [`Metadata`](../metadata) class. |

## Properties

| Name | Description |
| --- | --- |
| [FileFormat](../../groupdocs.metadata/metadata/fileformat) { get; } | Gets the type of the loaded file (if recognized). |

## Methods

| Name | Description |
| --- | --- |
| [AddProperties](../../groupdocs.metadata/metadata/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Adds known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |
| [CopyTo](../../groupdocs.metadata/metadata/copyto#copyto_1)(MetadataPackage) | Copy known metadata properties from source package to destination package. The operation is recursive so it affects all nested packages as well. If an existing property its value is updated. If there is a known property missing in a destination package it is added to the package. If there is a known property missing in a source package it is not remove from destination package. If that need, use Sanitize method before. |
| [CopyTo](../../groupdocs.metadata/metadata/copyto#copyto)(MetadataPackage, List&lt;PropertyTag&gt;) | Copy known metadata properties from source package to destination package. The operation is recursive so it affects all nested packages as well. If an existing property its value is updated. If there is a known property missing in a destination package it is added to the package. If there is a known property missing in a source package it is not remove from destination package. If that need, use Sanitize method before. |
| [Dispose](../../groupdocs.metadata/metadata/dispose)() | Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources. |
| [FindProperties](../../groupdocs.metadata/metadata/findproperties)(Func&lt;MetadataProperty, bool&gt;) | Finds the metadata properties satisfying the specified predicate. The search is recursive so it affects all nested packages as well. |
| [GeneratePreview](../../groupdocs.metadata/metadata/generatepreview)(PreviewOptions) | Creates preview images for specified pages. |
| [GetDocumentInfo](../../groupdocs.metadata/metadata/getdocumentinfo)() | Gets common information about the loaded document. |
| [GetRootPackage](../../groupdocs.metadata/metadata/getrootpackage#getrootpackage)() | Gets the root package providing access to all metadata properties extracted from the file. |
| [GetRootPackage&lt;TRoot&gt;](../../groupdocs.metadata/metadata/getrootpackage#getrootpackage_1)() | Gets the root package providing access to all metadata properties extracted from the file. |
| [RemoveProperties](../../groupdocs.metadata/metadata/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | Removes metadata properties satisfying the specified predicate. |
| [Sanitize](../../groupdocs.metadata/metadata/sanitize)() | Removes writable metadata properties from all detected packages or whole packages if possible. The operation is recursive so it affects all nested packages as well. |
| [Save](../../groupdocs.metadata/metadata/save#save)() | Saves all changes made in the loaded document. |
| [Save](../../groupdocs.metadata/metadata/save#save_1)(Stream) | Saves the document content into a stream. |
| [Save](../../groupdocs.metadata/metadata/save#save_2)(string) | Saves the document content to the specified file. |
| [SetProperties](../../groupdocs.metadata/metadata/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Sets known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. This method is a combination of [`AddProperties`](./addproperties) and [`UpdateProperties`](./updateproperties). If an existing property satisfies the predicate its value is updated. If there is a known property missing in a package that satisfies the predicate it is added to the package. |
| [UpdateProperties](../../groupdocs.metadata/metadata/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | Updates known metadata properties satisfying the specified predicate. The operation is recursive so it affects all nested packages as well. |

### See Also

* namespace [GroupDocs.Metadata](../../groupdocs.metadata)
* assembly [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.metadata.dll -->
