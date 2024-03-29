---
title: CreateModificationTimeRange
second_title: GroupDocs.Search for .NET API リファレンス
description: 変更日が指定範囲外のドキュメントをスキップするためのフィルタを作成します
type: docs
weight: 110
url: /ja/net/groupdocs.search.options/documentfilter/createmodificationtimerange/
---
## DocumentFilter.CreateModificationTimeRange method

変更日が指定範囲外のドキュメントをスキップするためのフィルタを作成します。

```csharp
public static DocumentFilter CreateModificationTimeRange(DateTime lowerBound, DateTime upperBound)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| lowerBound | DateTime | ドキュメント変更時間の下限。 |
| upperBound | DateTime | ドキュメント変更時間の上限。 |

### 戻り値

ドキュメントの変更時間によるドキュメント フィルター。

### 関連項目

* class [DocumentFilter](../../documentfilter)
* 名前空間 [GroupDocs.Search.Options](../../documentfilter)
* 組み立て [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
