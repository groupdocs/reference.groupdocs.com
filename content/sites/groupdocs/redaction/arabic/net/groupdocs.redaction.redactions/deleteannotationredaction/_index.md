---
title: DeleteAnnotationRedaction
second_title: GroupDocs.Redaction لمرجع .NET API
description: يمثل تنقيح النص الذي يحذف التعليقات التوضيحية إذا كان النص مطابقًا للتعبير العادي المعطى اختياريًا يحذف جميع التعليقات التوضيحية .
type: docs
weight: 470
url: /ar/net/groupdocs.redaction.redactions/deleteannotationredaction/
---
## DeleteAnnotationRedaction class

يمثل تنقيح النص الذي يحذف التعليقات التوضيحية إذا كان النص مطابقًا للتعبير العادي المعطى (اختياريًا يحذف جميع التعليقات التوضيحية) .

```csharp
public class DeleteAnnotationRedaction : Redaction
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [DeleteAnnotationRedaction](deleteannotationredaction#constructor)() | تهيئة مثيل جديد لفئة DeleteAnnotationRedaction ، مع إعدادات لحذف جميع التعليقات التوضيحية (تطابق كل شيء) . |
| [DeleteAnnotationRedaction](deleteannotationredaction#constructor_2)(Regex) | يقوم بتهيئة مثيل جديد لفئة DeleteAnnotationRedaction وحذف التعليقات التوضيحية التي تطابق التعبير المحدد. |
| [DeleteAnnotationRedaction](deleteannotationredaction#constructor_1)(string) | يقوم بتهيئة مثيل جديد لفئة DeleteAnnotationRedaction وحذف التعليقات التوضيحية التي تطابق التعبير المحدد. |

## الخصائص

| اسم | وصف |
| --- | --- |
| override [Description](../../groupdocs.redaction.redactions/deleteannotationredaction/description) { get; } | إرجاع سلسلة تصف التنقيح ومعلماته. |
| [Expression](../../groupdocs.redaction.redactions/deleteannotationredaction/expression) { get; } | الحصول على التعبير العادي للمطابقة . |

## طُرق

| اسم | وصف |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/deleteannotationredaction/applyto)(DocumentFormatInstance) | يطبق التنقيح على مثيل تنسيق معين. |

### ملاحظات

**يتعلم أكثر**

* مزيد من التفاصيل حول تطبيق التنقيحات: [أساسيات التنقيح](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* مزيد من التفاصيل حول تنقيح التعليقات التوضيحية على المستند: [تنقيح التعليقات التوضيحية](https://docs.groupdocs.com/redaction/net/annotation-redactions/)

### أمثلة

يوضح المثال التالي كيفية إزالة جميع التعليقات التوضيحية التي تحتوي على كلمات "استخدم" أو "عرض" أو "وصف" من المستند (واترك الآخرين) .

```csharp
using (Redactor redactor = new Redactor(@"D:\test.docx"))
{
   redactor.Apply(new DeleteAnnotationRedaction("(?im:(use|show|describe))"));
   redactor.Save()
}
```

### أنظر أيضا

* class [Redaction](../../groupdocs.redaction/redaction)
* مساحة الاسم [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* المجسم [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
