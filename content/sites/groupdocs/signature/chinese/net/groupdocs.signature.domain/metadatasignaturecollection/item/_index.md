---
title: Item
second_title: GroupDocs.Signature for .NET API 参考
description: 按属性名称返回 MetadataSignature 对象
type: docs
weight: 30
url: /zh/net/groupdocs.signature.domain/metadatasignaturecollection/item/
---
## MetadataSignatureCollection indexer (1 of 2)

按属性名称返回 MetadataSignature 对象。

```csharp
public MetadataSignature this[string name] { get; }
```

| 范围 | 描述 |
| --- | --- |
| name | 要检索的属性的不区分大小写的名称。 |

### 返回值

返回元数据签名[`MetadataSignature`](../../metadatasignature)对象的属性名称。

### 评论

如果未找到具有指定名称的属性，则返回 null。

### 也可以看看

* class [MetadataSignature](../../metadatasignature)
* class [MetadataSignatureCollection](../../metadatasignaturecollection)
* 命名空间 [GroupDocs.Signature.Domain](../../metadatasignaturecollection)
* 部件 [GroupDocs.Signature](../../../)

---

## MetadataSignatureCollection indexer (2 of 2)

按索引返回一个 MetadataSignature 对象。

```csharp
public MetadataSignature this[int index] { get; }
```

| 范围 | 描述 |
| --- | --- |
| index | 要检索的 MetadataSignature 的从零开始的索引。 |

### 返回值

返回元数据签名[`MetadataSignature`](../../metadatasignature)按集合索引的对象。

### 评论

如果具有指定索引的属性不存在，则返回 null。

### 也可以看看

* class [MetadataSignature](../../metadatasignature)
* class [MetadataSignatureCollection](../../metadatasignaturecollection)
* 命名空间 [GroupDocs.Signature.Domain](../../metadatasignaturecollection)
* 部件 [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
