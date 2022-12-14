---
title: Features
second_title: Référence de l'API GroupDocs.Parser pour .NET
description: Obtient les fonctionnalités prises en charge.
type: docs
weight: 20
url: /fr/net/groupdocs.parser/parser/features/
---
## Parser.Features property

Obtient les fonctionnalités prises en charge.

```csharp
public Features Features { get; }
```

### Valeur de la propriété

Un exemple de[`Features`](../../../groupdocs.parser.options/features) classe qui représente les fonctionnalités prises en charge.

### Remarques

**Apprendre encore plus:**

* [Obtenir les fonctionnalités prises en charge](https://docs.groupdocs.com/display/parsernet/Get+supported+features)

### Exemples

Si la fonctionnalité n'est pas prise en charge, la méthode renvoie`nul` à la place de la valeur. Certaines opérations peuvent prendre beaucoup de temps. Il n'est donc pas optimal d'appeler la méthode pour vérifier simplement la prise en charge de la fonctionnalité. À cette fin, la propriété Features est utilisée :

```csharp
using(Parser parser = new Parser("doc.zip"))
{
    if(!parser.Features.Text)
    {
        Console.WriteLine("Text extraction isn't supported");
        return;
    }
 
    using(TextReader reader = parser.GetText())
    {
        Console.WriteLine(reader.ReadToEnd());
    }
}
```

### Voir également

* class [Features](../../../groupdocs.parser.options/features)
* class [Parser](../../parser)
* espace de noms [GroupDocs.Parser](../../parser)
* Assemblée [GroupDocs.Parser](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Parser.dll -->
