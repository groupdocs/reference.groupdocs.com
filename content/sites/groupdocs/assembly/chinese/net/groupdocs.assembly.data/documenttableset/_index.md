---
title: DocumentTableSet
second_title: GroupDocs.Assembly for .NET API 参考
description: 提供对位于外部文档中的多个表格或电子表格数据的访问以便在 汇编文档时使用此外还可以为文档表定义父子关系从而简化 对模板文档中相关数据的访问
type: docs
weight: 120
url: /zh/net/groupdocs.assembly.data/documenttableset/
---
## DocumentTableSet class

提供对位于外部文档中的多个表格（或电子表格）数据的访问，以便在 汇编文档时使用。此外，还可以为文档表定义父子关系，从而简化 对模板文档中相关数据的访问。

```csharp
public class DocumentTableSet
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [DocumentTableSet](documenttableset#constructor)(Stream) | 创建此类的新实例，使用默认 从文档加载所有表[`DocumentTableOptions`](../documenttableoptions). |
| [DocumentTableSet](documenttableset#constructor_2)(string) | 创建此类的新实例，使用默认 从文档加载所有表[`DocumentTableOptions`](../documenttableoptions). |
| [DocumentTableSet](documenttableset#constructor_1)(Stream, IDocumentTableLoadHandler) | 创建此类的新实例。 |
| [DocumentTableSet](documenttableset#constructor_3)(string, IDocumentTableLoadHandler) | 创建此类的新实例。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Relations](../../groupdocs.assembly.data/documenttableset/relations) { get; } | 获取为该集合的文档表定义的父子关系集合。 |
| [Tables](../../groupdocs.assembly.data/documenttableset/tables) { get; } | 获取集合[`DocumentTable`](../documenttable)代表这个集合的表的对象. |

### 评论

对于电子表格文件格式的文档，a[`DocumentTableSet`](../documenttableset) instance 表示一组 sheet. 对于其他文件格式的文档，一个[`DocumentTableSet`](../documenttableset)实例代表一组表.

要在组装文档时访问相应表的数据，将此类的实例作为 数据源传递给其中之一[`DocumentAssembler`](../../groupdocs.assembly/documentassembler).AssembleDocument 重载.

在模板文档中，一个[`DocumentTableSet`](../documenttableset)应以与 was a 相同的方式对待实例DataSet实例。有关详细信息，请参阅模板语法参考。

### 也可以看看

* 命名空间 [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* 部件 [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
