---
title: TextWatermark
second_title: GroupDocs.Watermark for .NET API リファレンス
description: テキストの透かしを表します
type: docs
weight: 3160
url: /ja/net/groupdocs.watermark.watermarks/textwatermark/
---
## TextWatermark class

テキストの透かしを表します。

```csharp
public class TextWatermark : Watermark
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [TextWatermark](textwatermark)(string, Font) | の新しいインスタンスを初期化します[`TextWatermark`](../textwatermark)指定されたテキストとフォントを持つクラス. |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [BackgroundColor](../../groupdocs.watermark.watermarks/textwatermark/backgroundcolor) { get; set; } | テキストの背景色を取得または設定します。 |
| [ConsiderParentMargins](../../groupdocs.watermark/watermark/considerparentmargins) { get; set; } | 透かしのサイズと座標が 親マージンを考慮して計算されるかどうかを示す値を取得または設定します. |
| [Font](../../groupdocs.watermark.watermarks/textwatermark/font) { get; set; } | テキストのフォントを取得または設定します。 |
| [ForegroundColor](../../groupdocs.watermark.watermarks/textwatermark/foregroundcolor) { get; set; } | テキストの前景色を取得または設定します。 |
| [Height](../../groupdocs.watermark/watermark/height) { get; set; } | 目的の高さを取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |
| [HorizontalAlignment](../../groupdocs.watermark/watermark/horizontalalignment) { get; set; } | この水平方向の配置を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |
| [IsBackground](../../groupdocs.watermark/watermark/isbackground) { get; set; } | 透かしを背景に配置するかどうかを示す値を取得または設定します。 |
| [Margins](../../groupdocs.watermark/watermark/margins) { get; set; } | このマージン設定を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |
| [Opacity](../../groupdocs.watermark/watermark/opacity) { get; set; } | この不透明度を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |
| [Padding](../../groupdocs.watermark.watermarks/textwatermark/padding) { get; set; } | このパディング設定を取得または設定します[`TextWatermark`](../textwatermark). このプロパティは、イメージ ファイルにのみ適用されます。 |
| [RotateAngle](../../groupdocs.watermark/watermark/rotateangle) { get; set; } | この回転角度を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark)度単位. |
| [ScaleFactor](../../groupdocs.watermark/watermark/scalefactor) { get; set; } | 透かしのサイズが親のサイズにどのように依存するかを定義する値を取得または設定します。 |
| [SizingType](../../groupdocs.watermark/watermark/sizingtype) { get; set; } | 透かしのサイズを指定する方法を指定する値を取得または設定します. |
| [Text](../../groupdocs.watermark.watermarks/textwatermark/text) { get; set; } | 透かしとして使用するテキストを取得または設定します。 |
| [TextAlignment](../../groupdocs.watermark.watermarks/textwatermark/textalignment) { get; set; } | 透かしテキストの配置を取得または設定します。 |
| [VerticalAlignment](../../groupdocs.watermark/watermark/verticalalignment) { get; set; } | この垂直方向の配置を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |
| [Width](../../groupdocs.watermark/watermark/width) { get; set; } | 目的の幅を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |
| [X](../../groupdocs.watermark/watermark/x) { get; set; } | この x 座標を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |
| [Y](../../groupdocs.watermark/watermark/y) { get; set; } | この y 座標を取得または設定します[`Watermark`](../../groupdocs.watermark/watermark). |

### 備考

**もっと詳しく知る：**

* [テキスト透かしの追加](https://docs.groupdocs.com/display/watermarknet/Adding+text+watermarks)

### 例

親のサイズに応じてテキストの透かしをスケーリングします。

```csharp
foreach (string file in Directory.GetFiles("C:\\test"))
{
    using (Watermarker watermarker = new Watermarker(file))
    {
        TextWatermark watermark = new TextWatermark("test watermark", new Font("Arial", 36));
        watermark.HorizontalAlignment = HorizontalAlignment.Center;
        watermark.VerticalAlignment = VerticalAlignment.Center;
        watermark.SizingType = SizingType.ScaleToParentDimensions;
        watermark.RotateAngle = 45;
        watermark.ScaleFactor = 0.4;

        watermarker.Add(watermark);
        watermarker.Save();
    }
}
```

### 関連項目

* class [Watermark](../../groupdocs.watermark/watermark)
* 名前空間 [GroupDocs.Watermark.Watermarks](../../groupdocs.watermark.watermarks)
* 組み立て [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
