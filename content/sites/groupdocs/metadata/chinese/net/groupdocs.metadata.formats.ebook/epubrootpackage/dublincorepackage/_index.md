---
title: DublinCorePackage
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取从电子书中提取的 Dublin Core 元数据包
type: docs
weight: 10
url: /zh/net/groupdocs.metadata.formats.ebook/epubrootpackage/dublincorepackage/
---
## EpubRootPackage.DublinCorePackage property

获取从电子书中提取的 Dublin Core 元数据包。

```csharp
public DublinCorePackage DublinCorePackage { get; }
```

### 适当的价值

从电子书中提取的都柏林核心元数据包。

### 评论

**学到更多**

* [在 EPUB 电子书中处理元数据](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+EPUB+E-Books)

### 例子

此示例说明如何从 EPUB 文件中提取都柏林核心元数据。

```csharp
using (Metadata metadata = new Metadata(Constants.InputEpub))
{
    var root = metadata.GetRootPackage<EpubRootPackage>();

    if (root.DublinCorePackage != null)
    {
        Console.WriteLine(root.DublinCorePackage.Rights);
        Console.WriteLine(root.DublinCorePackage.Publisher);
        Console.WriteLine(root.DublinCorePackage.Title);
        Console.WriteLine(root.DublinCorePackage.Creator);
        Console.WriteLine(root.DublinCorePackage.Language);
        Console.WriteLine(root.DublinCorePackage.Date);

        // ...
    }
}
```

### 也可以看看

* class [DublinCorePackage](../../../groupdocs.metadata.standards.dublincore/dublincorepackage)
* class [EpubRootPackage](../../epubrootpackage)
* 命名空间 [GroupDocs.Metadata.Formats.Ebook](../../epubrootpackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->