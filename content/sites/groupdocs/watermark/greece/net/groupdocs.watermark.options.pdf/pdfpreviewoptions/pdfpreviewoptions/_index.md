---
title: PdfPreviewOptions
second_title: GroupDocs.Watermark για Αναφορά API .NET
description: Αρχικοποιεί μια νέα παρουσία τουPdfPreviewOptionsgroupdocs.watermark.options.pdf/pdfpreviewoptions κλάση που προκαλεί το κλείσιμο της ροής εξόδου.
type: docs
weight: 10
url: /el/net/groupdocs.watermark.options.pdf/pdfpreviewoptions/pdfpreviewoptions/
---
## PdfPreviewOptions(CreatePageStream) {#constructor}

Αρχικοποιεί μια νέα παρουσία του[`PdfPreviewOptions`](../../pdfpreviewoptions) κλάση που προκαλεί το κλείσιμο της ροής εξόδου.

```csharp
public PdfPreviewOptions(CreatePageStream createPageStream)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| createPageStream | CreatePageStream | Δημιουργεί μια ροή για μια συγκεκριμένη προεπισκόπηση σελίδας. |

### Δείτε επίσης

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [PdfPreviewOptions](../../pdfpreviewoptions)
* χώρος ονομάτων [GroupDocs.Watermark.Options.Pdf](../../pdfpreviewoptions)
* συνέλευση [GroupDocs.Watermark](../../../)

---

## PdfPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Αρχικοποιεί μια νέα παρουσία του[`PdfPreviewOptions`](../../pdfpreviewoptions) κλάση που κάνει τη ροή εξόδου να επιστραφεί στον πελάτη για περαιτέρω χρήση.

```csharp
public PdfPreviewOptions(CreatePageStream createPageStream, ReleasePageStream releasePageStream)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| createPageStream | CreatePageStream | Δημιουργεί μια ροή για μια συγκεκριμένη προεπισκόπηση σελίδας. |
| releasePageStream | ReleasePageStream | Ειδοποιεί ότι η δημιουργία προεπισκόπησης σελίδας έχει ολοκληρωθεί και λαμβάνει τη ροή εξόδου. |

### Δείτε επίσης

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [PdfPreviewOptions](../../pdfpreviewoptions)
* χώρος ονομάτων [GroupDocs.Watermark.Options.Pdf](../../pdfpreviewoptions)
* συνέλευση [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
