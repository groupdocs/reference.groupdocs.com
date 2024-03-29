---
title: CheckboxFormFieldSignature
second_title: Référence de l'API GroupDocs.Signature pour .NET
description: Contient des propriétés de signature de champ de formulaire de saisie de case à cocher.
type: docs
weight: 80
url: /fr/net/groupdocs.signature.domain/checkboxformfieldsignature/
---
## CheckboxFormFieldSignature class

Contient des propriétés de signature de champ de formulaire de saisie de case à cocher.

```csharp
public sealed class CheckboxFormFieldSignature : FormFieldSignature
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [CheckboxFormFieldSignature](checkboxformfieldsignature#constructor)(string) | Crée CheckboxFormFieldSignature avec un nom prédéfini. |
| [CheckboxFormFieldSignature](checkboxformfieldsignature#constructor_1)(string, bool) | Crée CheckboxFormFieldSignature avec un nom et une valeur prédéfinis |

## Propriétés

| Nom | La description |
| --- | --- |
| [Checked](../../groupdocs.signature.domain/checkboxformfieldsignature/checked) { get; set; } | Obtient ou définit la valeur cochée de l'entrée de la case à cocher du champ de formulaire. |
| [CreatedOn](../../groupdocs.signature.domain/basesignature/createdon) { get; set; } | Obtenir ou définir la date de création de la signature. |
| [Deleted](../../groupdocs.signature.domain/basesignature/deleted) { get; } | Obtenez l'indicateur qui indique si cette signature a été supprimée du document. Cette propriété est utilisée uniquement pour les enregistrements du journal de l'historique du document afin de conserver la liste des signatures supprimées. |
| [Height](../../groupdocs.signature.domain/basesignature/height) { get; set; } | Spécifie la hauteur de la signature. |
| [IsSignature](../../groupdocs.signature.domain/basesignature/issignature) { get; set; } | Obtenir ou définir un indicateur pour indiquer si ce composant est une signature ou un contenu de document. Cette propriété est utilisée avec la méthode Update pour définir l'élément comme signature (true) ou élément de document (false). |
| [Left](../../groupdocs.signature.domain/basesignature/left) { get; set; } | Spécifie la position gauche de la signature. |
| [ModifiedOn](../../groupdocs.signature.domain/basesignature/modifiedon) { get; set; } | Obtenir ou définir la date de modification de la signature. |
| [Name](../../groupdocs.signature.domain/formfieldsignature/name) { get; set; } | Spécifie un nom de champ de formulaire unique. |
| [PageNumber](../../groupdocs.signature.domain/basesignature/pagenumber) { get; } | Spécifie que la signature de page a été trouvée sur. |
| [SignatureId](../../groupdocs.signature.domain/basesignature/signatureid) { get; } | Identifiant de signature unique pour modifier la signature dans le document via les méthodes Update ou Delete. Cette propriété sera définie automatiquement après l'appel de la méthode Sign ou Search. Si cette propriété a été enregistrée avant de pouvoir être définie manuellement pour manipuler la signature. |
| [SignatureType](../../groupdocs.signature.domain/basesignature/signaturetype) { get; } | Spécifie le type de signature. |
| [Top](../../groupdocs.signature.domain/basesignature/top) { get; set; } | Spécifie la position supérieure de la signature. |
| [Type](../../groupdocs.signature.domain/formfieldsignature/type) { get; } | Spécifie le type de champ de formulaire. |
| [Value](../../groupdocs.signature.domain/formfieldsignature/value) { get; set; } | Spécifie l'objet de données de champ de formulaire. |
| [Width](../../groupdocs.signature.domain/basesignature/width) { get; set; } | Spécifie la largeur de la signature. |

## Méthodes

| Nom | La description |
| --- | --- |
| override [Clone](../../groupdocs.signature.domain/checkboxformfieldsignature/clone)() | Cloner l'instance FormField Signature. |
| override [Equals](../../groupdocs.signature.domain/checkboxformfieldsignature/equals)(object) | Écrase la méthode Equals pour comparer les propriétés de la signature |
| override [GetHashCode](../../groupdocs.signature.domain/checkboxformfieldsignature/gethashcode)() | Remplace la méthode GetHashCode |

### Voir également

* class [FormFieldSignature](../formfieldsignature)
* espace de noms [GroupDocs.Signature.Domain](../../groupdocs.signature.domain)
* Assemblée [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
