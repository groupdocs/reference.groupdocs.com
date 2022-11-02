---
title: PresentationWatermarkSlideOptions
second_title: GroupDocs.Watermark für .NET-API-Referenz
description: Repräsentiert Optionen beim Hinzufügen von Wasserzeichen zu einer Folie eines Präsentationsdokuments.
type: docs
weight: 2060
url: /de/net/groupdocs.watermark.options.presentation/presentationwatermarkslideoptions/
---
## PresentationWatermarkSlideOptions class

Repräsentiert Optionen beim Hinzufügen von Wasserzeichen zu einer Folie eines Präsentationsdokuments.

```csharp
public sealed class PresentationWatermarkSlideOptions : PresentationWatermarkBaseSlideOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [PresentationWatermarkSlideOptions](presentationwatermarkslideoptions)() | Initialisiert eine neue Instanz von[`PresentationWatermarkSlideOptions`](../presentationwatermarkslideoptions) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AlternativeText](../../groupdocs.watermark.options.presentation/presentationwatermarkbaseslideoptions/alternativetext) { get; set; } | Ruft den beschreibenden (alternativen) Text ab oder legt ihn fest, der einer Form zugeordnet wird. |
| [Effects](../../groupdocs.watermark.options.presentation/presentationwatermarkbaseslideoptions/effects) { get; set; } | Erhält oder setzt einen Wert von[`PresentationImageEffects`](../presentationimageeffects) oder [`PresentationTextEffects`](../presentationtexteffects) für Effekte, die auf das Wasserzeichen angewendet werden sollen. |
| [IsLocked](../../groupdocs.watermark.options.presentation/presentationwatermarkbaseslideoptions/islocked) { get; set; } | Ruft oder setzt einen Wert, der angibt, ob eine Bearbeitung der Form in PowerPoint verboten ist. |
| [Name](../../groupdocs.watermark.options.presentation/presentationwatermarkbaseslideoptions/name) { get; set; } | Ruft den Namen einer Form ab oder legt ihn fest. |
| [ProtectWithUnreadableCharacters](../../groupdocs.watermark.options.presentation/presentationwatermarkbaseslideoptions/protectwithunreadablecharacters) { get; set; } | Ruft einen Wert ab oder legt einen Wert fest, der angibt, ob die Zeichen des Textwasserzeichens mit nicht lesbaren Zeichen gemischt sind. |
| [SlideIndex](../../groupdocs.watermark.options.presentation/presentationwatermarkslideoptions/slideindex) { get; set; } | Ruft den Index der Folie ab oder legt ihn fest, zu der das Wasserzeichen hinzugefügt werden soll. |

### Bemerkungen

**Mehr erfahren:**

* [Fügen Sie Präsentationsdokumenten Wasserzeichen hinzu](https://docs.groupdocs.com/display/watermarknet/Add+watermarks+to+presentation+documents)

### Beispiele

Wasserzeichen zu einer bestimmten Folie einer PowerPoint-Präsentation hinzufügen.

```csharp
PresentationLoadOptions loadOptions = new PresentationLoadOptions();
using (Watermarker watermarker = new Watermarker(@"C:\Documents\test.ppt", loadOptions))
{
    TextWatermark watermark = new TextWatermark("Test watermark", new Font("Arial", 36, FontStyle.Bold | FontStyle.Italic));
    watermark.HorizontalAlignment = HorizontalAlignment.Center;
    watermark.VerticalAlignment = VerticalAlignment.Center;

    PresentationWatermarkSlideOptions options = new PresentationWatermarkSlideOptions();
    options.SlideIndex = 0;
    options.IsLocked = false; // Ursprünglich
    options.ProtectWithUnreadableCharacters = false; // Ursprünglich
    options.Name = null; // Ursprünglich
    options.AlternativeText = null; // Ursprünglich

    watermarker.Add(watermark, options);
    watermarker.Save();
}
```

### Siehe auch

* class [PresentationWatermarkBaseSlideOptions](../presentationwatermarkbaseslideoptions)
* namensraum [GroupDocs.Watermark.Options.Presentation](../../groupdocs.watermark.options.presentation)
* Montage [GroupDocs.Watermark](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Watermark.dll -->