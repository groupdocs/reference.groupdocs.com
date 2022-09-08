---
title: FromExtension
second_title: GroupDocs.Editor for .NET API Reference
description: Returns instance of EmailFormatsgroupdocs.editor.formats/emailformats structure associated to specified filename extension or throws an exception if extension cannot be properly parsed
type: docs
weight: 120
url: /net/groupdocs.editor.formats/emailformats/fromextension/
---
## EmailFormats.FromExtension method

Returns instance of [`EmailFormats`](../../emailformats) structure, associated to specified filename extension, or throws an exception, if extension cannot be properly parsed

```csharp
public static EmailFormats FromExtension(string extension)
```

| Parameter | Type | Description |
| --- | --- | --- |
| extension | String | Filename extension of any supportable Email format, with or without leading dot character, case-independent. Cannot be NULL or empty, should be valid. |

### Return Value

Instance of [`EmailFormats`](../../emailformats) structure on success or thrown exception on failure

### See Also

* struct [EmailFormats](../../emailformats)
* namespace [GroupDocs.Editor.Formats](../../emailformats)
* assembly [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->