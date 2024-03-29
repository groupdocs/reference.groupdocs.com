---
title: RemoveProperties
second_title: GroupDocs.Metadata για Αναφορά API .NET
description: Καταργεί τις ιδιότητες μεταδεδομένων που ικανοποιούν το καθορισμένο κατηγόρημα.
type: docs
weight: 90
url: /el/net/groupdocs.metadata/metadata/removeproperties/
---
## Metadata.RemoveProperties method

Καταργεί τις ιδιότητες μεταδεδομένων που ικανοποιούν το καθορισμένο κατηγόρημα.

```csharp
public int RemoveProperties(Func<MetadataProperty, bool> predicate)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| predicate | Func`2 | Μια συνάρτηση για τον έλεγχο κάθε ιδιότητας μεταδεδομένων για μια συνθήκη. |

### Επιστρεφόμενη Αξία

Ο αριθμός των επηρεαζόμενων ακινήτων.

### Παρατηρήσεις

**Μάθε περισσότερα**

* Περισσότερα παραδείγματα που δείχνουν τις χρήσεις αυτής της μεθόδου: [Κατάργηση μεταδεδομένων](https://docs.groupdocs.com/display/metadatanet/Removing+metadata)

### Παραδείγματα

Αυτό το παράδειγμα δείχνει πώς να αφαιρέσετε συγκεκριμένες ιδιότητες μεταδεδομένων χρησιμοποιώντας διάφορα κριτήρια.

```csharp
using (Metadata metadata = new Metadata(Constants.InputDocx))
{
    // Αφαιρέστε όλες τις ιδιότητες που ικανοποιούν το κατηγόρημα:
    Η ιδιότητα // περιέχει το όνομα του συντάκτη του εγγράφου Ή
    // αναφέρεται στον τελευταίο επεξεργαστή Ή
    // η τιμή της ιδιότητας είναι μια συμβολοσειρά που περιέχει τη δευτερεύουσα συμβολοσειρά "John" (για να αφαιρέσετε τυχόν αναφορές του John από τα μεταδεδομένα που εντοπίστηκαν)
    var affected = metadata.RemoveProperties(
            p => p.Tags.Contains(Tags.Person.Creator) ||
            p.Tags.Contains(Tags.Person.Editor) ||
            p.Value.Type == MetadataPropertyType.String && p.Value.ToString().Contains("John"));

    Console.WriteLine("Properties removed: {0}", affected);

    metadata.Save(Constants.OutputDocx);
}
```

### Δείτε επίσης

* delegate [Func&lt;T,TResult&gt;](../../../groupdocs.metadata.common/func-2)
* class [MetadataProperty](../../../groupdocs.metadata.common/metadataproperty)
* class [Metadata](../../metadata)
* χώρος ονομάτων [GroupDocs.Metadata](../../metadata)
* συνέλευση [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
