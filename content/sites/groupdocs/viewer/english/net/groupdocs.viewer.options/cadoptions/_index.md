---
title: CadOptions
second_title: GroupDocs.Viewer for .NET API Reference
description: Contains options for rendering CAD drawings. For more information and code examples see the Render CAD drawings and models as HTML PDF and image fileshttps//docs.groupdocs.com/viewer/net/rendercaddrawingsandmodels/ and Specify rendering options for CAD fileshttps//docs.groupdocs.com/viewer/net/specifycadrenderingoptions/.
type: docs
weight: 430
url: /net/groupdocs.viewer.options/cadoptions/
---
## CadOptions class

Contains options for rendering CAD drawings. For more information and code examples, see the [Render CAD drawings and models as HTML, PDF, and image files](https://docs.groupdocs.com/viewer/net/render-cad-drawings-and-models/) and [Specify rendering options for CAD files](https://docs.groupdocs.com/viewer/net/specify-cad-rendering-options/).

```csharp
public class CadOptions
```

## Properties

| Name | Description |
| --- | --- |
| [BackgroundColor](../../groupdocs.viewer.options/cadoptions/backgroundcolor) { get; set; } | Image background color. |
| [EnablePerformanceConversionMode](../../groupdocs.viewer.options/cadoptions/enableperformanceconversionmode) { get; set; } | Setting this flag to `true` enables a special performance-oriented conversion mode for all formats within CAD family — in this mode the conversion speed is much faster, but the quality of the resultant documents is signifiantly worser. By default is disabled (`false`) — the quality of the resultant documents is the best possible at the expense of performance. |
| [Height](../../groupdocs.viewer.options/cadoptions/height) { get; } | The height of the output result (in pixels). |
| [Layers](../../groupdocs.viewer.options/cadoptions/layers) { get; set; } | The CAD drawing layers to render. |
| [LayoutName](../../groupdocs.viewer.options/cadoptions/layoutname) { get; set; } | The name of the specific layout to render. Layout name is case-sensitive. |
| [Pc3File](../../groupdocs.viewer.options/cadoptions/pc3file) { get; set; } | PC3 - plotter configuration file |
| [RenderLayouts](../../groupdocs.viewer.options/cadoptions/renderlayouts) { get; set; } | Flag if layouts from CAD document should be rendered. |
| [ScaleFactor](../../groupdocs.viewer.options/cadoptions/scalefactor) { get; } | Value higher than 1 enlarges output result; value between 0 and 1 reduces output result. |
| [Tiles](../../groupdocs.viewer.options/cadoptions/tiles) { get; set; } | The drawing regions to render. |
| [Width](../../groupdocs.viewer.options/cadoptions/width) { get; } | The width of the output result (in pixels). |

## Methods

| Name | Description |
| --- | --- |
| static [ForRenderingByHeight](../../groupdocs.viewer.options/cadoptions/forrenderingbyheight)(int) | Initializes an instance of the [`CadOptions`](../cadoptions) class for rendering by height. |
| static [ForRenderingByScaleFactor](../../groupdocs.viewer.options/cadoptions/forrenderingbyscalefactor)(float) | Initializes an instance of the [`CadOptions`](../cadoptions) class for rendering by scale factor. |
| static [ForRenderingByWidth](../../groupdocs.viewer.options/cadoptions/forrenderingbywidth)(int) | Initializes an instance of the [`CadOptions`](../cadoptions) class for rendering by width. |
| static [ForRenderingByWidthAndHeight](../../groupdocs.viewer.options/cadoptions/forrenderingbywidthandheight)(int, int) | Initializes an instance of the [`CadOptions`](../cadoptions) class for rendering by width and height. |

### See Also

* namespace [GroupDocs.Viewer.Options](../../groupdocs.viewer.options)
* assembly [GroupDocs.Viewer](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.viewer.dll -->
