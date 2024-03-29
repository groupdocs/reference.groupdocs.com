---
title: GetBodyContent
second_title: GroupDocs.Editor för .NET API-referens
description: Returnerar en brödtext i HTMLdokumentet inre innehåll mellan öppnande och avslutande BODYtaggar utan dessa taggar som en sträng.
type: docs
weight: 120
url: /sv/net/groupdocs.editor/editabledocument/getbodycontent/
---
## GetBodyContent() {#getbodycontent}

Returnerar en brödtext i HTML-dokumentet (inre innehåll mellan öppnande och avslutande BODY-taggar utan dessa taggar) som en sträng.

```csharp
public string GetBodyContent()
```

### Returvärde

String, som innehåller HTML-dokumentets brödtext (utan öppnande och stängande BODY-taggar)

### Anmärkningar

De flesta WYSIWYG-redigerare arbetar vanligtvis med det inre innehållet i dokumentets BODY och kan inte korrekt bearbeta dess metainformation från HEAD-blocket. Denna metod är utformad för sådana fall. Denna överbelastning tillåter inte att justera URI:er för externa resursbegäranden.

### Se även

* class [EditableDocument](../../editabledocument)
* namnutrymme [GroupDocs.Editor](../../editabledocument)
* hopsättning [GroupDocs.Editor](../../../)

---

## GetBodyContent(string) {#getbodycontent_1}

Returnerar en brödtext i HTML-dokumentet (inre innehåll mellan öppnande och avslutande BODY-taggar utan dessa taggar) som en sträng, där länkar till de externa resurserna innehåller specificerat prefix.

```csharp
public string GetBodyContent(string externalImagesPrefix)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| externalImagesPrefix | String | Genom denna parameter som används kan ange ett prefix, som kommer att läggas till i links till alla externa bilder i IMG-element, som kommer att finnas i den resulterande HTML-strängen. Om NULL eller tomt, kommer prefix inte att läggas till. |

### Returvärde

String, som innehåller HTML-dokumentets brödtext (utan öppnande och stängande BODY-taggar) med länkar, anpassad till de externa bilderna

### Anmärkningar

De flesta WYSIWYG-redigerare arbetar vanligtvis med det inre innehållet i dokumentets BODY och kan inte korrekt bearbeta dess metainformation från HEAD-blocket. Denna metod är utformad för sådana fall. Denna överbelastning gör det möjligt att justera URI:er för externa resursbegäranden.

### Se även

* class [EditableDocument](../../editabledocument)
* namnutrymme [GroupDocs.Editor](../../editabledocument)
* hopsättning [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
