---
title: DetectBarcodeTypes
second_title: Riferimento API GroupDocs.Metadata per .NET
description: Estrae i tipi dei codici a barre presentati nellimmagine.
type: docs
weight: 60
url: /it/net/groupdocs.metadata.formats.image/jpegrootpackage/detectbarcodetypes/
---
## JpegRootPackage.DetectBarcodeTypes method

Estrae i tipi dei codici a barre presentati nell'immagine.

```csharp
public string[] DetectBarcodeTypes()
```

### Valore di ritorno

Un array di tipi di codici a barre.

### Osservazioni

**Saperne di più**

* [Lavorare con i metadati nelle immagini JPEG](https://docs.groupdocs.com/display/metadatanet/Working+with+metadata+in+JPEG+images)

### Esempi

Questo frammento di codice mostra come rilevare i codici a barre in un'immagine JPEG.

```csharp
using (Metadata metadata = new Metadata(Constants.JpegWithBarcodes))
{
    var root = metadata.GetRootPackage<JpegRootPackage>();

    var barcodeTypes = root.DetectBarcodeTypes();

    foreach (var barcodeType in barcodeTypes)
    {
        Console.WriteLine(barcodeType);
    }
}
```

### Guarda anche

* class [JpegRootPackage](../../jpegrootpackage)
* spazio dei nomi [GroupDocs.Metadata.Formats.Image](../../jpegrootpackage)
* assemblea [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
