---
title: TableDiscreteFunction
second_title: GroupDocs. ابحث عن مرجع .NET API
description: يقوم بتهيئة مثيل جديد لملفTableDiscreteFunctiongroupdocs.search.options/tablediscretefunction فئة .
type: docs
weight: 10
url: /ar/net/groupdocs.search.options/tablediscretefunction/tablediscretefunction/
---
## TableDiscreteFunction(int, int[]) {#constructor_1}

يقوم بتهيئة مثيل جديد لملف[`TableDiscreteFunction`](../../tablediscretefunction) فئة .

```csharp
public TableDiscreteFunction(int offsetOfInputs, int[] tableOfOutputs)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| offsetOfInputs | Int32 | إزاحة الجدول غير صحيحة بالنسبة لقيم الإدخال. |
| tableOfOutputs | Int32[] | جدول قيم المخرجات. |

### استثناءات

| استثناء | حالة |
| --- | --- |
| ArgumentNullException | عندما ألقيت*tableOfOutputs* يكون`باطل`. |
| ArgumentException | يتم طرحه عندما يكون عدد عناصر الجدول 0. |

### أنظر أيضا

* class [TableDiscreteFunction](../../tablediscretefunction)
* مساحة الاسم [GroupDocs.Search.Options](../../tablediscretefunction)
* المجسم [GroupDocs.Search](../../../)

---

## TableDiscreteFunction(int, params Step[]) {#constructor}

يقوم بتهيئة مثيل جديد لملف[`TableDiscreteFunction`](../../tablediscretefunction) فئة .

```csharp
public TableDiscreteFunction(int firstStepLevel, params Step[] steps)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| firstStepLevel | Int32 | مستوى الخطوة الأولى لوظيفة الخطوة. |
| steps | Step[] | الخطوات التالية لوظيفة الخطوة. |

### استثناءات

| استثناء | حالة |
| --- | --- |
| ArgumentNullException | عندما ألقيت*steps* يكون`باطل`. |
| ArgumentException | يتم إلقاؤها عندما لا تتزايد حدود الخطوات بشكل صارم. |

### أنظر أيضا

* class [Step](../../step)
* class [TableDiscreteFunction](../../tablediscretefunction)
* مساحة الاسم [GroupDocs.Search.Options](../../tablediscretefunction)
* المجسم [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
