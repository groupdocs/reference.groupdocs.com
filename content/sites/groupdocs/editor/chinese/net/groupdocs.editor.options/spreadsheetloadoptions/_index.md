---
title: SpreadsheetLoadOptions
second_title: GroupDocs.Editor for .NET API 参考
description: 包含将二进制电子表格单元格Excel 兼容文档如 XLSXODS 等加载到编辑器中的选项 class
type: docs
weight: 900
url: /zh/net/groupdocs.editor.options/spreadsheetloadoptions/
---
## SpreadsheetLoadOptions class

包含将二进制电子表格（单元格、Excel 兼容）文档（如 XLS(X)、ODS 等）加载到编辑器中的选项 class

```csharp
public sealed class SpreadsheetLoadOptions : ILoadOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [SpreadsheetLoadOptions](spreadsheetloadoptions)() | 默认无参数构造函数 - 所有参数都有默认值 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [OptimizeMemoryUsage](../../groupdocs.editor.options/spreadsheetloadoptions/optimizememoryusage) { get; set; } | 在输入文档处理期间启用内存优化机制，在某些特殊情况下可能会降低性能， 但另一方面会降低内存使用量。在处理大量文档并面临 OutOfMemoryException 时很有用。 默认为 false（为了更好的性能而禁用内存优化）。 |
| [Password](../../groupdocs.editor.options/spreadsheetloadoptions/password) { get; set; } | 允许指定、修改和获取密码，该密码将用于打开电子表格文档（如果已编码）。 设置为 NULL 或空字符串，以便不使用密码（默认值）。 |

### 也可以看看

* interface [ILoadOptions](../iloadoptions)
* 命名空间 [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* 部件 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
