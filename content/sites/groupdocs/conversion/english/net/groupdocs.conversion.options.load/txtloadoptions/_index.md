---
title: TxtLoadOptions
second_title: GroupDocs.Conversion for .NET API Reference
description: Options for loading Txt documents.
type: docs
weight: 2720
url: /net/groupdocs.conversion.options.load/txtloadoptions/
---
## TxtLoadOptions class

Options for loading Txt documents.

```csharp
public sealed class TxtLoadOptions : LoadOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [TxtLoadOptions](txtloadoptions)() | Initializes new instance of [`TxtLoadOptions`](../txtloadoptions) class. |

## Properties

| Name | Description |
| --- | --- |
| [DetectNumberingWithWhitespaces](../../groupdocs.conversion.options.load/txtloadoptions/detectnumberingwithwhitespaces) { get; set; } | Allows to specify how numbered list items are recognized when plain text document is converted. The default value is true. |
| [Encoding](../../groupdocs.conversion.options.load/txtloadoptions/encoding) { get; set; } | Gets or sets the encoding that will be used when loading Txt document. Can be null. Default is null. |
| [Format](../../groupdocs.conversion.options.load/txtloadoptions/format) { get; } | Input document file type. |
| virtual [Format](../../groupdocs.conversion.options.load/loadoptions/format) { get; } | Input document file type. |
| [LeadingSpacesOptions](../../groupdocs.conversion.options.load/txtloadoptions/leadingspacesoptions) { get; set; } | Gets or sets preferred option of a leading space handling. Default value is [`ConvertToIndent`](../txtleadingspacesoptions/converttoindent). |
| [TrailingSpacesOptions](../../groupdocs.conversion.options.load/txtloadoptions/trailingspacesoptions) { get; set; } | Gets or sets preferred option of a trailing space handling. Default value is [`Trim`](../txttrailingspacesoptions/trim). |

## Methods

| Name | Description |
| --- | --- |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Determines whether two object instances are equal. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Determines whether two object instances are equal. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Serves as the default hash function. |

### See Also

* class [LoadOptions](../loadoptions)
* namespace [GroupDocs.Conversion.Options.Load](../../groupdocs.conversion.options.load)
* assembly [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.conversion.dll -->
