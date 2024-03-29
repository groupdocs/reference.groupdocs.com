---
title: XmlFormatOptions
second_title: GroupDocs.Editor για Αναφορά API .NET
description: Περιέχει επιλογές που επιτρέπουν την προσαρμογή της μορφοποίησης του εγγράφου XML όταν αυτό αναπαρίσταται ως HTML
type: docs
weight: 1280
url: /el/net/groupdocs.editor.options/xmlformatoptions/
---
## XmlFormatOptions class

Περιέχει επιλογές που επιτρέπουν την προσαρμογή της μορφοποίησης του εγγράφου XML, όταν αυτό αναπαρίσταται ως HTML

```csharp
public sealed class XmlFormatOptions : IEditOptions
```

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [EachAttributeFromNewline](../../groupdocs.editor.options/xmlformatoptions/eachattributefromnewline) { get; set; } | Όταν ενεργοποιηθεί, κάθε ζεύγος τιμής χαρακτηριστικών σε κάθε στοιχείο XML θα τοποθετηθεί σε μια νέα γραμμή. Από προεπιλογή είναι false (απενεργοποιημένο) — όλα τα ζεύγη χαρακτηριστικών-τιμών τοποθετούνται σε μία γραμμή. |
| [IsDefault](../../groupdocs.editor.options/xmlformatoptions/isdefault) { get; } | Υποδεικνύει εάν αυτή η παρουσία επιλογών μορφοποίησης XML έχει προεπιλεγμένη τιμή |
| [LeafTextNodesOnNewline](../../groupdocs.editor.options/xmlformatoptions/leaftextnodesonnewline) { get; set; } | Όταν είναι ενεργοποιημένοι, οι κόμβοι κειμένου φύλλου (κειμενικό περιεχόμενο εντός στοιχείων XML, χωρίς παιδιά) θα αποδοθούν σε μια νέα γραμμή με μεγαλύτερη αριστερή εσοχή. Από προεπιλογή είναι false (απενεργοποιημένο) — οι κόμβοι κειμένου φύλλου τοποθετούνται στην ίδια γραμμή με οι γονείς τους, χωρίς νέα εσοχή. |
| [LeftIndent](../../groupdocs.editor.options/xmlformatoptions/leftindent) { get; set; } | Επιτρέπει τον καθορισμό μιας μετατόπισης για την αριστερή εσοχή κάθε νέας γραμμής. Δεν μπορεί να είναι μη μηδενική τιμή χωρίς μονάδα. Από προεπιλογή είναι 10pt |

### Δείτε επίσης

* interface [IEditOptions](../ieditoptions)
* χώρος ονομάτων [GroupDocs.Editor.Options](../../groupdocs.editor.options)
* συνέλευση [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
