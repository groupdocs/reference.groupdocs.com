---
title: Attachment
second_title: GroupDocs.Viewer για Αναφορά API .NET
description: Αρχικοποιεί νέα παρουσία τουAttachmentgroupdocs.viewer.results/attachment τάξη.
type: docs
weight: 10
url: /el/net/groupdocs.viewer.results/attachment/attachment/
---
## Attachment() {#constructor}

Αρχικοποιεί νέα παρουσία του[`Attachment`](../../attachment) τάξη.

```csharp
public Attachment()
```

### Δείτε επίσης

* class [Attachment](../../attachment)
* χώρος ονομάτων [GroupDocs.Viewer.Results](../../attachment)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## Attachment(string, string) {#constructor_1}

Αρχικοποιεί νέα παρουσία του[`Attachment`](../../attachment) τάξη.

```csharp
public Attachment(string fileName, string filePath)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| fileName | String | Όνομα αρχείου συνημμένου. |
| filePath | String | Σχετική διαδρομή προσάρτησης π.χφάκελος/αρχείο.docx ή όνομα αρχείου όταν το αρχείο βρίσκεται στη ρίζα ενός αρχείου, σε μήνυμα ηλεκτρονικού ταχυδρομείου ή αρχείο δεδομένων. |

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentException | Ρίχτηκε όταν*fileName* είναι μηδενικό ή κενό. |
| ArgumentException | Ρίχτηκε όταν*filePath* είναι μηδενικό ή κενό. |

### Δείτε επίσης

* class [Attachment](../../attachment)
* χώρος ονομάτων [GroupDocs.Viewer.Results](../../attachment)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## Attachment(string, string, string, long) {#constructor_3}

Αρχικοποιεί νέα παρουσία του[`Attachment`](../../attachment) τάξη.

```csharp
public Attachment(string id, string fileName, string filePath, long size)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| id | String | Μοναδικό (στο πλαίσιο μεμονωμένου αρχείου) αναγνωριστικό του συνημμένου. |
| fileName | String | Όνομα αρχείου συνημμένου. |
| filePath | String | Σχετική διαδρομή προσάρτησης π.χφάκελος/αρχείο.docx ή όνομα αρχείου όταν το αρχείο βρίσκεται στη ρίζα ενός αρχείου, σε μήνυμα ηλεκτρονικού ταχυδρομείου ή αρχείο δεδομένων. |
| size | Int64 | Μέγεθος αρχείου συνημμένου σε byte. |

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentException | Ρίχτηκε όταν*id* είναι μηδενικό ή κενό. |
| ArgumentException | Ρίχτηκε όταν*fileName* είναι μηδενικό ή κενό. |
| ArgumentException | Ρίχτηκε όταν*filePath* είναι μηδενικό ή κενό. |

### Δείτε επίσης

* class [Attachment](../../attachment)
* χώρος ονομάτων [GroupDocs.Viewer.Results](../../attachment)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## Attachment(string, string, string, FileType, long) {#constructor_2}

Αρχικοποιεί νέα παρουσία του[`Attachment`](../../attachment) τάξη.

```csharp
public Attachment(string id, string fileName, string filePath, FileType fileType, long size)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| id | String | Μοναδικό (στο πλαίσιο μεμονωμένου αρχείου) αναγνωριστικό του συνημμένου. |
| fileName | String | Όνομα αρχείου συνημμένου. |
| filePath | String | Σχετική διαδρομή προσάρτησης π.χφάκελος/αρχείο.docx ή όνομα αρχείου όταν το αρχείο βρίσκεται στη ρίζα ενός αρχείου, σε μήνυμα ηλεκτρονικού ταχυδρομείου ή αρχείο δεδομένων. |
| fileType | FileType | Τύπος αρχείου συνημμένου. |
| size | Int64 | Μέγεθος αρχείου συνημμένου σε byte. |

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentException | Ρίχτηκε όταν*id* είναι μηδενικό ή κενό. |
| ArgumentException | Ρίχτηκε όταν*fileName* είναι μηδενικό ή κενό. |
| ArgumentException | Ρίχτηκε όταν*filePath* είναι μηδενικό ή κενό. |
| ArgumentNullException | Ρίχτηκε όταν*fileType* είναι μηδενικό. |

### Δείτε επίσης

* class [FileType](../../../groupdocs.viewer/filetype)
* class [Attachment](../../attachment)
* χώρος ονομάτων [GroupDocs.Viewer.Results](../../attachment)
* συνέλευση [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
