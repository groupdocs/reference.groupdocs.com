---
title: SvgImage
second_title: GroupDocs.Editor for .NET API リファレンス
description: コンテンツから新しい SvgImage インスタンスを作成し通常の文字列として表され指定された name を使用します
type: docs
weight: 10
url: /ja/net/groupdocs.editor.htmlcss.resources.images.vector/svgimage/svgimage/
---
## SvgImage(string, string) {#constructor_1}

コンテンツから新しい SvgImage インスタンスを作成し、通常の文字列として表され、指定された name を使用します

```csharp
public SvgImage(string name, string content)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| name | String | SVG 画像の名前。 null、空、または空白にすることはできません。 |
| content | String | SVG 画像の有効な XML 準拠コンテンツを含む、通常の文字列としてのコンテンツ。 null、空、または空白にすることはできません。 SVG コンテンツでない場合、例外がスローされます。 |

### 例外

| 例外 | 調子 |
| --- | --- |
| ArgumentException | パラメータの一部が無効です |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) | *content*引数に無効な SVG コンテンツが含まれています |

### 関連項目

* class [SvgImage](../../svgimage)
* 名前空間 [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../svgimage)
* 組み立て [GroupDocs.Editor](../../../)

---

## SvgImage(string, Stream) {#constructor}

コンテンツから新しい SvgImage インスタンスを作成し、バイト ストリームとして表され、指定された name を使用します

```csharp
public SvgImage(string name, Stream binaryContent)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| name | String | SVG 画像の名前。 null、空、または空白にすることはできません。 |
| binaryContent | Stream | バイトストリームとしてのコンテンツ。読み取りは元の位置から開始されます。 null にすることはできません。 読み取り可能でシーク可能である必要があります。このインスタンスが破棄される場合、このストリームも破棄されます。 |

### 例外

| 例外 | 調子 |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### 関連項目

* class [SvgImage](../../svgimage)
* 名前空間 [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../svgimage)
* 組み立て [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
