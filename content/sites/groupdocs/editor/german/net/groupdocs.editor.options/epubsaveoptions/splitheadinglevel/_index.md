---
title: SplitHeadingLevel
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Gibt die maximale Überschriftenebene an bei der die ePubDatei geteilt werden soll. Standardwert ist2 Einstellung auf0 wird die Aufteilung deaktivieren sodass der gesamte Inhalt des EBooks in ein einzelnes Paket innerhalb des ePub integriert wird.
type: docs
weight: 30
url: /de/net/groupdocs.editor.options/epubsaveoptions/splitheadinglevel/
---
## EpubSaveOptions.SplitHeadingLevel property

Gibt die maximale Überschriftenebene an, bei der die ePub-Datei geteilt werden soll. Standardwert ist`2` Einstellung auf`0` wird die Aufteilung deaktivieren, sodass der gesamte Inhalt des E-Books in ein einzelnes Paket innerhalb des ePub integriert wird.

```csharp
public int SplitHeadingLevel { get; set; }
```

### Bemerkungen

Wenn diese Eigenschaft auf einen Wert zwischen 1 und 9 gesetzt ist, wird das Dokument an Absätzen geteilt, die mit formatiert sind.**Überschrift 1** ,**Überschrift 2** ,**Überschrift 3** usw. Stile bis zur angegebenen Überschriftenebene.

Nur standardmäßig**Überschrift 1** und**Überschrift 2** Absätze führen dazu, dass das Dokument geteilt wird. Wenn Sie diese Eigenschaft auf Null setzen, wird das Dokument überhaupt nicht an Überschriftenabsätzen geteilt.

### Siehe auch

* class [EpubSaveOptions](../../epubsaveoptions)
* namensraum [GroupDocs.Editor.Options](../../epubsaveoptions)
* Montage [GroupDocs.Editor](../../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->