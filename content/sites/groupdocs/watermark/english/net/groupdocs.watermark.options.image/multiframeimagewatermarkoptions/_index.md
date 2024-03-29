---
title: MultiframeImageWatermarkOptions
second_title: GroupDocs.Watermark for .NET API Reference
description: Represents watermark adding options when adding watermark to a multiframe image.
type: docs
weight: 1840
url: /net/groupdocs.watermark.options.image/multiframeimagewatermarkoptions/
---
## MultiframeImageWatermarkOptions class

Represents watermark adding options when adding watermark to a multi-frame image.

```csharp
public class MultiframeImageWatermarkOptions : WatermarkOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [MultiframeImageWatermarkOptions](multiframeimagewatermarkoptions#constructor)() | Initializes a new instance of the [`MultiframeImageWatermarkOptions`](../multiframeimagewatermarkoptions) class. |
| [MultiframeImageWatermarkOptions](multiframeimagewatermarkoptions#constructor_1)(int) | Initializes a new instance of the [`MultiframeImageWatermarkOptions`](../multiframeimagewatermarkoptions) class with a specified index of the frame. |

## Properties

| Name | Description |
| --- | --- |
| [FrameIndex](../../groupdocs.watermark.options.image/multiframeimagewatermarkoptions/frameindex) { get; set; } | Gets or sets the index of frame to add watermark. |

### Remarks

**Learn more:**

* [Add watermarks to images](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+images)

### Examples

Add watermark to a particular frame of multi-frame image.

```csharp
ImageLoadOptions loadOptions = new ImageLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\test.gif", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test", new Font("Arial", 12));

    MultiframeImageWatermarkOptions options = new MultiframeImageWatermarkOptions();
    options.FrameIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### See Also

* class [WatermarkOptions](../../groupdocs.watermark.options/watermarkoptions)
* namespace [GroupDocs.Watermark.Options.Image](../../groupdocs.watermark.options.image)
* assembly [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->
