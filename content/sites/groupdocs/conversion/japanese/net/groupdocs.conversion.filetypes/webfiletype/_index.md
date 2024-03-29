---
title: WebFileType
second_title: GroupDocs.Conversion for .NET API リファレンス
description: Web ドキュメントを定義します次のファイル タイプが含まれます Xml./webfiletype/xmlJson./webfiletype/jsonHtml./webfiletype/htmlHtm./webfiletype/htmMht./webfiletype/mhtMhtml./webfiletype/mhtmlChm./webfiletype/chm
type: docs
weight: 1080
url: /ja/net/groupdocs.conversion.filetypes/webfiletype/
---
## WebFileType class

Web ドキュメントを定義します。次のファイル タイプが含まれます: [`Xml`](./xml)[`Json`](./json)[`Html`](./html)[`Htm`](./htm)[`Mht`](./mht)[`Mhtml`](./mhtml)[`Chm`](./chm)

```csharp
public sealed class WebFileType : FileType
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [WebFileType](webfiletype)() | シリアル化コンストラクター |

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [Description](../../groupdocs.conversion.filetypes/filetype/description) { get; } | ファイルタイプの説明 |
| [Extension](../../groupdocs.conversion.filetypes/filetype/extension) { get; } | ファイル拡張子 |
| [Family](../../groupdocs.conversion.filetypes/filetype/family) { get; } | ファイル family |
| [FileFormat](../../groupdocs.conversion.filetypes/filetype/fileformat) { get; } | ファイル形式 |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | 現在のオブジェクトを他のオブジェクトと比較します。 |
| override [Equals](../../groupdocs.conversion.filetypes/filetype/equals)(Enumeration) | 2 つのオブジェクト インスタンスが等しいかどうかを判断します。 |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | 2 つのオブジェクト インスタンスが等しいかどうかを判断します。 |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | デフォルトのハッシュ関数として機能します。 |
| override [ToString](../../groupdocs.conversion.filetypes/filetype/tostring)() | 文字列表現 |
| [explicit operator](../../groupdocs.conversion.filetypes/webfiletype/op_explicit) | DataFileType を明示的に WebFileType に変換します |

## 田畑

| 名前 | 説明 |
| --- | --- |
| static readonly [Chm](../../groupdocs.conversion.filetypes/webfiletype/chm) | CHM ファイル形式は、HTML ページのコレクションで構成される Microsoft HTML ヘルプ ファイルを表します。トピックにすばやくアクセスするためのインデックスと、ヘルプ ドキュメントのさまざまな部分へのナビゲーションを提供します。 このファイル形式の詳細[ここ](https://docs.fileformat.com/web/chm) |
| static readonly [Htm](../../groupdocs.conversion.filetypes/webfiletype/htm) | HTM (ハイパー テキスト マークアップ言語) は、ブラウザーで表示するために作成された Web ページの拡張機能です。 このファイル形式の詳細[ここ](https://wiki.fileformat.com/web/html) |
| static readonly [Html](../../groupdocs.conversion.filetypes/webfiletype/html) | HTML (ハイパー テキスト マークアップ言語) は、ブラウザーで表示するために作成された Web ページの拡張機能です。 このファイル形式の詳細[ここ](https://wiki.fileformat.com/web/html) |
| static readonly [Json](../../groupdocs.conversion.filetypes/webfiletype/json) | JSON (JavaScript Object Notation) は、人間が判読できるテキストを使用してデータを保存および送信するデータ共有用のオープン スタンダード ファイル形式です。 このファイル形式の詳細[ここ](https://docs.fileformat.com/web/json) |
| static readonly [Mht](../../groupdocs.conversion.filetypes/webfiletype/mht) | MHTML 拡張子を持つファイルは、さまざまなアプリケーションで作成できる Web ページ アーカイブ形式を表します。この形式は、Web HTML コードと関連するリソースを 1 つのファイルに保存するため、アーカイブ形式として知られています。 このファイル形式の詳細[ここ](https://wiki.fileformat.com/web/mhtml) |
| static readonly [Mhtml](../../groupdocs.conversion.filetypes/webfiletype/mhtml) | MHTML 拡張子を持つファイルは、さまざまなアプリケーションで作成できる Web ページ アーカイブ形式を表します。この形式は、Web HTML コードと関連するリソースを 1 つのファイルに保存するため、アーカイブ形式として知られています。 このファイル形式の詳細[ここ](https://wiki.fileformat.com/web/mhtml) |
| static readonly [Xml](../../groupdocs.conversion.filetypes/webfiletype/xml) | XML は Extensible Markup Language の略で、HTML に似ていますが、オブジェクトを定義するためのタグの使用が異なります。 このファイル形式の詳細[ここ](https://wiki.fileformat.com/web/xml) |

### 関連項目

* class [FileType](../filetype)
* 名前空間 [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* 組み立て [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
