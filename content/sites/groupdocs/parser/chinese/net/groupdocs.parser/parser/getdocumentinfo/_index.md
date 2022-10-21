---
title: GetDocumentInfo
second_title: GroupDocs.Parser for .NET API 参考
description: 返回有关文档的一般信息
type: docs
weight: 70
url: /zh/net/groupdocs.parser/parser/getdocumentinfo/
---
## Parser.GetDocumentInfo method

返回有关文档的一般信息。

```csharp
public IDocumentInfo GetDocumentInfo()
```

### 返回值

实现的类的实例[`IDocumentInfo`](../../../groupdocs.parser.options/idocumentinfo)界面。

### 评论

**学到更多：**

* [获取文档信息](https://docs.groupdocs.com/display/parsernet/Get+document+info)
* [检测编码](https://docs.groupdocs.com/display/parsernet/Detect+encoding)

### 例子

以下示例显示了如何获取文档信息：

```csharp
// 创建 Parser 类的实例
using(Parser parser = new Parser(filePath))
{
    // 获取文档信息
    IDocumentInfo info = parser.GetDocumentInfo();

    Console.WriteLine(string.Format("FileType: {0}", info.FileType));
    Console.WriteLine(string.Format("PageCount: {0}", info.PageCount));
    Console.WriteLine(string.Format("Size: {0}", info.Size));
}
```

### 也可以看看

* interface [IDocumentInfo](../../../groupdocs.parser.options/idocumentinfo)
* class [Parser](../../parser)
* 命名空间 [GroupDocs.Parser](../../parser)
* 部件 [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->