---
title: DocumentTableColumnCollection
second_title: GroupDocs.Assembly for .NET API 参考
description: 代表一个只读集合DocumentTableColumn./documenttablecolumn特定 的对象DocumentTable./documenttable实例.
type: docs
weight: 70
url: /zh/net/groupdocs.assembly.data/documenttablecolumncollection/
---
## DocumentTableColumnCollection class

代表一个只读集合[`DocumentTableColumn`](../documenttablecolumn)特定 的对象[`DocumentTable`](../documenttable)实例.

```csharp
public class DocumentTableColumnCollection : IEnumerable
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Count](../../groupdocs.assembly.data/documenttablecolumncollection/count) { get; } | 获取总数[`DocumentTableColumn`](../documenttablecolumn)集合中的对象. |
| [Item](../../groupdocs.assembly.data/documenttablecolumncollection/item) { get; } | 得到一个[`DocumentTableColumn`](../documenttablecolumn)来自指定索引处集合的实例. (2 indexers) |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Contains](../../groupdocs.assembly.data/documenttablecolumncollection/contains#contains)(DocumentTableColumn) | 返回一个值，指示此集合是否包含指定的列。 |
| [Contains](../../groupdocs.assembly.data/documenttablecolumncollection/contains#contains_1)(string) | 返回一个值，指示此集合是否包含具有指定名称的列。 |
| [GetEnumerator](../../groupdocs.assembly.data/documenttablecolumncollection/getenumerator)() | 返回一个枚举器进行迭代[`DocumentTableColumn`](../documenttablecolumn)此集合的对象. |
| [IndexOf](../../groupdocs.assembly.data/documenttablecolumncollection/indexof#indexof)(DocumentTableColumn) | 返回此集合中指定列的索引。 |
| [IndexOf](../../groupdocs.assembly.data/documenttablecolumncollection/indexof#indexof_1)(string) | 返回此集合中具有指定名称的列的索引。 |

### 评论

集合在从文档加载相应表格时自动填充，无法修改。 但是，属性[`DocumentTableColumn`](../documenttablecolumn)可以修改集合中包含的对象。

### 也可以看看

* 命名空间 [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* 部件 [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
