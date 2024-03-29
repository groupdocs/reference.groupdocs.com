---
title: SetLicense
second_title: GroupDocs.Signature για Αναφορά API .NET
description: Παρέχει άδεια χρήσης του στοιχείου.
type: docs
weight: 20
url: /el/net/groupdocs.signature/license/setlicense/
---
## SetLicense(string) {#setlicense_1}

Παρέχει άδεια χρήσης του στοιχείου.

```csharp
public void SetLicense(string licensePath)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| licensePath | String | Η διαδρομή άδειας. |

### Παραδείγματα

Το ακόλουθο παράδειγμα δείχνει πώς να ορίσετε μια άδεια περνώντας μια διαδρομή στο αρχείο άδειας χρήσης.

```csharp
string licensePath = "GroupDocs.Signature.lic";
GroupDocs.Signature.License lic = new GroupDocs.Signature.License();
lic.SetLicense(licensePath);
```

### Δείτε επίσης

* class [License](../../license)
* χώρος ονομάτων [GroupDocs.Signature](../../license)
* συνέλευση [GroupDocs.Signature](../../../)

---

## SetLicense(Stream) {#setlicense}

Παρέχει άδεια χρήσης του στοιχείου.

```csharp
public void SetLicense(Stream licenseStream)
```

| Παράμετρος | Τύπος | Περιγραφή |
| --- | --- | --- |
| licenseStream | Stream | Η ροή αδειών. |

### Παραδείγματα

Το ακόλουθο παράδειγμα δείχνει πώς να ορίσετε μια άδεια περνώντας ροή του αρχείου άδειας χρήσης.

```csharp
using (FileStream licenseStream = new FileStream("GroupDocs.Signature.lic", FileMode.Open))
{
    GroupDocs.Signature.License lic = new GroupDocs.Signature.License();
    lic.SetLicense(licenseStream);
}
```

### Δείτε επίσης

* class [License](../../license)
* χώρος ονομάτων [GroupDocs.Signature](../../license)
* συνέλευση [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
