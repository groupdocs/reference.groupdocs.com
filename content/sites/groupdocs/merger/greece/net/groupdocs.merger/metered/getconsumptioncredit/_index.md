---
title: GetConsumptionCredit
second_title: GroupDocs.Merger for .NET API Reference
description: Ανακτά το ποσό των χρησιμοποιημένων πιστώσεων
type: docs
weight: 30
url: /el/net/groupdocs.merger/metered/getconsumptioncredit/
---
## Metered.GetConsumptionCredit method

Ανακτά το ποσό των χρησιμοποιημένων πιστώσεων

```csharp
public static decimal GetConsumptionCredit()
```

### Παραδείγματα

Το ακόλουθο παράδειγμα δείχνει πώς να ανακτήσετε την ποσότητα των MB που έχουν υποστεί επεξεργασία.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal usedCredits = Metered.GetConsumptionCredit();
```

### Δείτε επίσης

* class [Metered](../../metered)
* χώρος ονομάτων [GroupDocs.Merger](../../metered)
* συνέλευση [GroupDocs.Merger](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Merger.dll -->
