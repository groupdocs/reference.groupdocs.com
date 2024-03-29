---
title: BarcodeSignature
second_title: GroupDocs.Signature για Αναφορά API .NET
description: Περιέχει ιδιότητες υπογραφής γραμμικού κώδικα.
type: docs
weight: 20
url: /el/net/groupdocs.signature.domain/barcodesignature/
---
## BarcodeSignature class

Περιέχει ιδιότητες υπογραφής γραμμικού κώδικα.

```csharp
public class BarcodeSignature : BaseSignature
```

## Κατασκευαστές

| Ονομα | Περιγραφή |
| --- | --- |
| [BarcodeSignature](barcodesignature)(string) | Εκκίνηση αντικειμένου BarcodeSignature με αναγνωριστικό υπογραφής που λήφθηκε μετά τη διαδικασία αναζήτησης. Αυτό το μοναδικό αναγνωριστικό χρησιμοποιείται για την εύρεση πρόσθετων ιδιοτήτων για αυτήν την υπογραφή από το επίπεδο πληροφοριών υπογραφής εγγράφου. |

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [Content](../../groupdocs.signature.domain/barcodesignature/content) { get; } | Καθορίζει το περιεχόμενο εικόνας δυαδικών δεδομένων γραμμικού κώδικα του τύπου[`Format`](./format) . Από προεπιλογή αυτή η ιδιότητα δεν θα οριστεί. Χρήση ιδιότητας[`ReturnContent`](../../groupdocs.signature.options/barcodesearchoptions/returncontent) για να ενεργοποιήσετε αυτήν τη δυνατότητα. |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | Λάβετε ή ορίστε την ημερομηνία δημιουργίας υπογραφής. |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | Λάβετε τη σημαία που υποδεικνύει εάν αυτή η υπογραφή διαγράφηκε από το έγγραφο. Αυτή η ιδιότητα χρησιμοποιείται μόνο για εγγραφές καταγραφής ιστορικού εγγράφων για τη διατήρηση της λίστας των διαγραμμένων υπογραφών. |
| [EncodeType](../../groupdocs.signature.domain/barcodesignature/encodetype) { get; } | Καθορίζει τον τύπο κωδικοποίησης γραμμικού κώδικα. |
| [Format](../../groupdocs.signature.domain/barcodesignature/format) { get; } | Καθορίζει τη μορφή της εικόνας υπογραφής Barcode. |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | Καθορίζει το ύψος της υπογραφής. |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | Λάβετε ή ορίστε σημαία για να υποδείξετε εάν αυτό το στοιχείο είναι περιεχόμενο υπογραφής ή εγγράφου. Αυτή η ιδιότητα χρησιμοποιείται με τη μέθοδο ενημέρωσης για να ορίσετε το στοιχείο ως υπογραφή (true) ή ως στοιχείο εγγράφου (false). |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | Καθορίζει την αριστερή θέση της υπογραφής. |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | Λάβετε ή ορίστε την ημερομηνία τροποποίησης της υπογραφής. |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | Καθορίζει την υπογραφή της σελίδας που βρέθηκε. |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | Μοναδικό αναγνωριστικό υπογραφής για την τροποποίηση της υπογραφής στο έγγραφο μέσω των μεθόδων ενημέρωσης ή διαγραφής. Αυτή η ιδιότητα θα οριστεί αυτόματα μετά την κλήση της μεθόδου Sign ή Search. Εάν αυτή η ιδιότητα αποθηκεύτηκε προτού μπορέσει να οριστεί χειροκίνητα για χειρισμό της υπογραφής. |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | Καθορίζει τον τύπο της υπογραφής. |
| [Text](../../groupdocs.signature.domain/barcodesignature/text) { get; } | Καθορίζει το κείμενο του Barcode. |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | Καθορίζει την επάνω θέση της υπογραφής. |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | Καθορίζει το πλάτος της υπογραφής. |

## Μέθοδοι

| Ονομα | Περιγραφή |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/barcodesignature/clone)() | Παράδειγμα υπογραφής γραμμικού κώδικα κλωνοποίησης. |
| override [Equals](../../groupdocs.signature.domain/barcodesignature/equals)(object) | Αντικαθιστά τη μέθοδο Equals για σύγκριση ιδιοτήτων υπογραφής |
| override [GetHashCode](../../groupdocs.signature.domain/barcodesignature/gethashcode)() | Αντικαθιστά τη μέθοδο GetHashCode |

### Δείτε επίσης

* class [BaseSignature](../basesignature)
* χώρος ονομάτων [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* συνέλευση [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
