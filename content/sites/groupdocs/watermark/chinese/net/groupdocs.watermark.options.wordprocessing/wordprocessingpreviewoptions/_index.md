---
title: WordProcessingPreviewOptions
second_title: .NET API 参考的 GroupDocs.Watermark
description: 提供选项来设置要求和流委托以预览生成 WordProcessing 文档
type: docs
weight: 2300
url: /zh/net/groupdocs.watermark.options.wordprocessing/wordprocessingpreviewoptions/
---
## WordProcessingPreviewOptions class

提供选项来设置要求和流委托以预览生成 WordProcessing 文档。

```csharp
public class WordProcessingPreviewOptions : PreviewOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [WordProcessingPreviewOptions](wordprocessingpreviewoptions#constructor)(CreatePageStream) | 初始化一个新的实例[`WordProcessingPreviewOptions`](../wordprocessingpreviewoptions)导致输出流关闭的类。 |
| [WordProcessingPreviewOptions](wordprocessingpreviewoptions#constructor_1)(CreatePageStream, ReleasePageStream) | 初始化一个新实例[`WordProcessingPreviewOptions`](../wordprocessingpreviewoptions)导致输出流被返回 到客户端以供进一步使用的类。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CreatePageStream](../../groupdocs.watermark.options/previewoptions/createpagestream) { get; set; } | 获取或设置页面流创建委托的实例。 |
| [Height](../../groupdocs.watermark.options/previewoptions/height) { get; set; } | 获取或设置页面预览高度。 |
| [PageNumbers](../../groupdocs.watermark.options/previewoptions/pagenumbers) { get; set; } | 获取或设置页码数组以生成预览。 |
| [PreviewFormat](../../groupdocs.watermark.options/previewoptions/previewformat) { get; set; } | 获取或设置预览图像格式。 |
| [ReleasePageStream](../../groupdocs.watermark.options/previewoptions/releasepagestream) { get; set; } | 获取或设置页面预览完成委托的实例。 |
| [Resolution](../../groupdocs.watermark.options.wordprocessing/wordprocessingpreviewoptions/resolution) { get; set; } | 获取或设置生成图像的分辨率，以每英寸点数为单位。 |
| [Width](../../groupdocs.watermark.options/previewoptions/width) { get; set; } | 获取或设置页面预览宽度。 |

## 字段

| 姓名 | 描述 |
| --- | --- |
| const [DefaultResolution](../../groupdocs.watermark.options.wordprocessing/wordprocessingpreviewoptions/defaultresolution) | 默认分辨率（以每英寸点数为单位）. |

### 也可以看看

* class [PreviewOptions](../../groupdocs.watermark.options/previewoptions)
* 命名空间 [GroupDocs.Watermark.Options.WordProcessing](../../groupdocs.watermark.options.wordprocessing)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
