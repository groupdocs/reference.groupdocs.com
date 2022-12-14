---
title: GroupDocs.Redaction.Integration
second_title: Référence de l'API GroupDocs.Redaction pour .NET
description: LeIntegrationnamespace fournit des interfaces et des classes utilisées pour intégrer des documents de différents formats avec GroupDocs.Redaction.
type: docs
weight: 40
url: /fr/net/groupdocs.redaction.integration/
---
LeIntegrationnamespace fournit des interfaces et des classes, utilisées pour intégrer des documents de différents formats avec GroupDocs.Redaction.

## Des classes

| Classer | La description |
| --- | --- |
| [DocumentFormatInstance](./documentformatinstance) | Représente un format spécifique d'un document. Implémentez cette classe pour ajouter vos propres types de documents. |
| [MetadataCollection](./metadatacollection) | Représente un dictionnaire de[`MetadataItem`](../groupdocs.redaction.integration/metadataitem) avec son titre comme clé. |
| [MetadataItem](./metadataitem) | Représente un élément de métadonnées, commun à tous les formats pris en charge et utilisé dans les suppressions de métadonnées. |
## Interfaces

| Interface | La description |
| --- | --- |
| [IAnnotatedDocument](./iannotateddocument) | Définit les méthodes requises pour accéder aux annotations, telles que les commentaires. Doit être mis en œuvre par[`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance) - classe dérivée pour effectuer des suppressions d'annotations. |
| [ICellularFormatInstance](./icellularformatinstance) | Définit les méthodes requises pour accéder aux formats de feuille de calcul, ayant une ou plusieurs feuilles de calcul. |
| [IImageFormatInstance](./iimageformatinstance) | Définit les méthodes requises pour les suppressions de format d'image raster. |
| [IMetadataAccess](./imetadataaccess) | Définit les méthodes requises pour accéder aux métadonnées d'un document, si le format le prend en charge. |
| [IPaginatedDocument](./ipaginateddocument) | Définit les méthodes requises pour manipuler les pages d'un document. Doit être mis en œuvre par[`DocumentFormatInstance`](../groupdocs.redaction.integration/documentformatinstance) -classe dérivée pour effectuer des suppressions de pages. |
| [IPreviewable](./ipreviewable) | Définit les méthodes pour créer un aperçu du document. |
| [IRasterizableDocument](./irasterizabledocument) | Définit les méthodes requises pour enregistrer un document sous n'importe quelle forme binaire. Les types intégrés enregistrent un document au format PDF avec des images de ses pages. |
| [ITextualFormatInstance](./itextualformatinstance) | Définit les méthodes requises pour la rédaction de données textuelles dans tout document contenant du texte. |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Redaction.dll -->
