---
title: AddProperties
second_title: GroupDocs.Metadata voor .NET API-referentie
description: Voegt bekende metadataeigenschappen toe die voldoen aan het opgegeven predikaat. De bewerking is recursief dus het is ook van invloed op alle geneste pakketten.
type: docs
weight: 60
url: /nl/net/groupdocs.metadata.common/metadatapackage/addproperties/
---
## MetadataPackage.AddProperties method

Voegt bekende metadata-eigenschappen toe die voldoen aan het opgegeven predikaat. De bewerking is recursief, dus het is ook van invloed op alle geneste pakketten.

```csharp
public int AddProperties(Func<MetadataProperty, bool> predicate, PropertyValue value)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| predicate | Func`2 | Een functie om elke metadata-eigenschap te testen op een voorwaarde. |
| value | PropertyValue | Een waarde voor de gekozen eigenschappen. |

### Winstwaarde

Het aantal getroffen eigendommen.

### Opmerkingen

**Kom meer te weten**

* Meer voorbeelden die het gebruik van deze methode demonstreren: [Metagegevens toevoegen](https://docs.groupdocs.com/display/metadatanet/Adding+metadata)

### Zie ook

* delegate [Func&lt;T,TResult&gt;](../../func-2)
* class [MetadataProperty](../../metadataproperty)
* class [PropertyValue](../../propertyvalue)
* class [MetadataPackage](../../metadatapackage)
* naamruimte [GroupDocs.Metadata.Common](../../metadatapackage)
* montage [GroupDocs.Metadata](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Metadata.dll -->
