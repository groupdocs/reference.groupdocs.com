---
title: XmpGuid
second_title: GroupDocs.Metadata for .NET API 参考
description: 表示 XMP 全局唯一标识符
type: docs
weight: 3410
url: /zh/net/groupdocs.metadata.standards.xmp/xmpguid/
---
## XmpGuid class

表示 XMP 全局唯一标识符。

```csharp
public sealed class XmpGuid : XmpValueBase
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [XmpGuid](xmpguid#constructor)(Guid) | 初始化[`XmpGuid`](../xmpguid)类. |
| [XmpGuid](xmpguid#constructor_1)(string) | 初始化[`XmpGuid`](../xmpguid)类. |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [RawValue](../../groupdocs.metadata.common/propertyvalue/rawvalue) { get; } | 获取原始值。 |
| [Type](../../groupdocs.metadata.common/propertyvalue/type) { get; } | 获取[`MetadataPropertyType`](../../groupdocs.metadata.common/metadatapropertytype). |
| [Value](../../groupdocs.metadata.standards.xmp/xmpguid/value) { get; } | 获取值。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [AcceptValue](../../groupdocs.metadata.common/propertyvalue/acceptvalue)(ValueAcceptor) | 使用自定义提取属性值[`ValueAcceptor`](../../groupdocs.metadata.common/valueacceptor). |
| override [GetXmpRepresentation](../../groupdocs.metadata.standards.xmp/xmpguid/getxmprepresentation)() | 以 XMP 格式返回包含字符串的值。 |
| [ToArray&lt;TElement&gt;](../../groupdocs.metadata.common/propertyvalue/toarray)() | 将属性值转换为指定类型的数组。 |
| [ToClass&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/toclass)() | 将属性值转换为引用类型。 |
| override [ToString](../../groupdocs.metadata.standards.xmp/xmpvaluebase/tostring)() | 返回一个表示属性值的字符串。 |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)() | 将属性值转换为值类型。 |
| [ToStruct&lt;T&gt;](../../groupdocs.metadata.common/propertyvalue/tostruct)(T) | 将属性值转换为值类型。 |

### 也可以看看

* class [XmpValueBase](../xmpvaluebase)
* 命名空间 [GroupDocs.Metadata.Standards.Xmp](../../groupdocs.metadata.standards.xmp)
* 部件 [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->