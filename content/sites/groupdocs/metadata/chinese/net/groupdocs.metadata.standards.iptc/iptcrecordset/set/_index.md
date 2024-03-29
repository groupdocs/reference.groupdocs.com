---
title: Set
second_title: GroupDocs.Metadata for .NET API 参考
description: 在适当的记录中添加或更新指定的数据集
type: docs
weight: 80
url: /zh/net/groupdocs.metadata.standards.iptc/iptcrecordset/set/
---
## IptcRecordSet.Set method

在适当的记录中添加或更新指定的数据集。

```csharp
public void Set(IptcDataSet dataSet)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| dataSet | IptcDataSet | 要添加/更新的 IPTC 数据集。 |

### 例子

此示例说明如何在文件中添加或更新自定义 IPTC 数据集。

```csharp
using (Metadata metadata = new Metadata(Constants.PsdWithIptc))
{
    IIptc root = metadata.GetRootPackage() as IIptc;
    if (root != null)
    {
        // 如果缺少 IPTC 包，则设置它
        if (root.IptcPackage == null)
        {
            root.IptcPackage = new IptcRecordSet();
        }

        // 使用 DataSet API 添加一个已知属性
        root.IptcPackage.Set(new IptcDataSet((byte) IptcRecordType.ApplicationRecord, (byte) IptcApplicationRecordDataSet.BylineTitle, "test code sample"));

        // 添加自定义 IPTC 数据集
        root.IptcPackage.Set(new IptcDataSet(255, 255, new byte[] { 1, 2, 3 }));

        metadata.Save(Constants.OutputPsd);
    }
}
```

### 也可以看看

* class [IptcDataSet](../../iptcdataset)
* class [IptcRecordSet](../../iptcrecordset)
* 命名空间 [GroupDocs.Metadata.Standards.Iptc](../../iptcrecordset)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
