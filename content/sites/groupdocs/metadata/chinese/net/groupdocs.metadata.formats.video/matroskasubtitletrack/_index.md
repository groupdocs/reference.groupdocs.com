---
title: MatroskaSubtitleTrack
second_title: GroupDocs.Metadata for .NET API 参考
description: 表示 Matroska 视频中的字幕元数据
type: docs
weight: 2520
url: /zh/net/groupdocs.metadata.formats.video/matroskasubtitletrack/
---
## MatroskaSubtitleTrack class

表示 Matroska 视频中的字幕元数据。

```csharp
public class MatroskaSubtitleTrack : MatroskaTrack
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CodecID](../../groupdocs.metadata.formats.video/matroskatrack/codecid) { get; } | 获取codec对应的ID。 |
| [CodecName](../../groupdocs.metadata.formats.video/matroskatrack/codecname) { get; } | 获取指定编解码器的人类可读字符串。 |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | 获取元数据属性的数量。 |
| [DefaultDuration](../../groupdocs.metadata.formats.video/matroskatrack/defaultduration) { get; } | 获取纳秒数（不通过[`TimecodeScale`](../matroskasegment/timecodescale) 每帧. |
| [FlagEnabled](../../groupdocs.metadata.formats.video/matroskatrack/flagenabled) { get; } | 获取启用标志，如果轨道可用则为真。 |
| [Item](../../groupdocs.metadata.common/metadatapackage/item) { get; } | 获取[`MetadataProperty`](../../groupdocs.metadata.common/metadataproperty)具有指定名称. |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | 获取元数据属性名称的集合。 |
| [Language](../../groupdocs.metadata.formats.video/matroskatrack/language) { get; } | 获取 Matroska 语言形式的轨道语言。 如果[`LanguageIetf`](../matroskatrack/languageietf)Element用在同一个TrackEntry. |
| [LanguageIetf](../../groupdocs.metadata.formats.video/matroskatrack/languageietf) { get; } | 根据 BCP 47 并使用 IANA 语言子标签注册表获取轨道语言。 如果使用此元素，则任何[`Language`](../matroskatrack/language)必须忽略同一 TrackEntry 中使用的元素。 |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | 获取元数据类型。 |
| [Name](../../groupdocs.metadata.formats.video/matroskatrack/name) { get; } | 获取人类可读的曲目名称。 |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | 获取描述符集合，其中包含有关可通过 GroupDocs.Metadata 搜索引擎访问的属性的信息。 |
| [Subtitles](../../groupdocs.metadata.formats.video/matroskasubtitletrack/subtitles) { get; } | 获取字幕。 |
| [TrackNumber](../../groupdocs.metadata.formats.video/matroskatrack/tracknumber) { get; } | 获取块标头中使用的轨道编号。 不鼓励使用超过 127 个轨道，尽管设计允许数量不受限制。 |
| [TrackType](../../groupdocs.metadata.formats.video/matroskatrack/tracktype) { get; } | 获取轨道的类型。 |
| [TrackUid](../../groupdocs.metadata.formats.video/matroskatrack/trackuid) { get; } | 获取唯一 ID 以标识轨道。 在将轨道直接流复制到另一个文件时，应保持相同。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 添加满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | 确定包是否包含具有指定名称的元数据属性。 |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | 查找满足指定谓词的元数据属性。 搜索是递归的，因此它也会影响所有嵌套包。 |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | 返回一个遍历集合的枚举器。 |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | 删除满足指定谓词的元数据属性。 |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | 从包中删除可写元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 设置满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 此方法是以下方法的组合[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties)和[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) 如果现有属性满足谓词，则更新其值。 如果包中缺少满足谓词的已知属性，则将其添加到包中。 |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 更新满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |

### 评论

**了解更多**

* [使用 Matroska (MKV) 文件中的元数据](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+Matroska+%28MKV%29+files)

### 也可以看看

* class [MatroskaTrack](../matroskatrack)
* 命名空间 [GroupDocs.Metadata.Formats.Video](../../groupdocs.metadata.formats.video)
* 部件 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
