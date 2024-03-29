---
title: TxtLoadOptions
second_title: GroupDocs.Conversion for .NET API リファレンス
description: Txt ドキュメントをロードするためのオプション
type: docs
weight: 2300
url: /ja/net/groupdocs.conversion.options.load/txtloadoptions/
---
## TxtLoadOptions class

Txt ドキュメントをロードするためのオプション。

```csharp
public sealed class TxtLoadOptions : LoadOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [TxtLoadOptions](txtloadoptions)() | の新しいインスタンスを初期化します[`TxtLoadOptions`](../txtloadoptions)class. |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [DetectNumberingWithWhitespaces](../../groupdocs.conversion.options.load/txtloadoptions/detectnumberingwithwhitespaces) { get; set; } | プレーン テキスト ドキュメントの変換時に番号付きリスト アイテムを認識する方法を指定できます。 デフォルト値は true です。 |
| [Encoding](../../groupdocs.conversion.options.load/txtloadoptions/encoding) { get; set; } | Txt ドキュメントをロードするときに使用されるエンコーディングを取得または設定します。 null にすることができます。デフォルトは null. です。 |
| [Format](../../groupdocs.conversion.options.load/txtloadoptions/format) { get; } | 入力ドキュメントのファイル形式. (2 properties) |
| [LeadingSpacesOptions](../../groupdocs.conversion.options.load/txtloadoptions/leadingspacesoptions) { get; set; } | 先行スペース処理の優先オプションを取得または設定します。 デフォルト値は[`ConvertToIndent`](../txtleadingspacesoptions/converttoindent). |
| [TrailingSpacesOptions](../../groupdocs.conversion.options.load/txtloadoptions/trailingspacesoptions) { get; set; } | 末尾のスペース処理の優先オプションを取得または設定します。 デフォルト値は[`Trim`](../txttrailingspacesoptions/trim). |

## メソッド

| 名前 | 説明 |
| --- | --- |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | 2 つのオブジェクト インスタンスが等しいかどうかを判断します。 |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | 2 つのオブジェクト インスタンスが等しいかどうかを判断します。 |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | デフォルトのハッシュ関数として機能します。 |

### 関連項目

* class [LoadOptions](../loadoptions)
* 名前空間 [GroupDocs.Conversion.Options.Load](../../groupdocs.conversion.options.load)
* 組み立て [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
