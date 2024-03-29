---
title: ReleasePageStream
second_title: GroupDocs.Viewer voor .NET API-referentie
description: Geeft een stream vrij die is geïnstantieerd door de methode die is gekoppeld aanCreatePageStream./createpagestream delegeren.
type: docs
weight: 200
url: /nl/net/groupdocs.viewer.interfaces/releasepagestream/
---
## ReleasePageStream delegate

Geeft een stream vrij die is geïnstantieerd door de methode die is gekoppeld aan[`CreatePageStream`](../createpagestream) delegeren.

```csharp
public delegate void ReleasePageStream(int pageNumber, Stream pageStream);
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| pageNumber | Int32 | Nummer van de pagina. |
| pageStream | Stream | De stream die is gemaakt door de methode die is gekoppeld aan[`CreatePageStream`](../createpagestream) delegeren. |

### Zie ook

* naamruimte [GroupDocs.Viewer.Interfaces](../../groupdocs.viewer.interfaces)
* montage [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
