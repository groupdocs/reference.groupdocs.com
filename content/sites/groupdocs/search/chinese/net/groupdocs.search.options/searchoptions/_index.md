---
title: SearchOptions
second_title: GroupDocs.Search for .NET API 参考
description: 提供搜索操作的选项
type: docs
weight: 1000
url: /zh/net/groupdocs.search.options/searchoptions/
---
## SearchOptions class

提供搜索操作的选项。

```csharp
public class SearchOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [SearchOptions](searchoptions)() | 初始化[`SearchOptions`](../searchoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Cancellation](../../groupdocs.search.options/searchoptions/cancellation) { get; set; } | 获取或设置操作取消对象。 默认值为`无效的`. |
| [DateFormats](../../groupdocs.search.options/searchoptions/dateformats) { get; } | 获取日期范围搜索的日期格式集合。 默认日期格式为“dd.MM.yyyy”、“MM/dd/yyyy”和“yyyy-MM-dd”。 |
| [FuzzySearch](../../groupdocs.search.options/searchoptions/fuzzysearch) { get; } | 获取模糊搜索选项。 |
| [IsChunkSearch](../../groupdocs.search.options/searchoptions/ischunksearch) { get; set; } | 获取或设置分块搜索的标志。 默认值为`错误的`. |
| [KeyboardLayoutCorrector](../../groupdocs.search.options/searchoptions/keyboardlayoutcorrector) { get; } | 获取键盘布局校正器选项。 |
| [MaxOccurrenceCountPerTerm](../../groupdocs.search.options/searchoptions/maxoccurrencecountperterm) { get; set; } | 获取或设置搜索查询中每个词的最大出现次数。 默认值为`100000`. |
| [MaxTotalOccurrenceCount](../../groupdocs.search.options/searchoptions/maxtotaloccurrencecount) { get; set; } | 获取或设置搜索查询中所有词条出现的最大总次数。 默认值为`500000`. |
| [SearchDocumentFilter](../../groupdocs.search.options/searchoptions/searchdocumentfilter) { get; set; } | 获取或设置搜索文档过滤器。 [`SearchDocumentFilter`](./searchdocumentfilter)适用于包含逻辑。 使用[`SearchDocumentFilter`](../searchdocumentfilter)用于创建搜索文档过滤器实例的类。 默认值为`无效的`，这意味着将返回所有找到的文档。 |
| [SpellingCorrector](../../groupdocs.search.options/searchoptions/spellingcorrector) { get; } | 获取拼写校正选项。 |
| [UseCaseSensitiveSearch](../../groupdocs.search.options/searchoptions/usecasesensitivesearch) { get; set; } | 获取或设置区分大小写搜索的标志。 默认值为`错误的`. |
| [UseHomophoneSearch](../../groupdocs.search.options/searchoptions/usehomophonesearch) { get; set; } | 获取或设置搜索中使用同音字的标志。 默认值为`错误的`. |
| [UseSynonymSearch](../../groupdocs.search.options/searchoptions/usesynonymsearch) { get; set; } | 获取或设置在搜索中使用同义词的标志。 默认值为`错误的`. |
| [UseWordFormsSearch](../../groupdocs.search.options/searchoptions/usewordformssearch) { get; set; } | 获取或设置搜索使用不同词形的标志。 默认值为`错误的`. |

### 评论

**学到更多**

* [搜索选项](https://docs.groupdocs.com/display/searchnet/Search+options)

### 也可以看看

* 命名空间 [GroupDocs.Search.Options](../../groupdocs.search.options)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->