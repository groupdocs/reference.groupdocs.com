---
title: RegionReplacementOptions
second_title: GroupDocs.Redaction لمرجع .NET API
description: يمثل معلمات اللون والمساحة لاستبدال منطقة الصورة. يرىImageAreaRedaction./imagearearedaction .
type: docs
weight: 600
url: /ar/net/groupdocs.redaction.redactions/regionreplacementoptions/
---
## RegionReplacementOptions class

يمثل معلمات اللون والمساحة لاستبدال منطقة الصورة. يرى[`ImageAreaRedaction`](../imagearearedaction) .

```csharp
public class RegionReplacementOptions
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [RegionReplacementOptions](regionreplacementoptions#constructor_1)(Color, Size) | تهيئة مثيل جديد لفئة RegionReplacementOptions . |
| [RegionReplacementOptions](regionreplacementoptions#constructor)(Color, Font, string) | تهيئة مثيل جديد لفئة RegionReplacementOptions التي يتطابق الحجم مع النص المحدد. |

## الخصائص

| اسم | وصف |
| --- | --- |
| [FillColor](../../groupdocs.redaction.redactions/regionreplacementoptions/fillcolor) { get; set; } | الحصول على اللون أو تعيينه لملء المنطقة المنقحة. |
| [Size](../../groupdocs.redaction.redactions/regionreplacementoptions/size) { get; set; } | الحصول على أو تعيين المستطيل بالارتفاع. |

### ملاحظات

**يتعلم أكثر**

* مزيد من التفاصيل حول تنقيح الصورة: [تنقيح الصورة](https://docs.groupdocs.com/redaction/net/image-redactions/)

### أمثلة

يوضح المثال التالي استبدال منطقة داخل الصورة بمستطيل بلون خالص.

```csharp
    using (Redactor redactor = new Redactor("D:\\test.jpg"))
    {
       System.Drawing.Point samplePoint = new System.Drawing.Point(516, 311);
       System.Drawing.Size sampleSize = new System.Drawing.Size(170, 35);
       RedactorChangeLog result = redactor.Apply(new ImageAreaRedaction(samplePoint,
                     new RegionReplacementOptions(System.Drawing.Color.Blue, sampleSize)));
       if (result.Status != RedactionStatus.Failed)
       {
          redactor.Save();
       };
    } 
```

### أنظر أيضا

* مساحة الاسم [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* المجسم [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
