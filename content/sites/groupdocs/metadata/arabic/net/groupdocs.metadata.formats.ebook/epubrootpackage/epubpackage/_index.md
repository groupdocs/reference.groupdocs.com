---
title: EpubPackage
second_title: GroupDocs.Metadata لمرجع .NET API
description: يحصل على حزمة البيانات الوصفية EPUB .
type: docs
weight: 20
url: /ar/net/groupdocs.metadata.formats.ebook/epubrootpackage/epubpackage/
---
## EpubRootPackage.EpubPackage property

يحصل على حزمة البيانات الوصفية EPUB .

```csharp
public EpubPackage EpubPackage { get; }
```

### Property_Value

حزمة البيانات الوصفية EPUB.

### ملاحظات

**يتعلم أكثر**

* [العمل مع البيانات الوصفية في الكتب الإلكترونية EPUB](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+EPUB+E-Books)

### أمثلة

يوضح نموذج التعليمات البرمجية هذا كيفية قراءة خصائص البيانات الوصفية الخاصة بتنسيق EPUB.

```csharp
using (Metadata metadata = new Metadata(Constants.InputEpub))
{
    var root = metadata.GetRootPackage<EpubRootPackage>();

    Console.WriteLine(root.EpubPackage.Version);
    Console.WriteLine(root.EpubPackage.UniqueIdentifier);
    Console.WriteLine(root.EpubPackage.ImageCover != null ? root.EpubPackage.ImageCover.Length : 0);
}
```

### أنظر أيضا

* class [EpubPackage](../../epubpackage)
* class [EpubRootPackage](../../epubrootpackage)
* مساحة الاسم [GroupDocs.Metadata.Formats.Ebook](../../epubrootpackage)
* المجسم [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
