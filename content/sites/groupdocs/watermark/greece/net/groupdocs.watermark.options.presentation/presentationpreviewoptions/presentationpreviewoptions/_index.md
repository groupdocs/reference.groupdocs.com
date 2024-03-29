---
title: PresentationPreviewOptions
second_title: GroupDocs.Watermark για Αναφορά API .NET
description: Αρχικοποιεί μια νέα παρουσία τουPresentationPreviewOptionsgroupdocs.watermark.options.presentation/presentationpreviewoptions κλάση που προκαλεί το κλείσιμο της ροής εξόδου.
type: docs
weight: 10
url: /el/net/groupdocs.watermark.options.presentation/presentationpreviewoptions/presentationpreviewoptions/
---
## PresentationPreviewOptions(CreatePageStream) {#constructor}

Αρχικοποιεί μια νέα παρουσία του[`PresentationPreviewOptions`](../../presentationpreviewoptions) κλάση που προκαλεί το κλείσιμο της ροής εξόδου.

```csharp
public PresentationPreviewOptions(CreatePageStream createPageStream)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| createPageStream | CreatePageStream | Δημιουργεί μια ροή για μια συγκεκριμένη προεπισκόπηση σελίδας. |

### Δείτε επίσης

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* class [PresentationPreviewOptions](../../presentationpreviewoptions)
* χώρος ονομάτων [GroupDocs.Watermark.Options.Presentation](../../presentationpreviewoptions)
* συνέλευση [GroupDocs.Watermark](../../../)

---

## PresentationPreviewOptions(CreatePageStream, ReleasePageStream) {#constructor_1}

Αρχικοποιεί μια νέα παρουσία του[`PresentationPreviewOptions`](../../presentationpreviewoptions) κλάση που κάνει τη ροή εξόδου να επιστραφεί στον πελάτη για περαιτέρω χρήση.

```csharp
public PresentationPreviewOptions(CreatePageStream createPageStream, 
    ReleasePageStream releasePageStream)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| createPageStream | CreatePageStream | Δημιουργεί μια ροή για μια συγκεκριμένη προεπισκόπηση σελίδας. |
| releasePageStream | ReleasePageStream | Ειδοποιεί ότι η δημιουργία προεπισκόπησης σελίδας έχει ολοκληρωθεί και λαμβάνει τη ροή εξόδου. |

### Δείτε επίσης

* delegate [CreatePageStream](../../../groupdocs.watermark.options/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.watermark.options/releasepagestream)
* class [PresentationPreviewOptions](../../presentationpreviewoptions)
* χώρος ονομάτων [GroupDocs.Watermark.Options.Presentation](../../presentationpreviewoptions)
* συνέλευση [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
