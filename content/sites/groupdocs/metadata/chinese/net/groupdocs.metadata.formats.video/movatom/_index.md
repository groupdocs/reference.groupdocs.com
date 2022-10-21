---
title: MovAtom
second_title: GroupDocs.Metadata for .NET API 参考
description: 表示一个 QuickTime 原子
type: docs
weight: 2620
url: /zh/net/groupdocs.metadata.formats.video/movatom/
---
## MovAtom class

表示一个 QuickTime 原子。

```csharp
public sealed class MovAtom : CustomPackage
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | 获取元数据属性的数量。 |
| [DataOffset](../../groupdocs.metadata.formats.video/movatom/dataoffset) { get; } | 获取数据偏移量。 |
| [DataSize](../../groupdocs.metadata.formats.video/movatom/datasize) { get; } | 以字节为单位获取数据大小。 |
| [HasExtendedSize](../../groupdocs.metadata.formats.video/movatom/hasextendedsize) { get; } | 获取一个值，该值指示扩展大小字段是否用于存储原子数据。 |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | 获取[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty)具有指定的名称。 |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | 获取元数据属性名称的集合。 |
| [LongSize](../../groupdocs.metadata.formats.video/movatom/longsize) { get; } | 以字节为单位获取原子大小。 |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | 获取元数据类型。 |
| [Offset](../../groupdocs.metadata.formats.video/movatom/offset) { get; } | 获取原子偏移量。 |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | 获取描述符集合，其中包含有关可通过 GroupDocs.Metadata 搜索引擎访问的属性的信息。 |
| [Size](../../groupdocs.metadata.formats.video/movatom/size) { get; } | 以字节为单位获取原子大小。 |
| [Type](../../groupdocs.metadata.formats.video/movatom/type) { get; } | 获取 4 字符类型。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 添加满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | 确定包是否包含具有指定名称的元数据属性。 |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | 查找满足指定谓词的元数据属性。 搜索是递归的，因此它也会影响所有嵌套包。 |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | 返回一个遍历集合的枚举器。 |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | 删除满足指定谓词的元数据属性。 |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | 从包中删除可写元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 设置满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 此方法是[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties)和[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) 如果现有属性满足谓词，则更新其值。 如果包中缺少满足谓词的已知属性，则将其添加到包中。 |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 更新满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |

### 评论

**学到更多**

* [使用 MOV 文件中的元数据](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+MOV+Files)

### 也可以看看

* class [CustomPackage](../../groupdocs.metadata.common/custompackage)
* 命名空间 [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* 部件 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->