---
title: SaveOptions
second_title: GroupDocs.Redaction for .NET API リファレンス
description: 出力ファイル名を変更したりドキュメントを画像ベースの PDF ラスタライズ に変換したりするためのオプションを提供します
type: docs
weight: 380
url: /ja/net/groupdocs.redaction.options/saveoptions/
---
## SaveOptions class

出力ファイル名を変更したり、ドキュメントを画像ベースの PDF (ラスタライズ) に変換したりするためのオプションを提供します。

```csharp
public class SaveOptions
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [SaveOptions](saveoptions#constructor)() | 新しいインスタンスをデフォルトで初期化します: PDF へのラスタライズ - false、接尾辞の追加 - false. |
| [SaveOptions](saveoptions#constructor_1)(bool, string) | 指定されたパラメーターで新しいインスタンスを初期化します。 |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [AddSuffix](../../groupdocs.redaction.options/saveoptions/addsuffix) { get; set; } | 保存する前にファイル名を変更する必要があるかどうかを示す値を取得または設定します。デフォルトでは False. |
| [Rasterization](../../groupdocs.redaction.options/saveoptions/rasterization) { get; } | ラスタライズ設定を取得します。 |
| [RasterizeToPDF](../../groupdocs.redaction.options/saveoptions/rasterizetopdf) { get; set; } | ドキュメント内のすべてのページを画像に変換して 1 つの PDF ファイルに入れる必要があるかどうかを示す値を取得または設定します。 |
| [RedactedFileSuffix](../../groupdocs.redaction.options/saveoptions/redactedfilesuffix) { get; set; } | 出力ファイル名のカスタム サフィックスを取得または設定します。指定されていない場合は、[`SaveSuffix`](./savesuffix)定数が使用されます. |

## 田畑

| 名前 | 説明 |
| --- | --- |
| const [SaveSuffix](../../groupdocs.redaction.options/saveoptions/savesuffix) | デフォルトのサフィックス値を表します。これは「編集済み」です。 |

### 備考

**もっと詳しく知る**

* [デフォルトのオプションで保存](https://docs.groupdocs.com/redaction/net/save-with-default-options/)
* [ラスタライズしたPDFで保存](https://docs.groupdocs.com/redaction/net/save-in-rasterized-pdf/)
* [ラスタライズされた PDF の特定のページを選択する](https://docs.groupdocs.com/redaction/net/select-specific-pages-for-rasterized-pdf/)
* [元の形式で保存](https://docs.groupdocs.com/redaction/net/save-in-original-format/)
* [元のファイルを上書き保存](https://docs.groupdocs.com/redaction/net/save-overwriting-original-file/)
* [ストリームに保存](https://docs.groupdocs.com/redaction/net/save-to-stream/)

### 例

次の例は、SaveOptions を使用してドキュメントを保存する方法を示しています。

```csharp
    using (Redactor redactor = new Redactor(@"C:\sample.pdf"))
    {
       // ドキュメントのリダクションがここに入る
       // ...
    
       // ドキュメントをデフォルトのオプションで保存します (ページを画像に変換し、PDF として保存します)
       redactor.Save();
    
       // ドキュメントを元の形式で保存し、元のファイルを上書きします
       redactor.Save(new SaveOptions() { AddSuffix = false, RasterizeToPDF = false });
    
       // ドキュメントを「*_Redacted.*」ファイルに元の形式で保存します
       redactor.Save(new SaveOptions() { AddSuffix = true, RasterizeToPDF = false });
    
       // ドキュメントをラスタライズせずに、そのファイル名で "*_AnyText.*" (たとえば、"AnyText" ではなくタイムスタンプ) に保存します。
       redactor.Save(new SaveOptions(false, "AnyText"));
    }    
```

### 関連項目

* 名前空間 [GroupDocs.Redaction.Options](../../groupdocs.redaction.options)
* 組み立て [GroupDocs.Redaction](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
