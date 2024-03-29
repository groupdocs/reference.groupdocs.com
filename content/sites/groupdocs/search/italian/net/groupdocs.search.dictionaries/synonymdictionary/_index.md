---
title: SynonymDictionary
second_title: GroupDocs.Cerca il riferimento dell'API .NET
description: Rappresenta un dizionario di sinonimi.
type: docs
weight: 490
url: /it/net/groupdocs.search.dictionaries/synonymdictionary/
---
## SynonymDictionary class

Rappresenta un dizionario di sinonimi.

```csharp
public class SynonymDictionary : DictionaryBase, IEnumerable<string>
```

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [Count](../../groupdocs.search.dictionaries/synonymdictionary/count) { get; } | Ottiene il numero di parole contenute in this[`SynonymDictionary`](../synonymdictionary) . |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [AddRange](../../groupdocs.search.dictionaries/synonymdictionary/addrange#addrange)(IEnumerable&lt;string[]&gt;) | Aggiunge la raccolta specificata di gruppi di sinonimi a questa istanza di[`SynonymDictionary`](../synonymdictionary) . |
| [AddRange](../../groupdocs.search.dictionaries/synonymdictionary/addrange#addrange_1)(string[][]) | Aggiunge la raccolta specificata di gruppi di sinonimi a questa istanza di[`SynonymDictionary`](../synonymdictionary) . |
| [Clear](../../groupdocs.search.dictionaries/synonymdictionary/clear)() | Rimuove tutte le parole da questo[`SynonymDictionary`](../synonymdictionary) oggetto. |
| [ExportDictionary](../../groupdocs.search.dictionaries/dictionarybase/exportdictionary)(string) | Esporta il dizionario in un file con il nome specificato. |
| [GetAllSynonymGroups](../../groupdocs.search.dictionaries/synonymdictionary/getallsynonymgroups)() | Recupera tutti i gruppi di sinonimi contenuti in questo dizionario. |
| [GetEnumerator](../../groupdocs.search.dictionaries/synonymdictionary/getenumerator)() | Restituisce un enumeratore che scorre la raccolta. |
| [GetSynonymGroups](../../groupdocs.search.dictionaries/synonymdictionary/getsynonymgroups)(string) | Recupera tutti i gruppi di sinonimi a cui appartiene la parola specificata. |
| [GetSynonyms](../../groupdocs.search.dictionaries/synonymdictionary/getsynonyms)(string) | Ottiene i sinonimi per la parola specificata. L'array risultante non contiene la parola originale. |
| [ImportDictionary](../../groupdocs.search.dictionaries/dictionarybase/importdictionary)(string) | Importa un dizionario dal file specificato. |

### Osservazioni

**Saperne di più**

* [Ricerca di sinonimi](https://docs.groupdocs.com/display/searchnet/Synonym+search)
* [Gestione del dizionario dei sinonimi](https://docs.groupdocs.com/display/searchnet/Synonym+dictionary)

### Guarda anche

* class [DictionaryBase](../dictionarybase)
* spazio dei nomi [GroupDocs.Search.Dictionaries](../../groupdocs.search.dictionaries)
* assemblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
