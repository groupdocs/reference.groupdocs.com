---
title: DocumentData
second_title: GroupDocs.Parser for .NET API 参考
description: 表示文档的数据它包括FieldData./fielddataobjects 包含来自 document. 的字段数据
type: docs
weight: 20
url: /zh/net/groupdocs.parser.data/documentdata/
---
## DocumentData class

表示文档的数据。它包括[`FieldData`](../fielddata)objects 包含来自 document. 的字段数据

```csharp
public class DocumentData : IEnumerable<FieldData>
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [DocumentData](documentdata)(IEnumerable&lt;FieldData&gt;) | 初始化一个新的实例[`FieldData`](../fielddata)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Count](../../groupdocs.parser.data/documentdata/count) { get; } | 获取字段数据总数。 |
| [Item](../../groupdocs.parser.data/documentdata/item) { get; } | 通过索引获取字段数据。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [GetEnumerator](../../groupdocs.parser.data/documentdata/getenumerator)() | 返回字段数据的枚举器。 |
| [GetFieldsByName](../../groupdocs.parser.data/documentdata/getfieldsbyname)(string) | 返回名称等于的字段数据集合*fieldName*. |

### 评论

的实例[`DocumentData`](../documentdata)类用作返回值 的[`ParseByTemplate`](../../groupdocs.parser/parser/parsebytemplate)和[`ParseForm`](../../groupdocs.parser/parser/parseform) methods. 请参阅此处的用法示例。

### 也可以看看

* class [FieldData](../fielddata)
* 命名空间 [GroupDocs.Parser.Data](../../groupdocs.parser.data)
* 部件 [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
