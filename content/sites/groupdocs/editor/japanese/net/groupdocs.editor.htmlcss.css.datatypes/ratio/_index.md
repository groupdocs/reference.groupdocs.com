---
title: Ratio
second_title: GroupDocs.Editor for .NET API リファレンス
description: 分子と分母と呼ばれる 2 つの単位のない値の間の比率を示すことによってメディア クエリおよびラスター イメージの縦横比を記述するために使用される比率CSS データ型を表します不変の構造体.
type: docs
weight: 280
url: /ja/net/groupdocs.editor.htmlcss.css.datatypes/ratio/
---
## Ratio structure

「分子」と「分母」と呼ばれる 2 つの単位のない値の間の比率を示すことによって、メディア クエリおよびラスター イメージの縦横比を記述するために使用される「比率」CSS データ型を表します。不変の構造体.

```csharp
public struct Ratio : ICloneable, ICssDataType, IEquatable<Ratio>
```

## プロパティ

| 名前 | 説明 |
| --- | --- |
| [Denominator](../../groupdocs.editor.htmlcss.css.datatypes/ratio/denominator) { get; } | この比率の分母を返します |
| [Numerator](../../groupdocs.editor.htmlcss.css.datatypes/ratio/numerator) { get; } | この比率の分子を返します |

## メソッド

| 名前 | 説明 |
| --- | --- |
| static [Create](../../groupdocs.editor.htmlcss.css.datatypes/ratio/create)(ushort, ushort) | 指定された分子と分母から 1 つの Ratio インスタンスを作成して返します |
| [Calculate](../../groupdocs.editor.htmlcss.css.datatypes/ratio/calculate)() | この比率を計算し、単一の浮動小数点数として返します |
| [Clone](../../groupdocs.editor.htmlcss.css.datatypes/ratio/clone)() | この比率の完全なコピーを返します |
| override [Equals](../../groupdocs.editor.htmlcss.css.datatypes/ratio/equals#equals_1)(object) | このインスタンスが指定されたキャストされていないオブジェクトと等しいかどうかを判断します。これはおそらく別の「比率」です。 instance |
| [Equals](../../groupdocs.editor.htmlcss.css.datatypes/ratio/equals#equals)(Ratio) | このインスタンスが指定された「比率」と等しいかどうかを判断します instance |
| override [GetHashCode](../../groupdocs.editor.htmlcss.css.datatypes/ratio/gethashcode)() | このインスタンスのハッシュコードを返します。これは、有効期間中は変更できません |
| [GetInverseRatio](../../groupdocs.editor.htmlcss.css.datatypes/ratio/getinverseratio)() | この比率の逆 (逆数) 比率を生成して返します |
| [SerializeDefault](../../groupdocs.editor.htmlcss.css.datatypes/ratio/serializedefault)() | この比率を文字列にシリアル化し、it を返します |
| override [ToString](../../groupdocs.editor.htmlcss.css.datatypes/ratio/tostring)() | この比率の文字列表現を返します。 「SerializeDefault()」と同じ |
| [operator ==](../../groupdocs.editor.htmlcss.css.datatypes/ratio/op_equality) | 2 つの比率を比較し、2 つが一致するかどうかを示すブール値を返します。 |
| [operator !=](../../groupdocs.editor.htmlcss.css.datatypes/ratio/op_inequality) | 2 つの比率を比較し、2 つが一致しないかどうかを示すブール値を返します。 |

## 田畑

| 名前 | 説明 |
| --- | --- |
| static readonly [Single](../../groupdocs.editor.htmlcss.css.datatypes/ratio/single) | 単一のデフォルト比率 1/1 |

### 備考

https://developer.mozilla.org/en-US/docs/Web/CSS/ratio

### 関連項目

* interface [ICssDataType](../icssdatatype)
* 名前空間 [GroupDocs.Editor.HtmlCss.Css.DataTypes](../../groupdocs.editor.htmlcss.css.datatypes)
* 組み立て [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
