---
title: FileType
second_title: .NET API 参考的 GroupDocs.Watermark
description: 代表文件类型
type: docs
weight: 40
url: /zh/net/groupdocs.watermark.common/filetype/
---
## FileType class

代表文件类型。

```csharp
public sealed class FileType : IEquatable<FileType>
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Extension](../../groupdocs.watermark.common/filetype/extension) { get; } | 获取文件名后缀（包括句点“.”），例如，“.doc”. |
| [FileFormatName](../../groupdocs.watermark.common/filetype/fileformatname) { get; } | 获取文件类型名称，例如“Microsoft Word 文档”。 |
| [FormatFamily](../../groupdocs.watermark.common/filetype/formatfamily) { get; } | 获取格式系列。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| static [FromExtension](../../groupdocs.watermark.common/filetype/fromextension)(string) | 将文件扩展名映射到文件类型。 |
| [Equals](../../groupdocs.watermark.common/filetype/equals#equals)(FileType) | 判断当前是否[`FileType`](../filetype)与指定的相同[`FileType`](../filetype)对象. |
| override [Equals](../../groupdocs.watermark.common/filetype/equals#equals_1)(object) | 判断当前是否[`FileType`](../filetype)与指定对象相同。 |
| override [GetHashCode](../../groupdocs.watermark.common/filetype/gethashcode)() | 返回当前的哈希码[`FileType`](../filetype)对象. |
| override [ToString](../../groupdocs.watermark.common/filetype/tostring)() | 返回表示当前对象的字符串。 |
| static [GetSupportedFileTypes](../../groupdocs.watermark.common/filetype/getsupportedfiletypes)() | 检索支持的文件类型。 |
| [operator ==](../../groupdocs.watermark.common/filetype/op_equality) | 判断是否两个[`FileType`](../filetype)对象是相同的。 |
| [operator !=](../../groupdocs.watermark.common/filetype/op_inequality) | 判断是否两个[`FileType`](../filetype)对象不一样. |

## 字段

| 姓名 | 描述 |
| --- | --- |
| static readonly [BMP](../../groupdocs.watermark.common/filetype/bmp) | 扩展名为 .BMP 的文件表示用于存储位图数字图像的位图图像文件。 这些图像独立于图形适配器，也称为设备独立位图 (DIB) 文件 格式。了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/bmp/). |
| static readonly [DOC](../../groupdocs.watermark.common/filetype/doc) | 扩展名为 .doc 的文件表示由 Microsoft Word 或其他文字处理生成的文档， 二进制文件格式的文档。详细了解此文件格式 [这里](https://wiki.fileformat.com/word-processing/doc/). |
| static readonly [DOCM](../../groupdocs.watermark.common/filetype/docm) | DOCM 文件是 Microsoft Word 2007 或更高版本生成的文档，能够运行宏。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/word-processing/docm/). |
| static readonly [DOCX](../../groupdocs.watermark.common/filetype/docx) | DOCX 是一种众所周知的 Microsoft Word 文档格式。从 2007 年随 Microsoft Office 2007 的 release 引入，这种新文档格式的结构从普通的 binary 更改为 XML 和二进制文件的组合。详细了解此文件格式 [这里](https://wiki.fileformat.com/word-processing/docx/). |
| static readonly [DOT](../../groupdocs.watermark.common/filetype/dot) | 扩展名为 .DOT 的文件是由 Microsoft Word 创建的模板文件，具有预格式化设置 用于生成更多 DOC 或 DOCX 文件。详细了解此文件格式 [这里](https://wiki.fileformat.com/word-processing/dot/). |
| static readonly [DOTM](../../groupdocs.watermark.common/filetype/dotm) | 带有 DOTM 扩展名的文件表示使用 Microsoft Word 2007 或更高版本创建的模板文件。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/word-processing/dotm/). |
| static readonly [DOTX](../../groupdocs.watermark.common/filetype/dotx) | 具有 DOTX 扩展名的文件是由 Microsoft Word 创建的模板文件，具有预格式化设置 用于生成更多 DOCX 文件。详细了解此文件格式 [这里](https://wiki.fileformat.com/word-processing/dotx/). |
| static readonly [EML](../../groupdocs.watermark.common/filetype/eml) | EML 文件格式表示使用 Outlook 和其他相关应用程序保存的电子邮件。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/email/eml/). |
| static readonly [EMLX](../../groupdocs.watermark.common/filetype/emlx) | EMLX 文件格式由 Apple 实施和开发。 Apple Mail 应用程序使用 EMLX 文件格式导出电子邮件。详细了解此文件格式 [这里](https://wiki.fileformat.com/email/emlx/). |
| static readonly [FlatOpc](../../groupdocs.watermark.common/filetype/flatopc) | Office Open XML WordprocessingML 存储在平面 XML 文件而不是 ZIP 包 (.xml) 中。 了解有关此文件格式的更多信息[这里](https://en.wikipedia.org/wiki/Office_Open_XML). |
| static readonly [FlatOpcMacroEnabled](../../groupdocs.watermark.common/filetype/flatopcmacroenabled) | Office Open XML WordprocessingML 启用宏的文档存储在平面 XML 文件中，而不是 ZIP 包 (.xml)。 了解有关此文件格式的更多信息[这里](https://en.wikipedia.org/wiki/Office_Open_XML). |
| static readonly [FlatOpcTemplate](../../groupdocs.watermark.common/filetype/flatopctemplate) | Office Open XML WordprocessingML 模板（无宏）存储在平面 XML 文件中，而不是 ZIP 包 (.xml)。 了解有关此文件格式的更多信息[这里](https://en.wikipedia.org/wiki/Office_Open_XML). |
| static readonly [FlatOpcTemplateMacroEnabled](../../groupdocs.watermark.common/filetype/flatopctemplatemacroenabled) | Office Open XML WordprocessingML 启用宏的模板存储在平面 XML 文件中，而不是 ZIP 包 (.xml)。 了解有关此文件格式的更多信息[这里](https://en.wikipedia.org/wiki/Office_Open_XML). |
| static readonly [GIF](../../groupdocs.watermark.common/filetype/gif) | GIF 或图形交换格式是一种高度压缩的图像。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/gif/). |
| static readonly [JPEG](../../groupdocs.watermark.common/filetype/jpeg) | JPEG 是一种使用有损压缩方法保存的图像格式。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/jpeg/). |
| static readonly [JPF](../../groupdocs.watermark.common/filetype/jpf) | JPEG 2000 (JPF) 是一种图像编码系统和最先进的图像压缩标准。 使用小波技术设计的 JPEG 2000 可以一次对任何质量的无损内容进行编码。详细了解 此文件格式[这里](https://wiki.fileformat.com/image/jp2/). |
| static readonly [JPG](../../groupdocs.watermark.common/filetype/jpg) | JPEG 是一种使用有损压缩方法保存的图像格式。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/jpeg/). |
| static readonly [JPM](../../groupdocs.watermark.common/filetype/jpm) | JPEG 2000 (JPM) 是图像编码系统和最先进的图像压缩标准。 使用小波技术设计的 JPEG 2000 可以一次对任何质量的无损内容进行编码。详细了解 此文件格式[这里](https://wiki.fileformat.com/image/jp2/). |
| static readonly [JPX](../../groupdocs.watermark.common/filetype/jpx) | JPEG 2000 (JPX) 是一种图像编码系统和最先进的图像压缩标准。 使用小波技术设计的 JPEG 2000 可以一次对任何质量的无损内容进行编码。详细了解 此文件格式[这里](https://wiki.fileformat.com/image/jp2/). |
| static readonly [MSG](../../groupdocs.watermark.common/filetype/msg) | MSG 是 Microsoft Outlook 和 Exchange 用于存储电子邮件、联系人、 约会或其他任务的文件格式。详细了解此文件格式 [这里](https://wiki.fileformat.com/email/msg/). |
| static readonly [ODT](../../groupdocs.watermark.common/filetype/odt) | ODT 文件是使用基于 OpenDocument 文本文件格式的文字处理应用程序创建的文档类型。这些是使用文字处理器应用程序创建的，例如免费的 OpenOffice Writer 和 可以保存文本、图像、对象和样式等内容。详细了解此文件格式 [这里](https://wiki.fileformat.com/word-processing/odt/). |
| static readonly [OFT](../../groupdocs.watermark.common/filetype/oft) | 扩展名为 .OFT 的文件表示使用 Microsoft Outlook 创建的消息模板文件。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/email/oft/). |
| static readonly [OOXML](../../groupdocs.watermark.common/filetype/ooxml) | Office 打开 xml 文件 (.ooxml). |
| static readonly [PDF](../../groupdocs.watermark.common/filetype/pdf) | 便携式文档格式 (PDF) 是 Adobe 在 1990 年代创建的一种文档。 this 文件格式的目的是在 中引入文档和其他参考资料的表示标准，这是一种独立于应用程序软件、硬件和操作系统的格式。了解有关此文件格式的更多信息 [这里](https://wiki.fileformat.com/view/pdf/). |
| static readonly [PNG](../../groupdocs.watermark.common/filetype/png) | PNG，便携式网络图形，指的是一种使用无损压缩的光栅图像文件格式。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/png/). |
| static readonly [POTM](../../groupdocs.watermark.common/filetype/potm) | 带有 POTM 扩展名的文件是支持宏的 Microsoft PowerPoint 模板文件。 POTM 文件 是使用 PowerPoint 2007 或更高版本创建的，包含可用于创建 更多演示文稿文件的默认设置。详细了解此文件格式 [这里](https://wiki.fileformat.com/presentation/potm/). |
| static readonly [POTX](../../groupdocs.watermark.common/filetype/potx) | 带有 .POTX 扩展名的文件表示使用 Microsoft PowerPoint 2007 及更高版本创建的 Microsoft PowerPoint 模板演示文稿。详细了解此文件格式 [这里](https://wiki.fileformat.com/presentation/potx/). |
| static readonly [PPS](../../groupdocs.watermark.common/filetype/pps) | PPS、PowerPoint 幻灯片，文件是使用 Microsoft PowerPoint 为幻灯片放映目的创建的。 Microsoft PowerPoint 97-2003 支持读取和创建 PPS 文件。详细了解此文件格式 [这里](https://wiki.fileformat.com/presentation/pps/). |
| static readonly [PPSM](../../groupdocs.watermark.common/filetype/ppsm) | 带有 PPSM 扩展名的文件表示使用 Microsoft PowerPoint 2007 或更高版本创建的启用宏的幻灯片放映文件格式。详细了解此文件格式 [这里](https://wiki.fileformat.com/presentation/ppsm/). |
| static readonly [PPSX](../../groupdocs.watermark.common/filetype/ppsx) | PPSX、Power Point 幻灯片放映文件是使用 Microsoft PowerPoint 2007 及更高版本创建的，用于 幻灯片放映目的。详细了解此文件格式 [这里](https://wiki.fileformat.com/presentation/ppsx/). |
| static readonly [PPT](../../groupdocs.watermark.common/filetype/ppt) | 带有 PPT 扩展名的文件代表 PowerPoint 文件，它由一组显示为 SlideShow 的幻灯片 for 组成。它指定 Microsoft PowerPoint 97-2003 使用的二进制文件格式。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/presentation/ppt/). |
| static readonly [PPTM](../../groupdocs.watermark.common/filetype/pptm) | 具有 PPTM 扩展名的文件是使用 Microsoft PowerPoint 2007 或更高版本创建的启用宏的演示文稿文件。详细了解此文件格式 [这里](https://wiki.fileformat.com/presentation/pptm/). |
| static readonly [PPTX](../../groupdocs.watermark.common/filetype/pptx) | 带有 PPTX 扩展名的文件是使用流行的 Microsoft PowerPoint 应用程序创建的演示文稿文件。 与以前版本的二进制演示文稿文件格式 PPT 不同，PPTX 格式基于 Microsoft PowerPoint open XML 演示文稿文件格式。详细了解此文件格式 [这里](https://wiki.fileformat.com/presentation/pptx/). |
| static readonly [RTF](../../groupdocs.watermark.common/filetype/rtf) | 富文本格式 (RTF) 由 Microsoft 引入并记录在案，代表了一种编码 格式的文本和图形以在应用程序中使用的方法。该格式便于与其他 Microsoft 产品进行跨平台 document 交换，从而达到互操作性的目的。详细了解 此文件格式[这里](https://wiki.fileformat.com/word-processing/rtf/). |
| static readonly [TIF](../../groupdocs.watermark.common/filetype/tif) | TIFF 或 TIF，标记图像文件格式，表示用于各种 符合此文件格式标准的设备的光栅图像。详细了解此文件格式 [这里](https://wiki.fileformat.com/image/tiff/). |
| static readonly [TIFF](../../groupdocs.watermark.common/filetype/tiff) | TIFF 或 TIF，标记图像文件格式，表示用于各种 符合此文件格式标准的设备的光栅图像。详细了解此文件格式 [这里](https://wiki.fileformat.com/image/tiff/). |
| static readonly [Unknown](../../groupdocs.watermark.common/filetype/unknown) | 代表未知文件类型。 |
| static readonly [VDW](../../groupdocs.watermark.common/filetype/vdw) | VDW 是 Visio 图形服务文件格式，它指定 呈现 Web 绘图所需的流和存储。详细了解此文件格式 [这里](https://wiki.fileformat.com/web/vdw/). |
| static readonly [VDX](../../groupdocs.watermark.common/filetype/vdx) | 在 Microsoft Visio 中创建但以 XML 格式保存的任何绘图或图表都具有 .VDX 扩展名。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/vdx/). |
| static readonly [VSD](../../groupdocs.watermark.common/filetype/vsd) | VSD 文件是使用 Microsoft Visio 应用程序创建的图形，用于表示各种图形 对象以及它们之间的互连。详细了解此文件格式 [这里](https://wiki.fileformat.com/image/vsd/). |
| static readonly [VSDM](../../groupdocs.watermark.common/filetype/vsdm) | 带有 VSDM 扩展名的文件是使用支持宏的 Microsoft Visio 应用程序创建的绘图文件。 了解有关此文件格式的更多信息 [这里](https://wiki.fileformat.com/image/vsdm/). |
| static readonly [VSDX](../../groupdocs.watermark.common/filetype/vsdx) | 扩展名为 .VSDX 的文件代表从 Microsoft Office 2013 开始引入的 Microsoft Visio 文件格式。详细了解此文件格式 [这里](https://wiki.fileformat.com/image/vsdx/). |
| static readonly [VSS](../../groupdocs.watermark.common/filetype/vss) | VSS 是使用 Microsoft Visio 2007 及更早版本创建的模板文件。模板文件提供可以包含在 .VSD Visio 绘图中的 drawing 对象。详细了解此文件格式 [这里](https://wiki.fileformat.com/image/vss/). |
| static readonly [VSSM](../../groupdocs.watermark.common/filetype/vssm) | 带有 .VSSM 扩展名的文件是支持宏的 Microsoft Visio Stencil 文件。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/vssm/). |
| static readonly [VSSX](../../groupdocs.watermark.common/filetype/vssx) | 扩展名为 .VSSX 的文件是使用 Microsoft Visio 2013 及更高版本创建的绘图模板。 了解有关此文件格式的更多信息 [这里](https://wiki.fileformat.com/image/vssx/). |
| static readonly [VST](../../groupdocs.watermark.common/filetype/vst) | 具有 VST 扩展名的文件是使用 Microsoft Visio 创建的矢量图像文件，可作为 创建更多文件的模板。详细了解此文件格式 [这里](https://wiki.fileformat.com/image/vst/). |
| static readonly [VSTM](../../groupdocs.watermark.common/filetype/vstm) | 具有 VSTM 扩展名的文件是使用支持宏的 Microsoft Visio 创建的模板文件。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/vstm/). |
| static readonly [VSTX](../../groupdocs.watermark.common/filetype/vstx) | 带有 VSTX 扩展名的文件是使用 Microsoft Visio 2013 及更高版本创建的绘图模板文件。 了解有关此文件格式的更多信息 [这里](https://wiki.fileformat.com/image/vstx/). |
| static readonly [VSX](../../groupdocs.watermark.common/filetype/vsx) | 具有 .VSX 扩展名的文件是指由图形和形状组成的模板，这些图形和形状用于 在 Microsoft Visio 中创建图表。详细了解此文件格式 [这里](https://wiki.fileformat.com/image/vsx/). |
| static readonly [VTX](../../groupdocs.watermark.common/filetype/vtx) | 带有 VTX 扩展名的文件是以 XML 文件格式保存到光盘的 Microsoft Visio 绘图模板。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/vtx/). |
| static readonly [WEBP](../../groupdocs.watermark.common/filetype/webp) | WebP，由谷歌推出，是一种基于无损和 有损压缩的现代光栅网络图像文件格式。它提供相同的图像质量，同时显着减小图像大小。 了解有关此文件格式的更多信息[这里](https://wiki.fileformat.com/image/webp/). |
| static readonly [XLS](../../groupdocs.watermark.common/filetype/xls) | 具有 XLS 扩展名的文件代表 Excel 二进制文件格式。此类文件可以由 Microsoft Excel 以及其他类似的电子表格程序（例如 OpenOffice Calc 或 Apple Numbers）创建。详细了解 此文件格式[这里](https://wiki.fileformat.com/specification/spreadsheet/xls/). |
| static readonly [XLSB](../../groupdocs.watermark.common/filetype/xlsb) | XLSB 文件格式指定 Excel 二进制文件格式，它是指定 Excel 工作簿内容的记录和 结构的集合。详细了解此文件格式 [这里](https://wiki.fileformat.com/specification/spreadsheet/xlsb/). |
| static readonly [XLSM](../../groupdocs.watermark.common/filetype/xlsm) | 具有 XLSM 扩展名的文件是一种支持宏的 Spreasheet 文件。详细了解此文件格式 [这里](https://wiki.fileformat.com/specification/spreadsheet/xlsm/). |
| static readonly [XLSX](../../groupdocs.watermark.common/filetype/xlsx) | XLSX 是众所周知的 Microsoft Excel 文档格式，由 Microsoft 在 Microsoft Office 2007 的 版本中引入。了解有关此文件格式 的更多信息[这里](https://wiki.fileformat.com/specification/spreadsheet/xlsx/). |
| static readonly [XLT](../../groupdocs.watermark.common/filetype/xlt) | 扩展名为 .XLT 的文件是使用 Microsoft Excel 创建的模板文件，Microsoft Excel 是一个电子表格 应用程序，是 Microsoft Office 套件的一部分。详细了解此文件格式 [这里](https://wiki.fileformat.com/specification/spreadsheet/xlt/). |
| static readonly [XLTM](../../groupdocs.watermark.common/filetype/xltm) | XLTM 文件扩展名表示由 Microsoft Excel 生成的文件，作为启用宏的 模板文件。详细了解此文件格式 [这里](https://wiki.fileformat.com/specification/spreadsheet/xltm/). |
| static readonly [XLTX](../../groupdocs.watermark.common/filetype/xltx) | 具有 XLTX 扩展名的文件表示基于 Office OpenXML 文件格式规范的 Microsoft Excel 模板文件。详细了解此文件格式 [这里](https://wiki.fileformat.com/specification/spreadsheet/xltx/). |

### 评论

这个类提供方法来获取所有支持的文件类型的列表**GroupDocs.水印**.**了解更多**

* [支持的文档格式](https://docs.groupdocs.com/display/watermarknet/Supported+Document+Formats)
* [获取支持的文件格式](https://docs.groupdocs.com/display/watermarknet/Get+supported+file+formats)
* [获取文档信息](https://docs.groupdocs.com/display/watermarknet/Get+document+info)

### 也可以看看

* 命名空间 [GroupDocs.Watermark.Common](../../groupdocs.watermark.common)
* 部件 [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
