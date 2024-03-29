---
title: AliasDictionary
second_title: GroupDocs.Search efter .NET API Reference
description: Representerar en ordbok med alias.
type: docs
weight: 350
url: /sv/net/groupdocs.search.dictionaries/aliasdictionary/
---
## AliasDictionary class

Representerar en ordbok med alias.

```csharp
public class AliasDictionary : DictionaryBase, IEnumerable<string>
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/aliasdictionary/count) { get; } | Hämtar antalet alias som finns i[`AliasDictionary`](../aliasdictionary) . |

## Metoder

| namn | Beskrivning |
| --- | --- |
| [Add](../../groupdocs.search.dictionaries/aliasdictionary/add)(string, string) | Lägger till det angivna aliasparet och associerad text till den här instansen av[`AliasDictionary`](../aliasdictionary) . |
| [AddRange](../../groupdocs.search.dictionaries/aliasdictionary/addrange#addrange)(AliasReplacementPair[]) | Lägger till den angivna samlingen av alias/ersättningspar till denna instans av[`AliasDictionary`](../aliasdictionary) . |
| [AddRange](../../groupdocs.search.dictionaries/aliasdictionary/addrange#addrange_1)(IEnumerable&lt;AliasReplacementPair&gt;) | Lägger till den angivna samlingen av alias/ersättningspar till denna instans av[`AliasDictionary`](../aliasdictionary) . |
| [AddRange](../../groupdocs.search.dictionaries/aliasdictionary/addrange#addrange_2)(IEnumerable&lt;KeyValuePair&lt;string, string&gt;&gt;) | Lägger till den angivna samlingen av alias/ersättningspar till denna instans av[`AliasDictionary`](../aliasdictionary) . |
| [Clear](../../groupdocs.search.dictionaries/aliasdictionary/clear)() | Tar bort alla alias från en[`AliasDictionary`](../aliasdictionary) objekt. |
| [Contains](../../groupdocs.search.dictionaries/aliasdictionary/contains)(string) | Bestämmer om en[`AliasDictionary`](../aliasdictionary) objektet innehåller det angivna alias. |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | Exporterar ordboken till en fil med det angivna namnet. |
| [GetEnumerator](../../groupdocs.search.dictionaries/aliasdictionary/getenumerator)() | Returnerar en uppräkning som itererar genom samlingen. |
| [GetText](../../groupdocs.search.dictionaries/aliasdictionary/gettext)(string) | Hämtar en text som är associerad med det angivna aliaset. |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | Importerar en ordbok från den angivna filen. |
| [Remove](../../groupdocs.search.dictionaries/aliasdictionary/remove)(string) | Tar bort det angivna aliaset från en[`AliasDictionary`](../aliasdictionary) objekt. |

### Anmärkningar

**Läs mer**

* [Använda alias](https://docs.groupdocs.com/display/searchnet/Using+aliases)
* [Hantera alias ordbok](https://docs.groupdocs.com/display/searchnet/Alias+dictionary)

### Se även

* class [DictionaryBase](../dictionarybase)
* namnutrymme [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* hopsättning [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
