---
title: Sanitize
second_title: GroupDocs.Metadata voor .NET API-referentie
description: Verwijdert beschrijfbare metadataeigenschappen van alle gedetecteerde pakketten of hele pakketten indien mogelijk. De bewerking is recursief dus het is ook van invloed op alle geneste pakketten.
type: docs
weight: 100
url: /nl/net/groupdocs.metadata/metadata/sanitize/
---
## Metadata.Sanitize method

Verwijdert beschrijfbare metadata-eigenschappen van alle gedetecteerde pakketten of hele pakketten indien mogelijk. De bewerking is recursief, dus het is ook van invloed op alle geneste pakketten.

```csharp
public int Sanitize()
```

### Winstwaarde

Het aantal getroffen eigendommen.

### Opmerkingen

**Kom meer te weten**

* [Schone metagegevens](https://docs.groupdocs.com/display/metadatanet/Clean+metadata)

### Voorbeelden

Dit voorbeeld laat zien hoe u alle gedetecteerde metadatapakketten/eigenschappen uit een bestand kunt verwijderen.

```csharp
using (Metadata metadata = new Metadata(Constants.InputPdf))
{
    // Verwijder gedetecteerde metadatapakketten
    var affected = metadata.Sanitize();
    Console.WriteLine("Properties removed: {0}", affected);

    metadata.Save(Constants.OutputPdf);
}
```

### Zie ook

* class [Metadata](../../metadata)
* naamruimte [GroupDocs.Metadata](../../metadata)
* montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
