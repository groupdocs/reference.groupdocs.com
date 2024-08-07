---
title: DocumentFormatBase
second_title: GroupDocs.Editor for .NET API Reference
description: Represents the base class for document formats providing common functionality for format instances.
type: docs
weight: 50
url: /net/groupdocs.editor.formats.abstraction/documentformatbase/
---
## DocumentFormatBase class

Represents the base class for document formats, providing common functionality for format instances.

```csharp
public abstract class DocumentFormatBase : FormatFamilyBase, IDocumentFormat
```

## Properties

| Name | Description |
| --- | --- |
| [Extension](../../groupdocs.editor.formats.abstraction/documentformatbase/extension) { get; } | Gets the file extension of the document format. |
| [FormatFamily](../../groupdocs.editor.formats.abstraction/documentformatbase/formatfamily) { get; } | Gets the format family to which the document format belongs. |
| [Id](../../groupdocs.editor.formats.abstraction/formatfamilybase/id) { get; } | Gets the unique identifier for the format family. |
| [Mime](../../groupdocs.editor.formats.abstraction/documentformatbase/mime) { get; } | Gets the MIME type of the document format. |
| [Name](../../groupdocs.editor.formats.abstraction/formatfamilybase/name) { get; } | Gets the name of the format family. |

## Methods

| Name | Description |
| --- | --- |
| [Equals](../../groupdocs.editor.formats.abstraction/formatfamilybase/equals)(FormatFamilyBase) | Determines whether this instance is equal to the specified [`FormatFamilyBase`](../formatfamilybase) instance. |
| [Equals](../../groupdocs.editor.formats.abstraction/documentformatbase/equals#equals_1)(IDocumentFormat) | Determines whether this instance is equal to the specified [`IDocumentFormat`](../idocumentformat) instance. |
| override [Equals](../../groupdocs.editor.formats.abstraction/documentformatbase/equals#equals_2)(object) | Determines whether this instance is equal to the specified [`DocumentFormatBase`](../documentformatbase) instance. |
| override [GetHashCode](../../groupdocs.editor.formats.abstraction/documentformatbase/gethashcode)() | Returns a hash code for the current object. |
| override [ToString](../../groupdocs.editor.formats.abstraction/formatfamilybase/tostring)() | Returns a string that represents the current object. |
| static [FromMime&lt;T&gt;](../../groupdocs.editor.formats.abstraction/documentformatbase/frommime)(string) | Retrieves an instance of the specified type *T* that has the specified MIME type. |
| [implicit operator](../../groupdocs.editor.formats.abstraction/documentformatbase/op_implicit) | Converts a [`DocumentFormatBase`](../documentformatbase) instance to a string implicitly. |

### See Also

* class [FormatFamilyBase](../formatfamilybase)
* interface [IDocumentFormat](../idocumentformat)
* namespace [GroupDocs.Editor.Formats.Abstraction](../../groupdocs.editor.formats.abstraction)
* assembly [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->
