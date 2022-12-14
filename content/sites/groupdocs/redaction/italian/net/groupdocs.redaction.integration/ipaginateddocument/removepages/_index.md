---
title: RemovePages
second_title: Riferimento API GroupDocs.Redaction per .NET
description: Rimuove una o più pagine a seconda della posizione iniziale delloffset e del conteggio.
type: docs
weight: 10
url: /it/net/groupdocs.redaction.integration/ipaginateddocument/removepages/
---
## IPaginatedDocument.RemovePages method

Rimuove una o più pagine a seconda della posizione iniziale, dell'offset e del conteggio.

```csharp
public RedactionResult RemovePages(PageSeekOrigin origin, int index, int count)
```

| Parametro | Tipo | Descrizione |
| --- | --- | --- |
| origin | PageSeekOrigin | Cerca la posizione di origine, l'inizio o la fine del documento |
| index | Int32 | Indice della posizione iniziale (in base a 0) |
| count | Int32 | Numero di pagine da rimuovere |

### Valore di ritorno

Risultato della redazione della rimozione delle pagine

### Guarda anche

* class [RedactionResult](../../../groupdocs.redaction/redactionresult)
* enum [PageSeekOrigin](../../../groupdocs.redaction.redactions/pageseekorigin)
* interface [IPaginatedDocument](../../ipaginateddocument)
* spazio dei nomi [GroupDocs.Redaction.Integration](../../ipaginateddocument)
* assemblea [GroupDocs.Redaction](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
