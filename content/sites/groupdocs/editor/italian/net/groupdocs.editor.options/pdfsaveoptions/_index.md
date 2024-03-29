---
title: PdfSaveOptions
second_title: GroupDocs.Editor per Riferimento API .NET
description: Consente di specificare opzioni personalizzate per la generazione e il salvataggio di documenti PDF Portable Document Format
type: docs
weight: 1060
url: /it/net/groupdocs.editor.options/pdfsaveoptions/
---
## PdfSaveOptions class

Consente di specificare opzioni personalizzate per la generazione e il salvataggio di documenti PDF (Portable Document Format)

```csharp
public sealed class PdfSaveOptions : ISaveOptions
```

## Costruttori

| Nome | Descrizione |
| --- | --- |
| [PdfSaveOptions](pdfsaveoptions)() | Default_Costruttore |

## Proprietà

| Nome | Descrizione |
| --- | --- |
| [Compliance](../../groupdocs.editor.options/pdfsaveoptions/compliance) { get; set; } | Specifica il livello di conformità agli standard PDF per i documenti di output. L'impostazione predefinita è PdfCompliance.Pdf17. |
| [FontEmbedding](../../groupdocs.editor.options/pdfsaveoptions/fontembedding) { get; set; } | Responsabile dell'incorporamento delle risorse dei caratteri, utilizzate nel documento originale, nel documento PDF risultante. Per impostazione predefinita non incorpora alcun tipo di carattere (NotEmbed). |
| [OptimizeMemoryUsage](../../groupdocs.editor.options/pdfsaveoptions/optimizememoryusage) { get; set; } | Abilita i meccanismi di ottimizzazione della memoria durante la generazione di documenti da HTML, che degradano le prestazioni come costo della riduzione dell'utilizzo della memoria. L'impostazione di questa opzione su true può ridurre significativamente il consumo di memoria durante la generazione di documenti di grandi dimensioni al costo di un tempo di salvataggio più lento. L'impostazione predefinita è false (l'ottimizzazione della memoria è disabilitata per migliorare le prestazioni). |
| [Password](../../groupdocs.editor.options/pdfsaveoptions/password) { get; set; } | Password, che verrà applicata al documento PDF generato come password utente, necessaria per l'apertura. Se NULL o vuoto, nessuna password verrà applicata al documento. In caso contrario, il documento verrà crittografato con RC4 (lunghezza della chiave di 128 bit). Per impostazione predefinita è NULL — la password non viene applicata. |

### Guarda anche

* interface [ISaveOptions](../isaveoptions)
* spazio dei nomi [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* assemblea [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
