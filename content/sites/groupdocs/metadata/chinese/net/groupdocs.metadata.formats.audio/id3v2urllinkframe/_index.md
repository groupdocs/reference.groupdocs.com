---
title: ID3V2UrlLinkFrame
second_title: GroupDocs.Metadata for .NET API 参考
description: 表示一个 URL 链接框架ID3V2Tag./id3v2tag.框架名称始终以 W 字符开头
type: docs
weight: 530
url: /zh/net/groupdocs.metadata.formats.audio/id3v2urllinkframe/
---
## ID3V2UrlLinkFrame class

表示一个 URL 链接框架[`ID3V2Tag`](../id3v2tag).框架名称始终以 W 字符开头。

```csharp
public sealed class ID3V2UrlLinkFrame : ID3V2TagFrame
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [ID3V2UrlLinkFrame](id3v2urllinkframe)(string, string) | 初始化[`ID3V2UrlLinkFrame`](../id3v2urllinkframe)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | 获取元数据属性的数量。 |
| [Data](../../groupdocs.metadata.formats.audio/id3v2tagframe/data) { get; } | 获取帧数据。 |
| [Flags](../../groupdocs.metadata.formats.audio/id3v2tagframe/flags) { get; } | 获取帧标志。 |
| [Id](../../groupdocs.metadata.formats.audio/id3v2tagframe/id) { get; } | 获取框架的 id（四个字符匹配模式 [A-Z0-9]）。 |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | 获取[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty)具有指定的名称。 |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | 获取元数据属性名称的集合。 |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | 获取元数据类型。 |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | 获取描述符集合，其中包含有关可通过 GroupDocs.Metadata 搜索引擎访问的属性的信息。 |
| [Url](../../groupdocs.metadata.formats.audio/id3v2urllinkframe/url) { get; } | 获取 URL 值。 |

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

* [处理 ID3v2 标签](https://docs.groupdocs.com/display/metadatanet/Handling+the+ID3v2+tag)

### 也可以看看

* class [ID3V2TagFrame](../id3v2tagframe)
* 命名空间 [GroupDocs.Metadata.Formats.Audio](../../groupdocs.metadata.formats.audio)
* 部件 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->