---
title: WoffFont
second_title: GroupDocs.Editor voor .NET API-referentie
description: Maakt nieuwe WoffFontklasse van inhoud weergegeven als base64gecodeerde tekenreeks en met gespecificeerde naam
type: docs
weight: 10
url: /nl/net/groupdocs.editor.htmlcss.resources.fonts/wofffont/wofffont/
---
## WoffFont(string, string) {#constructor_1}

Maakt nieuwe WoffFont-klasse van inhoud, weergegeven als base64-gecodeerde tekenreeks, en met gespecificeerde naam

```csharp
public WoffFont(string name, string contentInBase64)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| name | String | Naam van het WOFF-lettertype. Mag niet null, leeg of spaties zijn. |
| contentInBase64 | String | Inhoud als base64-gecodeerde tekenreeks. Mag niet null, leeg of spaties zijn. Als het geen WOFF-inhoud is, wordt er een uitzondering gegenereerd. |

### Uitzonderingen

| uitzondering | voorwaarde |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Zie ook

* class [WoffFont](../../wofffont)
* naamruimte [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../wofffont)
* montage [GroupDocs.Editor](../../../)

---

## WoffFont(string, Stream) {#constructor}

Creëert nieuwe WoffFont-klasse van inhoud, weergegeven als bytestroom, en met gespecificeerde naam

```csharp
public WoffFont(string name, Stream binaryContent)
```

| Parameter | Type | Beschrijving |
| --- | --- | --- |
| name | String | Naam van het WOFF-lettertype. Mag niet null, leeg of spaties zijn. |
| binaryContent | Stream | Inhoud als bytestroom. Het lezen begint vanaf de oorspronkelijke positie. Kan niet nul zijn. Moet leesbaar en zeebaar zijn. Als deze instantie wordt verwijderd, wordt deze stream ook verwijderd. |

### Uitzonderingen

| uitzondering | voorwaarde |
| --- | --- |
| ArgumentException |  |
| [InvalidImageFormatException](../../../groupdocs.editor.htmlcss.exceptions/invalidimageformatexception) |  |

### Zie ook

* class [WoffFont](../../wofffont)
* naamruimte [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../wofffont)
* montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
