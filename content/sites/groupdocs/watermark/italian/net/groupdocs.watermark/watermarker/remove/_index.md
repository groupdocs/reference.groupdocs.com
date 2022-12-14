---
title: Remove
second_title: Riferimento API GroupDocs.Watermark per .NET
description: Rimuove la filigrana dal documento.
type: docs
weight: 90
url: /it/net/groupdocs.watermark/watermarker/remove/
---
## Remove(PossibleWatermark) {#remove}

Rimuove la filigrana dal documento.

```csharp
public void Remove(PossibleWatermark possibleWatermark)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| possibleWatermark | PossibleWatermark | La filigrana da rimuovere. |

### Osservazioni

Ulteriori informazioni sulla rimozione delle filigrane: [Rimozione delle filigrane trovate](https://docs.groupdocs.com/display/watermarknet/Removing+found+watermarks) .

### Esempi

Trova e rimuovi la prima filigrana possibile contenente testo o immagine particolare da un documento di qualsiasi tipo supportato.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    ImageSearchCriteria imageSearchCriteria = new ImageDctHashSearchCriteria(@"D:\logo.png");
    Regex regex = new Regex(@"^Company\sName$", RegexOptions.IgnoreCase);
    TextSearchCriteria textSearchCriteria = new TextSearchCriteria(regex);
    PossibleWatermarkCollection watermarks = watermarker.Search(textSearchCriteria.Or(imageSearchCriteria));
    if (watermarks.Count > 0)
    {
        watermarker.Remove(watermarks[0]);
    }

    watermarker.Save(@"D:\output.doc");
}
```

### Guarda anche

* class [PossibleWatermark](../../../groupdocs.watermark.search/possiblewatermark)
* class [Watermarker](../../watermarker)
* spazio dei nomi [GroupDocs.Watermark](../../watermarker)
* assemblea [GroupDocs.Watermark](../../../)

---

## Remove(PossibleWatermarkCollection) {#remove_1}

Rimuove tutte le filigrane nella raccolta dal documento.

```csharp
public void Remove(PossibleWatermarkCollection possibleWatermarks)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| possibleWatermarks | PossibleWatermarkCollection | La raccolta di filigrane da rimuovere. |

### Osservazioni

Ulteriori informazioni sulla rimozione delle filigrane [Rimozione delle filigrane trovate](https://docs.groupdocs.com/display/watermarknet/Removing+found+watermarks) .

### Esempi

Trova e rimuovi tutte le possibili filigrane contenenti testo o immagine particolare da un documento di qualsiasi tipo supportato.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    ImageSearchCriteria imageSearchCriteria = new ImageDctHashSearchCriteria(@"D:\logo.png");
    Regex regex = new Regex(@"^Company\sName$", RegexOptions.IgnoreCase);
    TextSearchCriteria textSearchCriteria = new TextSearchCriteria(regex);
    PossibleWatermarkCollection watermarks = watermarker.Search(textSearchCriteria.Or(imageSearchCriteria));
    watermarker.Remove(watermarks);
    watermarker.Save(@"D:\output.doc");
}
```

### Guarda anche

* class [PossibleWatermarkCollection](../../../groupdocs.watermark.search/possiblewatermarkcollection)
* class [Watermarker](../../watermarker)
* spazio dei nomi [GroupDocs.Watermark](../../watermarker)
* assemblea [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
