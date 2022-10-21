---
title: RasterizationOptions
second_title: GroupDocs.Redaction for .NET API 参考
description: 提供将文件转换为 PDF 的选项
type: docs
weight: 340
url: /zh/net/groupdocs.redaction.options/rasterizationoptions/
---
## RasterizationOptions class

提供将文件转换为 PDF 的选项。

```csharp
public class RasterizationOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [RasterizationOptions](rasterizationoptions)() | 初始化一个新实例。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Compliance](../../groupdocs.redaction.options/rasterizationoptions/compliance) { get; set; } | 获取或设置 PDF 合规级别。 |
| [Enabled](../../groupdocs.redaction.options/rasterizationoptions/enabled) { get; set; } | 获取或设置一个值，该值指示是否需要将文档中的所有页面转换为图像并放入单个 PDF 文件中。默认为 TRUE，设置为 FALSE 以避免光栅化。 |
| [PageCount](../../groupdocs.redaction.options/rasterizationoptions/pagecount) { get; set; } | 获取或设置要转换成PDF的页数。 |
| [PageIndex](../../groupdocs.redaction.options/rasterizationoptions/pageindex) { get; set; } | 获取或设置要转换为 PDF 的第一页的索引（从 0 开始）。 |

### 评论

**学到更多**

* 有关将文档另存为光栅化 PDF 的更多详细信息： [保存为栅格化 PDF](https://docs.groupdocs.com/redaction/net/save-in-rasterized-pdf/)
* 有关光栅化选项的更多详细信息： [为光栅化 PDF 选择特定页面](https://docs.groupdocs.com/redaction/net/select-specific-pages-for-rasterized-pdf/)

### 例子

以下示例演示了如何为光栅化过程设置选项。

```csharp
    using (var redactor = new Redactor("SomePresentation.pptx"))
    {
        // 在第一张幻灯片上编辑敏感数据 
    
        var rasterizationOptions = new RasterizationOptions();
        rasterizationOptions.PageIndex = 0;
        rasterizationOptions.PageCount = 1;
        rasterizationOptions.Compliance = PdfComplianceLevel.PdfA1a;
        using (var stream = File.Open(Path.Combine(@"C:\Temp", "PresentationFirstSlide.pdf")))
        {
            redactor.Save(stream, rasterizationOptions);
        }
    }      
```

### 也可以看看

* 命名空间 [GroupDocs.Redaction.Options](../../groupdocs.redaction.options)
* 部件 [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->