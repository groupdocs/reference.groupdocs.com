---
title: ResourceLoadBaseUri
second_title: GroupDocs.Assembly für .NET-API-Referenz
description: Ruft einen BasisURI ab oder legt einen BasisURI fest um die relativen URIs externer Ressourcendateien in absolute URIs aufzulösen während ein HTMLVorlagendokument geladen wird das zusammengesetzt und in einem NichtHTMLFormat gespeichert werden soll. Der Standardwert ist eine leere Zeichenfolge.
type: docs
weight: 20
url: /de/net/groupdocs.assembly/loadsaveoptions/resourceloadbaseuri/
---
## LoadSaveOptions.ResourceLoadBaseUri property

Ruft einen Basis-URI ab oder legt einen Basis-URI fest, um die relativen URIs externer Ressourcendateien in absolute URIs aufzulösen, während ein HTML-Vorlagendokument geladen wird, das zusammengesetzt und in einem Nicht-HTML-Format gespeichert werden soll. Der Standardwert ist eine leere Zeichenfolge.

```csharp
public string ResourceLoadBaseUri { get; set; }
```

### Bemerkungen

Beim Laden eines HTML-Dokuments aus einer Datei wird der enthaltende Ordner standardmäßig als Basis-URI verwendet, was beim Laden eines HTML-Dokuments aus einem Stream nicht passieren kann. Legen Sie diese Eigenschaft fest, um einen Basis-URI anzugeben, wenn ein HTML- -Dokument aus einem Stream geladen wird, oder um den standardmäßigen Basis-URI zu überschreiben, wenn ein HTML-Dokument aus einer Datei geladen wird.

Ein Wert dieser Eigenschaft wird in folgenden Fällen ignoriert:

* Ein geladenes HTML-Dokument enthält ein BASE-HTML-Element, das einen Basis-URI bereitstellt.
* Ein zu ladendes HTML-Dokument soll zusammengesetzt und in HTML gespeichert werden (externe Ressourcendateien werden nicht geladen und relative URIs werden dann nicht geändert).

### Siehe auch

* class [LoadSaveOptions](../../loadsaveoptions)
* namensraum [GroupDocs.Assembly](../../loadsaveoptions)
* Montage [GroupDocs.Assembly](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Assembly.dll -->