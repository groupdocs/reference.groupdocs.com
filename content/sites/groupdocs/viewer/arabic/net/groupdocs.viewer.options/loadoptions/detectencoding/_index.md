---
title: DetectEncoding
second_title: GroupDocs.Viewer لمرجع .NET API
description: يتيح هذا الخيارTXTgroupdocs.viewer/filetype/txt وTSVgroupdocs.viewer/filetype/tsv  وCSVgroupdocs.viewer/filetype/csvكشف تشفير الملفات. في حالة تعذر اكتشاف الترميز الافتراضيEncodinggroupdocs.viewer.options/loadoptions/encoding يستخدم .
type: docs
weight: 20
url: /ar/net/groupdocs.viewer.options/loadoptions/detectencoding/
---
## LoadOptions.DetectEncoding property

يتيح هذا الخيار[`TXT`](../../../groupdocs.viewer/filetype/txt) و[`TSV`](../../../groupdocs.viewer/filetype/tsv) ، و[`CSV`](../../../groupdocs.viewer/filetype/csv)كشف تشفير الملفات. في حالة تعذر اكتشاف الترميز الافتراضي[`Encoding`](../encoding) يستخدم .

```csharp
public bool DetectEncoding { get; set; }
```

### ملاحظات

**تعرف على المزيد حول عرض النص والملفات المحددة بعلامات جدولة / فاصلة**

* [عرض المستندات النصية بتنسيق HTML و PDF وملفات الصور](https://docs.groupdocs.com/viewer/net/render-text-files/)
* [اعرض جداول بيانات Excel و Apple Numbers كملفات HTML و PDF وصورة](https://docs.groupdocs.com/viewer/net/render-excel-and-apple-numbers-spreadsheets/)

### أمثلة

يوضح المثال استخدامًا نموذجيًا لهذا الخيار.

```csharp
LoadOptions loadOptions = new LoadOptions();
loadOptions.DetectEncoding = true; // تمكين اكتشاف التشفير

using (Viewer viewer = new Viewer("employees.csv", loadOptions))
{
    HtmlViewOptions viewOptions = 
        HtmlViewOptions.ForEmbeddedResources();

    viewer.View(viewOptions);
}
```

### أنظر أيضا

* class [LoadOptions](../../loadoptions)
* مساحة الاسم [GroupDocs.Viewer.Options](../../loadoptions)
* المجسم [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
