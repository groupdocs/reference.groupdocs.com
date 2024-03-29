---
title: DiagramPreviewOptions
second_title: GroupDocs.Watermark for .NET API リファレンス
description: ダイアグラム ドキュメントのプレビュー生成の要件とストリーム デリゲートを設定するオプションを提供します
type: docs
weight: 1660
url: /ja/net/groupdocs.watermark.options.diagram/diagrampreviewoptions/
---
## DiagramPreviewOptions class

ダイアグラム ドキュメントのプレビュー生成の要件とストリーム デリゲートを設定するオプションを提供します。

```csharp
public class DiagramPreviewOptions : PreviewOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [DiagramPreviewOptions](diagrampreviewoptions#constructor)(CreatePageStream) | の新しいインスタンスを初期化します[`DiagramPreviewOptions`](../diagrampreviewoptions)出力ストリームを閉じるクラス. |
| [DiagramPreviewOptions](diagrampreviewoptions#constructor_1)(CreatePageStream, ReleasePageStream) | の新しいインスタンスを初期化します[`DiagramPreviewOptions`](../diagrampreviewoptions)出力ストリームをさらに使用するために クライアントに返すクラス. |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [CreatePageStream](../../groupdocs.watermark.options/previewoptions/createpagestream) { get; set; } | ページ ストリーム作成デリゲートのインスタンスを取得または設定します。 |
| [Height](../../groupdocs.watermark.options/previewoptions/height) { get; set; } | ページ プレビューの高さを取得または設定します。 |
| [HighQualityRendering](../../groupdocs.watermark.options.diagram/diagrampreviewoptions/highqualityrendering) { get; set; } | 高品質レンダリングのフラグを取得または設定します。 |
| [PageNumbers](../../groupdocs.watermark.options/previewoptions/pagenumbers) { get; set; } | プレビューを生成するページ番号の配列を取得または設定します。 |
| [PreviewFormat](../../groupdocs.watermark.options/previewoptions/previewformat) { get; set; } | プレビュー イメージ形式を取得または設定します。 |
| [ReleasePageStream](../../groupdocs.watermark.options/previewoptions/releasepagestream) { get; set; } | ページ プレビュー完了デリゲートのインスタンスを取得または設定します。 |
| [Resolution](../../groupdocs.watermark.options.diagram/diagrampreviewoptions/resolution) { get; set; } | 生成された画像の解像度を 1 インチあたりのドット数で取得または設定します。 |
| [Width](../../groupdocs.watermark.options/previewoptions/width) { get; set; } | ページ プレビューの幅を取得または設定します。 |

## 田畑

| 名前 | 説明 |
| --- | --- |
| const [DefaultResolution](../../groupdocs.watermark.options.diagram/diagrampreviewoptions/defaultresolution) | デフォルトの解像度 (ドット/インチ)。 |

### 関連項目

* class [PreviewOptions](../../groupdocs.watermark.options/previewoptions)
* 名前空間 [GroupDocs.Watermark.Options.Diagram](../../groupdocs.watermark.options.diagram)
* 組み立て [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
