---
title: BarcodeSettings
second_title: GroupDocs.Assembly for .NET API Reference
description: Represents a set of settings controlling barcode generation while assembling a document.
type: docs
weight: 10
url: /net/groupdocs.assembly/barcodesettings/
---
## BarcodeSettings class

Represents a set of settings controlling barcode generation while assembling a document.

```csharp
public class BarcodeSettings
```

## Properties

| Name | Description |
| --- | --- |
| [BaseXDimension](../../groupdocs.assembly/barcodesettings/basexdimension) { get; set; } | Gets or sets a base x-dimension, that is, the smallest width of the unit of barcode bars and spaces. Measured in [`GraphicsUnit`](./graphicsunit). |
| [BaseYDimension](../../groupdocs.assembly/barcodesettings/baseydimension) { get; set; } | Gets or sets a base y-dimension, that is, the smallest height of the unit of 2D barcode modules. Measured in [`GraphicsUnit`](./graphicsunit). |
| [GraphicsUnit](../../groupdocs.assembly/barcodesettings/graphicsunit) { get; set; } | Gets or sets a graphics unit used to measure [`BaseXDimension`](./basexdimension) and [`BaseYDimension`](./baseydimension). The default value is Millimeter. |
| [Resolution](../../groupdocs.assembly/barcodesettings/resolution) { get; set; } | Gets or sets the horizontal and vertical resolution of a barcode image being generated. Measured in dots per inch. The default value is 96. |
| [UseAutoCorrection](../../groupdocs.assembly/barcodesettings/useautocorrection) { get; set; } | Gets or sets a value indicating whether an invalid barcode value should be corrected automatically (if possible) to fit the barcode's specification or an exception should be thrown to indicate the error. The default value is true. |

### See Also

* namespace [GroupDocs.Assembly](../../groupdocs.assembly)
* assembly [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
