---
title: ImageMetadataSignature
second_title: GroupDocs.Signature for .NET API 参考
description: 包含图像元数据签名属性
type: docs
weight: 570
url: /zh/net/groupdocs.signature.domain/imagemetadatasignature/
---
## ImageMetadataSignature class

包含图像元数据签名属性。

```csharp
public sealed class ImageMetadataSignature : MetadataSignature
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [ImageMetadataSignature](imagemetadatasignature)(ushort, object) | 使用 Id 和 value 创建图像元数据签名 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | 获取或设置签名创建日期。 |
| [DataEncryption](../../groupdocs.signature.domain/metadatasignature/dataencryption) { get; set; } | 获取或设置的实现[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption)编码和解码签名值属性的接口。 |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | 获取指示此签名是否已从文档中删除的标志。 此属性仅用于文档历史日志记录以保留已删除签名的列表。 |
| [Description](../../groupdocs.signature.domain/imagemetadatasignature/description) { get; } | 用于获取标准图像元数据签名 描述的只读值 |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | 指定签名高度。 |
| [Id](../../groupdocs.signature.domain/imagemetadatasignature/id) { get; set; } | Image Metadata 签名的标识符。 见ImageMetadataSignatures包含具有预定义 Id 值的标准签名的类。 |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | 获取或设置标志以指示此组件是签名还是文档内容。 此属性与 Update 方法一起使用以将元素设置为签名 (true) 或文档元素 (false)。 |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | 指定签名的左侧位置。 |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | 获取或设置签名修改日期。 |
| [Name](../../groupdocs.signature.domain/metadatasignature/name) { get; set; } | 指定唯一的元数据名称。 |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | 指定找到的页面签名。 |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | 用于通过 Update 或 Delete 方法修改文档中签名的唯一签名标识符。 此属性将在调用 Sign 或 Search 方法后自动设置。 如果此属性在可以手动设置之前保存以操作签名。 |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | 指定签名类型。 |
| [Size](../../groupdocs.signature.domain/imagemetadatasignature/size) { get; } | 获取元数据值大小的只读值 value |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | 指定签名的顶部位置。 |
| [Type](../../groupdocs.signature.domain/metadatasignature/type) { get; } | 指定元数据值类型。 |
| [Value](../../groupdocs.signature.domain/metadatasignature/value) { get; set; } | 指定元数据对象。 |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | 指定签名宽度。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/imagemetadatasignature/clone#clone_1)() | 克隆元数据签名实例。 |
| override [Clone](../../groupdocs.signature.domain/imagemetadatasignature/clone#clone)(object) | 克隆具有给定值的图像元数据签名实例。 |
| override [Equals](../../groupdocs.signature.domain/imagemetadatasignature/equals)(object) | 覆盖 Equals 方法以比较签名属性 |
| [GetData&lt;T&gt;](../../groupdocs.signature.domain/metadatasignature/getdata)() | 通过反序列化从元数据签名值中获取对象。 |
| [GetData&lt;T&gt;](../../groupdocs.signature.domain/metadatasignature/getdata)(IDataEncryption) | 通过反序列化从元数据签名文本中获取对象。 |
| override [GetHashCode](../../groupdocs.signature.domain/imagemetadatasignature/gethashcode)() | 覆盖 GetHashCode 方法 |
| override [ToBoolean](../../groupdocs.signature.domain/imagemetadatasignature/toboolean)() | 转换为布尔值。 |
| override [ToDateTime](../../groupdocs.signature.domain/imagemetadatasignature/todatetime#todatetime)() | 转换为 DateTime. |
| override [ToDateTime](../../groupdocs.signature.domain/imagemetadatasignature/todatetime#todatetime_1)(IFormatProvider) | 转换为 DateTime. |
| override [ToDecimal](../../groupdocs.signature.domain/imagemetadatasignature/todecimal#todecimal)() | 转换为十进制。 |
| override [ToDecimal](../../groupdocs.signature.domain/imagemetadatasignature/todecimal#todecimal_1)(IFormatProvider) | 转换为十进制。 |
| override [ToDouble](../../groupdocs.signature.domain/imagemetadatasignature/todouble#todouble)() | 转换为 Double. |
| override [ToDouble](../../groupdocs.signature.domain/imagemetadatasignature/todouble#todouble_1)(IFormatProvider) | 转换为 Double. |
| override [ToInteger](../../groupdocs.signature.domain/imagemetadatasignature/tointeger)() | 转换为整数。 |
| [ToLong](../../groupdocs.signature.domain/imagemetadatasignature/tolong)() | 转换为 long. |
| override [ToSingle](../../groupdocs.signature.domain/imagemetadatasignature/tosingle#tosingle)() | 转换为 float. |
| override [ToSingle](../../groupdocs.signature.domain/imagemetadatasignature/tosingle#tosingle_1)(IFormatProvider) | 转换为 float. |
| override [ToString](../../groupdocs.signature.domain/imagemetadatasignature/tostring#tostring)() | 使用覆盖 ToString() 方法转换为字符串 |
| override [ToString](../../groupdocs.signature.domain/imagemetadatasignature/tostring#tostring_1)(string) | 转换为具有指定格式的字符串 |
| override [ToString](../../groupdocs.signature.domain/imagemetadatasignature/tostring#tostring_2)(string, IFormatProvider) | 转换为具有指定格式的字符串 |

### 也可以看看

* class [MetadataSignature](../metadatasignature)
* 命名空间 [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* 部件 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
