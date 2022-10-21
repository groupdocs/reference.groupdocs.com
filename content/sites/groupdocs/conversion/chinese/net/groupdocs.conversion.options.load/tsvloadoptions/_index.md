---
title: TsvLoadOptions
second_title: GroupDocs.Conversion for .NET API 参考
description: 加载 Tsv 文档的选项
type: docs
weight: 2030
url: /zh/net/groupdocs.conversion.options.load/tsvloadoptions/
---
## TsvLoadOptions class

加载 Tsv 文档的选项。

```csharp
public sealed class TsvLoadOptions : SpreadsheetLoadOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [TsvLoadOptions](tsvloadoptions)() | 初始化的新实例[`TsvLoadOptions`](../tsvloadoptions)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CheckExcelRestriction](../../groupdocs.conversion.options.load/spreadsheetloadoptions/checkexcelrestriction) { get; set; } | 用户修改单元格相关对象时是否检查excel文件的限制。例如，excel 不允许输入超过 32K 的字符串值。当你输入一个超过 32K 的值时，如果这个属性为真，你会得到一个 Exception。如果此属性为 false，我们将接受您输入的字符串值作为单元格的值，以便稍后您可以为其他文件格式（例如 CSV）输出完整的字符串值。但是，如果您设置了此类对 excel 文件格式无效的值，则以后不应将工作簿另存为 excel 文件格式。否则生成的excel文件可能会出现意外错误。 |
| [ConvertRange](../../groupdocs.conversion.options.load/spreadsheetloadoptions/convertrange) { get; set; } | 转换为非电子表格格式时转换特定范围。示例：“D1:F8”. |
| [CultureInfo](../../groupdocs.conversion.options.load/spreadsheetloadoptions/cultureinfo) { get; set; } | 获取或设置文件加载时的系统文化信息 |
| [DefaultFont](../../groupdocs.conversion.options.load/spreadsheetloadoptions/defaultfont) { get; set; } | 电子表格文档的默认字体。如果缺少字体，将使用以下字体。 |
| [FontSubstitutes](../../groupdocs.conversion.options.load/spreadsheetloadoptions/fontsubstitutes) { get; set; } | 转换电子表格文档时替换特定字体。 |
| [Format](../../groupdocs.conversion.options.load/spreadsheetloadoptions/format) { get; set; } | 输入文档文件类型。 |
| [Format](../../groupdocs.conversion.options.load/loadoptions/format) { get; } | 输入文档文件类型。 |
| [HideComments](../../groupdocs.conversion.options.load/spreadsheetloadoptions/hidecomments) { get; set; } | 隐藏评论。 |
| [OnePagePerSheet](../../groupdocs.conversion.options.load/spreadsheetloadoptions/onepagepersheet) { get; set; } | 如果 OnePagePerSheet 为真，则工作表的内容将转换为 PDF 文档中的一页。默认值为真。 |
| [OptimizePdfSize](../../groupdocs.conversion.options.load/spreadsheetloadoptions/optimizepdfsize) { get; set; } | 如果为真并转换为 Pdf，则优化转换以获得比打印质量更好的文件大小。 |
| [Password](../../groupdocs.conversion.options.load/spreadsheetloadoptions/password) { get; set; } | 设置密码以取消保护受保护的文档。 |
| [Sheets](../../groupdocs.conversion.options.load/spreadsheetloadoptions/sheets) { get; set; } | 要转换的工作表名称 |
| [ShowGridLines](../../groupdocs.conversion.options.load/spreadsheetloadoptions/showgridlines) { get; set; } | 转换 Excel 文件时显示网格线。 |
| [ShowHiddenSheets](../../groupdocs.conversion.options.load/spreadsheetloadoptions/showhiddensheets) { get; set; } | 转换 Excel 文件时显示隐藏的工作表。 |
| [SkipEmptyRowsAndColumns](../../groupdocs.conversion.options.load/spreadsheetloadoptions/skipemptyrowsandcolumns) { get; set; } | 转换时跳过空行和列。默认为真。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.load/spreadsheetloadoptions/clone)() | 克隆当前实例。 |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | 确定两个对象实例是否相等。 |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | 确定两个对象实例是否相等。 |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | 用作默认哈希函数。 |

### 也可以看看

* class [SpreadsheetLoadOptions](../spreadsheetloadoptions)
* 命名空间 [GroupDocs.Conversion.Options.Load](../../groupdocs.conversion.options.load)
* 部件 [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->