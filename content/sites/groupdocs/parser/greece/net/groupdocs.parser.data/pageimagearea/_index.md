---
title: PageImageArea
second_title: GroupDocs.Parser για Αναφορά API .NET
description: Αντιπροσωπεύει μια περιοχή εικόνας σελίδας που χρησιμοποιείται για την αναπαράσταση μιας εικόνας στη σελίδα στην ανάλυση κατά πρότυπο functionality ή ένα συνημμένο εικόνας εάν οι εικόνες εξάγονται από μηνύματα ηλεκτρονικού ταχυδρομείου ή από αρχεία Zip.
type: docs
weight: 110
url: /el/net/groupdocs.parser.data/pageimagearea/
---
## PageImageArea class

Αντιπροσωπεύει μια περιοχή εικόνας σελίδας που χρησιμοποιείται για την αναπαράσταση μιας εικόνας στη σελίδα στην ανάλυση κατά πρότυπο functionality ή ένα συνημμένο εικόνας εάν οι εικόνες εξάγονται από μηνύματα ηλεκτρονικού ταχυδρομείου ή από αρχεία Zip.

```csharp
public sealed class PageImageArea : PageArea
```

## Κατασκευαστές

| Ονομα | Περιγραφή |
| --- | --- |
| [PageImageArea](pageimagearea#constructor)(Stream, FileType, double) | Αρχικοποιεί μια νέα παρουσία του[`PageImageArea`](../pageimagearea) τάξη. |
| [PageImageArea](pageimagearea#constructor_1)(Stream, FileType, double, Page, Rectangle) | Αρχικοποιεί μια νέα παρουσία του[`PageImageArea`](../pageimagearea) τάξη. |

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [FileType](../../groupdocs.parser.data/pageimagearea/filetype) { get; } | Λαμβάνει τη μορφή της εικόνας. |
| [Page](../../groupdocs.parser.data/pagearea/page) { get; } | Λαμβάνει τις πληροφορίες της σελίδας του εγγράφου, όπως ευρετήριο σελίδας και μέγεθος σελίδας. |
| [Rectangle](../../groupdocs.parser.data/pagearea/rectangle) { get; } | Παίρνει το ορθογώνιο εμβαδόν. |
| [Rotation](../../groupdocs.parser.data/pageimagearea/rotation) { get; } | Λαμβάνει τη γωνία περιστροφής της εικόνας. |

## Μέθοδοι

| Ονομα | Περιγραφή |
| --- | --- |
| [GetImageStream](../../groupdocs.parser.data/pageimagearea/getimagestream#getimagestream)() | Επιστρέφει τη ροή εικόνας. |
| [GetImageStream](../../groupdocs.parser.data/pageimagearea/getimagestream#getimagestream_1)(ImageOptions) | Επιστρέφει τη ροή εικόνας σε διαφορετική μορφή. |
| [Save](../../groupdocs.parser.data/pageimagearea/save#save)(string) | Αποθηκεύει την εικόνα στο αρχείο. |
| [Save](../../groupdocs.parser.data/pageimagearea/save#save_1)(string, ImageOptions) | Αποθηκεύει την εικόνα στο αρχείο σε διαφορετική μορφή. |

### Παρατηρήσεις

Ένα παράδειγμα του[`PageImageArea`](../pageimagearea) Η κλάση χρησιμοποιείται ως επιστρεφόμενη τιμή των ακόλουθων μεθόδων:

* [`GetImages`](../../groupdocs.parser/parser/getimages)
* [`GetImages`](../../groupdocs.parser/parser/getimages)
* [`GetImages`](../../groupdocs.parser/parser/getimages)
* [`GetImages`](../../groupdocs.parser/parser/getimages)

Δείτε τα παραδείγματα χρήσης εκεί.

### Δείτε επίσης

* class [PageArea](../pagearea)
* χώρος ονομάτων [GroupDocs.Parser.Data](../../groupdocs.parser.data)
* συνέλευση [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
