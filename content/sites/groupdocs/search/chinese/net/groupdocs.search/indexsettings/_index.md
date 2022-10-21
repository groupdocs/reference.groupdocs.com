---
title: IndexSettings
second_title: GroupDocs.Search for .NET API 参考
description: 表示允许自定义索引操作的索引设置
type: docs
weight: 670
url: /zh/net/groupdocs.search/indexsettings/
---
## IndexSettings class

表示允许自定义索引操作的索引设置。

```csharp
public class IndexSettings
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [IndexSettings](indexsettings)() | 初始化[`IndexSettings`](../indexsettings)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [AutoDetectEncoding](../../groupdocs.search/indexsettings/autodetectencoding) { get; set; } | 获取或设置是否自动检测编码的值。 默认值为`错误的`. |
| [CustomExtractors](../../groupdocs.search/indexsettings/customextractors) { get; } | 获取自定义提取器集合。 |
| [DocumentFilter](../../groupdocs.search/indexsettings/documentfilter) { get; set; } | 获取或设置文档过滤器。 [`DocumentFilter`](./documentfilter)适用于包含逻辑。 使用[`DocumentFilter`](../../groupdocs.search.options/documentfilter)用于创建文档过滤器实例的类。 默认值为`无效的`，这意味着所有添加的文档都被索引。 |
| [IndexType](../../groupdocs.search/indexsettings/indextype) { get; set; } | 获取或设置索引类型。 默认值为NormalIndex. |
| [InMemoryIndex](../../groupdocs.search/indexsettings/inmemoryindex) { get; } | 获取一个值，指示索引是存储在内存中还是磁盘上。 |
| [Logger](../../groupdocs.search/indexsettings/logger) { get; set; } | 获取或设置一个记录器，用于记录索引中的事件和错误。 注意记录器不保存，必须在每次创建或加载索引时创建和分配。 |
| [MaxIndexingReportCount](../../groupdocs.search/indexsettings/maxindexingreportcount) { get; set; } | 获取或设置索引报告的最大数量。 默认值为`5`. |
| [MaxSearchReportCount](../../groupdocs.search/indexsettings/maxsearchreportcount) { get; set; } | 获取或设置搜索报告的最大数量。 默认值为`10`. |
| [SearchThreads](../../groupdocs.search/indexsettings/searchthreads) { get; set; } | 获取或设置用于搜索的线程数。 默认值为Default, 这意味着将使用等于处理器内核数的线程数执行搜索。 |
| [TextStorageSettings](../../groupdocs.search/indexsettings/textstoragesettings) { get; set; } | 获取或设置文本存储设置。 默认值为`无效的`，这意味着不存储文档文本。 |
| [UseCharacterReplacements](../../groupdocs.search/indexsettings/usecharacterreplacements) { get; set; } | 获取或设置是否使用字符替换的值。 默认值为`错误的`. |
| [UseRawTextExtraction](../../groupdocs.search/indexsettings/userawtextextraction) { get; set; } | 获取或设置一个值，如果可能，是否使用原始模式进行文本提取。 默认值为`真的`. 原始模式可以显着提高索引速度，但普通模式改进了提取文本的格式。 |
| [UseStopWords](../../groupdocs.search/indexsettings/usestopwords) { get; set; } | 获取或设置是否使用停用词的值。 默认值为`真的`. |

### 评论

**学到更多**

* [搜索索引设置](https://docs.groupdocs.com/display/searchnet/Search+index+settings)

### 例子

该示例演示了类的典型用法。

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex; // 设置索引类型

Index index = new Index(indexFolder, settings); // 创建索引
```

### 也可以看看

* 命名空间 [GroupDocs.Search](../../groupdocs.search)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->