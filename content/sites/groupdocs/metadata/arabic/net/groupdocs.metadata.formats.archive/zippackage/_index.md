---
title: ZipPackage
second_title: GroupDocs.Metadata لمرجع .NET API
description: يمثل بيانات تعريف أرشيف ZIP .
type: docs
weight: 360
url: /ar/net/groupdocs.metadata.formats.archive/zippackage/
---
## ZipPackage class

يمثل بيانات تعريف أرشيف ZIP .

```csharp
public sealed class ZipPackage : CustomPackage
```

## الخصائص

| اسم | وصف |
| --- | --- |
| [Comment](../../groupdocs.metadata.formats.archive/zippackage/comment) { get; set; } | الحصول على أو تعيين تعليق أرشيف ZIP الذي تم إنشاؤه بواسطة المستخدم. |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | الحصول على عدد خصائص البيانات الوصفية. |
| [Files](../../groupdocs.metadata.formats.archive/zippackage/files) { get; } | يحصل على مجموعة من[`ZipFile`](../zipfile) إدخالات داخل أرشيف ZIP. |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | يحصل على ملف[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty) بالاسم المحدد. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | الحصول على مجموعة من أسماء خصائص البيانات الوصفية. |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | الحصول على نوع البيانات الوصفية . |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | يحصل على مجموعة من الواصفات التي تحتوي على معلومات حول الخصائص التي يمكن الوصول إليها من خلال GroupDocs.Metadata search engine . |
| [TotalEntries](../../groupdocs.metadata.formats.archive/zippackage/totalentries) { get; } | الحصول على العدد الإجمالي للإدخالات داخل أرشيف ZIP . |

## طُرق

| اسم | وصف |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | يضيف خصائص البيانات الوصفية المعروفة التي تفي بالمسند المحدد . العملية متكررة لذا فهي تؤثر على جميع الحزم المتداخلة أيضًا. |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | لتحديد ما إذا كانت الحزمة تحتوي على خاصية بيانات التعريف بالاسم المحدد. |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | البحث عن خصائص البيانات الوصفية التي تفي بالمسند المحدد. البحث متكرر لذا فهو يؤثر على جميع الحزم المتداخلة أيضًا. |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | إرجاع عداد يتكرر خلال المجموعة. |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | يزيل خصائص البيانات الوصفية التي تفي بالتقييم المحدد. |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | إزالة خصائص البيانات الوصفية القابلة للكتابة من الحزمة. العملية متكررة لذا فهي تؤثر على جميع الحزم المتداخلة أيضًا. |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | تعيين خصائص البيانات الوصفية المعروفة التي تفي بالمسند المحدد . العملية متكررة لذا فهي تؤثر على جميع الحزم المتداخلة أيضًا.[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties) و[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) إذا كانت خاصية موجودة تحقق القيمة الأصلية ، فسيتم تحديث قيمتها. إذا كانت هناك خاصية معروفة مفقودة في الحزمة التي ترضي المسند ، فستتم إضافتها إلى الحزمة. |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | يقوم بتحديث خصائص البيانات الوصفية المعروفة التي تفي بالمسند المحدد . العملية متكررة لذا فهي تؤثر على جميع الحزم المتداخلة أيضًا. |

### ملاحظات

**يتعلم أكثر**

* [العمل مع أرشيفات ZIP](https://docs.groupdocs.com/display/metadatanet/Working+with+ZIP+archives)

### أمثلة

يوضح مقتطف الشفرة التالي كيفية الحصول على البيانات الوصفية من أرشيف ZIP.

```csharp
Encoding encoding = Encoding.GetEncoding(866);

using (Metadata metadata = new Metadata(Constants.InputZip))
{
    var root = metadata.GetRootPackage<ZipRootPackage>();

    Console.WriteLine(root.ZipPackage.Comment);
    Console.WriteLine(root.ZipPackage.TotalEntries);

    foreach (var file in root.ZipPackage.Files)
    {
        Console.WriteLine(file.Name);
        Console.WriteLine(file.CompressedSize);
        Console.WriteLine(file.CompressionMethod);
        Console.WriteLine(file.Flags);
        Console.WriteLine(file.ModificationDateTime);
        Console.WriteLine(file.UncompressedSize);

        // استخدم ترميزًا محددًا لأسماء الملفات
        Console.WriteLine(encoding.GetString(file.RawName));
    }
}
```

### أنظر أيضا

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* مساحة الاسم [GroupDocs.Metadata.Formats.Archive](../../groupdocs.metadata.formats.archive)
* المجسم [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
