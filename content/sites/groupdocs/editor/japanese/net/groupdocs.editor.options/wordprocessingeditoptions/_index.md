---
title: WordProcessingEditOptions
second_title: GroupDocs.Editor for .NET API リファレンス
description: DOCXRTFODT などサポート可能なすべての WordProcessing Words 準拠 形式のドキュメントを編集するためのカスタム オプションを指定できます
type: docs
weight: 1200
url: /ja/net/groupdocs.editor.options/wordprocessingeditoptions/
---
## WordProcessingEditOptions class

DOC(X)、RTF、ODT など、サポート可能なすべての WordProcessing (Words 準拠) 形式のドキュメントを編集するためのカスタム オプションを指定できます。

```csharp
public class WordProcessingEditOptions : IEditOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [WordProcessingEditOptions](wordprocessingeditoptions#constructor)() | WordProcessingEditOptions クラスの新しいインスタンスを作成して返します。ここでは、すべてのオプションがデフォルト値に設定されています |
| [WordProcessingEditOptions](wordprocessingeditoptions#constructor_1)(bool) | 指定されたページネーションとデフォルトの他のすべてのオプションで WordProcessingEditOptions クラスの新しいインスタンスを作成して返します |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [EnableLanguageInformation](../../groupdocs.editor.options/wordprocessingeditoptions/enablelanguageinformation) { get; set; } | 言語情報を「lang」HTML 属性の形式で HTML マークアップにエクスポートするかどうかを指定します。 このオプションは、多言語ドキュメントのラウンドトリップ変換に役立ちます。デフォルトでは無効になっています (false). |
| [EnablePagination](../../groupdocs.editor.options/wordprocessingeditoptions/enablepagination) { get; set; } | 結果の HTML ドキュメントでページネーションを有効または無効にできます。デフォルトでは無効になっています (false). |
| [ExtractOnlyUsedFont](../../groupdocs.editor.options/wordprocessingeditoptions/extractonlyusedfont) { get; set; } | ドキュメントのテキスト コンテンツで使用されているフォント リソースのみを抽出するかどうかを示す値を取得または設定します。 |
| [FontExtraction](../../groupdocs.editor.options/wordprocessingeditoptions/fontextraction) { get; set; } | 入力 WordProcessing ドキュメントで使用されるフォント リソースの抽出を担当します。デフォルトでは、フォントを抽出しません (NotExtract). |
| [InputControlsClassName](../../groupdocs.editor.options/wordprocessingeditoptions/inputcontrolsclassname) { get; set; } | すべての HTML 要素の「class」属性に配置される、入力 WordProcessing ドキュメント内のフィールドを表すクラス名を指定できます。デフォルトでは NULL です - 'class' 属性は適用されません. |

### 関連項目

* interface [IEditOptions](../ieditoptions)
* 名前空間 [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* 組み立て [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
