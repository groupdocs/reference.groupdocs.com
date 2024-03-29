---
title: NsfLoadOptions
second_title: GroupDocs.Conversion for .NET API リファレンス
description: Nsf ドキュメントをロードするためのオプション
type: docs
weight: 2200
url: /ja/net/groupdocs.conversion.options.load/nsfloadoptions/
---
## NsfLoadOptions class

Nsf ドキュメントをロードするためのオプション。

```csharp
public sealed class NsfLoadOptions : LoadOptions, IDocumentsContainerLoadOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [NsfLoadOptions](nsfloadoptions)() | の新しいインスタンスを初期化します[`NsfLoadOptions`](../nsfloadoptions)class. |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [ConvertOwned](../../groupdocs.conversion.options.load/nsfloadoptions/convertowned) { get; } | ドキュメント コンテナ内の所有ドキュメントを変換する必要があるかどうかを制御するオプション |
| [ConvertOwner](../../groupdocs.conversion.options.load/nsfloadoptions/convertowner) { get; } | ドキュメント コンテナ自体を変換する必要があるかどうかを制御するオプション このプロパティが true の場合、ドキュメント コンテナは最初に変換されたドキュメントになります |
| [Depth](../../groupdocs.conversion.options.load/nsfloadoptions/depth) { get; set; } | 変換を実行する深さのレベル数を制御するオプション |
| [Format](../../groupdocs.conversion.options.load/loadoptions/format) { get; } | 入力ドキュメントのファイル形式. |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [Clone](../../groupdocs.conversion.options.load/nsfloadoptions/clone)() | 現在のインスタンスを複製します。 |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | 2 つのオブジェクト インスタンスが等しいかどうかを判断します。 |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | 2 つのオブジェクト インスタンスが等しいかどうかを判断します。 |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | デフォルトのハッシュ関数として機能します。 |

### 関連項目

* class [LoadOptions](../loadoptions)
* interface [IDocumentsContainerLoadOptions](../../groupdocs.conversion.contracts/idocumentscontainerloadoptions)
* 名前空間 [GroupDocs.Conversion.Options.Load](../../groupdocs.conversion.options.load)
* 組み立て [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
