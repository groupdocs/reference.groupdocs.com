---
title: Add
second_title: GroupDocs.Assembly للحصول على مرجع .NET API
description: يضيف المحددType تعترض على المجموعة.
type: docs
weight: 20
url: /ar/net/groupdocs.assembly/knowntypeset/add/
---
## KnownTypeSet.Add method

يضيف المحددType تعترض على المجموعة.

رمياتArgumentException في الحالات التالية:

-*type* باطل.

-*type* يمثل نوع الفراغ.

-*type* يمثل نوعًا غير مرئي ، أي نوع غير عام أو نوع متداخل عام له نوع خارجي غير عام.

-*type* يمثل نوعًا عامًا.

-*type* يمثل نوع المصفوفة.

-*type* تمت إضافته إلى المجموعة بالفعل.

```csharp
public void Add(Type type)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| type | Type | أType كائن للإضافة. |

### أنظر أيضا

* class [KnownTypeSet](../../knowntypeset)
* مساحة الاسم [GroupDocs.Assembly](../../knowntypeset)
* المجسم [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
