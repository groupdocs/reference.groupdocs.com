---
title: GetBodyContent
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Gibt einen Hauptteil des HTMLDokuments innerer Inhalt zwischen öffnenden und schließenden BODYTags ohne diese Tags als Zeichenfolge zurück.
type: docs
weight: 120
url: /de/net/groupdocs.editor/editabledocument/getbodycontent/
---
## GetBodyContent() {#getbodycontent}

Gibt einen Hauptteil des HTML-Dokuments (innerer Inhalt zwischen öffnenden und schließenden BODY-Tags ohne diese Tags) als Zeichenfolge zurück.

```csharp
public string GetBodyContent()
```

### Rückgabewert

String, der den Body des HTML-Dokuments enthält (ohne öffnende und schließende BODY-Tags)

### Bemerkungen

Die meisten WYSIWYG-Editoren arbeiten normalerweise mit dem inneren Inhalt des BODY des Dokuments und können dessen Metainformationen aus dem HEAD-Block nicht korrekt verarbeiten. Diese Methode ist für solche Fälle gedacht. Diese Überladung erlaubt es nicht, URIs für externe Ressourcenanforderungen anzupassen.

### Siehe auch

* class [EditableDocument](../../editabledocument)
* namensraum [GroupDocs.Editor](../../editabledocument)
* Montage [GroupDocs.Editor](../../../)

---

## GetBodyContent(string) {#getbodycontent_1}

Gibt einen Hauptteil des HTML-Dokuments (innerer Inhalt zwischen öffnenden und schließenden BODY-Tags ohne diese Tags) als Zeichenfolge zurück, wobei Links zu externen Ressourcen das angegebene Präfix enthalten.

```csharp
public string GetBodyContent(string externalImagesPrefix)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| externalImagesPrefix | String | Durch diesen verwendeten Parameter kann ein Präfix angegeben werden, das den links zu allen externen Bildern in IMG-Elementen hinzugefügt wird, die im resultierenden HTML-String vorhanden sein werden. Wenn NULL oder leer, werden keine Präfixe hinzugefügt. |

### Rückgabewert

String, der den Body des HTML-Dokuments (ohne öffnende und schließende BODY-Tags) mit Links enthält, angepasst an die externen Bilder

### Bemerkungen

Die meisten WYSIWYG-Editoren arbeiten normalerweise mit dem inneren Inhalt des BODY des Dokuments und können dessen Metainformationen aus dem HEAD-Block nicht korrekt verarbeiten. Diese Methode ist für solche Fälle gedacht. Diese Überladung ermöglicht das Anpassen von URIs für externe Ressourcenanforderungen.

### Siehe auch

* class [EditableDocument](../../editabledocument)
* namensraum [GroupDocs.Editor](../../editabledocument)
* Montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
