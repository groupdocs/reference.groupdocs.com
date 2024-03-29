---
title: GetData
second_title: Riferimento API GroupDocs.Signature per .NET
description: Ottieni loggetto dal valore della firma dei metadati tramite la deserializzazione.
type: docs
weight: 70
url: /it/net/groupdocs.signature.domain/metadatasignature/getdata/
---
## GetData&lt;T&gt;() {#getdata}

Ottieni l'oggetto dal valore della firma dei metadati tramite la deserializzazione.

```csharp
public T GetData<T>()
    where T : class
```

| Parametro | Descrizione |
| --- | --- |
| T | Tipo di oggetto da deserializzare dal valore dei metadati |

### Valore di ritorno

Istanza dell'oggetto T

### Guarda anche

* class [MetadataSignature](../../metadatasignature)
* spazio dei nomi [GroupDocs.Signature.Domain](../../metadatasignature)
* assemblea [GroupDocs.Signature](../../../)

---

## GetData&lt;T&gt;(IDataEncryption) {#getdata_1}

Ottieni l'oggetto dal testo della firma dei metadati tramite la deserializzazione.

```csharp
public T GetData<T>(IDataEncryption dataEncryption)
    where T : class
```

| Parametro | Descrizione |
| --- | --- |
| T | Tipo di oggetto da deserializzare dal valore dei metadati |
| dataEncryption | Imposta l'implementazione della crittografia dei dati personalizzata |

### Guarda anche

* interface [IDataEncryption](../../../groupdocs.signature.domain.extensions/idataencryption)
* class [MetadataSignature](../../metadatasignature)
* spazio dei nomi [GroupDocs.Signature.Domain](../../metadatasignature)
* assemblea [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
