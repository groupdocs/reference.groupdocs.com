---
title: TextSignature
second_title: GroupDocs.Signature for .NET API 参考
description: 包含文本签名属性
type: docs
weight: 970
url: /zh/net/groupdocs.signature.domain/textsignature/
---
## TextSignature class

包含文本签名属性。

```csharp
public class TextSignature : BaseSignature
```

## 构造函数

| 姓名 | 描述 |
| --- | --- |
| [TextSignature](textsignature)(string) | 使用搜索过程后获得的签名标识符初始化 TextSignature 对象。 此唯一标识符用于从文档签名信息层查找此签名的其他属性。 |

## 特性

| 姓名 | 描述 |
| --- | --- |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | 获取或设置签名创建日期。 |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | 获取指示此签名是否已从文档中删除的标志。 此属性仅用于文档历史日志记录，以保留已删除签名的列表。 |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | 指定签名的高度。 |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | 获取或设置标志以指示此组件是签名还是文档内容。 此属性与 Update 方法一起使用以将元素设置为签名 (true) 或文档元素 (false)。 |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | 指定签名的左侧位置。 |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | 获取或设置签名修改日期 |
| [Native](../../groupdocs.signature.domain/textsignature/native) { get; set; } | 指定本机属性。如果签名是特定于文档的，则为真。 |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | 指定页面签名位于。 |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | 通过更新或删除方法修改文档中签名的唯一签名标识符。 在调用签名或搜索方法后将自动设置此属性。 如果此属性在手动设置以操作签名之前保存。 |
| [SignatureImplementation](../../groupdocs.signature.domain/textsignature/signatureimplementation) { get; } | 指定文本签名实现。 |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | 指定签名的类型。 |
| [Text](../../groupdocs.signature.domain/textsignature/text) { get; set; } | 指定签名中的文本。 |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | 指定签名的顶部位置。 |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | 指定签名的宽度。 |

## 方法

| 姓名 | 描述 |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/textsignature/clone)() | 克隆文本签名实例。 |
| override [Equals](../../groupdocs.signature.domain/textsignature/equals)(object) | 覆盖 Equals 方法以比较签名属性 |
| override [GetHashCode](../../groupdocs.signature.domain/textsignature/gethashcode)() | 覆盖 GetHashCode 方法 |

### 也可以看看

* class [BaseSignature](../basesignature)
* 命名空间 [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* 部件 [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->