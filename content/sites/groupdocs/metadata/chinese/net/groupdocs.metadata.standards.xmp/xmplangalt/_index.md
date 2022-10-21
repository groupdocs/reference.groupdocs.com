---
title: XmpLangAlt
second_title: GroupDocs.Metadata for .NET API 参考
description: 代表 XMP 语言替代
type: docs
weight: 3450
url: /zh/net/groupdocs.metadata.standards.xmp/xmplangalt/
---
## XmpLangAlt class

代表 XMP 语言替代。

简单文本项的替代数组。语言备选方案有助于基于所需语言选择简单的文本 item 。每个数组项都应有一个 xml:lang 限定符。每个 xml:lang 值在项目中应该是 唯一的。

```csharp
public sealed class XmpLangAlt : XmpArray
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [XmpLangAlt](xmplangalt#constructor)(IDictionary&lt;string, string&gt;) | 初始化[`XmpLangAlt`](../xmplangalt)类. |
| [XmpLangAlt](xmplangalt#constructor_1)(string) | 初始化[`XmpLangAlt`](../xmplangalt)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [ArrayType](../../groupdocs.metadata.standards.xmp/xmparray/arraytype) { get; } | 获取 XMP 数组的类型。 |
| [Item](../../groupdocs.metadata.standards.xmp/xmplangalt/item) { get; } | 获取与指定语言关联的值。 |
| [Languages](../../groupdocs.metadata.standards.xmp/xmplangalt/languages) { get; } | 获取在实例中注册的所有语言的数组[`XmpLangAlt`](../xmplangalt). |
| [RawValue](../../groupdocs.metadata.common/propertyvalue/rawvalue) { get; } | 获取原始值。 |
| [Type](../../groupdocs.metadata.common/propertyvalue/type) { get; } | 获取[`MetadataPropertyType`](../../groupdocs.metadata.common/metadatapropertytype). |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [AcceptValue](../../groupdocs.metadata.common/propertyvalue/acceptvalue)(ValueAcceptor) | 使用自定义提取属性值[`ValueAcceptor`](../../groupdocs.metadata.common/valueacceptor). |
| [Contains](../../groupdocs.metadata.standards.xmp/xmplangalt/contains)(string) | 确定是否[`XmpLangAlt`](../xmplangalt)包含指定的语言。 |
| override [GetXmpRepresentation](../../groupdocs.metadata.standards.xmp/xmplangalt/getxmprepresentation)() | 将 XMP 值转换为 xml 表示形式。 |
| [ToArray&lt;TElement&gt;](../../groupdocs.metadata.common/propertyvalue/toarray)() | 将属性值转换为指定类型的数组。 |
| [ToClass&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/toclass)() | 将属性值转换为引用类型。 |
| [ToPlatformArray&lt;T&gt;](../../groupdocs.metadata.standards.xmp/xmparray/toplatformarray)() | 转换[`XmpArray`](../xmparray)到特定于平台的数组。 |
| override [ToString](../../groupdocs.metadata.standards.xmp/xmpvaluebase/tostring)() | 返回一个表示属性值的字符串。 |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)() | 将属性值转换为值类型。 |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)(T) | 将属性值转换为值类型。 |

### 也可以看看

* class [XmpArray](../xmparray)
* 命名空间 [GroupDocs.Metadata.Standards.Xmp](../../groupdocs.metadata.standards.xmp)
* 部件 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->