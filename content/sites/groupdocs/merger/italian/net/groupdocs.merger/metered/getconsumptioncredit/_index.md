---
title: GetConsumptionCredit
second_title: Riferimento API GroupDocs.Merger per .NET
description: Recupera la quantità di crediti utilizzati
type: docs
weight: 30
url: /it/net/groupdocs.merger/metered/getconsumptioncredit/
---
## Metered.GetConsumptionCredit method

Recupera la quantità di crediti utilizzati

```csharp
public static decimal GetConsumptionCredit()
```

### Esempi

L'esempio seguente mostra come recuperare la quantità di MB elaborati.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal usedCredits = Metered.GetConsumptionCredit();
```

### Guarda anche

* class [Metered](../../metered)
* spazio dei nomi [GroupDocs.Merger](../../metered)
* assemblea [GroupDocs.Merger](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
