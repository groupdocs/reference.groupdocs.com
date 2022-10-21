---
title: CustomExtractorCollection
second_title: GroupDocs.Search for .NET API 参考
description: 包含自定义提取器的集合 如果集合包含内置提取器覆盖的某些文件扩展名的提取器 则将使用此提取器而不是内置提取器
type: docs
weight: 40
url: /zh/net/groupdocs.search.common/customextractorcollection/
---
## CustomExtractorCollection class

包含自定义提取器的集合。 如果集合包含内置提取器覆盖的某些文件扩展名的提取器， 则将使用此提取器而不是内置提取器。

```csharp
public class CustomExtractorCollection : ICollection<IFieldExtractor>
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Count](../../groupdocs.search.common/customextractorcollection/count) { get; } | 获取集合中包含的提取器的数量。 |
| [IsReadOnly](../../groupdocs.search.common/customextractorcollection/isreadonly) { get; } | 获取一个值，该值指示该集合是否为只读。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [Add](../../groupdocs.search.common/customextractorcollection/add)(IFieldExtractor) | 将提取器添加到集合中。 |
| [Clear](../../groupdocs.search.common/customextractorcollection/clear)() | 从集合中删除所有提取器。 |
| [Contains](../../groupdocs.search.common/customextractorcollection/contains)(IFieldExtractor) | 确定集合是否包含特定的提取器。 |
| [CopyTo](../../groupdocs.search.common/customextractorcollection/copyto)(IFieldExtractor[], int) | 将集合的元素复制到数组中，从特定的数组索引开始。 |
| [GetEnumerator](../../groupdocs.search.common/customextractorcollection/getenumerator)() | 返回此集合的枚举数。 |
| [Remove](../../groupdocs.search.common/customextractorcollection/remove)(IFieldExtractor) | 从集合中删除一个提取器。 |

### 评论

**学到更多**

* [自定义文本提取器](https://docs.groupdocs.com/display/searchnet/Custom+text+extractors)

### 也可以看看

* interface [IFieldExtractor](../ifieldextractor)
* 命名空间 [GroupDocs.Search.Common](../../groupdocs.search.common)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->