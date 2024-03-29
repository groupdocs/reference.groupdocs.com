---
title: TextOptions
second_title: GroupDocs.Search for .NET API リファレンス
description: インデックスからドキュメント テキストを取得するためのオプションを提供します
type: docs
weight: 1100
url: /ja/net/groupdocs.search.options/textoptions/
---
## TextOptions class

インデックスからドキュメント テキストを取得するためのオプションを提供します。

```csharp
public class TextOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [TextOptions](textoptions)() | の新しいインスタンスを初期化します[`TextOptions`](../textoptions)class. |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [AdditionalFields](../../groupdocs.search.options/textoptions/additionalfields) { get; set; } | インデックス作成に使用された追加のドキュメント フィールドを取得または設定します。 デフォルト値は`ヌル`. この値は、ドキュメントのテキストがインデックスに保存されていない場合にのみ使用されることに注意してください. |
| [Cancellation](../../groupdocs.search.options/textoptions/cancellation) { get; set; } | キャンセル オブジェクトを取得または設定します。 デフォルト値は`ヌル`. |
| [CustomExtractor](../../groupdocs.search.options/textoptions/customextractor) { get; set; } | インデックス作成に使用されたカスタム テキスト エクストラクタを取得または設定します。 デフォルト値は`ヌル`. この値は、ドキュメントのテキストがインデックスに保存されていない場合にのみ使用されることに注意してください. |
| [GenerateHead](../../groupdocs.search.options/textoptions/generatehead) { get; set; } | 出力 HTML で Head タグが生成されるかどうかを示す値を取得または設定します。 デフォルト値は`真実`. |
| [ImageIndexingOptions](../../groupdocs.search.options/textoptions/imageindexingoptions) { get; } | 画像逆検索の画像インデックス オプションを取得します。 |
| [MetadataIndexingOptions](../../groupdocs.search.options/textoptions/metadataindexingoptions) { get; } | メタデータ フィールドのインデックス作成のオプションを取得します。 |
| [OcrIndexingOptions](../../groupdocs.search.options/textoptions/ocrindexingoptions) { get; } | OCR 処理と認識されたテキストのインデックス作成のオプションを取得します。 |

### 備考

**もっと詳しく知る**

* [インデックス付きドキュメントの取得](https://docs.groupdocs.com/display/searchnet/Getting+indexed+documents)
* [検索結果のハイライト](https://docs.groupdocs.com/display/searchnet/Highlighting+search+results)

### 関連項目

* 名前空間 [GroupDocs.Search.Options](../../groupdocs.search.options)
* 組み立て [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
