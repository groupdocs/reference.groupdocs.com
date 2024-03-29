---
title: SvgImage
second_title: GroupDocs.Editor voor .NET API-referentie
description: Vertegenwoordigt één vectorafbeelding in SVGindeling Scalable Vector Graphics met zijn metagegevens en aanvullende methoden
type: docs
weight: 590
url: /nl/net/groupdocs.editor.htmlcss.resources.images.vector/svgimage/
---
## SvgImage class

Vertegenwoordigt één vectorafbeelding in SVG-indeling (Scalable Vector Graphics) met zijn metagegevens en aanvullende methoden

```csharp
public sealed class SvgImage : VectorImageResourceBase
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [SvgImage](svgimage#constructor)(string, Stream) | Maakt nieuwe SvgImage-instantie van inhoud, weergegeven als bytestroom, en met opgegeven naam |
| [SvgImage](svgimage#constructor_1)(string, string) | Maakt een nieuwe SvgImage-instantie van inhoud, weergegeven als gebruikelijke tekenreeks, en met opgegeven naam |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/aspectratio) { get; } | Retourneert beeldverhouding van deze vectorafbeelding |
| override [ByteContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/bytecontent) { get; } | Retourneert een inhoud van deze SVG-afbeelding als een binaire stream |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/filenamewithextension) { get; } | Retourneert de juiste bestandsnaam van deze vectorafbeelding, die bestaat uit naam en extensie. Theoretisch kan afwijken van de naam. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/isdisposed) { get; } | Bepaalt of deze rasterafbeelding wordt weggegooid (`WAAR`) of niet (`vals` ) |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/lineardimensions) { get; } | Retourneert lineaire afmetingen van deze vectorafbeelding (breedte en hoogte) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/name) { get; } | Geeft de naam van deze vectorafbeelding terug. Bevat meestal geen bestandsnaamextensie en kan theoretisch verschillen van bestandsnaam. |
| override [TextContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/textcontent) { get; } | Retourneert een inhoud van deze SVG-afbeelding als een base64-gecodeerde binaire inhoud (niet als onbewerkte tekst in XML-indeling) |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/type) { get; } | Retourneert ImageType.Svg |
| [XmlContent](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/xmlcontent) { get; } | Retourneert een inhoud van deze SVG-afbeelding in de originele XML-compatibele tekstuele vorm |

## methoden

| Naam | Beschrijving |
| --- | --- |
| override [Dispose](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/dispose)() | Verwijdert deze rasterafbeelding, verwijdert de inhoud en maakt de meeste methoden en eigenschappen niet-werkend |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/equals)(IHtmlResource) | Controleert deze instantie met gespecificeerde referentiegelijkheid. |
| override [Save](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/save)(string) | Slaat deze SVG-afbeelding op in het bestand |
| override [SaveToPng](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/savetopng)(Stream) | Slaat deze vector SVG-afbeelding op in raster PNG-afbeelding |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.vector/svgimage/isvalid)(string) | Voert een oppervlakkige controle uit of gespecificeerde tekstuele XML-compatibele inhoud een SVG-afbeelding vertegenwoordigt |

## Evenementen

| Naam | Beschrijving |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.vector/vectorimageresourcebase/disposed) | Gebeurtenis die optreedt wanneer deze rasterafbeelding wordt weggegooid |

### Zie ook

* class [VectorImageResourceBase](../vectorimageresourcebase)
* naamruimte [GroupDocs.Editor.HtmlCss.Resources.Images.Vector](../../groupdocs.editor.htmlcss.resources.images.vector)
* montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
