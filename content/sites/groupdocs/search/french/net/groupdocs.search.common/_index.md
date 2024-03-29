---
title: GroupDocs.Search.Common
second_title: Référence de l'API GroupDocs.Search pour .NET
description: Lespace de noms fournit des classes communes de la bibliothèque.
type: docs
weight: 20
url: /fr/net/groupdocs.search.common/
---
L'espace de noms fournit des classes communes de la bibliothèque.

## Des classes

| Classer | La description |
| --- | --- |
| [AttributeChangeBatch](./attributechangebatch) | Représente un conteneur pour les modifications d'attributs. |
| [Cancellation](./cancellation) | Représente un objet pour demander l'annulation d'une opération. |
| [ChunkSearchToken](./chunksearchtoken) | Représente un jeton pour la poursuite de la recherche par bloc (recherche par pages). |
| [CustomExtractorCollection](./customextractorcollection) | Contient une collection d'extracteurs personnalisés. Si la collection contient un extracteur pour une extension de fichier couverte par des extracteurs intégrés, alors cet extracteur sera utilisé à la place de celui intégré. |
| [Document](./document) | Représente la classe de base pour les documents ajoutés à un index à partir d'un système de fichiers, d'un flux ou d'une structure. Contient des méthodes statiques pour créer des documents à partir de différents types de sources. |
| [DocumentField](./documentfield) | Représente une donnée de champ de document. |
| [DocumentImage](./documentimage) | Représente les données d'une image de document. |
| [Encodings](./encodings) | Contient les noms des encodages possibles. |
| [ExtractedData](./extracteddata) | Représente les données extraites d'un document et préparées pour l'indexation. |
| [ExtractedItemInfo](./extractediteminfo) | Représente les informations d'un élément de conteneur. |
| [ExtractorSettings](./extractorsettings) | Contient les paramètres de l'extracteur de données de document. |
| [FileLogger](./filelogger) | Représente un enregistreur qui consigne les événements et les erreurs dans un fichier local. |
| [FileOutputAdapter](./fileoutputadapter) | Représente un adaptateur de sortie qui collecte la sortie dans un fichier. |
| [FragmentContainer](./fragmentcontainer) | Représente un conteneur pour les fragments de texte avec les termes trouvés en surbrillance d'un champ de document. |
| [ImageFrame](./imageframe) | Représente un cadre d'image. |
| [IndexInfo](./indexinfo) | Contient des informations de base sur un[`Index`](../groupdocs.search/index) . |
| [IndexingReport](./indexingreport) | Représente une information détaillée sur une opération d'indexation. |
| [Notification](./notification) | La classe de base pour toutes les notifications à l'index. Cette classe contient également des méthodes pour créer des objets de notification. |
| [OutputAdapter](./outputadapter) | Représente la classe de base d'un adaptateur de sortie utilisé pour collecter une sortie sous une forme généralisée. Les adaptateurs actuellement disponibles sont[`FileOutputAdapter`](../groupdocs.search.common/fileoutputadapter) , [`StreamOutputAdapter`](../groupdocs.search.common/streamoutputadapter) , [`StructureOutputAdapter`](../groupdocs.search.common/structureoutputadapter) , et[`StringOutputAdapter`](../groupdocs.search.common/stringoutputadapter) . |
| [ResultBuilderFactory](./resultbuilderfactory) | Représente la classe de base d'une fabrique de générateur de résultats. |
| [SearchImage](./searchimage) | Représente une image à rechercher. |
| [SearchReport](./searchreport) | Représente une information détaillée sur une opération de recherche. |
| [StreamOutputAdapter](./streamoutputadapter) | Représente un adaptateur de sortie qui collecte la sortie dans unStream . |
| [StringOutputAdapter](./stringoutputadapter) | Représente un adaptateur de sortie qui collecte la sortie en tant queString . |
| [StructureOutputAdapter](./structureoutputadapter) | Représente un adaptateur de sortie qui collecte la sortie sous la forme d'une structure contenant chaque champ séparément. |
| [WordPattern](./wordpattern) | Représente un modèle de mot à utiliser dans la recherche de mots génériques. |
## Interfaces

| Interface | La description |
| --- | --- |
| [IContainerItemExtractor](./icontaineritemextractor) | Fournit des méthodes pour extraire des éléments de documents conteneurs. |
| [IDocumentLoader](./idocumentloader) | Définit l'interface du chargeur de documents utilisée pour charger les documents paresseux. |
| [IFieldExtractor](./ifieldextractor) | Fournit des méthodes pour extraire des champs d'un document. |
| [ILogger](./ilogger) | Définit l'interface d'un enregistreur utilisé pour consigner les événements et les erreurs dans un index. |
## Énumération

| Énumération | La description |
| --- | --- |
| [DocumentSourceKind](./documentsourcekind) | Définit les types de sources de documents. |
| [DocumentStatus](./documentstatus) | Représente un statut de traitement de document. |
| [IndexStatus](./indexstatus) | Spécifie un état d'index. |
| [VersionUpdateResult](./versionupdateresult) | Représente le résultat d'une opération de mise à jour de la version d'index. |

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Search.dll -->
