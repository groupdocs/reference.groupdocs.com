---
title: DataSourceInfo
second_title: GroupDocs.Assembly للحصول على مرجع .NET API
description: إنشاء مثيل جديد لهذه الفئة بدون تحديد أية خصائص.
type: docs
weight: 10
url: /ar/net/groupdocs.assembly/datasourceinfo/datasourceinfo/
---
## DataSourceInfo() {#constructor}

إنشاء مثيل جديد لهذه الفئة بدون تحديد أية خصائص.

```csharp
public DataSourceInfo()
```

### أنظر أيضا

* class [DataSourceInfo](../../datasourceinfo)
* مساحة الاسم [GroupDocs.Assembly](../../datasourceinfo)
* المجسم [GroupDocs.Assembly](../../../)

---

## DataSourceInfo(object) {#constructor_1}

إنشاء مثيل جديد لهذه الفئة مع تحديد كائن مصدر البيانات.

```csharp
public DataSourceInfo(object dataSource)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| dataSource | Object | كائن مصدر البيانات. |

### ملاحظات

يمكن أن يكون كائن مصدر البيانات من أحد الأنواع التالية:

* [`XmlDataSource`](../../../groupdocs.assembly.data/xmldatasource)
* [`JsonDataSource`](../../../groupdocs.assembly.data/jsondatasource)
* [`CsvDataSource`](../../../groupdocs.assembly.data/csvdatasource)
* [`DocumentTableSet`](../../../groupdocs.assembly.data/documenttableset)
* [`DocumentTable`](../../../groupdocs.assembly.data/documenttable)
* DataSet
* DataTable
* DataRow
* IDataReader
* IDataRecord
* DataView
* DataRowView
* أي نوع تعسفي آخر غير ديناميكي وغير مجهول. NET type

للحصول على معلومات حول كيفية العمل مع مصادر البيانات من أنواع مختلفة في مستندات النموذج ، راجع مرجع بناء الجملة (https://docs.groupdocs.com/display/assemblynet/Template+Syntax+-+Part+1+of+2# TemplateSyntax-Part1of2-UsingDataSources) .

### أنظر أيضا

* class [DataSourceInfo](../../datasourceinfo)
* مساحة الاسم [GroupDocs.Assembly](../../datasourceinfo)
* المجسم [GroupDocs.Assembly](../../../)

---

## DataSourceInfo(object, string) {#constructor_2}

إنشاء مثيل جديد لهذه الفئة مع تحديد كائن مصدر البيانات واسمه.

```csharp
public DataSourceInfo(object dataSource, string name)
```

| معامل | يكتب | وصف |
| --- | --- | --- |
| dataSource | Object | كائن مصدر البيانات . |
| name | String | اسم كائن مصدر البيانات الذي سيتم استخدامه للوصول إلى كائن مصدر البيانات في مستند قالب. |

### ملاحظات

يمكن أن يكون كائن مصدر البيانات من أحد الأنواع التالية:

* [`XmlDataSource`](../../../groupdocs.assembly.data/xmldatasource)
* [`JsonDataSource`](../../../groupdocs.assembly.data/jsondatasource)
* [`CsvDataSource`](../../../groupdocs.assembly.data/csvdatasource)
* [`DocumentTableSet`](../../../groupdocs.assembly.data/documenttableset)
* [`DocumentTable`](../../../groupdocs.assembly.data/documenttable)
* DataSet
* DataTable
* DataRow
* IDataReader
* IDataRecord
* DataView
* DataRowView
* أي نوع تعسفي آخر غير ديناميكي وغير مجهول. NET type

للحصول على معلومات حول كيفية العمل مع مصادر البيانات من أنواع مختلفة في مستندات النموذج ، راجع مرجع بناء الجملة (https://docs.groupdocs.com/display/assemblynet/Template+Syntax+-+Part+1+of+2# TemplateSyntax-Part1of2-UsingDataSources) .

عند تحديد اسم كائن مصدر البيانات ، يمكنك الوصول إلى كائن مصدر البيانات وأعضائه في مستند قالب باستخدام الاسم.

عندما يكون اسم كائن مصدر البيانات فارغًا أو فارغًا ، لا يزال بإمكانك الوصول إلى أعضاء كائن مصدر البيانات في مستند قالب باستخدام وصول عضو كائن السياق (انظر مرجع بناء الجملة لمزيد من المعلومات) ، ولكن لا يمكنك الوصول إلى كائن مصدر البيانات نفسه.

عند المرور عدة مرات[`DataSourceInfo`](../../datasourceinfo) حالات ل[`DocumentAssembler`](../../documentassembler) ، فقط الاسم of كائن مصدر البيانات الأول يمكن أن يكون فارغًا أو فارغًا. يجب تحديد أسماء البقية وفريدة من نوعها.

### أنظر أيضا

* class [DataSourceInfo](../../datasourceinfo)
* مساحة الاسم [GroupDocs.Assembly](../../datasourceinfo)
* المجسم [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
