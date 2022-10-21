---
title: ExtractionOptions
second_title: GroupDocs.Search for .NET API 参考
description: 提供从文档中提取数据的选项
type: docs
weight: 790
url: /zh/net/groupdocs.search.options/extractionoptions/
---
## ExtractionOptions class

提供从文档中提取数据的选项。

```csharp
public class ExtractionOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [ExtractionOptions](extractionoptions)() | 初始化[`ExtractionOptions`](../extractionoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CustomExtractor](../../groupdocs.search.options/extractionoptions/customextractor) { get; set; } | 获取或设置自定义文本提取器。 默认值为`无效的`. |
| [Encoding](../../groupdocs.search.options/extractionoptions/encoding) { get; set; } | 获取或设置用于从文本文档中提取的编码。 |
| [ImageIndexingOptions](../../groupdocs.search.options/extractionoptions/imageindexingoptions) { get; } | 获取用于反向图像搜索的图像索引选项。 |
| [MetadataIndexingOptions](../../groupdocs.search.options/extractionoptions/metadataindexingoptions) { get; } | 获取索引元数据字段的选项。 |
| [OcrIndexingOptions](../../groupdocs.search.options/extractionoptions/ocrindexingoptions) { get; } | 获取 OCR 处理和索引识别文本的选项。 |
| [UseRawTextExtraction](../../groupdocs.search.options/extractionoptions/userawtextextraction) { get; set; } | 获取或设置一个值，如果可能，是否使用原始模式进行文本提取。 默认值为`真的`. 原始模式可以显着提高索引速度，但普通模式改进了提取文本的格式。 |

### 也可以看看

* 命名空间 [GroupDocs.Search.Options](../../groupdocs.search.options)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->