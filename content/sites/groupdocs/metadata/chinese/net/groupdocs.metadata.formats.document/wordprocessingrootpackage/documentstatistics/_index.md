---
title: DocumentStatistics
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取文档统计包
type: docs
weight: 10
url: /zh/net/groupdocs.metadata.formats.document/wordprocessingrootpackage/documentstatistics/
---
## WordProcessingRootPackage.DocumentStatistics property

获取文档统计包。

```csharp
public DocumentStatistics DocumentStatistics { get; }
```

### 适当的价值

文档统计包。

### 评论

**学到更多**

* [在文字处理文档中使用元数据](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+WordProcessing+documents)

### 例子

此代码示例展示了如何获取 WordProcessing 文档的简单文本统计信息。

```csharp
using (Metadata metadata = new Metadata(Constants.InputDocx))
{
    var root = metadata.GetRootPackage<WordProcessingRootPackage>();

    Console.WriteLine(root.DocumentStatistics.CharacterCount);
    Console.WriteLine(root.DocumentStatistics.PageCount);
    Console.WriteLine(root.DocumentStatistics.WordCount);
}
```

### 也可以看看

* class [DocumentStatistics](../../documentstatistics)
* class [WordProcessingRootPackage](../../wordprocessingrootpackage)
* 命名空间 [GroupDocs.Metadata.Formats.Document](../../wordprocessingrootpackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->