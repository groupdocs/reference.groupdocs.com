---
title: WordProcessingSaveOptions
second_title: GroupDocs.Editor for .NET API 参考
description: 允许指定自定义选项以在编辑后生成和保存符合 WordProcessing 的文档
type: docs
weight: 1010
url: /zh/net/groupdocs.editor.options/wordprocessingsaveoptions/
---
## WordProcessingSaveOptions class

允许指定自定义选项以在编辑后生成和保存符合 WordProcessing 的文档

```csharp
public sealed class WordProcessingSaveOptions : ICloneable, ISaveOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [WordProcessingSaveOptions](wordprocessingsaveoptions)(WordProcessingFormats) | 使用指定的强制字处理输出格式创建 WordProcessingSaveOptions 的新实例，而所有其他参数均为默认值 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [EnablePagination](../../groupdocs.editor.options/wordprocessingsaveoptions/enablepagination) { get; set; } | 允许启用或禁用用于保存字处理文档的分页。 如果在分页模式下打开和编辑原始文档，也应启用此选项。默认情况下是禁用的。 |
| [FontEmbedding](../../groupdocs.editor.options/wordprocessingsaveoptions/fontembedding) { get; set; } | 负责将字体资源嵌入到输出字处理文档中。默认情况下不嵌入任何字体（NotEmbed）。 |
| [Locale](../../groupdocs.editor.options/wordprocessingsaveoptions/locale) { get; set; } | 允许为 WordProcessing 文档设置覆盖默认区域设置（语言），这将在其创建期间应用。 如果未指定（默认值），MS Word（或其他程序）将检测（或选择）文档区域设置 根据取决于它自己的设置或其他因素。 |
| [LocaleBi](../../groupdocs.editor.options/wordprocessingsaveoptions/localebi) { get; set; } | 允许为 RTL（从右到左）文本的 WordProcessing 文档设置覆盖区域设置（语言），这将在其创建期间应用。 未指定时（默认值），MS Word（或其他程序）会根据自己的设置或其他因素检测（或选择）文档RTL locale 。 |
| [LocaleFarEast](../../groupdocs.editor.options/wordprocessingsaveoptions/localefareast) { get; set; } | 允许覆盖东亚文本的 WordProcessing 文档的区域设置（语言），这将在其创建期间应用。 如果未指定（默认值），MS Word（或其他程序）将检测（或选择) 文档东亚locale 根据自己的设置或其他因素. |
| [OptimizeMemoryUsage](../../groupdocs.editor.options/wordprocessingsaveoptions/optimizememoryusage) { get; set; } | 在从 HTML 生成文档期间启用内存优化机制，这会降低性能，以减少内存使用量为代价。 将此选项设置为 true 可以显着减少内存消耗，同时以较慢的节省时间为代价生成大型文档。 默认为 false （为了更好的性能，禁用了内存优化）. |
| [OutputFormat](../../groupdocs.editor.options/wordprocessingsaveoptions/outputformat) { get; set; } | 允许指定用于保存文档的字处理格式 |
| [Password](../../groupdocs.editor.options/wordprocessingsaveoptions/password) { get; set; } | 允许指定、修改、获取或删除密码，该密码将用于对生成的文字处理文档进行编码。 指定 NULL 或空字符串以删除（清除）密码。 |
| [Protection](../../groupdocs.editor.options/wordprocessingsaveoptions/protection) { get; set; } | 允许控制和应用任何格式的 WordProcessing 文档的文档保护选项，支持文档保护。 默认为 NULL - 将不使用文档保护。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Clone](../../groupdocs.editor.options/wordprocessingsaveoptions/clone)() | 创建并返回此 WordProcessingSaveOptions 类实例的完整副本 |

### 评论

WordProcessingSaveOptions 适用于存在 EditableDocument 类的实例，其中包含已编辑的文档内容，并且需要将该内容保存到 WordProcessing 格式的新文档的情况。

### 也可以看看

* interface [ISaveOptions](../isaveoptions)
* 命名空间 [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* 部件 [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
