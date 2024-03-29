---
title: FileLogger
second_title: Référence de l'API GroupDocs.Signature pour .NET
description: Écrit les messages du journal dans le fichier.
type: docs
weight: 1150
url: /fr/net/groupdocs.signature.logging/filelogger/
---
## FileLogger class

Écrit les messages du journal dans le fichier.

```csharp
public class FileLogger : ILogger
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [FileLogger](filelogger)(string) | Créer un enregistreur dans un fichier. |

## Méthodes

| Nom | La description |
| --- | --- |
| [Error](../../groupdocs.signature.logging/filelogger/error)(string, Exception) | Écrit un message d'erreur sur la console. Les messages du journal des erreurs fournissent des informations sur les événements irrécupérables dans le flux d'application. |
| [Trace](../../groupdocs.signature.logging/filelogger/trace)(string) | Écrit le message de suivi sur la console. Les messages du journal de suivi fournissent des informations généralement utiles sur le flux d'application. |
| [Warning](../../groupdocs.signature.logging/filelogger/warning)(string) | Écrit un message d'avertissement sur la console ; Les messages du journal d'avertissement fournissent des informations sur l'événement inattendu et récupérable dans le flux d'application. |

### Voir également

* interface [ILogger](../ilogger)
* espace de noms [GroupDocs.Signature.Logging](../../groupdocs.signature.logging)
* Assemblée [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
