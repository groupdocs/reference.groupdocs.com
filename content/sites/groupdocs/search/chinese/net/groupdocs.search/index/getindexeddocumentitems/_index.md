---
title: GetIndexedDocumentItems
second_title: GroupDocs.Search for .NET API 参考
description: 获取指定文档的嵌套项数组用于ZIPOSTPST等容器文档
type: docs
weight: 130
url: /zh/net/groupdocs.search/index/getindexeddocumentitems/
---
## Index.GetIndexedDocumentItems method

获取指定文档的嵌套项数组（用于ZIP、OST、PST等容器文档）。

```csharp
public DocumentInfo[] GetIndexedDocumentItems(DocumentInfo documentInfo)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| documentInfo | DocumentInfo | 文档信息。 |

### 返回值

文档项的数组。

### 例子

该示例演示了如何从索引中获取索引文档的项目列表。

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
 
// 在指定文件夹中创建索引
Index index = new Index(indexFolder);
 
// 索引指定文件夹中的文档
index.Add(documentsFolder);
 
// 获取索引文档列表
DocumentInfo[] documents = index.GetIndexedDocuments();
for (int i = 0; i < documents.Length; i++)
{
    DocumentInfo document = documents[i];
    Console.WriteLine(document.FilePath);
    DocumentInfo[] items = index.GetIndexedDocumentItems(document); // 获取文档项列表
    for (int j = 0; j < items.Length; j++)
    {
        DocumentInfo item = items[j];
        Console.WriteLine("\t" + item.InnerPath);
    }
}
```

### 也可以看看

* class [DocumentInfo](../../../groupdocs.search.results/documentinfo)
* class [Index](../../index)
* 命名空间 [GroupDocs.Search](../../index)
* 部件 [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->