---
title: MetadataSignOptions
second_title: Référence de l'API GroupDocs.Signature pour .NET
description: Représente les options de signature des métadonnées.
type: docs
weight: 1490
url: /fr/net/groupdocs.signature.options/metadatasignoptions/
---
## MetadataSignOptions class

Représente les options de signature des métadonnées.

```csharp
public class MetadataSignOptions : SignOptions
```

## Constructeurs

| Nom | La description |
| --- | --- |
| [MetadataSignOptions](metadatasignoptions#constructor)() | Initialise une nouvelle instance de la classe MetadataSignOptions avec les valeurs par défaut. |
| [MetadataSignOptions](metadatasignoptions#constructor_1)(IEnumerable&lt;MetadataSignature&gt;) | Initialise une nouvelle instance de la classe MetadataSignOptions avec Metadata. |

## Propriétés

| Nom | La description |
| --- | --- |
| virtual [AllPages](../../groupdocs.signature.options/signoptions/allpages) { get; set; } | Mettre la signature sur toutes les pages du document. |
| [Appearance](../../groupdocs.signature.options/signoptions/appearance) { get; set; } | Apparence de signature supplémentaire. |
| [DataEncryption](../../groupdocs.signature.options/metadatasignoptions/dataencryption) { get; set; } | Obtient ou définit l'implémentation de[`IDataEncryption`](../../groupdocs.signature.domain.extensions/idataencryption)interface pour chiffrer toutes les signatures de métadonnées avec cette collection d'options. Si cette valeur est définie, toutes les signatures ajoutées utiliseront ce chiffrement par défaut ou son propre DataEncryption s'il a été attribué. |
| [DocumentType](../../groupdocs.signature.options/signoptions/documenttype) { get; set; } | Obtenir ou définir le type de document des options de signature[`DocumentType`](../../groupdocs.signature.domain/documenttype) |
| [Extensions](../../groupdocs.signature.options/signoptions/extensions) { get; } | Extensions de signature. |
| virtual [PageNumber](../../groupdocs.signature.options/signoptions/pagenumber) { get; set; } | Obtient ou définit le numéro de page du document pour la signature. La valeur minimale et par défaut est 1. |
| virtual [PagesSetup](../../groupdocs.signature.options/signoptions/pagessetup) { get; set; } | Options pour spécifier les pages à signer. |
| [Signatures](../../groupdocs.signature.options/metadatasignoptions/signatures) { get; set; } | Obtient ou définit les métadonnées de la signature. |
| [SignatureType](../../groupdocs.signature.options/signoptions/signaturetype) { get; } | Obtenir le type de signature[`SignatureType`](../../groupdocs.signature.domain/signaturetype) |
| [ZOrder](../../groupdocs.signature.options/signoptions/zorder) { get; set; } | Obtient ou définit la position de l'ordre Z de la signature textuelle. Détermine l'ordre d'affichage des signatures qui se chevauchent. |

## Méthodes

| Nom | La description |
| --- | --- |
| [Add](../../groupdocs.signature.options/metadatasignoptions/add)(MetadataSignature) | Ajouter une instance MetadataSignature existante à la collection. |
| [AddImageSignature](../../groupdocs.signature.options/metadatasignoptions/addimagesignature)(ushort, object) | Crée une nouvelle ImageMetadataSignature avec les arguments passés et l'ajoute à la collection. |
| [AddPdfSignature](../../groupdocs.signature.options/metadatasignoptions/addpdfsignature)(string, object, string) | Crée un nouveau PdfMetadataSignature avec les arguments passés et l'ajoute à la collection. |

### Remarques

**Apprendre encore plus**

* Utilisation de base de la création de signature électronique de métadonnées par GroupDocs.Signature : [Comment signer un document électronique avec signature de métadonnées](https://docs.groupdocs.com/display/signaturenet/eSign+document+with+Metadata+signature)
* Utilisation avancée des paramètres de signature électronique des métadonnées avec GroupDocs.Signature : [Utilisation avancée du document eSign avec signature de métadonnées et paramètres supplémentaires](https://docs.groupdocs.com/display/signaturenet/Sign+document+with+Metadata+signature+-+advanced)

### Voir également

* class [SignOptions](../signoptions)
* espace de noms [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* Assemblée [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
