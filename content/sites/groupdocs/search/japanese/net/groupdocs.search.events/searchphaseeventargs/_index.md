---
title: SearchPhaseEventArgs
second_title: GroupDocs.Search for .NET API リファレンス
description: 検索フェーズ変更イベントの引数を表します
type: docs
weight: 600
url: /ja/net/groupdocs.search.events/searchphaseeventargs/
---
## SearchPhaseEventArgs class

検索フェーズ変更イベントの引数を表します。

```csharp
public class SearchPhaseEventArgs : BaseIndexEventArgs
```

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [IndexFolder](../../groupdocs.search.events/baseindexeventargs/indexfolder) { get; } | インデックス フォルダーを取得します。 |
| [IndexId](../../groupdocs.search.events/baseindexeventargs/indexid) { get; } | インデックス ID を取得します。 |
| [Query](../../groupdocs.search.events/searchphaseeventargs/query) { get; } | 現在の検索の最初のクエリを取得します。 |
| [SearchPhase](../../groupdocs.search.events/searchphaseeventargs/searchphase) { get; } | 検索フェーズを取得します。 |
| [Status](../../groupdocs.search.events/baseindexeventargs/status) { get; } | インデックスの状態を取得します。 |
| [Time](../../groupdocs.search.events/baseindexeventargs/time) { get; } | イベントの時刻を取得します。 |
| [Words](../../groupdocs.search.events/searchphaseeventargs/words) { get; } | 現在のフェーズで取得した単語を取得します。 |

### 備考

**もっと詳しく知る**

* [検索インデックス イベント](https://docs.groupdocs.com/display/searchnet/Search+index+events)

### 関連項目

* class [BaseIndexEventArgs](../baseindexeventargs)
* 名前空間 [GroupDocs.Search.Events](../../groupdocs.search.events)
* 組み立て [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
