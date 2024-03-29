---
title: XpsSaveOptions
second_title: GroupDocs.Editor لمرجع .NET API
description: يسمح بتحديد خيارات مخصصة لإنشاء مستندات XPS مواصفات ورق XML وحفظها
type: docs
weight: 1310
url: /ar/net/groupdocs.editor.options/xpssaveoptions/
---
## XpsSaveOptions class

يسمح بتحديد خيارات مخصصة لإنشاء مستندات XPS (مواصفات ورق XML) وحفظها

```csharp
public sealed class XpsSaveOptions : ISaveOptions
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [XpsSaveOptions](xpssaveoptions)() | Default_Constructor |

## الخصائص

| اسم | وصف |
| --- | --- |
| [OptimizeMemoryUsage](../../groupdocs.editor.options/xpssaveoptions/optimizememoryusage) { get; set; } | تمكين آليات تحسين الذاكرة أثناء إنشاء المستندات من HTML ، مما يقلل من الأداء كتكلفة لتقليل استخدام الذاكرة . يمكن أن يؤدي تعيين هذا الخيار على القيمة الحقيقية إلى تقليل استهلاك الذاكرة بشكل كبير أثناء إنشاء مستندات كبيرة بتكلفة توفير الوقت البطيء . الإعداد الافتراضي خطأ (تم تعطيل تحسين الذاكرة من أجل أداء أفضل) . |

### ملاحظات

يمثل ملف XPS ملفات تخطيط الصفحة التي تستند إلى مواصفات ورق XML التي أنشأتها Microsoft . تم تطويره كبديل لتنسيق ملف EMF وهو مشابه لتنسيق ملف PDF ، ولكنه يستخدم XML في التخطيط والمظهر ومعلومات الطباعة الخاصة بـ وثيقة.

### أنظر أيضا

* interface [ISaveOptions](../isaveoptions)
* مساحة الاسم [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* المجسم [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
