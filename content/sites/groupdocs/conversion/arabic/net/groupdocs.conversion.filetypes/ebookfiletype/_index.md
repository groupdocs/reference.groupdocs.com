---
title: EBookFileType
second_title: GroupDocs.Conversion لمرجع .NET API
description: يحدد وثائق الكتاب الإلكتروني. يتضمن أنواع الملفات التالية Epub./ebookfiletype/epubMobi./ebookfiletype/mobiAzw3./ebookfiletype/azw3
type: docs
weight: 910
url: /ar/net/groupdocs.conversion.filetypes/ebookfiletype/
---
## EBookFileType class

يحدد وثائق الكتاب الإلكتروني. يتضمن أنواع الملفات التالية: [`Epub`](./epub)[`Mobi`](./mobi)[`Azw3`](./azw3)

```csharp
public sealed class EBookFileType : FileType
```

## المنشئون

| اسم | وصف |
| --- | --- |
| [EBookFileType](ebookfiletype)() | مُنشئ التسلسل |

## الخصائص

| اسم | وصف |
| --- | --- |
| [Description](../../groupdocs.conversion.filetypes/filetype/description) { get; } | نوع الملف description |
| [Extension](../../groupdocs.conversion.filetypes/filetype/extension) { get; } | امتداد الملف |
| [Family](../../groupdocs.conversion.filetypes/filetype/family) { get; } | الملف family |
| [FileFormat](../../groupdocs.conversion.filetypes/filetype/fileformat) { get; } | تنسيق الملف |

## طُرق

| اسم | وصف |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | مقارنة الكائن الحالي بآخر . |
| override [Equals](../../groupdocs.conversion.filetypes/filetype/equals)(Enumeration) | تحديد ما إذا كان مثيلا الكائن متساويان. |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | تحديد ما إذا كان مثيلا الكائن متساويان. |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | تعمل كوظيفة تجزئة افتراضية . |
| override [ToString](../../groupdocs.conversion.filetypes/filetype/tostring)() | تمثيل السلسلة |

## مجالات

| اسم | وصف |
| --- | --- |
| static readonly [Azw3](../../groupdocs.conversion.filetypes/ebookfiletype/azw3) | AZW3 ، المعروف أيضًا باسم Kindle Format 8 (KF8) ، هو النسخة المعدلة من تنسيق الملفات الرقمية AZW للكتب الإلكترونية المطورة لأجهزة Amazon Kindle. يعد التنسيق تحسينًا لملفات AZW الأقدم ويتم استخدامه على أجهزة Kindle Fire فقط مع التوافق مع الإصدارات السابقة لتنسيق ملف السلف مثل MOBI و AZW . تعرف على المزيد حول تنسيق الملف هذا[هنا](https://docs.fileformat.com/ebook/azw3/) . |
| static readonly [Epub](../../groupdocs.conversion.filetypes/ebookfiletype/epub) | امتداد EPUB هو تنسيق ملف كتاب إلكتروني يوفر تنسيقًا قياسيًا للنشر الرقمي للناشرين والمستهلكين. أصبح التنسيق شائعًا جدًا حتى الآن لدرجة أنه مدعوم من قبل العديد من برامج القراءة الإلكترونية وتطبيقات البرامج . تعرف على المزيد حول تنسيق الملف هذا[هنا](https://wiki.fileformat.com/ebook/epub) . |
| static readonly [Mobi](../../groupdocs.conversion.filetypes/ebookfiletype/mobi) | يعد تنسيق ملف MOBI أحد أكثر تنسيقات ملفات الكتب الإلكترونية استخدامًا. يعد التنسيق تحسينًا للتنسيق القديم OEB (تنسيق Open Ebook) وقد تم استخدامه كتنسيق خاص لـ Mobipocket Reader . تعرف على المزيد حول تنسيق الملف هذا[هنا](https://wiki.fileformat.com/ebook/mobi) . |

### أنظر أيضا

* class [FileType](../filetype)
* مساحة الاسم [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* المجسم [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
