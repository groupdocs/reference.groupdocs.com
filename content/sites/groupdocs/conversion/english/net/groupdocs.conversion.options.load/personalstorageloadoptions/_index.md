---
title: PersonalStorageLoadOptions
second_title: GroupDocs.Conversion for .NET API Reference
description: Options for loading personal storage documents.
type: docs
weight: 2610
url: /net/groupdocs.conversion.options.load/personalstorageloadoptions/
---
## PersonalStorageLoadOptions class

Options for loading personal storage documents.

```csharp
public sealed class PersonalStorageLoadOptions : LoadOptions, IDocumentsContainerLoadOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [PersonalStorageLoadOptions](personalstorageloadoptions)() | Initializes new instance of [`PersonalStorageLoadOptions`](../personalstorageloadoptions) class. |

## Properties

| Name | Description |
| --- | --- |
| [ConvertOwned](../../groupdocs.conversion.options.load/personalstorageloadoptions/convertowned) { get; } | Implements [`ConvertOwned`](../../groupdocs.conversion.contracts/idocumentscontainerloadoptions/convertowned) Readonly. Set to true. The owned documents will be converted |
| [ConvertOwner](../../groupdocs.conversion.options.load/personalstorageloadoptions/convertowner) { get; } | Implements [`ConvertOwner`](../../groupdocs.conversion.contracts/idocumentscontainerloadoptions/convertowner) Readonly. Set to false. The owner will not be converted |
| [Depth](../../groupdocs.conversion.options.load/personalstorageloadoptions/depth) { get; set; } | Implements [`Depth`](../../groupdocs.conversion.contracts/idocumentscontainerloadoptions/depth) Default: 3 |
| [Folder](../../groupdocs.conversion.options.load/personalstorageloadoptions/folder) { get; set; } | Folder which to be processed Default is Inbox |
| [Format](../../groupdocs.conversion.options.load/personalstorageloadoptions/format) { get; set; } | Input document file type. |
| virtual [Format](../../groupdocs.conversion.options.load/loadoptions/format) { get; } | Input document file type. |

## Methods

| Name | Description |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.load/personalstorageloadoptions/clone)() | Clones current instance. |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Determines whether two object instances are equal. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Determines whether two object instances are equal. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Serves as the default hash function. |

### See Also

* class [LoadOptions](../loadoptions)
* interface [IDocumentsContainerLoadOptions](../../groupdocs.conversion.contracts/idocumentscontainerloadoptions)
* namespace [GroupDocs.Conversion.Options.Load](../../groupdocs.conversion.options.load)
* assembly [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.conversion.dll -->
