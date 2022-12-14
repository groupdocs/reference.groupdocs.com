---
title: SetLicense
second_title: Référence de l'API GroupDocs.Viewer pour .NET
description: Licence du composant.
type: docs
weight: 20
url: /fr/net/groupdocs.viewer/license/setlicense/
---
## SetLicense(Stream) {#setlicense}

Licence du composant.

```csharp
public void SetLicense(Stream licenseStream)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| licenseStream | Stream | Le flux de licence. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Jeté quand*licenseStream* est nul. |

### Exemples

L'exemple suivant montre comment définir un flux de transmission license du fichier de licence.

```csharp
using (FileStream licenseStream = File.OpenRead("GroupDocs.Viewer.lic"))
{
    License license = new License();
    license.SetLicense(licenseStream);
}
```

### Voir également

* class [License](../../license)
* espace de noms [GroupDocs.Viewer](../../license)
* Assemblée [GroupDocs.Viewer](../../../)

---

## SetLicense(string) {#setlicense_1}

Licence du composant.

```csharp
public void SetLicense(string licensePath)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| licensePath | String | Le chemin du fichier de licence. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentException | Jeté quand*licensePath* est une chaîne nulle ou vide. |

### Exemples

L'exemple suivant montre comment définir une licence en transmettant un chemin d'accès au fichier de licence.

```csharp
string licensePath = "GroupDocs.Viewer.lic";
License license = new License();
license.SetLicense(licensePath);
```

### Voir également

* class [License](../../license)
* espace de noms [GroupDocs.Viewer](../../license)
* Assemblée [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
