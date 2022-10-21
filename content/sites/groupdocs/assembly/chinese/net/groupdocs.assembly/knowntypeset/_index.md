---
title: KnownTypeSet
second_title: GroupDocs.Assembly for .NET API 参考
description: 表示一个无序集合即唯一项的集合包含Type对象 可以在文档模板中使用完全或部分限定名称来调用相应的 类型的静态成员执行类型转换等
type: docs
weight: 230
url: /zh/net/groupdocs.assembly/knowntypeset/
---
## KnownTypeSet class

表示一个无序集合（即唯一项的集合），包含Type对象 可以在文档模板中使用完全或部分限定名称来调用相应的 类型的静态成员、执行类型转换等。

```csharp
public class KnownTypeSet : IEnumerable
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Count](../../groupdocs.assembly/knowntypeset/count) { get; } | 获取集合中项目的计数。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Add](../../groupdocs.assembly/knowntypeset/add)(Type) | 添加指定的Type反对集合。投掷ArgumentException在 以下情况： |
| [Clear](../../groupdocs.assembly/knowntypeset/clear)() | 从集合中移除所有项目。 |
| [GetEnumerator](../../groupdocs.assembly/knowntypeset/getenumerator)() | 返回一个IEnumerator对象迭代集合中的项目。 |
| [Remove](../../groupdocs.assembly/knowntypeset/remove)(Type) | 删除指定的Type集合中的对象。投掷ArgumentExceptionif *type*为空。 |

### 也可以看看

* 命名空间 [GroupDocs.Assembly](../../groupdocs.assembly)
* 部件 [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->