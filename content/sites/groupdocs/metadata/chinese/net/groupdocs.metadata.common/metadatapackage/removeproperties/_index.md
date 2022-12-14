---
title: RemoveProperties
second_title: GroupDocs.Metadata for .NET API 参考
description: 删除满足指定谓词的元数据属性
type: docs
weight: 100
url: /zh/net/groupdocs.metadata.common/metadatapackage/removeproperties/
---
## MetadataPackage.RemoveProperties method

删除满足指定谓词的元数据属性。

```csharp
public virtual int RemoveProperties(Func<MetadataProperty, bool> predicate)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| predicate | Func`2 | 用于测试每个元数据属性的条件的函数。 |

### 返回值

受影响属性的数量。

### 评论

**学到更多**

* 更多演示此方法用法的示例： [删除元数据](https://docs.groupdocs.com/display/metadatanet/Removing+metadata)

### 也可以看看

* delegate [Func&lt;T,TResult&gt;](../../func-2)
* class [MetadataProperty](../../metadataproperty)
* class [MetadataPackage](../../metadatapackage)
* 命名空间 [GroupDocs.Metadata.Common](../../metadatapackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
