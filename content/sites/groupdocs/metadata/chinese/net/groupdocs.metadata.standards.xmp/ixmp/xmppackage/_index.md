---
title: XmpPackage
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取或设置 XMP 元数据包
type: docs
weight: 10
url: /zh/net/groupdocs.metadata.standards.xmp/ixmp/xmppackage/
---
## IXmp.XmpPackage property

获取或设置 XMP 元数据包。

```csharp
public XmpPacketWrapper XmpPackage { get; set; }
```

### 适当的价值

XMP 元数据包。

### 评论

**了解更多**

* [使用 XMP 元数据](https://docs.groupdocs.com/display/metadatanet/Working+with+XMP+metadata)

### 例子

此代码示例展示了如何从文件中删除 XMP 元数据。

```csharp
using (Metadata metadata = new Metadata(Constants.JpegWithXmp))
{
    IXmp root = metadata.GetRootPackage() as IXmp;
    if (root != null)
    {
        root.XmpPackage = null;
        metadata.Save(Constants.OutputJpeg);
    }
}
```

### 也可以看看

* class [XmpPacketWrapper](../../xmppacketwrapper)
* interface [IXmp](../../ixmp)
* 命名空间 [GroupDocs.Metadata.Standards.Xmp](../../ixmp)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
