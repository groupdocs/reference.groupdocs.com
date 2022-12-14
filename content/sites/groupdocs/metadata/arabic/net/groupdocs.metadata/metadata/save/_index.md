---
title: Save
second_title: GroupDocs.Metadata لمرجع .NET API
description: يحفظ كل التغييرات التي تم إجراؤها في المستند الذي تم تحميله.
type: docs
weight: 110
url: /ar/net/groupdocs.metadata/metadata/save/
---
## Save() {#save}

يحفظ كل التغييرات التي تم إجراؤها في المستند الذي تم تحميله.

```csharp
public void Save()
```

### ملاحظات

**يتعلم أكثر**

* [احفظ ملف معدل إلى المصدر الأصلي](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [حفظ ملف معدل في موقع محدد](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [حفظ ملف معدل إلى دفق](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### أمثلة

يوضح هذا المثال كيفية حفظ المحتوى المعدل في المصدر الأساسي.

```csharp
using (Metadata metadata = new Metadata(Constants.OutputPpt))
{
    // تحرير أو إزالة البيانات الوصفية هنا

    // يحفظ المستند إلى المصدر الأساسي (تيار أو ملف)
    metadata.Save();
}
```

### أنظر أيضا

* class [Metadata](../../metadata)
* مساحة الاسم [GroupDocs.Metadata](../../metadata)
* المجسم [GroupDocs.Metadata](../../../)

---

## Save(Stream) {#save_1}

يحفظ محتوى المستند في تدفق .

```csharp
public void Save(Stream document)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| document | Stream | تدفق الإخراج للمستند. |

### ملاحظات

**يتعلم أكثر**

* [احفظ ملف معدل إلى المصدر الأصلي](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [حفظ ملف معدل في موقع محدد](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [حفظ ملف معدل إلى دفق](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### أمثلة

يوضح هذا المثال كيفية حفظ مستند في الدفق المحدد.

```csharp
using (MemoryStream stream = new MemoryStream())
{
    using (Metadata metadata = new Metadata(Constants.InputPng))
    {
        // تحرير أو إزالة البيانات الوصفية هنا

        metadata.Save(stream);
    }
}
```

### أنظر أيضا

* class [Metadata](../../metadata)
* مساحة الاسم [GroupDocs.Metadata](../../metadata)
* المجسم [GroupDocs.Metadata](../../../)

---

## Save(string) {#save_2}

يحفظ محتوى المستند في الملف المحدد.

```csharp
public void Save(string filePath)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| filePath | String | الاسم الكامل لملف الإخراج. |

### ملاحظات

**يتعلم أكثر**

* [احفظ ملف معدل إلى المصدر الأصلي](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+the+original+source)
* [حفظ ملف معدل في موقع محدد](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+specified+location)
* [حفظ ملف معدل إلى دفق](https://docs.groupdocs.com/display/metadatanet/Save+a+modified+file+to+a+stream)

### أمثلة

يوضح هذا المثال كيفية حفظ مستند في الموقع المحدد.

```csharp
using (Metadata metadata = new Metadata(Constants.InputJpeg))
{
    // تحرير أو إزالة البيانات الوصفية هنا

    metadata.Save(Constants.OutputJpeg);
}
```

### أنظر أيضا

* class [Metadata](../../metadata)
* مساحة الاسم [GroupDocs.Metadata](../../metadata)
* المجسم [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
