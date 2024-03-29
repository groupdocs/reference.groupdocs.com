---
title: SearchResult
second_title: GroupDocs.Cerca il riferimento dell'API .NET
description: Rappresenta un risultato di ricerca che corrisponde a una query di ricerca.
type: docs
weight: 1230
url: /it/net/groupdocs.search.results/searchresult/
---
## SearchResult class

Rappresenta un risultato di ricerca che corrisponde a una query di ricerca.

```csharp
public class SearchResult : IEnumerable<FoundDocument>
```

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [DocumentCount](../../groupdocs.search.results/searchresult/documentcount) { get; } | Ottiene il numero di documenti trovati. |
| [EndTime](../../groupdocs.search.results/searchresult/endtime) { get; } | Ottiene l'ora di fine della ricerca. |
| [NextChunkSearchToken](../../groupdocs.search.results/searchresult/nextchunksearchtoken) { get; } | Ottiene un token di ricerca del blocco per cercare il blocco successivo. |
| [OccurrenceCount](../../groupdocs.search.results/searchresult/occurrencecount) { get; } | Ottiene il numero totale di occorrenze trovate. |
| [SearchDuration](../../groupdocs.search.results/searchresult/searchduration) { get; } | Ottiene la durata della ricerca. |
| [StartTime](../../groupdocs.search.results/searchresult/starttime) { get; } | Ottiene l'ora di inizio della ricerca. |
| [Truncated](../../groupdocs.search.results/searchresult/truncated) { get; } | Ottiene un valore che indica che il risultato è troncato. |
| [Warnings](../../groupdocs.search.results/searchresult/warnings) { get; } | Ottiene un avviso che descrive il risultato. |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [GetEnumerator](../../groupdocs.search.results/searchresult/getenumerator)() | Restituisce un enumeratore che scorre la raccolta dei documenti trovati. |
| [GetFoundDocument](../../groupdocs.search.results/searchresult/getfounddocument)(int) | Ottiene il documento trovato per indice. |

### Osservazioni

**Saperne di più**

* [Ricerca](https://docs.groupdocs.com/display/searchnet/Searching)
* [Risultati di ricerca](https://docs.groupdocs.com/display/searchnet/Search+results)

### Esempi

L'esempio mostra un utilizzo tipico della classe.

```csharp
string indexFolder = @"c:\MyIndex\";
string documentFolder = @"c:\MyDocuments\";

// Creazione di un indice
Index index = new Index(indexFolder);

// Indicizzazione dei documenti dalla cartella specificata
index.Add(documentFolder);

// Impostazione delle opzioni di ricerca
SearchOptions options = new SearchOptions();
options.FuzzySearch.Enabled = true; // Abilitazione della ricerca fuzzy
options.FuzzySearch.FuzzyAlgorithm = new TableDiscreteFunction(3); // Imposta il numero massimo di differenze su 3

// Cerca documenti contenenti la parola "Einstein" o la frase "Teoria della relatività"
SearchResult result = index.Search("Einstein OR \"Theory of Relativity\"", options);

// Stampa il risultato
Console.WriteLine("Documents: " + result.DocumentCount);
Console.WriteLine("Total occurrences: " + result.OccurrenceCount);
for (int i = 0; i < result.DocumentCount; i++)
{
    FoundDocument document = result.GetFoundDocument(i);
    Console.WriteLine("\tDocument: " + document.DocumentInfo.FilePath);
    Console.WriteLine("\tOccurrences: " + document.OccurrenceCount);
    for (int j = 0; j < document.FoundFields.Length; j++)
    {
        FoundDocumentField field = document.FoundFields[j];
        Console.WriteLine("\t\tField: " + field.FieldName);
        Console.WriteLine("\t\tOccurrences: " + document.OccurrenceCount);
        // Stampa termini trovati
        if (field.Terms != null)
        {
            for (int k = 0; k < field.Terms.Length; k++)
            {
                Console.WriteLine("\t\t\t" + field.Terms[k].PadRight(20) + field.TermsOccurrences[k]);
            }
        }
        // Stampa frasi trovate
        if (field.TermSequences != null)
        {
            for (int k = 0; k < field.TermSequences.Length; k++)
            {
                string sequence = string.Join(" ", field.TermSequences[k]);
                Console.WriteLine("\t\t\t" + sequence.PadRight(30) + field.TermSequencesOccurrences[k]);
            }
        }
    }
}
```

### Guarda anche

* class [FoundDocument](../founddocument)
* spazio dei nomi [GroupDocs.Search.Results](../../groupdocs.search.results)
* assemblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
