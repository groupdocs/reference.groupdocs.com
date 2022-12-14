---
title: ToDataSetList
second_title: GroupDocs.Metadata لمرجع .NET API
description: إنشاء قائمة بمجموعات البيانات من الحزمة.
type: docs
weight: 90
url: /ar/net/groupdocs.metadata.standards.iptc/iptcrecordset/todatasetlist/
---
## IptcRecordSet.ToDataSetList method

إنشاء قائمة بمجموعات البيانات من الحزمة.

```csharp
public IReadOnlyList<IptcDataSet> ToDataSetList()
```

### قيمة الإرجاع

قائمة تحتوي على جميع مجموعات بيانات IPTC من الحزمة.

### أمثلة

يوضح هذا المثال كيفية قراءة كافة مجموعات بيانات IPTC IIM من حزمة بيانات تعريف IPTC.

```csharp
using (Metadata metadata = new Metadata(Constants.PsdWithIptc))
{
    IIptc root = metadata.GetRootPackage() as IIptc;
    if (root != null && root.IptcPackage != null)
    {
        foreach (var dataSet in root.IptcPackage.ToDataSetList())
        {
            Console.WriteLine(dataSet.RecordNumber);
            Console.WriteLine(dataSet.DataSetNumber);
            Console.WriteLine(dataSet.AlternativeName);
            Console.WriteLine(dataSet.Value);
        }
    }
}
```

### أنظر أيضا

* interface [IReadOnlyList&lt;T&gt;](../../../groupdocs.metadata.common/ireadonlylist-1)
* class [IptcDataSet](../../iptcdataset)
* class [IptcRecordSet](../../iptcrecordset)
* مساحة الاسم [GroupDocs.Metadata.Standards.Iptc](../../iptcrecordset)
* المجسم [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
