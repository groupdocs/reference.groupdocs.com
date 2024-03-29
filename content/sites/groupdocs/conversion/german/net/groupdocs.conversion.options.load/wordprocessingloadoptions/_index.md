---
title: WordProcessingLoadOptions
second_title: GroupDocs.Conversion für .NET-API-Referenz
description: Optionen zum Laden von WordProcessingDokumenten.
type: docs
weight: 2360
url: /de/net/groupdocs.conversion.options.load/wordprocessingloadoptions/
---
## WordProcessingLoadOptions class

Optionen zum Laden von WordProcessing-Dokumenten.

```csharp
public class WordProcessingLoadOptions : LoadOptions
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [WordProcessingLoadOptions](wordprocessingloadoptions)() | Initialisiert eine neue Instanz von[`WordProcessingLoadOptions`](../wordprocessingloadoptions) Klasse. |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AutoFontSubstitution](../../groupdocs.conversion.options.load/wordprocessingloadoptions/autofontsubstitution) { get; set; } | Wenn AutoFontSubstitution deaktiviert ist, verwendet GroupDocs.Conversion den DefaultFont zum Ersetzen fehlender Schriftarten. Wenn AutoFontSubstitution aktiviert ist, wertet GroupDocs.Conversion alle verwandten Felder in FontInfo (Panose, Sig usw.) auf die fehlende Schriftart aus und findet die beste Übereinstimmung unter den verfügbaren Schriftartquellen. Beachten Sie, dass der Schriftartersetzungsmechanismus die DefaultFont in Fällen überschreibt, in denen FontInfo für die fehlende Schriftart ist im Dokument verfügbar. Der Standardwert ist True. |
| [BookmarkOptions](../../groupdocs.conversion.options.load/wordprocessingloadoptions/bookmarkoptions) { get; set; } | Lesezeichen-Optionen |
| [DefaultFont](../../groupdocs.conversion.options.load/wordprocessingloadoptions/defaultfont) { get; set; } | Standardschriftart für Words-Dokument. Die folgende Schriftart wird verwendet, wenn eine Schriftart fehlt. |
| [EmbedTrueTypeFonts](../../groupdocs.conversion.options.load/wordprocessingloadoptions/embedtruetypefonts) { get; set; } | Wenn EmbedTrueTypeFonts wahr ist, bettet GroupDocs.Conversion TrueType-Schriftarten in das Ausgabedokument ein. Standard: false |
| [FontSubstitutes](../../groupdocs.conversion.options.load/wordprocessingloadoptions/fontsubstitutes) { get; set; } | Bestimmte Schriftarten beim Konvertieren von Word-Dokumenten ersetzen. |
| [Format](../../groupdocs.conversion.options.load/wordprocessingloadoptions/format) { get; set; } | Dateityp des Eingabedokuments. |
| [Format](../../groupdocs.conversion.options.load/loadoptions/format) { get; } | Dateityp des Eingabedokuments. |
| [HideComments](../../groupdocs.conversion.options.load/wordprocessingloadoptions/hidecomments) { get; set; } | Kommentare ausblenden. |
| [HideWordTrackedChanges](../../groupdocs.conversion.options.load/wordprocessingloadoptions/hidewordtrackedchanges) { get; set; } | Markup ausblenden und Änderungen für Word-Dokumente nachverfolgen. |
| [KeepDateFieldOriginalValue](../../groupdocs.conversion.options.load/wordprocessingloadoptions/keepdatefieldoriginalvalue) { get; set; } | Originalwert des Datumsfeldes beibehalten. Standard: false |
| [Password](../../groupdocs.conversion.options.load/wordprocessingloadoptions/password) { get; set; } | Kennwort festlegen, um den Schutz des geschützten Dokuments aufzuheben. |
| [PreserveFormFields](../../groupdocs.conversion.options.load/wordprocessingloadoptions/preserveformfields) { get; set; } | Gibt an, ob Microsoft Word-Formularfelder als Formularfelder in PDF beibehalten oder in Text konvertiert werden sollen. Standard ist false. |
| [UpdateFields](../../groupdocs.conversion.options.load/wordprocessingloadoptions/updatefields) { get; set; } | Felder nach dem Laden aktualisieren. Standard: false |
| [UpdatePageLayout](../../groupdocs.conversion.options.load/wordprocessingloadoptions/updatepagelayout) { get; set; } | Seitenlayout nach dem Laden aktualisieren. Standard: false |
| [UseTextShaper](../../groupdocs.conversion.options.load/wordprocessingloadoptions/usetextshaper) { get; set; } | Gibt an, ob ein Textformer für eine bessere Kerning-Anzeige verwendet werden soll. Standard ist false. |

## Methoden

| Name | Beschreibung |
| --- | --- |
| override [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(object) | Bestimmt, ob zwei Objektinstanzen gleich sind. |
| virtual [Equals](../../groupdocs.conversion.contracts/valueobject/equals)(ValueObject) | Bestimmt, ob zwei Objektinstanzen gleich sind. |
| override [GetHashCode](../../groupdocs.conversion.contracts/valueobject/gethashcode)() | Dient als Standard-Hash-Funktion. |

### Siehe auch

* class [LoadOptions](../loadoptions)
* namensraum [GroupDocs.Conversion.Options.Load](../../groupdocs.conversion.options.load)
* Montage [GroupDocs.Conversion](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Conversion.dll -->
