---
title: SearchOptions
second_title: Riferimento API GroupDocs.Parser per .NET
description: Fornisce le opzioni utilizzate per la ricerca di testo.
type: docs
weight: 610
url: /it/net/groupdocs.parser.options/searchoptions/
---
## SearchOptions class

Fornisce le opzioni utilizzate per la ricerca di testo.

```csharp
public sealed class SearchOptions
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [SearchOptions](searchoptions#constructor)() | Inizializza una nuova istanza di[`SearchOptions`](../searchoptions) classe con valori predefiniti. Vedere le osservazioni per i dettagli. |
| [SearchOptions](searchoptions#constructor_1)(bool, bool, bool) | Inizializza una nuova istanza di[`SearchOptions`](../searchoptions) classe che viene utilizzata per search senza estrazione di evidenziazione. |
| [SearchOptions](searchoptions#constructor_2)(bool, bool, bool, bool) | Inizializza una nuova istanza di[`SearchOptions`](../searchoptions)classe che viene utilizzata per cercare per pagine e senza estrazione dell'evidenziazione. |
| [SearchOptions](searchoptions#constructor_4)(bool, bool, bool, HighlightOptions) | Inizializza una nuova istanza di[`SearchOptions`](../searchoptions) class che viene utilizzata per search con le stesse opzioni di evidenziazione per l'estrazione dell'evidenziazione sinistra e destra. |
| [SearchOptions](searchoptions#constructor_5)(bool, bool, bool, HighlightOptions, HighlightOptions) | Inizializza una nuova istanza di[`SearchOptions`](../searchoptions) classe che viene utilizzata per search con le opzioni di evidenziazione per l'estrazione dell'evidenziazione sinistra e destra. |
| [SearchOptions](searchoptions#constructor_3)(bool, bool, bool, bool, HighlightOptions, HighlightOptions) | Inizializza una nuova istanza di[`SearchOptions`](../searchoptions) classe. |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [LeftHighlightOptions](../../groupdocs.parser.options/searchoptions/lefthighlightoptions) { get; } | Ottiene le opzioni per l'evidenziazione a sinistra. |
| [MatchCase](../../groupdocs.parser.options/searchoptions/matchcase) { get; } | Ottiene il valore che indica se un caso di testo non viene ignorato. |
| [MatchWholeWord](../../groupdocs.parser.options/searchoptions/matchwholeword) { get; } | Ottiene il valore che indica se la ricerca di testo è limitata da una parola intera. |
| [RightHighlightOptions](../../groupdocs.parser.options/searchoptions/righthighlightoptions) { get; } | Ottiene le opzioni per l'evidenziazione a destra. |
| [SearchByPages](../../groupdocs.parser.options/searchoptions/searchbypages) { get; } | Ottiene il valore che indica se la ricerca viene eseguita per pagine. |
| [UseRegularExpression](../../groupdocs.parser.options/searchoptions/useregularexpression) { get; } | Ottiene il valore che indica se viene utilizzata un'espressione regolare. |

### Osservazioni

Un'istanza di[`SearchOptions`](../searchoptions) la classe viene utilizzata come parametro in[`Search`](../../groupdocs.parser/parser/search) metodo. Guarda gli esempi di utilizzo qui.

**Saperne di più:**

* [Cerca testo](https://docs.groupdocs.com/display/parsernet/Search+text)
* [Cerca testo nei documenti di Microsoft Office Word](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+Office+Word+documents)
* [Cerca testo nei fogli di calcolo di Microsoft Office Excel](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+Office+Excel+spreadsheets)
* [Cerca testo nelle presentazioni di Microsoft Office PowerPoint](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+Office+PowerPoint+presentations)
* [Cerca testo nei documenti PDF](https://docs.groupdocs.com/display/parsernet/Search+text+in+PDF+documents)
* [Cerca testo nelle e-mail](https://docs.groupdocs.com/display/parsernet/Search+text+in+Emails)
* [Cerca il testo negli eBook EPUB](https://docs.groupdocs.com/display/parsernet/Search+text+in+EPUB+eBooks)
* [Cerca testo nei documenti HTML](https://docs.groupdocs.com/display/parsernet/Search+text+in+HTML+documents)
* [Cerca testo nelle sezioni di Microsoft OneNote](https://docs.groupdocs.com/display/parsernet/Search+text+in+Microsoft+OneNote+sections)

### Guarda anche

* spazio dei nomi [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* assemblea [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
