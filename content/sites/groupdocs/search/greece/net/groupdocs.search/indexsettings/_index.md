---
title: IndexSettings
second_title: GroupDocs.Αναζήτηση για αναφορά API .NET
description: Αντιπροσωπεύει τις ρυθμίσεις ευρετηρίου που επιτρέπουν την προσαρμογή των λειτουργιών ευρετηρίασης.
type: docs
weight: 700
url: /el/net/groupdocs.search/indexsettings/
---
## IndexSettings class

Αντιπροσωπεύει τις ρυθμίσεις ευρετηρίου που επιτρέπουν την προσαρμογή των λειτουργιών ευρετηρίασης.

```csharp
public class IndexSettings
```

## Κατασκευαστές

| Ονομα | Περιγραφή |
| --- | --- |
| [IndexSettings](indexsettings)() | Αρχικοποιεί μια νέα παρουσία του[`IndexSettings`](../indexsettings) τάξη. |

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [AutoDetectEncoding](../../groupdocs.search/indexsettings/autodetectencoding) { get; set; } | Λαμβάνει ή ορίζει μια τιμή που υποδεικνύει εάν θα εντοπιστεί αυτόματα η κωδικοποίηση ή όχι. Η προεπιλεγμένη τιμή είναι`ψευδής` . |
| [CustomExtractors](../../groupdocs.search/indexsettings/customextractors) { get; } | Λαμβάνει την προσαρμοσμένη συλλογή εξολκέων. |
| [DocumentFilter](../../groupdocs.search/indexsettings/documentfilter) { get; set; } | Λαμβάνει ή ορίζει ένα φίλτρο εγγράφου. Το[`DocumentFilter`](./documentfilter) λειτουργεί στη λογική συμπερίληψης. Χρησιμοποιήστε το[`DocumentFilter`](../../groupdocs.search.options/documentfilter) κλάση για τη δημιουργία παρουσιών φίλτρου εγγράφου. Η προεπιλεγμένη τιμή είναι`μηδενικό` , πράγμα που σημαίνει ότι όλα τα έγγραφα που προστέθηκαν είναι ευρετηριασμένα. |
| [IndexType](../../groupdocs.search/indexsettings/indextype) { get; set; } | Λαμβάνει ή ορίζει τον τύπο ευρετηρίου. Η προεπιλεγμένη τιμή είναιNormalIndex . |
| [InMemoryIndex](../../groupdocs.search/indexsettings/inmemoryindex) { get; } | Λαμβάνει μια τιμή που υποδεικνύει εάν το ευρετήριο είναι αποθηκευμένο στη μνήμη ή στο δίσκο. |
| [Logger](../../groupdocs.search/indexsettings/logger) { get; set; } | Λαμβάνει ή ορίζει ένα καταγραφικό που χρησιμοποιείται για την καταγραφή συμβάντων και σφαλμάτων στο ευρετήριο. Σημειώστε ότι το καταγραφικό δεν αποθηκεύεται και πρέπει να δημιουργείται και να εκχωρείται κάθε φορά που δημιουργείται ή φορτώνεται το ευρετήριο. |
| [MaxIndexingReportCount](../../groupdocs.search/indexsettings/maxindexingreportcount) { get; set; } | Λαμβάνει ή ορίζει τον μέγιστο αριθμό αναφορών ευρετηρίασης. Η προεπιλεγμένη τιμή είναι`5` . |
| [MaxSearchReportCount](../../groupdocs.search/indexsettings/maxsearchreportcount) { get; set; } | Λαμβάνει ή ορίζει τον μέγιστο αριθμό αναφορών αναζήτησης. Η προεπιλεγμένη τιμή είναι`10` . |
| [SearchThreads](../../groupdocs.search/indexsettings/searchthreads) { get; set; } | Λαμβάνει ή ορίζει τον αριθμό των νημάτων που χρησιμοποιούνται για την αναζήτηση. Η προεπιλεγμένη τιμή είναιDefault , που σημαίνει ότι η αναζήτηση θα εκτελεστεί χρησιμοποιώντας τον αριθμό των νημάτων ίσο με τον αριθμό των πυρήνων του επεξεργαστή. |
| [TextStorageSettings](../../groupdocs.search/indexsettings/textstoragesettings) { get; set; } | Λαμβάνει ή ορίζει τις ρυθμίσεις αποθήκευσης κειμένου. Η προεπιλεγμένη τιμή είναι`μηδενικό` , που σημαίνει ότι τα κείμενα των εγγράφων δεν αποθηκεύονται. |
| [UseCharacterReplacements](../../groupdocs.search/indexsettings/usecharacterreplacements) { get; set; } | Λαμβάνει ή ορίζει μια τιμή που υποδεικνύει εάν θα χρησιμοποιηθούν αντικαταστάσεις χαρακτήρων ή όχι. Η προεπιλεγμένη τιμή είναι`ψευδής` . |
| [UseRawTextExtraction](../../groupdocs.search/indexsettings/userawtextextraction) { get; set; } | Λαμβάνει ή ορίζει μια τιμή που υποδεικνύει εάν η μη επεξεργασμένη λειτουργία χρησιμοποιείται για εξαγωγή κειμένου, εάν είναι δυνατόν. Η προεπιλεγμένη τιμή είναι`αληθής` . Η μη επεξεργασμένη λειτουργία μπορεί να αυξήσει σημαντικά την ταχύτητα ευρετηρίασης, αλλά η κανονική λειτουργία βελτιώνει τη μορφοποίηση του εξαγόμενου κειμένου. |
| [UseStopWords](../../groupdocs.search/indexsettings/usestopwords) { get; set; } | Λαμβάνει ή ορίζει μια τιμή που υποδεικνύει εάν θα χρησιμοποιηθούν λέξεις διακοπής ή όχι. Η προεπιλεγμένη τιμή είναι`αληθής` . |

### Παρατηρήσεις

**Μάθε περισσότερα**

* [Ρυθμίσεις ευρετηρίου αναζήτησης](https://docs.groupdocs.com/display/searchnet/Search+index+settings)

### Παραδείγματα

Το παράδειγμα δείχνει μια τυπική χρήση της κλάσης.

```csharp
string indexFolder = @"c:\MyIndex\";
IndexSettings settings = new IndexSettings();
settings.IndexType = IndexType.CompactIndex; // Ρύθμιση του τύπου ευρετηρίου

Index index = new Index(indexFolder, settings); // Δημιουργία ευρετηρίου
```

### Δείτε επίσης

* χώρος ονομάτων [GroupDocs.Search](../../groupdocs.search)
* συνέλευση [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
