---
title: GetConsumptionQuantity
second_title: GroupDocs.Parser για Αναφορά API .NET
description: Ανακτά την ποσότητα των MB που έχουν υποστεί επεξεργασία.
type: docs
weight: 40
url: /el/net/groupdocs.parser/metered/getconsumptionquantity/
---
## Metered.GetConsumptionQuantity method

Ανακτά την ποσότητα των MB που έχουν υποστεί επεξεργασία.

```csharp
public static decimal GetConsumptionQuantity()
```

### Επιστρεφόμενη Αξία

Μια δεκαδική τιμή που αντιπροσωπεύει την ποσότητα κατανάλωσης.

### Παραδείγματα

Το παρακάτω παράδειγμα δείχνει πώς να ανακτήσετε την ποσότητα των MB που έχουν υποστεί επεξεργασία.

```csharp
string publicKey = "Public Key";
string privateKey = "Private Key";

Metered metered = new Metered();
metered.SetMeteredKey(publicKey, privateKey);

decimal mbProcessed = Metered.GetConsumptionQuantity();
```

### Δείτε επίσης

* class [Metered](../../metered)
* χώρος ονομάτων [GroupDocs.Parser](../../metered)
* συνέλευση [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
