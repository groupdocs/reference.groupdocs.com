---
title: JsonDataLoadOptions
second_title: GroupDocs.Assembly για Αναφορά API .NET
description: Αντιπροσωπεύει επιλογές για την ανάλυση δεδομένων JSON.
type: docs
weight: 140
url: /el/net/groupdocs.assembly.data/jsondataloadoptions/
---
## JsonDataLoadOptions class

Αντιπροσωπεύει επιλογές για την ανάλυση δεδομένων JSON.

```csharp
public class JsonDataLoadOptions
```

## Κατασκευαστές

| Ονομα | Περιγραφή |
| --- | --- |
| [JsonDataLoadOptions](jsondataloadoptions)() | Αρχικοποιεί μια νέα παρουσία αυτής της κλάσης με προεπιλεγμένες επιλογές. |

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [AlwaysGenerateRootObject](../../groupdocs.assembly.data/jsondataloadoptions/alwaysgeneraterootobject) { get; set; } | Λαμβάνει ή ορίζει μια σημαία που υποδεικνύει εάν μια προέλευση δεδομένων που δημιουργείται θα περιέχει πάντα ένα αντικείμενο για ένα στοιχείο JSON root . Εάν ένα ριζικό στοιχείο JSON περιέχει μια μεμονωμένη σύνθετη ιδιότητα, ένα τέτοιο αντικείμενο δεν δημιουργείται από προεπιλογή. |
| [ExactDateTimeParseFormats](../../groupdocs.assembly.data/jsondataloadoptions/exactdatetimeparseformats) { get; set; } | Λαμβάνει ή ορίζει ακριβείς μορφές για την ανάλυση των τιμών ημερομηνίας-ώρας JSON κατά τη φόρτωση του JSON. Η προεπιλογή είναι**μηδενικό** . |
| [SimpleValueParseMode](../../groupdocs.assembly.data/jsondataloadoptions/simplevalueparsemode) { get; set; } | Λαμβάνει ή ορίζει μια λειτουργία για την ανάλυση JSON απλών τιμών (null, boolean, αριθμός, ακέραιος και συμβολοσειρά) κατά τη φόρτωση του JSON. Μια τέτοια λειτουργία δεν επηρεάζει την ανάλυση των τιμών ημερομηνίας-ώρας. Η προεπιλογή είναι Loose . |

### Παρατηρήσεις

Ένα στιγμιότυπο αυτής της κλάσης μπορεί να περάσει στους κατασκευαστές του[`JsonDataSource`](../jsondatasource) .

### Δείτε επίσης

* χώρος ονομάτων [GroupDocs.Assembly.Data](../../groupdocs.assembly.data)
* συνέλευση [GroupDocs.Assembly](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
