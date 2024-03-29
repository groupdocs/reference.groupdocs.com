---
title: FromStream
second_title: GroupDocs.Viewer for .NET API リファレンス
description: ファイルの署名を読み取ってファイルの種類を検出します
type: docs
weight: 1950
url: /ja/net/groupdocs.viewer/filetype/fromstream/
---
## FromStream(Stream) {#fromstream}

ファイルの署名を読み取ってファイルの種類を検出します。

```csharp
public static FileType FromStream(Stream stream)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| stream | Stream | ファイル ストリーム。 |

### 関連項目

* class [FileType](../../filetype)
* 名前空間 [GroupDocs.Viewer](../../filetype)
* 組み立て [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string) {#fromstream_2}

ファイルの署名を読み取ってファイルの種類を検出します。

```csharp
public static FileType FromStream(Stream stream, string password)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| stream | Stream | ファイル ストリーム。 |
| password | String | ファイルを開くためのパスワード。 |

### 関連項目

* class [FileType](../../filetype)
* 名前空間 [GroupDocs.Viewer](../../filetype)
* 組み立て [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, ILogger) {#fromstream_1}

ファイルの署名を読み取ってファイルの種類を検出します。

```csharp
public static FileType FromStream(Stream stream, ILogger logger)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| stream | Stream | ファイル ストリーム。 |
| logger | ILogger | ロガー。 |

### 戻り値

正常に検出された場合はファイル タイプを返し、それ以外の場合はデフォルトを返します[`Unknown`](../unknown)ファイルの種類。

### 関連項目

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* 名前空間 [GroupDocs.Viewer](../../filetype)
* 組み立て [GroupDocs.Viewer](../../../)

---

## FromStream(Stream, string, ILogger) {#fromstream_3}

ファイルの署名を読み取ってファイルの種類を検出します。

```csharp
public static FileType FromStream(Stream stream, string password, ILogger logger)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| stream | Stream | ファイル ストリーム。 |
| password | String | ファイルを開くためのパスワード。 |
| logger | ILogger | ロガー。 |

### 戻り値

正常に検出された場合はファイル タイプを返し、それ以外の場合はデフォルトを返します[`Unknown`](../unknown)ファイルの種類。

### 関連項目

* interface [ILogger](../../../groupdocs.viewer.logging/ilogger)
* class [FileType](../../filetype)
* 名前空間 [GroupDocs.Viewer](../../filetype)
* 組み立て [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
