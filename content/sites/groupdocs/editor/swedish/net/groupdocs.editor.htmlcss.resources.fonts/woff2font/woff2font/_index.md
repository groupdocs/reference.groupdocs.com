---
title: Woff2Font
second_title: GroupDocs.Editor för .NET API-referens
description: Skapar ny Woff2Fontklass från innehåll representerad som base64kodad sträng och med specificerat namn
type: docs
weight: 10
url: /sv/net/groupdocs.editor.htmlcss.resources.fonts/woff2font/woff2font/
---
## Woff2Font(string, string) {#constructor_1}

Skapar ny Woff2Font-klass från innehåll, representerad som base64-kodad sträng och med specificerat namn

```csharp
public Woff2Font(string name, string contentInBase64)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| name | String | Namnet på WOFF2-teckensnittet. Kan inte vara null, tom eller blanksteg. |
| contentInBase64 | String | Innehåll som base64-kodad sträng. Kan inte vara null, tom eller blanksteg. Om det inte är ett WOFF2-innehåll kommer undantag att kastas. |

### Undantag

| undantag | skick |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Se även

* class [Woff2Font](../../woff2font)
* namnutrymme [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../woff2font)
* hopsättning [GroupDocs.Editor](../../../)

---

## Woff2Font(string, Stream) {#constructor}

Skapar en ny Woff2Font-klass från innehåll, representerat som byteström och med specificerat namn

```csharp
public Woff2Font(string name, Stream binaryContent)
```

| Parameter | Typ | Beskrivning |
| --- | --- | --- |
| name | String | Namnet på WOFF2-teckensnittet. Kan inte vara null, tom eller blanksteg. |
| binaryContent | Stream | Innehåll som byteström. Läsningen börjar från den ursprungliga positionen. Kan inte vara null. Bör vara läsbar och öppningsbar. Om den här instansen kommer att kasseras kommer även denna ström att kasseras. |

### Undantag

| undantag | skick |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Se även

* class [Woff2Font](../../woff2font)
* namnutrymme [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../woff2font)
* hopsättning [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
