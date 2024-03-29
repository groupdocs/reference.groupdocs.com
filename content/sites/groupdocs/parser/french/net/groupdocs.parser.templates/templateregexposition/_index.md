---
title: TemplateRegexPosition
second_title: Référence de l'API GroupDocs.Parser pour .NET
description: Fournit une position de champ de modèle qui utilise lexpression régulière.
type: docs
weight: 730
url: /fr/net/groupdocs.parser.templates/templateregexposition/
---
## TemplateRegexPosition class

Fournit une position de champ de modèle qui utilise l'expression régulière.

```csharp
public sealed class TemplateRegexPosition : TemplatePosition
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [TemplateRegexPosition](templateregexposition#constructor)(string) | Initialise une nouvelle instance du[`TemplateRegexPosition`](../templateregexposition) classe. |
| [TemplateRegexPosition](templateregexposition#constructor_1)(string, bool) | Initialise une nouvelle instance du[`TemplateRegexPosition`](../templateregexposition) classe. |

## Propriétés

| Nom | La description |
| --- | --- |
| [Expression](../../groupdocs.parser.templates/templateregexposition/expression) { get; } | Obtient l'expression régulière. |
| [MatchCase](../../groupdocs.parser.templates/templateregexposition/matchcase) { get; } | Obtient la valeur qui indique si une casse de texte n'est pas ignorée. |

### Exemples

L'exemple suivant montre la situation si le document contient "Numéro de facture INV-12345", alors le champ de modèle peut être défini de la manière suivante :

Dans ce cas, en tant que valeur, la chaîne entière est extraite. Pour extraire uniquement une partie de la chaîne, le groupe d'expressions régulières "valeur" est utilisé :

Dans ce cas, en tant que valeur, la chaîne "INV-3337" est extraite.

```csharp
// Crée un champ de modèle de regex avec le nom "InvoiceNumber"
TemplateField templateField = new TemplateField(
    new TemplateRegexPosition("Invoice Number\\s+[A-Z0-9\\-]+"),
    "InvoiceNumber");
```

```csharp
// Créer un champ de modèle regex avec le nom "InvoiceNumber" avec le groupe "value"
TemplateField templateField = new TemplateField(
    new TemplateRegexPosition("Invoice Number\\s+(?<value>[A-Z0-9\\-]+)"),
    "InvoiceNumber");
```

### Voir également

* class [TemplatePosition](../templateposition)
* espace de noms [GroupDocs.Parser.Templates](../../groupdocs.parser.templates)
* Assemblée [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
