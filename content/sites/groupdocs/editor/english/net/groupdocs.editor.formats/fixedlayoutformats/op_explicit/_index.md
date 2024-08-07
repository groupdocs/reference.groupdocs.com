---
title: op_Explicit
second_title: GroupDocs.Editor for .NET API Reference
description: Converts a string representing a file extension to a FixedLayoutFormatsgroupdocs.editor.formats/fixedlayoutformats object.
type: docs
weight: 40
url: /net/groupdocs.editor.formats/fixedlayoutformats/op_explicit/
---
## FixedLayoutFormats Explicit operator

Converts a string representing a file extension to a [`FixedLayoutFormats`](../../fixedlayoutformats) object.

```csharp
public static explicit operator FixedLayoutFormats(string extension)
```

| Parameter | Type | Description |
| --- | --- | --- |
| extension | String | The file extension to convert. If the extension contains multiple periods, the part after the last period is used. |

### Return Value

A [`FixedLayoutFormats`](../../fixedlayoutformats) object corresponding to the specified file extension.

### Exceptions

| exception | condition |
| --- | --- |
| [FixedLayoutFormats](../../fixedlayoutformats) | Thrown when the specified file extension is null. |

### See Also

* class [FixedLayoutFormats](../../fixedlayoutformats)
* namespace [GroupDocs.Editor.Formats](../../../groupdocs.editor.formats)
* assembly [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->
