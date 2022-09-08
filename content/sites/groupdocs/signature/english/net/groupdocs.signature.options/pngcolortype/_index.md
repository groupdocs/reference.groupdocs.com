---
title: PngColorType
second_title: GroupDocs.Signature for .NET API Reference
description: Represents the PNG image color type.
type: docs
weight: 1450
url: /net/groupdocs.signature.options/pngcolortype/
---
## PngColorType enumeration

Represents the PNG image color type.

```csharp
[Flags]
public enum PngColorType
```

### Values

| Name | Value | Description |
| --- | --- | --- |
| Grayscale | `0` | Represents the color type where each pixel is a grayscale sample. |
| Truecolor | `2` | Represents the color type where each pixel is an R,G,B triple. |
| IndexedColor | `3` | Represents the color type where each pixel is a palette index; a PLTE chunk shall appear. |
| GrayscaleWithAlpha | `4` | Represents the color type where each pixel is a grayscale sample followed by an alpha sample. |
| TruecolorWithAlpha | `6` | Represents the color type where each pixel is an R,G,B triple followed by an alpha sample. |

### See Also

* namespace [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* assembly [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->