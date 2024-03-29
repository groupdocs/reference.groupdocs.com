---
title: EventHub
second_title: GroupDocs.Search for .NET API リファレンス
description: サブスクライブ用のインデックス イベントを提供します
type: docs
weight: 510
url: /ja/net/groupdocs.search.events/eventhub/
---
## EventHub class

サブスクライブ用のインデックス イベントを提供します。

```csharp
public class EventHub
```

## イベント

| 名前 | 説明 |
| --- | --- |
| event [ErrorOccurred](../../groupdocs.search.events/eventhub/erroroccurred) | インデックス操作中にエラーが発生した場合に発生します。 |
| event [FileIndexing](../../groupdocs.search.events/eventhub/fileindexing) | ドキュメントが索引付けされるときに発生します。 |
| event [ImagePreparing](../../groupdocs.search.events/eventhub/imagepreparing) | 画像が索引付けのために準備されるときに発生します。 |
| event [OperationFinished](../../groupdocs.search.events/eventhub/operationfinished) | インデックス操作が終了したときに発生します。 |
| event [OperationProgressChanged](../../groupdocs.search.events/eventhub/operationprogresschanged) | インデックス作成または更新操作の進行状況が変更されたときに発生します。 |
| event [PasswordRequired](../../groupdocs.search.events/eventhub/passwordrequired) | ドキュメントを開くためにパスワードが必要な場合に発生します。 |
| event [SearchPhaseCompleted](../../groupdocs.search.events/eventhub/searchphasecompleted) | 検索フェーズが完了すると発生します。 |
| event [StatusChanged](../../groupdocs.search.events/eventhub/statuschanged) | インデックスの状態が変化したときに発生します。 |

### 備考

**もっと詳しく知る**

* [検索インデックス イベント](https://docs.groupdocs.com/display/searchnet/Search+index+events)

### 例

この例は、インターフェイスの一般的な使用法を示しています.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
string query = "Einstein";

// インデックスを作成する
Index index = new Index(indexFolder);

// イベントへのサブスクライブ
index.Events.ErrorOccurred += (sender, args) =>
{
    Console.WriteLine(args.Message);
};

// 指定されたフォルダからのドキュメントのインデックス作成
index.Add(documentsFolder);

// インデックスで検索
SearchResult result = index.Search(query);
```

### 関連項目

* 名前空間 [GroupDocs.Search.Events](../../groupdocs.search.events)
* 組み立て [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
