---
title: FromExtension
second_title: GroupDocs.Parser for .NET API リファレンス
description: ファイル拡張子をファイル タイプにマップします
type: docs
weight: 900
url: /ja/net/groupdocs.parser.options/filetype/fromextension/
---
## FileType.FromExtension method

ファイル拡張子をファイル タイプにマップします。

```csharp
public static FileType FromExtension(string extension)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| extension | String | ファイル拡張子（ピリオド「.」を含む）。 |

### 戻り値

ファイルタイプがサポートされている場合はそれを返し、そうでない場合はデフォルトを返します[`Unknown`](../unknown)ファイルの種類。

### 例外

| 例外 | 調子 |
| --- | --- |
| ArgumentException | スローされるタイミング*extension*null または空の文字列です。 |

### 関連項目

* class [FileType](../../filetype)
* 名前空間 [GroupDocs.Parser.Options](../../filetype)
* 組み立て [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
