---
title: IptcEnvelopeRecordDataSet
second_title: Référence de l'API GroupDocs.Metadata pour .NET
description: Définit les numéros densemble de données denregistrement denveloppe IPTC.
type: docs
weight: 2920
url: /fr/net/groupdocs.metadata.standards.iptc/iptcenveloperecorddataset/
---
## IptcEnvelopeRecordDataSet enumeration

Définit les numéros d'ensemble de données d'enregistrement d'enveloppe IPTC.

```csharp
public enum IptcEnvelopeRecordDataSet
```

### Valeurs

| Nom | Évaluer | La description |
| --- | --- | --- |
| ModelVersion | `0` | Un nombre binaire identifiant la version de l'Information  Interchange Model, Part I, utilisé par le fournisseur. Les numéros de version sont attribués par IPTC et NAA.  Le numéro de version de cet enregistrement est quatre (4). |
| Destination | `5` | Facultatif, répétable, maximum 1024 octets, composé de caractères graphiques séquentiellement contigus.  Ce DataSet est destiné à accueillir certains fournisseurs qui ont besoin d'informations de routage au-dessus des couches OSI appropriées. |
| FileFormat | `20` | Format de fichier. |
| FileFormatVersion | `22` | Obligatoire, non répétable, deux octets.  Un nombre binaire représentant la version particulière du format de fichier spécifié dans 1:20.  Une liste des formats de fichiers, y compris les références croisées des versions, est incluse dans l'annexe A. |
| ServiceIdentifier | `30` | Obligatoire, non répétable. Jusqu'à 10 octets, composés de caractères graphiques.  Identifie le fournisseur et le produit. |
| EnvelopeNumber | `40` | Obligatoire, non répétable, huit octets, composé de caractères numériques.  Les caractères forment un nombre qui sera unique pour la date spécifiée en 1:70 et pour l'Identifiant de Service spécifié en 1:30.  Si des numéros d'enveloppe identiques apparaissent avec la même date et avec le même identifiant de service, les enregistrements 2 à 9 doivent être inchangés par rapport à l'original.  Il ne s'agit pas d'un contrôle séquentiel de réception du numéro de série . |
| ProductID | `50` | Facultatif, répétable. Jusqu'à 32 octets, composés de caractères graphiques.  Permet à un fournisseur d'identifier des sous-ensembles de son service global.  Utilisé pour fournir les données de l'organisation réceptrice sur lesquelles sélectionner, acheminer ou autrement gérer les données. |
| EnvelopePriority | `60` | Facultatif, non répétable. Un seul octet, composé d'un caractère numérique.  Spécifie la priorité de traitement des enveloppes et non l'urgence éditoriale (voir 2:10, Urgence). '1' indique la copie la plus urgente, '5' l'urgence normale, et '8' la copie la moins urgente. Le chiffre '9' indique une priorité définie par l'utilisateur. Le chiffre '0' est réservé pour une utilisation future. |
| DateSent | `70` | Obligatoire, non répétable. Huit octets, composés de caractères numériques.  Utilise le format CCYYMMDD (siècle, année, mois, jour) tel que défini dans la norme ISO 8601 pour indiquer l'année, le mois et le jour où le service a envoyé le matériel. |
| TimeSent | `80` | Utilise le format HHMMSS±HHMM où HHMMSS fait référence à l'heure, les minutes et les secondes locales et HHMM fait référence aux heures et minutes en avance (+) ou en retard (-) sur le temps universel coordonné comme décrit dans la norme ISO 8601. Il s'agit de l'heure à laquelle le service a envoyé le matériel. |
| CodedCharacterSet | `90` | Facultatif, non répétable, jusqu'à 32 octets, consistant en une ou plusieurs fonctions de contrôle utilisées pour l'annonce, l'invocation ou la désignation de jeux de caractères codés. Les fonctions de contrôle suivent la norme ISO 2022 et peuvent être constituées du caractère de contrôle d'échappement et d'un ou plusieurs caractères graphiques. Pour plus de détails voir l'annexe C, la bibliothèque de codes IPTC-NAA. |
| Uno | `100` | Non valide (identifiant éternel). |
| ArmIdentifier | `120` | Le DataSet identifie la méthode de relation abstraite (ARM) qui est décrite dans un document enregistré par l'auteur de l'ARM auprès de l'IPTC et de la NAA. |
| ArmVersion | `122` | Nombre binaire représentant la version particulière de l'ARM spécifié dans DataSet 1:120. |

### Voir également

* espace de noms [GroupDocs.Metadata.Standards.Iptc](../../groupdocs.metadata.standards.iptc)
* Assemblée [GroupDocs.Metadata](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
