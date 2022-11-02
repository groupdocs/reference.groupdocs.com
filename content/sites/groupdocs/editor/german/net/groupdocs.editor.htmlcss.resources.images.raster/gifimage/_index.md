---
title: GifImage
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Stellt ein Bild im GIFFormat Graphics Interchange Format mit seinen Metadaten und zusätzlichen Methoden dar
type: docs
weight: 410
url: /de/net/groupdocs.editor.htmlcss.resources.images.raster/gifimage/
---
## GifImage class

Stellt ein Bild im GIF-Format (Graphics Interchange Format) mit seinen Metadaten und zusätzlichen Methoden dar

```csharp
public sealed class GifImage : RasterImageResourceBase
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [GifImage](gifimage#constructor)(string, Stream) | Erstellt eine neue GifImage-Instanz aus Inhalt, dargestellt als Byte-Stream, und mit dem angegebenen Namen |
| [GifImage](gifimage#constructor_1)(string, string) | Erstellt eine neue GifImage-Instanz aus Inhalt, dargestellt als base64-codierte Zeichenfolge und mit dem angegebenen Namen |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/aspectratio) { get; } | Gibt ein Seitenverhältnis dieses Bildes als Verhältnis von Breite zu Höhe zurück |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/bytecontent) { get; } | Gibt den Inhalt dieses Rasterbildes als Bytestream zurück |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/filenamewithextension) { get; } | Gibt den korrekten Dateinamen dieses Rasterbildes zurück, der sich aus Name und Erweiterung zusammensetzt. Kann theoretisch vom Namen abweichen. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/isdisposed) { get; } | Bestimmt, ob dieses Rasterbild verworfen wird oder nicht |
| [Length](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/length) { get; } | Gibt die Länge dieser Rasterbilddatei in Bytes zurück |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/lineardimensions) { get; } | Gibt lineare Abmessungen dieses Rasterbildes zurück (Breite und Höhe) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/name) { get; } | Gibt den Namen dieses Rasterbildes zurück. Enthält normalerweise keine Dateinamenerweiterung und kann theoretisch von Dateiname abweichen. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/textcontent) { get; } | Gibt den Inhalt dieses Rasterbildes als base64-kodierten String zurück |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.raster/gifimage/type) { get; } | Gibt ImageType.Gif zurück |
| [Version](../../groupdocs.editor.htmlcss.resources.images.raster/gifimage/version) { get; } | Gibt die interne Version dieses GIF-Bildes zurück (Version wird aus Header extrahiert) |

## Methoden

| Name | Beschreibung |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/dispose)() | Löscht dieses Rasterbild, löscht seinen Inhalt und macht die meisten Methoden und Eigenschaften nicht funktionsfähig |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/equals)(IHtmlResource) | Prüft diese Instanz mit Angabe auf Referenzgleichheit. |
| [GenerateBitmap](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/generatebitmap)() | Erzeugt und gibt eine neue Instanz der 'System.Drawing.Bitmap' aus diesem Rasterbild zurück. |
| [ReduceToNewHeight](../../groupdocs.editor.htmlcss.resources.images.raster/gifimage/reducetonewheight#reducetonewheight)(ushort) | Erstellt ein neues reduziertes GIF-Bild und gibt es zurück, jedoch mit der angegebenen neuen reduzierten Höhe und proportional reduzierter Breite. (2 methods) |
| [Save](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/save)(string) | Speichert dieses Rasterbild in der angegebenen Datei |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/gifimage/isvalid#isvalid)(Stream) | Überprüft, ob der angegebene Stream ein gültiges GIF-Bild ist |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/gifimage/isvalid#isvalid_1)(string) | Überprüft, ob die angegebene base64-codierte Zeichenfolge ein gültiges GIF-Bild ist |

## Veranstaltungen

| Name | Beschreibung |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/disposed) | Ereignis, das eintritt, wenn dieses Rasterbild entsorgt wird |

### Siehe auch

* class [RasterImageResourceBase](../rasterimageresourcebase)
* namensraum [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../groupdocs.editor.htmlcss.resources.images.raster)
* Montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->