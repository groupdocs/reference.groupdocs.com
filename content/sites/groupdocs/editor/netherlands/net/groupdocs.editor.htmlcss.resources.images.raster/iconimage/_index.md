---
title: IconImage
second_title: GroupDocs.Editor voor .NET API-referentie
description: Vertegenwoordigt één afbeelding in ICONformaat met zijn metadata en aanvullende methoden
type: docs
weight: 520
url: /nl/net/groupdocs.editor.htmlcss.resources.images.raster/iconimage/
---
## IconImage class

Vertegenwoordigt één afbeelding in ICON-formaat met zijn metadata en aanvullende methoden

```csharp
public sealed class IconImage : RasterImageResourceBase
```

## Constructeurs

| Naam | Beschrijving |
| --- | --- |
| [IconImage](iconimage#constructor)(string, Stream) | Maakt een nieuwe IconImage-instantie van inhoud, weergegeven als bytestream, en met opgegeven naam |
| [IconImage](iconimage#constructor_1)(string, string) | Maakt nieuwe IconImage-instantie van inhoud, weergegeven als base64-gecodeerde tekenreeks, en met opgegeven naam |

## Eigenschappen

| Naam | Beschrijving |
| --- | --- |
| [AspectRatio](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/aspectratio) { get; } | Retourneert een beeldverhouding van deze afbeelding als de breedte-tot-hoogte-relatie |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/bytecontent) { get; } | Retourneert de inhoud van deze rasterafbeelding als bytestream |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/filenamewithextension) { get; } | Retourneert de juiste bestandsnaam van deze rasterafbeelding, die bestaat uit naam en extensie. Theoretisch kan afwijken van de naam. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/isdisposed) { get; } | Bepaalt of deze rasterafbeelding wordt weggegooid of niet |
| [Length](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/length) { get; } | Geeft de lengte van dit rasterafbeeldingsbestand terug in bytes |
| [LinearDimensions](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/lineardimensions) { get; } | Retourneert lineaire afmetingen van deze rasterafbeelding (breedte en hoogte) |
| [Name](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/name) { get; } | Geeft de naam van deze rasterafbeelding terug. Bevat meestal geen bestandsnaamextensie en kan theoretisch verschillen van bestandsnaam. |
| [NumberOfImages](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/numberofimages) { get; } | Retourneert het aantal afbeeldingen dat aanwezig is in dit ICON-bestand |
| [TextContent](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/textcontent) { get; } | Retourneert inhoud van deze rasterafbeelding als base64-gecodeerde string |
| override [Type](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/type) { get; } | Retourneert ImageType.Icon |

## methoden

| Naam | Beschrijving |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/dispose)() | Verwijdert deze rasterafbeelding, verwijdert de inhoud en maakt de meeste methoden en eigenschappen niet-werkend |
| [Equals](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/equals)(IHtmlResource) | Controleert deze instantie met gespecificeerde referentiegelijkheid. |
| [GenerateBitmap](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/generatebitmap)() | Genereert en retourneert een nieuwe instantie van de 'System.Drawing.Bitmap' van deze rasterafbeelding. |
| [ReduceToNewHeight](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/reducetonewheight#reducetonewheight)(ushort) | Creëert en retourneert een nieuwe verkleinde pictogramafbeelding, maar met een gespecificeerde nieuwe verkleinde hoogte en proportioneel verkleinde breedte. (2 methods) |
| [Save](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/save)(string) | Slaat deze rasterafbeelding op in het opgegeven bestand |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/isvalid#isvalid)(Stream) | Controleert of opgegeven stream een geldige ICON-afbeelding is |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.images.raster/iconimage/isvalid#isvalid_1)(string) | Controleert of opgegeven base64-gecodeerde tekenreeks een geldige ICON-afbeelding is |

## Evenementen

| Naam | Beschrijving |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.images.raster/rasterimageresourcebase/disposed) | Gebeurtenis die optreedt wanneer deze rasterafbeelding wordt weggegooid |

### Zie ook

* class [RasterImageResourceBase](../rasterimageresourcebase)
* naamruimte [GroupDocs.Editor.HtmlCss.Resources.Images.Raster](../../groupdocs.editor.htmlcss.resources.images.raster)
* montage [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->
