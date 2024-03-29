---
title: DocumentInfo
second_title: GroupDocs.Metadata για Αναφορά API .NET
description: Παρέχει κοινές πληροφορίες σχετικά με ένα φορτωμένο έγγραφο.
type: docs
weight: 30
url: /el/net/groupdocs.metadata.common/documentinfo/
---
## DocumentInfo class

Παρέχει κοινές πληροφορίες σχετικά με ένα φορτωμένο έγγραφο.

```csharp
public class DocumentInfo : IDocumentInfo
```

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [FileType](../../groupdocs.metadata.common/documentinfo/filetype) { get; } | Λαμβάνει τον τύπο αρχείου του εγγράφου που έχει φορτωθεί. |
| [IsEncrypted](../../groupdocs.metadata.common/documentinfo/isencrypted) { get; } | Λαμβάνει μια τιμή που υποδεικνύει εάν το έγγραφο είναι κρυπτογραφημένο και απαιτεί κωδικό πρόσβασης για να ανοίξει. |
| [PageCount](../../groupdocs.metadata.common/documentinfo/pagecount) { get; } | Λαμβάνει τον αριθμό των σελίδων (διαφάνειες, φύλλα εργασίας, κ.λπ.) στο φορτωμένο έγγραφο. |
| [Pages](../../groupdocs.metadata.common/documentinfo/pages) { get; } | Λαμβάνει μια συλλογή αντικειμένων που αντιπροσωπεύουν κοινές πληροφορίες σχετικά με τις σελίδες του εγγράφου (διαφάνειες, φύλλα εργασίας, κ.λπ.). |
| [Size](../../groupdocs.metadata.common/documentinfo/size) { get; } | Λαμβάνει το μέγεθος του φορτωμένου εγγράφου σε byte. |

### Παρατηρήσεις

**Μάθε περισσότερα**

* [Λάβετε πληροφορίες εγγράφων](https://docs.groupdocs.com/display/metadatanet/Get+document+info)

### Παραδείγματα

Αυτό το παράδειγμα δείχνει πώς να εξαγάγετε πληροφορίες βασικής μορφής από ένα αρχείο.

```csharp
using (Metadata metadata = new Metadata(Constants.InputXlsx))
{
    if (metadata.FileFormat != FileFormat.Unknown)
    {
        IDocumentInfo info = metadata.GetDocumentInfo();

        Console.WriteLine("File format: {0}", info.FileType.FileFormat);
        Console.WriteLine("File extension: {0}", info.FileType.Extension);
        Console.WriteLine("MIME Type: {0}", info.FileType.MimeType);
        Console.WriteLine("Number of pages: {0}", info.PageCount);
        Console.WriteLine("Document size: {0} bytes", info.Size);
        Console.WriteLine("Is document encrypted: {0}", info.IsEncrypted);
    }
}
```

### Δείτε επίσης

* interface [IDocumentInfo](../idocumentinfo)
* χώρος ονομάτων [GroupDocs.Metadata.Common](../../groupdocs.metadata.common)
* συνέλευση [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
