---
title: set_replacement_image method
second_title: GroupDocs.Markdown for Python via .NET API References
description: 
type: docs
url: /python-net/groupdocs.markdown/customimagesavingargs/set_replacement_image/
is_root: false
weight: 1030
---


## set_replacement_image {#image_stream}

Provides a replacement image to use instead of the original image from the source document; the stream must contain the complete replacement image data (e.g., PNG or JPEG bytes), and the library writes this data to the output instead of the original image.

```python
def set_replacement_image(self, image_stream):
    ...
```

| Parameter | Type | Description |
| :- | :- | :- |
| image_stream | `io.RawIOBase` | A readable stream containing the replacement image data. |

| Raises | Description |
| :- | :- |
| `ValueError` | Thrown when `image_stream` is None. |

### See Also
* class [`CustomImageSavingArgs`](/python-net/groupdocs.markdown/customimagesavingargs/)
