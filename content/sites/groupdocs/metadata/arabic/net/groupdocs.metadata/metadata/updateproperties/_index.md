---
title: UpdateProperties
second_title: GroupDocs.Metadata لمرجع .NET API
description: يقوم بتحديث خصائص البيانات الوصفية المعروفة التي تفي بالمسند المحدد . العملية متكررة لذا فهي تؤثر على جميع الحزم المتداخلة أيضًا.
type: docs
weight: 130
url: /ar/net/groupdocs.metadata/metadata/updateproperties/
---
## Metadata.UpdateProperties method

يقوم بتحديث خصائص البيانات الوصفية المعروفة التي تفي بالمسند المحدد . العملية متكررة لذا فهي تؤثر على جميع الحزم المتداخلة أيضًا.

```csharp
public int UpdateProperties(Func<MetadataProperty, bool> predicate, PropertyValue value)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| predicate | Func`2 | وظيفة لاختبار كل خاصية من خصائص البيانات الوصفية لشرط ما. |
| value | PropertyValue | قيمة جديدة للخصائص التي تمت تصفيتها. |

### قيمة الإرجاع

عدد الخصائص المتأثرة.

### ملاحظات

يرجى ملاحظة أن GroupDocs.Metadata يتحقق ضمنيًا من نوع كل خاصية تمت تصفيتها. من المستحيل تحديث خاصية ذات قيمة ذات نوع غير مناسب .

**يتعلم أكثر**

* مزيد من الأمثلة التي توضح استخدامات هذه الطريقة: [تحديث البيانات الوصفية](https://docs.groupdocs.com/display/metadatanet/Updating+metadata)

### أمثلة

```csharp
using (Metadata metadata = new Metadata(Constants.InputXlsx))
{
    if (metadata.FileFormat != FileFormat.Unknown && !metadata.GetDocumentInfo().IsEncrypted)
    {
        // قم بتحديث تاريخ / وقت إنشاء الملف إذا كانت القيمة الحالية أقدم من 3 أيام
        var affected = metadata.UpdateProperties(p => p.Tags.Contains(Tags.Time.Created) &&
                p.Value.Type == MetadataPropertyType.DateTime &&
                p.Value.ToStruct<DateTime>() < threeDaysAgo, new PropertyValue(today));

        Console.WriteLine("Affected properties: {0}", affected);

        metadata.Save(Constants.OutputXlsx);
    }
}
```

### أنظر أيضا

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [PropertyValue](../../../groupdocs.metadata.common/propertyvalue)
* class [Metadata](../../metadata)
* مساحة الاسم [GroupDocs.Metadata](../../metadata)
* المجسم [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
