---
title: DocumentTableSet
second_title: Riferimento API GroupDocs.Assembly per .NET
description: Fornisce laccesso ai dati di più tabelle o fogli di calcolo situati in un documento esterno da utilizzare durante lassemblaggio di un documento. Inoltre consente di definire relazioni padrefiglio per le tabelle del documento semplificando così laccesso ai dati correlati allinterno dei documenti modello.
type: docs
weight: 120
url: /it/net/groupdocs.assembly.data/documenttableset/
---
## DocumentTableSet class

Fornisce l'accesso ai dati di più tabelle (o fogli di calcolo) situati in un documento esterno da utilizzare durante l'assemblaggio di un documento. Inoltre, consente di definire relazioni padre-figlio per le tabelle del documento semplificando così l'accesso ai dati correlati all'interno dei documenti modello.

```csharp
public class DocumentTableSet
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [DocumentTableSet](documenttableset#constructor)(Stream) | Crea una nuova istanza di questa classe caricando tutte le tabelle da un documento utilizzando predefinito[`DocumentTableOptions`](../documenttableoptions) . |
| [DocumentTableSet](documenttableset#constructor_2)(string) | Crea una nuova istanza di questa classe caricando tutte le tabelle da un documento utilizzando predefinito[`DocumentTableOptions`](../documenttableoptions) . |
| [DocumentTableSet](documenttableset#constructor_1)(Stream, IDocumentTableLoadHandler) | Crea una nuova istanza di questa classe. |
| [DocumentTableSet](documenttableset#constructor_3)(string, IDocumentTableLoadHandler) | Crea una nuova istanza di questa classe. |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [Relations](../../groupdocs.assembly.data/documenttableset/relations) { get; } | Ottiene la raccolta delle relazioni padre-figlio definite per le tabelle dei documenti di questo insieme. |
| [Tables](../../groupdocs.assembly.data/documenttableset/tables) { get; } | Ottiene la raccolta di[`DocumentTable`](../documenttable) oggetti che rappresentano le tabelle di questo set. |

### Osservazioni

Per i documenti nei formati di file Spreadsheet, a[`DocumentTableSet`](../documenttableset) instance rappresenta un insieme di fogli. Per documenti di altri formati di file, a[`DocumentTableSet`](../documenttableset) l'istanza rappresenta un insieme di tabelle.

Per accedere ai dati delle tabelle corrispondenti durante l'assemblaggio di un documento, passare un'istanza di questa classe come un'origine dati a uno dei[`DocumentAssembler`](../../groupdocs.assembly/documentassembler) .AssembleDocument sovraccarichi.

Nei documenti modello, a[`DocumentTableSet`](../documenttableset) instance dovrebbe essere trattato come se fosse aDataSet esempio. Per ulteriori informazioni, vedere il riferimento alla sintassi del modello.

### Guarda anche

* spazio dei nomi [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* assemblea [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
