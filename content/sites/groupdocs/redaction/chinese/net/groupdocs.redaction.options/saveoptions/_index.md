---
title: SaveOptions
second_title: GroupDocs.Redaction for .NET API 参考
description: 提供用于更改输出文件名和/或将文档转换为基于图像的 PDF光栅化的选项
type: docs
weight: 370
url: /zh/net/groupdocs.redaction.options/saveoptions/
---
## SaveOptions class

提供用于更改输出文件名和/或将文档转换为基于图像的 PDF（光栅化）的选项。

```csharp
public class SaveOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [SaveOptions](saveoptions#constructor)() | 使用默认值初始化新实例：光栅化为 PDF - false，添加后缀 - false. |
| [SaveOptions](saveoptions#constructor_1)(bool, string) | 使用给定参数初始化一个新实例。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [AddSuffix](../../groupdocs.redaction.options/saveoptions/addsuffix) { get; set; } | 获取或设置一个值，该值指示在保存之前是否需要更改文件名。默认为假。 |
| [Rasterization](../../groupdocs.redaction.options/saveoptions/rasterization) { get; } | 获取光栅化设置。 |
| [RasterizeToPDF](../../groupdocs.redaction.options/saveoptions/rasterizetopdf) { get; set; } | 获取或设置一个值，该值指示是否需要将文档中的所有页面都转换为图像并放入单个 PDF 文件中。 |
| [RedactedFileSuffix](../../groupdocs.redaction.options/saveoptions/redactedfilesuffix) { get; set; } | 获取或设置输出文件名的自定义后缀。如果未指定，则[`SaveSuffix`](./savesuffix)将使用常量。 |

## 字段

| 姓名 | 描述 |
| --- | --- |
| const [SaveSuffix](../../groupdocs.redaction.options/saveoptions/savesuffix) | 表示默认后缀值，即“Redacted”。 |

### 评论

**学到更多**

* [使用默认选项保存](https://docs.groupdocs.com/redaction/net/save-with-default-options/)
* [保存为栅格化 PDF](https://docs.groupdocs.com/redaction/net/save-in-rasterized-pdf/)
* [为光栅化 PDF 选择特定页面](https://docs.groupdocs.com/redaction/net/select-specific-pages-for-rasterized-pdf/)
* [以原始格式保存](https://docs.groupdocs.com/redaction/net/save-in-original-format/)
* [保存覆盖原始文件](https://docs.groupdocs.com/redaction/net/save-overwriting-original-file/)
* [保存到流](https://docs.groupdocs.com/redaction/net/save-to-stream/)

### 例子

以下示例演示如何使用 SaveOptions 保存文档。

```csharp
    using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
    {
       // 文档编辑在这里
       // ...
    
       // 使用默认选项保存文档（将页面转换为图像，另存为 PDF）
       redactor.Save();
    
       // 以原始格式保存文档覆盖原始文件
       redactor.Save(new SaveOptions() { AddSuffix = false, RasterizeToPDF = false });
    
       // 将文档以原始格式保存到“*_Redacted.*”文件
       redactor.Save(new SaveOptions() { AddSuffix = true, RasterizeToPDF = false });
    
       // 将文档保存到其文件名中的“*_AnyText.*”（例如时间戳而不是“AnyText”），无需光栅化
       redactor.Save(new SaveOptions(false, "AnyText"));
    }    
```

### 也可以看看

* 命名空间 [GroupDocs.Redaction.Options](../../groupdocs.redaction.options)
* 部件 [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->