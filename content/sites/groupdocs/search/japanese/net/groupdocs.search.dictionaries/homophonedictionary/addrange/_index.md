---
title: AddRange
second_title: GroupDocs.Search for .NET API リファレンス
description: 指定された同音異義語グループのコレクションをHomophoneDictionarygroupdocs.search.dictionaries/homophonedictionary.
type: docs
weight: 20
url: /ja/net/groupdocs.search.dictionaries/homophonedictionary/addrange/
---
## AddRange(IEnumerable&lt;string[]&gt;) {#addrange}

指定された同音異義語グループのコレクションを、[`HomophoneDictionary`](../../homophonedictionary).

```csharp
public void AddRange(IEnumerable<string[]> homophones)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| homophones | IEnumerable`1 | ディクショナリに追加する同音異義語グループのコレクション。 |

### 例外

| 例外 | 調子 |
| --- | --- |
| ArgumentNullException | スローされるタイミング*homophones*は`ヌル`. |
| ArgumentException | グループ内の同音異義語の数が 2 未満の場合にスローされます。 |

### 関連項目

* class [HomophoneDictionary](../../homophonedictionary)
* 名前空間 [GroupDocs.Search.Dictionaries](../../homophonedictionary)
* 組み立て [GroupDocs.Search](../../../)

---

## AddRange(string[][]) {#addrange_1}

指定された同音異義語グループのコレクションを、[`HomophoneDictionary`](../../homophonedictionary).

```csharp
public void AddRange(string[][] homophones)
```

| パラメータ | タイプ | 説明 |
| --- | --- | --- |
| homophones | String[][] | ディクショナリに追加する同音異義語グループのコレクション。 |

### 例外

| 例外 | 調子 |
| --- | --- |
| ArgumentNullException | スローされるタイミング*homophones*は`ヌル`. |
| ArgumentException | グループ内の同音異義語の数が 2 未満の場合にスローされます。 |

### 関連項目

* class [HomophoneDictionary](../../homophonedictionary)
* 名前空間 [GroupDocs.Search.Dictionaries](../../homophonedictionary)
* 組み立て [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
