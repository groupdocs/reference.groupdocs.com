---
title: PngViewOptions
second_title: GroupDocs.Viewer for .NET API リファレンス
description: ドキュメントを PNG 形式にレンダリングするためのオプションを提供します
type: docs
weight: 440
url: /ja/net/groupdocs.viewer.options/pngviewoptions/
---
## PngViewOptions class

ドキュメントを PNG 形式にレンダリングするためのオプションを提供します。

```csharp
public class PngViewOptions : ViewOptions, IMaxSizeOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [PngViewOptions](pngviewoptions#constructor)() | の新しいインスタンスを初期化します[`PngViewOptions`](../pngviewoptions)class. |
| [PngViewOptions](pngviewoptions#constructor_1)(CreatePageStream) | の新しいインスタンスを初期化します[`PngViewOptions`](../pngviewoptions)class. |
| [PngViewOptions](pngviewoptions#constructor_3)(IPageStreamFactory) | の新しいインスタンスを初期化します[`PngViewOptions`](../pngviewoptions)class. |
| [PngViewOptions](pngviewoptions#constructor_4)(string) | の新しいインスタンスを初期化します[`PngViewOptions`](../pngviewoptions)class. |
| [PngViewOptions](pngviewoptions#constructor_2)(CreatePageStream, ReleasePageStream) | の新しいインスタンスを初期化します[`PngViewOptions`](../pngviewoptions)class. |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [ArchiveOptions](../../groupdocs.viewer.options/baseviewoptions/archiveoptions) { get; set; } | アーカイブ ファイルの表示オプション。 |
| [CadOptions](../../groupdocs.viewer.options/baseviewoptions/cadoptions) { get; set; } | CAD 図面表示オプション。 |
| [DefaultFontName](../../groupdocs.viewer.options/baseviewoptions/defaultfontname) { get; set; } | ドキュメントで使用されている特定のフォントが見つからない場合に使用されるデフォルトのフォント. |
| [EmailOptions](../../groupdocs.viewer.options/baseviewoptions/emailoptions) { get; set; } | 電子メール メッセージの表示オプション。 |
| [ExtractText](../../groupdocs.viewer.options/pngviewoptions/extracttext) { get; set; } | テキスト抽出を有効にします。 |
| [Height](../../groupdocs.viewer.options/pngviewoptions/height) { get; set; } | ピクセル単位の出力画像の高さ. |
| [MailStorageOptions](../../groupdocs.viewer.options/baseviewoptions/mailstorageoptions) { get; set; } | メール ストレージ データ ファイルの表示オプション. |
| [MaxHeight](../../groupdocs.viewer.options/pngviewoptions/maxheight) { get; set; } | 出力画像の最大高さ (ピクセル単位)。 |
| [MaxWidth](../../groupdocs.viewer.options/pngviewoptions/maxwidth) { get; set; } | 出力画像の最大幅 (ピクセル単位)。 |
| [OutlookOptions](../../groupdocs.viewer.options/baseviewoptions/outlookoptions) { get; set; } | MS Outlook データ ファイルの表示オプション. |
| [PdfOptions](../../groupdocs.viewer.options/baseviewoptions/pdfoptions) { get; set; } | PDF ドキュメントの表示オプション. |
| [PresentationOptions](../../groupdocs.viewer.options/baseviewoptions/presentationoptions) { get; set; } | プレゼンテーション処理ドキュメント ビュー オプション. |
| [ProjectManagementOptions](../../groupdocs.viewer.options/baseviewoptions/projectmanagementoptions) { get; set; } | プロジェクト管理ファイルの表示オプション. |
| [RenderComments](../../groupdocs.viewer.options/baseviewoptions/rendercomments) { get; set; } | コメントのレンダリングを有効にします。 |
| [RenderHiddenPages](../../groupdocs.viewer.options/baseviewoptions/renderhiddenpages) { get; set; } | 隠しページのレンダリングを有効にします。 |
| [RenderNotes](../../groupdocs.viewer.options/baseviewoptions/rendernotes) { get; set; } | レンダリング ノートを有効にします。 |
| [SpreadsheetOptions](../../groupdocs.viewer.options/baseviewoptions/spreadsheetoptions) { get; set; } | スプレッドシート ファイルの表示オプション。 |
| [TextOptions](../../groupdocs.viewer.options/baseviewoptions/textoptions) { get; set; } | テキスト ファイルのページ オプションへの分割. |
| [VisioRenderingOptions](../../groupdocs.viewer.options/baseviewoptions/visiorenderingoptions) { get; set; } | ドキュメントを処理する Visio ファイルの表示オプション。 |
| [Watermark](../../groupdocs.viewer.options/viewoptions/watermark) { get; set; } | 各ページに適用されるテキスト透かし. |
| [WebDocumentOptions](../../groupdocs.viewer.options/baseviewoptions/webdocumentoptions) { get; set; } | このレンダリング オプションを使用すると、Web ドキュメントをレンダリングするときの出力 HTML/PDF/PNG/JPEG の 外観をカスタマイズできます。 |
| [Width](../../groupdocs.viewer.options/pngviewoptions/width) { get; set; } | ピクセル単位の出力画像の幅. |
| [WordProcessingOptions](../../groupdocs.viewer.options/baseviewoptions/wordprocessingoptions) { get; set; } | このレンダリング オプションを使用すると、Word ドキュメントをレンダリングする際に出力 HTML/PDF/PNG/JPEG の 外観をカスタマイズできます。 |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [RotatePage](../../groupdocs.viewer.options/viewoptions/rotatepage)(int, Rotation) | ページに時計回りの回転を適用します。 |

## 田畑

| 名前 | 説明 |
| --- | --- |
| readonly [PageRotations](../../groupdocs.viewer.options/viewoptions/pagerotations) | ページの回転。 |

### 関連項目

* class [ViewOptions](../viewoptions)
* interface [IMaxSizeOptions](../imaxsizeoptions)
* 名前空間 [GroupDocs.Viewer.Options](../../groupdocs.viewer.options)
* 組み立て [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
