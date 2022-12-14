---
title: TiffImageWatermarkOptions
second_title: GroupDocs.Watermark لـ .NET API Reference
description: يمثل خيارات إضافة العلامة المائية عند إضافة علامة مائية إلى صورة TIFF.
type: docs
weight: 1830
url: /ar/net/groupdocs.watermark.options.image/tiffimagewatermarkoptions/
---
## TiffImageWatermarkOptions class

يمثل خيارات إضافة العلامة المائية عند إضافة علامة مائية إلى صورة TIFF.

```csharp
public sealed class TiffImageWatermarkOptions : MultiframeImageWatermarkOptions
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [TiffImageWatermarkOptions](tiffimagewatermarkoptions#constructor)() | يقوم بتهيئة مثيل جديد لملف[`TiffImageWatermarkOptions`](../tiffimagewatermarkoptions) فئة . |
| [TiffImageWatermarkOptions](tiffimagewatermarkoptions#constructor_1)(int) | يقوم بتهيئة مثيل جديد لملف[`TiffImageWatermarkOptions`](../tiffimagewatermarkoptions) class مع فهرس محدد للإطار. |

## الخصائص

| اسم | وصف |
| --- | --- |
| [FrameIndex](../../groupdocs.watermark.options.image/multiframeimagewatermarkoptions/frameindex) { get; set; } | الحصول على أو تحديد فهرس الإطار لإضافة علامة مائية. |

### ملاحظات

**يتعلم أكثر:**

* [أضف العلامات المائية إلى الصور](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+images)

### أمثلة

أضف علامة مائية إلى إطار معين لصورة TIFF.

```csharp
TiffImageLoadOptions loadOptions = new TiffImageLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\test.tiff", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test", new Font("Arial", 12));

    TiffImageWatermarkOptions options = new TiffImageWatermarkOptions();
    options.FrameIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### أنظر أيضا

* class [MultiframeImageWatermarkOptions](../multiframeimagewatermarkoptions)
* مساحة الاسم [GroupDocs.Watermark.Options.Image](../../groupdocs.watermark.options.image)
* المجسم [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
