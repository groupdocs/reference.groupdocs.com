---
title: CanonMakerNotePackage
second_title: GroupDocs.Metadata for .NET API 参考
description: 表示 CANON MakerNote 元数据
type: docs
weight: 2820
url: /zh/net/groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/
---
## CanonMakerNotePackage class

表示 CANON MakerNote 元数据。

```csharp
public sealed class CanonMakerNotePackage : MakerNotePackage
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CameraSettings](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/camerasettings) { get; } | 获取相机设置。 |
| [CanonFileLength](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/canonfilelength) { get; } | 获取佳能文件的长度。 |
| [CanonFirmwareVersion](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/canonfirmwareversion) { get; } | 获取佳能固件版本。 |
| [CanonImageType](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/canonimagetype) { get; } | 获取佳能图像类型。 |
| [CanonModelID](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/canonmodelid) { get; } | 获取佳能型号标识符。 |
| [Count](../../groupdocs.metadata.common/metadatapackage/count) { get; } | 获取元数据属性的数量。 |
| [FileNumber](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/filenumber) { get; } | 获取文件编号。 |
| [Item](../../groupdocs.metadata.standards.exif/exifdictionarybasepackage/item) { get; } | 获取指定id的TIFF标签。 (2 indexers) |
| [Keys](../../groupdocs.metadata.common/metadatapackage/keys) { get; } | 获取元数据属性名称的集合。 |
| [MetadataType](../../groupdocs.metadata.common/metadatapackage/metadatatype) { get; } | 获取元数据类型。 |
| [OwnerName](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/ownername) { get; } | 获取所有者的名称。 |
| [PropertyDescriptors](../../groupdocs.metadata.common/metadatapackage/propertydescriptors) { get; } | 获取描述符集合，其中包含有关可通过 GroupDocs.Metadata 搜索引擎访问的属性的信息。 |
| [SerialNumber](../../groupdocs.metadata.standards.exif.makernote/canonmakernotepackage/serialnumber) { get; } | 获取序列号。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [AddProperties](../../groupdocs.metadata.common/metadatapackage/addproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 添加满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |
| [Clear](../../groupdocs.metadata.standards.exif/exifdictionarybasepackage/clear)() | 删除存储在包中的所有 TIFF 标签。 |
| [Contains](../../groupdocs.metadata.common/metadatapackage/contains)(string) | 确定包是否包含具有指定名称的元数据属性。 |
| virtual [FindProperties](../../groupdocs.metadata.common/metadatapackage/findproperties)(Func&lt;MetadataProperty, bool&gt;) | 查找满足指定谓词的元数据属性。 搜索是递归的，因此它也会影响所有嵌套包。 |
| [GetEnumerator](../../groupdocs.metadata.common/metadatapackage/getenumerator)() | 返回一个遍历集合的枚举器。 |
| [Remove](../../groupdocs.metadata.standards.exif/exifdictionarybasepackage/remove)(TiffTagID) | 删除具有指定 id 的属性。 |
| virtual [RemoveProperties](../../groupdocs.metadata.common/metadatapackage/removeproperties)(Func&lt;MetadataProperty, bool&gt;) | 删除满足指定谓词的元数据属性。 |
| virtual [Sanitize](../../groupdocs.metadata.common/metadatapackage/sanitize)() | 从包中删除可写元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |
| [Set](../../groupdocs.metadata.standards.exif/exifdictionarybasepackage/set)(TiffTag) | 添加或替换指定的标记。 |
| [SetProperties](../../groupdocs.metadata.common/metadatapackage/setproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 设置满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 此方法是以下方法的组合[`AddProperties`](../../groupdocs.metadata.common/metadatapackage/addproperties)和[`UpdateProperties`](../../groupdocs.metadata.common/metadatapackage/updateproperties) 如果现有属性满足谓词，则更新其值。 如果包中缺少满足谓词的已知属性，则将其添加到包中。 |
| [ToList](../../groupdocs.metadata.standards.exif/exifdictionarybasepackage/tolist)() | 从包中创建一个列表。 |
| [UpdateProperties](../../groupdocs.metadata.common/metadatapackage/updateproperties)(Func&lt;MetadataProperty, bool&gt;, PropertyValue) | 更新满足指定谓词的已知元数据属性。 该操作是递归的，因此它也会影响所有嵌套包。 |

### 也可以看看

* class [MakerNotePackage](../makernotepackage)
* 命名空间 [GroupDocs.Metadata.Standards.Exif.MakerNote](../../groupdocs.metadata.standards.exif.makernote)
* 部件 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
