---
title: JpegSaveOptions
second_title: GroupDocs.Signature for .NET API リファレンス
description: 画像ドキュメントの Jpeg 保存オプション.
type: docs
weight: 1460
url: /ja/net/groupdocs.signature.options/jpegsaveoptions/
---
## JpegSaveOptions class

画像ドキュメントの Jpeg 保存オプション.

```csharp
public sealed class JpegSaveOptions : ImageSaveOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [JpegSaveOptions](jpegsaveoptions)() | デフォルト値で JpegSaveOptions を作成します。 |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | 出力ファイル path に拡張子がない場合に自動的に拡張子を追加するフラグを取得または設定します。デフォルト値は false です。 |
| [BitsPerChannel](../../groupdocs.signature.options/jpegsaveoptions/bitsperchannel) { get; set; } | ロスレス jpeg 画像のチャネルあたりのビット数を取得または設定します。 チャネルごとに 2 ～ 8 ビットをサポートするようになりました. |
| [ColorType](../../groupdocs.signature.options/jpegsaveoptions/colortype) { get; set; } | jpeg 画像の色の種類を取得または設定します。 |
| [Comment](../../groupdocs.signature.options/jpegsaveoptions/comment) { get; set; } | jpeg ファイルのコメントを取得または設定します。 |
| [CompressionType](../../groupdocs.signature.options/jpegsaveoptions/compressiontype) { get; set; } | 圧縮タイプを取得または設定します。 |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | 署名済みドキュメントのファイル形式を取得または設定します。 |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | 既存のファイルを新しい出力ファイルで上書きするかどうかを取得または設定します。 それ以外の場合、新しいファイルはサフィックスとして数字で作成されます. デフォルトでは、この値は true に設定されており、ファイルが上書きされることを意味します. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | 署名されたドキュメントをパスワードで保護して保存するためのパスワードを取得または設定します。 このプロパティは、画像ドキュメントではサポートされていません。 |
| [Quality](../../groupdocs.signature.options/jpegsaveoptions/quality) { get; set; } | 画質を取得または設定します。 |
| [SampleRoundingMode](../../groupdocs.signature.options/jpegsaveoptions/sampleroundingmode) { get; set; } | 8 ビット値を n ビット値に合わせるサンプル丸めモードを取得または設定します JpegOptions.BitsPerChannel. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | LoadOptions からのパスワードを使用して、署名済みドキュメントを保護されたものとして保存するかどうかを取得または設定します。 デフォルト値は true です。 このプロパティは、画像ドキュメントではサポートされていません。 |

### 関連項目

* class [ImageSaveOptions](../imagesaveoptions)
* 名前空間 [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* 組み立て [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
