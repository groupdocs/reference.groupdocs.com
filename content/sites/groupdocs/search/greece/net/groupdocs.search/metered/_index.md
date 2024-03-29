---
title: Metered
second_title: GroupDocs.Αναζήτηση για αναφορά API .NET
description: Παρέχει μεθόδους που επιτρέπουν την ενεργοποίηση προϊόντος με άδεια Metered και την ανάκτηση του όγκου των MB που έχουν υποστεί επεξεργασία. Μάθετε περισσότερα για τις άδειες Meteredεδώhttps//purchase.groupdocs.com/faqs/licensing/metered .
type: docs
weight: 730
url: /el/net/groupdocs.search/metered/
---
## Metered class

Παρέχει μεθόδους που επιτρέπουν την ενεργοποίηση προϊόντος με άδεια Metered και την ανάκτηση του όγκου των MB που έχουν υποστεί επεξεργασία. Μάθετε περισσότερα για τις άδειες Metered[εδώ](https://purchase.groupdocs.com/faqs/licensing/metered) .

```csharp
public class Metered
```

## Κατασκευαστές

| Ονομα | Περιγραφή |
| --- | --- |
| [Metered](metered)() | Αρχικοποιεί μια νέα παρουσία του[`Metered`](../metered) τάξη. |

## Μέθοδοι

| Ονομα | Περιγραφή |
| --- | --- |
| [SetMeteredKey](../../groupdocs.search/metered/setmeteredkey)(string, string) | Ορίζει το μετρημένο δημόσιο και ιδιωτικό κλειδί. |
| static [GetConsumptionCredit](../../groupdocs.search/metered/getconsumptioncredit)() | Λαμβάνει την πίστωση κατανάλωσης. |
| static [GetConsumptionQuantity](../../groupdocs.search/metered/getconsumptionquantity)() | Παίρνει την ποσότητα κατανάλωσης. |

### Παρατηρήσεις

**Μάθε περισσότερα**

* [Περιορισμοί Αξιολόγησης και Αδειοδότηση](https://docs.groupdocs.com/display/searchnet/Evaluation+Limitations+and+Licensing)

### Παραδείγματα

Το παράδειγμα δείχνει πώς να ορίσετε μετρημένα δημόσια και ιδιωτικά κλειδιά.

```csharp
Metered metered = new Metered();
metered.SetMeteredKey("PublicKey", "PrivateKey");
```

### Δείτε επίσης

* χώρος ονομάτων [GroupDocs.Search](../../groupdocs.search)
* συνέλευση [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
