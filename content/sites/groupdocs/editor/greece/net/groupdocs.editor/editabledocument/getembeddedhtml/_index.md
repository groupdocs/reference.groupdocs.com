---
title: GetEmbeddedHtml
second_title: GroupDocs.Editor για Αναφορά API .NET
description: Επιστρέφει όλο το περιεχόμενο αυτού του εγγράφου HTML με όλους τους σχετικούς πόρους σε μια μορφή μιας συμβολοσειράς όπου όλοι οι πόροι είναι ενσωματωμένοι μέσα στη σήμανση HTML σε μια κωδικοποιημένη μορφή βάσης64.
type: docs
weight: 150
url: /el/net/groupdocs.editor/editabledocument/getembeddedhtml/
---
## EditableDocument.GetEmbeddedHtml method

Επιστρέφει όλο το περιεχόμενο αυτού του εγγράφου HTML με όλους τους σχετικούς πόρους σε μια μορφή μιας συμβολοσειράς, όπου όλοι οι πόροι είναι ενσωματωμένοι μέσα στη σήμανση HTML σε μια κωδικοποιημένη μορφή βάσης64.

```csharp
public string GetEmbeddedHtml()
```

### Επιστρεφόμενη Αξία

Συμβολοσειρά, η οποία δεν είναι NULL ή κενή σε καμία περίπτωση

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ObjectDisposedException | Αυτή η παρουσία EditableDocument είχε ήδη απορριφθεί |

### Παρατηρήσεις

Αυτή η μέθοδος μετατρέπει αυτό το EditableDocument σε HTML και σειριοποιεί σε μία συμβολοσειρά, όπου όλοι οι πόροι είναι ενσωματωμένοι σε συμβολοσειρά μαζί με τη σήμανση HTML:

* Όλες οι εικόνες από HTML-&gt;BODY μετατρέπονται σε μορφή base64 και βρίσκονται στο χαρακτηριστικό IMG 'src'
* Όλα τα φύλλα στυλ αποθηκεύονται στα στοιχεία STYLE μέσα στις ενότητες HTML-&gt;HEAD
* Όλες οι εικόνες από φύλλα στυλ μετατρέπονται σε μορφή base64 και βρίσκονται στις κατάλληλες δηλώσεις CSS
* Όλες οι γραμματοσειρές από φύλλα στυλ μετατρέπονται σε μορφή base64 και βρίσκονται στους κατάλληλους κανόνες @font-face at-rules

### Δείτε επίσης

* class [EditableDocument](../../editabledocument)
* χώρος ονομάτων [GroupDocs.Editor](../../editabledocument)
* συνέλευση [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
