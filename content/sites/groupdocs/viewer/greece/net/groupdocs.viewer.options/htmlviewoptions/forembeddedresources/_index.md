---
title: ForEmbeddedResources
second_title: GroupDocs.Viewer για Αναφορά API .NET
description: Αρχικοποιεί νέα παρουσία τουHtmlViewOptionsgroupdocs.viewer.options/htmlviewoptions κλάση για απόδοση σε HTML με ενσωματωμένους πόρους.
type: docs
weight: 10
url: /el/net/groupdocs.viewer.options/htmlviewoptions/forembeddedresources/
---
## ForEmbeddedResources(CreatePageStream) {#forembeddedresources_1}

Αρχικοποιεί νέα παρουσία του[`HtmlViewOptions`](../../htmlviewoptions) κλάση για απόδοση σε HTML με ενσωματωμένους πόρους.

```csharp
public static HtmlViewOptions ForEmbeddedResources(CreatePageStream createPageStream)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| createPageStream | CreatePageStream | Η μέθοδος που δημιουργεί τη ροή που χρησιμοποιείται για την εγγραφή δεδομένων σελίδας εξόδου. |

### Επιστρεφόμενη Αξία

Νέο παράδειγμα του[`HtmlViewOptions`](../../htmlviewoptions) κλάση για απόδοση σε HTML με ενσωματωμένους πόρους.

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentNullException | Ρίχτηκε όταν*createPageStream* είναι μηδενικό. |

### Δείτε επίσης

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* class [HtmlViewOptions](../../htmlviewoptions)
* χώρος ονομάτων [GroupDocs.Viewer.Options](../../htmlviewoptions)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources(CreatePageStream, ReleasePageStream) {#forembeddedresources_2}

Αρχικοποιεί νέα παρουσία του[`HtmlViewOptions`](../../htmlviewoptions) κλάση για απόδοση σε HTML με ενσωματωμένους πόρους.

```csharp
public static HtmlViewOptions ForEmbeddedResources(CreatePageStream createPageStream, 
    ReleasePageStream releasePageStream)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| createPageStream | CreatePageStream | Η μέθοδος που δημιουργεί τη ροή που χρησιμοποιείται για την εγγραφή δεδομένων σελίδας εξόδου. |
| releasePageStream | ReleasePageStream | Η μέθοδος που απελευθερώνει τη ροή που δημιουργήθηκε με τη μέθοδο που έχει εκχωρηθεί για την ανάθεση της ροής στη*createPageStream* παράμετρος. |

### Επιστρεφόμενη Αξία

Νέο παράδειγμα του[`HtmlViewOptions`](../../htmlviewoptions) κλάση για απόδοση σε HTML με ενσωματωμένους πόρους.

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentNullException | Ρίχτηκε όταν*createPageStream* είναι μηδενικό. |
| ArgumentNullException | Ρίχτηκε όταν*releasePageStream* είναι μηδενικό. |

### Δείτε επίσης

* delegate [CreatePageStream](../../../groupdocs.viewer.interfaces/createpagestream)
* delegate [ReleasePageStream](../../../groupdocs.viewer.interfaces/releasepagestream)
* class [HtmlViewOptions](../../htmlviewoptions)
* χώρος ονομάτων [GroupDocs.Viewer.Options](../../htmlviewoptions)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources(IPageStreamFactory) {#forembeddedresources_3}

Αρχικοποιεί νέα παρουσία του[`HtmlViewOptions`](../../htmlviewoptions) κλάση για απόδοση σε HTML με ενσωματωμένους πόρους.

```csharp
public static HtmlViewOptions ForEmbeddedResources(IPageStreamFactory pageStreamFactory)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| pageStreamFactory | IPageStreamFactory | Το εργοστάσιο που εφαρμόζει μεθόδους για τη δημιουργία και την απελευθέρωση ροής σελίδας εξόδου. |

### Επιστρεφόμενη Αξία

Νέο παράδειγμα του[`HtmlViewOptions`](../../htmlviewoptions) κλάση για απόδοση σε HTML με ενσωματωμένους πόρους.

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentNullException | Ρίχτηκε όταν*pageStreamFactory* είναι μηδενικό. |

### Δείτε επίσης

* interface [IPageStreamFactory](../../../groupdocs.viewer.interfaces/ipagestreamfactory)
* class [HtmlViewOptions](../../htmlviewoptions)
* χώρος ονομάτων [GroupDocs.Viewer.Options](../../htmlviewoptions)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources() {#forembeddedresources}

Αρχικοποιεί νέα παρουσία του[`HtmlViewOptions`](../../htmlviewoptions) τάξη.

```csharp
public static HtmlViewOptions ForEmbeddedResources()
```

### Δείτε επίσης

* class [HtmlViewOptions](../../htmlviewoptions)
* χώρος ονομάτων [GroupDocs.Viewer.Options](../../htmlviewoptions)
* συνέλευση [GroupDocs.Viewer](../../../)

---

## ForEmbeddedResources(string) {#forembeddedresources_4}

Αρχικοποιεί νέα παρουσία του[`HtmlViewOptions`](../../htmlviewoptions) τάξη.

```csharp
public static HtmlViewOptions ForEmbeddedResources(string filePathFormat)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| filePathFormat | String | Η μορφή διαδρομής αρχείου π.χ. "page_{0}.html". |

### Εξαιρέσεις

| εξαίρεση | κατάσταση |
| --- | --- |
| ArgumentException | Ρίχτηκε όταν*filePathFormat* είναι μηδενικό ή κενό. |

### Δείτε επίσης

* class [HtmlViewOptions](../../htmlviewoptions)
* χώρος ονομάτων [GroupDocs.Viewer.Options](../../htmlviewoptions)
* συνέλευση [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
