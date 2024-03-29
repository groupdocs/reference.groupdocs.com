---
title: GroupDocs.Redaction.Integration
second_title: GroupDocs.Redaction for .NET API リファレンス
description: Integration名前空間はさまざまな形式のドキュメントを GroupDocs.Redaction. と統合するために使用されるインターフェイスとクラスを提供します
type: docs
weight: 40
url: /ja/net/groupdocs.redaction.integration/
---
Integration名前空間は、さまざまな形式のドキュメントを GroupDocs.Redaction. と統合するために使用されるインターフェイスとクラスを提供します。

## クラス

| クラス | 説明 |
| --- | --- |
| [DocumentFormatInstance](./documentformatinstance) | ドキュメントの特定の形式を表します。このクラスを実装して、独自のドキュメント タイプを追加します。 |
| [MetadataCollection](./metadatacollection) | の辞書を表します[`MetadataItem`](../groupdocs.redaction.integration/metadataitem)タイトルをキーに. |
| [MetadataItem](./metadataitem) | サポートされているすべての形式に共通で、メタデータのリダクションで使用されるメタデータのアイテムを表します。 |
## インターフェース

| インターフェース | 説明 |
| --- | --- |
| [IAnnotatedDocument](./iannotateddocument) | コメントなどの注釈へのアクセスに必要なメソッドを定義します。によって実装する必要があります[`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance)アノテーションのリダクションを実行する派生クラス。 |
| [ICellularFormatInstance](./icellularformatinstance) | 1 つまたは複数のワークシートを持つスプレッドシート形式へのアクセスに必要なメソッドを定義します。 |
| [IImageFormatInstance](./iimageformatinstance) | ラスター イメージ形式のリダクションに必要なメソッドを定義します。 |
| [IMetadataAccess](./imetadataaccess) | フォーマットがサポートしている場合、ドキュメントのメタデータへのアクセスに必要なメソッドを定義します. |
| [IPaginatedDocument](./ipaginateddocument) | ドキュメントのページを操作するために必要なメソッドを定義します。によって実装する必要があります[`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance)ページのリダクションを実行する派生クラス。 |
| [IPreviewable](./ipreviewable) | ドキュメントのプレビューを作成するメソッドを定義します. |
| [IRasterizableDocument](./irasterizabledocument) | ドキュメントを任意のバイナリ形式で保存するために必要なメソッドを定義します。組み込み型は、ページの画像を含む PDF としてドキュメントを保存します。 |
| [ITextualFormatInstance](./itextualformatinstance) | テキストを含むドキュメント内のテキスト データを編集するために必要なメソッドを定義します。 |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
