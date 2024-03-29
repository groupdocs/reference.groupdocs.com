---
title: EraseMetadataRedaction
second_title: GroupDocs.Redaction لمرجع .NET API
description: يمثل تنقيح البيانات الوصفية الذي يمحو جميع البيانات الوصفية أو البيانات الوصفية التي تطابق MetadataFilters معينة من المستند.
type: docs
weight: 480
url: /ar/net/groupdocs.redaction.redactions/erasemetadataredaction/
---
## EraseMetadataRedaction class

يمثل تنقيح البيانات الوصفية الذي يمحو جميع البيانات الوصفية أو البيانات الوصفية التي تطابق MetadataFilters معينة من المستند.

```csharp
public class EraseMetadataRedaction : MetadataRedaction
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [EraseMetadataRedaction](erasemetadataredaction#constructor)() | يقوم بتهيئة مثيل جديد لفئة EraseMetadataRedaction ، مما يؤدي إلى محو كافة البيانات الوصفية. |
| [EraseMetadataRedaction](erasemetadataredaction#constructor_1)(MetadataFilters) | تهيئة مثيل جديد لفئة EraseMetadataRedaction ، ومحو البيانات الأولية ، ومطابقة مجموعة معينة من[`MetadataFilters`](../metadatafilters) . |

## الخصائص

| اسم | وصف |
| --- | --- |
| override [Description](../../groupdocs.redaction.redactions/erasemetadataredaction/description) { get; } | إرجاع سلسلة تصف التنقيح ومعلماته. |
| [Filter](../../groupdocs.redaction.redactions/metadataredaction/filter) { get; set; } | الحصول على أو تعيين عامل التصفية ، والذي يُستخدم لتحديد كل البيانات الوصفية أو بيانات تعريف محددة ، على سبيل المثال المؤلف أو الشركة. |

## طُرق

| اسم | وصف |
| --- | --- |
| override [ApplyTo](../../groupdocs.redaction.redactions/metadataredaction/applyto)(DocumentFormatInstance) | يطبق التنقيح على مثيل تنسيق معين. |

### ملاحظات

**يتعلم أكثر**

* مزيد من التفاصيل حول تطبيق التنقيحات: [أساسيات التنقيح](https://docs.groupdocs.com/redaction/net/redaction-basics/)
* مزيد من التفاصيل حول تنقيح بيانات تعريف المستند: [تنقيح البيانات الوصفية](https://docs.groupdocs.com/redaction/net/metadata-redactions/)

### أمثلة

يوضح المثال التالي كيفية محو (تعيين مساوٍ للقيم الفارغة) جميع البيانات الوصفية أو المحددة.

```csharp
using (Redactor redactor = new Redactor(@"C:\sample.docx"))
{
   // محو المؤلف والمدير والشركة
   redactor.Apply(new EraseMetadataRedaction(MetadataFilters.Author | MetadataFilters.Manager | MetadataFilters.Company));
   // محو كل البيانات الوصفية
   redactor.Apply(new EraseMetadataRedaction(MetadataFilters.All));
   redactor.Save();
}
```

### أنظر أيضا

* class [MetadataRedaction](../metadataredaction)
* مساحة الاسم [GroupDocs.Redaction.Redactions](../../groupdocs.redaction.redactions)
* المجسم [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
