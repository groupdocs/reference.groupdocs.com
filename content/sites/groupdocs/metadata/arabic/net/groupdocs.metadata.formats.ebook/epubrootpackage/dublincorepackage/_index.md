---
title: DublinCorePackage
second_title: GroupDocs.Metadata لمرجع .NET API
description: الحصول على حزمة بيانات تعريف دبلن كور المستخرجة من الكتاب الإلكتروني.
type: docs
weight: 10
url: /ar/net/groupdocs.metadata.formats.ebook/epubrootpackage/dublincorepackage/
---
## EpubRootPackage.DublinCorePackage property

الحصول على حزمة بيانات تعريف دبلن كور المستخرجة من الكتاب الإلكتروني.

```csharp
public DublinCorePackage DublinCorePackage { get; }
```

### Property_Value

حزمة بيانات تعريف Dublin Core المستخرجة من الكتاب الإلكتروني.

### ملاحظات

**يتعلم أكثر**

* [العمل مع البيانات الوصفية في الكتب الإلكترونية EPUB](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+EPUB+E-Books)

### أمثلة

يوضح هذا المثال كيفية استخراج بيانات تعريف دبلن كور من ملف EPUB.

```csharp
using (Metadata metadata = new Metadata(Constants.InputEpub))
{
    var root = metadata.GetRootPackage<EpubRootPackage>();

    if (root.DublinCorePackage != null)
    {
        Console.WriteLine(root.DublinCorePackage.Rights);
        Console.WriteLine(root.DublinCorePackage.Publisher);
        Console.WriteLine(root.DublinCorePackage.Title);
        Console.WriteLine(root.DublinCorePackage.Creator);
        Console.WriteLine(root.DublinCorePackage.Language);
        Console.WriteLine(root.DublinCorePackage.Date);

        // ...
    }
}
```

### أنظر أيضا

* class [DublinCorePackage](../../../groupdocs.metadata.standards.dublincore/dublincorepackage)
* class [EpubRootPackage](../../epubrootpackage)
* مساحة الاسم [GroupDocs.Metadata.Formats.Ebook](../../epubrootpackage)
* المجسم [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
