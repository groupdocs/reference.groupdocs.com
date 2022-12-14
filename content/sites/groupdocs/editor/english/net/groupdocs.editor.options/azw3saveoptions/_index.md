---
title: Azw3SaveOptions
second_title: GroupDocs.Editor for .NET API Reference
description: Allows to specify custom options for generating and saving the AZW3 ebooks also known as Kindle Format 8 KF8
type: docs
weight: 710
url: /net/groupdocs.editor.options/azw3saveoptions/
---
## Azw3SaveOptions class

Allows to specify custom options for generating and saving the AZW3 e-books, also known as Kindle Format 8 (KF8)

```csharp
public sealed class Azw3SaveOptions : ISaveOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [Azw3SaveOptions](azw3saveoptions)() | The default constructor. |

## Properties

| Name | Description |
| --- | --- |
| [SplitHeadingLevel](../../groupdocs.editor.options/azw3saveoptions/splitheadinglevel) { get; set; } | Specifies whether to split the content of AZW3 e-book onto packages and if yes, the maximum level of headings at which to split the content of the AZW3. Default value is `2`. Setting it to `0` will disable splitting, so all content of the e-book will be incorporarted into a single package inside the AZW3. |

### See Also

* interface [ISaveOptions](../isaveoptions)
* namespace [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* assembly [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->
