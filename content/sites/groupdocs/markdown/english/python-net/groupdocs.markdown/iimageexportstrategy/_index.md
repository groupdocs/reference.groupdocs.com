---
title: IImageExportStrategy class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /markdown/python-net/groupdocs.markdown/iimageexportstrategy/
is_root: false
weight: 140
---


## IImageExportStrategy class

Defines a strategy for handling image export during document-to-Markdown conversion.

The library ships with several built-in strategies:
- [`ExportImagesAsBase64Strategy`](/markdown/python-net/groupdocs.markdown/exportimagesasbase64strategy/) -- embeds images inline as Base64 (the default).
- [`ExportImagesToFileSystemStrategy`](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/) -- writes images to a folder on disk.
- [`SkipImagesStrategy`](/markdown/python-net/groupdocs.markdown/skipimagesstrategy/) -- omits images entirely.
- [`CustomImagesStrategy`](/markdown/python-net/groupdocs.markdown/customimagesstrategy/) -- delegates to a callback you supply.

Implement this interface directly when none of the built-in strategies meet your needs.

The IImageExportStrategy type exposes the following members:

### Methods
| Method | Description |
| :- | :- |
| [get_image_stream](/markdown/python-net/groupdocs.markdown/iimageexportstrategy/get_image_stream/#context) | Returns a writable stream for the image described by `context`. |

### Properties
| Property | Description |
| :- | :- |
| [images_folder](/markdown/python-net/groupdocs.markdown/iimageexportstrategy/images_folder/) | The folder path where exported images will be stored. |

### See Also
* module [`groupdocs.markdown`](/markdown/python-net/groupdocs.markdown/)
