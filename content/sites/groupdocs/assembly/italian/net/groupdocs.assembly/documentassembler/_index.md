---
title: DocumentAssembler
second_title: Riferimento API GroupDocs.Assembly per .NET
description: Fornisce routine per popolare i documenti modello con dati e una serie di impostazioni per controllare queste routine.
type: docs
weight: 200
url: /it/net/groupdocs.assembly/documentassembler/
---
## DocumentAssembler class

Fornisce routine per popolare i documenti modello con dati e una serie di impostazioni per controllare queste routine.

```csharp
public class DocumentAssembler
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [DocumentAssembler](documentassembler)() | Inizializza una nuova istanza di questa classe. |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [BarcodeSettings](../../groupdocs.assembly/documentassembler/barcodesettings) { get; } | Ottiene una serie di impostazioni che controllano la generazione del codice a barre durante l'assemblaggio di un documento. |
| [KnownTypes](../../groupdocs.assembly/documentassembler/knowntypes) { get; } | Ottiene un set non ordinato (ovvero una raccolta di elementi univoci) contenenteType oggetti i cui nomi completi o parzialmente qualificati possono essere utilizzati all'interno dei modelli di documento elaborati da questa istanza assembler per richiamare i membri statici dei tipi corrispondenti, eseguire cast di tipi, ecc. |
| [Options](../../groupdocs.assembly/documentassembler/options) { get; set; } | Ottiene o imposta un insieme di flag che controllano il comportamento di this[`DocumentAssembler`](../documentassembler) istanza durante l'assemblaggio di un documento. |
| static [UseReflectionOptimization](../../groupdocs.assembly/documentassembler/usereflectionoptimization) { get; set; } | Ottiene o imposta un valore che indica se le chiamate di membri di tipo personalizzato eseguite tramite l'API reflection sono ottimizzate utilizzando la generazione di classi dinamiche o meno. Il valore predefinito è true. |

## Metodi

| Nome | Descrizione |
| --- | --- |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument)(Stream, Stream, params DataSourceInfo[]) | Carica un documento modello dal flusso di origine specificato, popola il documento modello con i dati provenienti da le origini singole o multiple specificate e memorizza il documento risultante nel flusso di destinazione utilizzando default [`LoadSaveOptions`](../loadsaveoptions) . |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument_2)(string, string, params DataSourceInfo[]) | Carica un documento modello dal percorso di origine specificato, popola il documento modello con i dati provenienti da le origini singole o multiple specificate e memorizza il documento risultante nel percorso di destinazione utilizzando default [`LoadSaveOptions`](../loadsaveoptions) . |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument_1)(Stream, Stream, LoadSaveOptions, params DataSourceInfo[]) | Carica un documento modello dal flusso di origine specificato, popola il documento modello con i dati provenienti da le origini singole o multiple specificate e memorizza il documento risultante nel flusso di destinazione utilizzando il given [`LoadSaveOptions`](../loadsaveoptions) . |
| [AssembleDocument](../../groupdocs.assembly/documentassembler/assembledocument#assembledocument_3)(string, string, LoadSaveOptions, params DataSourceInfo[]) | Carica un documento modello dal percorso di origine specificato, popola il documento modello con i dati provenienti da le origini singole o multiple specificate e memorizza il documento risultante nel percorso di destinazione utilizzando given [`LoadSaveOptions`](../loadsaveoptions) . |

### Guarda anche

* spazio dei nomi [GroupDocs.Assembly](../../groupdocs.assembly)
* assemblea [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
