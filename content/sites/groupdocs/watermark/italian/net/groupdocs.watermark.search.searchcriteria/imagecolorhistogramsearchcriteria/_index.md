---
title: ImageColorHistogramSearchCriteria
second_title: Riferimento API GroupDocs.Watermark per .NET
description: Rappresenta i criteri di ricerca per trovare immagini in un contenuto.
type: docs
weight: 2580
url: /it/net/groupdocs.watermark.search.searchcriteria/imagecolorhistogramsearchcriteria/
---
## ImageColorHistogramSearchCriteria class

Rappresenta i criteri di ricerca per trovare immagini in un contenuto.

```csharp
public class ImageColorHistogramSearchCriteria : ImageSearchCriteria
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [ImageColorHistogramSearchCriteria](imagecolorhistogramsearchcriteria#constructor)(Stream) | Inizializza una nuova istanza di[`ImageColorHistogramSearchCriteria`](../imagecolorhistogramsearchcriteria) classe con un flusso specificato. |
| [ImageColorHistogramSearchCriteria](imagecolorhistogramsearchcriteria#constructor_1)(string) | Inizializza una nuova istanza di[`ImageColorHistogramSearchCriteria`](../imagecolorhistogramsearchcriteria) classe con un percorso di file specificato. |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [BinsCount](../../groupdocs.watermark.search.searchcriteria/imagecolorhistogramsearchcriteria/binscount) { get; set; } | Ottiene o imposta un numero di contenitori che verranno utilizzati per la creazione di istogrammi colore. |
| [MaxDifference](../../groupdocs.watermark.search.searchcriteria/imagesearchcriteria/maxdifference) { get; set; } | Ottiene o imposta la differenza massima consentita tra le immagini. |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [And](../../groupdocs.watermark.search.searchcriteria/searchcriteria/and)(SearchCriteria) | Combina questo[`SearchCriteria`](../searchcriteria) con altri criteri utilizzando l'operatore AND logico. |
| [Not](../../groupdocs.watermark.search.searchcriteria/searchcriteria/not)() | Nega questo[`SearchCriteria`](../searchcriteria) . |
| [Or](../../groupdocs.watermark.search.searchcriteria/searchcriteria/or)(SearchCriteria) | Combina questo[`SearchCriteria`](../searchcriteria) con altri criteri utilizzando l'operatore OR logico. |

### Osservazioni

Questo criterio di ricerca utilizza gli istogrammi del colore dell'immagine per calcolare la somiglianza dell'immagine.

### Guarda anche

* class [ImageSearchCriteria](../imagesearchcriteria)
* spazio dei nomi [GroupDocs.Watermark.Search.SearchCriteria](../../groupdocs.watermark.search.searchcriteria)
* assemblea [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
