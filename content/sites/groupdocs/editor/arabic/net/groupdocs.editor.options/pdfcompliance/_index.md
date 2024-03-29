---
title: PdfCompliance
second_title: GroupDocs.Editor لمرجع .NET API
description: يحدد مستوى الامتثال لمعايير PDF
type: docs
weight: 1030
url: /ar/net/groupdocs.editor.options/pdfcompliance/
---
## PdfCompliance enumeration

يحدد مستوى الامتثال لمعايير PDF

```csharp
public enum PdfCompliance : byte
```

### قيم

| اسم | قيمة | وصف |
| --- | --- | --- |
| Pdf17 | `0` | PDF 1.7 (ISO 32000-1) قياسي |
| Pdf20 | `1` | PDF 2.0 (ISO 32000-2) قياسي |
| PdfA1a | `2` | معيار PDF / A-1a. يتضمن هذا المستوى جميع متطلبات PDF / A-1b ويتطلب بالإضافة إلى ذلك تضمين بنية المستند (المعروف أيضًا باسم "الموسومة") ، بهدف ضمان إمكانية البحث في محتوى المستند وإعادة توجيهه. |
| PdfA1b | `3` | PDF / A-1b (ISO 19005-1). يهدف PDF / A-1b إلى ضمان إعادة إنتاج موثوق للمظهر المرئي للمستند. |
| PdfA2a | `4` | معيار PDF / A-2a (ISO 19005-2). يتضمن هذا المستوى جميع متطلبات PDF / A-2u ويتطلب بالإضافة إلى ذلك تضمين هيكل المستند (المعروف أيضًا باسم "الموسومة") ، بهدف ضمان إمكانية البحث في محتوى المستند وإعادة توجيهه. |
| PdfA2u | `5` | معيار PDF / A-2u (ISO 19005-2). يهدف PDF / A-2u إلى الحفاظ على المظهر المرئي الثابت للوثيقة بمرور الوقت ، بغض النظر عن الأدوات والأنظمة المستخدمة لإنشاء الملفات أو تخزينها أو عرضها. بالإضافة إلى ذلك ، يمكن استخراج أي نص موجود في المستند بشكل موثوق به كسلسلة من نقاط ترميز Unicode. |
| PdfUa1 | `6` | معيار PDF / UA-1 (ISO 14289-1). الغرض الأساسي من PDF / UA هو تحديد كيفية تمثيل المستندات الإلكترونية بتنسيق PDF بطريقة تسمح بالوصول إلى الملف. |

### أنظر أيضا

* مساحة الاسم [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* المجسم [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
