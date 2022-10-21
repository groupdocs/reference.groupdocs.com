---
title: CharacterReplacementDictionary
second_title: GroupDocs.Search for .NET API 参考
description: 表示在索引过程中使用的字符替换字典 可以使用字符替换例如从重音字符中删除重音或制作不区分大小写的索引
type: docs
weight: 370
url: /zh/net/groupdocs.search.dictionaries/characterreplacementdictionary/
---
## CharacterReplacementDictionary class

表示在索引过程中使用的字符替换字典。 可以使用字符替换，例如，从重音字符中删除重音或制作不区分大小写的索引。

```csharp
public class CharacterReplacementDictionary : DictionaryBase, IEnumerable<char>
```

## 特性

| 姓名 | 描述 |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/characterreplacementdictionary/count) { get; } | 获取此包含的字符数[`CharacterReplacementDictionary`](../characterreplacementdictionary). |

## 方法

| 姓名 | 描述 |
| --- | --- |
| [AddRange](../../groupdocs.search.dictionaries/characterreplacementdictionary/addrange#addrange)(CharacterReplacementPair[]) | 将指定的字符替换集合添加到[`CharacterReplacementDictionary`](../characterreplacementdictionary). |
| [AddRange](../../groupdocs.search.dictionaries/characterreplacementdictionary/addrange#addrange_1)(IEnumerable&lt;CharacterReplacementPair&gt;) | 将指定的字符替换集合添加到[`CharacterReplacementDictionary`](../characterreplacementdictionary). |
| [AddRange](../../groupdocs.search.dictionaries/characterreplacementdictionary/addrange#addrange_2)(IEnumerable&lt;KeyValuePair&lt;char, char&gt;&gt;) | 将指定的字符替换集合添加到[`CharacterReplacementDictionary`](../characterreplacementdictionary). |
| [Clear](../../groupdocs.search.dictionaries/characterreplacementdictionary/clear)() | 删除所有字符替换[`CharacterReplacementDictionary`](../characterreplacementdictionary)对象. |
| [Contains](../../groupdocs.search.dictionaries/characterreplacementdictionary/contains)(char) | 确定是否[`CharacterReplacementDictionary`](../characterreplacementdictionary)对象包含指定字符的替换。 |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | 将字典导出到具有指定名称的文件。 |
| [GetEnumerator](../../groupdocs.search.dictionaries/characterreplacementdictionary/getenumerator)() | 返回一个遍历集合的枚举器。 |
| [GetReplacement](../../groupdocs.search.dictionaries/characterreplacementdictionary/getreplacement)(char) | 获取指定字符的替换。 |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | 从指定文件导入字典。 |
| [RemoveRange](../../groupdocs.search.dictionaries/characterreplacementdictionary/removerange#removerange)(char[]) | 从此实例中删除指定的字符替换集合[`CharacterReplacementDictionary`](../characterreplacementdictionary). |
| [RemoveRange](../../groupdocs.search.dictionaries/characterreplacementdictionary/removerange#removerange_1)(IEnumerable&lt;char&gt;) | 从此实例中删除指定的字符替换集合[`CharacterReplacementDictionary`](../characterreplacementdictionary). |

### 评论

**学到更多**

* [索引期间的字符替换](https://docs.groupdocs.com/display/searchnet/Character+replacement+during+Indexing)
* [管理字符替换](https://docs.groupdocs.com/display/searchnet/Character+replacements)

### 也可以看看

* class [DictionaryBase](../dictionarybase)
* 命名空间 [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* 部件 [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->