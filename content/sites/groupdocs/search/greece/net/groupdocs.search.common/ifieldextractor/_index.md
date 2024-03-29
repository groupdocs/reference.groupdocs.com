---
title: IFieldExtractor
second_title: GroupDocs.Αναζήτηση για αναφορά API .NET
description: Παρέχει μεθόδους εξαγωγής πεδίων από ένα έγγραφο.
type: docs
weight: 190
url: /el/net/groupdocs.search.common/ifieldextractor/
---
## IFieldExtractor interface

Παρέχει μεθόδους εξαγωγής πεδίων από ένα έγγραφο.

```csharp
public interface IFieldExtractor
```

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [Extensions](../../groupdocs.search.common/ifieldextractor/extensions) { get; } | Λαμβάνει τις υποστηριζόμενες επεκτάσεις. |

## Μέθοδοι

| Ονομα | Περιγραφή |
| --- | --- |
| [GetFields](../../groupdocs.search.common/ifieldextractor/getfields#getfields)(Stream) | Εξάγει όλα τα πεδία από το καθορισμένο έγγραφο. |
| [GetFields](../../groupdocs.search.common/ifieldextractor/getfields#getfields_1)(string) | Εξάγει όλα τα πεδία από το καθορισμένο έγγραφο. |

### Παρατηρήσεις

**Μάθε περισσότερα**

* [Εξαγωγείς προσαρμοσμένων κειμένων](https://docs.groupdocs.com/display/searchnet/Custom+text+extractors)

### Παραδείγματα

Το παράδειγμα δείχνει πώς να υλοποιήσετε τη διεπαφή[`IFieldExtractor`](../ifieldextractor) .

```csharp
public class LogExtractor : IFieldExtractor
{
    private readonly string[] extensions = new string[] { ".log" };

    public string[] Extensions
    {
        get { return extensions; }
    }

    public DocumentField[] GetFields(string filePath)
    {
        FileInfo fileInfo = new FileInfo(filePath);
        DocumentField[] fields = new DocumentField[]
        {
            new DocumentField("FileName", fileInfo.FullName),
            new DocumentField("CreationDate", fileInfo.CreationTime.ToString(CultureInfo.InvariantCulture)),
            new DocumentField("Content", ExtractContent(filePath)),
        };
        return fields;
    }

    private string ExtractContent(string filePath)
    {
        StringBuilder result = new StringBuilder();
        using (StreamReader streamReader = File.OpenText(filePath))
        {
            string line = streamReader.ReadLine();
            string processedLine = line.Remove(0, 12);
            result.AppendLine(processedLine);
        }
        return result.ToString();
    }
}
```

Το παράδειγμα δείχνει πώς να χρησιμοποιήσετε τον εξαγωγέα custorm για δημιουργία ευρετηρίου.

```csharp
string indexFolder = @"c:\MyIndex\"; // Καθορίστε τη διαδρομή προς το φάκελο ευρετηρίου
string documentsFolder = @"c:\MyDocuments\"; // Καθορίστε τη διαδρομή προς έναν φάκελο που περιέχει έγγραφα προς αναζήτηση

Index index = new Index(indexFolder); // Δημιουργία ή φόρτωση ευρετηρίου

index.IndexSettings.CustomExtractors.Add(new LogExtractor()); // Προσθήκη προσαρμοσμένου εργαλείου εξαγωγής κειμένου στις ρυθμίσεις ευρετηρίου

index.Add(documentsFolder); // Δημιουργία ευρετηρίου εγγράφων από τον καθορισμένο φάκελο
```

### Δείτε επίσης

* χώρος ονομάτων [GroupDocs.Search.Common](../../groupdocs.search.common)
* συνέλευση [GroupDocs.Search](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
