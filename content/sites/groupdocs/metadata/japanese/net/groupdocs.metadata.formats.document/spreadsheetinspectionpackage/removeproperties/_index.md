---
title: RemoveProperties
second_title: GroupDocs.Metadata for .NET API リファレンス
description: 指定された述語を満たすメタデータ プロパティを削除します
type: docs
weight: 70
url: /ja/net/groupdocs.metadata.formats.document/spreadsheetinspectionpackage/removeproperties/
---
## SpreadsheetInspectionPackage.RemoveProperties method

指定された述語を満たすメタデータ プロパティを削除します。

```csharp
public override int RemoveProperties(Func<MetadataProperty, bool> predicate)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| predicate | Func`2 | 条件の各メタデータ プロパティをテストする関数。 |

### 戻り値

影響を受けるプロパティの数。

### 関連項目

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [SpreadsheetInspectionPackage](../../spreadsheetinspectionpackage)
* 名前空間 [GroupDocs.Metadata.Formats.Document](../../spreadsheetinspectionpackage)
* 組み立て [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
