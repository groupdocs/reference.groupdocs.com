---
title: EmailFileType
second_title: Référence de l'API GroupDocs.Conversion pour .NET
description: Définit les formats de fichiers de courrier électronique utilisés par les applications de messagerie pour stocker leurs diverses données notamment les messages électroniques les pièces jointes les dossiers les carnets dadresses etc. Inclut les types de fichiers suivants  Eml./emailfiletype/eml  Emlx./emailfiletype/emlx  Msg./emailfiletype/msg  Vcf./emailfiletype/vcf . Mbox./emailfiletype/mbox . Pst./emailfiletype/pst . Ost./emailfiletype/ost . En savoir plus sur les formats demailicihttps//wiki.fileformat.com/email .
type: docs
weight: 920
url: /fr/net/groupdocs.conversion.filetypes/emailfiletype/
---
## EmailFileType class

Définit les formats de fichiers de courrier électronique utilisés par les applications de messagerie pour stocker leurs diverses données, notamment les messages électroniques, les pièces jointes, les dossiers, les carnets d'adresses, etc. Inclut les types de fichiers suivants : [`Eml`](./eml) , [`Emlx`](./emlx) , [`Msg`](./msg) , [`Vcf`](./vcf) . [`Mbox`](./mbox) . [`Pst`](./pst) . [`Ost`](./ost) . En savoir plus sur les formats d'e-mail[ici](https://wiki.fileformat.com/email) .

```csharp
public sealed class EmailFileType : FileType
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [EmailFileType](emailfiletype)() | Constructeur de sérialisation |

## Propriétés

| Nom | La description |
| --- | --- |
| [Description](../../groupdocs.conversion.filetypes/filetype/description) { get; } | Description du type de fichier |
| [Extension](../../groupdocs.conversion.filetypes/filetype/extension) { get; } | L'extension de fichier |
| [Family](../../groupdocs.conversion.filetypes/filetype/family) { get; } | La famille de fichiers |
| [FileFormat](../../groupdocs.conversion.filetypes/filetype/fileformat) { get; } | Le format de fichier |

## Méthodes

| Nom | La description |
| --- | --- |
| [CompareTo](../../groupdocs.conversion.contracts/enumeration/compareto)(object) | Compare l'objet actuel à un autre. |
| override [Equals](../../groupdocs.conversion.filetypes/filetype/equals)(Enumeration) | Détermine si deux instances d'objet sont égales. |
| override [Equals](../../groupdocs.conversion.contracts/enumeration/equals)(object) | Détermine si deux instances d'objet sont égales. |
| override [GetHashCode](../../groupdocs.conversion.contracts/enumeration/gethashcode)() | Sert de fonction de hachage par défaut. |
| override [ToString](../../groupdocs.conversion.filetypes/filetype/tostring)() | Représentation sous forme de chaîne |

## Des champs

| Nom | La description |
| --- | --- |
| static readonly [Eml](../../groupdocs.conversion.filetypes/emailfiletype/eml) | Le format de fichier EML représente les messages électroniques enregistrés à l'aide d'Outlook et d'autres applications pertinentes. Presque tous les clients de messagerie prennent en charge ce format de fichier pour sa conformité avec la norme de format de message Internet RFC-822. En savoir plus sur ce format de fichier[ici](https://wiki.fileformat.com/email/eml) . |
| static readonly [Emlx](../../groupdocs.conversion.filetypes/emailfiletype/emlx) | Le format de fichier EMLX est implémenté et développé par Apple. L'application Apple Mail utilise le format de fichier EMLX pour exporter les e-mails. En savoir plus sur ce format de fichier[ici](https://wiki.fileformat.com/email/emlx) . |
| static readonly [Mbox](../../groupdocs.conversion.filetypes/emailfiletype/mbox) | Le format de fichier MBox est un terme générique qui représente un conteneur pour la collecte de messages électroniques. Les messages sont stockés dans le conteneur avec leurs pièces jointes. En savoir plus sur ce format de fichier[ici](https://docs.fileformat.com/email/mbox/) . |
| static readonly [Msg](../../groupdocs.conversion.filetypes/emailfiletype/msg) | MSG est un format de fichier utilisé par Microsoft Outlook et Exchange pour stocker des messages électroniques, des contacts, des rendez-vous ou d'autres tâches. En savoir plus sur ce format de fichier[ici](https://wiki.fileformat.com/email/msg) . |
| static readonly [Ost](../../groupdocs.conversion.filetypes/emailfiletype/ost) | OST ou les fichiers de stockage hors ligne représentent les données de la boîte aux lettres de l'utilisateur en mode hors ligne sur la machine locale lors de l'enregistrement auprès d'Exchange Server à l'aide de Microsoft Outlook. En savoir plus sur ce format de fichier[ici](https://wiki.fileformat.com/email/ost) . |
| static readonly [Pst](../../groupdocs.conversion.filetypes/emailfiletype/pst) | Les fichiers avec l'extension .PST représentent les fichiers de stockage personnels Outlook (également appelés tableau de stockage personnel) qui stockent diverses informations utilisateur. En savoir plus sur ce format de fichier[ici](https://wiki.fileformat.com/email/pst) . |
| static readonly [Vcf](../../groupdocs.conversion.filetypes/emailfiletype/vcf) | VCF (Virtual Card Format) ou vCard est un format de fichier numérique pour stocker les informations de contact. Le format est largement utilisé pour l'échange de données entre les applications d'échange d'informations populaires. En savoir plus sur ce format de fichier[ici](https://wiki.fileformat.com/email/vcf) . |

### Voir également

* class [FileType](../filetype)
* espace de noms [GroupDocs.Conversion.FileTypes](../../groupdocs.conversion.filetypes)
* Assemblée [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
