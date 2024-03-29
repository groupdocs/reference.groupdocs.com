---
title: FontStyle
second_title: GroupDocs.Editor لمرجع .NET API
description: يحدد كيفية تصميم الخط باستخدام وجه عادي أو مائل أو مائل من عائلة الخطوط .
type: docs
weight: 300
url: /ar/net/groupdocs.editor.htmlcss.css.properties/fontstyle/
---
## FontStyle structure

يحدد كيفية تصميم الخط باستخدام: وجه عادي أو مائل أو مائل من عائلة الخطوط .

```csharp
public struct FontStyle
```

## الخصائص

| اسم | وصف |
| --- | --- |
| [IsInitial](../../groupdocs.editor.htmlcss.css.properties/fontstyle/isinitial) { get; } | يشير إلى ما إذا كان نمط الخط هذا يحتوي على قيمة أولية (عادي) |
| [Value](../../groupdocs.editor.htmlcss.css.properties/fontstyle/value) { get; } | إرجاع قيمة نمط الخط هذا كسلسلة |

## طُرق

| اسم | وصف |
| --- | --- |
| [Equals](../../groupdocs.editor.htmlcss.css.properties/fontstyle/equals#equals)(FontStyle) | لتحديد ما إذا كان مثيل نمط الخط هذا يساوي المحدد |
| override [Equals](../../groupdocs.editor.htmlcss.css.properties/fontstyle/equals#equals_1)(object) | تحديد ما إذا كان مثيل نمط الخط هذا مساويًا لـ uncasted المحدد |
| override [GetHashCode](../../groupdocs.editor.htmlcss.css.properties/fontstyle/gethashcode)() | إرجاع رمز تجزئة لهذا المثيل |
| static [TryParse](../../groupdocs.editor.htmlcss.css.properties/fontstyle/tryparse)(string, out FontStyle) | يحاول التعرف على كلمة رئيسية محددة على أنها قيمة كلمة رئيسية مناسبة لـ "نمط الخط" وإعادتها عند النجاح أو القيمة NULL عند الفشل. |
| [operator ==](../../groupdocs.editor.htmlcss.css.properties/fontstyle/op_equality) | التحقق مما إذا كانت قيمتا "FontStyle" متساويتين |
| [operator !=](../../groupdocs.editor.htmlcss.css.properties/fontstyle/op_inequality) | التحقق مما إذا كانت قيمتا "FontStyle" غير متساويتين |

## مجالات

| اسم | وصف |
| --- | --- |
| static readonly [Italic](../../groupdocs.editor.htmlcss.css.properties/fontstyle/italic) | تحديد خط مصنف على أنه مائل. في حالة عدم توفر نسخة مائلة من الوجه ، يتم استخدام نسخة مائلة بدلاً من ذلك. إذا لم يكن أي منهما متاحًا ، فسيتم محاكاة النمط بشكل مصطنع. |
| static readonly [Normal](../../groupdocs.editor.htmlcss.css.properties/fontstyle/normal) | يحدد خطًا مصنفًا كخط عادي ضمن عائلة الخطوط. القيمة الأولية . |
| static readonly [Oblique](../../groupdocs.editor.htmlcss.css.properties/fontstyle/oblique) | تحديد خط مصنف على أنه مائل. في حالة عدم توفر نسخة مائلة من الوجه ، يتم استخدام نسخة مصنفة على أنها مائلة بدلاً من ذلك. إذا لم يكن أي منهما متاحًا ، فسيتم محاكاة النمط بشكل مصطنع. |

### أنظر أيضا

* مساحة الاسم [GroupDocs.Editor.HtmlCss.Css.Properties](../../groupdocs.editor.htmlcss.css.properties)
* المجسم [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
