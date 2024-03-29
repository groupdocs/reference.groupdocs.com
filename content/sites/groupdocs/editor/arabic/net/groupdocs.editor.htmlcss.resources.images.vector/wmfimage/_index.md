---
title: WmfImage
second_title: GroupDocs.Editor لمرجع .NET API
description: يمثل صورة متجهية واحدة بتنسيق WMF Windows MetaFile مع البيانات الوصفية والأساليب الإضافية
type: docs
weight: 610
url: /ar/net/groupdocs.editor.htmlcss.resources.images.vector/wmfimage/
---
## WmfImage class

يمثل صورة متجهية واحدة بتنسيق WMF (Windows MetaFile) مع البيانات الوصفية والأساليب الإضافية

```csharp
public sealed class WmfImage : MetaImageBase
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [WmfImage](wmfimage#constructor)(string, Stream) | إنشاء مثيل WmfImage جديد من المحتوى ، يتم تمثيله على شكل دفق بايت ، وباسم محدد |
| [WmfImage](wmfimage#constructor_1)(string, string) | إنشاء مثيل WmfImage جديد من المحتوى ، يتم تمثيله كسلسلة مشفرة باستخدام base64 ، وباسم محدد |

## الخصائص

| اسم | وصف |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/aspectratio) { get; } | إرجاع نسبة العرض إلى الارتفاع لهذه الصورة المتجهة |
| override [ByteContent](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/bytecontent) { get; } | إرجاع محتوى صورة WMF هذه على هيئة دفق ثنائي |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/filenamewithextension) { get; } | إرجاع اسم الملف الصحيح لهذه الصورة المتجهة ، والتي تتكون من الاسم والامتداد. من الناحية النظرية يمكن أن تختلف عن الاسم. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/isdisposed) { get; } | لتحديد ما إذا كان سيتم التخلص من هذه الصورة النقطية (`حقيقي`) أم لا (`خطأ شنيع` ) |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/lineardimensions) { get; } | إرجاع الأبعاد الخطية لهذه الصورة المتجهة (العرض والارتفاع) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/name) { get; } | يقوم بإرجاع اسم هذه الصورة المتجهة. عادة لا يحتوي على امتداد اسم الملف ويمكن نظريًا أن يختلف عن اسم الملف. |
| override [TextContent](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/textcontent) { get; } | إرجاع محتوى صورة WMF كنص عادي |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/type) { get; } | إرجاع ImageType.Wmf |

## طُرق

| اسم | وصف |
| --- | --- |
| override [Dispose](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/dispose)() | التخلص من صورة WMF هذه عن طريق التخلص من محتواها وجعل معظم أساليبها وخصائصها غير عاملة |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/equals)(IHtmlResource) | التحقق من هذا المثيل بالمساواة المحددة في المرجع . |
| override [Save](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/save)(string) | يحفظ صورة WMF هذه في file |
| override [SaveToPng](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/savetopng)(Stream) | يحفظ صورة WMF المتجهة هذه في صورة PNG نقطية |
| override [SaveToSvg](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/savetosvg)(Stream) | يحفظ صورة WMF المتجهية هذه في صورة متجهية SVG |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/isvalid#isvalid)(Stream) | للتحقق مما إذا كان الدفق المحدد صورة WMF صالحة |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.vector/wmfimage/isvalid#isvalid_1)(string) | للتحقق مما إذا كانت السلسلة المحددة بترميز base64 هي صورة WMF صالحة |

## الأحداث

| اسم | وصف |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/disposed) | الحدث الذي يحدث عند التخلص من هذه الصورة النقطية |

### أنظر أيضا

* class [MetaImageBase](../metaimagebase)
* مساحة الاسم [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../groupdocs.editor.htmlcss.resources.images.vector)
* المجسم [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
