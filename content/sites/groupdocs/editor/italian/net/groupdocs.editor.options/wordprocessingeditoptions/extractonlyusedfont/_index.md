---
title: ExtractOnlyUsedFont
second_title: GroupDocs.Editor per Riferimento API .NET
description: Ottiene o imposta un valore che indica se estrarre solo le risorse dei caratteri utilizzate nel contenuto testuale del documento.
type: docs
weight: 40
url: /it/net/groupdocs.editor.options/wordprocessingeditoptions/extractonlyusedfont/
---
## WordProcessingEditOptions.ExtractOnlyUsedFont property

Ottiene o imposta un valore che indica se estrarre solo le risorse dei caratteri utilizzate nel contenuto testuale del documento.

```csharp
public bool ExtractOnlyUsedFont { get; set; }
```

### Valore della proprietà

`VERO` se è necessario estrarre solo quelle risorse di carattere utilizzate nel contenuto testuale del documento; Altrimenti,`falso` . Il valore predefinito è`falso` .

### Osservazioni

Non tutti i font, usati nel documento WordProcessing, sono usati direttamente al 100% (applicati a del testo). Potrebbe esserci una situazione in cui il carattere è referenziato nel documento e può anche essere incorporato, ma non viene applicato a nessuna parte di testo. Ad esempio, alcuni caratteri possono essere associati a uno stile, ma questo stile non viene applicato a nessuna parte del testo. Questa opzione controlla come elaborare tali casi.

### Guarda anche

* class [WordProcessingEditOptions](../../wordprocessingeditoptions)
* spazio dei nomi [GroupDocs.Editor.Options](../../wordprocessingeditoptions)
* assemblea [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
