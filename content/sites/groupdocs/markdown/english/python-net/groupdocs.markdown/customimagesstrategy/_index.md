---
title: CustomImagesStrategy class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/customimagesstrategy/
is_root: false
weight: 40
---


## CustomImagesStrategy class

Implements an image export strategy that gives you full control over how images are saved during conversion.

Supply an `IImageSavingHandler` implementation to rename images, redirect them to a custom stream, or apply any other custom logic when each image is encountered.

The CustomImagesStrategy type exposes the following members:

### Constructors
| Constructor | Description |
| :- | :- |
| [__init__](/python-net/groupdocs.markdown/customimagesstrategy/__init__/#images_folder-handler) | Initializes a new instance of the [`CustomImagesStrategy`](/python-net/groupdocs.markdown/customimagesstrategy/) class. |

### Methods
| Method | Description |
| :- | :- |
| [get_image_stream](/python-net/groupdocs.markdown/customimagesstrategy/get_image_stream/#context) | Gets a stream for writing the exported image to the file system. |

### Properties
| Property | Description |
| :- | :- |
| [images_folder](/python-net/groupdocs.markdown/customimagesstrategy/images_folder/) | The physical folder where images will be saved on disk. |
| [images_relative_path](/python-net/groupdocs.markdown/customimagesstrategy/images_relative_path/) | The path used in the Markdown image references. |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
