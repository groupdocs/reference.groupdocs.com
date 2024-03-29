---
title: AssembleDocument
second_title: GroupDocs.Assembly for .NET API リファレンス
description: 指定されたソース パスからテンプレート ドキュメントを読み込み 指定された単一または複数のソースからのデータをテンプレート ドキュメントに入力しdefault を使用して結果ドキュメントをターゲット パスに保存しますLoadSaveOptionsgroupdocs.assembly/loadsaveoptions.
type: docs
weight: 50
url: /ja/net/groupdocs.assembly/documentassembler/assembledocument/
---
## AssembleDocument(string, string, params DataSourceInfo[]) {#assembledocument_2}

指定されたソース パスからテンプレート ドキュメントを読み込み、 指定された単一または複数のソースからのデータをテンプレート ドキュメントに入力し、default を使用して結果ドキュメントをターゲット パスに保存します。[`LoadSaveOptions`](../../loadsaveoptions).

```csharp
public bool AssembleDocument(string sourcePath, string targetPath, 
    params DataSourceInfo[] dataSourceInfos)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| sourcePath | String | データを入力するテンプレート ドキュメントへのパス。 |
| targetPath | String | 結果ドキュメントへのパス。 |
| dataSourceInfos | DataSourceInfo[] | 使用するデータ ソース オブジェクトに関する情報を提供します。 |

### 戻り値

テンプレート ドキュメントの解析が成功したかどうかを示すフラグ。返されたフラグは、 の値が[`Options`](../options)プロパティには、InlineErrorMessages オプション.

### 関連項目

* class [DataSourceInfo](../../datasourceinfo)
* class [DocumentAssembler](../../documentassembler)
* 名前空間 [GroupDocs.Assembly](../../documentassembler)
* 組み立て [GroupDocs.Assembly](../../../)

---

## AssembleDocument(string, string, LoadSaveOptions, params DataSourceInfo[]) {#assembledocument_3}

指定されたソース パスからテンプレート ドキュメントを読み込み、 指定された単一または複数のソースからのデータをテンプレート ドキュメントに入力し、指定された を使用して結果ドキュメントをターゲット パスに保存します。[`LoadSaveOptions`](../../loadsaveoptions).

```csharp
public bool AssembleDocument(string sourcePath, string targetPath, LoadSaveOptions loadSaveOptions, 
    params DataSourceInfo[] dataSourceInfos)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| sourcePath | String | データを入力するテンプレート ドキュメントへのパス。 |
| targetPath | String | 結果ドキュメントへのパス。 |
| loadSaveOptions | LoadSaveOptions | ドキュメントの読み込みと保存の追加オプションを指定します。 |
| dataSourceInfos | DataSourceInfo[] | 使用するデータ ソース オブジェクトに関する情報を提供します。 |

### 戻り値

テンプレート ドキュメントの解析が成功したかどうかを示すフラグ。返されたフラグは、 の値が[`Options`](../options)プロパティには、InlineErrorMessages オプション.

### 関連項目

* class [LoadSaveOptions](../../loadsaveoptions)
* class [DataSourceInfo](../../datasourceinfo)
* class [DocumentAssembler](../../documentassembler)
* 名前空間 [GroupDocs.Assembly](../../documentassembler)
* 組み立て [GroupDocs.Assembly](../../../)

---

## AssembleDocument(Stream, Stream, params DataSourceInfo[]) {#assembledocument}

指定されたソース ストリームからテンプレート ドキュメントをロードし、 指定された単一または複数のソースからのデータをテンプレート ドキュメントに入力し、default を使用して結果ドキュメントをターゲット ストリームに保存します。[`LoadSaveOptions`](../../loadsaveoptions).

```csharp
public bool AssembleDocument(Stream sourceStream, Stream targetStream, 
    params DataSourceInfo[] dataSourceInfos)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| sourceStream | Stream | テンプレート ドキュメントを読み取るストリーム。 |
| targetStream | Stream | 結果ドキュメントを書き込むストリーム。 |
| dataSourceInfos | DataSourceInfo[] | 使用するデータ ソース オブジェクトに関する情報を提供します。 |

### 戻り値

テンプレート ドキュメントの解析が成功したかどうかを示すフラグ。返されたフラグは、 の値が[`Options`](../options)プロパティには、InlineErrorMessages オプション.

### 関連項目

* class [DataSourceInfo](../../datasourceinfo)
* class [DocumentAssembler](../../documentassembler)
* 名前空間 [GroupDocs.Assembly](../../documentassembler)
* 組み立て [GroupDocs.Assembly](../../../)

---

## AssembleDocument(Stream, Stream, LoadSaveOptions, params DataSourceInfo[]) {#assembledocument_1}

指定されたソース ストリームからテンプレート ドキュメントを読み込み、 指定された単一または複数のソースからのデータをテンプレート ドキュメントに入力し、指定された を使用して結果ドキュメントをターゲット ストリームに保存します。[`LoadSaveOptions`](../../loadsaveoptions).

```csharp
public bool AssembleDocument(Stream sourceStream, Stream targetStream, 
    LoadSaveOptions loadSaveOptions, params DataSourceInfo[] dataSourceInfos)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| sourceStream | Stream | テンプレート ドキュメントを読み取るストリーム。 |
| targetStream | Stream | 結果ドキュメントを書き込むストリーム。 |
| loadSaveOptions | LoadSaveOptions | ドキュメントの読み込みと保存の追加オプションを指定します。 |
| dataSourceInfos | DataSourceInfo[] | 使用するデータ ソース オブジェクトに関する情報を提供します。 |

### 戻り値

テンプレート ドキュメントの解析が成功したかどうかを示すフラグ。返されたフラグは、 の値が[`Options`](../options)プロパティには、InlineErrorMessages オプション.

### 関連項目

* class [LoadSaveOptions](../../loadsaveoptions)
* class [DataSourceInfo](../../datasourceinfo)
* class [DocumentAssembler](../../documentassembler)
* 名前空間 [GroupDocs.Assembly](../../documentassembler)
* 組み立て [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
