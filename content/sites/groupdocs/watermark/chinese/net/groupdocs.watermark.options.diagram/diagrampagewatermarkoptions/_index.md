---
title: DiagramPageWatermarkOptions
second_title: .NET API 参考的 GroupDocs.Watermark
description: 表示将形状水印添加到 Visio 文档的特定页面时添加水印的选项
type: docs
weight: 1650
url: /zh/net/groupdocs.watermark.options.diagram/diagrampagewatermarkoptions/
---
## DiagramPageWatermarkOptions class

表示将形状水印添加到 Visio 文档的特定页面时添加水印的选项。

```csharp
public sealed class DiagramPageWatermarkOptions : DiagramWatermarkOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [DiagramPageWatermarkOptions](diagrampagewatermarkoptions)() | 初始化[`DiagramPageWatermarkOptions`](../diagrampagewatermarkoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [IsLocked](../../groupdocs.watermark.options.diagram/diagramwatermarkoptions/islocked) { get; set; } | 获取或设置一个值，该值指示是否禁止在 Visio 中编辑形状。 |
| [PageIndex](../../groupdocs.watermark.options.diagram/diagrampagewatermarkoptions/pageindex) { get; set; } | 获取或设置要添加水印的页面索引。 |

### 评论

**学到更多：**

* [为图表文档添加水印](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+diagram+documents)

### 例子

将受保护的水印添加到 Visio 文档的第一页。

```csharp
DiagramLoadOptions loadOptions = new DiagramLoadOptions();
using (Watermarker watermarker = new Watermarker(@"D:\test.vsdx", loadOptions))
{
    TextWatermark watermark = new TextWatermark("watermark test", new Font("Arial", 42));

    DiagramPageWatermarkOptions options = new DiagramPageWatermarkOptions();
    options.IsLocked = true;
    options.PageIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### 也可以看看

* class [DiagramWatermarkOptions](../diagramwatermarkoptions)
* 命名空间 [GroupDocs.Watermark.Options.Diagram](../../groupdocs.watermark.options.diagram)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->