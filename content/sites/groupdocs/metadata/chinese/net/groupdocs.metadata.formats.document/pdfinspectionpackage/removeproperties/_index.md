---
title: RemoveProperties
second_title: GroupDocs.Metadata for .NET API 参考
description: 删除满足指定谓词的元数据属性
type: docs
weight: 110
url: /zh/net/groupdocs.metadata.formats.document/pdfinspectionpackage/removeproperties/
---
## PdfInspectionPackage.RemoveProperties method

删除满足指定谓词的元数据属性。

```csharp
public override int RemoveProperties(Func<MetadataProperty, bool> predicate)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| predicate | Func`2 | 用于测试条件的每个元数据属性的函数。 |

### 返回值

受影响的属性的数量。

### 也可以看看

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [PdfInspectionPackage](../../pdfinspectionpackage)
* 命名空间 [GroupDocs.Metadata.Formats.Document](../../pdfinspectionpackage)
* 部件 [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
