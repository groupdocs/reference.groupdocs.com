---
title: IndexSettings
second_title: GroupDocs.Cerca il riferimento dell'API .NET
description: Rappresenta le impostazioni dellindice che consentono di personalizzare le operazioni di indicizzazione.
type: docs
weight: 700
url: /it/net/groupdocs.search/indexsettings/
---
## IndexSettings class

Rappresenta le impostazioni dell'indice che consentono di personalizzare le operazioni di indicizzazione.

```csharp
public class IndexSettings
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [IndexSettings](indexsettings)() | Inizializza una nuova istanza di[`IndexSettings`](../indexsettings) classe. |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [AutoDetectEncoding](../../groupdocs.search/indexsettings/autodetectencoding) { get; set; } | Ottiene o imposta un valore che indica se rilevare automaticamente o meno la codifica. Il valore predefinito è`falso` . |
| [CustomExtractors](../../groupdocs.search/indexsettings/customextractors) { get; } | Ottiene la raccolta di estrattori personalizzati. |
| [DocumentFilter](../../groupdocs.search/indexsettings/documentfilter) { get; set; } | Ottiene o imposta un filtro documento. The[`DocumentFilter`](./documentfilter) lavora sulla logica di inclusione. Usa il[`DocumentFilter`](../../groupdocs.search.options/documentfilter) class per la creazione di un documento filter instances. Il valore predefinito è`nullo` , il che significa che tutti i documenti aggiunti vengono indicizzati. |
| [IndexType](../../groupdocs.search/indexsettings/indextype) { get; set; } | Ottiene o imposta il tipo di indice. Il valore predefinito èNormalIndex . |
| [InMemoryIndex](../../groupdocs.search/indexsettings/inmemoryindex) { get; } | Ottiene un valore che indica se l'indice è archiviato in memoria o su disco. |
| [Logger](../../groupdocs.search/indexsettings/logger) { get; set; } | Ottiene o imposta un logger utilizzato per la registrazione di eventi ed errori nell'indice. Si noti che il logger non viene salvato e deve essere creato e assegnato ogni volta che l'indice viene creato o caricato. |
| [MaxIndexingReportCount](../../groupdocs.search/indexsettings/maxindexingreportcount) { get; set; } | Ottiene o imposta il numero massimo di rapporti di indicizzazione. Il valore predefinito è`5` . |
| [MaxSearchReportCount](../../groupdocs.search/indexsettings/maxsearchreportcount) { get; set; } | Ottiene o imposta il numero massimo di rapporti di ricerca. Il valore predefinito è`10` . |
| [SearchThreads](../../groupdocs.search/indexsettings/searchthreads) { get; set; } | Ottiene o imposta il numero di thread utilizzati per la ricerca. Il valore predefinito èDefault , che significa che la ricerca verrà eseguita utilizzando il numero di thread pari al numero di core del processore. |
| [TextStorageSettings](../../groupdocs.search/indexsettings/textstoragesettings) { get; set; } | Ottiene o imposta le impostazioni di archiviazione del testo. Il valore predefinito è`nullo` , il che significa che i testi del documento non vengono memorizzati. |
| [UseCharacterReplacements](../../groupdocs.search/indexsettings/usecharacterreplacements) { get; set; } | Ottiene o imposta un valore che indica se utilizzare o meno la sostituzione dei caratteri. Il valore predefinito è`falso` . |
| [UseRawTextExtraction](../../groupdocs.search/indexsettings/userawtextextraction) { get; set; } | Ottiene o imposta un valore che indica se la modalità raw viene utilizzata per l'estrazione del testo, se possibile. Il valore predefinito è`VERO` . La modalità raw può aumentare significativamente la velocità di indicizzazione, ma la modalità normale migliora la formattazione del testo estratto. |
| [UseStopWords](../../groupdocs.search/indexsettings/usestopwords) { get; set; } | Ottiene o imposta un valore che indica se utilizzare parole non significative o meno. Il valore predefinito è`VERO` . |

### Osservazioni

**Saperne di più**

* [Impostazioni dell'indice di ricerca](https://docs.groupdocs.com/display/searchnet/Search+index+settings)

### Esempi

L'esempio mostra un utilizzo tipico della classe.

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex; // Impostazione del tipo di indice

Index index = new Index(indexFolder, settings); // Creazione di un indice
```

### Guarda anche

* spazio dei nomi [GroupDocs.Search](../../groupdocs.search)
* assemblea [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
