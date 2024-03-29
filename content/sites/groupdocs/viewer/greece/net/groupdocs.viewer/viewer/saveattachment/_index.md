---
title: SaveAttachment
second_title: GroupDocs.Viewer για Αναφορά API .NET
description: Αποθηκεύει το αρχείο συνημμένου σεdestination ροή.
type: docs
weight: 60
url: /el/net/groupdocs.viewer/viewer/saveattachment/
---
## SaveAttachment(Attachment, Stream, CancellationToken) {#saveattachment_1}

Αποθηκεύει το αρχείο συνημμένου σε*destination* ροή.

```csharp
public void SaveAttachment(Attachment attachment, Stream destination, 
    CancellationToken cancellationToken)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| attachment | Attachment | Το συνημμένο. |
| destination | Stream | Το εγγράψιμο ρεύμα. |
| cancellationToken | CancellationToken | Διακριτικό ακύρωσης. |

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentNullException | Ρίχτηκε όταν*attachment* είναι μηδενικό. |
| ArgumentNullException | Ρίχτηκε όταν*destination* είναι μηδενικό. |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Πετάγεται όταν απαιτείται κωδικός πρόσβασης για το άνοιγμα του εγγράφου. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Πετάγεται όταν ο κωδικός πρόσβασης που καθορίστηκε είναι εσφαλμένος. |
| [GroupDocsViewerException](../../../groupdocs.viewer.exceptions/groupdocsviewerexception) | Ρίχτηκε όταν δεν ήταν δυνατή η εύρεση του συνημμένου. |

### Παρατηρήσεις

**Μάθε περισσότερα**

* Μάθετε περισσότερα σχετικά με τη λήψη συνημμένων εγγράφων σε C#: [Τρόπος λήψης λίστας συνημμένων εγγράφων χρησιμοποιώντας το GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+attachments)
* Μάθετε περισσότερα σχετικά με την αποθήκευση συνημμένων εγγράφων σε C#: [Πώς να αποθηκεύσετε συνημμένα εγγράφων χρησιμοποιώντας το GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Save+attachments)

### Δείτε επίσης

* class [Attachment](../../../groupdocs.viewer.results/attachment)
* class [Viewer](../../viewer)
* χώρος ονομάτων [GroupDocs.Viewer](../../viewer)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## SaveAttachment(Attachment, Stream) {#saveattachment}

Αποθηκεύει το αρχείο συνημμένου σε*destination* ροή.

```csharp
public void SaveAttachment(Attachment attachment, Stream destination)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| attachment | Attachment | Το συνημμένο. |
| destination | Stream | Το εγγράψιμο ρεύμα. |

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentNullException | Ρίχτηκε όταν*attachment* είναι μηδενικό. |
| ArgumentNullException | Ρίχτηκε όταν*destination* είναι μηδενικό. |
| [PasswordRequiredException](../../../groupdocs.viewer.exceptions/passwordrequiredexception) | Πετάγεται όταν απαιτείται κωδικός πρόσβασης για το άνοιγμα του εγγράφου. |
| [IncorrectPasswordException](../../../groupdocs.viewer.exceptions/incorrectpasswordexception) | Πετάγεται όταν ο κωδικός πρόσβασης που καθορίστηκε είναι εσφαλμένος. |
| [GroupDocsViewerException](../../../groupdocs.viewer.exceptions/groupdocsviewerexception) | Ρίχτηκε όταν δεν ήταν δυνατή η εύρεση του συνημμένου. |

### Παρατηρήσεις

**Μάθε περισσότερα**

* Μάθετε περισσότερα σχετικά με τη λήψη συνημμένων εγγράφων σε C#: [Τρόπος λήψης λίστας συνημμένων εγγράφων χρησιμοποιώντας το GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Get+attachments)
* Μάθετε περισσότερα σχετικά με την αποθήκευση συνημμένων εγγράφων σε C#: [Πώς να αποθηκεύσετε συνημμένα εγγράφων χρησιμοποιώντας το GroupDocs.Viewer](https://docs.groupdocs.com/display/viewernet/Save+attachments)

### Δείτε επίσης

* class [Attachment](../../../groupdocs.viewer.results/attachment)
* class [Viewer](../../viewer)
* χώρος ονομάτων [GroupDocs.Viewer](../../viewer)
* συνέλευση [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
