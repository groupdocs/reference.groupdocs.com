---
title: FromExtension
second_title: Riferimento API GroupDocs.Signature per .NET
description: Associa lestensione del file al tipo di file.
type: docs
weight: 580
url: /it/net/groupdocs.signature.domain/filetype/fromextension/
---
## FileType.FromExtension method

Associa l'estensione del file al tipo di file.

```csharp
public static FileType FromExtension(string extension)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| extension | String | Estensione del file (incluso il punto "."). |

### Valore di ritorno

Quando il tipo di file è supportato lo restituisce, altrimenti restituisce default[`Unknown`](../unknown) tipo di file.

### Eccezioni

| eccezione | condizione |
| --- | --- |
| ArgumentException | Lanciato quando*extension* è una stringa nulla o vuota. |

### Guarda anche

* class [FileType](../../filetype)
* spazio dei nomi [GroupDocs.Signature.Domain](../../filetype)
* assemblea [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
