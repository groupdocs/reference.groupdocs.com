---
title: Remove
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Entfernt Wasserzeichen aus dem Dokument.
type: docs
weight: 90
url: /de/net/groupdocs.watermark/watermarker/remove/
---
## Remove(PossibleWatermark) {#remove}

Entfernt Wasserzeichen aus dem Dokument.

```csharp
public void Remove(PossibleWatermark possibleWatermark)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| possibleWatermark | PossibleWatermark | Das zu entfernende Wasserzeichen. |

### Bemerkungen

Weitere Informationen zum Entfernen von Wasserzeichen: [Gefundene Wasserzeichen entfernen](https://docs.groupdocs.com/display/watermarknet/Removing+found+watermarks) .

### Beispiele

Suchen und entfernen Sie das erste mögliche Wasserzeichen, das einen bestimmten Text oder ein bestimmtes Bild enthält, aus einem Dokument eines beliebigen unterstützten Typs.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    ImageSearchCriteria imageSearchCriteria = new ImageDctHashSearchCriteria(@"D:\logo.png");
    Regex regex = new Regex(@"^Company\sName$", RegexOptions.IgnoreCase);
    TextSearchCriteria textSearchCriteria = new TextSearchCriteria(regex);
    PossibleWatermarkCollection watermarks = watermarker.Search(textSearchCriteria.Or(imageSearchCriteria));
    if (watermarks.Count > 0)
    {
        watermarker.Remove(watermarks[0]);
    }

    watermarker.Save(@"D:\output.doc");
}
```

### Siehe auch

* class [PossibleWatermark](../../../groupdocs.watermark.search/possiblewatermark)
* class [Watermarker](../../watermarker)
* namensraum [GroupDocs.Watermark](../../watermarker)
* Montage [GroupDocs.Watermark](../../../)

---

## Remove(PossibleWatermarkCollection) {#remove_1}

Entfernt alle Wasserzeichen in der Sammlung aus dem Dokument.

```csharp
public void Remove(PossibleWatermarkCollection possibleWatermarks)
```

| Parameter | Typ | Beschreibung |
| --- | --- | --- |
| possibleWatermarks | PossibleWatermarkCollection | Die Sammlung der zu entfernenden Wasserzeichen. |

### Bemerkungen

Weitere Informationen zum Entfernen von Wasserzeichen [Gefundene Wasserzeichen entfernen](https://docs.groupdocs.com/display/watermarknet/Removing+found+watermarks) .

### Beispiele

Suchen und entfernen Sie alle möglichen Wasserzeichen, die einen bestimmten Text oder ein bestimmtes Bild aus einem Dokument eines beliebigen unterstützten Typs enthalten.

```csharp
using (Watermarker watermarker = new Watermarker(@"D:\input.doc"))
{
    ImageSearchCriteria imageSearchCriteria = new ImageDctHashSearchCriteria(@"D:\logo.png");
    Regex regex = new Regex(@"^Company\sName$", RegexOptions.IgnoreCase);
    TextSearchCriteria textSearchCriteria = new TextSearchCriteria(regex);
    PossibleWatermarkCollection watermarks = watermarker.Search(textSearchCriteria.Or(imageSearchCriteria));
    watermarker.Remove(watermarks);
    watermarker.Save(@"D:\output.doc");
}
```

### Siehe auch

* class [PossibleWatermarkCollection](../../../groupdocs.watermark.search/possiblewatermarkcollection)
* class [Watermarker](../../watermarker)
* namensraum [GroupDocs.Watermark](../../watermarker)
* Montage [GroupDocs.Watermark](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->