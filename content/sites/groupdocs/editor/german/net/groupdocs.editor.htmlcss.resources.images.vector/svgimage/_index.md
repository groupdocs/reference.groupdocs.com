---
title: SvgImage
second_title: GroupDocs.Editor für .NET-API-Referenz
description: Repräsentiert ein Vektorbild im SVGFormat Scalable Vector Graphics mit seinen Metadaten und zusätzlichen Methoden
type: docs
weight: 590
url: /de/net/groupdocs.editor.htmlcss.resources.images.vector/svgimage/
---
## SvgImage class

Repräsentiert ein Vektorbild im SVG-Format (Scalable Vector Graphics) mit seinen Metadaten und zusätzlichen Methoden

```csharp
public sealed class SvgImage : VectorImageResourceBase
```

## Konstrukteure

| Name | Beschreibung |
| --- | --- |
| [SvgImage](svgimage#constructor)(string, Stream) | Erstellt eine neue SvgImage-Instanz aus Inhalt, dargestellt als Byte-Stream, und mit dem angegebenen Namen |
| [SvgImage](svgimage#constructor_1)(string, string) | Erstellt eine neue SvgImage-Instanz aus Inhalt, dargestellt als übliche Zeichenfolge und mit dem angegebenen Namen |

## Eigenschaften

| Name | Beschreibung |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/aspectratio) { get; } | Gibt das Seitenverhältnis dieses Vektors zurück image |
| override [ByteContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/bytecontent) { get; } | Gibt einen Inhalt dieses SVG-Bildes als binären Stream zurück |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/filenamewithextension) { get; } | Gibt den korrekten Dateinamen dieses Vektorbildes zurück, der aus Name und Erweiterung besteht. Kann theoretisch vom Namen abweichen. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/isdisposed) { get; } | Bestimmt, ob dieses Rasterbild verworfen wird (`WAHR`) oder nicht (`FALSCH` ) |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/lineardimensions) { get; } | Gibt lineare Abmessungen dieses Vektorbildes zurück (Breite und Höhe) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/name) { get; } | Gibt den Namen dieses Vektorbildes zurück. Enthält normalerweise keine Dateinamenerweiterung und kann theoretisch von Dateiname abweichen. |
| override [TextContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/textcontent) { get; } | Gibt einen Inhalt dieses SVG-Bildes als base64-codierten binären Inhalt zurück (nicht als Rohtext im XML-Format) |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/type) { get; } | Gibt ImageType.Svg zurück |
| [XmlContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/xmlcontent) { get; } | Gibt einen Inhalt dieses SVG-Bildes in seiner ursprünglichen XML-konformen Textform zurück |

## Methoden

| Name | Beschreibung |
| --- | --- |
| override [Dispose](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/dispose)() | Löscht dieses Rasterbild, löscht seinen Inhalt und macht die meisten Methoden und Eigenschaften nicht funktionsfähig |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/equals)(IHtmlResource) | Prüft diese Instanz mit Angabe auf Referenzgleichheit. |
| override [Save](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/save)(string) | Speichert dieses SVG-Bild in der Datei |
| override [SaveToPng](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/savetopng)(Stream) | Speichert dieses Vektor-SVG-Bild als Raster-PNG-Bild |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/isvalid)(string) | Führt eine Oberflächenprüfung durch, ob angegebener textueller XML-konformer Inhalt ein SVG-Bild darstellt |

## Veranstaltungen

| Name | Beschreibung |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/disposed) | Ereignis, das eintritt, wenn dieses Rasterbild entsorgt wird |

### Siehe auch

* class [VectorImageResourceBase](../vectorimageresourcebase)
* namensraum [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../groupdocs.editor.htmlcss.resources.images.vector)
* Montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
