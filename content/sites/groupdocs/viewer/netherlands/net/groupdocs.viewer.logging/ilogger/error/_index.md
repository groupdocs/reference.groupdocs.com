---
title: Error
second_title: GroupDocs.Viewer voor .NET API-referentie
description: Schrijft een foutbericht. Foutlogboekberichten geven informatie over onherstelbare gebeurtenissen in de toepassingsstroom.
type: docs
weight: 10
url: /nl/net/groupdocs.viewer.logging/ilogger/error/
---
## ILogger.Error method

Schrijft een foutbericht. Foutlogboekberichten geven informatie over onherstelbare gebeurtenissen in de toepassingsstroom.

```csharp
public void Error(string message, Exception exception)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| message | String | De foutmelding. |
| exception | Exception | De uitzondering. |

### Uitzonderingen

| uitzondering | voorwaarde |
| --- | --- |
| ArgumentNullException | Wanneer gegooid*message* is niets. |
| ArgumentNullException | Wanneer gegooid*exception* is niets. |

### Zie ook

* interface [ILogger](../../ilogger)
* naamruimte [GroupDocs.Viewer.Logging](../../ilogger)
* montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
