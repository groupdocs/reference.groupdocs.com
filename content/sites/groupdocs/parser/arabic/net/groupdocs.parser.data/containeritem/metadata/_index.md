---
title: Metadata
second_title: GroupDocs.Parser لمرجع .NET API
description: الحصول على مجموعة عناصر البيانات الوصفية.
type: docs
weight: 30
url: /ar/net/groupdocs.parser.data/containeritem/metadata/
---
## ContainerItem.Metadata property

الحصول على مجموعة عناصر البيانات الوصفية.

```csharp
public IEnumerable<MetadataItem> Metadata { get; }
```

### Property_Value

مجموعة من[`MetadataItem`](../../metadataitem) أشياء؛ فارغة إذا لم يتم تعيين البيانات الوصفية.

### ملاحظات

تشير هذه البيانات الوصفية إلى عنصر الحاوية نفسه ، وليس إلى مستند. اعتمادًا على نوع الحاوية ، يمكن أن تحتوي البيانات الوصفية على العناصر التالية:

**مرفقات البريد الإلكتروني**

**اسم**

**وصف**

**نوع المحتوى**

نوع MIME لمحتوى المرفق.

**أرشيفات ZIP**

**اسم**

**وصف**

**تاريخ**

وقت وتاريخ آخر تعديل للملف المشار إليه بواسطة Zip Entry.

**تخزين Outlook**

**اسم**

**وصف**

**تاريخ**

وقت وتاريخ آخر تعديل لعنصر تخزين Outlook.

**مرسل البريد الإلكتروني**

قيمة حقل "المرسل".

**بريد إلكتروني إلى**

قيمة الحقل "إلى".

**موضوع**

قيمة حقل "الموضوع".

### أنظر أيضا

* class [MetadataItem](../../metadataitem)
* class [ContainerItem](../../containeritem)
* مساحة الاسم [GroupDocs.Parser.Data](../../containeritem)
* المجسم [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
