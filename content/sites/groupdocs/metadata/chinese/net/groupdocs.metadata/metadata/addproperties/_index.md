---
title: AddProperties
second_title: GroupDocs.Metadata for .NET API 参考
description: 添加满足指定谓词的已知元数据属性 该操作是递归的因此它也会影响所有嵌套包
type: docs
weight: 30
url: /zh/net/groupdocs.metadata/metadata/addproperties/
---
## Metadata.AddProperties method

添加满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。

```csharp
public int AddProperties(Func<MetadataProperty, bool> predicate, PropertyValue value)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| predicate | Func`2 | 用于测试每个元数据属性的条件的函数。 |
| value | PropertyValue | 拾取属性的值。 |

### 返回值

受影响属性的数量。

### 评论

**学到更多**

* 更多演示此方法用法的示例： [添加元数据](https://docs.groupdocs.com/display/metadatanet/Adding+metadata)

### 例子

此示例演示如何将一些缺少的元数据属性添加到文件中，而不管其格式如何。

```csharp
using (Metadata metadata = new Metadata(Constants.InputDocx))
{
    // 添加一个包含文件上次打印日期的属性（如果缺少）
    // 请注意，该属性将被添加到满足以下条件的元数据包中：
    // 1) 只有现有的元数据包会受到影响。此操作期间不添加新包
    // 2) 包结构中应该有一个已知的元数据属性，它符合搜索条件，但实际上在包中是缺失的。
    // 某个包支持的所有属性通常定义在特定元数据标准的规范中
    var affected = metadata.AddProperties(p => p.Tags.Contains(Tags.Time.Printed), new PropertyValue(DateTime.Now));

    Console.WriteLine("Affected properties: {0}", affected);

    metadata.Save(Constants.OutputDocx);
}
```

### 也可以看看

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [PropertyValue](../../../groupdocs.metadata.common/propertyvalue)
* class [Metadata](../../metadata)
* 命名空间 [GroupDocs.Metadata](../../metadata)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->