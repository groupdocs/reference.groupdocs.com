---
title: ShapePossibleWatermarkT
second_title: GroupDocs.Watermark for .NET API Reference
description: Represents shape watermark in a content of any supported format.
type: docs
weight: 2760
url: /net/groupdocs.watermark.search/shapepossiblewatermark-1/
---
## ShapePossibleWatermark&lt;T&gt; class

Represents shape watermark in a content of any supported format.

```csharp
public abstract class ShapePossibleWatermark<T> : TwoDObjectPossibleWatermark
    where T : ShapeSearchAdapter, ITwoDObject
```

| Parameter | Description |
| --- | --- |
| T | The type of the shape. |

## Properties

| Name | Description |
| --- | --- |
| override [FormattedTextFragments](../../groupdocs.watermark.search/shapepossiblewatermark-1/formattedtextfragments) { get; } | Gets the collection of formatted text fragments of the shape. |
| override [Height](../../groupdocs.watermark.search/twodobjectpossiblewatermark/height) { get; } | Gets the height of the 2D object. |
| [ImageData](../../groupdocs.watermark.search/possiblewatermark/imagedata) { get; set; } | Gets or sets the image of this [`PossibleWatermark`](../possiblewatermark). |
| abstract [Parent](../../groupdocs.watermark.search/possiblewatermark/parent) { get; } | Gets the parent of this [`PossibleWatermark`](../possiblewatermark). |
| override [RotateAngle](../../groupdocs.watermark.search/shapepossiblewatermark-1/rotateangle) { get; } | Gets the rotate angle of the shape in degrees. |
| override [Text](../../groupdocs.watermark.search/shapepossiblewatermark-1/text) { get; set; } | Gets or sets the text of the shape. |
| override [UnitOfMeasurement](../../groupdocs.watermark.search/twodobjectpossiblewatermark/unitofmeasurement) { get; } | Gets the unit of measurement of the 2D object. |
| override [Width](../../groupdocs.watermark.search/twodobjectpossiblewatermark/width) { get; } | Gets the width of the 2D object. |
| override [X](../../groupdocs.watermark.search/twodobjectpossiblewatermark/x) { get; } | Gets the x-coordinate of the 2D object. |
| override [Y](../../groupdocs.watermark.search/twodobjectpossiblewatermark/y) { get; } | Gets the y-coordinate of the 2D object. |

### See Also

* class [TwoDObjectPossibleWatermark](../twodobjectpossiblewatermark)
* class [ShapeSearchAdapter](../shapesearchadapter)
* interface [ITwoDObject](../itwodobject)
* namespace [GroupDocs.Watermark.Search](../../groupdocs.watermark.search)
* assembly [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.watermark.dll -->
