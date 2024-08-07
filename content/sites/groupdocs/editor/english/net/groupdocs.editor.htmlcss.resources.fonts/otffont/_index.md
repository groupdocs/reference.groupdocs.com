---
title: OtfFont
second_title: GroupDocs.Editor for .NET API Reference
description: Represents one font in the OTF Open Type Format format
type: docs
weight: 370
url: /net/groupdocs.editor.htmlcss.resources.fonts/otffont/
---
## OtfFont class

Represents one font in the OTF (Open Type Format) format

```csharp
public sealed class OtfFont : FontResourceBase
```

## Constructors

| Name | Description |
| --- | --- |
| [OtfFont](otffont#constructor)(string, Stream) | Creates new OtfFont class from content, represented as byte stream, and with specified name |
| [OtfFont](otffont#constructor_1)(string, string) | Creates new OtfFont class from content, represented as base64-encoded string, and with specified name |

## Properties

| Name | Description |
| --- | --- |
| [ByteContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/bytecontent) { get; } | Returns content of this font as byte stream |
| [FilenameWithExtension](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/filenamewithextension) { get; } | Returns correct filename of this font resource, which consists of name and extension. Theoretically can differ from the name. |
| [IsDisposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/isdisposed) { get; } | Determines whether this font is disposed or not |
| [Name](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/name) { get; } | Returns name of this font resource. Usually doesn't contain filename extension and theoretically can differ from filename. |
| [TextContent](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/textcontent) { get; } | Returns content of this font as base64-encoded string. This value is cached after first invoke. |
| override [Type](../../groupdocs.editor.htmlcss.resources.fonts/otffont/type) { get; } | Returns [`Otf`](../fonttype/otf) |

## Methods

| Name | Description |
| --- | --- |
| [Dispose](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/dispose)() | Disposes this font resource, disposing its content and making most methods and properties non-working |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals)(FontResourceBase) | Checks this instance with specified font resource on reference equality |
| [Equals](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/equals)(IHtmlResource) | Checks this instance with specified HTML resource on reference equality |
| [Save](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/save)(string) | Saves this font to the specified file |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.fonts/otffont/isvalid#isvalid)(Stream) | Checks whether specified stream is a valid OTF font |
| static [IsValid](../../groupdocs.editor.htmlcss.resources.fonts/otffont/isvalid#isvalid_1)(string) | Checks whether specified base64-encoded string is a valid OTF font |

## Fields

| Name | Description |
| --- | --- |
| const [RequiredHeaderSize](../../groupdocs.editor.htmlcss.resources.fonts/otffont/requiredheadersize) | OTF header size (in bytes), which is required for its validation |

## Events

| Name | Description |
| --- | --- |
| event [Disposed](../../groupdocs.editor.htmlcss.resources.fonts/fontresourcebase/disposed) | Event, which occurs when this font is disposed |

### See Also

* class [FontResourceBase](../fontresourcebase)
* namespace [GroupDocs.Editor.HtmlCss.Resources.Fonts](../../groupdocs.editor.htmlcss.resources.fonts)
* assembly [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.editor.dll -->
