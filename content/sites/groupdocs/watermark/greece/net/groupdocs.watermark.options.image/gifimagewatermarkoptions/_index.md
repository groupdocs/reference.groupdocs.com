---
title: GifImageWatermarkOptions
second_title: GroupDocs.Watermark για Αναφορά API .NET
description: Αντιπροσωπεύει επιλογές προσθήκης υδατογραφήματος κατά την προσθήκη υδατογραφήματος σε εικόνα GIF.
type: docs
weight: 1760
url: /el/net/groupdocs.watermark.options.image/gifimagewatermarkoptions/
---
## GifImageWatermarkOptions class

Αντιπροσωπεύει επιλογές προσθήκης υδατογραφήματος κατά την προσθήκη υδατογραφήματος σε εικόνα GIF.

```csharp
public sealed class GifImageWatermarkOptions : MultiframeImageWatermarkOptions
```

## Κατασκευαστές

| Ονομα | Περιγραφή |
| --- | --- |
| [GifImageWatermarkOptions](gifimagewatermarkoptions#constructor)() | Αρχικοποιεί μια νέα παρουσία του[`GifImageWatermarkOptions`](../gifimagewatermarkoptions) τάξη. |
| [GifImageWatermarkOptions](gifimagewatermarkoptions#constructor_1)(int) | Αρχικοποιεί μια νέα παρουσία του[`GifImageWatermarkOptions`](../gifimagewatermarkoptions) κλάση με καθορισμένο ευρετήριο ενός πλαισίου. |

## Ιδιότητες

| Ονομα | Περιγραφή |
| --- | --- |
| [FrameIndex](../../groupdocs.watermark.options.image/multiframeimagewatermarkoptions/frameindex) { get; set; } | Λαμβάνει ή ορίζει το ευρετήριο του πλαισίου για να προσθέσει υδατογράφημα. |

### Παρατηρήσεις

**Μάθε περισσότερα:**

* [Προσθέστε υδατογραφήματα σε εικόνες](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+images)

### Παραδείγματα

Προσθέστε ένα υδατογράφημα σε ένα συγκεκριμένο πλαίσιο εικόνας GIF.

```csharp
GifImageLoadOptions loadOptions = new GifImageLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\test.gif", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test", new Font("Arial", 12));

    GifImageWatermarkOptions options = new GifImageWatermarkOptions();
    options.FrameIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Δείτε επίσης

* class [MultiframeImageWatermarkOptions](../multiframeimagewatermarkoptions)
* χώρος ονομάτων [GroupDocs.Watermark.Options.Image](../../groupdocs.watermark.options.image)
* συνέλευση [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
