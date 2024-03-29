---
title: PdfDigitalSignatureAppearance
second_title: GroupDocs.Signature for .NET API リファレンス
description: PDF ドキュメント上のデジタル署名の外観について説明します
type: docs
weight: 1210
url: /ja/net/groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/
---
## PdfDigitalSignatureAppearance class

PDF ドキュメント上のデジタル署名の外観について説明します。

```csharp
public sealed class PdfDigitalSignatureAppearance : SignatureAppearance
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [PdfDigitalSignatureAppearance](pdfdigitalsignatureappearance)() | デフォルト値で署名外観オブジェクトを作成します。 |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [Background](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/background) { get; set; } | 署名の外観の背景色を取得または設定します。 デフォルトの値は SystemColors.Windows です。 |
| [ContactInfoLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/contactinfolabel) { get; set; } | 連絡先情報ラベルを取得または設定します。デフォルト値: "連絡先". この値が空の場合、デジタル署名領域に連絡先ラベルは表示されません. |
| [DateSignedAtLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/datesignedatlabel) { get; set; } | 日付署名ラベルを取得または設定します。デフォルト値: "日付". |
| [DigitalSignedLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/digitalsignedlabel) { get; set; } | デジタル署名ラベルを取得または設定します。デフォルト値: 「デジタル署名者」. |
| [FontFamilyName](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/fontfamilyname) { get; set; } | ラベルを表示するフォント ファミリ名を取得または設定します。デフォルト値は「Arial」. |
| [FontSize](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/fontsize) { get; set; } | ラベルを表示するフォント サイズを取得または設定します。デフォルト値は 10. です。 |
| [Foreground](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/foreground) { get; set; } | 署名の外観の前景色を取得または設定します。 デフォルトの値は Color.FromArgb(76, 100, 255) です。 |
| [LocationLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/locationlabel) { get; set; } | ロケーション ラベルを取得または設定します。デフォルト値: "Location". この値が空の場合、デジタル署名領域に場所ラベルは表示されません. |
| [ReasonLabel](../../groupdocs.signature.options.appearances/pdfdigitalsignatureappearance/reasonlabel) { get; set; } | 理由ラベルを取得または設定します。デフォルト値: "Reason". この値が空の場合、デジタル署名領域に理由ラベルは表示されません. |

### 備考

**もっと詳しく知る**

* GroupDocs.Signature を使用してデジタル電子署名を作成する簡単な例を参照してください: [デジタル電子署名を使用した高度な署名ドキュメント](https://docs.groupdocs.com/signature/net/sign-document-with-digital-signature-advanced/)
* GroupDocs.Signature による各種電子署名のより高度な設定例を見る: [高度な電子署名のプロパティ](https://docs.groupdocs.com/signature/net/sign-documents-with-extra-digital-signature-properties/)

### 関連項目

* class [SignatureAppearance](../signatureappearance)
* 名前空間 [GroupDocs.Signature.Options.Appearances](../../groupdocs.signature.options.appearances)
* 組み立て [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
