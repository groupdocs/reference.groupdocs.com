---
title: ExportImagesAsBase64Strategy class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/exportimagesasbase64strategy/
is_root: false
weight: 90
---


## ExportImagesAsBase64Strategy class

Implements an image export strategy that embeds images as Base64 strings directly in the Markdown.

This strategy converts all images to Base64 format and embeds them directly in the Markdown document using the data URI scheme. This eliminates the need for separate image files, making the Markdown document self-contained. However, this approach increases the size of the Markdown file and may not be supported by all Markdown viewers.

The ExportImagesAsBase64Strategy type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/python-net/groupdocs.markdown/exportimagesasbase64strategy/__init__/) |  |

### Methods
| Method | Description |
| :- | :- |
| [get_image_stream](/python-net/groupdocs.markdown/exportimagesasbase64strategy/get_image_stream/#context) | Returns None to indicate that the image should be embedded as Base64. |

### Properties
| Property | Description |
| :- | :- |
| [images_folder](/python-net/groupdocs.markdown/exportimagesasbase64strategy/images_folder/) | The images folder is an empty string because this strategy embeds images directly in the Markdown. |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
