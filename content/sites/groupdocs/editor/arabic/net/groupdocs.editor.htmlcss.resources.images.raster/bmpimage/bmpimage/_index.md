---
title: BmpImage
second_title: GroupDocs.Editor لمرجع .NET API
description: إنشاء مثيل BmpImage جديد من المحتوى  يتم تمثيله كسلسلة بتشفير base64  وباسم محدد
type: docs
weight: 10
url: /ar/net/groupdocs.editor.htmlcss.resources.images.raster/bmpimage/bmpimage/
---
## BmpImage(string, string) {#constructor_1}

إنشاء مثيل BmpImage جديد من المحتوى ، يتم تمثيله كسلسلة بتشفير base64 ، وباسم محدد

```csharp
public BmpImage(string name, string contentInBase64)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| name | String | اسم صورة BMP. لا يمكن أن يكون فارغًا أو فارغًا أو مسافات بيضاء. |
| contentInBase64 | String | المحتوى كسلسلة بترميز base64. لا يمكن أن يكون فارغًا أو فارغًا أو مسافات بيضاء. إذا لم يكن محتوى BMP ، فسيتم طرح استثناء. |

### استثناءات

| استثناء | حالة |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### أنظر أيضا

* class [BmpImage](../../bmpimage)
* مساحة الاسم [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../bmpimage)
* المجسم [GroupDocs.Editor](../../../)

---

## BmpImage(string, Stream) {#constructor}

إنشاء مثيل BmpImage جديد من المحتوى ، يتم تمثيله على شكل دفق بايت ، وباسم محدد

```csharp
public BmpImage(string name, Stream binaryContent)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| name | String | اسم صورة BMP. لا يمكن أن يكون فارغًا أو فارغًا أو مسافات بيضاء. |
| binaryContent | Stream | المحتوى كتيار بايت. تبدأ القراءة من الموضع الأصلي. لا يمكن أن تكون لاغية. يجب أن يكون مقروءًا ويمكن البحث عنه. إذا تم التخلص من هذا المثيل ، فسيتم التخلص من هذا التدفق أيضًا. |

### استثناءات

| استثناء | حالة |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### أنظر أيضا

* class [BmpImage](../../bmpimage)
* مساحة الاسم [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../bmpimage)
* المجسم [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
