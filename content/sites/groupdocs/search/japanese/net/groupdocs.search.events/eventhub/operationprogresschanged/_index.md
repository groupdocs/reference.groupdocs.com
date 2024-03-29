---
title: OperationProgressChanged
second_title: GroupDocs.Search for .NET API リファレンス
description: インデックス作成または更新操作の進行状況が変更されたときに発生します
type: docs
weight: 50
url: /ja/net/groupdocs.search.events/eventhub/operationprogresschanged/
---
## EventHub.OperationProgressChanged event

インデックス作成または更新操作の進行状況が変更されたときに発生します。

```csharp
public event EventHandler<OperationProgressEventArgs> OperationProgressChanged;
```

### 例

この例は、イベントの使用方法を示しています。

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";

// インデックスを作成する
Index index = new Index(indexFolder);

// イベントへのサブスクライブ
index.Events.OperationProgressChanged += (sender, args) =>
{
    Console.WriteLine("Last processed: " + args.LastDocumentPath);
    Console.WriteLine("Result: " + args.LastDocumentStatus);
    Console.WriteLine("Processed documents: " + args.TotalDocuments);
    Console.WriteLine("Progress percentage: " + args.ProgressPercentage);
};

// 指定されたフォルダからのドキュメントのインデックス作成
index.Add(documentsFolder);
```

### 関連項目

* class [OperationProgressEventArgs](../../operationprogresseventargs)
* class [EventHub](../../eventhub)
* 名前空間 [GroupDocs.Search.Events](../../eventhub)
* 組み立て [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
