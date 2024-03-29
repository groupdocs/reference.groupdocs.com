---
title: FontsToExclude
second_title: GroupDocs.Viewer voor .NET API-referentie
description: De lijst met lettertypenamen die moeten worden uitgesloten van HTMLdocument.
type: docs
weight: 40
url: /nl/net/groupdocs.viewer.options/htmlviewoptions/fontstoexclude/
---
## HtmlViewOptions.FontsToExclude property

De lijst met lettertypenamen die moeten worden uitgesloten van HTML-document.

```csharp
public List<string> FontsToExclude { get; set; }
```

### Opmerkingen

Deze optie wordt alleen ondersteund voor presentaties. De lettertypen die aan het HTML-document worden toegevoegd, verbeteren de stabiliteit van de uitvoerweergave, en vergroten tegelijkertijd de grootte van het weergaveresultaat. Met deze optie, let vindt u een compromis tussen stabiliteit en uitvoergrootte. Neem de lettertypenamen op die populair zijn en in de meeste systemen zijn geïnstalleerd. Let op: deze eigenschap is alleen actief wanneer[`ExcludeFonts`](../excludefonts) opties is uitgeschakeld.

### Zie ook

* class [HtmlViewOptions](../../htmlviewoptions)
* naamruimte [GroupDocs.Viewer.Options](../../htmlviewoptions)
* montage [GroupDocs.Viewer](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Viewer.dll -->
