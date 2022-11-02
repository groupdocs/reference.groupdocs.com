---
title: FromMarkup
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Statische Factory die eine Instanz von EditableDocument aus dem angegebenen HTMLMarkup und einem Satz entsprechender verknüpfter Ressourcen erstellt
type: docs
weight: 20
url: /de/net/groupdocs.editor/editabledocument/frommarkup/
---
## EditableDocument.FromMarkup method

Statische Factory, die eine Instanz von EditableDocument aus dem angegebenen HTML-Markup und einem Satz entsprechender verknüpfter Ressourcen erstellt

```csharp
public static EditableDocument FromMarkup(string newHtmlContent, 
    IEnumerable<IHtmlResource> resources)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| newHtmlContent | String | Zeichenfolge, die rohes HTML-Markup enthält, das analysiert werden sollte. Darf nicht NULL, leer oder ungültig sein. |
| resources | IEnumerable`1 | Sammlung aller Ressourcen (Bilder, Stylesheets, Schriftarten), die in dem in angegebenen HTML-Dokument verwendet werden*newHtmlContent* Parameter. Kann fehlen (NULL oder leere Sammlung). |

### Rückgabewert

Neue Nicht-Null-Instanz von EditableDocument

### Ausnahmen

| Ausnahme | Bedingung |
| --- | --- |
| ArgumentException | Zeichenfolge mit eingegebenem Roh-HTML-Markup darf nicht null oder leer sein |

### Siehe auch

* interface [IHtmlResource](../../../groupdocs.editor.htmlcss.resources/ihtmlresource)
* class [EditableDocument](../../editabledocument)
* namensraum [GroupDocs.Editor](../../editabledocument)
* Montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->