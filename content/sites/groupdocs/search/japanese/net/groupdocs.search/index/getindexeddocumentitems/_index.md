---
title: GetIndexedDocumentItems
second_title: GroupDocs.Search for .NET API リファレンス
description: 指定されたドキュメントのネストされたアイテムの配列を取得します ZIPOSTPST などのコンテナー ドキュメントの場合
type: docs
weight: 130
url: /ja/net/groupdocs.search/index/getindexeddocumentitems/
---
## Index.GetIndexedDocumentItems method

指定されたドキュメントのネストされたアイテムの配列を取得します (ZIP、OST、PST などのコンテナー ドキュメントの場合)。

```csharp
public DocumentInfo[] GetIndexedDocumentItems(DocumentInfo documentInfo)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| documentInfo | DocumentInfo | ドキュメント情報。 |

### 戻り値

ドキュメント項目の配列。

### 例

この例は、インデックスからインデックス付きドキュメントのアイテムのリストを取得する方法を示しています.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentsFolder = @"c:\MyDocuments\";
 
// 指定したフォルダにインデックスを作成
Index index = new Index(indexFolder);
 
// 指定されたフォルダからのドキュメントのインデックス作成
index.Add(documentsFolder);
 
// 索引付けされたドキュメントのリストを取得
DocumentInfo[] documents = index.GetIndexedDocuments();
for (int i = 0; i < documents.Length; i++)
{
    DocumentInfo document = documents[i];
    Console.WriteLine(document.FilePath);
    DocumentInfo[] items = index.GetIndexedDocumentItems(document); // ドキュメント項目のリストを取得
    for (int j = 0; j < items.Length; j++)
    {
        DocumentInfo item = items[j];
        Console.WriteLine("\t" + item.InnerPath);
    }
}
```

### 関連項目

* class [DocumentInfo](../../../groupdocs.search.results/documentinfo)
* class [Index](../../index)
* 名前空間 [GroupDocs.Search](../../index)
* 組み立て [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
