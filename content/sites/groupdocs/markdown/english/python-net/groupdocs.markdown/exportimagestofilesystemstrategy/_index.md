---
title: ExportImagesToFileSystemStrategy class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/exportimagestofilesystemstrategy/
is_root: false
weight: 100
---


## ExportImagesToFileSystemStrategy class

Saves images to a folder on disk during conversion.

By default, the Markdown output references images using the full [`ExportImagesToFileSystemStrategy.images_folder`](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/images_folder/) path. Set [`ExportImagesToFileSystemStrategy.images_relative_path`](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/images_relative_path/) to control the path that appears in the Markdown image links — typically a path relative to the output `.md` file.

The ExportImagesToFileSystemStrategy type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/__init__/#images_folder) | Initializes a new instance of the [`ExportImagesToFileSystemStrategy`](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/) class. |

### Methods
| Method | Description |
| :- | :- |
| [get_image_stream](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/get_image_stream/#context) | Returns a stream for writing the exported image to the file system. |

### Properties
| Property | Description |
| :- | :- |
| [images_folder](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/images_folder/) | The physical folder where images will be saved on disk. |
| [images_relative_path](/markdown/python-net/groupdocs.markdown/exportimagestofilesystemstrategy/images_relative_path/) | The path used in the Markdown image references. |

### See Also
* module [`groupdocs.markdown`](/markdown/python-net/groupdocs.markdown/)
