---
title: IptcPackage
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取或设置与文件关联的 IPTC 元数据包
type: docs
weight: 10
url: /zh/net/groupdocs.metadata.standards.iptc/iiptc/iptcpackage/
---
## IIptc.IptcPackage property

获取或设置与文件关联的 IPTC 元数据包。

```csharp
public IptcRecordSet IptcPackage { get; set; }
```

### 适当的价值

与文件关联的 IPTC 元数据包。

### 评论

**了解更多**

* [使用 IPTC IIM 元数据](https://docs.groupdocs.com/display/metadatanet/Working+with+IPTC+IIM+metadata)

### 例子

此代码示例展示了如何从文件中删除 IPTC 元数据。

```csharp
using (Metadata metadata = new Metadata(Constants.JpegWithIptc))
{
    IIptc root = metadata.GetRootPackage() as IIptc;
    if (root != null)
    {
        root.IptcPackage = null;

        metadata.Save(Constants.OutputJpeg);
    }
}
```

### 也可以看看

* class [IptcRecordSet](../../iptcrecordset)
* interface [IIptc](../../iiptc)
* 命名空间 [GroupDocs.Metadata.Standards.Iptc](../../iiptc)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
