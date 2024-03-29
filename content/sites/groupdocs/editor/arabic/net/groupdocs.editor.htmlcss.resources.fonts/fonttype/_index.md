---
title: FontType
second_title: GroupDocs.Editor لمرجع .NET API
description: يمثل نوع خط واحد يمكن دعمه
type: docs
weight: 380
url: /ar/net/groupdocs.editor.htmlcss.resources.fonts/fonttype/
---
## FontType structure

يمثل نوع خط واحد يمكن دعمه

```csharp
public struct FontType : IEquatable<FontType>, IResourceType
```

## الخصائص

| اسم | وصف |
| --- | --- |
| static [Eot](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/eot) { get; } | يمثل نوع خط EOT (OpenType مضمن) |
| static [Otf](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/otf) { get; } | يمثل نوع خط OTF (خط OpenType ) |
| static [Ttf](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/ttf) { get; } | يمثل نوع خط TTF (خط TrueType ) |
| static [Undefined](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/undefined) { get; } | قيمة خاصة ، والتي تشير إلى مورد خط غير معروف أو غير معروف أو غير مدعوم |
| static [Woff](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/woff) { get; } | يمثل نوع خط WOFF (تنسيق خط الويب المفتوح) |
| static [Woff2](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/woff2) { get; } | يمثل WOFF2 (تنسيق خط الويب المفتوح الإصدار 2) نوع الخط |
| [CssName](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/cssname) { get; } | إرجاع اسم متوافق مع CSS لنوع الخط هذا ، والذي يُستخدم في @ font-face at-rule |
| [FileExtension](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/fileextension) { get; } | امتداد اسم الملف (بدون حرف نقطة) لنوع الخط هذا |
| [FontFormat](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/fontformat) { get; } | تنسيق الخط لـ @ font-face format |
| [FormalName](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/formalname) { get; } | إرجاع الاسم الرسمي لنوع الخط هذا |
| [MimeCode](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/mimecode) { get; } | كود MIME لنوع خط معين |

## طُرق

| اسم | وصف |
| --- | --- |
| static [GetFirstDefined](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/getfirstdefined)(params FontType[]) | إرجاع نوع الخط الأول من مجموعة محددة ، وهي ليست قيمة "غير محددة" ، أو نوع خط "غير محدد" وإلا (عندما تكون جميع العناصر "غير محددة") |
| static [ParseFromCssName](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/parsefromcssname)(string) | إرجاع قيمة نوع الخط ، والتي تعادل الاسم المحدد المتوافق مع CSS لنوع الخط |
| static [ParseFromFilenameWithExtension](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/parsefromfilenamewithextension)(string) | إرجاع قيمة نوع الخط ، التي تعادل ملحق اسم الملف ، المستخرج من اسم الملف المحدد |
| static [ParseFromMime](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/parsefrommime)(string) | إرجاع قيمة نوع الخط ، والتي تعادل MIME-code |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/equals#equals)(FontType) | تحديد ما إذا كان هذا المثيل مساويًا لـ "نوع الخط" مثيل |
| override [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/equals#equals_1)(object) | تحديد ما إذا كان هذا المثيل مساويًا لكائن غير مسبوق محدد ، والذي يفترض أنه مثيل "نوع الخط" آخر |
| override [GetHashCode](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/gethashcode)() | إرجاع رمز التجزئة ، وهو رقم ثابت لنوع القيمة المحددة هذا |
| [operator ==](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/op_equality) | التحقق مما إذا كانت قيمتا "FontType" متساويتين |
| [operator !=](../../groupdocs.editor.htmlcss.resources.fonts/fonttype/op_inequality) | التحقق مما إذا كانت قيمتا "FontType" غير متساويتين |

### أنظر أيضا

* interface [IResourceType](../../groupdocs.editor.htmlcss.resources/iresourcetype)
* مساحة الاسم [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../groupdocs.editor.htmlcss.resources.fonts)
* المجسم [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
