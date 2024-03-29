---
title: XmlHighlightOptions
second_title: GroupDocs.Editor for .NET API リファレンス
description: XML から HTML への変換中に XML の強調表示をカスタマイズできるオプションが含まれています
type: docs
weight: 1290
url: /ja/net/groupdocs.editor.options/xmlhighlightoptions/
---
## XmlHighlightOptions class

XML から HTML への変換中に XML の強調表示をカスタマイズできるオプションが含まれています

```csharp
public sealed class XmlHighlightOptions : IEditOptions
```

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [AttributeNamesFontSettings](../../groupdocs.editor.options/xmlhighlightoptions/attributenamesfontsettings) { get; } | 属性名のフォントを表す責任があります |
| [AttributeValuesFontSettings](../../groupdocs.editor.options/xmlhighlightoptions/attributevaluesfontsettings) { get; } | 属性値のフォントを表す責任があります |
| [CDataFontSettings](../../groupdocs.editor.options/xmlhighlightoptions/cdatafontsettings) { get; } | CDATA セクションのフォントを表す責任があります (開始タグと終了タグのペアを含む) |
| [HtmlCommentsFontSettings](../../groupdocs.editor.options/xmlhighlightoptions/htmlcommentsfontsettings) { get; } | HTML コメントのフォントを表す責任があります (開始タグと終了タグのペアを含む) |
| [InnerTextFontSettings](../../groupdocs.editor.options/xmlhighlightoptions/innertextfontsettings) { get; } | 内部タグ text のフォントの表現を担当 |
| [IsDefault](../../groupdocs.editor.options/xmlhighlightoptions/isdefault) { get; } | この XML ハイライト オプション オブジェクトにデフォルトのフォント設定があるかどうかを決定します |
| [XmlTagsFontSettings](../../groupdocs.editor.options/xmlhighlightoptions/xmltagsfontsettings) { get; } | XML タグ (タグ名を含む山かっこ) のフォントを表す責任があります |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [ResetToDefault](../../groupdocs.editor.options/xmlhighlightoptions/resettodefault)() | 現在のフォント設定をデフォルト値にリセットします |

### 関連項目

* interface [IEditOptions](../ieditoptions)
* 名前空間 [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* 組み立て [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
