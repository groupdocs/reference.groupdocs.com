---
title: CustomImageSavingArgs class
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/customimagesavingargs/
is_root: false
weight: 30
---


## CustomImageSavingArgs class

Provides information and controls for saving a single image during document-to-Markdown conversion.

Use [`CustomImageSavingArgs.set_output_image_file_name`](/python-net/groupdocs.markdown/customimagesavingargs/set_output_image_file_name/) to change the file name the image is saved under, or [`CustomImageSavingArgs.set_output_stream`](/python-net/groupdocs.markdown/customimagesavingargs/set_output_stream/) to redirect the image data to a custom stream.

If neither method is called, the library uses the defaults provided by [`CustomImageSavingArgs.image_file_name`](/python-net/groupdocs.markdown/customimagesavingargs/image_file_name/) and [`CustomImageSavingArgs.output_directory`](/python-net/groupdocs.markdown/customimagesavingargs/output_directory/).

The CustomImageSavingArgs type exposes the following members:

### Methods
| Method | Description |
| :- | :- |
| [set_output_image_file_name](/python-net/groupdocs.markdown/customimagesavingargs/set_output_image_file_name/#file_name) | Overrides the default file name for this image. The image will be saved under the specified name instead of the library-generated [`CustomImageSavingArgs.image_file_name`](/python-net/groupdocs.markdown/customimagesavingargs/image_file_name/). |
| [set_output_stream](/python-net/groupdocs.markdown/customimagesavingargs/set_output_stream/#stream) | Redirects the image data to a custom writable stream instead of the default file output. |
| [set_replacement_image](/python-net/groupdocs.markdown/customimagesavingargs/set_replacement_image/#image_stream) | Provides a replacement image to use instead of the original image from the source document; the stream must contain the complete replacement image data (e.g., PNG or JPEG bytes), and the library writes this data to the output instead of the original image. |

### Properties
| Property | Description |
| :- | :- |
| [image_file_name](/python-net/groupdocs.markdown/customimagesavingargs/image_file_name/) | The default file name (without path) suggested by the library for this image. |
| [image_file_name_output](/python-net/groupdocs.markdown/customimagesavingargs/image_file_name_output/) | The overridden file name set by [`CustomImageSavingArgs.set_output_image_file_name`](/python-net/groupdocs.markdown/customimagesavingargs/set_output_image_file_name/), or `None` if no override was specified. |
| [output_directory](/python-net/groupdocs.markdown/customimagesavingargs/output_directory/) | The output directory where images are being saved. |
| [output_stream](/python-net/groupdocs.markdown/customimagesavingargs/output_stream/) | The custom output stream set by [`CustomImageSavingArgs.set_output_stream`](/python-net/groupdocs.markdown/customimagesavingargs/set_output_stream/), or `None` if no custom stream was specified. |
| [replacement_image_stream](/python-net/groupdocs.markdown/customimagesavingargs/replacement_image_stream/) | The replacement image stream set by [`CustomImageSavingArgs.set_replacement_image`](/python-net/groupdocs.markdown/customimagesavingargs/set_replacement_image/), or `None` if no replacement was specified. |
| [shape_type](/python-net/groupdocs.markdown/customimagesavingargs/shape_type/) | The type of the shape that contains the image in the source document (for example, "Picture" or "Shape"). |

### See Also
* module [`groupdocs.markdown`](/python-net/groupdocs.markdown/)
