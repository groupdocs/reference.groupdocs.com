---
title: Merger
second_title: GroupDocs.Merger for .NET API リファレンス
description: ドキュメントのマージ プロセスを制御するメイン クラスを表します
type: docs
weight: 790
url: /ja/net/groupdocs.merger/merger/
---
## Merger class

ドキュメントのマージ プロセスを制御するメイン クラスを表します。

```csharp
public class Merger : IDisposable
```

## コンストラクター

| 名前 | 説明 |
| --- | --- |
| [Merger](merger#constructor)(Func&lt;Stream&gt;) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_4)(Stream) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_8)(string) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_1)(Func&lt;Stream&gt;, ILoadOptions) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_3)(Func&lt;Stream&gt;, MergerSettings) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_5)(Stream, ILoadOptions) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_7)(Stream, MergerSettings) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_9)(string, ILoadOptions) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_11)(string, MergerSettings) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_2)(Func&lt;Stream&gt;, ILoadOptions, MergerSettings) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_6)(Stream, ILoadOptions, MergerSettings) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |
| [Merger](merger#constructor_10)(string, ILoadOptions, MergerSettings) | の新しいインスタンスを初期化します[`Merger`](../merger)class. |

## メソッド

| 名前 | 説明 |
| --- | --- |
| [AddPassword](../../groupdocs.merger/merger/addpassword)(IAddPasswordOptions) | パスワードでドキュメントを保護します。 |
| [ChangeOrientation](../../groupdocs.merger/merger/changeorientation)(IOrientationOptions) | 指定したページに新しい方向モードを適用します。 |
| [Dispose](../../groupdocs.merger/merger/dispose)() | リソースを破棄します。 |
| [ExtractPages](../../groupdocs.merger/merger/extractpages)(IExtractOptions) | ソース ドキュメントのいくつかのページで新しいドキュメントを作成します。 |
| [GeneratePreview](../../groupdocs.merger/merger/generatepreview)(IPreviewOptions) | ドキュメント ページのプレビューを生成します。 |
| [GetDocumentInfo](../../groupdocs.merger/merger/getdocumentinfo)() | ドキュメント ページに関する情報を取得します: サイズ、最大ページ高さ、最大高さのページの幅. |
| [ImportDocument](../../groupdocs.merger/merger/importdocument)(IImportDocumentOptions) | ドキュメントを添付ファイルとしてインポートするか、Ole. を介して埋め込みます。 |
| [IsPasswordSet](../../groupdocs.merger/merger/ispasswordset)() | ドキュメントがパスワードで保護されているかどうかを確認します。 |
| [Join](../../groupdocs.merger/merger/join#join)(Stream) | ドキュメントを 1 つのドキュメントに結合します。 |
| [Join](../../groupdocs.merger/merger/join#join_3)(string) | ドキュメントを 1 つのドキュメントに結合します。 |
| [Join](../../groupdocs.merger/merger/join#join_1)(Stream, IImageJoinOptions) | ドキュメントを 1 つのドキュメントに結合します。 |
| [Join](../../groupdocs.merger/merger/join#join_2)(Stream, IJoinOptions) | ドキュメントを 1 つのドキュメントに結合します。 |
| [Join](../../groupdocs.merger/merger/join#join_4)(string, IImageJoinOptions) | ドキュメントを 1 つのドキュメントに結合します。 |
| [Join](../../groupdocs.merger/merger/join#join_5)(string, IJoinOptions) | ドキュメントを 1 つのドキュメントに結合します。 |
| [MovePage](../../groupdocs.merger/merger/movepage)(IMoveOptions) | 既知の形式のドキュメント内の新しい位置にページを移動します。 |
| [RemovePages](../../groupdocs.merger/merger/removepages)(IRemoveOptions) | 既知の形式のドキュメントからページを削除します。 |
| [RemovePassword](../../groupdocs.merger/merger/removepassword)() | ドキュメントからパスワードを削除します。 |
| [RotatePages](../../groupdocs.merger/merger/rotatepages)(IRotateOptions) | ドキュメントのページを回転します。 |
| [Save](../../groupdocs.merger/merger/save#save)(Stream) | 結果ドキュメントをストリームに保存します*document*. |
| [Save](../../groupdocs.merger/merger/save#save_1)(string) | 結果ドキュメント ファイルを*filePath*. |
| [Save](../../groupdocs.merger/merger/save#save_2)(string, bool) | 結果ドキュメント ファイルを*filePath*. |
| [Split](../../groupdocs.merger/merger/split#split)(ISplitOptions) | 単一の文書を複数の文書に分割します。 |
| [Split](../../groupdocs.merger/merger/split#split_1)(ITextSplitOptions) | 単一の文書を複数の文書に分割します。 |
| [SwapPages](../../groupdocs.merger/merger/swappages)(ISwapOptions) | 既知の形式のドキュメント内の 2 つのページを入れ替えます。 |
| [UpdatePassword](../../groupdocs.merger/merger/updatepassword)(IUpdatePasswordOptions) | ドキュメントの既存のパスワードを更新します。 |

### 関連項目

* 名前空間 [GroupDocs.Merger](../../groupdocs.merger)
* 組み立て [GroupDocs.Merger](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
