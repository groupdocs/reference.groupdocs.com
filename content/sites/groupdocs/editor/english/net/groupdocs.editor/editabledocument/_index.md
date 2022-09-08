---
title: EditableDocument
second_title: GroupDocs.Editor for .NET API Reference
description: Intermediate document that contains content before and after editing
type: docs
weight: 10
url: /net/groupdocs.editor/editabledocument/
---
## EditableDocument class

Intermediate document, that contains content before and after editing

```csharp
public sealed class EditableDocument : IAuxDisposable
```

## Properties

| Name | Description |
| --- | --- |
| [AllResources](../../groupdocs.editor/editabledocument/allresources) { get; } | Returns a list of all existing resources: all stylesheets, images from HTML and all stylesheets, fonts |
| [Audio](../../groupdocs.editor/editabledocument/audio) { get; } | Returns a list of audio resources |
| [Css](../../groupdocs.editor/editabledocument/css) { get; } | Returns a list of CSS resources |
| [Fonts](../../groupdocs.editor/editabledocument/fonts) { get; } | Allows to obtain external font resources, which are used by this HTML document |
| [Images](../../groupdocs.editor/editabledocument/images) { get; } | Allows to obtain external image resources (raster images), which are used by this HTML document |
| [IsDisposed](../../groupdocs.editor/editabledocument/isdisposed) { get; } | Determines whether this Editable document was already disposed (true) or not (false) |

## Methods

| Name | Description |
| --- | --- |
| static [FromFile](../../groupdocs.editor/editabledocument/fromfile)(string, string) | Static factory, that creates an instance of EditableDocument from a HTML file, that is specified by a path to the *.html file itself and a folder with linked resources |
| static [FromMarkup](../../groupdocs.editor/editabledocument/frommarkup)(string, IEnumerable&lt;IHtmlResource&gt;) | Static factory, that creates an instance of EditableDocument from specified HTML markup and a set of corresponding linked resources |
| static [FromMarkupAndResourceFolder](../../groupdocs.editor/editabledocument/frommarkupandresourcefolder)(string, string) | Static factory, that creates an instance of EditableDocument from a specified HTML markup and from resources, located in the folder, specified by the full path |
| [Dispose](../../groupdocs.editor/editabledocument/dispose)() | Disposes this Editable document instance, disposing its content and making its methods and properties non-working |
| [GetBodyContent](../../groupdocs.editor/editabledocument/getbodycontent#getbodycontent)() | Returns a body of the HTML document (content between opening and closing BODY tags without these tags) as a string. |
| [GetBodyContent](../../groupdocs.editor/editabledocument/getbodycontent#getbodycontent_1)(string) | Returns a body of the HTML document (content between opening and closing BODY tags without these tags) as a string, where links to the external resources contain specified prefix. |
| [GetContent](../../groupdocs.editor/editabledocument/getcontent#getcontent)() | Returns overall content of the HTML document as a string. |
| [GetContent](../../groupdocs.editor/editabledocument/getcontent#getcontent_1)(string, string) | Returns overall content of the HTML document as a string, where links to the external resources contain specified prefix. |
| [GetCssContent](../../groupdocs.editor/editabledocument/getcsscontent#getcsscontent)() | Returns content of all external stylesheets as a list of strings, where one string represents one stylesheet. Returns empty list, if there is no CSS for this document. |
| [GetCssContent](../../groupdocs.editor/editabledocument/getcsscontent#getcsscontent_1)(string, string) | Returns content of all external stylesheets as a list of strings, where one string represents one stylesheet. Specified prefix will be applied to every link to the external resource in every resultant stylesheet. Returns empty list, if there is no CSS for this document. |
| [GetEmbeddedHtml](../../groupdocs.editor/editabledocument/getembeddedhtml)() | Returns all content of this HTML document with all related resources in a form of a single string, where all resources are embedded inside the HTML markup in a base64-encoded form. |
| [Save](../../groupdocs.editor/editabledocument/save#save)(string) | Saves this HTML document to the file on specified path, where HTML markup will be stored, and to the accompanying folder with resources. |
| [Save](../../groupdocs.editor/editabledocument/save#save_1)(string, string) | Saves this HTML document to the file on specified path, where HTML markup will be stored, and to the accompanying folder with resources, which is located on specified path. |

### Remarks

Instance of EditableDocument class can be produced by the '[`Edit`](../editor/edit)' method or created by the user himself using static factories. EditableDocument internally stores document in its own closed format, which is compatible (convertible) with all import and export formats, that GroupDocs.Editor supports. In order to make document editable in any WYSIWYG client-side editor (like CKEditor or TinyMCE), EditableDocument provides methods for generating HTML markup and producing resources, that can be accepted by the user.

### See Also

* interface [IAuxDisposable](../../groupdocs.editor.htmlcss.resources/iauxdisposable)
* namespace [GroupDocs.Editor](../../groupdocs.editor)
* assembly [GroupDocs.Editor](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Editor.dll -->