---
title: SetLicense
second_title: GroupDocs.Viewer für .NET-API-Referenz
description: Lizenziert die Komponente.
type: docs
weight: 20
url: /de/net/groupdocs.viewer/license/setlicense/
---
## SetLicense(Stream) {#setlicense}

Lizenziert die Komponente.

```csharp
public void SetLicense(Stream licenseStream)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| licenseStream | Stream | Der Lizenzstrom. |

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentNullException | Wann geworfen*licenseStream* ist Null. |

### Beispiele

Das folgende Beispiel zeigt, wie eine Lizenz festgelegt wird, die den Stream der Lizenzdatei durchläuft.

```csharp
using (FileStream licenseStream = File.OpenRead("GroupDocs.Viewer.lic"))
{
    License license = new License();
    license.SetLicense(licenseStream);
}
```

### Siehe auch

* class [License](../../license)
* namensraum [GroupDocs.Viewer](../../license)
* Montage [GroupDocs.Viewer](../../../)

---

## SetLicense(string) {#setlicense_1}

Lizenziert die Komponente.

```csharp
public void SetLicense(string licensePath)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| licensePath | String | Der Pfad der Lizenzdatei. |

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentException | Wann geworfen*licensePath* ist null oder eine leere Zeichenfolge. |

### Beispiele

Das folgende Beispiel zeigt, wie eine Lizenz festgelegt wird, indem ein Pfad zur Lizenzdatei übergeben wird.

```csharp
string licensePath = "GroupDocs.Viewer.lic";
License license = new License();
license.SetLicense(licensePath);
```

### Siehe auch

* class [License](../../license)
* namensraum [GroupDocs.Viewer](../../license)
* Montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->