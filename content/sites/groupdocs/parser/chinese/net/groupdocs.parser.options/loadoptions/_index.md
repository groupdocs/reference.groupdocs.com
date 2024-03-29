---
title: LoadOptions
second_title: GroupDocs.Parser for .NET API 参考
description: 提供用于打开文件的选项
type: docs
weight: 470
url: /zh/net/groupdocs.parser.options/loadoptions/
---
## LoadOptions class

提供用于打开文件的选项。

```csharp
public sealed class LoadOptions
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [LoadOptions](loadoptions#constructor)() | 初始化一个新的实例[`LoadOptions`](../loadoptions) 类为空[`Password`](./password),[`FileFormat`](./fileformat)等于Unknown 和默认编码。 |
| [LoadOptions](loadoptions#constructor_1)(FileFormat) | 初始化一个新的实例[`LoadOptions`](../loadoptions) class 为空[`Password`](./password)和默认编码. |
| [LoadOptions](loadoptions#constructor_4)(string) | 初始化一个新的实例[`LoadOptions`](../loadoptions) class 与[`FileFormat`](./fileformat)等于Unknown 和默认编码。 |
| [LoadOptions](loadoptions#constructor_2)(FileFormat, string) | 初始化一个新的实例[`LoadOptions`](../loadoptions)带有密码和默认编码的类。 |
| [LoadOptions](loadoptions#constructor_3)(FileFormat, string, Encoding, Encoding) | 初始化一个新的实例[`LoadOptions`](../loadoptions)具有自定义编码的类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [DefaultAnsiEncoding](../../groupdocs.parser.options/loadoptions/defaultansiencoding) { get; } | 获取用于编码检测的默认 ANSI 编码。 |
| [Encoding](../../groupdocs.parser.options/loadoptions/encoding) { get; } | 获取文档的编码。 |
| [FileFormat](../../groupdocs.parser.options/loadoptions/fileformat) { get; } | 获取文件格式。 |
| [Password](../../groupdocs.parser.options/loadoptions/password) { get; } | 获取密码。 |

### 评论

此类的一个实例用作参数[`Parser`](../../groupdocs.parser/parser)类构造函数：

* [`Parser`](../../groupdocs.parser/parser/parser)
* [`Parser`](../../groupdocs.parser/parser/parser)

请参阅此处的用法示例。

**了解更多：**

* [加载特定文件格式](https://docs.groupdocs.com/display/parsernet/Loading+specific+file+formats)
* [装入受密码保护的文档](https://docs.groupdocs.com/display/parsernet/Password-protected+documents)

### 也可以看看

* 命名空间 [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* 部件 [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
