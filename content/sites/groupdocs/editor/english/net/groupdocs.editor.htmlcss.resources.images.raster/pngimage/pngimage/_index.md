---
title: PngImage
second_title: GroupDocs.Editor for .NET API Reference
description: Creates new PngImage instance from content represented as base64encoded string and with specified name
type: docs
weight: 10
url: /net/groupdocs.editor.htmlcss.resources.images.raster/pngimage/pngimage/
---
## PngImage(string, string) {#constructor_1}

Creates new PngImage instance from content, represented as base64-encoded string, and with specified name

```csharp
public PngImage(string name, string contentInBase64)
```

| Parameter | Type | Description |
| --- | --- | --- |
| name | String | Name of the PNG image. Cannot be null, empty or whitespaces. |
| contentInBase64 | String | Content as base64-encoded string. Cannot be null, empty or whitespaces. If it is not a PNG content, exception will be thrown. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### See Also

* class [PngImage](../../pngimage)
* namespace [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../pngimage)
* assembly [GroupDocs.Editor](../../../)

---

## PngImage(string, Stream) {#constructor}

Creates new PngImage instance from content, represented as byte stream, and with specified name

```csharp
public PngImage(string name, Stream binaryContent)
```

| Parameter | Type | Description |
| --- | --- | --- |
| name | String | Name of the PNG image. Cannot be null, empty or whitespaces. |
| binaryContent | Stream | Content as byte stream. Reading begins from original position. Cannot be null. Should be readable and seekable. If this instance will be disposed, this stream will be disposed too. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### See Also

* class [PngImage](../../pngimage)
* namespace [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../pngimage)
* assembly [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->