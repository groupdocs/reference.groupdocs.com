---
title: SplitHeadingLevel
second_title: GroupDocs.Editor per Riferimento API .NET
description: Specifica se suddividere il contenuto dellebook AZW3 in pacchetti e in caso affermativo il livello massimo di intestazioni a cui suddividere il contenuto dellAZW3. Il valore predefinito è2 . Impostandolo su0disabiliterà la divisione quindi tutto il contenuto dellebook verrà incorporato in un unico pacchetto allinterno dellAZW3.
type: docs
weight: 20
url: /it/net/groupdocs.editor.options/azw3saveoptions/splitheadinglevel/
---
## Azw3SaveOptions.SplitHeadingLevel property

Specifica se suddividere il contenuto dell'e-book AZW3 in pacchetti e, in caso affermativo, il livello massimo di intestazioni a cui suddividere il contenuto dell'AZW3. Il valore predefinito è`2` . Impostandolo su`0`disabiliterà la divisione, quindi tutto il contenuto dell'e-book verrà incorporato in un unico pacchetto all'interno dell'AZW3.

```csharp
public int SplitHeadingLevel { get; set; }
```

### Osservazioni

In alcuni casi è preferibile suddividere il contenuto dell'e-book in diversi pacchetti più piccoli, situati all'interno del file AZW3 di output. Questa proprietà controlla se tale separazione deve essere eseguita e, in caso affermativo, come.

Quando questa proprietà è impostata su un valore compreso tra 1 e 9, il documento verrà suddiviso in paragrafi formattati utilizzando **Titolo 1** ,**Titolo 2** ,**Titolo 3** ecc. stili fino al livello di intestazione specificato.

Per impostazione predefinita (valore di`2` ), soltanto**Titolo 1** E**Titolo 2** i paragrafi causano la divisione del documento. L'impostazione di questa proprietà su zero farà sì che il documento non venga affatto suddiviso in corrispondenza dei paragrafi di intestazione.

### Guarda anche

* class [Azw3SaveOptions](../../azw3saveoptions)
* spazio dei nomi [GroupDocs.Editor.Options](../../azw3saveoptions)
* assemblea [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
