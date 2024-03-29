---
title: PageRange
second_title: GroupDocs.Editor για Αναφορά API .NET
description: Ενσωματώνει ένα εύρος σελίδων το οποίο μπορεί να έχει ανοιχτά ή κλειστά όρια. Από προεπιλογή είναι πλήρως ανοιχτό  περιλαμβάνει όλες τις υπάρχουσες σελίδες. Η αρίθμηση σελίδων ξεκινά από το 1 όχι από το 0.
type: docs
weight: 1020
url: /el/net/groupdocs.editor.options/pagerange/
---
## PageRange structure

Ενσωματώνει ένα εύρος σελίδων, το οποίο μπορεί να έχει ανοιχτά ή κλειστά όρια. Από προεπιλογή είναι "πλήρως ανοιχτό" - περιλαμβάνει όλες τις υπάρχουσες σελίδες. Η αρίθμηση σελίδων ξεκινά από το 1, όχι από το 0.

```csharp
public struct PageRange : IEquatable<PageRange>
```

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [Count](../../groupdocs.editor.options/pagerange/count) { get; } | Αριθμοί σελίδων εντός εμβέλειας. Εάν 0 - το εύρος σελίδων εξαπλώνεται μέχρι το τέλος του εγγράφου ανεξάρτητα από το πόσες σελίδες αποτελείται από |
| [EndNumber](../../groupdocs.editor.options/pagerange/endnumber) { get; } | Αποκλειστικός αριθμός τέλους σελίδας, μέχρι τον οποίο συνεχίζεται αυτό το εύρος σελίδων και στον οποίο σταματά αποκλειστικά. Εάν 0 - το εύρος σελίδων εξαπλώνεται μέχρι το τέλος του document |
| [IsDefault](../../groupdocs.editor.options/pagerange/isdefault) { get; } | Υποδεικνύει εάν αυτή η παρουσία αντιπροσωπεύει μια προεπιλεγμένη περιοχή σελίδων "πλήρως ανοιχτή", δηλαδή αντιπροσωπεύει όλες τις σελίδες ενός εγγράφου (true) ή όχι (false) |
| [StartNumber](../../groupdocs.editor.options/pagerange/startnumber) { get; } | Συμπεριλαμβανόμενος αριθμός αρχικής σελίδας, από τον οποίο ξεκινά αυτό το εύρος σελίδων. Εάν το εύρος 1 - σελίδας ξεκινά από την πρώτη σελίδα ενός εγγράφου |

## Μέθοδοι

| Ονομα | Περιγραφή |
| --- | --- |
| static [FromBeginningWithCount](../../groupdocs.editor.options/pagerange/frombeginningwithcount)(ushort) | Δημιουργεί ένα εύρος σελίδων, που ξεκινά από την πρώτη σελίδα και έχει καθορισμένο αριθμό σελίδων |
| static [FromStartPageTillEnd](../../groupdocs.editor.options/pagerange/fromstartpagetillend)(ushort) | Δημιουργεί ένα εύρος σελίδων, που ξεκινά από τον καθορισμένο αριθμό σελίδας και συνεχίζει μέχρι το τέλος του εγγράφου |
| static [FromStartPageTillEndPage](../../groupdocs.editor.options/pagerange/fromstartpagetillendpage)(ushort, ushort) | Δημιουργεί ένα εύρος σελίδων, που ξεκινά από τον καθορισμένο αριθμό σελίδας (συμπεριλαμβανομένου) και συνεχίζει μέχρι τον καθορισμένο αριθμό σελίδας (αποκλειστικά) |
| static [FromStartPageWithCount](../../groupdocs.editor.options/pagerange/fromstartpagewithcount)(ushort, ushort) | Δημιουργεί ένα εύρος σελίδων, που ξεκινά από τον καθορισμένο αριθμό σελίδας και έχει καθορισμένο αριθμό σελίδων ή απεριόριστο αριθμό σελίδων (μέχρι το τέλος) |
| [Equals](../../groupdocs.editor.options/pagerange/equals#equals)(PageRange) | Ανιχνεύει εάν αυτή η παρουσία του εύρους σελίδας είναι ίση με specified |

## Πεδία

| Ονομα | Περιγραφή |
| --- | --- |
| static readonly [AllPages](../../groupdocs.editor.options/pagerange/allpages) | Αντιπροσωπεύει όλες τις υπάρχουσες σελίδες ενός εγγράφου. Προεπιλεγμένη τιμή. |

### Παρατηρήσεις

Immutable struct, που ενσωματώνει μια περιοχή σελίδων, η οποία δεν σχετίζεται με κάποιο συγκεκριμένο έγγραφο και μπορεί να αντιπροσωπεύει μια περιοχή σελίδων για οποιοδήποτε έγγραφο.

### Δείτε επίσης

* χώρος ονομάτων [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* συνέλευση [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
