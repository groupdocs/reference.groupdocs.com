---
title: FileType
second_title: GroupDocs.Metadata لمرجع .NET API
description: يحصل على حزمة البيانات الوصفية لنوع الملف.
type: docs
weight: 20
url: /ar/net/groupdocs.metadata.formats.document/pdfrootpackage/filetype/
---
## PdfRootPackage.FileType property

يحصل على حزمة البيانات الوصفية لنوع الملف.

```csharp
public PdfTypePackage FileType { get; }
```

### Property_Value

حزمة البيانات الوصفية لنوع الملف.

### أمثلة

يوضح مقتطف الشفرة هذا كيفية اكتشاف إصدار PDF وهو مستند محمل واستخراج بعض معلومات تنسيق الملف الإضافية.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPdf))
{
    var root = metadata.GetRootPackage<PdfRootPackage>();

    Console.WriteLine(root.FileType.FileFormat);
    Console.WriteLine(root.FileType.Version);
    Console.WriteLine(root.FileType.MimeType);
    Console.WriteLine(root.FileType.Extension);
}
```

### أنظر أيضا

* class [PdfTypePackage](../../pdftypepackage)
* class [PdfRootPackage](../../pdfrootpackage)
* مساحة الاسم [GroupDocs.Metadata.Formats.Document](../../pdfrootpackage)
* المجسم [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
