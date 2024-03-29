---
title: ToDateTime
second_title: Référence de l'API GroupDocs.Signature pour .NET
description: Convertit en DateHeure.
type: docs
weight: 100
url: /fr/net/groupdocs.signature.domain/metadatasignature/todatetime/
---
## ToDateTime() {#todatetime}

Convertit en DateHeure.

```csharp
public virtual DateTime ToDateTime()
```

### Return_Value

Renvoie la valeur de la signature des métadonnées sous la forme DateTime.

### Remarques

Lève une exception si la valeur Metadata n'a pas pu être convertie. Si la valeur d'origine est basée sur une chaîne, les informations de propriété de culture par défaut seront utilisées à partir des propriétés SignatureSettings[`DefaultCulture`](../../../groupdocs.signature/signaturesettings/defaultculture)

### Voir également

* class [MetadataSignature](../../metadatasignature)
* espace de noms [GroupDocs.Signature.Domain](../../metadatasignature)
* Assemblée [GroupDocs.Signature](../../../)

---

## ToDateTime(IFormatProvider) {#todatetime_1}

Convertit en DateHeure.

```csharp
public virtual DateTime ToDateTime(IFormatProvider provider)
```

| Paramètre | Taper | La description |
| --- | --- | --- |
| provider | IFormatProvider | Formater le fournisseur de données à utiliser avec les opérations de conversion de données. |

### Return_Value

Renvoie la valeur de la signature des métadonnées sous la forme DateTime.

### Remarques

Lève une exception si la valeur des métadonnées n'a pas pu être convertie

### Voir également

* class [MetadataSignature](../../metadatasignature)
* espace de noms [GroupDocs.Signature.Domain](../../metadatasignature)
* Assemblée [GroupDocs.Signature](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->
