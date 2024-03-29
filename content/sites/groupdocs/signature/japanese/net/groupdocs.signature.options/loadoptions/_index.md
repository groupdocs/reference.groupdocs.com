---
title: LoadOptions
second_title: GroupDocs.Signature for .NET API リファレンス
description: 署名するドキュメントを開くときに追加のオプション パスワードなど を指定できます
type: docs
weight: 1470
url: /ja/net/groupdocs.signature.options/loadoptions/
---
## LoadOptions class

署名するドキュメントを開くときに、追加のオプション (パスワードなど) を指定できます。

```csharp
public class LoadOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [LoadOptions](loadoptions)() | LoadOptions クラスの新しいインスタンスを初期化します。 |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [LoadExternalResources](../../groupdocs.signature.options/loadoptions/loadexternalresources) { get; set; } | 外部ドキュメント リソースをロードする必要があるかどうかを指定するオプションを取得または設定します。 このオプションを無効な値 (false) にすると、多数または大規模な外部リソース リンクを含むドキュメントのロード時間を節約できます。 デフォルト値は有効 (true) です。 |
| [Password](../../groupdocs.signature.options/loadoptions/password) { get; set; } | 保護されたドキュメントを開くためのパスワードを取得または設定します。 署名されたドキュメントを保護されたものとして保存するためにも使用されます。 |

### 関連項目

* 名前空間 [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* 組み立て [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
