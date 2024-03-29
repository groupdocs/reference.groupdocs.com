---
title: QrCodeVerifyOptions
second_title: GroupDocs.Signature for .NET API リファレンス
description: ドキュメントの QR コード署名を検証するオプションを保持します
type: docs
weight: 1640
url: /ja/net/groupdocs.signature.options/qrcodeverifyoptions/
---
## QrCodeVerifyOptions class

ドキュメントの QR コード署名を検証するオプションを保持します。

```csharp
public class QrCodeVerifyOptions : TextVerifyOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [QrCodeVerifyOptions](qrcodeverifyoptions#constructor)() | QR コード署名の検証オプション QrCodeVerifyOptions を作成します。 |
| [QrCodeVerifyOptions](qrcodeverifyoptions#constructor_1)(string) | 検証する QR コード テキストを含む QR コード署名の検証オプション QrCodeVerifyOptions を作成します。 |
| [QrCodeVerifyOptions](qrcodeverifyoptions#constructor_2)(string, QrCodeType) | 検証するテキストと QR-Code エンコード タイプを使用して、QR-Code 署名の検証オプション QrCodeVerifyOptions を作成します。 |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [AllPages](../../groupdocs.signature.options/verifyoptions/allpages) { get; set; } | 各文書ページを検証するためのフラグ。デフォルト値は true. です。 |
| [DataEncryption](../../groupdocs.signature.options/qrcodeverifyoptions/dataencryption) { get; set; } | の実装を取得または設定します[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption) QR コード署名テキスト プロパティをエンコードおよびデコードするためのインターフェイス. |
| [EncodeType](../../groupdocs.signature.options/qrcodeverifyoptions/encodetype) { get; set; } | QR コード タイプ検証を取得または設定します。このプロパティはオプションです. |
| [Extensions](../../groupdocs.signature.options/verifyoptions/extensions) { get; set; } | 代替署名オプションの検証のための追加の拡張機能. |
| [FormTextFieldTitle](../../groupdocs.signature.options/textverifyoptions/formtextfieldtitle) { get; set; } | 検証するフォーム フィールドのタイトルを取得または設定します。 このプロパティ セットのテキストは、テキスト フォーム フィールドでのみ検出される場合。 |
| [FormTextFieldType](../../groupdocs.signature.options/textverifyoptions/formtextfieldtype) { get; set; } | 確認するフォーム フィールドのタイプを取得または設定します。 このプロパティが設定されている場合、テキストはテキスト フォーム フィールドでのみ検出されます。 |
| [IsValid](../../groupdocs.signature.options/verifyoptions/isvalid) { get; } | 有効なプロパティ フラグ. |
| [MatchType](../../groupdocs.signature.options/textverifyoptions/matchtype) { get; set; } | テキスト一致タイプの検証を取得または設定します。 |
| virtual [PageNumber](../../groupdocs.signature.options/verifyoptions/pagenumber) { get; set; } | 検証するドキュメントのページ番号。プロパティが設定されていない場合 - ドキュメントのすべてのページが最初に出現したかどうかが検証されます. 最小値は 1. です |
| virtual [PagesSetup](../../groupdocs.signature.options/verifyoptions/pagessetup) { get; set; } | 検証するページを指定するページ オプション. |
| [SignatureID](../../groupdocs.signature.options/textverifyoptions/signatureid) { get; set; } | 検証する必要がある場合は、ゼロより大きいテキスト署名 ID を指定してください。このプロパティは、PDF ドキュメントのみでサポートされています |
| [SignatureImplementation](../../groupdocs.signature.options/textverifyoptions/signatureimplementation) { get; set; } | 検証する署名のタイプ. |
| [Text](../../groupdocs.signature.options/textverifyoptions/text) { get; set; } | 検証する必要がある場合は、署名テキストを指定します。 |

### 備考

**もっと詳しく知る**

* GroupDocs.SignatureによるQRコード電子署名の検証の基本的な使い方: [ドキュメント内の QR コード署名を eVerification する方法](https://docs.groupdocs.com/display/signaturenet/Verify+QR-code+signatures+in+the+document)
* GroupDocs.SignatureによるQRコード電子署名の検証設定の高度な使い方: [ドキュメントでの eVerification QR コード署名の高度な使用と追加設定](https://docs.groupdocs.com/display/signaturenet/Verify+QR-code+signatures)

### 関連項目

* class [TextVerifyOptions](../textverifyoptions)
* 名前空間 [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* 組み立て [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
