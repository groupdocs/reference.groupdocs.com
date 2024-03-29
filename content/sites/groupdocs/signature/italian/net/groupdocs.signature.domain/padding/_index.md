---
title: Padding
second_title: Riferimento API GroupDocs.Signature per .NET
description: Rappresenta il riempimento o le informazioni sui margini associate allelemento.
type: docs
weight: 640
url: /it/net/groupdocs.signature.domain/padding/
---
## Padding class

Rappresenta il riempimento o le informazioni sui margini associate all'elemento.

```csharp
public class Padding : ICloneable
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [Padding](padding#constructor)() | Inizializza una nuova istanza della classe Padding utilizzando valori zero. |
| [Padding](padding#constructor_1)(int) | Inizializza una nuova istanza della classe Padding utilizzando la dimensione di riempimento fornita per tutti i bordi. |
| [Padding](padding#constructor_2)(int, int, int, int) | Inizializza una nuova istanza della classe Padding utilizzando le dimensioni di riempimento fornite. |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [All](../../groupdocs.signature.domain/padding/all) { get; set; } | Ottiene o imposta il valore di riempimento per tutti i bordi. La modifica di qualsiasi bordo parziale come left o top rende questa proprietà uguale a 0; |
| [Bottom](../../groupdocs.signature.domain/padding/bottom) { get; set; } | Ottiene o imposta il valore di riempimento per il bordo inferiore. |
| [Horizontal](../../groupdocs.signature.domain/padding/horizontal) { get; } | Ottiene il riempimento combinato per i bordi destro e sinistro. |
| [Left](../../groupdocs.signature.domain/padding/left) { get; set; } | Ottiene o imposta il valore di riempimento per il bordo sinistro. |
| [Right](../../groupdocs.signature.domain/padding/right) { get; set; } | Ottiene o imposta il valore di riempimento per il bordo destro. |
| [Top](../../groupdocs.signature.domain/padding/top) { get; set; } | Ottiene o imposta il valore di riempimento per il bordo superiore. |
| [Vertical](../../groupdocs.signature.domain/padding/vertical) { get; } | Ottiene il riempimento combinato per i bordi superiore e inferiore. |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [Clone](../../groupdocs.signature.domain/padding/clone)() | Ottiene una copia di questo oggetto. |

## Campi

| Nome | Descrizione |
| --- | --- |
| static readonly [Empty](../../groupdocs.signature.domain/padding/empty) | Fornisce un oggetto Padding senza padding. |

### Guarda anche

* spazio dei nomi [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* assemblea [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
