---
title: SkipImagesStrategy class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/skipimagesstrategy/
is_root: false
weight: 210
---


## SkipImagesStrategy class

Implements an image export strategy that skips saving images during document conversion.

This strategy is useful when you want to convert a document to Markdown without saving the actual image files.
When this strategy is used, the output Markdown will still contain image references (e.g., ![](img-001.png)), but the actual image files will not be saved to disk.

The SkipImagesStrategy type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/python-net/groupdocs.markdown/skipimagesstrategy/__init__/) |  |

### Methods
| Method | Description |
| :- | :- |
| [get_image_stream](/python-net/groupdocs.markdown/skipimagesstrategy/get_image_stream/#context) | Returns None to indicate that the image should be skipped. |

### Properties
| Property | Description |
| :- | :- |
| [images_folder](/python-net/groupdocs.markdown/skipimagesstrategy/images_folder/) | The images folder path, which is an empty string because this strategy does not use an images folder. |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
