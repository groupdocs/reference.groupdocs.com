---
title: AddRange
second_title: GroupDocs.Cerca il riferimento dell'API .NET
description: Aggiunge la raccolta specificata di gruppi di sinonimi a questa istanza diSynonymDictionarygroupdocs.search.dictionaries/synonymdictionary .
type: docs
weight: 20
url: /it/net/groupdocs.search.dictionaries/synonymdictionary/addrange/
---
## AddRange(IEnumerable&lt;string[]&gt;) {#addrange}

Aggiunge la raccolta specificata di gruppi di sinonimi a questa istanza di[`SynonymDictionary`](../../synonymdictionary) .

```csharp
public void AddRange(IEnumerable<string[]> synonyms)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| synonyms | IEnumerable`1 | Raccolta di gruppi di sinonimi da aggiungere al dizionario. |

### Eccezioni

| eccezione | condizione |
| --- | --- |
| ArgumentNullException | Lanciato quando*synonyms* È`nullo`. |
| ArgumentException | Generato quando il numero di sinonimi in un gruppo è inferiore a 2. |

### Guarda anche

* class [SynonymDictionary](../../synonymdictionary)
* spazio dei nomi [GroupDocs.Search.Dictionaries](../../synonymdictionary)
* assemblea [GroupDocs.Search](../../../)

---

## AddRange(string[][]) {#addrange_1}

Aggiunge la raccolta specificata di gruppi di sinonimi a questa istanza di[`SynonymDictionary`](../../synonymdictionary) .

```csharp
public void AddRange(string[][] synonyms)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| synonyms | String[][] | Raccolta di gruppi di sinonimi da aggiungere al dizionario. |

### Eccezioni

| eccezione | condizione |
| --- | --- |
| ArgumentNullException | Lanciato quando*synonyms* È`nullo`. |
| ArgumentException | Generato quando il numero di sinonimi in un gruppo è inferiore a 2. |

### Guarda anche

* class [SynonymDictionary](../../synonymdictionary)
* spazio dei nomi [GroupDocs.Search.Dictionaries](../../synonymdictionary)
* assemblea [GroupDocs.Search](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
