---
title: PdfSearchableObjects
second_title: GroupDocs.Watermark لـ .NET API Reference
description: يحدد العلامات التي تمثل كائنات محتوى pdf التي سيتم تضمينها في بحث العلامة المائية.
type: docs
weight: 2490
url: /ar/net/groupdocs.watermark.search.objects/pdfsearchableobjects/
---
## PdfSearchableObjects enumeration

يحدد العلامات التي تمثل كائنات محتوى pdf التي سيتم تضمينها في بحث العلامة المائية.

```csharp
[Flags]
public enum PdfSearchableObjects
```

### قيم

| اسم | قيمة | وصف |
| --- | --- | --- |
| None | `0` | لا يحدد أي كائنات بحث . |
| XObjects | `1` | بحث في XObjects. |
| Artifacts | `2` | بحث في القطع الأثرية. |
| Annotations | `4` | بحث في التعليقات التوضيحية . |
| Text | `8` | بحث في نص المحتوى . |
| Hyperlinks | `10` | بحث في الارتباطات التشعبية. |
| AttachedImages | `20` | بحث في الصور المرفقة. |
| All | `3F` | بحث في كل كائنات المحتوى . |

### أنظر أيضا

* مساحة الاسم [GroupDocs.Watermark.Search.Objects](../../groupdocs.watermark.search.objects)
* المجسم [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
