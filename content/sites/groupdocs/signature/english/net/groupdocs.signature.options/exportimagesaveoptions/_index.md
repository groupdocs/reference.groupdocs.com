---
title: ExportImageSaveOptions
second_title: GroupDocs.Signature for .NET API Reference
description: Save options for exporting documents to image.
type: docs
weight: 1270
url: /net/groupdocs.signature.options/exportimagesaveoptions/
---
## ExportImageSaveOptions class

Save options for exporting documents to image.

```csharp
public class ExportImageSaveOptions : ImageSaveOptions
```

## Constructors

| Name | Description |
| --- | --- |
| [ExportImageSaveOptions](exportimagesaveoptions#constructor)() | Initializes a new instance of ExportAsImageSaveOptions class with default values. |
| [ExportImageSaveOptions](exportimagesaveoptions#constructor_1)(ImageSaveFileFormat) | Initializes a new instance of ExportAsImageSaveOptions class with specified file format. |

## Properties

| Name | Description |
| --- | --- |
| [AddMissingExtenstion](../../groupdocs.signature.options/saveoptions/addmissingextenstion) { get; set; } | Gets or sets flag to automatically add extension when it was missing in output file path Default value is false. |
| [Border](../../groupdocs.signature.options/exportimagesaveoptions/border) { get; set; } | Gets or sets the image border settings. By default this value is not set. |
| [ExportAllPages](../../groupdocs.signature.options/exportimagesaveoptions/exportallpages) { get; set; } | Flag to export each page. |
| [FileFormat](../../groupdocs.signature.options/imagesaveoptions/fileformat) { get; set; } | Gets or sets file format of signed document. |
| [OverwriteExistingFiles](../../groupdocs.signature.options/saveoptions/overwriteexistingfiles) { get; set; } | Gets or sets whether to overwrite existing file with new output file. Otherwise new file will be created with number as suffix. By default this value set to true that means file will be overwritten. |
| [PageColumns](../../groupdocs.signature.options/exportimagesaveoptions/pagecolumns) { get; set; } | Gets or sets number of columns for exported images. Use this property if you need put images in a row. |
| [PageNumber](../../groupdocs.signature.options/exportimagesaveoptions/pagenumber) { get; set; } | Gets or sets document page number for export. Minimal value is 1. |
| [PagesSetup](../../groupdocs.signature.options/exportimagesaveoptions/pagessetup) { get; set; } | Options to specify pages to be signed. |
| [Password](../../groupdocs.signature.options/saveoptions/password) { get; set; } | Gets or sets password to save signed document with password protection. This property is not supported for Image documents. |
| [TiffMultipage](../../groupdocs.signature.options/exportimagesaveoptions/tiffmultipage) { get; set; } | Put document pages on different frames in Tiff image. |
| [UseOriginalPassword](../../groupdocs.signature.options/saveoptions/useoriginalpassword) { get; set; } | Gets or sets whether to use password from LoadOptions to save signed document as protected. Default value is true. This property is not supported for Image documents. |

### See Also

* class [ImageSaveOptions](../imagesaveoptions)
* namespace [GroupDocs.Signature.Options](../../groupdocs.signature.options)
* assembly [GroupDocs.Signature](../../)

<!-- DO NOT EDIT: generated by xmldocmd for GroupDocs.Signature.dll -->