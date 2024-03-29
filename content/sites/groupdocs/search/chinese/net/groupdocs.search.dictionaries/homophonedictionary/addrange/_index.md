---
title: AddRange
second_title: GroupDocs.Search for .NET API 参考
description: 将指定的同音字组集合添加到该实例HomophoneDictionarygroupdocs.search.dictionaries/homophonedictionary.
type: docs
weight: 20
url: /zh/net/groupdocs.search.dictionaries/homophonedictionary/addrange/
---
## AddRange(IEnumerable&lt;string[]&gt;) {#addrange}

将指定的同音字组集合添加到该实例[`HomophoneDictionary`](../../homophonedictionary).

```csharp
public void AddRange(IEnumerable<string[]> homophones)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| homophones | IEnumerable`1 | 要添加到词典中的同音词组的集合。 |

### 例外

| 例外 | （健康）状况 |
| --- | --- |
| ArgumentNullException | 抛出时*homophones*是`无效的`. |
| ArgumentException | 当一组中的同音字数小于 2 时抛出。 |

### 也可以看看

* class [HomophoneDictionary](../../homophonedictionary)
* 命名空间 [GroupDocs.Search.Dictionaries](../../homophonedictionary)
* 部件 [GroupDocs.Search](../../../)

---

## AddRange(string[][]) {#addrange_1}

将指定的同音字组集合添加到该实例[`HomophoneDictionary`](../../homophonedictionary).

```csharp
public void AddRange(string[][] homophones)
```

| 范围 | 类型 | 描述 |
| --- | --- | --- |
| homophones | String[][] | 要添加到词典中的同音词组的集合。 |

### 例外

| 例外 | （健康）状况 |
| --- | --- |
| ArgumentNullException | 抛出时*homophones*是`无效的`. |
| ArgumentException | 当一组中的同音字数小于 2 时抛出。 |

### 也可以看看

* class [HomophoneDictionary](../../homophonedictionary)
* 命名空间 [GroupDocs.Search.Dictionaries](../../homophonedictionary)
* 部件 [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
