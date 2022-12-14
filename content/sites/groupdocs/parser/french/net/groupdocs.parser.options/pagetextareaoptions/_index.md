---
title: PageTextAreaOptions
second_title: Référence de l'API GroupDocs.Parser pour .NET
description: Fournit les options utilisées pour lextraction des zones de texte de la page.
type: docs
weight: 500
url: /fr/net/groupdocs.parser.options/pagetextareaoptions/
---
## PageTextAreaOptions class

Fournit les options utilisées pour l'extraction des zones de texte de la page.

```csharp
public sealed class PageTextAreaOptions : PageAreaOptions
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [PageTextAreaOptions](pagetextareaoptions#constructor)(string) | Initialise une nouvelle instance du[`PageTextAreaOptions`](../pagetextareaoptions) classe avec l'expression régulière. D'autres options sont définies par défaut (voir les remarques pour plus de détails). |
| [PageTextAreaOptions](pagetextareaoptions#constructor_2)(string, Rectangle) | Initialise une nouvelle instance du[`PageTextAreaOptions`](../pagetextareaoptions) class avec l'expression régulière et la zone rectangulaire. D'autres options sont définies par défaut (voir les remarques pour plus de détails). |
| [PageTextAreaOptions](pagetextareaoptions#constructor_1)(string, bool, bool, bool, Rectangle) | Initialise une nouvelle instance du[`PageTextAreaOptions`](../pagetextareaoptions) classe. |

## Propriétés

| Nom | La description |
| --- | --- |
| [Expression](../../groupdocs.parser.options/pagetextareaoptions/expression) { get; } | Obtient l'expression régulière. |
| [IgnoreFormatting](../../groupdocs.parser.options/pagetextareaoptions/ignoreformatting) { get; } | Obtient la valeur qui indique si la mise en forme du texte est ignorée. |
| [MatchCase](../../groupdocs.parser.options/pagetextareaoptions/matchcase) { get; } | Obtient la valeur qui indique si une casse de texte n'est pas ignorée. |
| [Rectangle](../../groupdocs.parser.options/pageareaoptions/rectangle) { get; } | Obtient la zone rectangulaire qui contient les zones de page. |
| [UniteSegments](../../groupdocs.parser.options/pagetextareaoptions/unitesegments) { get; } | Obtient la valeur qui indique si les segments sont unis. |

### Remarques

Une instance de[`PageTextAreaOptions`](../pagetextareaoptions) class est utilisé comme paramètre dans[`GetTextAreas`](../../groupdocs.parser/parser/gettextareas) et[`GetTextAreas`](../../groupdocs.parser/parser/gettextareas) méthodes. Voir les exemples d'utilisation ici. **Apprendre encore plus:**

* [Extraire des zones de texte](https://docs.groupdocs.com/display/parsernet/Extract+text+areas)

### Voir également

* class [PageAreaOptions](../pageareaoptions)
* espace de noms [GroupDocs.Parser.Options](../../groupdocs.parser.options)
* Assemblée [GroupDocs.Parser](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
