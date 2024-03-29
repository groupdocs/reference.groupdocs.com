---
title: TextResourceBase
second_title: Référence de l'API GroupDocs.Editor pour .NET
description: Classe de base pour toute ressource texte prise en charge avec contenu textuel et encodage
type: docs
weight: 640
url: /fr/net/groupdocs.editor.htmlcss.resources.textual/textresourcebase/
---
## TextResourceBase class

Classe de base pour toute ressource texte prise en charge avec contenu textuel et encodage

```csharp
public abstract class TextResourceBase : IHtmlResource
```

## Propriétés

| Nom | La description |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/bytecontent) { get; } | Renvoie le contenu de cette ressource texte sous forme de flux d'octets avec l'encodage d'origine |
| [Encoding](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/encoding) { get; } | Renvoie l'encodage de cette ressource textuelle. Renvoie généralement UTF-8. |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/filenamewithextension) { get; } | Renvoie le nom de fichier correct de cette ressource texte, qui se compose du nom et de l'extension |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/isdisposed) { get; } | Détermine si cette ressource texte est supprimée ou non |
| [Name](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/name) { get; } | Renvoie le nom de cette ressource texte sans extension de fichier |
| [TextContent](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/textcontent) { get; } | Renvoie le contenu de cette ressource texte sous forme de chaîne standard |
| abstract [Type](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/type) { get; } | Lors de l'implémentation, le type doit renvoyer des informations sur le type du texte resource |

## Méthodes

| Nom | La description |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/dispose)() | Supprime cette ressource texte, supprimant son contenu et rendant la plupart des méthodes et propriétés non fonctionnelles. Tolérant aux appels multiples. |
| [Equals](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/equals#equals)(IHtmlResource) | Vérifie cette instance avec spécifié sur l'égalité. |
| [Save](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/save)(string) | Enregistre cette ressource texte dans le fichier spécifié |

## Événements

| Nom | La description |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.textual/textresourcebase/disposed) | Evénement, qui se produit lorsque cette ressource texte est supprimée |

### Voir également

* interface [IHtmlResource](../../groupdocs.editor.htmlcss.resources/ihtmlresource)
* espace de noms [GroupDocs.Editor.HtmlCss.Resources.Textual](../../groupdocs.editor.htmlcss.resources.textual)
* Assemblée [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
