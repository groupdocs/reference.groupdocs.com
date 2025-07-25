---
title: RasterImageLoadOptions
second_title: GroupDocs.Conversion for .NET API Reference
description: Options for loading Image documents.
type: docs
weight: 2660
url: /net/groupdocs.conversion.options.load/rasterimageloadoptions/
---
## RasterImageLoadOptions class

Options for loading Image documents.

```csharp
public sealed class RasterImageLoadOptions : BaseImageLoadOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [RasterImageLoadOptions](rasterimageloadoptions)() | Initializes new instance of [`ImageLoadOptions`](../imageloadoptions) class. |

## Properties

| Name | Description |
| --- | --- |
| [CropArea](../../groupdocs.conversion.options.load/rasterimageloadoptions/croparea) { get; set; } | Crop image area before conversion |
| [DefaultFont](../../groupdocs.conversion.options.load/baseimageloadoptions/defaultfont) { get; set; } | Default font for Psd, Emf, Wmf document types. The following font will be used if a font is missing. |
| [Format](../../groupdocs.conversion.options.load/rasterimageloadoptions/format) { get; set; } | Input document file type. |
| virtual [Format](../../groupdocs.conversion.options.load/loadoptions/format) { get; } | Input document file type. |
| [ResetFontFolders](../../groupdocs.conversion.options.load/baseimageloadoptions/resetfontfolders) { get; set; } | Reset font folders before loading document |
| [VectorizationOptions](../../groupdocs.conversion.options.load/rasterimageloadoptions/vectorizationoptions) { get; set; } | Sets vectorization options |

## Methods

| Name | Description |
| --- | --- |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Determines whether two object instances are equal. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Determines whether two object instances are equal. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Serves as the default hash function. |
| [SetHeicConnector](../../groupdocs.conversion.options.load/rasterimageloadoptions/setheicconnector)(IHeicConnector) | Set Heic image connector |
| [SetOcrConnector](../../groupdocs.conversion.options.load/rasterimageloadoptions/setocrconnector)(IOcrConnector) | Set image OCR connector |

### See Also

* class [BaseImageLoadOptions](../baseimageloadoptions)
* namespace [GroupDocs.Conversion.Options.Load](../../groupdocs.conversion.options.load)
* assembly [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.conversion.dll -->
