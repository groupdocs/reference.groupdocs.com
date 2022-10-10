---
title: EpubSaveOptions
second_title: GroupDocs.Editor for .NET API Reference
description: Allows to specify custom options for generating and saving the IDPF EPUB documents open standard for ebooks created by the International Digital Publishing Forum
type: docs
weight: 720
url: /net/groupdocs.editor.options/epubsaveoptions/
---
## EpubSaveOptions class

Allows to specify custom options for generating and saving the IDPF EPUB documents (open standard for e-books created by the International Digital Publishing Forum)

```csharp
public sealed class EpubSaveOptions : ISaveOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [EpubSaveOptions](epubsaveoptions)() | The default constructor. |

## Properties

| Name | Description |
| --- | --- |
| [ExportDocumentProperties](../../groupdocs.editor.options/epubsaveoptions/exportdocumentproperties) { get; set; } | Specifies whether to export built-in and custom document properties in IDPF EPUB format. Default value is `false`. |
| [SplitHeadingLevel](../../groupdocs.editor.options/epubsaveoptions/splitheadinglevel) { get; set; } | Specifies the maximum level of headings at which to split the ePub file. Default value is `2`. Setting it to `0` will disable splitting, so all content of the e-Book will be incorporarted into a single package inside the ePub. |

### See Also

* interface [ISaveOptions](../isaveoptions)
* namespace [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* assembly [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->