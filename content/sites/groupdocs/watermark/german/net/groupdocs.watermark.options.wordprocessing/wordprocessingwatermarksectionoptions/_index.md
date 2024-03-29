---
title: WordProcessingWatermarkSectionOptions
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Repräsentiert Optionen beim Hinzufügen von Formwasserzeichen zu einem WordDokumentabschnitt.
type: docs
weight: 2380
url: /de/net/groupdocs.watermark.options.wordprocessing/wordprocessingwatermarksectionoptions/
---
## WordProcessingWatermarkSectionOptions class

Repräsentiert Optionen beim Hinzufügen von Formwasserzeichen zu einem Word-Dokumentabschnitt.

```csharp
public sealed class WordProcessingWatermarkSectionOptions : WordProcessingWatermarkBaseOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [WordProcessingWatermarkSectionOptions](wordprocessingwatermarksectionoptions)() | Initialisiert eine neue Instanz von[`WordProcessingWatermarkSectionOptions`](../wordprocessingwatermarksectionoptions) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AlternativeText](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/alternativetext) { get; set; } | Ruft den beschreibenden (alternativen) Text ab oder legt ihn fest, der einer Form zugeordnet wird. |
| [Effects](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/effects) { get; set; } | Erhält oder setzt einen Wert von[`WordProcessingImageEffects`](../wordprocessingimageeffects) oder [`WordProcessingTextEffects`](../wordprocessingtexteffects) für Effekte, die auf das Wasserzeichen angewendet werden sollen. |
| [IsLocked](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/islocked) { get; set; } | Ruft oder setzt einen Wert, der angibt, ob eine Bearbeitung der Form in Word verboten ist. |
| [LockType](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/locktype) { get; set; } | Ruft den Typ der Wasserzeichensperre ab oder legt ihn fest. |
| [Name](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/name) { get; set; } | Ruft den Namen einer Form ab oder legt ihn fest. |
| [Password](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarkbaseoptions/password) { get; set; } | Ruft ein Passwort ab oder legt es fest, das zum Sperren des Wasserzeichens verwendet wird. |
| [SectionIndex](../../groupdocs.watermark.options.wordprocessing/wordprocessingwatermarksectionoptions/sectionindex) { get; set; } | Ruft den Index eines Abschnitts ab oder legt ihn fest, dem das Wasserzeichen hinzugefügt werden soll. |

### Bemerkungen

**Erfahren Sie mehr:**

* [Fügen Sie Textverarbeitungsdokumenten Wasserzeichen hinzu](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+word+processing+documents)

### Beispiele

Wasserzeichen zu einem bestimmten Abschnitt eines Word-Dokuments hinzufügen.

```csharp
WordProcessingLoadOptions loadOptions = new WordProcessingLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\Documents\test.doc", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test watermark", new Font("Arial", 36, FontStyle.Bold | FontStyle.Italic));
    watermark.HorizontalAlignment = HorizontalAlignment.Center;
    watermark.VerticalAlignment = VerticalAlignment.Center;
    watermark.ForegroundColor = Color.Red;

    WordProcessingWatermarkSectionOptions options = new WordProcessingWatermarkSectionOptions();
    options.SectionIndex = 0;

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Siehe auch

* class [WordProcessingWatermarkBaseOptions](../wordprocessingwatermarkbaseoptions)
* namensraum [GroupDocs.Watermark.Options.WordProcessing](../../groupdocs.watermark.options.wordprocessing)
* Montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->
