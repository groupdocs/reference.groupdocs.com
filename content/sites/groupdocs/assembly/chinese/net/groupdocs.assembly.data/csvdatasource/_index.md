---
title: CsvDataSource
second_title: GroupDocs.Assembly for .NET API 参考
description: 提供对组合文档时要使用的 CSV 文件或流的数据的访问
type: docs
weight: 30
url: /zh/net/groupdocs.assembly.data/csvdatasource/
---
## CsvDataSource class

提供对组合文档时要使用的 CSV 文件或流的数据的访问。

```csharp
public class CsvDataSource
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [CsvDataSource](csvdatasource#constructor)(Stream) | 使用解析 CSV 数据的默认选项，使用来自 CSV 流的数据创建新数据源。 |
| [CsvDataSource](csvdatasource#constructor_2)(string) | 使用解析 CSV 数据的默认选项，使用来自 CSV 文件的数据创建新数据源。 |
| [CsvDataSource](csvdatasource#constructor_1)(Stream, CsvDataLoadOptions) | 使用用于解析 CSV 数据的指定选项，使用来自 CSV 流的数据创建新数据源。 |
| [CsvDataSource](csvdatasource#constructor_3)(string, CsvDataLoadOptions) | 使用用于解析 CSV 数据的指定选项使用 CSV 文件中的数据创建新数据源。 |

### 评论

要在组装文档时访问相应文件或流的数据，请将此类的实例作为 数据源传递给其中一个[`DocumentAssembler`](../../groupdocs.assembly/documentassembler).AssembleDocument 重载.

在模板文档中，一个[`CsvDataSource`](../csvdatasource)实例应该以与 was a 相同的方式处理DataTable实例。有关详细信息，请参阅模板语法参考 (https://docs.groupdocs.com/display/assemblynet/Template+Syntax+-+Part+1+of+2#TemplateSyntax-Part1of2-UsingDataSources)。

逗号分隔值的数据类型根据其字符串表示形式自动确定。因此，在 template 文档中，您可以使用类型化的值而不仅仅是字符串。引擎能够自动识别以下类型的 值：

* Nullable
* Nullable
* Nullable
* Nullable
* String

请注意，为了自动识别数据类型，逗号分隔值的字符串表示应该 使用不变的区域性设置形成。

要覆盖 CSV 数据加载的默认行为，初始化并传递[`CsvDataLoadOptions`](../csvdataloadoptions)instance 到此类的构造函数。

### 也可以看看

* 命名空间 [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* 部件 [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->