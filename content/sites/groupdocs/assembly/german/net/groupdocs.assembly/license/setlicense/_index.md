---
title: SetLicense
second_title: GroupDocs.Assembly für .NET-API-Referenz
description: Lizenziert die Komponente.
type: docs
weight: 30
url: /de/net/groupdocs.assembly/license/setlicense/
---
## SetLicense(string) {#setlicense_1}

Lizenziert die Komponente.

```csharp
public void SetLicense(string licenseName)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| licenseName | String | Kann ein vollständiger oder kurzer Dateiname oder Name einer eingebetteten Ressource sein. Verwenden Sie eine leere Zeichenfolge, um in den Evaluierungsmodus zu wechseln. |

### Bemerkungen

Versucht, die Lizenz an den folgenden Orten zu finden:

1. Explizite Pfad.

2. Der Ordner, der die GroupDocs-Komponentenassembly enthält.

3. Der Ordner, der die aufrufende Assembly des Clients enthält.

4. Der Ordner, der den Eintrag (Startup) Assembly enthält.

5. Eine eingebettete Ressource in der aufrufenden Assembly des Clients.

### Siehe auch

* class [License](../../license)
* namensraum [GroupDocs.Assembly](../../license)
* Montage [GroupDocs.Assembly](../../../)

---

## SetLicense(Stream) {#setlicense}

Lizenziert die Komponente.

```csharp
public void SetLicense(Stream stream)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| stream | Stream | Ein Stream, der die Lizenz enthält. |

### Bemerkungen

Verwenden Sie diese Methode, um eine Lizenz aus einem Stream zu laden.

### Siehe auch

* class [License](../../license)
* namensraum [GroupDocs.Assembly](../../license)
* Montage [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->
