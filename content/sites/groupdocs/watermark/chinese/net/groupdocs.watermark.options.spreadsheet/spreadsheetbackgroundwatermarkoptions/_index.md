---
title: SpreadsheetBackgroundWatermarkOptions
second_title: .NET API 参考的 GroupDocs.Watermark
description: 表示将水印作为背景添加到电子表格工作表时的选项
type: docs
weight: 2120
url: /zh/net/groupdocs.watermark.options.spreadsheet/spreadsheetbackgroundwatermarkoptions/
---
## SpreadsheetBackgroundWatermarkOptions class

表示将水印作为背景添加到电子表格工作表时的选项。

```csharp
public sealed class SpreadsheetBackgroundWatermarkOptions : SpreadsheetWatermarkOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [SpreadsheetBackgroundWatermarkOptions](spreadsheetbackgroundwatermarkoptions)() | 初始化一个新的实例[`SpreadsheetBackgroundWatermarkOptions`](../spreadsheetbackgroundwatermarkoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [BackgroundHeight](../../groupdocs.watermark.options.spreadsheet/spreadsheetbackgroundwatermarkoptions/backgroundheight) { get; set; } | 获取或设置所需的背景图像高度（以像素为单位）。 |
| [BackgroundWidth](../../groupdocs.watermark.options.spreadsheet/spreadsheetbackgroundwatermarkoptions/backgroundwidth) { get; set; } | 获取或设置所需的背景图像宽度（以像素为单位）。 |
| [WorksheetIndex](../../groupdocs.watermark.options.spreadsheet/spreadsheetbackgroundwatermarkoptions/worksheetindex) { get; set; } | 获取或设置要添加水印的工作表索引。 |

### 评论

**了解更多：**

* [向电子表格文档添加水印](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+spreadsheet+documents)

### 例子

将文本水印添加到 Excel 文档工作表作为背景。

```csharp
SpreadsheetLoadOptions loadOptions = new SpreadsheetLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\Documents\test.xlsx", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test watermark", new Font("Arial", 36));

    SpreadsheetBackgroundWatermarkOptions options = new SpreadsheetBackgroundWatermarkOptions();
    options.WorksheetIndex = -1; // 默认
    options.BackgroundWidth = 800;
    options.BackgroundHeight = 600;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### 也可以看看

* class [SpreadsheetWatermarkOptions](../spreadsheetwatermarkoptions)
* 命名空间 [GroupDocs.Watermark.Options.Spreadsheet](../../groupdocs.watermark.options.spreadsheet)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
