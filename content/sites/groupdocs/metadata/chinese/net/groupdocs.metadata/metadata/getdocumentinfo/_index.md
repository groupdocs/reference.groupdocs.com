---
title: GetDocumentInfo
second_title: GroupDocs.Metadata for .NET API 参考
description: 获取有关已加载文档的公共信息
type: docs
weight: 70
url: /zh/net/groupdocs.metadata/metadata/getdocumentinfo/
---
## Metadata.GetDocumentInfo method

获取有关已加载文档的公共信息。

```csharp
public IDocumentInfo GetDocumentInfo()
```

### 返回值

表示公共文档信息的对象。

### 评论

**了解更多**

* [获取文档信息](https://docs.groupdocs.com/display/metadatanet/Get+document+info)

### 例子

此示例演示如何从文件中提取基本格式信息。

```csharp
using (Metadata metadata = new Metadata(Constants.InputXlsx))
{
    if (metadata.FileFormat != FileFormat.Unknown)
    {
        IDocumentInfo info = metadata.GetDocumentInfo();
        Console.WriteLine("File format: {0}", info.FileType.FileFormat);
        Console.WriteLine("File extension: {0}", info.FileType.Extension);
        Console.WriteLine("MIME Type: {0}", info.FileType.MimeType);
        Console.WriteLine("Number of pages: {0}", info.PageCount);
        Console.WriteLine("Document size: {0} bytes", info.Size);
        Console.WriteLine("Is document encrypted: {0}", info.IsEncrypted);
    }
}
```

### 也可以看看

* interface [IDocumentInfo](../../../groupdocs.metadata.common/idocumentinfo)
* class [Metadata](../../metadata)
* 命名空间 [GroupDocs.Metadata](../../metadata)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
