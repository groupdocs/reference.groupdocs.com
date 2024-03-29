---
title: MultiframeImageWatermarkOptions
second_title: GroupDocs.Watermark for .NET API リファレンス
description: マルチフレーム画像に透かしを追加するときの透かし追加オプションを表します.
type: docs
weight: 1800
url: /ja/net/groupdocs.watermark.options.image/multiframeimagewatermarkoptions/
---
## MultiframeImageWatermarkOptions class

マルチフレーム画像に透かしを追加するときの透かし追加オプションを表します.

```csharp
public class MultiframeImageWatermarkOptions : WatermarkOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [MultiframeImageWatermarkOptions](multiframeimagewatermarkoptions#constructor)() | の新しいインスタンスを初期化します[`MultiframeImageWatermarkOptions`](../multiframeimagewatermarkoptions)class. |
| [MultiframeImageWatermarkOptions](multiframeimagewatermarkoptions#constructor_1)(int) | の新しいインスタンスを初期化します[`MultiframeImageWatermarkOptions`](../multiframeimagewatermarkoptions) frame. の指定されたインデックスを持つ class |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [FrameIndex](../../groupdocs.watermark.options.image/multiframeimagewatermarkoptions/frameindex) { get; set; } | 透かしを追加するフレームのインデックスを取得または設定します。 |

### 備考

**もっと詳しく知る：**

* [画像に透かしを追加する](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+images)

### 例

マルチフレーム画像の特定のフレームに透かしを追加します。

```csharp
ImageLoadOptions loadOptions = new ImageLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\test.gif", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test", new Font("Arial", 12));

    MultiframeImageWatermarkOptions options = new MultiframeImageWatermarkOptions();
    options.FrameIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### 関連項目

* class [WatermarkOptions](../../groupdocs.watermark.options/watermarkoptions)
* 名前空間 [GroupDocs.Watermark.Options.Image](../../groupdocs.watermark.options.image)
* 組み立て [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
