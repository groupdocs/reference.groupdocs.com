---
title: Alphabet
second_title: GroupDocs.Search efter .NET API Reference
description: Representerar en ordbok med tecken som används under indexering för att detektera teckentyp. Varje tecken kan hanteras som avgränsare som bokstav eller båda.
type: docs
weight: 370
url: /sv/net/groupdocs.search.dictionaries/alphabet/
---
## Alphabet class

Representerar en ordbok med tecken som används under indexering för att detektera teckentyp. Varje tecken kan hanteras som avgränsare, som bokstav eller båda.

```csharp
public class Alphabet : DictionaryBase, IEnumerable<char>
```

## Egenskaper

| namn | Beskrivning |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/alphabet/count) { get; } | Hämtar antalet tecken som finns i[`Alphabet`](../alphabet) . |

## Metoder

| namn | Beskrivning |
| --- | --- |
| [Clear](../../groupdocs.search.dictionaries/alphabet/clear)() | Ställer inSeparator typ för alla tecken i detta[`Alphabet`](../alphabet) . |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | Exporterar ordboken till en fil med det angivna namnet. |
| [GetCharacterType](../../groupdocs.search.dictionaries/alphabet/getcharactertype)(char) | Får en typ av tecken. |
| [GetEnumerator](../../groupdocs.search.dictionaries/alphabet/getenumerator)() | Returnerar en uppräkning som itererar genom samlingen. |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | Importerar en ordbok från den angivna filen. |
| [SetRange](../../groupdocs.search.dictionaries/alphabet/setrange)(char[], CharacterType) | Anger typen för varje tecken i den angivna samlingen i den här instansen av[`Alphabet`](../alphabet) . |

### Anmärkningar

**Läs mer**

* [Karaktärstyper](https://docs.groupdocs.com/display/searchnet/Character+types)
* [Hantera alfabetet](https://docs.groupdocs.com/display/searchnet/Alphabet)

### Se även

* class [DictionaryBase](../dictionarybase)
* namnutrymme [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* hopsättning [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
