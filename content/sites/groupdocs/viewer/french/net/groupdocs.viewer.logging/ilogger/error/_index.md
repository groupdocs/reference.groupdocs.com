---
title: Error
second_title: Référence de l'API GroupDocs.Viewer pour .NET
description: Écrit un message derreur. Les messages du journal des erreurs fournissent des informations sur les événements irrécupérables dans le flux dapplication.
type: docs
weight: 10
url: /fr/net/groupdocs.viewer.logging/ilogger/error/
---
## ILogger.Error method

Écrit un message d'erreur. Les messages du journal des erreurs fournissent des informations sur les événements irrécupérables dans le flux d'application.

```csharp
public void Error(string message, Exception exception)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| message | String | Le message d'erreur. |
| exception | Exception | L'éxéption. |

### Exceptions

| exception | condition |
| --- | --- |
| ArgumentNullException | Jeté quand*message* est nul. |
| ArgumentNullException | Jeté quand*exception* est nul. |

### Voir également

* interface [ILogger](../../ilogger)
* espace de noms [GroupDocs.Viewer.Logging](../../ilogger)
* Assemblée [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
