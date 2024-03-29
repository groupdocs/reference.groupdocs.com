---
title: ImageSearchOptions
second_title: GroupDocs.Search for .NET API 参考
description: 提供反向图像搜索操作的选项
type: docs
weight: 910
url: /zh/net/groupdocs.search.options/imagesearchoptions/
---
## ImageSearchOptions class

提供反向图像搜索操作的选项。

```csharp
public class ImageSearchOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [ImageSearchOptions](imagesearchoptions)() | 初始化一个新的实例[`ImageSearchOptions`](../imagesearchoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [HashDifferences](../../groupdocs.search.options/imagesearchoptions/hashdifferences) { get; set; } | 获取或设置图像哈希中的最大不匹配位数。 默认值为`5个`. |
| [MaxResultCount](../../groupdocs.search.options/imagesearchoptions/maxresultcount) { get; set; } | 获取或设置图片反向搜索请求的最大找到图片数。 默认值为`1000`. |
| [SearchDocumentFilter](../../groupdocs.search.options/imagesearchoptions/searchdocumentfilter) { get; set; } | 获取或设置搜索文档过滤器。 [`SearchDocumentFilter`](./searchdocumentfilter)处理包含逻辑。 使用[`SearchDocumentFilter`](../searchdocumentfilter)用于创建搜索文档过滤器实例的类。 默认值为`无效的`，这意味着将返回所有找到的文档。 |

### 也可以看看

* 命名空间 [GroupDocs.Search.Options](../../groupdocs.search.options)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
