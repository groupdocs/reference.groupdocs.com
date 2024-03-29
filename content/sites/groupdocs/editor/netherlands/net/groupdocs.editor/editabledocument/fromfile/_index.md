---
title: FromFile
second_title: GroupDocs.Editor voor .NET API-referentie
description: Statische fabriek die een exemplaar van EditableDocument maakt van een HTMLbestand dat wordt gespecificeerd door een pad naar het .htmlbestand zelf en een map met gekoppelde bronnen
type: docs
weight: 10
url: /nl/net/groupdocs.editor/editabledocument/fromfile/
---
## EditableDocument.FromFile method

Statische fabriek, die een exemplaar van EditableDocument maakt van een HTML-bestand, dat wordt gespecificeerd door een pad naar het *.html-bestand zelf en een map met gekoppelde bronnen

```csharp
public static EditableDocument FromFile(string htmlFilePath, string resourceFolderPath)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| htmlFilePath | String | String, die een volledig pad naar het HTML-bestand bevat. Mag niet null zijn, moet een geldig bestandspad zijn en het bestand zelf moet bestaan. |
| resourceFolderPath | String | Optioneel pad naar de map met HTML-resources. Als NULL, ongeldig of een dergelijke map niet bestaat, zal Editor zelf proberen deze map te vinden door de HTML-opmaak te analyseren |

### Winstwaarde

Nieuw niet-null exemplaar van EditableDocument

### Uitzonderingen

| uitzondering | voorwaarde |
| --- | --- |
| ArgumentException | HTML-bestandspad en/of het pad naar de bronmap is/zijn ongeldig |
| FileNotFoundException | Opgegeven HTML-bestand kan niet worden gevonden |

### Zie ook

* class [EditableDocument](../../editabledocument)
* naamruimte [GroupDocs.Editor](../../editabledocument)
* montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
